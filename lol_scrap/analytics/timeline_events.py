"""Parser de eventos de timeline-v5 (CHAMPION_KILL, LEVEL_UP, etc.).

Riot devuelve los timelines con shape:
    {
      "metadata": {...},
      "info": {
        "frames": [
          {
            "timestamp": <ms>,
            "participantFrames": {"1": {...}, ...},
            "events": [{"type": "CHAMPION_KILL", "timestamp": ..., ...}, ...]
          },
          ...
        ],
        "participants": [{"participantId": 1, "puuid": "..."}, ...]
      }
    }

El proyecto cachea los timelines completos (incluyendo events) en cache/timelines/.
Este modulo expone helpers para extraer informacion de los events sin imponer
la estructura de los analytics que ya existen (que solo leen participantFrames).
"""
from __future__ import annotations

from typing import Any


def player_id_for_puuid(timeline: dict[str, Any], puuid: str) -> int | None:
    """Devuelve el participantId asociado al puuid en el timeline, o None.

    Riot incluye el mapping en `info.participants` (NO confundir con el de
    matches que tiene mucho mas detalle). Para timelines es solo
    [{participantId, puuid}, ...].
    """
    for entry in timeline.get("info", {}).get("participants", []) or []:
        if entry.get("puuid") == puuid:
            pid = entry.get("participantId")
            if pid is None:
                return None
            try:
                return int(pid)
            except (TypeError, ValueError):
                return None
    return None


def _iter_events(timeline: dict[str, Any]):
    """Itera todos los events de todos los frames en orden cronologico."""
    for frame in timeline.get("info", {}).get("frames", []) or []:
        for ev in frame.get("events", []) or []:
            yield ev


def player_deaths(timeline: dict[str, Any], participant_id: int) -> list[int]:
    """Lista de timestamps_ms (sorted) donde el participant murio.

    Filtra events `CHAMPION_KILL` con `victimId == participant_id`. Si no hay
    eventos de muerte (o el timeline no tiene events), devuelve [].
    """
    out: list[int] = []
    for ev in _iter_events(timeline):
        if ev.get("type") != "CHAMPION_KILL":
            continue
        if ev.get("victimId") != participant_id:
            continue
        ts = ev.get("timestamp")
        if ts is None:
            continue
        try:
            out.append(int(ts))
        except (TypeError, ValueError):
            continue
    out.sort()
    return out


def player_kills_assists(
    timeline: dict[str, Any], participant_id: int
) -> list[tuple[int, str]]:
    """Lista de (timestamp_ms, kind) donde kind es 'kill' o 'assist'.

    Util para analizar cuando el jugador participa en takedowns. No se usa hoy
    pero queda expuesto para futuras metricas (ej. avg time to first kill).
    """
    out: list[tuple[int, str]] = []
    for ev in _iter_events(timeline):
        if ev.get("type") != "CHAMPION_KILL":
            continue
        ts = ev.get("timestamp")
        if ts is None:
            continue
        try:
            ts_i = int(ts)
        except (TypeError, ValueError):
            continue
        if ev.get("killerId") == participant_id:
            out.append((ts_i, "kill"))
            continue
        assistants = ev.get("assistingParticipantIds") or []
        if participant_id in assistants:
            out.append((ts_i, "assist"))
    out.sort(key=lambda x: x[0])
    return out


def player_level_ups(
    timeline: dict[str, Any], participant_id: int
) -> list[tuple[int, int]]:
    """Lista de (level, timestamp_ms) sorted por timestamp.

    Filtra events `LEVEL_UP` con `participantId == participant_id`. Cada event
    indica el level *nuevo* (post level-up).
    """
    out: list[tuple[int, int]] = []
    for ev in _iter_events(timeline):
        if ev.get("type") != "LEVEL_UP":
            continue
        if ev.get("participantId") != participant_id:
            continue
        level = ev.get("level")
        ts = ev.get("timestamp")
        if level is None or ts is None:
            continue
        try:
            out.append((int(level), int(ts)))
        except (TypeError, ValueError):
            continue
    out.sort(key=lambda x: x[1])
    return out


__all__ = [
    "player_id_for_puuid",
    "player_deaths",
    "player_kills_assists",
    "player_level_ups",
]
