"""Deteccion de debilidades: champs con WR bajo, metricas bajo baseline, patrones."""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from ._helpers import find_participant, is_remake, safe_div


def detect_low_winrate_champs(
    champion_pool: list[dict[str, Any]],
    *,
    min_games: int = 5,
    wr_threshold: float = 0.40,
) -> list[dict[str, Any]]:
    """Champs con suficiente muestra y WR bajo el umbral."""
    return [
        r
        for r in champion_pool
        if r["games"] >= min_games and r["winrate"] < wr_threshold
    ]


def detect_high_winrate_champs(
    champion_pool: list[dict[str, Any]],
    *,
    min_games: int = 5,
    wr_threshold: float = 0.55,
) -> list[dict[str, Any]]:
    """Champs con muestra y WR alto: senal de fortaleza."""
    return [
        r
        for r in champion_pool
        if r["games"] >= min_games and r["winrate"] >= wr_threshold
    ]


def detect_metrics_below_baseline(
    playstyle: dict[str, Any],
    *,
    deficit_pct: float = 0.10,
) -> list[dict[str, Any]]:
    """Roles donde alguna metrica esta >=deficit_pct por debajo de su baseline."""
    out: list[dict[str, Any]] = []
    for row in playstyle.get("by_role", []):
        baseline = row.get("baseline") or {}
        deficits: list[dict[str, Any]] = []
        for metric in ("cs10", "cs15", "kp", "vspm", "dpm"):
            actual = row.get(metric)
            target = baseline.get(metric)
            if actual is None or target is None or target == 0:
                continue
            ratio = actual / target
            if ratio < (1.0 - deficit_pct):
                deficits.append(
                    {
                        "metric": metric,
                        "actual": actual,
                        "target": target,
                        "ratio": ratio,
                    }
                )
        if deficits:
            out.append(
                {
                    "role": row["role"],
                    "role_display": row["role_display"],
                    "sample_size": row["sample_size"],
                    "deficits": deficits,
                }
            )
    return out


def detect_loss_patterns(
    matches: list[dict[str, Any]],
    puuid: str,
) -> dict[str, Any]:
    """Patrones agregados separando wins vs losses (KDA, deaths, kp, etc.)."""
    agg = {
        "win": defaultdict(float),
        "loss": defaultdict(float),
        "win_n": 0,
        "loss_n": 0,
    }

    for match in matches:
        if is_remake(match):
            continue
        p = find_participant(match, puuid)
        if p is None:
            continue
        bucket_key = "win" if p.get("win") else "loss"
        agg[f"{bucket_key}_n"] += 1
        bucket = agg[bucket_key]
        bucket["kills"] += p.get("kills", 0)
        bucket["deaths"] += p.get("deaths", 0)
        bucket["assists"] += p.get("assists", 0)
        bucket["dmg"] += p.get("totalDamageDealtToChampions", 0)
        bucket["vision"] += p.get("visionScore", 0)
        bucket["dmg_taken"] += p.get("totalDamageTaken", 0)
        bucket["cc_score"] += p.get("timeCCingOthers", 0)
        bucket["gold"] += p.get("goldEarned", 0)
        team_id = p.get("teamId")
        team_kills = sum(
            q.get("kills", 0)
            for q in match.get("info", {}).get("participants", [])
            if q.get("teamId") == team_id
        )
        if team_kills:
            bucket["kp_acc"] += (p.get("kills", 0) + p.get("assists", 0)) / team_kills

    def _avg(side: str, key: str) -> float:
        n = agg[f"{side}_n"]
        return safe_div(agg[side][key], n)

    win_n, loss_n = agg["win_n"], agg["loss_n"]
    return {
        "wins": win_n,
        "losses": loss_n,
        "in_wins": {
            "deaths_avg": _avg("win", "deaths"),
            "kills_avg": _avg("win", "kills"),
            "assists_avg": _avg("win", "assists"),
            "kp_avg": _avg("win", "kp_acc"),
            "vision_avg": _avg("win", "vision"),
            "dmg_avg": _avg("win", "dmg"),
            "dmg_taken_avg": _avg("win", "dmg_taken"),
        },
        "in_losses": {
            "deaths_avg": _avg("loss", "deaths"),
            "kills_avg": _avg("loss", "kills"),
            "assists_avg": _avg("loss", "assists"),
            "kp_avg": _avg("loss", "kp_acc"),
            "vision_avg": _avg("loss", "vision"),
            "dmg_avg": _avg("loss", "dmg"),
            "dmg_taken_avg": _avg("loss", "dmg_taken"),
        },
    }


__all__ = [
    "detect_low_winrate_champs",
    "detect_high_winrate_champs",
    "detect_metrics_below_baseline",
    "detect_loss_patterns",
]
