"""CLI entrypoint para LoL Player Scraper."""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from lol_scrap.analytics._helpers import filter_matches_by_role
from lol_scrap.analytics.ally_champions import compute_ally_champions
from lol_scrap.analytics.champion_pool import (
    compute_champion_pool,
    summarize_overall,
)
from lol_scrap.analytics.derived_aggregations import compute_tier_a
from lol_scrap.analytics.derived_metrics import compute_tier_b, compute_tier_s
from lol_scrap.analytics.game_phases import compute_game_phases
from lol_scrap.analytics.matchups import compute_matchups
from lol_scrap.analytics.playstyle import compute_playstyle
from lol_scrap.analytics.role_advanced import compute_role_advanced
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
    ROLE_DISPLAY,
    available_ranks,
    load_baselines,
    normalize_platform,
    normalize_rank,
    normalize_role,
    rank_display,
    tier_from_league_entries,
)
from lol_scrap.fetcher import fetch_player_data, parse_riot_id
from lol_scrap.prompts import build_master_prompt
from lol_scrap.report import build_report
from lol_scrap.riot_client import RiotApiError, RiotClient


MIN_GAMES_PER_ROLE = 10


def _slugify(value: str) -> str:
    value = value.replace("#", "-")
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", value)
    return value.strip("_-") or "player"


def _build_role_report(
    player,
    role_filter: str | None,
    baselines: dict,
    rank_key: str,
    rank_source: str,
    rank_source_label: str,
    queues: list[int],
    count: int,
    global_overall: dict,
    global_role_stats: list[dict],
    console: Console,
) -> str:
    """Calcula analytics y devuelve el .md como string.

    Si `role_filter` es None genera un reporte global (sin sec. 6/6.1).
    Si `role_filter` es un canonical role, filtra al subset y agrega las
    secciones rol-especificas.
    """
    if role_filter is not None:
        effective_matches = filter_matches_by_role(
            player.matches, player.puuid, role_filter
        )
        if not effective_matches:
            role_label = ROLE_DISPLAY.get(role_filter, role_filter)
            console.print(
                f"[yellow]  Sin partidas como {role_label} ({role_filter}) "
                f"en la muestra.[/]"
            )
            return ""
        console.print(
            f"  Filtrando a rol "
            f"[bold]{ROLE_DISPLAY.get(role_filter, role_filter)}[/]: "
            f"{len(effective_matches)}/{len(player.matches)} partidas."
        )
    else:
        effective_matches = player.matches

    effective_timelines = {
        mid: tl
        for mid, tl in player.timelines.items()
        if any(
            (m.get("metadata", {}).get("matchId") == mid)
            for m in effective_matches
        )
    }

    overall = summarize_overall(effective_matches, player.puuid)
    champion_pool = compute_champion_pool(effective_matches, player.puuid)
    roles = compute_role_stats(effective_matches, player.puuid)
    playstyle = compute_playstyle(
        effective_matches, effective_timelines, player.puuid,
        baselines=baselines,
    )
    duo_partners = compute_duo_partners(effective_matches, player.puuid)
    champ_synergies = compute_champion_synergies(effective_matches, player.puuid)
    matchups = compute_matchups(effective_matches, player.puuid)
    ally_champions = compute_ally_champions(effective_matches, player.puuid)
    team_comps = compute_team_compositions(effective_matches, player.puuid)
    weaknesses = {
        "metric_deficits": detect_metrics_below_baseline(playstyle),
        "loss_patterns": detect_loss_patterns(effective_matches, player.puuid),
    }

    if role_filter:
        role_advanced_base = compute_role_advanced(
            effective_matches, player.puuid, role_filter
        )
        tier_s = compute_tier_s(
            effective_matches, player.puuid, role_filter
        )
        tier_b = compute_tier_b(
            effective_matches, effective_timelines, player.puuid, role_filter
        )
        role_advanced = role_advanced_base + tier_s + tier_b
        tier_a = compute_tier_a(
            effective_matches,
            player.puuid,
            role_filter,
            duo_partners=duo_partners,
        )
    else:
        role_advanced = None
        tier_a = None

    game_phases = compute_game_phases(
        effective_matches, effective_timelines, player.puuid,
        baselines=baselines,
    )

    return build_report(
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
        queues=queues,
        count=count,
        role_filter=role_filter,
        global_overall=global_overall if role_filter else None,
        global_role_stats=global_role_stats if role_filter else None,
        role_advanced=role_advanced,
        tier_a=tier_a,
        game_phases=game_phases,
        rank_key=rank_key,
        rank_source=rank_source,
        rank_source_label=rank_source_label,
    )


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
            "Con --role: ruta del .md de salida (default: "
            "reports/<riot-id>_<role>_<ts>.md). "
            "Sin --role: carpeta destino para el modo multi-rol "
            "(default: reports/<riot-id>/)."
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
    p.add_argument(
        "--role",
        default=None,
        help=(
            "Filtrar el analisis a un solo rol. "
            "Acepta alias (top, jungle/jng/jg, mid, bot/adc, sup) o canonical "
            "(TOP, JUNGLE, MIDDLE, BOTTOM, UTILITY). "
            f"Sin este flag se entra en MODO MULTI: genera un .md por cada "
            f"rol con >={MIN_GAMES_PER_ROLE} partidas + un GLOBAL.md, todos "
            f"en reports/<riot-id>/ (sobreescribe la version anterior)."
        ),
    )
    p.add_argument(
        "--rank",
        default=None,
        help=(
            "Rank/tier contra el cual comparar las metricas (define los "
            "baselines de las secciones 4 y 5). Sin este flag se intenta "
            "auto-detectar del Solo/Duo del jugador (fallback: Flex y luego "
            "'default'). Valores soportados: iron, bronze, silver, gold, "
            "platinum, emerald, diamond, master, grandmaster, challenger, "
            "default. Los valores se cargan desde data/baselines.json y son "
            "totalmente editables."
        ),
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

    role_filter: str | None = None
    if args.role is not None:
        try:
            role_filter = normalize_role(args.role)
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

    # === Resolver rank y cargar baselines ===
    rank_source: str  # "explicit", "auto" o "fallback"
    if args.rank is not None:
        rank_key = normalize_rank(args.rank)
        # Si el usuario pidio algo que cayo en fallback, avisar.
        if rank_key == "default" and args.rank.strip().lower() not in (
            "default",
            "",
        ):
            console.print(
                f"[yellow]Rank '{args.rank}' no reconocido — usando "
                f"baselines 'default'.[/] Disponibles: "
                f"{', '.join(available_ranks())}, master, grandmaster, "
                f"challenger."
            )
        rank_source = "explicit"
        rank_source_label = f"--rank {args.rank}"
    else:
        detected_tier, detected_queue = tier_from_league_entries(
            player.league_entries
        )
        if detected_tier is not None:
            rank_key = normalize_rank(detected_tier)
            rank_source = "auto"
            rank_source_label = (
                f"auto-detectado del {detected_queue} del jugador "
                f"({detected_tier.upper()})"
            )
        else:
            rank_key = normalize_rank(None)
            rank_source = "fallback"
            rank_source_label = (
                "fallback (sin rank en league_entries; usá --rank para forzar)"
            )

    baselines = load_baselines(rank_key)
    console.print(
        f"[bold cyan]Baselines:[/] comparado vs "
        f"[bold]{rank_display(rank_key)}[/] ({rank_source_label})."
    )

    global_overall = summarize_overall(player.matches, player.puuid)
    global_role_stats = compute_role_stats(player.matches, player.puuid)

    common_kwargs = dict(
        player=player,
        baselines=baselines,
        rank_key=rank_key,
        rank_source=rank_source,
        rank_source_label=rank_source_label,
        queues=args.queues,
        count=args.count,
        global_overall=global_overall,
        global_role_stats=global_role_stats,
        console=console,
    )

    # === Modo single (con --role) ===
    if role_filter is not None:
        console.print("[bold cyan]Calculando analytics...[/]")
        md = _build_role_report(role_filter=role_filter, **common_kwargs)
        if not md:
            console.print(
                f"[yellow]Sin partidas como "
                f"{ROLE_DISPLAY.get(role_filter, role_filter)} en la "
                f"muestra.[/] Probá con otro rol o aumentá --count."
            )
            return 1
        if args.out:
            out_path = Path(args.out)
        else:
            from datetime import datetime, timezone

            ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
            out_path = (
                Path("reports")
                / f"{_slugify(player.riot_id)}_{role_filter}_{ts}.md"
            )
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
        console.print(f"[bold green]Reporte escrito:[/] {out_path}")
        console.print(
            "[dim]Abrílo en Cursor y pedile al chat las conclusiones tipo "
            "coach (prompt sugerido al final del .md).[/]"
        )
        return 0

    # === Modo multi (sin --role): un .md por rol con >=N partidas + GLOBAL ===
    if args.out:
        player_dir = Path(args.out)
    else:
        player_dir = Path("reports") / _slugify(player.riot_id)
    player_dir.mkdir(parents=True, exist_ok=True)

    roles_eligible = [
        r["role"]
        for r in global_role_stats
        if r["games"] >= MIN_GAMES_PER_ROLE and r["role"]
    ]

    console.print(
        f"[bold cyan]Modo multi-rol[/]: generando reportes en "
        f"[bold]{player_dir}/[/] (threshold: "
        f"≥{MIN_GAMES_PER_ROLE} partidas por rol)."
    )
    skipped = [
        f"{r['role_display']} ({r['games']}g)"
        for r in global_role_stats
        if r["role"] and r["games"] < MIN_GAMES_PER_ROLE
    ]
    if skipped:
        console.print(
            f"[dim]  Skipeados por debajo del threshold: "
            f"{', '.join(skipped)}.[/]"
        )

    written: list[Path] = []
    for role in roles_eligible:
        role_label = ROLE_DISPLAY.get(role, role)
        console.print(
            f"[bold cyan]>>>[/] Reporte [bold]{role_label}[/] ({role})..."
        )
        md = _build_role_report(role_filter=role, **common_kwargs)
        if not md:
            continue
        out_path = player_dir / f"{role}.md"
        out_path.write_text(md, encoding="utf-8")
        written.append(out_path)
        console.print(f"[bold green]    Escrito:[/] {out_path}")

    console.print("[bold cyan]>>>[/] Reporte [bold]GLOBAL[/] (sin filtro)...")
    md_global = _build_role_report(role_filter=None, **common_kwargs)
    out_global = player_dir / "GLOBAL.md"
    out_global.write_text(md_global, encoding="utf-8")
    written.append(out_global)
    console.print(f"[bold green]    Escrito:[/] {out_global}")

    # === Meta-prompt 360 ===
    from datetime import datetime, timezone

    role_label_lookup = {r["role"]: r["role_display"] for r in global_role_stats}
    games_lookup = {r["role"]: r["games"] for r in global_role_stats}
    roles_with_md = [
        (
            role,
            role_label_lookup.get(role, role),
            games_lookup.get(role, 0),
        )
        for role in roles_eligible
    ]
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    try:
        player_dir_relpath = str(player_dir.relative_to(Path.cwd()))
    except ValueError:
        player_dir_relpath = str(player_dir)
    master_prompt = build_master_prompt(
        player_riot_id=player.riot_id,
        player_dir_relpath=player_dir_relpath,
        roles_with_md=roles_with_md,
        has_global=True,
        generated_at=generated_at,
    )
    out_prompt = player_dir / "_COACH_PROMPT.md"
    out_prompt.write_text(master_prompt, encoding="utf-8")
    written.append(out_prompt)
    console.print(
        f"[bold magenta]    Meta-prompt 360°:[/] {out_prompt}"
    )

    console.print(
        f"\n[bold green]✓ {len(written)} archivos escritos en[/] "
        f"[bold]{player_dir}/[/]"
    )
    console.print(
        "[dim]Para el análisis 360° automático: abrí "
        f"`{out_prompt}` en Cursor, copiá su contenido al chat, y el LLM "
        f"generará `{player_dir_relpath}/COACH_ANALYSIS.md` con las "
        f"{len(roles_with_md) + 1} secciones (overview cross-role + una "
        "por cada rol).[/]"
    )
    console.print(
        "[dim]Alternativa manual: abrí cada .md de rol y pedí el coach "
        "rol-específico (prompt sugerido al final de cada .md).[/]"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
