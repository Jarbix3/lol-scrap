"""Stats agregados por campeon: games, WR, KDA, dmg share, gold share."""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from ._helpers import cs, iter_player_games, kda, safe_div, team_total


def compute_champion_pool(
    matches: list[dict[str, Any]],
    puuid: str,
) -> list[dict[str, Any]]:
    """Devuelve lista ordenada (desc por games) con stats por campeon."""
    buckets: dict[str, dict[str, float]] = defaultdict(
        lambda: {
            "games": 0.0,
            "wins": 0.0,
            "kills": 0.0,
            "deaths": 0.0,
            "assists": 0.0,
            "cs": 0.0,
            "duration_s": 0.0,
            "dmg_to_champs": 0.0,
            "team_dmg_to_champs": 0.0,
            "gold": 0.0,
            "team_gold": 0.0,
            "vision_score": 0.0,
        }
    )

    for match, p in iter_player_games(matches, puuid):
        champ = p.get("championName", "Unknown")
        b = buckets[champ]
        b["games"] += 1
        b["wins"] += 1 if p.get("win") else 0
        b["kills"] += p.get("kills", 0)
        b["deaths"] += p.get("deaths", 0)
        b["assists"] += p.get("assists", 0)
        b["cs"] += cs(p)
        duration = match.get("info", {}).get("gameDuration", 0)
        b["duration_s"] += duration
        dmg = p.get("totalDamageDealtToChampions", 0)
        b["dmg_to_champs"] += dmg
        team_id = p.get("teamId")
        team_dmg = team_total(match, team_id, "totalDamageDealtToChampions")
        b["team_dmg_to_champs"] += team_dmg
        gold = p.get("goldEarned", 0)
        b["gold"] += gold
        team_gold = team_total(match, team_id, "goldEarned")
        b["team_gold"] += team_gold
        b["vision_score"] += p.get("visionScore", 0)

    rows: list[dict[str, Any]] = []
    for champ, b in buckets.items():
        games = int(b["games"])
        if games == 0:
            continue
        minutes = b["duration_s"] / 60.0 if b["duration_s"] else 0
        rows.append(
            {
                "champion": champ,
                "games": games,
                "wins": int(b["wins"]),
                "losses": games - int(b["wins"]),
                "winrate": safe_div(b["wins"], games),
                "kda": safe_div(b["kills"] + b["assists"], max(b["deaths"], 1)),
                "kills_avg": safe_div(b["kills"], games),
                "deaths_avg": safe_div(b["deaths"], games),
                "assists_avg": safe_div(b["assists"], games),
                "cs_per_min": safe_div(b["cs"], minutes),
                "dmg_per_min": safe_div(b["dmg_to_champs"], minutes),
                "dmg_share": safe_div(b["dmg_to_champs"], b["team_dmg_to_champs"]),
                "gold_share": safe_div(b["gold"], b["team_gold"]),
                "vision_avg": safe_div(b["vision_score"], games),
            }
        )

    rows.sort(key=lambda r: (-r["games"], -r["winrate"]))
    return rows


def summarize_overall(
    matches: list[dict[str, Any]],
    puuid: str,
) -> dict[str, Any]:
    """Resumen global: total games, WR, KDA, etc."""
    games = 0
    wins = 0
    kills = deaths = assists = 0
    duration_s = 0
    cs_total = 0
    dmg = 0
    vision = 0

    for match, p in iter_player_games(matches, puuid):
        games += 1
        if p.get("win"):
            wins += 1
        kills += p.get("kills", 0)
        deaths += p.get("deaths", 0)
        assists += p.get("assists", 0)
        duration_s += match.get("info", {}).get("gameDuration", 0)
        cs_total += cs(p)
        dmg += p.get("totalDamageDealtToChampions", 0)
        vision += p.get("visionScore", 0)

    minutes = duration_s / 60.0 if duration_s else 0
    return {
        "games": games,
        "wins": wins,
        "losses": games - wins,
        "winrate": safe_div(wins, games),
        "kda": safe_div(kills + assists, max(deaths, 1)),
        "kills_avg": safe_div(kills, games),
        "deaths_avg": safe_div(deaths, games),
        "assists_avg": safe_div(assists, games),
        "cs_per_min": safe_div(cs_total, minutes),
        "dmg_per_min": safe_div(dmg, minutes),
        "vision_avg": safe_div(vision, games),
        "minutes_played": minutes,
    }


__all__ = ["compute_champion_pool", "summarize_overall", "kda"]
