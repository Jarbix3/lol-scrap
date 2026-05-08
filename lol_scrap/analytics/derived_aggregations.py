"""Stats agregadas Tier A: cruces de partidas (no per-participant).

A diferencia de `derived_metrics.compute_tier_s` (que computa una metrica por
partida y la promedia), estas metricas dividen la muestra en sub-grupos y
comparan WR/KDA entre ellos. Por eso tienen un shape distinto al de
`role_advanced` y se renderizan en una sub-seccion propia del reporte.

Bloques implementados:
- MIDDLE.roam_conversion: WR cuando hay >=2 roams vs WR cuando 0 roams.
- BOTTOM.scaling_score: KDA en partidas largas (>=30') vs cortas (<25').
- JUNGLE.soul_rate: % de partidas largas con dragonTakedowns >= 4.
- MIDDLE.jungle_synergy_wr: top duo cuyo primary_position es JUNGLE.
- BOTTOM.adc_sup_synergy_wr: top duo cuyo primary_position es UTILITY.

Output shape (compute_tier_a):
{
  "role": "BOTTOM",
  "blocks": [
    {
      "label": "Scaling Score",
      "summary": "KDA largas: 3.1 (n=12) | KDA cortas: 1.8 (n=8) | ratio 1.72",
      "rows": [
        {"label": "Partidas largas (>=30')", "wr": 0.66, "kda": 3.1, "n": 12},
        {"label": "Partidas cortas (<25')", "wr": 0.50, "kda": 1.8, "n": 8},
      ],
      "interpretation": "Te beneficia el late game.",
      "metric_value": 1.72,
      "metric_label": "Scaling ratio",
    },
    ...
  ]
}
"""
from __future__ import annotations

from typing import Any

from ._helpers import iter_player_games, kda


# ============================================================
# Helpers
# ============================================================


def _split_by(
    matches: list[dict[str, Any]],
    puuid: str,
    bucket_fn,
) -> dict[str, dict[str, Any]]:
    """Itera matches, evalua bucket_fn(participant, match) -> str|None y agrupa.

    Devuelve {bucket: {"games": int, "wins": int, "kdas": list[float]}}.
    """
    buckets: dict[str, dict[str, Any]] = {}
    for match, p in iter_player_games(matches, puuid):
        key = bucket_fn(p, match)
        if key is None:
            continue
        b = buckets.setdefault(key, {"games": 0, "wins": 0, "kdas": []})
        b["games"] += 1
        if p.get("win"):
            b["wins"] += 1
        b["kdas"].append(kda(p))
    return buckets


def _wr(b: dict[str, Any]) -> float | None:
    return b["wins"] / b["games"] if b["games"] > 0 else None


def _avg_kda(b: dict[str, Any]) -> float | None:
    return sum(b["kdas"]) / len(b["kdas"]) if b["kdas"] else None


def _format_pct(v: float | None) -> str:
    return f"{v * 100:.0f}%" if v is not None else "n/a"


# ============================================================
# MIDDLE: Roam Conversion Rate
# ============================================================


def _roam_conversion(
    matches: list[dict[str, Any]], puuid: str
) -> dict[str, Any] | None:
    def bucket(p, _m):
        v = (p.get("challenges") or {}).get("killsOnOtherLanesEarlyJungleAsLaner")
        if v is None:
            return None
        try:
            v_f = float(v)
        except (TypeError, ValueError):
            return None
        if v_f >= 2:
            return "high_roam"
        if v_f == 0:
            return "no_roam"
        return None  # low roam (1) excluido para que el contraste sea claro

    buckets = _split_by(matches, puuid, bucket)
    high = buckets.get("high_roam", {"games": 0, "wins": 0, "kdas": []})
    low = buckets.get("no_roam", {"games": 0, "wins": 0, "kdas": []})
    if high["games"] == 0 and low["games"] == 0:
        return None

    wr_high = _wr(high)
    wr_low = _wr(low)
    delta_pp: float | None = None
    if wr_high is not None and wr_low is not None:
        delta_pp = (wr_high - wr_low) * 100

    if delta_pp is None:
        interp = "Sin contraste suficiente entre partidas con vs sin roam."
    elif delta_pp > 5:
        interp = (
            f"Tu roam ayuda (+{delta_pp:.0f} pp WR cuando >=2 roams vs 0)."
        )
    elif delta_pp < -5:
        interp = (
            f"Tu roam perjudica ({delta_pp:.0f} pp WR vs no roamear). "
            f"Roameas en mal momento."
        )
    else:
        interp = "Roam neutro: poca diferencia entre roamear o no."

    summary = (
        f"WR con >=2 roams: {_format_pct(wr_high)} (n={high['games']}) | "
        f"WR con 0 roams: {_format_pct(wr_low)} (n={low['games']})"
    )

    return {
        "label": "Roam Conversion Rate",
        "summary": summary,
        "rows": [
            {
                "label": "Partidas con >=2 roams",
                "wr": wr_high,
                "kda": _avg_kda(high),
                "n": high["games"],
            },
            {
                "label": "Partidas con 0 roams",
                "wr": wr_low,
                "kda": _avg_kda(low),
                "n": low["games"],
            },
        ],
        "interpretation": interp,
        "metric_value": delta_pp,
        "metric_label": "Delta WR (pp)",
    }


# ============================================================
# BOTTOM: Scaling Score
# ============================================================


def _scaling_score(
    matches: list[dict[str, Any]], puuid: str
) -> dict[str, Any] | None:
    def bucket(_p, m):
        dur = (m.get("info") or {}).get("gameDuration", 0) or 0
        if dur >= 30 * 60:
            return "long"
        if dur < 25 * 60:
            return "short"
        return None  # 25-30 min excluido (ventana ambigua)

    buckets = _split_by(matches, puuid, bucket)
    long = buckets.get("long", {"games": 0, "wins": 0, "kdas": []})
    short = buckets.get("short", {"games": 0, "wins": 0, "kdas": []})
    if long["games"] == 0 and short["games"] == 0:
        return None

    kda_long = _avg_kda(long)
    kda_short = _avg_kda(short)
    ratio: float | None = None
    if kda_long is not None and kda_short is not None and kda_short > 0:
        ratio = kda_long / kda_short

    if ratio is None:
        interp = "Sin contraste suficiente entre partidas largas y cortas."
    elif ratio >= 1.5:
        interp = (
            f"Te beneficia el late game (KDA x{ratio:.2f}). Ideal para "
            f"scaling carries (Vayne, Twitch, Kog)."
        )
    elif ratio >= 1.1:
        interp = (
            f"Performeas mejor en partidas largas (x{ratio:.2f}) pero no "
            f"dramaticamente."
        )
    elif ratio >= 0.9:
        interp = "Performance estable: el scaling no marca diferencia."
    else:
        interp = (
            f"Tu rendimiento cae en partidas largas (x{ratio:.2f}). Posible "
            f"early-game ADC (Draven, Lucian) o problemas de positioning late."
        )

    summary = (
        f"KDA largas (>=30'): "
        f"{kda_long:.2f} (n={long['games']}) | "
        f"KDA cortas (<25'): "
        f"{kda_short:.2f} (n={short['games']})"
        if kda_long is not None and kda_short is not None
        else "Insuficientes datos."
    )

    return {
        "label": "Scaling Score",
        "summary": summary,
        "rows": [
            {
                "label": "Partidas largas (>=30')",
                "wr": _wr(long),
                "kda": kda_long,
                "n": long["games"],
            },
            {
                "label": "Partidas cortas (<25')",
                "wr": _wr(short),
                "kda": kda_short,
                "n": short["games"],
            },
        ],
        "interpretation": interp,
        "metric_value": ratio,
        "metric_label": "KDA ratio (largas / cortas)",
    }


# ============================================================
# JUNGLE: Soul Rate
# ============================================================


def _soul_rate(
    matches: list[dict[str, Any]], puuid: str
) -> dict[str, Any] | None:
    long_n = 0
    long_with_soul = 0
    long_wins = 0
    short_n = 0
    short_with_soul = 0
    short_wins = 0
    for match, p in iter_player_games(matches, puuid):
        dur = (match.get("info") or {}).get("gameDuration", 0) or 0
        ch = p.get("challenges") or {}
        drakes = ch.get("dragonTakedowns") or 0
        try:
            drakes_f = float(drakes)
        except (TypeError, ValueError):
            drakes_f = 0
        win = bool(p.get("win"))
        is_long = dur >= 25 * 60
        if is_long:
            long_n += 1
            if drakes_f >= 4:
                long_with_soul += 1
            if win:
                long_wins += 1
        else:
            short_n += 1
            if drakes_f >= 4:
                short_with_soul += 1
            if win:
                short_wins += 1

    if long_n == 0:
        return None

    soul_rate = long_with_soul / long_n
    long_wr = long_wins / long_n if long_n else None

    if soul_rate >= 0.5:
        interp = (
            f"Controlas el bot side (soul rate {soul_rate * 100:.0f}%). "
            f"Buen tempo de drake."
        )
    elif soul_rate >= 0.25:
        interp = (
            f"Soul rate medio ({soul_rate * 100:.0f}%): a veces ganas la "
            f"alma, a veces la perdes."
        )
    else:
        interp = (
            f"Cedes la soul ({soul_rate * 100:.0f}%). Priorizar ward de "
            f"drake desde el primer drake (4:30) y rotar bot lane."
        )

    summary = (
        f"Soul tomada en {long_with_soul}/{long_n} partidas largas "
        f"({soul_rate * 100:.0f}%) | WR partidas largas: "
        f"{_format_pct(long_wr)}"
    )

    return {
        "label": "Soul Rate",
        "summary": summary,
        "rows": [
            {
                "label": "Partidas largas (>=25') con soul",
                "wr": (long_wins / long_n) if long_n else None,
                "kda": None,
                "n": long_with_soul,
            },
            {
                "label": "Partidas largas totales",
                "wr": (long_wins / long_n) if long_n else None,
                "kda": None,
                "n": long_n,
            },
        ],
        "interpretation": interp,
        "metric_value": soul_rate,
        "metric_label": "Rate de soul tomada",
    }


# ============================================================
# Synergy WR (MIDDLE -> JUNGLE, BOTTOM -> UTILITY)
# ============================================================


def _synergy_wr(
    duo_partners: list[dict[str, Any]] | None,
    matches: list[dict[str, Any]],
    puuid: str,
    target_position: str,
) -> dict[str, Any] | None:
    """Encuentra el top duo cuyo primary_position == target_position.

    Compara su WR con el WR del jugador en partidas SIN ese duo. Si no hay duo
    matchando el rol, devuelve None.
    """
    if not duo_partners:
        return None
    candidates = [
        d
        for d in duo_partners
        if d.get("primary_position") == target_position
    ]
    if not candidates:
        return None
    # duo_partners ya viene sorted por -winrate. Tomamos el primero.
    top = max(
        candidates, key=lambda d: (d.get("winrate") or 0.0, d.get("games") or 0)
    )
    target_puuid = top.get("puuid")

    games_with = 0
    wins_with = 0
    games_without = 0
    wins_without = 0
    for match, p in iter_player_games(matches, puuid):
        team_id = p.get("teamId")
        win = bool(p.get("win"))
        is_with = False
        for ally in match.get("info", {}).get("participants", []):
            ally_puuid = ally.get("puuid")
            if not ally_puuid or ally_puuid == puuid:
                continue
            if ally.get("teamId") != team_id:
                continue
            if ally_puuid == target_puuid:
                is_with = True
                break
        if is_with:
            games_with += 1
            if win:
                wins_with += 1
        else:
            games_without += 1
            if win:
                wins_without += 1

    wr_with = wins_with / games_with if games_with else None
    wr_without = wins_without / games_without if games_without else None
    delta_pp: float | None = None
    if wr_with is not None and wr_without is not None:
        delta_pp = (wr_with - wr_without) * 100

    role_label = {"JUNGLE": "Jungla", "UTILITY": "Support"}.get(
        target_position, target_position
    )
    duo_name = top.get("display_name", "???")

    if delta_pp is None:
        interp = "Sin contraste suficiente."
    elif delta_pp > 10:
        interp = (
            f"{duo_name} es tu mejor duo {role_label} (+{delta_pp:.0f} pp WR). "
            f"Buscalo activamente."
        )
    elif delta_pp > 0:
        interp = (
            f"{duo_name} aporta marginalmente (+{delta_pp:.0f} pp WR)."
        )
    elif delta_pp > -10:
        interp = (
            f"Performance similar con o sin {duo_name}: synergy neutra."
        )
    else:
        interp = (
            f"WR cae con {duo_name} ({delta_pp:.0f} pp). Capaz no es buen duo "
            f"para vos en {role_label}."
        )

    summary = (
        f"Mejor duo {role_label}: **{duo_name}** "
        f"(WR juntos {_format_pct(wr_with)}, n={games_with}) | "
        f"WR sin él: {_format_pct(wr_without)} (n={games_without})"
    )

    return {
        "label": f"Synergy WR con {role_label}",
        "summary": summary,
        "rows": [
            {
                "label": f"Con {duo_name} ({role_label})",
                "wr": wr_with,
                "kda": None,
                "n": games_with,
            },
            {
                "label": f"Sin {duo_name}",
                "wr": wr_without,
                "kda": None,
                "n": games_without,
            },
        ],
        "interpretation": interp,
        "metric_value": delta_pp,
        "metric_label": "Delta WR (pp)",
    }


# ============================================================
# Public API
# ============================================================


def compute_tier_a(
    matches: list[dict[str, Any]],
    puuid: str,
    role: str,
    *,
    duo_partners: list[dict[str, Any]] | None = None,
) -> dict[str, Any] | None:
    """Stats Tier A para el rol indicado.

    Args:
        matches: matches v5 (filtrados al rol si corresponde).
        puuid: PUUID del jugador.
        role: TOP/JUNGLE/MIDDLE/BOTTOM/UTILITY.
        duo_partners: salida de `compute_duo_partners` (con campo
            `primary_position`). Necesario solo para Synergy WR.

    Returns:
        dict con shape `{"role": str, "blocks": [...]}` o None si el rol no
        tiene Tier A o no hay datos suficientes.
    """
    blocks: list[dict[str, Any]] = []

    if role == "MIDDLE":
        b = _roam_conversion(matches, puuid)
        if b is not None:
            blocks.append(b)
        b = _synergy_wr(duo_partners, matches, puuid, "JUNGLE")
        if b is not None:
            blocks.append(b)

    elif role == "BOTTOM":
        b = _scaling_score(matches, puuid)
        if b is not None:
            blocks.append(b)
        b = _synergy_wr(duo_partners, matches, puuid, "UTILITY")
        if b is not None:
            blocks.append(b)

    elif role == "JUNGLE":
        b = _soul_rate(matches, puuid)
        if b is not None:
            blocks.append(b)

    if not blocks:
        return None

    return {"role": role, "blocks": blocks}


__all__ = ["compute_tier_a"]
