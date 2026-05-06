"""Orquesta la extraccion: riot_id -> puuid -> matchIds -> matches + timelines."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable

from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeRemainingColumn,
)

from .cache import MatchCache
from .config import QUEUE_NAMES
from .riot_client import RiotApiError, RiotClient


@dataclass
class PlayerData:
    """Bundle de todos los datos extraidos para un jugador."""

    riot_id: str
    puuid: str
    summoner: dict[str, Any]
    league_entries: list[dict[str, Any]]
    matches: list[dict[str, Any]] = field(default_factory=list)
    timelines: dict[str, dict[str, Any]] = field(default_factory=dict)

    @property
    def game_name(self) -> str:
        return self.riot_id.split("#", 1)[0]

    @property
    def tag_line(self) -> str:
        return self.riot_id.split("#", 1)[1] if "#" in self.riot_id else ""


def parse_riot_id(riot_id: str) -> tuple[str, str]:
    if "#" not in riot_id:
        raise ValueError(
            f"Riot ID invalido: {riot_id!r}. Formato esperado: 'Nombre#TAG' (ej. Faker#KR1)"
        )
    name, tag = riot_id.split("#", 1)
    name, tag = name.strip(), tag.strip()
    if not name or not tag:
        raise ValueError(f"Riot ID invalido: {riot_id!r}")
    return name, tag


def fetch_player_data(
    client: RiotClient,
    cache: MatchCache,
    riot_id: str,
    queues: Iterable[int],
    count: int,
    *,
    use_cache: bool = True,
    fetch_timeline: bool = True,
    console: Console | None = None,
) -> PlayerData:
    """Pipeline completo de extraccion."""
    console = console or Console()
    game_name, tag_line = parse_riot_id(riot_id)

    console.print(f"[bold cyan]Resolviendo[/] Riot ID [bold]{riot_id}[/]...")
    account = client.get_account_by_riot_id(game_name, tag_line)
    puuid = account["puuid"]
    canonical_id = f"{account.get('gameName', game_name)}#{account.get('tagLine', tag_line)}"
    console.print(f"  PUUID: [dim]{puuid[:16]}...[/]")

    try:
        summoner = client.get_summoner_by_puuid(puuid)
    except RiotApiError as exc:
        console.print(f"[yellow]Aviso:[/] no se pudo obtener summoner ({exc})")
        summoner = {}

    try:
        league_entries = client.get_league_entries_by_puuid(puuid)
    except RiotApiError as exc:
        console.print(f"[yellow]Aviso:[/] no se pudo obtener rank ({exc})")
        league_entries = []

    queues = list(queues)
    all_match_ids: list[str] = []
    seen: set[str] = set()
    for queue in queues:
        queue_name = QUEUE_NAMES.get(queue, f"queue {queue}")
        console.print(f"[bold cyan]Listando[/] match IDs de [bold]{queue_name}[/] (count={count})...")
        per_queue: list[str] = []
        start = 0
        remaining = count
        while remaining > 0:
            page = min(100, remaining)
            ids = client.get_match_ids(puuid, queue=queue, count=page, start=start)
            if not ids:
                break
            per_queue.extend(ids)
            if len(ids) < page:
                break
            start += page
            remaining -= page
        for mid in per_queue:
            if mid not in seen:
                seen.add(mid)
                all_match_ids.append(mid)
        console.print(f"  -> {len(per_queue)} ids ({queue_name})")

    console.print(f"[bold]Total[/] match IDs unicos: [bold]{len(all_match_ids)}[/]")

    matches: list[dict[str, Any]] = []
    timelines: dict[str, dict[str, Any]] = {}

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TimeRemainingColumn(),
        console=console,
        transient=False,
    ) as progress:
        task = progress.add_task("Descargando matches", total=len(all_match_ids))
        for match_id in all_match_ids:
            match_data: dict[str, Any] | None = None
            if use_cache:
                match_data = cache.get_match(match_id)
            if match_data is None:
                try:
                    match_data = client.get_match(match_id)
                    cache.set_match(match_id, match_data)
                except RiotApiError as exc:
                    progress.console.print(
                        f"  [yellow]skip match {match_id}: {exc}[/]"
                    )
                    progress.advance(task)
                    continue

            matches.append(match_data)

            if fetch_timeline:
                tl: dict[str, Any] | None = None
                if use_cache:
                    tl = cache.get_timeline(match_id)
                if tl is None:
                    try:
                        tl = client.get_match_timeline(match_id)
                        cache.set_timeline(match_id, tl)
                    except RiotApiError as exc:
                        progress.console.print(
                            f"  [yellow]skip timeline {match_id}: {exc}[/]"
                        )
                        tl = None
                if tl is not None:
                    timelines[match_id] = tl

            progress.advance(task)

    console.print(
        f"[bold green]OK[/] {len(matches)} matches y {len(timelines)} timelines listos."
    )

    return PlayerData(
        riot_id=canonical_id,
        puuid=puuid,
        summoner=summoner,
        league_entries=league_entries,
        matches=matches,
        timelines=timelines,
    )
