"""Matchups: WR y stats contra el oponente directo del mismo rol."""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from ._helpers import cs, iter_player_games, normalized_role, safe_div


def compute_matchups(
    matches: list[dict[str, Any]],
    puuid: str,
    *,
    min_games: int = 3,
    top_n: int = 5,
) -> dict[str, Any]:
    """Por cada (mi_champ vs oponente_champ) en el mismo rol, calcula WR + stats.

    Devuelve dict con:
      - `all`: todos los matchups con muestra >= min_games, ordenados por WR desc
      - `best`: top N por mayor WR (sin umbral fijo, solo respeta min_games)
      - `worst`: top N por menor WR
    """
    buckets: dict[tuple[str, str], dict[str, float]] = defaultdict(
        lambda: {
            "games": 0.0,
            "wins": 0.0,
            "kills": 0.0,
            "deaths": 0.0,
            "assists": 0.0,
            "dmg": 0.0,
            "duration_s": 0.0,
            "cs": 0.0,
            "gold": 0.0,
        }
    )

    for match, p in iter_player_games(matches, puuid):
        role = normalized_role(p)
        if not role:
            continue
        my_team = p.get("teamId")
        my_champ = p.get("championName", "")
        opp = None
        for q in match.get("info", {}).get("participants", []):
            if q.get("teamId") == my_team:
                continue
            if normalized_role(q) == role:
                opp = q
                break
        if opp is None or not my_champ:
            continue
        opp_champ = opp.get("championName", "")
        if not opp_champ:
            continue
        key = (my_champ, opp_champ)
        b = buckets[key]
        b["games"] += 1
        if p.get("win"):
            b["wins"] += 1
        b["kills"] += p.get("kills", 0)
        b["deaths"] += p.get("deaths", 0)
        b["assists"] += p.get("assists", 0)
        b["dmg"] += p.get("totalDamageDealtToChampions", 0)
        b["duration_s"] += match.get("info", {}).get("gameDuration", 0)
        b["cs"] += cs(p)
        b["gold"] += p.get("goldEarned", 0)

    rows: list[dict[str, Any]] = []
    for (my_champ, opp_champ), b in buckets.items():
        games = int(b["games"])
        if games < min_games:
            continue
        minutes = b["duration_s"] / 60.0 if b["duration_s"] else 0
        rows.append(
            {
                "my_champion": my_champ,
                "opponent": opp_champ,
                "games": games,
                "wins": int(b["wins"]),
                "losses": games - int(b["wins"]),
                "winrate": safe_div(b["wins"], games),
                "kda": safe_div(b["kills"] + b["assists"], max(b["deaths"], 1)),
                "kills_avg": safe_div(b["kills"], games),
                "deaths_avg": safe_div(b["deaths"], games),
                "assists_avg": safe_div(b["assists"], games),
                "dpm": safe_div(b["dmg"], minutes),
                "cs_per_min": safe_div(b["cs"], minutes),
                "gold_per_min": safe_div(b["gold"], minutes),
            }
        )

    rows.sort(key=lambda r: (-r["winrate"], -r["games"]))
    best = rows[:top_n]
    worst = sorted(rows, key=lambda r: (r["winrate"], -r["games"]))[:top_n]
    return {"all": rows, "best": best, "worst": worst}


__all__ = ["compute_matchups"]
