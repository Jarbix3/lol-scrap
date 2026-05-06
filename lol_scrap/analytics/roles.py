"""Distribucion y rendimiento por rol."""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from ..config import ROLE_DISPLAY
from ._helpers import cs, iter_player_games, normalized_role, safe_div


def compute_role_stats(
    matches: list[dict[str, Any]],
    puuid: str,
) -> list[dict[str, Any]]:
    """Devuelve stats por rol (TOP/JUNGLE/MIDDLE/BOTTOM/UTILITY)."""
    buckets: dict[str, dict[str, float]] = defaultdict(
        lambda: {
            "games": 0.0,
            "wins": 0.0,
            "kills": 0.0,
            "deaths": 0.0,
            "assists": 0.0,
            "cs": 0.0,
            "duration_s": 0.0,
            "dmg": 0.0,
            "vision": 0.0,
        }
    )

    for match, p in iter_player_games(matches, puuid):
        role = normalized_role(p) or ""
        b = buckets[role]
        b["games"] += 1
        b["wins"] += 1 if p.get("win") else 0
        b["kills"] += p.get("kills", 0)
        b["deaths"] += p.get("deaths", 0)
        b["assists"] += p.get("assists", 0)
        b["cs"] += cs(p)
        b["duration_s"] += match.get("info", {}).get("gameDuration", 0)
        b["dmg"] += p.get("totalDamageDealtToChampions", 0)
        b["vision"] += p.get("visionScore", 0)

    rows: list[dict[str, Any]] = []
    for role, b in buckets.items():
        games = int(b["games"])
        if games == 0:
            continue
        minutes = b["duration_s"] / 60.0 if b["duration_s"] else 0
        rows.append(
            {
                "role": role,
                "role_display": ROLE_DISPLAY.get(role, role or "?"),
                "games": games,
                "wins": int(b["wins"]),
                "winrate": safe_div(b["wins"], games),
                "kda": safe_div(b["kills"] + b["assists"], max(b["deaths"], 1)),
                "cs_per_min": safe_div(b["cs"], minutes),
                "dmg_per_min": safe_div(b["dmg"], minutes),
                "vision_avg": safe_div(b["vision"], games),
            }
        )

    rows.sort(key=lambda r: -r["games"])
    return rows


__all__ = ["compute_role_stats"]
