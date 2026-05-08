"""Prompts LLM para coaching del jugador, generico y rol-especificos.

El reporte agrega al final una seccion con un prompt para que el usuario lo
copie al chat de Cursor. Hay dos modalidades:

- `GENERIC_PROMPT_TEMPLATE`: 5 preguntas standard (linea, rol, mejores/peores
  champs, mejor duo, mejor duo champ). Se usa cuando NO se pasa `--role`.
- `ROLE_PROMPTS`: dict {rol -> template} con preguntas rol-especificas
  (Positioning Index para ADC, Splitpush Index para TOP, etc.). Se activa
  cuando se pasa `--role <ROL>`.

Todos los templates usan `str.format(**ctx)` con keys como `role_label`,
`advanced_section_n`, etc. — ver `_render_role_prompt()` en `report.py` para el
detalle de las keys que se inyectan.

Los prompts rol-especificos son version textual de las secciones 3.3-7.3 de
`docs/role_metrics_guide.md`. Si se actualiza la doc, conviene reflejarlo aca.
"""
from __future__ import annotations


# ============================================================
# PROMPT GENERICO (sin --role)
# ============================================================
#
# Keys requeridas: phases_section_n, advanced_section_n,
# matchups_section_n, ally_section_n, draft_section_n,
# duo_section_n, synergy_section_n, role_filter_label,
# show_advanced (bool), show_phases (bool), role_label
#
# Para mantener el formato exacto que existia antes en report.py este template
# se renderiza con un helper en report.py que decide bullets segun los flags.
# Aqui solo exponemos el "nucleo" del prompt como helper para que report.py lo
# componga linea por linea.

GENERIC_INTRO = (
    "> Actuá como coach senior de League of Legends. Basándote\n"
    "> **exclusivamente** en los datos de este reporte, respondé\n"
    "> con **una oración muy breve cada uno**:"
)

GENERIC_OUTRO = (
    "> No inventes datos: si algo no está en el reporte, decí\n"
    "> **\"insuficientes datos\"**."
)


# ============================================================
# PROMPTS ROL-ESPECIFICOS
# ============================================================
#
# Keys requeridas: role_label, advanced_section_n, phases_section_n,
# cross_section_n (sub-seccion Tier A si aplica; si no, usa
# advanced_section_n), matchups_section_n, duo_section_n.
#
# Cada prompt es un blockquote completo (lineas con `> `). Se emite tal cual al
# reporte. Si una metrica Tier S/B/A no esta en el reporte (n=0 o no aplica al
# rol), el LLM debe decir "no medido aún" — esa instruccion va en el cierre.


_TOP_PROMPT = """\
> **Rol del jugador: {role_label} (TOP)** — un coach senior de Top lane analiza
> este reporte. Las **3 dimensiones críticas** del rol son:
>
> 1. **Lane dominance** (gano el 1v1 y lo traduzco en oro/CS/plates).
> 2. **Splitpush + side-laning** (aplico presión cuando los teamfights no convienen).
> 3. **Tank value / sustain en teamfights largos** (sobrevivo y absorbo daño).
>
> Basándote **exclusivamente en los datos del reporte abierto**, hacé lo siguiente:
>
> **A) Score 1-5 por stat core** (1=Pésimo, 2=Bajo, 3=Promedio del tier,
> 4=Bueno, 5=Excelente). Para cada uno citá el número exacto del reporte:
>
> - Gold diff @ 15 vs rival (sección 4 Playstyle).
> - **Lane phase win rate (oro+exp @14')** y **Lane lead promedio @14'**
>   (sección {phases_section_n} - Early). Target: ~50% de lanes ganadas y
>   lead positivo. < 40% sugiere problemas de matchup o ejecución de lane.
> - Solo kills + quick solo kills (sección {advanced_section_n} Stats avanzadas).
> - Plates tomadas + daño a torres (sección {advanced_section_n}).
> - Daño mitigado (sección {advanced_section_n}).
> - **Splitpush Index** (sección {advanced_section_n}; si dice n=0 decí "no medido aún").
> - KDA en partidas largas (`late_kda` en sección {phases_section_n}).
>
> **B) 3 fortalezas TOP-específicas** y **3 debilidades TOP-específicas** (no
> genéricas tipo "tenés bajo KDA" — sí específicas tipo "tu Splitpush Index
> está bajo para los champs (Fiora, Camille) que esperan side-laning").
>
> **C) 3 acciones concretas para la próxima semana**, contextualizadas al rol
> Top (ej. "cuando lleves Camille con `late_kda` < 2, fuerza side-laning
> después del primer drake en lugar de regroupar").
>
> **D) Fase del juego más fuerte y más débil** (early/mid/late, según los
> scores de la sección {phases_section_n}). Citá el score y la métrica que
> más arrastra para abajo en la peor fase.
>
> **E) Mejor matchup y peor matchup** (sección {matchups_section_n}). Sugerí
> qué hacer ante el peor: ban prioritario, swap a un counter pick, o
> adaptación de runas.
>
> **F) Conclusión general en 1 oración** sintetizando A-E.
>
> **Regla de oro**: no inventes datos. Si una stat no está en el reporte,
> decí "insuficiente data".
"""


_JUNGLE_PROMPT = """\
> **Rol del jugador: {role_label} (JUNGLE)** — coach senior de Jungla.
> **4 dimensiones críticas**:
>
> 1. **Pathing efficiency** (clear rápido + tempo a level 6).
> 2. **Counter-jungle** (invade y starvea al rival).
> 3. **Gank impact** (convertís presencia en otras lanes en takedowns).
> 4. **Objective control** (drakes/herald/baron + soul rate).
>
> Basándote **exclusivamente en los datos del reporte abierto**:
>
> **A) Score 1-5 por stat core**:
>
> - Jungle CS antes del 10' (sección {advanced_section_n}).
> - **Counter-jungle ratio** (sección {advanced_section_n}; si n=0 usar el
>   ratio de los dos campos `enemyJungleMonsterKills`/`alliedJungleMonsterKills`).
> - Takedowns en otras lanes early (sección {advanced_section_n}).
> - Drakes + Heralds + Barones por partida (sección {advanced_section_n}).
> - Cobertura de control wards en río/jungla enemiga (sección {advanced_section_n}).
> - **Tempo Index** a level 6 (sección {advanced_section_n}; si n=0 decí
>   "no medido aún", requiere timelines).
> - **Soul Rate** (sección {cross_section_n} — Análisis cruzado).
> - **Gank-to-Death ratio** (sección {advanced_section_n}; si n=0 decí
>   "no medido aún").
>
> **B) 3 fortalezas JUNGLE-específicas** y **3 debilidades JUNGLE-específicas**.
> Ejemplos del estilo esperado:
>
> - "Tu jungle CS @10' (52) está debajo del Diamond baseline (58) → estás
>   pateando camps en favor de ganks, pero tu gank impact (2.1) tampoco está
>   arriba — pathing ineficiente."
> - "Vision en río baja (18%) → tus invades son ciegos y eso explica deaths
>   early."
>
> **C) 3 acciones concretas para la próxima semana**, contextualizadas al rol:
>
> - "Andá a Lee Sin/Elise sólo si vas a hacer al menos 1 invade y 2 ganks
>   antes del 8'; tu winrate con Lee sin esos comportamientos cae al X%."
> - "Comprá Sweeper desde el 8' antes de cada drake; tu vision dominance
>   se duplicaría."
>
> **D) Fase del juego más fuerte y más débil** (sección {phases_section_n}).
>
> **E) Champ pool ideal**: dado los datos, ¿qué 3 junglers maximizan tus
> fortalezas y qué 3 deberías evitar?
>
> **F) Conclusión general en 1 oración**.
>
> **Regla de oro**: no inventes datos. Si una stat no está en el reporte,
> decí "insuficiente data".
"""


_MIDDLE_PROMPT = """\
> **Rol del jugador: {role_label} (MIDDLE)** — coach senior de Mid lane.
> **4 dimensiones críticas**:
>
> 1. **Lane priority** (gano la lane y libero al jungla).
> 2. **Roam impact** (visito side lanes y abro el mapa).
> 3. **Damage output en teamfights** (% del daño del equipo).
> 4. **Snowball capacity** (aces tempranos, mejais a tiempo).
>
> Basándote **exclusivamente en los datos del reporte abierto**:
>
> **A) Score 1-5 por stat core**:
>
> - **Lane phase win rate (oro+exp @14')** y **Lane lead promedio @14'**
>   (sección {phases_section_n} - Early). Target: ~50% de partidas ganadas
>   y lead positivo. Si win rate < 40% o lead < -500, hay un problema serio
>   de laning.
> - Max CS lead + max level lead vs rival (sección {advanced_section_n}).
> - Takedowns en otras lanes / roam impact (sección {advanced_section_n}).
> - % del daño del equipo + DPM (sección {advanced_section_n}).
> - Aces antes del 15' (sección {advanced_section_n}).
> - Solo kills (sección {advanced_section_n}).
> - **Roam Conversion Rate** (sección {cross_section_n} — Análisis cruzado;
>   si n=0 decí "no medido aún").
> - **Synergy WR con Jungla** (sección {cross_section_n}; si n=0 decí
>   "no medido aún").
>
> **B) 3 fortalezas MID-específicas** y **3 debilidades MID-específicas**.
> Estilo esperado:
>
> - "Tu damagePerMinute (520) está cerca del baseline Diamond Mid (857), pero
>   tu teamDmg% es 22% — significa que pegás poco aunque tus partidas duren
>   mucho; problema de positioning/build."
> - "Roam impact (4.2) está arriba del baseline, pero tu WR en partidas con
>   3+ roams es 45% vs 62% sin roams → estás roameando en momentos malos."
>
> **C) 3 acciones concretas para la próxima semana**:
>
> - "Si llevás Syndra/Orianna, no roamees antes del minuto 8 a menos que
>   tengas ventaja de wave; estás perdiendo CS @15."
> - "Compra Hexdrinker antes que Sorcerer Boots cuando hay Zed/Talon en banda
>   enemiga — tu survivedSingleDigitHpCount sugiere que necesitás más MR
>   temprano."
>
> **D) Fase del juego más fuerte y más débil** (sección {phases_section_n}).
>
> **E) Champ pool ideal**: 3 mids que potencian tus fortalezas (si sos roamer
> agresivo → Twisted Fate, Talon, Galio; si sos farmer → Azir, Cassio, Vex)
> y 3 que debés evitar.
>
> **F) Conclusión general en 1 oración**.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí "insuficiente data".
"""


_BOTTOM_PROMPT = """\
> **Rol del jugador: {role_label} (BOTTOM/ADC)** — coach senior de ADC.
> **4 dimensiones críticas**:
>
> 1. **Sustained DPS** (DPM + % daño del equipo en teamfights).
> 2. **Positioning** (ratio damage out / damage in — la regla #1).
> 3. **Scaling** (KDA crece en partidas largas si llevás scaling carries).
> 4. **Lane priority + plates con sup** (presión bot temprana).
>
> Basándote **exclusivamente en los datos del reporte abierto**:
>
> **A) Score 1-5 por stat core**:
>
> - DPM + % del daño del equipo (sección {advanced_section_n}).
> - **Positioning Index** (sección {advanced_section_n}; target Diamond
>   ~1.0-1.4. Si n=0 decí "no medido aún" y usá `damageTaken` agregado como
>   proxy).
> - Torres antes de plates / first turret rápida (sección {advanced_section_n}).
> - Items legendarios completados por partida (sección {advanced_section_n}).
> - **Scaling Score** (sección {cross_section_n} — Análisis cruzado;
>   si n=0 comparar KDA en partidas largas vs cortas a ojo).
> - **Lane phase win rate (oro+exp @14')** y **Lane lead promedio @14'**
>   (sección {phases_section_n} - Early). Para ADC el rival directo es el
>   ADC enemigo (no el sup). Target: ~50% de partidas ganadas y lead
>   positivo. < 40% indica problema bot lane (vos + sup).
> - **Muertes antes del 25'** (sección {advanced_section_n}; si n=0 decí
>   "no medido aún").
> - **Synergy WR con Support** (sección {cross_section_n}; si n=0 decí
>   "no medido aún").
>
> **B) 3 fortalezas ADC-específicas** y **3 debilidades ADC-específicas**.
> Estilo esperado:
>
> - "Tu Positioning Index es 0.75 (target Diamond ~1.1) → estás peleando
>   con poco margen, recibís más daño del que repartís en teamfights."
> - "Llevás Vayne pero tu Scaling Score es 0.9 — estás perdiendo partidas
>   largas con un champ que se suponía favorecía late."
>
> **C) 3 acciones concretas para la próxima semana**:
>
> - "Cuando lleves Cait/Jinx, no peleés antes de Phantom Dancer + IE; mová a
>   side push si tu equipo engagea sin tu spike."
> - "Comprá Stopwatch antes de Phage si hay Malzahar/Zed; tu
>   survivedSingleDigitHpCount es bajo y morís en la primera engage."
> - "Andá a Lucian solo si tenés Nami como sup en el draft (tu mejor
>   synergy según el reporte); WR con otros sups cae al 40%."
>
> **D) Fase del juego más fuerte y más débil** (sección {phases_section_n}).
> Un ADC con Late score bajo es un sign rojo grande.
>
> **E) Champ pool ideal**: 3 ADCs que maximizan tu rendimiento y 3 que
> deberías sacar.
>
> **F) Mejor sup duo + mejor matchup vs duo enemigo + peor matchup vs duo
> enemigo** (secciones {duo_section_n} y {matchups_section_n}).
>
> **G) Conclusión general en 1 oración**.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí "insuficiente data".
"""


_UTILITY_PROMPT = """\
> **Rol del jugador: {role_label} (UTILITY/SUPPORT)** — coach senior de
> Support. **4 dimensiones críticas**:
>
> 1. **Vision** (control + dominance — el rol más responsable del mapa).
> 2. **Engage / disengage** (CC chains, saves, picks).
> 3. **Enable** (heal+shield + facilitar al ADC).
> 4. **Roam impact** (presión en otras lanes cuando bot farmea).
>
> Basándote **exclusivamente en los datos del reporte abierto**:
>
> **A) Score 1-5 por stat core**:
>
> - Vision/min + advantage vs sup rival (sección {advanced_section_n}).
> - Cobertura de control wards en río/jungla enemiga (sección {advanced_section_n}).
> - Heal+shield efectivo + saves de aliados (sección {advanced_section_n}).
> - CC sobre enemigos + picks coordinados (sección {advanced_section_n}).
> - **Vision Dominance Ratio** (sección {advanced_section_n}; si n=0 usar
>   `visionScoreAdvantage` como proxy).
> - **Roam impact** — takedowns en otras lanes (sección {advanced_section_n}).
> - Rate de quest del support item completada a tiempo (sección {advanced_section_n}).
>
> **B) 3 fortalezas SUP-específicas** y **3 debilidades SUP-específicas**.
> Identificá primero el **arquetipo del jugador** (engage / enchanter / pick)
> según los stats y luego evaluá si el champ pool y los números coinciden.
> Estilo esperado:
>
> - "Sos arquetipo engage (Leona/Naut, immobilizations 18.3) pero tu
>   pickKillWithAlly es 4.1 — el CC va a aire, tu ADC no cierra; problema
>   de comm o ADC pool."
> - "Vision/min (1.3) está debajo del baseline Diamond Sup (2.6) — no comprás
>   suficientes wards o no los tirás bien al recall."
>
> **C) 3 acciones concretas para la próxima semana**:
>
> - "Comprá control ward antes de cada drake (timer en 4:30 + intervalo 5
>   min); tu drake side vision coverage está en 12% (target 30%)."
> - "Cuando lleves Naut/Leona, ahead solo si tu ADC es Lucian/Draven/Kalista
>   (early-game ADCs); con Cait/Jinx vas a perder lane phase porque ellos
>   quieren stack pasivo."
> - "Practicá Lulu — tu ADC pool está dominado por scalers (Vayne, Jinx) y
>   tu currente sup pool no incluye enchanters fuertes."
>
> **D) Fase del juego más fuerte y más débil** (sección {phases_section_n}).
>
> **E) Mejor ADC duo + mejor matchup vs sup enemigo + peor matchup vs sup
> enemigo** (secciones {duo_section_n} y {matchups_section_n}).
>
> **F) Champ pool ideal por arquetipo**: si el jugador rinde mejor como
> engage → 3 sups engage; si como enchanter → 3 enchanters; si como pick →
> 3 picks (Pyke, Bard, Senna).
>
> **G) Conclusión general en 1 oración**.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí "insuficiente data".
"""


ROLE_PROMPTS: dict[str, str] = {
    "TOP": _TOP_PROMPT,
    "JUNGLE": _JUNGLE_PROMPT,
    "MIDDLE": _MIDDLE_PROMPT,
    "BOTTOM": _BOTTOM_PROMPT,
    "UTILITY": _UTILITY_PROMPT,
}


def render_role_prompt(role: str, **ctx: object) -> str | None:
    """Devuelve el prompt rol-especifico interpolado, o None si no hay match.

    Args:
        role: rol canonical (TOP/JUNGLE/MIDDLE/BOTTOM/UTILITY).
        **ctx: keys para `str.format()`. Las requeridas son
            `role_label`, `advanced_section_n`, `phases_section_n`,
            `cross_section_n`, `matchups_section_n`, `duo_section_n`.
            Si falta alguna, devuelve None.

    Returns:
        El prompt como string multi-linea (terminando en `\n`), listo para
        `parts.append(prompt)` en report.py. Las lineas ya empiezan con `> `.
    """
    template = ROLE_PROMPTS.get(role)
    if template is None:
        return None
    try:
        return template.format(**ctx)
    except KeyError:
        return None


# ============================================================
# META-PROMPT 360° (modo multi-rol, sin --role)
# ============================================================
#
# Cuando se corre el script SIN --role, se generan multiples .md (uno por
# rol con >=10 partidas + GLOBAL.md). El meta-prompt instruye al LLM a
# leer todos esos archivos y escribir UN solo COACH_ANALYSIS.md en el
# mismo directorio del jugador, con secciones por rol mas un overview
# cross-role como Seccion 1.
#
# Reusa los ROLE_PROMPTS existentes pero sustituye "del reporte abierto"
# por "del archivo <ROL>.md" y agrega instrucciones globales de extension,
# estadistica, cross-check y evidencia.

# Secciones fijas del MD generado por report.py (cuando hay --role):
_SEC_PLAYSTYLE = "4"
_SEC_PHASES = "5"
_SEC_ADVANCED = "6"
_SEC_CROSS = "6.1"
_SEC_MATCHUPS = "9"
_SEC_DUO_PARTNERS = "12"


_OVERVIEW_PROMPT = """\
> ## Sección 1 — Overview Cross-Role (basado en `GLOBAL.md`)
>
> Generá las siguientes sub-secciones, **citando siempre el número exacto**
> y la sección/tabla del archivo `GLOBAL.md`:
>
> **1.1 Identificación del rol natural**: tabla con WR, KDA, CS/m, DPM,
> Vision por cada rol jugado (sec. 1 — Distribución entre tus roles).
> Identificá:
>
> - Rol con mejor WR (mín. 10 partidas para validez estadística)
> - Rol con peor WR (declarar sample size)
> - Rol con mejor KDA (puede no coincidir con WR — analizar por qué)
> - Rol con mejor DPM relativo a baseline (cita el delta vs baseline del rol)
>
> **1.2 Análisis de inversión de tiempo vs WR**: ¿es el rol más jugado el
> de mejor WR? Si no, hay misalignment estratégico. Citar % de partidas
> por rol y delta WR vs el rol top. Calculá la "tasa de oportunidad
> perdida": cuántos LP estás dejando en la mesa por jugar el rol
> sub-óptimo X partidas.
>
> **1.3 Sinergias humanas globales** (sec. 12 — Sinergias con personas
> de `GLOBAL.md`): identificá del top 5:
>
> - **Mejor sinergia** (WR + sample): la palanca más rentable. Citar:
>   "X games juntos, Y% WR vs Z% baseline del jugador → +Δpp".
> - **Peor sinergia** con sample útil (≥10 games): alguien que arrastra
>   tu WR — flag para evitar/reducir.
> - Patrones por rol del aliado: ¿qué tipo de roles te potencian más
>   (mid carries, jungla cargadora, sup engage, etc.)?
>
> **1.4 Patrones cruzados de fortalezas/debilidades**: identificá métricas
> que se repiten **en TODOS los roles** comparando entre los archivos por
> rol (TOP.md, MIDDLE.md, etc.). Ej.: si CS@10 está -20% vs baseline en
> Top Y en Mid Y en ADC, es un problema **mecánico transversal**, no de
> rol específico. Mismo análisis para vision, deaths antes del 25', Lane
> phase win rate (sección 5 Early). **Cross-check obligatorio**: cita el
> valor de cada archivo.
>
> **1.5 Recomendación estratégica de priorización**: 1 párrafo de 3-5
> oraciones con evidencia numérica que diga:
>
> - Qué rol priorizar (con cuántas LP-ganancia esperada vs el rol actual).
> - Qué rol abandonar/limitar (si hay uno con WR claramente subóptimo).
> - Si hay un "rol secundario sano" para flex queue.
> - Cuál es la palanca humana más rentable (mejor duo partner).
>
> **Regla**: cada afirmación de esta sección debe tener al menos 2 números
> citados. Si la diferencia entre dos roles es <5pp WR con samples chicos
> (<15 games el menor), declarar "diferencia no estadísticamente
> significativa".
"""


_RANKING_PROMPT = """\
> ## Sección {section_n} — Ranking final + Plan de acción (Coach Jefe)
>
> Como **cierre del análisis**, sintetizá las {n_previous_sections} secciones
> previas en **dos tablas markdown** + un párrafo final del coach jefe.
> Esta sección es el TL;DR ejecutivo: si el jugador solo lee esto, debe
> entender qué rol jugar y qué atacar primero.
>
> **{section_n}.1 Ranking de roles (mejor → peor fit estratégico)**
>
> Tabla con **todos los roles analizados**, ordenados por fit estratégico
> de mejor a peor. Criterios para el ordenamiento:
>
> - WR ajustado por sample (≥10 games = peso completo, 5-9 games = peso
>   reducido y caveat explícito, <5 = al fondo con flag "sample
>   insuficiente").
> - KDA, CS/m, DPM, Vision/min relativos al baseline del rank (sec. 4
>   Playstyle de cada `<ROL>.md`).
> - Score Early/Mid/Late del game_phases (sec. 5 de cada `<ROL>.md`).
> - Stats avanzadas del rol (sec. 6 + 6.1 cuando aplique).
> - Existencia de duos rentables disponibles para ese rol (sec. 12).
>
> **Formato exacto de la tabla**:
>
> | # | Rol | Games | WR | E / M / L | Justificación (1 oración, ≤25 palabras) | Datos clave (2-3 stats con valor) |
> |---|-----|------:|---:|-----------|------------------------------------------|------------------------------------|
> | 1 | Top | 245 | 51.8% | 5.4 / 5.1 / 7.0 | Tu rol natural — late game sólido sostenido por scaling champs. | WR 51.8%, Late 7.0/10, Mordekaiser 64% WR [TOP.md sec. 5, 7] |
> | 2 | ... | ... | ...% | x.x / x.x / x.x | ... | ... |
>
> **Reglas de llenado** (estrictas):
>
> - **Justificación**: máx. 25 palabras, declarando el "por qué" del fit
>   (o de la falta de fit).
> - **Datos clave**: 2-3 métricas con valor numérico, separadas por comas.
>   Cada una citando archivo+sección entre corchetes.
> - **Orden**: roles con sample <5 partidas van al final con flag
>   "sample insuficiente"; no se les asigna ranking comparativo.
> - **Consistencia**: el orden debe ser consistente con la sec. 1.5
>   (Recomendación estratégica) del overview. Si hay conflicto, se
>   prioriza este ranking y se aclara la actualización al final.
>
> **{section_n}.2 Top 5 acciones accionables cross-role (priorizadas)**
>
> Tabla con las **5 cosas más importantes que el jugador debe atacar
> esta semana**, ordenadas por impacto esperado en LP/WR. Estas pueden
> ser técnicas (mecánica), estratégicas (champ pool, queue, duo) o de
> macro (vision, rotaciones).
>
> **Formato exacto de la tabla**:
>
> | # | Acción | Por qué (evidencia con número) | Roles afectados | Esfuerzo |
> |---|--------|--------------------------------|-----------------|----------|
> | 1 | Subir CS@10 a 70+ | CS@10 = 58 vs baseline 72 [GLOBAL.md sec. 4]; afecta 3 roles | Top, Mid, ADC | Alto |
> | 2 | ... | ... | ... | Bajo/Medio/Alto |
>
> **Reglas de llenado**:
>
> - **Acción**: imperativa y concreta (ej. "Comprá control ward antes
>   de cada drake", NO "mejorá vision").
> - **Por qué**: SIEMPRE incluir el número exacto que motiva la acción
>   y su archivo/sección. Sin número → la acción no entra en el top 5.
> - **Roles afectados**: cuáles de los roles analizados se beneficiarían
>   (puede ser "Todos" si es transversal).
> - **Esfuerzo**: Bajo (queue/champ pick/duo), Medio (mecánica
>   replicable), Alto (cambio de hábito o pool nuevo).
> - **Diversidad**: que las 5 acciones no sean todas del mismo eje
>   (ej. no las 5 sobre CS); buscá mezclar mecánica + macro + draft.
>
> **{section_n}.3 Cierre del coach jefe** (1 párrafo, 4-6 oraciones,
> ≤120 palabras)
>
> Sintetizá en prosa:
>
> 1. **Rol primario** recomendado para ranked (con LP-ganancia esperada
>    estimada en %).
> 2. **Rol secundario** sano para flex queue / fill (si lo hay).
> 3. **Rol(es) a NO tocar** en ranked (con sample y WR para justificar).
> 4. **Palanca humana #1**: el mejor duo partner identificado y por qué
>    (cita WR juntos vs WR solo).
> 5. **Compromiso de la semana**: la acción #1 de la tabla {section_n}.2
>    + métrica de seguimiento concreta (ej. "el sábado que viene
>    re-medimos CS@10 en últimas 20 partidas").
>
> **Reglas globales de esta sección**:
>
> - **Cero invenciones**: si una métrica no aparece en los .md, no se
>   usa. Mejor menos puntos sustentados que más puntos vacíos.
> - **Coherencia interna**: las recomendaciones de cierre ({section_n}.3)
>   deben derivarse de las tablas {section_n}.1 y {section_n}.2 — no
>   pueden contradecirlas.
> - **Sin emojis**.
"""


# Header del meta-prompt (parametrizado por jugador / archivos disponibles).
_MASTER_PROMPT_HEADER = """\
# COACH 360° — Análisis cross-role para {player_riot_id}

> **Generado automáticamente por `lol-scrap` el {generated_at}.**
> Pegá este prompt completo en el chat de Cursor con la carpeta
> `{player_dir_relpath}/` abierta en el explorer y dejá que el LLM
> lea los .md y escriba el análisis.

## Contexto

El directorio `{player_dir_relpath}/` contiene **{n_files} archivos de
datos** generados por el scraper:

{files_listing}

## Tu tarea

Actuá como un **panel de coaches senior de League of Legends** (uno por
rol + un coach jefe que mira el cross-role). Generá un único archivo
de análisis llamado `COACH_ANALYSIS.md` en el mismo directorio
(`{player_dir_relpath}/COACH_ANALYSIS.md`) con **{n_sections} secciones**:

{sections_outline}

## Reglas globales (aplican a TODAS las secciones)

> **R1. Regla de oro**: NO INVENTES DATOS. Si una stat no está en los
> archivos, decí explícitamente "**insuficiente data**" o "**no medido
> aún**" (cuando una métrica de Riot challenge tenga n=0 en la sec. 6
> del MD del rol).
>
> **R2. Citar evidencia siempre**: cada número que uses debe venir con
> su archivo y sección de origen. Formato sugerido:
> "Splitpush Index 0.43 [TOP.md sec. 6]" o
> "Vision/min 1.59 vs baseline 2.60 [UTILITY.md sec. 4 Playstyle]".
>
> **R3. Cross-check entre archivos**: cuando una métrica aparezca en
> `GLOBAL.md` Y en un .md de rol específico, **comparar y comentar la
> diferencia** (ej. "el KDA Global es 2.46 pero el KDA filtrado a Top
> es 2.51, diferencia marginal — el desempeño Top es representativo
> del overall").
>
> **R4. Extensión y estadística**: cada afirmación debe estar respaldada
> por (a) número exacto citado y (b) **mecanismo causal** explícito de
> por qué esa stat conduce al problema/fortaleza identificado. **Más
> extenso y estadístico que un análisis de coaching tradicional** —
> apuntá a 800-1500 palabras por sección de rol, no a un párrafo
> conclusivo. Sección 1 (overview) puede ser más larga si hace falta.
>
> **R5. Sample chico**: si una métrica tiene n<5 games, declararlo
> explícitamente como caveat ("sample chico, dirección direccional
> pero no concluyente"). Si está entre 5-10 games, decir "sample
> moderado". Si ≥10, "sample sólido".
>
> **R6. Estructura por sección de rol**: además de las sub-secciones
> A-G del prompt original de cada rol, agregar **al final de cada
> sección de rol** una sub-sección "**Conexión con GLOBAL**" que
> compare las métricas clave del rol vs el promedio cross-role del
> jugador (ej. "tu KDA en Top es 2.51, vs Global 2.46 — el rol Top
> es ligeramente sobre tu media; lo confirma como tu rol natural").

---

"""


_FILE_LISTING_TEMPLATE = (
    "- `{path}` — {description}"
)


_SECTIONS_OUTLINE_TEMPLATE = (
    "{i}. **Sección {i} — {title}**: {description}"
)


def _adapt_role_prompt_to_file(role: str, role_label: str, filename: str) -> str:
    """Adapta un ROLE_PROMPTS[role] para apuntar al archivo <ROL>.md.

    El prompt original asume que el LLM tiene "el reporte abierto" y
    referencia secciones del mismo MD. Acá lo formateamos con las
    secciones fijas que reporta el script (sec. 4-6.1, 9, 12) y le
    agregamos un header que aclara que la fuente es el archivo
    `<filename>` especifico.
    """
    template = ROLE_PROMPTS.get(role)
    if template is None:
        return ""
    body = template.format(
        role_label=role_label,
        advanced_section_n=_SEC_ADVANCED,
        phases_section_n=_SEC_PHASES,
        cross_section_n=_SEC_CROSS,
        matchups_section_n=_SEC_MATCHUPS,
        duo_section_n=_SEC_DUO_PARTNERS,
    )
    # Reemplazar "del reporte abierto" -> "del archivo <filename>"
    body = body.replace(
        "datos del reporte abierto", f"datos del archivo `{filename}`"
    )
    return body


def build_master_prompt(
    player_riot_id: str,
    player_dir_relpath: str,
    roles_with_md: list[tuple[str, str, int]],
    has_global: bool,
    generated_at: str,
) -> str:
    """Arma el meta-prompt completo para analizar la carpeta del jugador.

    Args:
        player_riot_id: ej. "Manuchito#LAS".
        player_dir_relpath: path relativo al cwd del directorio del jugador,
            ej. "reports/Manuchito-LAS".
        roles_with_md: lista de (canonical_role, role_label, games)
            ordenada por games desc, ej.
            [("TOP", "Top", 162), ("MIDDLE", "Mid", 20)].
        has_global: si se genero GLOBAL.md.
        generated_at: timestamp legible para el header.

    Returns:
        El meta-prompt como string markdown listo para escribir a disco.
    """
    files: list[str] = []
    if has_global:
        files.append(
            _FILE_LISTING_TEMPLATE.format(
                path=f"{player_dir_relpath}/GLOBAL.md",
                description=(
                    "overview cross-role (datos sin filtro de rol; "
                    "incluye comparativa entre roles, sec. 12 sinergias "
                    "humanas globales)"
                ),
            )
        )
    for role, role_label, games in roles_with_md:
        files.append(
            _FILE_LISTING_TEMPLATE.format(
                path=f"{player_dir_relpath}/{role}.md",
                description=(
                    f"datos filtrados al rol **{role_label}** ({games} "
                    f"partidas) con stats avanzadas Riot challenges "
                    f"específicas (sec. 6) y análisis cruzado (sec. 6.1)"
                ),
            )
        )
    files_listing = "\n".join(files)

    sections: list[str] = []
    if has_global:
        sections.append(
            _SECTIONS_OUTLINE_TEMPLATE.format(
                i=1,
                title="Overview Cross-Role",
                description=(
                    "análisis transversal del jugador combinando todos los "
                    "roles, basado en `GLOBAL.md`. Incluye identificación del "
                    "rol natural, comparativa entre roles, sinergias humanas "
                    "globales, patrones cruzados y recomendación estratégica."
                ),
            )
        )
        next_i = 2
    else:
        next_i = 1

    last_role_idx = next_i - 1
    for idx, (role, role_label, games) in enumerate(roles_with_md, start=next_i):
        sections.append(
            _SECTIONS_OUTLINE_TEMPLATE.format(
                i=idx,
                title=f"{role_label} ({role})",
                description=(
                    f"análisis específico del rol {role_label} basado en "
                    f"`{role}.md` ({games} partidas). Sigue el formato "
                    f"coach senior de {role_label}: scores 1-5 por stat "
                    f"core, fortalezas/debilidades específicas, acciones "
                    f"semanales, fases del juego, matchups, pool ideal y "
                    f"conclusión sintetizada."
                ),
            )
        )
        last_role_idx = idx

    n_role_sections = len(roles_with_md)
    ranking_section_index = last_role_idx + 1 if n_role_sections > 0 else next_i
    has_ranking = n_role_sections > 0
    if has_ranking:
        sections.append(
            _SECTIONS_OUTLINE_TEMPLATE.format(
                i=ranking_section_index,
                title="Ranking final + Plan de acción (Coach Jefe)",
                description=(
                    "cierre ejecutivo: tabla ranking de los roles "
                    "analizados (mejor → peor fit), tabla con las 5 "
                    "acciones accionables priorizadas, y párrafo final "
                    "del coach jefe con rol primario, secundario, roles "
                    "a evitar, mejor duo y compromiso de la semana."
                ),
            )
        )

    sections_outline = "\n".join(sections)

    n_files = len(files)
    n_sections = len(sections)

    header = _MASTER_PROMPT_HEADER.format(
        player_riot_id=player_riot_id,
        player_dir_relpath=player_dir_relpath,
        generated_at=generated_at,
        files_listing=files_listing,
        sections_outline=sections_outline,
        n_files=n_files,
        n_sections=n_sections,
    )

    parts: list[str] = [header]

    if has_global:
        parts.append(_OVERVIEW_PROMPT)
        parts.append("\n---\n")

    section_index = 2 if has_global else 1
    for role, role_label, games in roles_with_md:
        filename = f"{role}.md"
        role_block = _adapt_role_prompt_to_file(role, role_label, filename)
        if not role_block:
            continue
        section_header = (
            f"> ## Sección {section_index} — {role_label} ({role}) — basado en "
            f"`{filename}` ({games} partidas)\n>\n"
        )
        # Bloque de extension extra: cada rol debe agregar evidencia
        # estadistica adicional + Conexion con GLOBAL.
        extension_tail = (
            ">\n"
            "> **Sub-sección extra (obligatoria) — Conexión con GLOBAL**:\n"
            f"> compará 3 métricas clave de `{filename}` (KDA, CS/m, DPM "
            "y/o cualquier stat avanzada relevante del rol) con el promedio "
            "cross-role en `GLOBAL.md` (sec. 1 — Resumen y sec. 1 — "
            "Distribución entre roles). Calculá el delta y declarálo: "
            "\"el rol X está +Y% sobre tu media → es tu rol natural\" o "
            "\"el rol X está -Y% bajo tu media → estás peor acá que en otros "
            "roles\".\n"
            ">\n"
            "> **Profundidad estadística esperada**: mínimo 800 palabras\n"
            "> para esta sección. Incluí siempre el delta vs baseline del\n"
            "> rank correspondiente (que está en sec. 4 Playstyle del .md\n"
            "> del rol) y la dirección del delta (positivo/negativo).\n"
        )
        parts.append(section_header + role_block + extension_tail)
        parts.append("\n---\n")
        section_index += 1

    if has_ranking:
        n_previous_sections = ranking_section_index - 1
        ranking_block = _RANKING_PROMPT.format(
            section_n=ranking_section_index,
            n_previous_sections=n_previous_sections,
        )
        parts.append(ranking_block)
        parts.append("\n---\n")

    parts.append(
        "\n## Cierre\n\n"
        "Cuando termines, **escribí el output a "
        f"`{player_dir_relpath}/COACH_ANALYSIS.md`** (un solo archivo con "
        f"las {n_sections} secciones). El archivo final debería rondar las "
        f"{800 * n_sections}-{1500 * n_sections} palabras totales y tener "
        "tablas markdown para los scores 1-5, para las comparativas de "
        "métricas entre archivos, y para el ranking final + plan de "
        f"acción de la sección {ranking_section_index}.\n"
    )

    return "".join(parts)


__all__ = [
    "ROLE_PROMPTS",
    "GENERIC_INTRO",
    "GENERIC_OUTRO",
    "render_role_prompt",
    "build_master_prompt",
]
