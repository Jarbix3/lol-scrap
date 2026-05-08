"""Analisis por fase del juego (early / mid / late) con scores 1-10.

Cada fase tiene un set de metricas relevantes. Cada metrica se compara contra
un target (baseline del rol cuando aplica, o un objetivo universal) y se
puntua de 1 a 10:
    - 1  = significativamente por debajo del target
    - 5  = en linea con el target (jugador promedio del nivel)
    - 10 = significativamente por encima del target

El score de la fase es el promedio simple de los scores de sus metricas
disponibles. Funciona para todos los roles: cuando una metrica usa baseline
de rol, se calcula el target ponderado por la cantidad de partidas que el
jugador jugo en cada rol dentro de la muestra.

Definicion de fases:
    - Early: 0-15 minutos (laning phase)
    - Mid:   15-25 minutos (objetivos, primeras peleas grandes)
    - Late:  25+ minutos   (baron / soul / cierre)
"""
from __future__ import annotations

from typing import Any

from ._helpers import iter_player_games
from .playstyle import (
    _direct_opponent_pid,
    _frame_at_minute,
    _participant_frame,
    _participant_id_for_puuid,
)

EARLY_LABEL = "Early game (0-15')"
MID_LABEL = "Mid game (15-25')"
LATE_LABEL = "Late game (25'+)"


def _score(
    actual: float | None,
    target: float | None,
    *,
    scale: float = 1.5,
) -> float | None:
    """Score 1-10 alrededor de un target.

    `scale` controla cuan agresivamente cambia el score:
    - scale=1.5 (default): actual = 1.667 * target -> 10; actual = 0.333 * target -> 1
    - scale=2.0:           actual = 1.5 * target   -> 10; actual = 0.5 * target   -> 1
    """
    if actual is None or target is None or target == 0:
        return None
    ratio = actual / target
    raw = 5 + 5 * (ratio - 1) * scale
    return max(1.0, min(10.0, raw))


def _score_diff(
    actual: float | None,
    *,
    scale_unit: float = 1500.0,
) -> float | None:
    """Score 1-10 para metricas que viven alrededor de 0 (ej: gold diff).

    actual = +scale_unit -> 10
    actual =  0          -> 5
    actual = -scale_unit -> 1 (clamped)
    """
    if actual is None:
        return None
    raw = 5.5 + 4.5 * (actual / scale_unit)
    return max(1.0, min(10.0, raw))


def _phase_score(metrics: list[dict[str, Any]]) -> float | None:
    """Promedio simple de los scores de las metricas que tienen score."""
    scores = [m["score"] for m in metrics if m.get("score") is not None]
    if not scores:
        return None
    return sum(scores) / len(scores)


def _avg_pair(pairs: list[tuple[float, float]]) -> tuple[float | None, float | None]:
    """Devuelve (avg_actual, avg_target) ponderado por cada partida."""
    if not pairs:
        return None, None
    n = len(pairs)
    return sum(a for a, _ in pairs) / n, sum(t for _, t in pairs) / n


def compute_game_phases(
    matches: list[dict[str, Any]],
    timelines: dict[str, dict[str, Any]],
    puuid: str,
    baselines: dict[str, dict[str, float]] | None = None,
) -> dict[str, Any]:
    """Calcula scores 1-10 para early / mid / late game.

    Args:
        matches: lista de matches v5 (cada uno con `metadata.matchId`).
        timelines: dict {match_id: timeline_v5}. Puede estar vacio.
        puuid: PUUID del jugador.
        baselines: dict {role: {metric: target}} para el rank elegido (ver
            config.load_baselines). Si no se pasa, las metricas que dependen
            del baseline no tendran score.

    Returns:
        dict con shape:
            {
              "early": {"label": str, "score": float|None, "metrics": [...]},
              "mid":   {"label": str, "score": float|None, "metrics": [...]},
              "late":  {"label": str, "score": float|None, "metrics": [...]},
              "total_games": int,
              "long_games_n": int,   # partidas >= 25 min
            }
        Cada metrica:
            {
              "label": str, "value": float|None, "target": float|None,
              "fmt": "decimal"|"int"|"pct"|"signed",
              "score": float|None, "n": int,
            }
    """
    if baselines is None:
        baselines = {}

    # === Early raw aggregations ===
    cs10_pairs: list[tuple[float, float]] = []          # (actual, role baseline)
    gold_diff15: list[float] = []                       # diff vs lane opp at 15'
    # Metricas propias derivadas del timeline al min 14:
    # - won_lane_at_14: 1 si (my_gold + my_xp) > (opp_gold + opp_xp), 0 si no.
    # - lane_lead_at_14: delta numerico (my - opp) en oro-equivalente (oro + xp).
    # Por construccion la mediana poblacional de won_lane_at_14 es ~0.5 (cada
    # partida un jugador gana, otro pierde), entonces target=0.5 es honesto.
    won_lane_at_14: list[float] = []
    lane_lead_at_14: list[float] = []
    early_takedowns_pairs: list[tuple[float, float]] = []  # (actual, baseline)

    # === Mid raw aggregations ===
    kp_pairs: list[tuple[float, float]] = []
    dpm_pairs: list[tuple[float, float]] = []
    vspm_pairs: list[tuple[float, float]] = []
    objectives_pairs: list[tuple[float, float]] = []    # (actual, baseline)

    # === Late raw aggregations ===
    long_games_n = 0
    long_games_wins = 0
    long_kda_pairs: list[tuple[float, float]] = []      # (actual, role baseline)
    long_dmg_share_pairs: list[tuple[float, float]] = []  # (actual, role baseline)

    total_games = 0

    for match, p in iter_player_games(matches, puuid):
        info = match.get("info", {})
        ch = p.get("challenges", {}) or {}
        role = p.get("teamPosition") or ""
        duration_s = info.get("gameDuration", 0) or 0
        match_id = match.get("metadata", {}).get("matchId")
        timeline = timelines.get(str(match_id)) if timelines else None
        baseline = baselines.get(role, {})

        total_games += 1

        # === EARLY: CS @10 vs role baseline (timeline) ===
        if timeline is not None and role and "cs10" in baseline:
            my_pid = _participant_id_for_puuid(match, puuid)
            if my_pid is not None:
                frame = _frame_at_minute(timeline, 10)
                if frame is not None:
                    pf = _participant_frame(frame, my_pid)
                    if pf is not None:
                        cs = pf.get("minionsKilled", 0) + pf.get(
                            "jungleMinionsKilled", 0
                        )
                        cs10_pairs.append((float(cs), baseline["cs10"]))

        # === EARLY: Gold diff @15 vs lane opp + Won lane @14 (timeline) ===
        if timeline is not None and role:
            my_pid = _participant_id_for_puuid(match, puuid)
            opp_pid = _direct_opponent_pid(match, p)
            if my_pid is not None and opp_pid is not None:
                # Gold diff @15 (metrica existente)
                frame15 = _frame_at_minute(timeline, 15)
                if frame15 is not None:
                    mine15 = _participant_frame(frame15, my_pid)
                    opp15 = _participant_frame(frame15, opp_pid)
                    if mine15 is not None and opp15 is not None:
                        my_gold = mine15.get("totalGold", 0) or mine15.get(
                            "currentGold", 0
                        )
                        opp_gold = opp15.get("totalGold", 0) or opp15.get(
                            "currentGold", 0
                        )
                        gold_diff15.append(float(my_gold - opp_gold))

                # Won lane @14 + lane lead @14 (metricas nuevas, oro+xp combinado)
                frame14 = _frame_at_minute(timeline, 14)
                if frame14 is not None:
                    mine14 = _participant_frame(frame14, my_pid)
                    opp14 = _participant_frame(frame14, opp_pid)
                    if mine14 is not None and opp14 is not None:
                        my_score = float(
                            (mine14.get("totalGold") or 0)
                            + (mine14.get("xp") or 0)
                        )
                        opp_score = float(
                            (opp14.get("totalGold") or 0)
                            + (opp14.get("xp") or 0)
                        )
                        delta = my_score - opp_score
                        lane_lead_at_14.append(delta)
                        won_lane_at_14.append(1.0 if delta > 0 else 0.0)

        # === EARLY: challenges-based ===
        v = ch.get("takedownsFirstXMinutes")
        if v is not None and "takedowns_first_14" in baseline:
            early_takedowns_pairs.append(
                (float(v), baseline["takedowns_first_14"])
            )

        # === MID: KP, DPM, Vision/min vs role baseline ===
        kp = ch.get("killParticipation")
        if kp is not None and "kp" in baseline:
            kp_pairs.append((float(kp), baseline["kp"]))

        dpm = ch.get("damagePerMinute")
        if dpm is not None and "dpm" in baseline:
            dpm_pairs.append((float(dpm), baseline["dpm"]))

        vspm = ch.get("visionScorePerMinute")
        if vspm is not None and "vspm" in baseline:
            vspm_pairs.append((float(vspm), baseline["vspm"]))

        # === MID: objective participation ===
        if "objectives_per_game" in baseline:
            objs = sum(
                float(ch.get(k) or 0)
                for k in (
                    "dragonTakedowns",
                    "riftHeraldTakedowns",
                    "baronTakedowns",
                )
            )
            objectives_pairs.append((objs, baseline["objectives_per_game"]))

        # === LATE: solo cuenta partidas >= 25 min ===
        if duration_s >= 25 * 60:
            long_games_n += 1
            if p.get("win"):
                long_games_wins += 1
            kda = (p.get("kills", 0) + p.get("assists", 0)) / max(
                p.get("deaths", 0), 1
            )
            if "late_kda" in baseline:
                long_kda_pairs.append((kda, baseline["late_kda"]))
            tdp = ch.get("teamDamagePercentage")
            if tdp is not None and "late_team_dmg_share" in baseline:
                long_dmg_share_pairs.append(
                    (float(tdp), baseline["late_team_dmg_share"])
                )

    # === Build EARLY metrics ===
    early_metrics: list[dict[str, Any]] = []
    if cs10_pairs:
        avg_a, avg_t = _avg_pair(cs10_pairs)
        early_metrics.append(
            {
                "label": "CS @ 10' (vs baseline rol)",
                "value": avg_a,
                "target": avg_t,
                "fmt": "decimal",
                "score": _score(avg_a, avg_t, scale=1.5),
                "n": len(cs10_pairs),
            }
        )
    if gold_diff15:
        avg = sum(gold_diff15) / len(gold_diff15)
        early_metrics.append(
            {
                "label": "Gold diff @ 15' vs lane opp",
                "value": avg,
                "target": 0.0,
                "fmt": "signed",
                "score": _score_diff(avg, scale_unit=1500.0),
                "n": len(gold_diff15),
            }
        )
    if won_lane_at_14:
        avg = sum(won_lane_at_14) / len(won_lane_at_14)
        early_metrics.append(
            {
                "label": "Lane phase win rate (oro+exp @14')",
                "value": avg,
                "target": 0.5,
                "fmt": "pct",
                "score": _score(avg, 0.5, scale=1.5),
                "n": len(won_lane_at_14),
            }
        )
    if lane_lead_at_14:
        avg = sum(lane_lead_at_14) / len(lane_lead_at_14)
        early_metrics.append(
            {
                "label": "Lane lead promedio @14' (oro+exp)",
                "value": avg,
                "target": 0.0,
                "fmt": "signed",
                "score": _score_diff(avg, scale_unit=2000.0),
                "n": len(lane_lead_at_14),
            }
        )
    if early_takedowns_pairs:
        avg_a, avg_t = _avg_pair(early_takedowns_pairs)
        early_metrics.append(
            {
                "label": "Takedowns en los primeros 14'",
                "value": avg_a,
                "target": avg_t,
                "fmt": "decimal",
                "score": _score(avg_a, avg_t, scale=1.5),
                "n": len(early_takedowns_pairs),
            }
        )

    # === Build MID metrics ===
    mid_metrics: list[dict[str, Any]] = []
    if kp_pairs:
        avg_a, avg_t = _avg_pair(kp_pairs)
        mid_metrics.append(
            {
                "label": "Kill participation",
                "value": avg_a,
                "target": avg_t,
                "fmt": "pct",
                "score": _score(avg_a, avg_t, scale=1.5),
                "n": len(kp_pairs),
            }
        )
    if dpm_pairs:
        avg_a, avg_t = _avg_pair(dpm_pairs)
        mid_metrics.append(
            {
                "label": "Damage / min",
                "value": avg_a,
                "target": avg_t,
                "fmt": "int",
                "score": _score(avg_a, avg_t, scale=1.5),
                "n": len(dpm_pairs),
            }
        )
    if vspm_pairs:
        avg_a, avg_t = _avg_pair(vspm_pairs)
        mid_metrics.append(
            {
                "label": "Vision / min",
                "value": avg_a,
                "target": avg_t,
                "fmt": "decimal",
                "score": _score(avg_a, avg_t, scale=1.5),
                "n": len(vspm_pairs),
            }
        )
    if objectives_pairs:
        avg_a, avg_t = _avg_pair(objectives_pairs)
        mid_metrics.append(
            {
                "label": "Drake + Heraldo + Baron takedowns / partida",
                "value": avg_a,
                "target": avg_t,
                "fmt": "decimal",
                "score": _score(avg_a, avg_t, scale=1.5),
                "n": len(objectives_pairs),
            }
        )

    # === Build LATE metrics ===
    late_metrics: list[dict[str, Any]] = []
    if long_games_n > 0:
        wr = long_games_wins / long_games_n
        late_metrics.append(
            {
                "label": "Winrate en partidas largas (>=25')",
                "value": wr,
                "target": 0.5,
                "fmt": "pct",
                "score": _score(wr, 0.5, scale=1.5),
                "n": long_games_n,
            }
        )
    if long_kda_pairs:
        avg_a, avg_t = _avg_pair(long_kda_pairs)
        late_metrics.append(
            {
                "label": "KDA en partidas largas",
                "value": avg_a,
                "target": avg_t,
                "fmt": "decimal",
                "score": _score(avg_a, avg_t, scale=1.5),
                "n": len(long_kda_pairs),
            }
        )
    if long_dmg_share_pairs:
        avg_a, avg_t = _avg_pair(long_dmg_share_pairs)
        late_metrics.append(
            {
                "label": "% del damage del equipo (partidas largas)",
                "value": avg_a,
                "target": avg_t,
                "fmt": "pct",
                "score": _score(avg_a, avg_t, scale=1.5),
                "n": len(long_dmg_share_pairs),
            }
        )

    return {
        "early": {
            "label": EARLY_LABEL,
            "score": _phase_score(early_metrics),
            "metrics": early_metrics,
        },
        "mid": {
            "label": MID_LABEL,
            "score": _phase_score(mid_metrics),
            "metrics": mid_metrics,
        },
        "late": {
            "label": LATE_LABEL,
            "score": _phase_score(late_metrics),
            "metrics": late_metrics,
        },
        "total_games": total_games,
        "long_games_n": long_games_n,
    }


__all__ = ["compute_game_phases"]
