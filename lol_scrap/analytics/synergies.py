"""Sinergias: duo partners por puuid y combos de champs aliados."""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from ._helpers import iter_player_games, safe_div


def compute_duo_partners(
    matches: list[dict[str, Any]],
    puuid: str,
    *,
    min_games: int = 5,
) -> list[dict[str, Any]]:
    """Aliados (por puuid) con los que se jugaron min_games o mas, ordenados por WR."""
    buckets: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "games": 0,
            "wins": 0,
            "name": "",
            "tag": "",
            "champions": defaultdict(int),
        }
    )

    for match, p in iter_player_games(matches, puuid):
        team_id = p.get("teamId")
        win = bool(p.get("win"))
        for ally in match.get("info", {}).get("participants", []):
            ally_puuid = ally.get("puuid")
            if not ally_puuid or ally_puuid == puuid:
                continue
            if ally.get("teamId") != team_id:
                continue
            b = buckets[ally_puuid]
            b["games"] += 1
            if win:
                b["wins"] += 1
            name = ally.get("riotIdGameName") or ally.get("summonerName") or ""
            tag = ally.get("riotIdTagline", "")
            if name:
                b["name"] = name
            if tag:
                b["tag"] = tag
            champ = ally.get("championName", "")
            if champ:
                b["champions"][champ] += 1

    rows: list[dict[str, Any]] = []
    for ally_puuid, b in buckets.items():
        games = b["games"]
        if games < min_games:
            continue
        top_champs = sorted(b["champions"].items(), key=lambda x: -x[1])[:3]
        display = b["name"]
        if b["tag"]:
            display = f"{display}#{b['tag']}" if display else f"???#{b['tag']}"
        rows.append(
            {
                "puuid": ally_puuid,
                "display_name": display or ally_puuid[:12] + "...",
                "games": games,
                "wins": b["wins"],
                "winrate": safe_div(b["wins"], games),
                "top_champs": [
                    {"champion": c, "games": n} for c, n in top_champs
                ],
            }
        )
    rows.sort(key=lambda r: (-r["winrate"], -r["games"]))
    return rows


def compute_champion_synergies(
    matches: list[dict[str, Any]],
    puuid: str,
    *,
    min_games: int = 5,
) -> list[dict[str, Any]]:
    """Pares (mi_champ, champ_aliado) con muestra suficiente, ordenados por WR."""
    buckets: dict[tuple[str, str], dict[str, int]] = defaultdict(
        lambda: {"games": 0, "wins": 0}
    )

    for match, p in iter_player_games(matches, puuid):
        my_champ = p.get("championName", "")
        team_id = p.get("teamId")
        win = bool(p.get("win"))
        for ally in match.get("info", {}).get("participants", []):
            if ally.get("puuid") == puuid:
                continue
            if ally.get("teamId") != team_id:
                continue
            ally_champ = ally.get("championName", "")
            if not my_champ or not ally_champ:
                continue
            key = (my_champ, ally_champ)
            buckets[key]["games"] += 1
            if win:
                buckets[key]["wins"] += 1

    rows: list[dict[str, Any]] = []
    for (my_champ, ally_champ), b in buckets.items():
        if b["games"] < min_games:
            continue
        rows.append(
            {
                "my_champion": my_champ,
                "ally_champion": ally_champ,
                "games": b["games"],
                "wins": b["wins"],
                "winrate": safe_div(b["wins"], b["games"]),
            }
        )
    rows.sort(key=lambda r: (-r["winrate"], -r["games"]))
    return rows


__all__ = ["compute_duo_partners", "compute_champion_synergies"]
