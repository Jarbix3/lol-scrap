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
python main.py "Faker#KR1" --region kr
python main.py "Manu#LAS" --region las
python main.py "MiNick#1234" --region las --queues 420 --count 50
python main.py "MiNick#1234" --region las --no-timeline   # mas rapido sin metricas @10/@15
```

### Flags

| Flag | Default | Descripción |
|---|---|---|
| `riot_id` (posicional) | — | `Nombre#TAG` (Riot ID, no summoner name) |
| `--region` | requerido | Alias (`las`, `lan`, `br`, `na`, `euw`, `eune`, `kr`, `jp`, `oce`...) o platform ID (`la2`, `la1`, `na1`, `euw1`, `kr`...) |
| `--queues` | `420,440` | Colas separadas por coma. 420 = Ranked Solo/Duo, 440 = Ranked Flex, 400 = Normal Draft, 450 = ARAM |
| `--count` | `100` | Partidas a pedir **por cada cola** |
| `--out` | `reports/<riot-id>_<ts>.md` | Ruta del .md de salida |
| `--no-cache` | off | Re-fetchea todo aunque esté cacheado |
| `--no-timeline` | off | Saltea timelines (más rápido pero sin CS@10/gold diff) |
| `--cache-dir` | `cache/` | Directorio del cache local |

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
├── lol_scrap/
│   ├── config.py                 # Routing platform↔regional, queues, baselines
│   ├── riot_client.py            # Wrapper Riot API + rate limiter + retries
│   ├── cache.py                  # JSON local por matchId
│   ├── fetcher.py                # riot_id → puuid → matchIds → matches+timelines
│   ├── report.py                 # Genera el .md final
│   └── analytics/
│       ├── _helpers.py
│       ├── champion_pool.py      # WR/KDA/dmg share por campeón
│       ├── roles.py              # rendimiento por rol
│       ├── playstyle.py          # CS@10/15, gold diff, KP, DPM (de timelines)
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
- Los baselines por rol son aproximados (Emerald/Diamond promedio); no son rigurosamente por liga.
- El script no analiza ARAM ni modos rotativos por defecto (podés pedirlos con `--queues 450`).
- La interpretación cualitativa (coaching) la hace Cursor, no el script.

## Troubleshooting

- **`401/403`**: tu API key venció (development keys duran 24h). Renovala en https://developer.riotgames.com.
- **`404` en account-v1**: revisá ortografía del Riot ID y región. El `#TAG` distingue cuentas con el mismo nombre.
- **Sin partidas**: probá con otra cola (`--queues 400`) o aumentá `--count`. Si el jugador no jugó ranked, no hay nada en 420/440.
- **`429` constantes**: estás compitiendo con otra herramienta que usa la misma key. Esperá unos minutos.
