"""Mapas de routing y constantes de Riot API."""
from __future__ import annotations

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

ROLE_BASELINES: dict[str, dict[str, float]] = {
    "TOP":     {"cs10": 70.0, "cs15": 110.0, "kp": 0.45, "vspm": 0.6, "dpm": 450.0},
    "JUNGLE":  {"cs10": 50.0, "cs15": 80.0,  "kp": 0.65, "vspm": 0.9, "dpm": 380.0},
    "MIDDLE":  {"cs10": 75.0, "cs15": 115.0, "kp": 0.55, "vspm": 0.8, "dpm": 550.0},
    "BOTTOM":  {"cs10": 75.0, "cs15": 115.0, "kp": 0.55, "vspm": 0.7, "dpm": 600.0},
    "UTILITY": {"cs10": 15.0, "cs15": 25.0,  "kp": 0.65, "vspm": 1.8, "dpm": 250.0},
}

ROLE_DISPLAY: dict[str, str] = {
    "TOP": "Top",
    "JUNGLE": "Jungla",
    "MIDDLE": "Mid",
    "BOTTOM": "ADC",
    "UTILITY": "Support",
    "": "Sin rol",
}
