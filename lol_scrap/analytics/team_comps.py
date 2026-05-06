"""Composiciones de equipo: drafts de 5 campeones aliados repetidos >=N veces."""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from ._helpers import iter_player_games, safe_div


def compute_team_compositions(
    matches: list[dict[str, Any]],
    puuid: str,
    *,
    min_games: int = 4,
    top_n: int = 5,
) -> dict[str, Any]:
    """Agrupa partidas por composicion exacta del equipo aliado (5 campeones).

    Devuelve dict con:
      - `all`: lista de comps con games >= min_games, ordenada por WR desc
      - `best`: top N comps con mejor WR
      - `worst`: top N comps con peor WR
      - `total_unique`: cuantas comps distintas hubo en total (para diagnostico)

    La clave es la tupla ORDENADA de los 5 nombres de campeon (incluyendo el mio).
    Asi dos partidas con la misma comp "matchean" sin importar el orden en que
    Riot devuelve los participants.
    """
    buckets: dict[tuple[str, ...], dict[str, float]] = defaultdict(
        lambda: {"games": 0.0, "wins": 0.0}
    )
    total_unique = 0

    for match, p in iter_player_games(matches, puuid):
        team_id = p.get("teamId")
        team_champs = [
            ally.get("championName", "")
            for ally in match.get("info", {}).get("participants", [])
            if ally.get("teamId") == team_id
        ]
        team_champs = [c for c in team_champs if c]
        if len(team_champs) != 5:
            continue
        key = tuple(sorted(team_champs))
        if buckets[key]["games"] == 0:
            total_unique += 1
        b = buckets[key]
        b["games"] += 1
        if p.get("win"):
            b["wins"] += 1

    rows: list[dict[str, Any]] = []
    for comp, b in buckets.items():
        games = int(b["games"])
        if games < min_games:
            continue
        rows.append(
            {
                "champions": list(comp),
                "games": games,
                "wins": int(b["wins"]),
                "losses": games - int(b["wins"]),
                "winrate": safe_div(b["wins"], games),
            }
        )

    rows.sort(key=lambda r: (-r["winrate"], -r["games"]))
    best = rows[:top_n]
    worst = sorted(rows, key=lambda r: (r["winrate"], -r["games"]))[:top_n]
    return {
        "all": rows,
        "best": best,
        "worst": worst,
        "total_unique": total_unique,
        "min_games": min_games,
    }


__all__ = ["compute_team_compositions"]
