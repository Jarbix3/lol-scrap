"""CLI entrypoint para LoL Player Scraper."""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from lol_scrap.analytics.ally_champions import compute_ally_champions
from lol_scrap.analytics.champion_pool import (
    compute_champion_pool,
    summarize_overall,
)
from lol_scrap.analytics.matchups import compute_matchups
from lol_scrap.analytics.playstyle import compute_playstyle
from lol_scrap.analytics.roles import compute_role_stats
from lol_scrap.analytics.synergies import (
    compute_champion_synergies,
    compute_duo_partners,
)
from lol_scrap.analytics.team_comps import compute_team_compositions
from lol_scrap.analytics.weaknesses import (
    detect_loss_patterns,
    detect_metrics_below_baseline,
)
from lol_scrap.cache import MatchCache
from lol_scrap.config import (
    DEFAULT_MATCH_COUNT,
    DEFAULT_QUEUES,
    normalize_platform,
)
from lol_scrap.fetcher import fetch_player_data, parse_riot_id
from lol_scrap.report import build_report
from lol_scrap.riot_client import RiotApiError, RiotClient


def _slugify(value: str) -> str:
    value = value.replace("#", "-")
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", value)
    return value.strip("_-") or "player"


def _parse_queues(raw: str) -> list[int]:
    out: list[int] = []
    for chunk in raw.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        try:
            out.append(int(chunk))
        except ValueError as exc:
            raise argparse.ArgumentTypeError(
                f"Cola invalida: {chunk!r} (debe ser entero, ej. 420)"
            ) from exc
    if not out:
        raise argparse.ArgumentTypeError("Lista de colas vacia")
    return out


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="lol-scrap",
        description=(
            "Scrapea el historial de un jugador de LoL via Riot API y "
            "genera un reporte Markdown analitico (Solo/Flex por defecto)."
        ),
    )
    p.add_argument(
        "riot_id",
        help="Riot ID del jugador en formato Nombre#TAG (ej. Faker#KR1)",
    )
    p.add_argument(
        "--region",
        required=True,
        help=(
            "Region/plataforma. Acepta alias (las, lan, br, na, euw, eune, "
            "kr, jp, oce) o platform IDs (la2, la1, br1, na1, euw1, kr...)."
        ),
    )
    p.add_argument(
        "--queues",
        type=_parse_queues,
        default=list(DEFAULT_QUEUES),
        help=(
            f"Colas separadas por coma. Default: "
            f"{','.join(str(q) for q in DEFAULT_QUEUES)} "
            f"(420=Solo/Duo, 440=Flex)."
        ),
    )
    p.add_argument(
        "--count",
        type=int,
        default=DEFAULT_MATCH_COUNT,
        help=f"Partidas a pedir POR cola. Default: {DEFAULT_MATCH_COUNT}.",
    )
    p.add_argument(
        "--out",
        default=None,
        help=(
            "Ruta del .md de salida. "
            "Default: reports/<riot-id>_<timestamp>.md"
        ),
    )
    p.add_argument(
        "--no-cache",
        action="store_true",
        help="Ignora el cache local y refetchea todo.",
    )
    p.add_argument(
        "--no-timeline",
        action="store_true",
        help="Saltea timelines (mas rapido pero sin metricas @10/@15).",
    )
    p.add_argument(
        "--cache-dir",
        default="cache",
        help="Directorio de cache. Default: ./cache",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    console = Console()

    load_dotenv()
    api_key = os.environ.get("RIOT_API_KEY", "").strip()
    if not api_key:
        console.print(
            "[red]Falta RIOT_API_KEY.[/] "
            "Copiá .env.example a .env y poné tu key de "
            "https://developer.riotgames.com"
        )
        return 2

    try:
        platform = normalize_platform(args.region)
    except ValueError as exc:
        console.print(f"[red]{exc}[/]")
        return 2

    try:
        parse_riot_id(args.riot_id)
    except ValueError as exc:
        console.print(f"[red]{exc}[/]")
        return 2

    client = RiotClient(api_key=api_key, platform=platform)
    cache = MatchCache(args.cache_dir)

    try:
        player = fetch_player_data(
            client,
            cache,
            args.riot_id,
            queues=args.queues,
            count=args.count,
            use_cache=not args.no_cache,
            fetch_timeline=not args.no_timeline,
            console=console,
        )
    except RiotApiError as exc:
        console.print(f"[red]Error de Riot API:[/] {exc}")
        return 1

    if not player.matches:
        console.print(
            "[yellow]Sin partidas para analizar.[/] "
            "Probá con otra cola o aumentá --count."
        )
        return 1

    console.print("[bold cyan]Calculando analytics...[/]")
    overall = summarize_overall(player.matches, player.puuid)
    champion_pool = compute_champion_pool(player.matches, player.puuid)
    roles = compute_role_stats(player.matches, player.puuid)
    playstyle = compute_playstyle(
        player.matches, player.timelines, player.puuid
    )
    duo_partners = compute_duo_partners(player.matches, player.puuid)
    champ_synergies = compute_champion_synergies(player.matches, player.puuid)
    matchups = compute_matchups(player.matches, player.puuid)
    ally_champions = compute_ally_champions(player.matches, player.puuid)
    team_comps = compute_team_compositions(player.matches, player.puuid)
    weaknesses = {
        "metric_deficits": detect_metrics_below_baseline(playstyle),
        "loss_patterns": detect_loss_patterns(player.matches, player.puuid),
    }

    md = build_report(
        player=player,
        overall=overall,
        champion_pool=champion_pool,
        roles=roles,
        playstyle=playstyle,
        duo_partners=duo_partners,
        champion_synergies=champ_synergies,
        matchups=matchups,
        ally_champions=ally_champions,
        team_comps=team_comps,
        weaknesses=weaknesses,
        queues=args.queues,
        count=args.count,
    )

    if args.out:
        out_path = Path(args.out)
    else:
        from datetime import datetime, timezone

        ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        out_path = Path("reports") / f"{_slugify(player.riot_id)}_{ts}.md"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")
    console.print(f"[bold green]Reporte escrito:[/] {out_path}")
    console.print(
        "[dim]Abrílo en Cursor y pedile al chat las conclusiones tipo coach "
        "(prompt sugerido al final del .md).[/]"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
