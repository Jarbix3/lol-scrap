"""Wrapper de Riot API con rate-limiting (token bucket) y retries."""
from __future__ import annotations

import threading
import time
from collections import deque
from typing import Any

import requests

from .config import regional_for


class RateLimiter:
    """Limita por dos ventanas en simultaneo: corta (20/1s) y larga (100/120s).

    Implementacion simple con deques de timestamps. Antes de cada request,
    espera lo necesario para no exceder ninguna de las dos ventanas.
    """

    def __init__(
        self,
        short_limit: int = 20,
        short_window: float = 1.0,
        long_limit: int = 100,
        long_window: float = 120.0,
    ) -> None:
        self.short_limit = short_limit
        self.short_window = short_window
        self.long_limit = long_limit
        self.long_window = long_window
        self._short: deque[float] = deque()
        self._long: deque[float] = deque()
        self._lock = threading.Lock()

    def _trim(self, now: float) -> None:
        while self._short and now - self._short[0] >= self.short_window:
            self._short.popleft()
        while self._long and now - self._long[0] >= self.long_window:
            self._long.popleft()

    def acquire(self) -> None:
        while True:
            with self._lock:
                now = time.monotonic()
                self._trim(now)
                wait_short = (
                    self.short_window - (now - self._short[0])
                    if len(self._short) >= self.short_limit
                    else 0.0
                )
                wait_long = (
                    self.long_window - (now - self._long[0])
                    if len(self._long) >= self.long_limit
                    else 0.0
                )
                wait = max(wait_short, wait_long)
                if wait <= 0:
                    self._short.append(now)
                    self._long.append(now)
                    return
            time.sleep(wait + 0.01)


class RiotApiError(Exception):
    def __init__(self, status_code: int, message: str, url: str) -> None:
        super().__init__(f"[{status_code}] {message} ({url})")
        self.status_code = status_code
        self.url = url


class RiotClient:
    """Cliente HTTP para Riot Games API."""

    def __init__(
        self,
        api_key: str,
        platform: str,
        timeout: float = 15.0,
        max_retries: int = 5,
        rate_limiter: RateLimiter | None = None,
    ) -> None:
        if not api_key:
            raise ValueError("RIOT_API_KEY vacio. Configuralo en .env")
        self.api_key = api_key
        self.platform = platform
        self.regional = regional_for(platform)
        self.timeout = timeout
        self.max_retries = max_retries
        self.rate_limiter = rate_limiter or RateLimiter()

        self._session = requests.Session()
        self._session.headers.update(
            {
                "X-Riot-Token": self.api_key,
                "Accept": "application/json",
                "User-Agent": "lol-scrap/0.1 (+local)",
            }
        )

    def _build_url(self, host_kind: str, path: str) -> str:
        host = self.regional if host_kind == "regional" else self.platform
        return f"https://{host}.api.riotgames.com{path}"

    def _request(
        self,
        host_kind: str,
        path: str,
        params: dict[str, Any] | None = None,
    ) -> Any:
        url = self._build_url(host_kind, path)
        last_exc: Exception | None = None

        for attempt in range(self.max_retries + 1):
            self.rate_limiter.acquire()
            try:
                resp = self._session.get(url, params=params, timeout=self.timeout)
            except requests.RequestException as exc:
                last_exc = exc
                wait = min(2 ** attempt, 30)
                time.sleep(wait)
                continue

            if resp.status_code == 200:
                return resp.json()

            if resp.status_code == 404:
                raise RiotApiError(404, "Recurso no encontrado", resp.url)

            if resp.status_code == 401 or resp.status_code == 403:
                raise RiotApiError(
                    resp.status_code,
                    "API key invalida o expirada (renovala en developer.riotgames.com)",
                    resp.url,
                )

            if resp.status_code == 429:
                retry_after = float(resp.headers.get("Retry-After", "1"))
                time.sleep(retry_after + 0.1)
                continue

            if 500 <= resp.status_code < 600:
                wait = min(2 ** attempt, 30)
                time.sleep(wait)
                continue

            raise RiotApiError(resp.status_code, resp.text[:200], resp.url)

        if last_exc is not None:
            raise RiotApiError(0, f"Network error: {last_exc}", url)
        raise RiotApiError(0, "Max retries exceeded", url)

    def get_account_by_riot_id(self, game_name: str, tag_line: str) -> dict[str, Any]:
        path = f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        return self._request("regional", path)

    def get_summoner_by_puuid(self, puuid: str) -> dict[str, Any]:
        path = f"/lol/summoner/v4/summoners/by-puuid/{puuid}"
        return self._request("platform", path)

    def get_league_entries_by_puuid(self, puuid: str) -> list[dict[str, Any]]:
        path = f"/lol/league/v4/entries/by-puuid/{puuid}"
        return self._request("platform", path)

    def get_match_ids(
        self,
        puuid: str,
        queue: int | None = None,
        count: int = 20,
        start: int = 0,
    ) -> list[str]:
        path = f"/lol/match/v5/matches/by-puuid/{puuid}/ids"
        params: dict[str, Any] = {"count": count, "start": start}
        if queue is not None:
            params["queue"] = queue
        return self._request("regional", path, params=params)

    def get_match(self, match_id: str) -> dict[str, Any]:
        path = f"/lol/match/v5/matches/{match_id}"
        return self._request("regional", path)

    def get_match_timeline(self, match_id: str) -> dict[str, Any]:
        path = f"/lol/match/v5/matches/{match_id}/timeline"
        return self._request("regional", path)
