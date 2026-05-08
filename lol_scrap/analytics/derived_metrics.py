"""Stats derivadas por rol calculadas a partir de campos existentes.

Las metricas de este modulo NO se leen directamente del payload (como hace
`role_advanced.py`) sino que se computan combinando campos:

- Tier S (per-participante): ratios simples como Positioning Index =
  damageDealtToChampions / max(totalDamageTaken, 1). Se computan por partida
  y se agregan como (mean, total, min, max, n).
- Tier B (timeline events): metricas que dependen de eventos del timeline
  (CHAMPION_KILL, LEVEL_UP). Ej: tasa de muertes antes del minuto 10, tiempo
  promedio al level 6.

El shape de salida es identico al de `compute_role_advanced` (label, key,
display, hint, mean, total, min, max, n) para que el reporte pueda concatenar
ambos sin tratamiento especial.
"""
from __future__ import annotations

from typing import Any, Callable

from ._helpers import iter_player_games, normalized_role
from .timeline_events import (
    player_deaths,
    player_id_for_puuid,
    player_level_ups,
)


# ============================================================
# Tier S - ratios per-partida
# ============================================================

ComputeFn = Callable[[dict[str, Any], dict[str, Any]], float | None]


def _positioning_index(p: dict[str, Any], _m: dict[str, Any]) -> float | None:
    """ADC: damageDealtToChampions / max(totalDamageTaken, 1)."""
    try:
        dmg = float(p.get("totalDamageDealtToChampions") or 0)
        taken = float(p.get("totalDamageTaken") or 0)
        if dmg <= 0 and taken <= 0:
            return None
        return dmg / max(taken, 1.0)
    except (TypeError, ValueError):
        return None


def _splitpush_index(p: dict[str, Any], _m: dict[str, Any]) -> float | None:
    """TOP: damageDealtToTurrets / max(totalDamageDealtToChampions, 1)."""
    try:
        turrets = float(p.get("damageDealtToTurrets") or 0)
        champs = float(p.get("totalDamageDealtToChampions") or 0)
        if turrets <= 0 and champs <= 0:
            return None
        return turrets / max(champs, 1.0)
    except (TypeError, ValueError):
        return None


def _counter_jungle_ratio(p: dict[str, Any], _m: dict[str, Any]) -> float | None:
    """JUNGLE: enemyJungleMonsterKills / max(alliedJungleMonsterKills, 1)."""
    ch = p.get("challenges") or {}
    enemy = ch.get("enemyJungleMonsterKills")
    allied = ch.get("alliedJungleMonsterKills")
    if enemy is None and allied is None:
        return None
    try:
        enemy_f = float(enemy or 0)
        allied_f = float(allied or 0)
        return enemy_f / max(allied_f, 1.0)
    except (TypeError, ValueError):
        return None


def _vision_dominance_ratio(
    p: dict[str, Any], match: dict[str, Any]
) -> float | None:
    """SUPPORT: visionScore propio / max(visionScore_opp_sup, 1).

    Busca al support del equipo rival usando `teamPosition == "UTILITY"`.
    Si no hay sup rival identificable, devuelve None.
    """
    my_team = p.get("teamId")
    my_vs = p.get("visionScore")
    if my_vs is None:
        return None
    opp_sup_vs: float | None = None
    for other in match.get("info", {}).get("participants", []):
        if other.get("teamId") == my_team:
            continue
        if normalized_role(other) == "UTILITY":
            v = other.get("visionScore")
            if v is not None:
                opp_sup_vs = float(v)
                break
    if opp_sup_vs is None:
        return None
    try:
        return float(my_vs) / max(opp_sup_vs, 1.0)
    except (TypeError, ValueError):
        return None


_TIER_S_REGISTRY: dict[str, list[dict[str, Any]]] = {
    "BOTTOM": [
        {
            "key": "derived.positioning_index",
            "label": "Positioning Index",
            "display": "decimal",
            "hint": (
                "Dano hecho / Dano recibido. Target Diamond ADC ~1.0-1.4. "
                "Bajo (<0.7) = peleas de adelante; alto (>1.6) = pasivo."
            ),
            "compute": _positioning_index,
        },
    ],
    "TOP": [
        {
            "key": "derived.splitpush_index",
            "label": "Splitpush Index",
            "display": "decimal",
            "hint": (
                "Dano a torres / Dano a champs. Splitpushers (Fiora, Trynda, "
                "Camille) ~0.4-0.6; teamfighters (Ornn, Mao) ~0.15-0.25."
            ),
            "compute": _splitpush_index,
        },
    ],
    "JUNGLE": [
        {
            "key": "derived.counter_jungle_ratio",
            "label": "Counter-jungle ratio",
            "display": "decimal",
            "hint": (
                "CS de jungla enemiga / propia. >1 = invader puro; "
                "0.5-0.8 = balanceado; <0.3 = pasivo."
            ),
            "compute": _counter_jungle_ratio,
        },
    ],
    "UTILITY": [
        {
            "key": "derived.vision_dominance_ratio",
            "label": "Vision Dominance Ratio",
            "display": "decimal",
            "hint": (
                "Vision score propio / vision del sup rival. Target sup pro "
                "diamond+: >1.3."
            ),
            "compute": _vision_dominance_ratio,
        },
    ],
    "MIDDLE": [],
}


def _aggregate(
    matches: list[dict[str, Any]],
    puuid: str,
    spec: dict[str, Any],
) -> dict[str, Any]:
    """Aplica spec['compute'] a cada partida y arma el dict agregado."""
    fn: ComputeFn = spec["compute"]
    values: list[float] = []
    for match, p in iter_player_games(matches, puuid):
        try:
            v = fn(p, match)
        except Exception:
            v = None
        if v is None:
            continue
        try:
            values.append(float(v))
        except (TypeError, ValueError):
            continue

    n = len(values)
    base = {
        "label": spec["label"],
        "key": spec["key"],
        "display": spec.get("display", "decimal"),
        "hint": spec.get("hint"),
    }
    if n == 0:
        return {
            **base,
            "mean": None,
            "total": None,
            "min": None,
            "max": None,
            "n": 0,
        }
    return {
        **base,
        "mean": sum(values) / n,
        "total": sum(values),
        "min": min(values),
        "max": max(values),
        "n": n,
    }


def compute_tier_s(
    matches: list[dict[str, Any]],
    puuid: str,
    role: str,
) -> list[dict[str, Any]]:
    """Stats derivadas Tier S para el rol indicado.

    Devuelve una lista con el mismo shape que `compute_role_advanced`. Si el
    rol no tiene metricas Tier S asociadas, devuelve [].
    """
    specs = _TIER_S_REGISTRY.get(role, [])
    return [_aggregate(matches, puuid, spec) for spec in specs]


# ============================================================
# Tier B - metricas de timeline events
# ============================================================


def _per_match_event_metric(
    matches: list[dict[str, Any]],
    timelines: dict[str, dict[str, Any]],
    puuid: str,
    extract_value: Callable[[dict[str, Any], int, dict[str, Any]], float | None],
) -> list[float]:
    """Itera matches y para cada uno aplica extract_value(timeline, pid, p).

    Devuelve la lista de valores no-None, descartando partidas sin timeline o
    sin participante encontrado.
    """
    values: list[float] = []
    for match, p in iter_player_games(matches, puuid):
        match_id = match.get("metadata", {}).get("matchId")
        if not match_id:
            continue
        timeline = timelines.get(str(match_id))
        if timeline is None:
            continue
        pid = player_id_for_puuid(timeline, puuid)
        if pid is None:
            continue
        try:
            v = extract_value(timeline, pid, p)
        except Exception:
            v = None
        if v is None:
            continue
        try:
            values.append(float(v))
        except (TypeError, ValueError):
            continue
    return values


def _early_death_count(
    threshold_ms: int,
) -> Callable[[dict[str, Any], int, dict[str, Any]], float]:
    """Factory: extrae numero de muertes antes de threshold_ms para cada partida."""

    def _fn(timeline: dict[str, Any], pid: int, _p: dict[str, Any]) -> float:
        deaths = player_deaths(timeline, pid)
        return float(sum(1 for ts in deaths if ts < threshold_ms))

    return _fn


def _level6_time_seconds(
    timeline: dict[str, Any], pid: int, _p: dict[str, Any]
) -> float | None:
    """Devuelve el tiempo (en segundos) del primer LEVEL_UP a level 6, o None."""
    for level, ts in player_level_ups(timeline, pid):
        if level == 6:
            return ts / 1000.0
    return None


def _build_metric_dict(
    *, label: str, key: str, display: str, hint: str | None, values: list[float]
) -> dict[str, Any]:
    n = len(values)
    base = {"label": label, "key": key, "display": display, "hint": hint}
    if n == 0:
        return {
            **base,
            "mean": None,
            "total": None,
            "min": None,
            "max": None,
            "n": 0,
        }
    return {
        **base,
        "mean": sum(values) / n,
        "total": sum(values),
        "min": min(values),
        "max": max(values),
        "n": n,
    }


def compute_tier_b(
    matches: list[dict[str, Any]],
    timelines: dict[str, dict[str, Any]] | None,
    puuid: str,
    role: str,
) -> list[dict[str, Any]]:
    """Stats Tier B (basadas en eventos del timeline) para el rol indicado.

    Si no hay timelines o el rol no tiene Tier B, devuelve []. Si los hay
    pero ninguna partida del rol tiene eventos extraibles, devuelve la
    metrica con n=0 para que el reporte muestre 'sin datos'.
    """
    if timelines is None:
        timelines = {}

    out: list[dict[str, Any]] = []

    if role == "TOP":
        values = _per_match_event_metric(
            matches, timelines, puuid, _early_death_count(10 * 60 * 1000)
        )
        out.append(
            _build_metric_dict(
                label="Muertes antes del 10' (avg)",
                key="derived.early_death_rate_10",
                display="decimal",
                hint="Sobreextension recurrente. Target: <0.5 por partida.",
                values=values,
            )
        )

    if role == "BOTTOM":
        values = _per_match_event_metric(
            matches, timelines, puuid, _early_death_count(25 * 60 * 1000)
        )
        out.append(
            _build_metric_dict(
                label="Muertes antes del 25' (avg)",
                key="derived.early_death_rate_25",
                display="decimal",
                hint=(
                    "ADCs no llegan al power spike (IE+PD) si mueren mucho. "
                    "Target: <3 por partida."
                ),
                values=values,
            )
        )

    if role == "JUNGLE":
        # Tempo a level 6
        tempo_values = _per_match_event_metric(
            matches, timelines, puuid, _level6_time_seconds
        )
        out.append(
            _build_metric_dict(
                label="Tiempo a level 6 (segundos avg)",
                key="derived.tempo_index_lvl6",
                display="int",
                hint=(
                    "Tempo del clear. Lee Sin diamond ~7:30 (450s); "
                    "Karthus ~8:30 (510s)."
                ),
                values=tempo_values,
            )
        )

        # Gank-to-Death ratio: precomputado a partir del agregado
        # gank_count = sum(challenges.killsOnOtherLanesEarlyJungleAsLaner)
        # death_early_count = sum(deaths_<900_000_ms)
        gank_total = 0.0
        gank_n = 0
        death_total = 0
        death_n = 0
        for match, p in iter_player_games(matches, puuid):
            ch = p.get("challenges") or {}
            v = ch.get("killsOnOtherLanesEarlyJungleAsLaner")
            if v is not None:
                try:
                    gank_total += float(v)
                    gank_n += 1
                except (TypeError, ValueError):
                    pass
            match_id = match.get("metadata", {}).get("matchId")
            if not match_id:
                continue
            timeline = timelines.get(str(match_id))
            if timeline is None:
                continue
            pid = player_id_for_puuid(timeline, puuid)
            if pid is None:
                continue
            deaths = player_deaths(timeline, pid)
            death_total += sum(1 for ts in deaths if ts < 15 * 60 * 1000)
            death_n += 1

        if gank_n > 0 and death_n > 0:
            ratio = gank_total / max(float(death_total), 1.0)
            out.append(
                {
                    "label": "Gank-to-Death ratio (early)",
                    "key": "derived.gank_to_death_ratio",
                    "display": "decimal",
                    "hint": (
                        "Total ganks early / total deaths antes del 15'. "
                        "Eficiente: >1.5; sobreextiende: <0.7."
                    ),
                    "mean": ratio,
                    "total": ratio,
                    "min": ratio,
                    "max": ratio,
                    "n": min(gank_n, death_n),
                }
            )
        else:
            out.append(
                {
                    "label": "Gank-to-Death ratio (early)",
                    "key": "derived.gank_to_death_ratio",
                    "display": "decimal",
                    "hint": (
                        "Total ganks early / total deaths antes del 15'. "
                        "Sin datos suficientes (necesita timelines)."
                    ),
                    "mean": None,
                    "total": None,
                    "min": None,
                    "max": None,
                    "n": 0,
                }
            )

    return out


__all__ = ["compute_tier_s", "compute_tier_b"]
