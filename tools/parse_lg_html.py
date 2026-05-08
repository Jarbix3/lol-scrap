"""
Parser de HTML de leagueofgraphs.com para refrescar `data/baselines.json`.

Flujo de uso:

1. Abrí en tu browser una URL como:

   https://www.leagueofgraphs.com/summoner/champions/<region>/<player>/<role>

   Por ejemplo:

   https://www.leagueofgraphs.com/summoner/champions/las/Manuchito-LAS/top
   https://www.leagueofgraphs.com/summoner/champions/las/Manuchito-LAS/jungle
   https://www.leagueofgraphs.com/summoner/champions/las/Manuchito-LAS/middle
   https://www.leagueofgraphs.com/summoner/champions/las/Manuchito-LAS/adc
   https://www.leagueofgraphs.com/summoner/champions/las/Manuchito-LAS/support

2. Una vez que la página termine de cargar (radar chart visible), guardá el HTML
   con `Ctrl+S` -> "Webpage, HTML only" en `data/raw/<lo_que_quieras>_<role>.html`.

   El nombre del archivo es libre, pero conviene incluir el rol al final para que
   el parser lo detecte automáticamente. Si no, podés pasar `--role` cuando lo
   corras.

3. Corré:

       python tools/parse_lg_html.py

   El script lee TODOS los `data/raw/*.html`, extrae los baselines de cada rango
   (Bronze, Silver, Gold, Platinum, Emerald, Diamond, Master+) para el rol
   detectado, y actualiza in-place `data/baselines.json`.

   Métricas que sobrescribe con datos reales de LG:

   A. Del radar chart (atributos data-chart-data):
     - kp                    (Kill participation)
     - dpm                   (Damage dealt / min)
     - gold_per_min          (Gold / min)
     - cs_per_min            (Creeps / min)
     - kills_assists_per_min (Kills + Assists / min)

   B. De las curvas temporales (charts en tabs farmingData/fightingData/...):
     - cs10                  (Minions killed @ t=10 min)
     - cs15                  (Minions killed @ t=15 min)
     - late_kda              ((K+A) @ t=30 / max(Deaths @ t=30, 1))
     - takedowns_first_14    (interpolacion lineal de K+A entre @t=10 y @t=15)

   C. De las tablas de baseline-por-rango (con progressBars):
     - vspm                  (Vision Score / minute, tabla en tab visionData)

   Métricas que NO toca (LG no las publica suficientemente; quedan en `null`
   o con el valor manual que vos hayas puesto):
     - objectives_per_game   (LG da Drakes del equipo + ratios de heralds/
                              barons; la metrica Riot original cuenta
                              takedowns DEL JUGADOR, no kills del equipo, asi
                              que mezclar ambas semanticas genera ruido)
     - late_team_dmg_share   (LG no expone "damage del equipo" en ninguna
                              tab; solo damage del jugador)

   Política de `null`: cuando una metrica vale `null` en el JSON, el script
   principal (game_phases / playstyle / report) la trata como "no disponible"
   y la omite del calculo en silencio. Las metricas no cubiertas por LG
   arrancan en `null` para que sea explicito que falta data confiable;
   completalas a mano cuando tengas datos reales (otras fuentes, papers,
   medicion propia, etc.).

4. Cada vez que LG actualice sus stats (~trimestral), repetí los pasos 1-3.

Notas:
  - Iron NO está cubierto por LG (sample chico). Su entry en baselines.json
    queda intacto.
  - LG agrupa Master, GrandMaster y Challenger en "Master" -> mapeamos a
    `master_plus` en el JSON.
  - Los charts de LG vienen embebidos en atributos `data-chart-data` /
    `data-chart-options` con HTML entities escapadas; no hace falta JS para
    leerlos.

Uso:

    python tools/parse_lg_html.py [--dry-run] [--baselines PATH]
                                  [--raw-dir PATH] [--role ROLE]
                                  [--only FILE.html ...]
"""

from __future__ import annotations

import argparse
import html as html_module
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASELINES = ROOT / "data" / "baselines.json"
DEFAULT_RAW_DIR = ROOT / "data" / "raw"


# Roles válidos en nuestro schema interno.
INTERNAL_ROLES = ("TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY")

# Aliases comunes -> rol interno. Aplican tanto al filename como al texto que
# aparece en el series.label de LG ("Average X Top", "Average X Jungle", etc.).
ROLE_ALIASES = {
    "top": "TOP",
    "jungle": "JUNGLE",
    "jungler": "JUNGLE",  # label que usa LG en sus series ("Average X Jungler")
    "jg": "JUNGLE",
    "mid": "MIDDLE",
    "middle": "MIDDLE",
    "bot": "BOTTOM",
    "bottom": "BOTTOM",
    "adc": "BOTTOM",
    "ad": "BOTTOM",
    "ad carry": "BOTTOM",  # label que usa LG en sus series ("Average X AD Carry")
    "carry": "BOTTOM",
    "sup": "UTILITY",
    "supp": "UTILITY",
    "support": "UTILITY",
    "utility": "UTILITY",
}

# Tier display de LG -> tier key del JSON.
TIER_LG_TO_JSON = {
    "Iron": "iron",
    "Bronze": "bronze",
    "Silver": "silver",
    "Gold": "gold",
    "Platinum": "platinum",
    "Emerald": "emerald",
    "Diamond": "diamond",
    "Master": "master_plus",
    "Grandmaster": "master_plus",
    "Challenger": "master_plus",
}

# Etiquetas esperadas (en orden) en `axis.labels` del radar chart de LG. Son
# strings tipo "Gold / min (431.5)" -> nos importa el prefijo.
EXPECTED_AXIS_PREFIXES = (
    "Gold / min",
    "Creeps / minute",
    "Kill participation",
    "Kills + Assists / min",
    "Damage dealt / min",
)

# Indices en el array `data` de cada series del radar, en el orden en que
# aparecen las labels del axis ("Gold / min", "Creeps / minute", ...).
IDX_GOLD_PER_MIN = 0
IDX_CS_PER_MIN = 1
IDX_KP = 2  # 0..1
IDX_KA_PER_MIN = 3
IDX_DPM = 4

# Regex para extraer todos los chart blocks del radar. data-chart-data viene
# como array JSON con HTML entities escapadas; data-chart-options idem.
CHART_BLOCK_RE = re.compile(
    r'data-chart-data="(\[.+?\])"\s+data-chart-options="(\{.+?\})"'
)

# Series.label de LG: "Average Bronze Top" / "Average Master Jungle" / etc.
SERIES_LABEL_RE = re.compile(
    r"^Average\s+(?P<tier>[A-Za-z]+)\s+(?P<role>.+)$"
)

# Regex para charts curvilineos (tabs farmingData / fightingData /
# visionData / objectivesData). Cada chart aparece como:
#
#   <h3 class="graph-title ...">{TITLE}</h3>
#   ...
#   <script ...>
#     ...
#     var datasetsgraph<id> = {
#         "Average Bronze Top": { label: "...", data: [[t,v],[t,v],...], ... },
#         "Average Silver Top": { ... },
#         ...
#         "Manuchito#LAS":      { ... }
#     };
#     ...
#   </script>
CURVE_BLOCK_RE = re.compile(
    r'<h3 class="graph-title[^"]*">([^<]+)</h3>'
    r'.*?datasetsgraph[A-Za-z0-9]+\s*=\s*\{(.*?)\};',
    re.S,
)
CURVE_SERIES_RE = re.compile(
    r'"([^"]+)"\s*:\s*\{[^}]*?data:\s*(\[\[.*?\]\])', re.S,
)
CURVE_PAIR_RE = re.compile(r"\[([\d.]+),([\d.eE+-]+)\]")

# Titulos exactos de los charts curvilineos que nos interesan.
CURVE_TITLE_MINIONS = "Minions killed"
CURVE_TITLE_KA = "Kills + Assists"
CURVE_TITLE_DEATHS = "Deaths"

# Regex para tablas de baseline-por-rango con barras de progreso.
# Estructura tipica:
#
#   <table class="data_table">
#     <tr ...><th colspan="3">Vision Score / minute</th></tr>
#     <tr>
#       <td>...<img alt="Bronze" .../>...</td>
#       <td>Bronze</td>
#       <td><progressBar data-value="0.6575..."data-minValue="0"... /></td>
#     </tr>
#     ...
#   </table>
#
# Notar que `<progressBar>` no tiene espacio entre atributos en el HTML
# original (no es HTML valido pero los browsers lo parsean).
PROGRESS_TABLE_RE_TEMPLATE = (
    r'<table\s+class="data_table">\s*<tr[^>]*>\s*<th[^>]*colspan="\d+"[^>]*>'
    r'\s*{title}\s*</th>(.*?)</table>'
)
PROGRESS_TABLE_ROW_RE = re.compile(r'<tr[^>]*>(.*?)</tr>', re.S)
PROGRESS_TIER_RE = re.compile(r'alt="(\w+)"')
PROGRESS_VALUE_RE = re.compile(r'<progressBar[^>]*data-value="([^"]+)"')

# Titulo de la tabla que contiene Vision Score / minute por rango.
PROGRESS_TITLE_VSPM = "Vision Score / minute"


@dataclass(frozen=True)
class LGSeries:
    """Baselines de un (tier, role) extraidos del HTML de LG.

    Combina datos del radar chart (5 metricas siempre presentes) y de los
    charts curvilineos (4 metricas opcionales, dependen de que el HTML
    tenga las tabs farmingData/fightingData visibles).
    """

    label: str
    tier_json: str | None  # None si es el jugador
    role_internal: str | None  # None si es el jugador
    # Del radar chart
    gold_per_min: float
    cs_per_min: float
    kp: float
    ka_per_min: float
    dpm: float
    # De las curvas (opcionales: pueden ser None si la tab no esta)
    cs10: float | None = None
    cs15: float | None = None
    late_kda: float | None = None
    takedowns_first_14: float | None = None
    # De las tablas con progressBars (opcionales)
    vspm: float | None = None


def role_from_filename(path: Path) -> str | None:
    """Intenta deducir el rol desde el filename (ej: `manu_top.html` -> TOP)."""
    stem = path.stem.lower()
    # Buscar token al final separado por _ o -.
    parts = re.split(r"[_\-]", stem)
    for token in reversed(parts):
        if token in ROLE_ALIASES:
            return ROLE_ALIASES[token]
    # Como fallback, scan de la string completa.
    for alias, role in ROLE_ALIASES.items():
        if re.search(rf"(?:^|[_\-]){re.escape(alias)}(?:$|[_\-])", stem):
            return role
    return None


def parse_axis_labels(opts_json: dict) -> list[str]:
    return list(opts_json.get("axis", {}).get("labels", []))


def axis_labels_match(labels: list[str]) -> bool:
    if len(labels) != len(EXPECTED_AXIS_PREFIXES):
        return False
    for got, expected in zip(labels, EXPECTED_AXIS_PREFIXES):
        if not got.startswith(expected):
            return False
    return True


def parse_series(series: dict) -> LGSeries | None:
    """Convierte un dict de series del chart en LGSeries (o None si no aplica)."""
    label = series.get("label", "").strip()
    data = series.get("data") or []
    if len(data) < 5:
        return None
    try:
        gpm = float(data[IDX_GOLD_PER_MIN])
        cspm = float(data[IDX_CS_PER_MIN])
        kp = float(data[IDX_KP])
        kapm = float(data[IDX_KA_PER_MIN])
        dpm = float(data[IDX_DPM])
    except (TypeError, ValueError):
        return None

    tier_json: str | None = None
    role_internal: str | None = None
    m = SERIES_LABEL_RE.match(label)
    if m:
        tier_raw = m.group("tier").strip().capitalize()
        role_raw = m.group("role").strip().lower()
        tier_json = TIER_LG_TO_JSON.get(tier_raw)
        role_internal = ROLE_ALIASES.get(role_raw)
        # Si no podemos mapear, descartamos esta serie.
        if not tier_json or not role_internal:
            return None

    return LGSeries(
        label=label,
        tier_json=tier_json,
        role_internal=role_internal,
        gold_per_min=gpm,
        cs_per_min=cspm,
        kp=kp,
        ka_per_min=kapm,
        dpm=dpm,
    )


def _series_label_to_tier(label: str, role_internal: str) -> str | None:
    """Convierte un label como 'Average Diamond Top' en el tier_json ('diamond').

    Devuelve None si el label no es un 'Average <tier> <role>' del rol pedido
    (ej. 'Manuchito#LAS' o un label de otro rol).
    """
    m = SERIES_LABEL_RE.match(label)
    if not m:
        return None
    tier_raw = m.group("tier").strip().capitalize()
    role_raw = m.group("role").strip().lower()
    tier_json = TIER_LG_TO_JSON.get(tier_raw)
    role_check = ROLE_ALIASES.get(role_raw)
    if not tier_json or role_check != role_internal:
        return None
    return tier_json


def parse_curve_charts(raw_html: str) -> dict[str, dict[str, dict[int, float]]]:
    """Extrae todos los charts curvilineos del HTML.

    Devuelve {chart_title: {series_label: {minute: value}}}.

    Cada chart tiene 7 series 'Average <tier> <role>' + 1 'Manuchito#LAS' (o
    el nombre del jugador). Los timestamps son enteros (0, 2, 3, 4, 5, 7,
    10, 15, 20, 25, 30 en los HTMLs probados).
    """
    out: dict[str, dict[str, dict[int, float]]] = {}
    for title, body in CURVE_BLOCK_RE.findall(raw_html):
        title = title.strip()
        series_map: dict[str, dict[int, float]] = {}
        for s in CURVE_SERIES_RE.finditer(body):
            label = s.group(1)
            pairs_str = s.group(2)
            points: dict[int, float] = {}
            for t_str, v_str in CURVE_PAIR_RE.findall(pairs_str):
                try:
                    t = int(float(t_str))
                    v = float(v_str)
                except ValueError:
                    continue
                points[t] = v
            if points:
                series_map[label] = points
        if series_map:
            # Si por algun motivo un titulo se repite, conservamos el primero.
            out.setdefault(title, series_map)
    return out


def parse_progress_table(raw_html: str, table_title: str) -> dict[str, float]:
    """Parsea una tabla de baseline-por-rango con `<progressBar data-value=...>`.

    Devuelve {tier_json: value}. Solo incluye tiers presentes en la tabla
    (LG omite tiers con sample chico). Si la tabla no existe en el HTML,
    devuelve dict vacio.
    """
    pattern = PROGRESS_TABLE_RE_TEMPLATE.format(title=re.escape(table_title))
    m = re.search(pattern, raw_html, re.S)
    if not m:
        return {}
    body = m.group(1)

    out: dict[str, float] = {}
    for row_m in PROGRESS_TABLE_ROW_RE.finditer(body):
        row = row_m.group(1)
        tier_m = PROGRESS_TIER_RE.search(row)
        val_m = PROGRESS_VALUE_RE.search(row)
        if not tier_m or not val_m:
            continue
        tier_raw = tier_m.group(1).strip().capitalize()
        tier_json = TIER_LG_TO_JSON.get(tier_raw)
        if not tier_json:
            continue
        try:
            out[tier_json] = float(val_m.group(1))
        except ValueError:
            continue
    return out


def derive_curve_metrics(
    curves: dict[str, dict[str, dict[int, float]]],
    role_internal: str,
) -> dict[str, dict[str, float]]:
    """A partir de los charts curvilineos, deriva las 4 metricas suplementarias.

    Devuelve {tier_json: {metric: value}} con las metricas que pudieron
    calcularse. Si un chart o un timestamp falta, esa metrica no se incluye
    para ese tier.

    Metricas derivadas:
        - cs10 = Minions killed @ t=10
        - cs15 = Minions killed @ t=15
        - late_kda = (K+A @ t=30) / max(Deaths @ t=30, 1)
        - takedowns_first_14 = K+A interpolado linealmente entre @t=10 y @t=15
    """
    minions = curves.get(CURVE_TITLE_MINIONS, {})
    ka = curves.get(CURVE_TITLE_KA, {})
    deaths = curves.get(CURVE_TITLE_DEATHS, {})

    # Recolectar tier -> metrica desde cada chart relevante.
    out: dict[str, dict[str, float]] = {}

    def _by_tier(series_map: dict[str, dict[int, float]]) -> dict[str, dict[int, float]]:
        result: dict[str, dict[int, float]] = {}
        for label, points in series_map.items():
            tier = _series_label_to_tier(label, role_internal)
            if tier is None:
                continue
            result[tier] = points
        return result

    minions_by_tier = _by_tier(minions)
    ka_by_tier = _by_tier(ka)
    deaths_by_tier = _by_tier(deaths)

    all_tiers = (
        set(minions_by_tier) | set(ka_by_tier) | set(deaths_by_tier)
    )
    for tier in all_tiers:
        metrics: dict[str, float] = {}

        cs_pts = minions_by_tier.get(tier, {})
        if 10 in cs_pts:
            metrics["cs10"] = cs_pts[10]
        if 15 in cs_pts:
            metrics["cs15"] = cs_pts[15]

        ka_pts = ka_by_tier.get(tier, {})
        deaths_pts = deaths_by_tier.get(tier, {})

        if 10 in ka_pts and 15 in ka_pts:
            # Interpolacion lineal a t=14 (mas cercano al challenge
            # takedownsFirstXMinutes con X=14).
            ka10 = ka_pts[10]
            ka15 = ka_pts[15]
            metrics["takedowns_first_14"] = ka10 + 0.8 * (ka15 - ka10)

        if 30 in ka_pts and 30 in deaths_pts:
            d30 = deaths_pts[30]
            metrics["late_kda"] = ka_pts[30] / max(d30, 1.0)

        if metrics:
            out[tier] = metrics

    return out


def parse_html_file(path: Path, role_override: str | None) -> tuple[str, list[LGSeries]]:
    """Lee un HTML, devuelve (role_internal, lista_de_baselines).

    El jugador se omite del resultado: solo nos quedamos con las series
    `Average <tier> <role>`. Combina datos del radar chart (5 metricas
    siempre presentes) y de las curvas temporales (4 metricas adicionales
    cuando estan visibles las tabs farmingData/fightingData).
    """
    raw = path.read_text(encoding="utf-8", errors="replace")

    # Detectar rol (override > filename).
    role_detected = role_override or role_from_filename(path)
    if role_detected is None:
        raise ValueError(
            f"{path.name}: no pude deducir el rol del filename. "
            f"Renombralo (ej: <algo>_top.html) o pasá --role."
        )

    blocks = CHART_BLOCK_RE.findall(raw)
    if not blocks:
        raise ValueError(
            f"{path.name}: no encontré ningún chart radar (data-chart-data). "
            f"¿Guardaste la página correcta y completa?"
        )

    baselines: dict[str, LGSeries] = {}
    valid_charts = 0
    for data_raw, opts_raw in blocks:
        try:
            data_json = json.loads(html_module.unescape(data_raw))
            opts_json = json.loads(html_module.unescape(opts_raw))
        except json.JSONDecodeError:
            continue

        labels = parse_axis_labels(opts_json)
        if not axis_labels_match(labels):
            # Probablemente es otro chart (por ejemplo, evolución temporal).
            continue
        valid_charts += 1

        for s in data_json:
            parsed = parse_series(s)
            if parsed is None or parsed.tier_json is None:
                continue
            # Sólo nos quedamos con series cuyo rol coincide con el detectado.
            if parsed.role_internal != role_detected:
                continue
            # Si por algún motivo se repite un tier en varios charts, el último
            # gana (igual deberían ser idénticos en valor).
            baselines[parsed.tier_json] = parsed

    if not baselines:
        raise ValueError(
            f"{path.name}: encontré {valid_charts} radar charts compatibles, "
            f"pero ninguno con series para el rol {role_detected}. "
            f"¿Guardaste el perfil del rol correcto?"
        )

    # Mergear metricas derivadas de las curvas (cs10/cs15/late_kda/
    # takedowns_first_14) y de las tablas de progressBars (vspm). Si las
    # tabs no estan en el HTML, simplemente no se agrega nada (los campos
    # quedan en None, lo que el caller trata como "sin override").
    curves = parse_curve_charts(raw)
    curve_metrics = derive_curve_metrics(curves, role_detected)
    vspm_by_tier = parse_progress_table(raw, PROGRESS_TITLE_VSPM)
    enriched: dict[str, LGSeries] = {}
    for tier, series in baselines.items():
        cm = curve_metrics.get(tier, {})
        enriched[tier] = LGSeries(
            label=series.label,
            tier_json=series.tier_json,
            role_internal=series.role_internal,
            gold_per_min=series.gold_per_min,
            cs_per_min=series.cs_per_min,
            kp=series.kp,
            ka_per_min=series.ka_per_min,
            dpm=series.dpm,
            cs10=cm.get("cs10"),
            cs15=cm.get("cs15"),
            late_kda=cm.get("late_kda"),
            takedowns_first_14=cm.get("takedowns_first_14"),
            vspm=vspm_by_tier.get(tier),
        )

    return role_detected, list(enriched.values())


def load_baselines(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_baselines(path: Path, data: dict) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    path.write_text(text + "\n", encoding="utf-8")


def update_metrics_for_role(
    baselines: dict,
    role_internal: str,
    series_per_tier: list[LGSeries],
) -> list[tuple[str, str, str, float, float]]:
    """Aplica overrides al dict baselines in-place. Devuelve lista de cambios:
    (tier, role, metric, old, new). `old` es None (representado como NaN-like)
    cuando es una key nueva.
    """
    ranks = baselines.setdefault("ranks", {})
    changes: list[tuple[str, str, str, float, float]] = []

    for series in series_per_tier:
        tier_key = series.tier_json
        assert tier_key is not None  # filtrado en parse_series
        tier_block = ranks.setdefault(tier_key, {})
        role_block = tier_block.setdefault(role_internal, {})

        # Metricas siempre presentes (radar) + opcionales (curvas/tablas).
        new_values: dict[str, float | None] = {
            "kp": series.kp,
            "dpm": series.dpm,
            "gold_per_min": series.gold_per_min,
            "cs_per_min": series.cs_per_min,
            "kills_assists_per_min": series.ka_per_min,
            "cs10": series.cs10,
            "cs15": series.cs15,
            "late_kda": series.late_kda,
            "takedowns_first_14": series.takedowns_first_14,
            "vspm": series.vspm,
        }
        for metric, new_val in new_values.items():
            # Si el HTML no incluyo la tab necesaria para esta metrica, no
            # hay valor nuevo; respetamos el valor previo (sea cual sea).
            if new_val is None:
                continue

            # Redondeo razonable según escala.
            if metric in ("dpm", "gold_per_min"):
                rounded = round(new_val, 1)
            elif metric == "cs_per_min":
                rounded = round(new_val, 2)
            elif metric in ("kp", "kills_assists_per_min"):
                rounded = round(new_val, 3)
            elif metric in ("cs10", "cs15"):
                rounded = round(new_val, 1)
            elif metric in ("late_kda", "takedowns_first_14", "vspm"):
                rounded = round(new_val, 2)
            else:
                rounded = round(new_val, 3)

            old_val = role_block.get(metric)
            old_is_set = old_val is not None
            if not old_is_set or abs(float(old_val) - rounded) > 1e-6:
                role_block[metric] = rounded
                changes.append((tier_key, role_internal, metric, old_val, rounded))

    return changes


def update_meta(baselines: dict, processed_files: list[Path]) -> None:
    """Actualiza el bloque `_meta` con la lista de HTMLs que se parsearon.

    Las descripciones de metricas y las notas son curadas a mano en el JSON;
    no las tocamos desde aca para evitar duplicar texto en cada corrida.
    """
    meta = baselines.setdefault("_meta", {})
    meta["lg_sources"] = sorted(p.name for p in processed_files)


def format_change(change: tuple[str, str, str, float, float]) -> str:
    tier, role, metric, old, new = change
    if old is None:
        return f"  + {tier:<11s} {role:<7s} {metric:<22s} = {new}"
    return f"  ~ {tier:<11s} {role:<7s} {metric:<22s} {old} -> {new}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--baselines",
        type=Path,
        default=DEFAULT_BASELINES,
        help="Path al baselines.json a actualizar (default: data/baselines.json).",
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=DEFAULT_RAW_DIR,
        help="Directorio con los HTML descargados (default: data/raw).",
    )
    parser.add_argument(
        "--role",
        default=None,
        help="Override del rol para todos los HTML procesados (TOP/JUNGLE/MIDDLE/BOTTOM/UTILITY).",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        default=None,
        help="Si se pasa, solo procesa estos archivos (relativos a --raw-dir).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Muestra los cambios pero no escribe baselines.json.",
    )
    args = parser.parse_args(argv)

    if not args.baselines.exists():
        print(f"ERROR: no existe {args.baselines}", file=sys.stderr)
        return 2
    if not args.raw_dir.exists():
        print(f"ERROR: no existe {args.raw_dir}", file=sys.stderr)
        return 2

    role_override: str | None = None
    if args.role is not None:
        role_override = ROLE_ALIASES.get(args.role.strip().lower()) or (
            args.role.strip().upper() if args.role.strip().upper() in INTERNAL_ROLES else None
        )
        if role_override is None:
            print(
                f"ERROR: --role {args.role!r} no es reconocido. "
                f"Usá uno de: {sorted(set(ROLE_ALIASES.values()))}",
                file=sys.stderr,
            )
            return 2

    if args.only:
        html_paths = [args.raw_dir / name for name in args.only]
        for p in html_paths:
            if not p.exists():
                print(f"ERROR: no existe {p}", file=sys.stderr)
                return 2
    else:
        html_paths = sorted(args.raw_dir.glob("*.html"))

    if not html_paths:
        print(f"ERROR: no hay archivos *.html en {args.raw_dir}", file=sys.stderr)
        return 2

    baselines = load_baselines(args.baselines)
    all_changes: list[tuple[str, str, str, float, float]] = []
    processed: list[Path] = []
    per_role_summary: list[tuple[Path, str, int]] = []

    for path in html_paths:
        try:
            role, series = parse_html_file(path, role_override)
        except ValueError as exc:
            print(f"WARN: {exc}", file=sys.stderr)
            continue

        changes = update_metrics_for_role(baselines, role, series)
        per_role_summary.append((path, role, len(series)))
        all_changes.extend(changes)
        processed.append(path)

    if not processed:
        print("ERROR: ningún HTML pudo ser procesado.", file=sys.stderr)
        return 1

    print("Procesados:")
    for path, role, n in per_role_summary:
        print(f"  {path.name:<40s} -> {role:<7s} ({n} rangos)")

    if all_changes:
        print(f"\nCambios ({len(all_changes)}):")
        for ch in all_changes:
            print(format_change(ch))
    else:
        print("\nSin cambios.")

    if args.dry_run:
        print("\n[dry-run] No escribí baselines.json.")
        return 0

    update_meta(baselines, processed)
    save_baselines(args.baselines, baselines)
    print(f"\nbaselines.json actualizado en {args.baselines}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
