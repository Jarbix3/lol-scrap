# LoL Player Scraper

Script en Python que extrae el historial de un jugador de League of Legends desde la **Riot API oficial**, calcula analytics determinísticos (champion pool, sinergias, matchups, playstyle por timeline) y genera un **reporte Markdown estructurado** pensado para que **Cursor lo interprete como coach**.

> Idea clave: el script no llama a ningún LLM. Produce un `.md` con todos los números y, en la última sección, te deja un prompt listo para pegar en el chat de Cursor. El LLM que vos ya estás usando hace las conclusiones cualitativas.

## Qué te dice el reporte

- Resumen de rank Solo/Flex, WR global, KDA promedio, CS/min.
- **Champion pool** (top 12): games, WR, KDA, CS/m, DPM, dmg share, vision.
- Distribución y rendimiento por rol.
- **Playstyle vs baseline** (de timelines): CS@10, CS@15, gold diff @10/@15, KP%, DPM, vision/min — comparado contra valores esperados por rol.
- **Fortalezas**: campeones con ≥55% WR, mejores matchups.
- **Debilidades**: campeones con <40% WR, peores matchups, métricas bajo baseline, comparativa wins vs losses.
- **Sinergias con personas** (duo partners por PUUID, ≥5 games juntos).
- **Sinergias de campeones** (mi_champ + champ aliado, WR del combo).

## Setup

### 1. Requisitos

- Python 3.11+
- Una **Riot API key** (gratis): registrate en https://developer.riotgames.com y copiá la *Development API Key* (se renueva cada 24h, suficiente para uso personal).

### 2. Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurar la API key

```bash
cp .env.example .env
# editá .env y poné tu key real:
# RIOT_API_KEY=RGAPI-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

## Uso

```bash
# Modo multi-rol (default sin --role): genera un .md por cada rol con >=10 games
# + GLOBAL.md + _COACH_PROMPT.md (meta-prompt 360 reusable), todos en
# reports/<riot-id>/. Sobreescribe la version anterior.
python main.py "Faker#KR1" --region kr
python main.py "Manu#LAS" --region las
# -> reports/Manu-LAS/{TOP.md, JUNGLE.md, MIDDLE.md, BOTTOM.md, UTILITY.md,
#                       GLOBAL.md, _COACH_PROMPT.md}
#    (solo los roles con >=10 partidas; los demas se reportan como skipeados)

# Modo single-rol (con --role): un solo .md con stats avanzadas Riot challenges
# de ese rol (secciones 6 + 6.1).
python main.py "Manu#LAS" --region las --role top
python main.py "Manu#LAS" --region las --role jungle
python main.py "Manu#LAS" --region las --role sup --out coach_analysis.md

python main.py "MiNick#1234" --region las --queues 420 --count 50
python main.py "MiNick#1234" --region las --no-timeline   # mas rapido sin metricas @10/@15
```

### Análisis 360° automatizado (modo multi-rol → meta-prompt)

Cuando corrés sin `--role`, además de los `.md` por línea, el script genera un **meta-prompt** (`_COACH_PROMPT.md`) que automatiza el análisis cross-role completo:

1. Corré: `python main.py "Manu#LAS" --region las` → se crea `reports/Manu-LAS/` con todos los `.md` de datos + `_COACH_PROMPT.md`.
2. Abrí `reports/Manu-LAS/_COACH_PROMPT.md` en Cursor.
3. Copiá su contenido al chat de Cursor (con la carpeta del jugador en el explorer).
4. El LLM lee los archivos referenciados (`GLOBAL.md`, `TOP.md`, `MIDDLE.md`, etc.) y genera un único archivo `reports/Manu-LAS/COACH_ANALYSIS.md` con **N+1 secciones** (overview cross-role + una por cada rol con datos suficientes).

El meta-prompt incluye:
- **Sección 1 — Overview Cross-Role**: identificación del rol natural, comparativa entre roles, sinergias humanas globales, patrones cruzados de fortalezas/debilidades, recomendación estratégica de priorización.
- **Secciones 2-N — Coach senior por rol**: usa los prompts rol-específicos de `lol_scrap/prompts.py` (las 3-4 dimensiones críticas + scores 1-5 + fortalezas/debilidades + acciones + fases + matchups + pool ideal + conclusión), con una **sub-sección extra "Conexión con GLOBAL"** que cruza las métricas del rol con el promedio cross-role.
- **6 reglas globales** que aplican a todas las secciones: regla de oro (no inventar), evidencia (citar archivo + sección), cross-check entre archivos, extensión + estadística (≥800 palabras por sección de rol), declarar samples chicos, sub-sección "Conexión con GLOBAL" obligatoria.

### Flags

| Flag | Default | Descripción |
|---|---|---|
| `riot_id` (posicional) | — | `Nombre#TAG` (Riot ID, no summoner name) |
| `--region` | requerido | Alias (`las`, `lan`, `br`, `na`, `euw`, `eune`, `kr`, `jp`, `oce`...) o platform ID (`la2`, `la1`, `na1`, `euw1`, `kr`...) |
| `--queues` | `420,440` | Colas separadas por coma. 420 = Ranked Solo/Duo, 440 = Ranked Flex, 400 = Normal Draft, 450 = ARAM |
| `--count` | `100` | Partidas a pedir **por cada cola** |
| `--out` | con `--role`: `reports/<riot-id>_<role>_<ts>.md`<br>sin `--role`: `reports/<riot-id>/` (carpeta) | Con `--role`: ruta del .md. Sin `--role`: carpeta destino del modo multi-rol. |
| `--no-cache` | off | Re-fetchea todo aunque esté cacheado |
| `--no-timeline` | off | Saltea timelines (más rápido pero sin CS@10/gold diff) |
| `--cache-dir` | `cache/` | Directorio del cache local |
| `--role` | (sin flag → modo multi) | **Con flag** (`top`/`jungle`/`mid`/`bot`/`sup` o canonical TOP/JUNGLE/MIDDLE/BOTTOM/UTILITY): genera **un solo .md** filtrado al rol con la sección 6 (Riot challenges específicas) + 6.1 (análisis cruzado). **Sin flag**: entra en **modo multi-rol** — genera un .md por cada rol con ≥10 partidas + un `GLOBAL.md` (overview cross-role), todos en `reports/<riot-id>/` (sobreescribe la versión anterior). |
| `--rank` | auto-detect del Solo/Duo del jugador (fallback Flex y luego `default`) | Tier contra el cual comparar baselines: `iron`, `bronze`, `silver`, `gold`, `platinum`, `emerald`, `diamond`, `master`, `grandmaster`, `challenger`, `default`. Los valores se cargan desde `data/baselines.json` y son **editables**. |

### Baselines configurables (`data/baselines.json`)

Las métricas vs baseline (sección 4 — Playstyle, sección 5 — Análisis por fase) usan **targets parametrizados por rank**, leídos de `data/baselines.json`. Cada combinación `tier × rol` puede definir:

- `cs10`, `cs15`, `kp`, `vspm`, `dpm` — usados por sección 4 y por mid/early de sección 5.
- `takedowns_first_14`, `objectives_per_game` — usados por early/mid de sección 5.
- `late_kda`, `late_team_dmg_share` — usados por late de sección 5.
- `gold_per_min`, `cs_per_min`, `kills_assists_per_min` — keys auxiliares (de leagueofgraphs); informativas para el LLM y ediciones manuales.

#### Política de `null`: el JSON solo tiene datos confiables

Cualquier métrica con valor `null` en el JSON se trata como **"no disponible"**: el código simplemente la **omite del cálculo** (no se computa score, no se muestra delta, ni se promedia con otras). Esto es intencional: preferimos un análisis incompleto pero honesto antes que uno completo con baselines fabricados.

El JSON se separa en dos grupos de métricas:

| Grupo | Métricas | Cómo se llenan |
|---|---|---|
| **`lg_confirmed_metrics`** (10) | `kp`, `dpm`, `gold_per_min`, `cs_per_min`, `kills_assists_per_min` (del radar chart) + `cs10`, `cs15`, `late_kda`, `takedowns_first_14` (de las curvas temporales en `farmingData`/`fightingData`) + `vspm` (de la tabla `Vision Score / minute` en `visionData`) | Auto, vía `tools/parse_lg_html.py` |
| **`manually_filled_metrics`** (2) | `objectives_per_game`, `late_team_dmg_share` | A mano: arrancan en `null`, completalas cuando tengas data confiable |

El bucket `iron`, todos los roles que aún no procesaste con LG, y `default` arrancan **completamente en `null`**. A medida que vas guardando HTMLs de leagueofgraphs y corriendo el parser (ver siguiente sub-sección), se van llenando los 10 valores LG; los 2 manuales los completás vos editando el JSON cuando consigas data confiable (otras páginas, papers, datos propios, etc.).

**Notas de cálculo de las métricas derivadas**:

- `cs10`, `cs15`: valor exacto de la curva *Minions killed* a `t=10` y `t=15`.
- `vspm`: valor exacto de la tabla *Vision Score / minute* (no es un proxy: es el visionScore promedio del rango, dividido por la duración promedio).
- `late_kda`: `(K+A @ t=30) / max(Deaths @ t=30, 1)` sobre el promedio del rango. Curiosamente es **casi constante entre rangos** (~1.75-1.86) porque el juego balancea kills/deaths simétricamente en agregados grandes.
- `takedowns_first_14`: interpolación lineal entre `K+A @ t=10` y `K+A @ t=15` evaluada en `t=14` (LG no expone exactamente t=14, pero la tasa entre 10 y 15 es ~lineal).
- Las 2 métricas que quedan en `null` LG no las publica de forma 1:1 con la semántica Riot:
  - `objectives_per_game`: la métrica Riot cuenta `dragonTakedowns + riftHeraldTakedowns + baronTakedowns` **del jugador**. LG da kills **del equipo** + ratios derivados (`Buildings killed with Rift Herald`, `Buildings killed with baron buff`), pero mezclar ambas semánticas genera ruido.
  - `late_team_dmg_share`: LG solo expone damage del jugador, no del equipo, así que no podemos derivar el porcentaje.

El flag `--rank` te deja **forzar el tier** contra el que se compara; sin flag, el script auto-detecta del rank Solo/Duo del jugador (cae a Flex y luego a `default`). `MASTER`, `GRANDMASTER` y `CHALLENGER` se agrupan bajo el bucket `master_plus` (samples chicos y stats similares).

#### Refrescar baselines desde leagueofgraphs.com

Los valores de `kp`, `dpm`, `cs_per_min`, `gold_per_min` y `kills_assists_per_min` se pueden actualizar con datos reales de [leagueofgraphs.com](https://www.leagueofgraphs.com), que publica promedios por rango (Bronze..Master+) y rol. Como LG usa Cloudflare y bloquea scraping automatizado, el flujo es **manual pero rápido** y se hace **una vez por trimestre** aprox:

1. Abrí en tu browser una URL como (cambiá región/jugador/rol):

   ```
   https://www.leagueofgraphs.com/summoner/champions/las/Manuchito-LAS/top
   https://www.leagueofgraphs.com/summoner/champions/las/Manuchito-LAS/jungle
   https://www.leagueofgraphs.com/summoner/champions/las/Manuchito-LAS/middle
   https://www.leagueofgraphs.com/summoner/champions/las/Manuchito-LAS/adc
   https://www.leagueofgraphs.com/summoner/champions/las/Manuchito-LAS/support
   ```

   No hace falta que el jugador sea el tuyo: alcanza con que tenga partidas suficientes en ese rol; lo único que nos importa son los baselines del radar chart, no las stats personales del jugador.

2. Esperá a que cargue el radar chart (ese que compara al jugador vs "Average X Tier"). Guardá la página con `Ctrl+S` -> "Webpage, HTML only" en `data/raw/` con un nombre que termine con el rol:

   ```
   data/raw/manuchito_top.html
   data/raw/manuchito_jungle.html
   data/raw/manuchito_mid.html
   data/raw/manuchito_bot.html
   data/raw/manuchito_sup.html
   ```

   El parser deduce el rol del filename (también acepta `--role` como override).

3. Corré el parser:

   ```bash
   python tools/parse_lg_html.py --dry-run   # preview
   python tools/parse_lg_html.py             # aplica
   ```

   El script:
   - Lee TODOS los `data/raw/*.html`.
   - Extrae los baselines de los 7 rangos cubiertos (Bronze, Silver, Gold, Platinum, Emerald, Diamond, Master+) para el rol de cada archivo.
   - Sobrescribe las **10 métricas LG-confirmed**: 5 del radar chart, 4 derivadas de las curvas temporales, y `vspm` de la tabla en la tab `visionData`.
   - **NO** toca `objectives_per_game` ni `late_team_dmg_share` (LG no las publica de forma 1:1; quedan en `null` o con el valor que vos hayas puesto a mano).
   - **NO** toca el bucket `iron` (LG no lo expone) ni `default`.

   Es idempotente: corrés el script de nuevo sin haber cambiado nada y dice "Sin cambios".

4. Re-corré `python main.py ...` para regenerar reportes con baselines actualizados. Los HTMLs de `data/raw/*.html` están en `.gitignore` (puede haber info personal del jugador en ellos).

### Exportar el reporte a PDF (opcional)

Hay un tool aparte que toma un `.md` (típicamente la respuesta del coach pegada en otro `.md`) y lo renderiza como PDF estilizado:

```bash
python _build_coach_pdf.py reports/MiNick-LAS_<ts>_coach.md
# genera reports/MiNick-LAS_<ts>_coach.pdf
```

Requiere `markdown` y `weasyprint` (ya están en `requirements.txt`). En Linux, `weasyprint` necesita `libpango`, `libcairo` y `libgdk-pixbuf` instalados a nivel de sistema (en Arch suelen venir con el escritorio; si no, `pacman -S pango cairo gdk-pixbuf2`).

### Cómo se interpreta el reporte (paso clave)

1. Abrí el `.md` generado en Cursor (`reports/...`).
2. Abrí el chat de Cursor (`Cmd/Ctrl+L`) **con ese archivo abierto**.
3. Pegá el prompt que hay al final del reporte (sección 9). Algo como:

   > Actuá como un coach senior de League of Legends. Basándote exclusivamente en el reporte de arriba, dame:
   > 1. 5 fortalezas, 2. 5 puntos a mejorar, 3. 3 acciones concretas para la próxima semana, 4. champion pool recomendado, 5. mejor duo recomendado.
   > No inventes datos: si algo no está en el reporte, decí "insuficientes datos".

   Cursor (con Claude/GPT detrás) te devuelve un coaching personalizado **gratis y sin SDKs externos**.

## Arquitectura

```
lol-scrap/
├── main.py                       # CLI entrypoint (argparse + pipeline)
├── tools/
│   └── parse_lg_html.py          # Refresca baselines.json desde HTMLs de leagueofgraphs
├── data/
│   ├── baselines.json            # Targets por tier × rol × métrica (EDITABLE)
│   └── raw/                      # HTMLs de leagueofgraphs (gitignored, fuente de baselines)
├── lol_scrap/
│   ├── config.py                 # Routing platform↔regional, queues, loader de baselines
│   ├── riot_client.py            # Wrapper Riot API + rate limiter + retries
│   ├── cache.py                  # JSON local por matchId
│   ├── fetcher.py                # riot_id → puuid → matchIds → matches+timelines
│   ├── report.py                 # Genera el .md final
│   └── analytics/
│       ├── _helpers.py
│       ├── champion_pool.py      # WR/KDA/dmg share por campeón
│       ├── roles.py              # rendimiento por rol
│       ├── playstyle.py          # CS@10/15, gold diff, KP, DPM (de timelines)
│       ├── game_phases.py        # Scores 1-10 early/mid/late vs baselines
│       ├── role_advanced.py      # Stats Riot challenges específicas por rol (con --role)
│       ├── ally_champions.py     # WR cuando un campeón está en mi equipo
│       ├── team_comps.py         # Drafts repetidos de 5 campeones
│       ├── synergies.py          # duo partners + combos aliados
│       ├── matchups.py           # WR vs oponente directo
│       └── weaknesses.py         # champs WR bajo, métricas bajo baseline, patrones
├── cache/                        # JSON cache (gitignored)
└── reports/                      # outputs .md (gitignored)
```

## Cache

Las partidas de Riot son inmutables, así que se guardan en `cache/matches/{matchId}.json` y `cache/timelines/{matchId}.json`. Re-correr el script sobre el mismo jugador es prácticamente instantáneo. Para ignorar el cache, usá `--no-cache`.

## Rate limits

La key de development tiene 20 req/s y 100 req/2min. El script implementa un rate limiter en memoria que respeta ambas ventanas, y reintenta con backoff exponencial en `429` y `5xx` (respetando `Retry-After`). 100 partidas con timeline tardan ~3-5 min la primera vez; ejecuciones siguientes son segundos gracias al cache.

## Limitaciones

- Riot deprecó los summoner names: hay que usar **Riot ID** (`Nombre#TAG`).
- Las "duo partners" se infieren por aparecer en el mismo equipo varias veces; si jugás solo en SoloQ no hay duos por definición.
- Los baselines de `data/baselines.json` se refrescan **manualmente** desde `leagueofgraphs.com` con `tools/parse_lg_html.py` (ver sección "Refrescar baselines"). Cloudflare impide scraping automatizado, así que el flujo es: guardás el HTML del perfil del rol → corrés el parser → JSON actualizado. Recomendado cada ~3 meses, en sync con el ciclo de patches/temporada.
- Las métricas que LG **no** publica directamente (`cs10`, `cs15`, `vspm`, `takedowns_first_14`, `objectives_per_game`, `late_kda`, `late_team_dmg_share`) viven como `null` en el JSON hasta que las completes a mano. Mientras estén en `null`, el script las omite del análisis (no fabrica targets).
- El script no analiza ARAM ni modos rotativos por defecto (podés pedirlos con `--queues 450`).
- La interpretación cualitativa (coaching) la hace Cursor, no el script.

## Troubleshooting

- **`401/403`**: tu API key venció (development keys duran 24h). Renovala en https://developer.riotgames.com.
- **`404` en account-v1**: revisá ortografía del Riot ID y región. El `#TAG` distingue cuentas con el mismo nombre.
- **Sin partidas**: probá con otra cola (`--queues 400`) o aumentá `--count`. Si el jugador no jugó ranked, no hay nada en 420/440.
- **`429` constantes**: estás compitiendo con otra herramienta que usa la misma key. Esperá unos minutos.
