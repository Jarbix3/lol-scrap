"""Mapas de routing y constantes de Riot API."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PLATFORM_TO_REGIONAL: dict[str, str] = {
    "br1": "americas",
    "la1": "americas",
    "la2": "americas",
    "na1": "americas",
    "oc1": "sea",

    "euw1": "europe",
    "eun1": "europe",
    "tr1": "europe",
    "ru": "europe",

    "jp1": "asia",
    "kr": "asia",

    "ph2": "sea",
    "sg2": "sea",
    "th2": "sea",
    "tw2": "sea",
    "vn2": "sea",
}

REGION_ALIAS: dict[str, str] = {
    "lan": "la1",
    "las": "la2",
    "br": "br1",
    "na": "na1",
    "euw": "euw1",
    "eune": "eun1",
    "tr": "tr1",
    "jp": "jp1",
    "oce": "oc1",
    "ph": "ph2",
    "sg": "sg2",
    "th": "th2",
    "tw": "tw2",
    "vn": "vn2",
}


def normalize_platform(region: str) -> str:
    """Acepta tanto alias humanos (las, euw) como platform IDs (la2, euw1)."""
    key = region.strip().lower()
    if key in PLATFORM_TO_REGIONAL:
        return key
    if key in REGION_ALIAS:
        return REGION_ALIAS[key]
    raise ValueError(
        f"Region desconocida: {region!r}. "
        f"Usa una de: {sorted(set(PLATFORM_TO_REGIONAL) | set(REGION_ALIAS))}"
    )


def regional_for(platform: str) -> str:
    """Devuelve el routing regional (americas/europe/asia/sea) para un platform ID."""
    return PLATFORM_TO_REGIONAL[platform]


QUEUE_RANKED_SOLO = 420
QUEUE_RANKED_FLEX = 440
QUEUE_NAMES: dict[int, str] = {
    QUEUE_RANKED_SOLO: "Ranked Solo/Duo",
    QUEUE_RANKED_FLEX: "Ranked Flex",
    400: "Normal Draft",
    430: "Normal Blind",
    450: "ARAM",
    700: "Clash",
}

DEFAULT_QUEUES: tuple[int, ...] = (QUEUE_RANKED_SOLO, QUEUE_RANKED_FLEX)
DEFAULT_MATCH_COUNT = 100


# === Baselines: cargadas dinamicamente desde data/baselines.json ===
#
# Estructura del JSON:
#   {
#     "_meta": {...},
#     "ranks": {
#       "iron": {"TOP": {...}, "JUNGLE": {...}, ...},
#       "bronze": {...},
#       ...
#       "default": {...}
#     }
#   }
#
# Uso desde el codigo:
#   from .config import load_baselines
#   baselines = load_baselines("diamond")  # devuelve {role: {metric: value}}
#
# El usuario edita data/baselines.json para tunear los targets.

# Path al archivo. Resuelto relativo a la ubicacion de este modulo
# (`<repo>/lol_scrap/config.py` -> `<repo>/data/baselines.json`).
BASELINES_PATH: Path = Path(__file__).resolve().parent.parent / "data" / "baselines.json"

# Tiers que se agrupan en el bucket "master_plus" del JSON.
_MASTER_PLUS_TIERS: frozenset[str] = frozenset(
    {"master", "grandmaster", "challenger"}
)
_FALLBACK_RANK = "default"


def _load_baselines_file() -> dict[str, Any]:
    """Lee y parsea data/baselines.json. Cacheado en memoria."""
    global _baselines_cache
    try:
        return _baselines_cache
    except NameError:
        pass
    if not BASELINES_PATH.exists():
        raise FileNotFoundError(
            f"No se encontro el archivo de baselines: {BASELINES_PATH}. "
            f"Asegurate que exista (deberia venir con el repo)."
        )
    with BASELINES_PATH.open("r", encoding="utf-8") as fh:
        _baselines_cache = json.load(fh)  # noqa: F841
    return _baselines_cache


def available_ranks() -> list[str]:
    """Lista de keys de rank disponibles en el JSON (sin alias)."""
    data = _load_baselines_file()
    return sorted(data.get("ranks", {}).keys())


def normalize_rank(rank: str | None) -> str:
    """Normaliza un nombre de rank al key usado en el JSON.

    Acepta tier strings tipo Riot ('IRON', 'DIAMOND', etc), variantes en
    minuscula/Mayuscula, y agrupa MASTER/GRANDMASTER/CHALLENGER bajo
    'master_plus'. Si el rank es None o desconocido, devuelve 'default'.
    """
    if not rank:
        return _FALLBACK_RANK
    key = rank.strip().lower().replace(" ", "_")
    if not key:
        return _FALLBACK_RANK
    if key in _MASTER_PLUS_TIERS or key == "masterplus":
        return "master_plus"
    data = _load_baselines_file()
    if key in data.get("ranks", {}):
        return key
    return _FALLBACK_RANK


def load_baselines(rank: str | None) -> dict[str, dict[str, float]]:
    """Devuelve {role: {metric: value}} para el rank pedido.

    Si el rank no existe, hace fallback silencioso a 'default'. Si la entry
    de un rol no esta en el JSON, devuelve {} para ese rol.

    Las metricas con valor `null` en el JSON se filtran del resultado: el
    caller chequea presencia con `"metric" in baseline` para saber si tiene
    target o no. Esto permite que el JSON tenga `null` como placeholder
    explicito ("falta completar"), en vez de eliminar la key, manteniendo
    el shape uniforme.
    """
    rank_key = normalize_rank(rank)
    data = _load_baselines_file()
    ranks = data.get("ranks", {})
    bucket = ranks.get(rank_key) or ranks.get(_FALLBACK_RANK) or {}
    out: dict[str, dict[str, float]] = {}
    for role in VALID_ROLES:
        role_baselines = bucket.get(role) or {}
        out[role] = {
            k: float(v)
            for k, v in role_baselines.items()
            if v is not None
        }
    return out


def tier_from_league_entries(
    entries: list[dict[str, Any]] | None,
) -> tuple[str, str | None] | tuple[None, None]:
    """Extrae el tier (IRON, DIAMOND, etc.) de las league_entries del summoner.

    Prioriza RANKED_SOLO_5x5; cae a RANKED_FLEX_SR si Solo/Duo no esta.
    Devuelve (tier_lowercase, queue_label_humano) o (None, None) si no hay.
    Tier viene en mayusculas desde Riot, lo bajo a lowercase para el JSON.
    """
    if not entries:
        return (None, None)
    by_queue = {e.get("queueType"): e for e in entries if isinstance(e, dict)}
    for q_key, q_label in (
        ("RANKED_SOLO_5x5", "Solo/Duo"),
        ("RANKED_FLEX_SR", "Flex"),
    ):
        e = by_queue.get(q_key)
        if e and e.get("tier"):
            return (str(e["tier"]).lower(), q_label)
    return (None, None)


def rank_display(rank_key: str) -> str:
    """Capitaliza un rank key para mostrarlo (master_plus -> 'Master+')."""
    if rank_key == "master_plus":
        return "Master+"
    if rank_key == _FALLBACK_RANK:
        return "Default (Platinum-ish)"
    return rank_key.capitalize()


ROLE_DISPLAY: dict[str, str] = {
    "TOP": "Top",
    "JUNGLE": "Jungla",
    "MIDDLE": "Mid",
    "BOTTOM": "ADC",
    "UTILITY": "Support",
    "": "Sin rol",
}

ROLE_ALIAS: dict[str, str] = {
    "top": "TOP",
    "jungle": "JUNGLE",
    "jung": "JUNGLE",
    "jun": "JUNGLE",
    "jng": "JUNGLE",
    "jg": "JUNGLE",
    "mid": "MIDDLE",
    "middle": "MIDDLE",
    "bot": "BOTTOM",
    "bottom": "BOTTOM",
    "adc": "BOTTOM",
    "sup": "UTILITY",
    "supp": "UTILITY",
    "support": "UTILITY",
    "utility": "UTILITY",
}

VALID_ROLES: tuple[str, ...] = ("TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY")


def normalize_role(role: str) -> str:
    """Acepta alias (top/jun/mid/bot/sup, etc.) o canonical (TOP/JUNGLE/...).

    Devuelve el nombre canonical: TOP, JUNGLE, MIDDLE, BOTTOM o UTILITY.
    """
    key = role.strip().lower()
    if key.upper() in VALID_ROLES:
        return key.upper()
    if key in ROLE_ALIAS:
        return ROLE_ALIAS[key]
    raise ValueError(
        f"Rol desconocido: {role!r}. "
        f"Usa uno de: top, jungle, mid, bottom, support "
        f"(o canonical: {', '.join(VALID_ROLES)})"
    )


# Metricas avanzadas por rol, extraidas del campo `participants[i].challenges`
# de match-v5 (pre-calculadas por Riot) y de algunos campos top-level.
#
# Formato de cada entry:
#   key:     dotted path desde el dict del participant (ej. "challenges.soloKills")
#   label:   texto humano para la tabla
#   display: como formatear el promedio
#       - "decimal": X.XX
#       - "int":     entero (rounded)
#       - "pct":     XX.X%  (asume valor 0-1, o sea es un rate/proporcion)
#       - "signed":  +/-X.X (puede ser negativo, importa el signo)
#   hint:    (opcional) tooltip para el LLM/usuario sobre que significa
ROLE_ADVANCED_METRICS: dict[str, list[dict[str, str]]] = {
    "TOP": [
        {"key": "challenges.maxCsAdvantageOnLaneOpponent",
         "label": "Max CS lead vs rival (avg)",
         "display": "signed"},
        {"key": "challenges.maxLevelLeadLaneOpponent",
         "label": "Max level lead vs rival (avg)",
         "display": "signed"},
        {"key": "challenges.soloKills",
         "label": "Solo kills (por partida)",
         "display": "decimal"},
        {"key": "challenges.quickSoloKills",
         "label": "Solo kills rapidos (por partida)",
         "display": "decimal"},
        {"key": "challenges.turretPlatesTaken",
         "label": "Plates tomadas (por partida)",
         "display": "decimal"},
        {"key": "damageDealtToTurrets",
         "label": "Dano a torres (avg)",
         "display": "int"},
        {"key": "damageSelfMitigated",
         "label": "Dano mitigado (avg)",
         "display": "int"},
        {"key": "challenges.survivedSingleDigitHpCount",
         "label": "Supervivencias 1HP (por partida)",
         "display": "decimal"},
        {"key": "challenges.tookLargeDamageSurvived",
         "label": "Toma dano grande y sobrevive (por partida)",
         "display": "decimal"},
    ],
    "JUNGLE": [
        {"key": "challenges.jungleCsBefore10Minutes",
         "label": "CS de jungla antes del 10' (avg)",
         "display": "decimal",
         "hint": "Eficiencia del clear inicial"},
        {"key": "challenges.alliedJungleMonsterKills",
         "label": "CS de mi propia jungla (avg)",
         "display": "decimal"},
        {"key": "challenges.enemyJungleMonsterKills",
         "label": "CS de jungla enemiga (avg)",
         "display": "decimal",
         "hint": "Counter-jungling"},
        {"key": "challenges.killsOnOtherLanesEarlyJungleAsLaner",
         "label": "Takedowns en otras lanes (early)",
         "display": "decimal",
         "hint": "Gank impact temprano"},
        {"key": "challenges.takedownsBeforeJungleMinionSpawn",
         "label": "Takedowns antes del 1er camp spawn",
         "display": "decimal",
         "hint": "Lvl 2/3 invades"},
        {"key": "challenges.initialCrabCount",
         "label": "Scuttles iniciales (por partida)",
         "display": "decimal"},
        {"key": "challenges.scuttleCrabKills",
         "label": "Total scuttles (por partida)",
         "display": "decimal"},
        {"key": "challenges.dragonTakedowns",
         "label": "Drakes (por partida)",
         "display": "decimal"},
        {"key": "challenges.riftHeraldTakedowns",
         "label": "Heraldos (por partida)",
         "display": "decimal"},
        {"key": "challenges.baronTakedowns",
         "label": "Barones (por partida)",
         "display": "decimal"},
        {"key": "challenges.epicMonsterSteals",
         "label": "Robos de objetivos epicos (por partida)",
         "display": "decimal"},
        {"key": "challenges.controlWardTimeCoverageInRiverOrEnemyHalf",
         "label": "Cobertura wards en rio/jungla enemiga",
         "display": "pct"},
    ],
    "MIDDLE": [
        {"key": "challenges.maxCsAdvantageOnLaneOpponent",
         "label": "Max CS lead vs rival (avg)",
         "display": "signed"},
        {"key": "challenges.maxLevelLeadLaneOpponent",
         "label": "Max level lead vs rival (avg)",
         "display": "signed"},
        {"key": "challenges.soloKills",
         "label": "Solo kills (por partida)",
         "display": "decimal"},
        {"key": "challenges.killsOnOtherLanesEarlyJungleAsLaner",
         "label": "Takedowns en otras lanes (roams)",
         "display": "decimal",
         "hint": "Roam impact a side lanes"},
        {"key": "challenges.acesBefore15Minutes",
         "label": "Aces antes del 15' (por partida)",
         "display": "decimal",
         "hint": "Snowball capacity"},
        {"key": "challenges.teamDamagePercentage",
         "label": "% del dano del equipo",
         "display": "pct"},
        {"key": "challenges.damagePerMinute",
         "label": "DPM (avg)",
         "display": "int"},
        {"key": "challenges.multiKillOneSpell",
         "label": "Multikills con un spell (por partida)",
         "display": "decimal"},
        {"key": "challenges.mejaisFullStackInTime",
         "label": "Mejais full stack a tiempo",
         "display": "decimal"},
    ],
    "BOTTOM": [
        {"key": "challenges.goldPerMinute",
         "label": "GPM (avg)",
         "display": "int"},
        {"key": "challenges.damagePerMinute",
         "label": "DPM (avg)",
         "display": "int"},
        {"key": "challenges.teamDamagePercentage",
         "label": "% del dano del equipo",
         "display": "pct"},
        {"key": "challenges.kTurretsDestroyedBeforePlatesFall",
         "label": "Torres destruidas antes de caer plates",
         "display": "decimal"},
        {"key": "challenges.quickFirstTurret",
         "label": "First turret rapida (rate)",
         "display": "decimal"},
        {"key": "challenges.dodgeSkillShotsSmallWindow",
         "label": "Skillshots dodgeados (small window)",
         "display": "decimal"},
        {"key": "challenges.landSkillShotsEarlyGame",
         "label": "Skillshots conectados early (avg)",
         "display": "decimal"},
        {"key": "challenges.legendaryCount",
         "label": "Items legendarios completados (por partida)",
         "display": "decimal"},
        {"key": "challenges.survivedSingleDigitHpCount",
         "label": "Supervivencias 1HP (por partida)",
         "display": "decimal"},
    ],
    "UTILITY": [
        {"key": "challenges.visionScorePerMinute",
         "label": "Vision/min (avg)",
         "display": "decimal",
         "hint": "Ideal sup: 1.8-2.5+"},
        {"key": "challenges.visionScoreAdvantageLaneOpponent",
         "label": "Diff de vision vs sup rival (avg)",
         "display": "signed"},
        {"key": "challenges.controlWardsPlaced",
         "label": "Control wards puestos (por partida)",
         "display": "decimal"},
        {"key": "challenges.stealthWardsPlaced",
         "label": "Wards stealth puestos (por partida)",
         "display": "decimal"},
        {"key": "challenges.wardTakedowns",
         "label": "Wards enemigas eliminadas (por partida)",
         "display": "decimal"},
        {"key": "challenges.wardTakedownsBefore20M",
         "label": "Wards eliminadas antes del 20' (por partida)",
         "display": "decimal"},
        {"key": "challenges.controlWardTimeCoverageInRiverOrEnemyHalf",
         "label": "Cobertura wards en rio/jungla enemiga",
         "display": "pct"},
        {"key": "challenges.enemyChampionImmobilizations",
         "label": "CC sobre enemigos (por partida)",
         "display": "decimal"},
        {"key": "challenges.effectiveHealAndShielding",
         "label": "Heals + shields efectivos (avg)",
         "display": "int"},
        {"key": "challenges.saveAllyFromDeath",
         "label": "Saves de aliados (por partida)",
         "display": "decimal"},
        {"key": "challenges.pickKillWithAlly",
         "label": "Picks coordinados (por partida)",
         "display": "decimal"},
        {"key": "challenges.immobilizeAndKillWithAlly",
         "label": "CC + kill con aliado (por partida)",
         "display": "decimal"},
        {"key": "challenges.completeSupportQuestInTime",
         "label": "Quest support a tiempo (rate)",
         "display": "decimal"},
        {"key": "challenges.killsOnOtherLanesEarlyJungleAsLaner",
         "label": "Roam impact (takedowns en otras lanes)",
         "display": "decimal",
         "hint": "Roams sup post drake/recall. Engage/pick sups: >2; enchanters: 0-1."},
    ],
}
