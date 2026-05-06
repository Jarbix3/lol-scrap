"""Stats por campeon aliado (excluyendo el mio): cuando aparece X en mi equipo, gano?"""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from ._helpers import iter_player_games, safe_div


def compute_ally_champions(
    matches: list[dict[str, Any]],
    puuid: str,
    *,
    min_games: int = 5,
    top_n: int = 5,
) -> dict[str, Any]:
    """Para cada campeon aliado (no el mio), agrega games/WR/KDA del jugador.

    Devuelve:
      - `all`: lista ordenada por WR desc (con games >= min_games)
      - `best`: top N (mejor WR cuando ese aliado esta en mi equipo)
      - `worst`: top N (peor WR cuando ese aliado esta en mi equipo)

    Nota: cada match aporta hasta 4 entradas (los 4 aliados que no soy yo).
    El KDA registrado es el MIO en esas partidas, no el del aliado.
    """
    buckets: dict[str, dict[str, float]] = defaultdict(
        lambda: {
            "games": 0.0,
            "wins": 0.0,
            "kills": 0.0,
            "deaths": 0.0,
            "assists": 0.0,
        }
    )

    for match, p in iter_player_games(matches, puuid):
        team_id = p.get("teamId")
        win = bool(p.get("win"))
        my_kills = p.get("kills", 0)
        my_deaths = p.get("deaths", 0)
        my_assists = p.get("assists", 0)
        for ally in match.get("info", {}).get("participants", []):
            if ally.get("puuid") == puuid:
                continue
            if ally.get("teamId") != team_id:
                continue
            champ = ally.get("championName", "")
            if not champ:
                continue
            b = buckets[champ]
            b["games"] += 1
            if win:
                b["wins"] += 1
            b["kills"] += my_kills
            b["deaths"] += my_deaths
            b["assists"] += my_assists

    rows: list[dict[str, Any]] = []
    for champ, b in buckets.items():
        games = int(b["games"])
        if games < min_games:
            continue
        rows.append(
            {
                "ally_champion": champ,
                "games": games,
                "wins": int(b["wins"]),
                "losses": games - int(b["wins"]),
                "winrate": safe_div(b["wins"], games),
                "my_kda": safe_div(
                    b["kills"] + b["assists"], max(b["deaths"], 1)
                ),
                "my_kills_avg": safe_div(b["kills"], games),
                "my_deaths_avg": safe_div(b["deaths"], games),
                "my_assists_avg": safe_div(b["assists"], games),
            }
        )

    rows.sort(key=lambda r: (-r["winrate"], -r["games"]))
    best = rows[:top_n]
    worst = sorted(rows, key=lambda r: (r["winrate"], -r["games"]))[:top_n]
    return {"all": rows, "best": best, "worst": worst}


__all__ = ["compute_ally_champions"]
