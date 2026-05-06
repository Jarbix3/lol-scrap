"""Helpers compartidos por los modulos de analytics."""
from __future__ import annotations

from typing import Any


def find_participant(match: dict[str, Any], puuid: str) -> dict[str, Any] | None:
    """Devuelve el dict del participant del jugador, o None si no esta."""
    info = match.get("info", {})
    for p in info.get("participants", []):
        if p.get("puuid") == puuid:
            return p
    return None


def is_remake(match: dict[str, Any]) -> bool:
    """Una partida es remake si dura menos de ~5 minutos (gameEndedInEarlySurrender)."""
    info = match.get("info", {})
    if info.get("gameDuration", 0) < 300:
        return True
    for p in info.get("participants", []):
        if p.get("gameEndedInEarlySurrender"):
            return True
    return False


def normalized_role(participant: dict[str, Any]) -> str:
    """Normaliza el rol usando teamPosition (mas confiable que individualPosition)."""
    role = participant.get("teamPosition") or participant.get("individualPosition") or ""
    if role in ("Invalid", "UTILITY", "TOP", "JUNGLE", "MIDDLE", "BOTTOM"):
        return "" if role == "Invalid" else role
    return ""


def kda(p: dict[str, Any]) -> float:
    k = p.get("kills", 0)
    a = p.get("assists", 0)
    d = max(p.get("deaths", 0), 1)
    return (k + a) / d


def cs(p: dict[str, Any]) -> int:
    return int(p.get("totalMinionsKilled", 0)) + int(p.get("neutralMinionsKilled", 0))


def team_total(match: dict[str, Any], team_id: int, key: str) -> float:
    info = match.get("info", {})
    return float(
        sum(
            p.get(key, 0)
            for p in info.get("participants", [])
            if p.get("teamId") == team_id
        )
    )


def safe_div(a: float, b: float) -> float:
    return a / b if b else 0.0


def iter_player_games(
    matches: list[dict[str, Any]],
    puuid: str,
    *,
    skip_remakes: bool = True,
):
    """Itera (match, participant) para el puuid dado."""
    for match in matches:
        if skip_remakes and is_remake(match):
            continue
        p = find_participant(match, puuid)
        if p is None:
            continue
        yield match, p
