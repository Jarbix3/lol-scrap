"""Stats avanzadas por rol, extraidas del campo `challenges` de match-v5.

Riot pre-calcula 130+ metricas por participante en `participants[i].challenges`
(plates tomadas, solo kills, ventaja en lane, robos de objetivos, etc.).
Este modulo lee las que son relevantes para cada rol segun ROLE_ADVANCED_METRICS
en config.py y las agrega como (mean, total, n) por partida.
"""
from __future__ import annotations

from typing import Any

from ..config import ROLE_ADVANCED_METRICS
from ._helpers import iter_player_games


def _get_nested(d: dict[str, Any], dotted_key: str) -> Any:
    """Acceso por path con notacion 'a.b.c' sobre dicts anidados.

    Devuelve None si cualquier eslabon falta o no es dict.
    """
    cur: Any = d
    for part in dotted_key.split("."):
        if not isinstance(cur, dict):
            return None
        cur = cur.get(part)
    return cur


def compute_role_advanced(
    matches: list[dict[str, Any]],
    puuid: str,
    role: str,
) -> list[dict[str, Any]]:
    """Para un rol dado, agrega cada metrica de ROLE_ADVANCED_METRICS[role]
    sobre las partidas del puuid.

    Devuelve una lista de dicts:
      {
        "label": str,                     # texto humano
        "key": str,                       # path original (challenges.X)
        "display": "decimal"|"int"|"pct"|"signed",
        "hint": str | None,               # opcional
        "mean": float | None,             # promedio por partida (None si N=0)
        "total": float | None,            # suma total
        "min": float | None,
        "max": float | None,
        "n": int,                         # partidas con valor presente
      }

    Cada partida se cuenta solo si el campo esta presente en sus participants.
    Asi metricas que solo existen para algunos campeones/builds no inflan
    falsamente el denominador.
    """
    metrics_def = ROLE_ADVANCED_METRICS.get(role, [])
    out: list[dict[str, Any]] = []

    for spec in metrics_def:
        values: list[float] = []
        for _match, p in iter_player_games(matches, puuid):
            v = _get_nested(p, spec["key"])
            if v is None:
                continue
            try:
                values.append(float(v))
            except (TypeError, ValueError):
                continue

        n = len(values)
        if n == 0:
            out.append(
                {
                    "label": spec["label"],
                    "key": spec["key"],
                    "display": spec.get("display", "decimal"),
                    "hint": spec.get("hint"),
                    "mean": None,
                    "total": None,
                    "min": None,
                    "max": None,
                    "n": 0,
                }
            )
            continue

        out.append(
            {
                "label": spec["label"],
                "key": spec["key"],
                "display": spec.get("display", "decimal"),
                "hint": spec.get("hint"),
                "mean": sum(values) / n,
                "total": sum(values),
                "min": min(values),
                "max": max(values),
                "n": n,
            }
        )

    return out


__all__ = ["compute_role_advanced"]
