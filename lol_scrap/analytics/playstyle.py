"""Metricas de playstyle desde el timeline: CS@10/15, gold diff@15, KP%, etc."""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from ..config import ROLE_DISPLAY
from ._helpers import find_participant, is_remake, normalized_role, safe_div


def _participant_id_for_puuid(match: dict[str, Any], puuid: str) -> int | None:
    for p in match.get("info", {}).get("participants", []):
        if p.get("puuid") == puuid:
            return int(p.get("participantId", 0))
    return None


def _direct_opponent_pid(match: dict[str, Any], player: dict[str, Any]) -> int | None:
    """Encuentra el participantId del oponente del mismo rol y team contrario."""
    role = normalized_role(player)
    if not role:
        return None
    my_team = player.get("teamId")
    for p in match.get("info", {}).get("participants", []):
        if p.get("teamId") == my_team:
            continue
        if normalized_role(p) == role:
            return int(p.get("participantId", 0))
    return None


def _frame_at_minute(timeline: dict[str, Any], minute: int) -> dict[str, Any] | None:
    """Devuelve el frame mas cercano al minuto X (frames son cada 1min aprox)."""
    frames = timeline.get("info", {}).get("frames", [])
    target_ms = minute * 60_000
    best = None
    for f in frames:
        ts = f.get("timestamp", 0)
        if ts <= target_ms:
            best = f
        else:
            if best is None:
                best = f
            break
    return best


def _participant_frame(frame: dict[str, Any], pid: int) -> dict[str, Any] | None:
    pf = frame.get("participantFrames", {}) or {}
    return pf.get(str(pid))


def compute_playstyle(
    matches: list[dict[str, Any]],
    timelines: dict[str, dict[str, Any]],
    puuid: str,
    baselines: dict[str, dict[str, float]] | None = None,
) -> dict[str, Any]:
    """Calcula metricas agregadas por rol vs baseline.

    `baselines` es el dict {role: {metric: target}} cargado para un rank
    especifico (ver `config.load_baselines`). Si no se pasa, se usa un
    fallback vacio: las metricas no van a tener target y los deltas
    aparecen como '—' en el reporte.
    """
    if baselines is None:
        baselines = {}
    by_role: dict[str, dict[str, list[float]]] = defaultdict(
        lambda: defaultdict(list)
    )

    for match in matches:
        if is_remake(match):
            continue
        info = match.get("info", {})
        match_id = match.get("metadata", {}).get("matchId") or info.get("gameId")

        player = find_participant(match, puuid)
        if player is None:
            continue
        role = normalized_role(player)
        if not role:
            continue
        my_pid = _participant_id_for_puuid(match, puuid)
        opp_pid = _direct_opponent_pid(match, player)

        timeline = timelines.get(str(match_id))
        team_id = player.get("teamId")
        team_kills = sum(
            p.get("kills", 0)
            for p in info.get("participants", [])
            if p.get("teamId") == team_id
        )
        my_kp = safe_div(
            player.get("kills", 0) + player.get("assists", 0), team_kills
        )
        by_role[role]["kp"].append(my_kp)

        duration_s = info.get("gameDuration", 0)
        minutes = duration_s / 60.0 if duration_s else 0
        if minutes > 0:
            by_role[role]["dpm"].append(
                safe_div(player.get("totalDamageDealtToChampions", 0), minutes)
            )
            by_role[role]["vspm"].append(
                safe_div(player.get("visionScore", 0), minutes)
            )

        if timeline is None or my_pid is None:
            continue

        for minute in (10, 15):
            frame = _frame_at_minute(timeline, minute)
            if frame is None:
                continue
            mine = _participant_frame(frame, my_pid)
            if mine is None:
                continue
            cs_at = (
                mine.get("minionsKilled", 0) + mine.get("jungleMinionsKilled", 0)
            )
            gold_at = mine.get("totalGold", 0) or mine.get("currentGold", 0)
            by_role[role][f"cs{minute}"].append(float(cs_at))
            by_role[role][f"gold{minute}"].append(float(gold_at))
            if opp_pid is not None:
                opp = _participant_frame(frame, opp_pid)
                if opp is not None:
                    opp_gold = opp.get("totalGold", 0) or opp.get("currentGold", 0)
                    opp_cs = opp.get("minionsKilled", 0) + opp.get(
                        "jungleMinionsKilled", 0
                    )
                    by_role[role][f"gold_diff{minute}"].append(
                        float(gold_at - opp_gold)
                    )
                    by_role[role][f"cs_diff{minute}"].append(float(cs_at - opp_cs))

    out: list[dict[str, Any]] = []
    for role, metrics in by_role.items():
        sample_n = len(metrics.get("kp", []))
        if sample_n == 0:
            continue
        baseline = baselines.get(role, {})

        def _mean(key: str) -> float | None:
            vals = metrics.get(key, [])
            if not vals:
                return None
            return sum(vals) / len(vals)

        out.append(
            {
                "role": role,
                "role_display": ROLE_DISPLAY.get(role, role),
                "sample_size": sample_n,
                "cs10": _mean("cs10"),
                "cs15": _mean("cs15"),
                "gold10": _mean("gold10"),
                "gold15": _mean("gold15"),
                "gold_diff10": _mean("gold_diff10"),
                "gold_diff15": _mean("gold_diff15"),
                "cs_diff10": _mean("cs_diff10"),
                "cs_diff15": _mean("cs_diff15"),
                "kp": _mean("kp"),
                "dpm": _mean("dpm"),
                "vspm": _mean("vspm"),
                "baseline": baseline,
            }
        )
    out.sort(key=lambda r: -r["sample_size"])
    return {"by_role": out}


__all__ = ["compute_playstyle"]
