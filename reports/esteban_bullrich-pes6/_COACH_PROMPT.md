# COACH 360° — Análisis cross-role para esteban bullrich#pes6

> **Generado automáticamente por `lol-scrap` el 2026-05-08 22:25 UTC.**
> Pegá este prompt completo en el chat de Cursor con la carpeta
> `reports/esteban_bullrich-pes6/` abierta en el explorer y dejá que el LLM
> lea los .md y escriba el análisis.

## Contexto

El directorio `reports/esteban_bullrich-pes6/` contiene **6 archivos de
datos** generados por el scraper:

- `reports/esteban_bullrich-pes6/GLOBAL.md` — overview cross-role (datos sin filtro de rol; incluye comparativa entre roles, sec. 12 sinergias humanas globales)
- `reports/esteban_bullrich-pes6/JUNGLE.md` — datos filtrados al rol **Jungla** (198 partidas) con stats avanzadas Riot challenges específicas (sec. 6) y análisis cruzado (sec. 6.1)
- `reports/esteban_bullrich-pes6/TOP.md` — datos filtrados al rol **Top** (133 partidas) con stats avanzadas Riot challenges específicas (sec. 6) y análisis cruzado (sec. 6.1)
- `reports/esteban_bullrich-pes6/UTILITY.md` — datos filtrados al rol **Support** (72 partidas) con stats avanzadas Riot challenges específicas (sec. 6) y análisis cruzado (sec. 6.1)
- `reports/esteban_bullrich-pes6/MIDDLE.md` — datos filtrados al rol **Mid** (35 partidas) con stats avanzadas Riot challenges específicas (sec. 6) y análisis cruzado (sec. 6.1)
- `reports/esteban_bullrich-pes6/BOTTOM.md` — datos filtrados al rol **ADC** (22 partidas) con stats avanzadas Riot challenges específicas (sec. 6) y análisis cruzado (sec. 6.1)

## Tu tarea

Actuá como un **panel de coaches senior de League of Legends** (uno por
rol + un coach jefe que mira el cross-role). Generá un único archivo
de análisis llamado `COACH_ANALYSIS.md` en el mismo directorio
(`reports/esteban_bullrich-pes6/COACH_ANALYSIS.md`) con **7 secciones**:

1. **Sección 1 — Overview Cross-Role**: análisis transversal del jugador combinando todos los roles, basado en `GLOBAL.md`. Incluye identificación del rol natural, comparativa entre roles, sinergias humanas globales, patrones cruzados y recomendación estratégica.
2. **Sección 2 — Jungla (JUNGLE)**: análisis específico del rol Jungla basado en `JUNGLE.md` (198 partidas). Sigue el formato coach senior de Jungla: scores 1-5 por stat core, fortalezas/debilidades específicas, acciones semanales, fases del juego, matchups, pool ideal y conclusión sintetizada.
3. **Sección 3 — Top (TOP)**: análisis específico del rol Top basado en `TOP.md` (133 partidas). Sigue el formato coach senior de Top: scores 1-5 por stat core, fortalezas/debilidades específicas, acciones semanales, fases del juego, matchups, pool ideal y conclusión sintetizada.
4. **Sección 4 — Support (UTILITY)**: análisis específico del rol Support basado en `UTILITY.md` (72 partidas). Sigue el formato coach senior de Support: scores 1-5 por stat core, fortalezas/debilidades específicas, acciones semanales, fases del juego, matchups, pool ideal y conclusión sintetizada.
5. **Sección 5 — Mid (MIDDLE)**: análisis específico del rol Mid basado en `MIDDLE.md` (35 partidas). Sigue el formato coach senior de Mid: scores 1-5 por stat core, fortalezas/debilidades específicas, acciones semanales, fases del juego, matchups, pool ideal y conclusión sintetizada.
6. **Sección 6 — ADC (BOTTOM)**: análisis específico del rol ADC basado en `BOTTOM.md` (22 partidas). Sigue el formato coach senior de ADC: scores 1-5 por stat core, fortalezas/debilidades específicas, acciones semanales, fases del juego, matchups, pool ideal y conclusión sintetizada.
7. **Sección 7 — Ranking final + Plan de acción (Coach Jefe)**: cierre ejecutivo: tabla ranking de los roles analizados (mejor → peor fit), tabla con las 5 acciones accionables priorizadas, y párrafo final del coach jefe con rol primario, secundario, roles a evitar, mejor duo y compromiso de la semana.

## Reglas globales (aplican a TODAS las secciones)

> **R1. Regla de oro**: NO INVENTES DATOS. Si una stat no está en los
> archivos fuente, decí explícitamente "**insuficiente data**" o "**no
> medido aún**" (cuando una métrica avanzada tenga n=0). **Internamente**
> los datos vienen de varios archivos, pero **el lector del análisis
> sólo verá este documento final** (no los archivos fuente).
>
> **R2. Cita evidencia con números, NO con archivos**: cada afirmación
> debe traer su número exacto integrado en lenguaje humano. **PROHIBIDO
> escribir "[GLOBAL.md sec. 4]", "[TOP.md sec. 6]", "(sec. 12)" o
> cualquier referencia a archivos `.md` o números de sección** —el
> lector del PDF no tiene acceso a esos archivos. Reemplazá por
> formulaciones humanas:
>
> - Mal: "KDA 2.51 [TOP.md sec. 4]". Bien: "KDA 2.51 en tu data de Top".
> - Mal: "Vision/min 1.59 vs 2.60 [UTILITY.md sec. 4 Playstyle]". Bien:
>   "Vision/min 1.59 vs baseline 2.60 (-39%) en tu Support".
> - Mal: "DPM 889 [MIDDLE.md sec. 6]". Bien: "DPM 889 en tu rol Mid".
> - Mal: "WR 56.3% [GLOBAL.md sec. 11]". Bien: "WR 56.3% en 135 games
>   juntos".
>
> El número y el contexto (rol, partidas, baseline) son obligatorios;
> el archivo y la sección son ruido y van **fuera**.
>
> **R3. Cross-check sin nombrar archivos**: cuando una métrica aparezca
> tanto en datos cross-role como en un rol específico, comparar y
> comentar la diferencia. Pero el cross-check se redacta sin mencionar
> archivos: "tu KDA cross-role es 2.46; filtrado a Top es 2.51,
> diferencia marginal — Top es representativo de tu overall".
>
> **R4. Tablas sobre prosa cuando hay ≥3 elementos comparables**:
> si vas a citar la **misma métrica para 3 o más entidades** (champs,
> roles, duos, matchups, partidas), USÁ TABLA MARKDOWN, no prosa.
> Toda tabla comparativa debe terminar con una columna **"Lectura"**
> o **"Acción"** de **una sola oración** que diga qué hacer con esa
> fila (no repetir el número, **interpretar**).
>
> - Mal: "Mid CS@10 61.8 vs 75.8 (-18.5%), Top 61.1 vs 70.3 (-13.1%),
>   Jungla 53.2 vs 68.0 (-21.7%), ADC 56.9 vs 75.1 (-24.2%)".
> - Bien: tabla con columnas `Rol | CS@10 | Baseline | Δ% | Lectura`
>   y una oración por fila ("Patrón transversal: el problema no es
>   matchup-específico, es hábito de farm").
>
> **R5. Patrón "tabla resumen → drill-down debajo"**: para cualquier
> sub-sección con datos comparables (champ pool, matchups, sinergias,
> ranking de roles, fases del juego), el formato obligatorio es:
>
> 1. **Tabla compacta primero** (visión rápida con columna "Lectura").
> 2. **Explicación detallada debajo en 1-3 párrafos cortos** que
>    profundicen sólo en las 1-2 filas más importantes
>    (mecanismo causal, por qué importa, qué cambia si se ataca).
>
> El lector promedio se queda en la tabla; el lector interesado baja
> a los párrafos. **No repitas en prosa lo que ya está en la tabla**.
>
> **R6. Mecanismo causal explícito**: cada número debe venir con (a)
> el dato y (b) el **por qué** ese dato conduce al problema/fortaleza
> identificado. La explicación bajo cada tabla profundiza el "por qué",
> no el "cuánto". **Más extenso y estadístico que un coaching
> tradicional**: apuntá a 800-1500 palabras por sección de rol, pero
> distribuidas entre tablas y párrafos cortos —no en murallas de texto.
>
> **R7. Sample chico**: si una métrica tiene n<5 games, declararlo
> explícitamente ("sample chico, direccional pero no concluyente").
> Entre 5-10 games: "sample moderado". ≥10: "sample sólido".
>
> **R8. Counter matchups obligatorios por rol**: en cada sección de
> rol incluí **una tabla dedicada de "Top 3-5 peores matchups en lane
> vs champ enemigo"** con columnas `Champ enemigo | Games | WR vs él |
> Métrica clave que se cae | Acción (ban / counter / runa)`. **El
> peor matchup es accionable** (sabés qué banear); por eso pesa más
> que el mejor. Si hay <3 matchups con sample útil, declararlo y
> mostrar los que haya. Adicionalmente, una tabla más chica de
> "Top 3 mejores matchups" con el mismo formato pero con columna
> final "Por qué te conviene".
>
> **R9. Estructura por sección de rol**: además de las sub-secciones
> A-G del prompt de cada rol, agregar al final una sub-sección
> "**Conexión con tu overall**" que compare las métricas clave del
> rol vs el promedio cross-role del jugador, también en formato tabla
> si hay ≥3 métricas a comparar.
>
> **R10. Sin emojis, sin formato decorativo innecesario**, sin "summary
> box" llamativos. Texto técnico, tablas markdown estándar, párrafos
> cortos. El PDF se renderiza con tipografía profesional; añadirle
> ruido visual lo empeora.

---

> ## Sección 1 — Overview Cross-Role
>
> **Recordatorio**: nada de "[GLOBAL.md sec. X]" en el texto. Cuando
> necesites referirte a la fuente, decí "tu data cross-role", "tu
> overall", "tu rol Mid", etc. (R2 + R9).
>
> **1.1 Identificación del rol natural** — TABLA OBLIGATORIA + 1 párrafo:
>
> Tabla con todos los roles jugados, ordenados por games desc:
>
> | Rol | Games | WR | KDA | CS/m | DPM | Vision/min | Lectura |
> |-----|------:|---:|----:|-----:|----:|-----------:|---------|
> | ... | ...   | ...% | ... | ... | ... | ...        | 1 oración: rol natural / experimento / off-role / abandonar |
>
> Debajo de la tabla, **1 párrafo de 3-5 oraciones** que explique:
>
> - Qué rol es el natural (mejor WR con sample ≥10) y por qué.
> - Qué rol tiene mejor KDA — si no coincide con mejor WR, explicar el
>   mecanismo (ej. "muere menos pero no domina daño").
> - Qué rol tiene mejor DPM **relativo al baseline del rol** (no DPM
>   bruto). Citar delta % vs baseline.
> - Una conclusión accionable de identificación de rol primario.
>
> **1.2 Inversión de tiempo vs WR** — TABLA + 1 párrafo:
>
> | Rol | % del pool | WR | Δpp vs WR mejor rol | Wins esperadas perdidas | Lectura |
> |-----|----------:|---:|--------------------:|-------------------------:|---------|
>
> Calculá "wins esperadas perdidas" = `games_rol * Δpp/100` (donde Δpp es
> contra el rol con mejor WR del jugador). Bajo la tabla, párrafo con la
> conclusión: ¿hay misalignment estratégico? ¿qué rol limitar?
>
> **1.3 Sinergias humanas globales** — TABLA + 1 párrafo:
>
> Top 5 aliados por volumen, con flags de mejor/peor:
>
> | Aliado | Games | WR juntos | Δpp vs tu WR overall | Lectura |
> |--------|------:|----------:|---------------------:|---------|
>
> Bajo la tabla, párrafo con:
>
> - Mejor palanca (mayor Δpp con sample ≥30 idealmente).
> - Peor sinergia útil (≥10 games con Δpp negativo) — flag para evitar.
> - Patrones de rol del aliado (qué tipo de aliado te potencia: mid
>   carry, jungla snowballer, sup engage, etc.) si la data lo permite.
>
> **1.4 Patrones cruzados de fortalezas/debilidades** — TABLAS POR EJE:
>
> Una tabla **por cada eje transversal** que muestre la métrica en TODOS
> los roles. Ejes mínimos a evaluar (incluí los que tengan datos):
>
> 1. **CS temprano**:
>
> | Rol | CS@10 | Baseline | Δ% | Lectura |
> |-----|------:|---------:|---:|---------|
>
> 2. **DPM relativo al rol**:
>
> | Rol | DPM | Baseline rol | Δ% | Lectura |
> |-----|----:|-------------:|---:|---------|
>
> 3. **Vision/min**:
>
> | Rol | Vision/min | Baseline | Δ% | Lectura |
> |-----|----------:|---------:|---:|---------|
>
> 4. **Lane phase win rate (oro+exp @14')**:
>
> | Rol | Lane WR @14 | Lane lead @14 | Lectura |
> |-----|------------:|--------------:|---------|
>
> Debajo de las 4 tablas, **1 párrafo de 4-6 oraciones** que **una los
> patrones**: si CS@10 está bajo en TODOS los roles, no es matchup —es
> hábito mecánico. Si lane WR sube en mid pero baja en top, es matchup
> dependiente. Sólo profundizar en los 1-2 patrones más fuertes.
>
> **1.5 Recomendación estratégica** — párrafo de 4-6 oraciones (sin
> tabla, esta es prosa):
>
> - Qué rol priorizar (con wins esperadas ganadas si subís volumen).
> - Qué rol abandonar/limitar (con sample y Δpp negativo).
> - Rol secundario sano para flex queue (si lo hay).
> - Mejor palanca humana (mejor duo) y por qué.
>
> **Regla de oro de esta sección**: el lector promedio tiene que
> entenderlo todo SOLO leyendo las tablas. Los párrafos profundizan
> el "por qué", no repiten el "cuánto".

---
> ## Sección 2 — Jungla (JUNGLE) — basado en `JUNGLE.md` (198 partidas)
>
> **Rol del jugador: Jungla (JUNGLE)** — coach senior de Jungla.
> **4 dimensiones críticas**:
>
> 1. **Pathing efficiency** (clear rápido + tempo a level 6).
> 2. **Counter-jungle** (invade y starvea al rival).
> 3. **Gank impact** (convertís presencia en otras lanes en takedowns).
> 4. **Objective control** (drakes/herald/baron + soul rate).
>
> **Recordatorio R2/R9**: el lector del PDF no ve archivos `.md` ni
> números de sección. Internamente los datos vienen del .md de Jungla,
> pero **en tu output NO menciones ni archivos ni números de sección**.
> Decí "tu data de Jungla", "en partidas largas", "vs el jungla rival",
> etc.
>
> **A) Score 1-5 por stat core** — TABLA OBLIGATORIA:
>
> | Stat core | Valor | Score 1-5 | Lectura (1 oración) |
> |-----------|------:|----------:|---------------------|
> | Jungle CS antes del 10' | ... | ... | Diamond baseline ~58 |
> | Counter-jungle ratio | ... | ... | <0.3 = pasivo, 0.3-0.5 = balanceado, >0.5 = agresivo |
> | Takedowns en otras lanes early | ... | ... | Refleja gank presence |
> | Drakes + Heralds + Barones | ... | ... | Suma por partida |
> | Cobertura wards en río/jungla enemiga | ... | ... | ... |
> | Tempo Index level 6 | ... | ... | Lee Sin Diamond ~450s, Karthus ~510s |
> | Soul Rate | ... | ... | % de partidas largas con soul |
> | Gank-to-Death ratio | ... | ... | ... |
>
> **B) 3 fortalezas JUNGLE-específicas + 3 debilidades JUNGLE-específicas**
> — prosa corta. Ejemplos de estilo:
>
> - "Tu jungle CS @10 (52) está bajo Diamond (58) y tu gank impact (2.1)
>   tampoco sube — pathing ineficiente."
> - "Vision en río 18% → tus invades son ciegos, explica deaths early."
>
> **C) 3 acciones concretas para la próxima semana** — prosa imperativa.
>
> **D) Fase del juego más fuerte y más débil** — 2-3 oraciones.
>
> **E1) Top 3-5 PEORES matchups vs jungla enemigo** — TABLA OBLIGATORIA +
> 1 párrafo:
>
> | Jungla enemigo | Games | WR vs él | Stat clave que se cae | Acción (ban / counter / pathing) |
> |----------------|------:|---------:|------------------------|------------------------------------|
> | ... | ... | ...% | ... | ... |
>
> Si no hay matchups con sample útil (≥3 games), declararlo y mostrar lo
> que haya. Bajo la tabla, **párrafo de 2-4 oraciones** explicando el
> peor matchup en detalle: por qué pierde el primer cangrejo / primer
> drake / primer invade, y qué jungler propio se le pega mejor.
>
> **E2) Top 3 MEJORES matchups vs jungla enemigo** — TABLA OBLIGATORIA:
>
> | Jungla enemigo | Games | WR vs él | Stat que sube | Acción (priorizar / pathing) |
> |----------------|------:|---------:|----------------|------------------------------|
>
> **F) Champ pool propio (junglas)** — TABLA OBLIGATORIA + 1-2 párrafos:
>
> | Champ propio | Games | WR | KDA | DPM o KP% | Recomendación |
> |--------------|------:|---:|----:|-----------:|---------------|
>
> Bajo la tabla, profundizar en el top 1 a priorizar y el top 1 a sacar
> (mecanismo causal: por qué WR alto con ese champ refleja una skill
> tuya o un meta-pick favorable; por qué el WR bajo con otro refleja
> un mismatch entre tu pathing y la identidad del champ).
>
> **G) Conclusión general en 1 oración**.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí
> "insuficiente data" o "no medido aún".
>
> **Sub-sección extra (obligatoria) — Conexión con tu overall**:
> TABLA con ≥3 métricas clave del rol (KDA, CS/m, DPM, Vision/min,
> y/o cualquier stat avanzada relevante) vs tu promedio cross-role:
>
> | Métrica | Este rol | Tu overall | Δ% | Lectura |
> |---------|---------:|-----------:|---:|---------|
> | ...     | ...      | ...        | ...| ...     |
>
> En la columna Lectura: 1 oración por fila declarando si el rol
> es **+** sobre tu media (rol natural / fortaleza) o **-** bajo
> tu media (estás peor acá que en otros roles). NO menciones
> archivos ni secciones (R2 + R9). Lenguaje humano: "este rol",
> "tu overall", "baseline del rank".
>
> **Profundidad estadística esperada**: mínimo 800 palabras
> para esta sección, distribuidas entre tablas y párrafos cortos
> (R6). Incluí siempre el delta vs baseline del rank correspondiente
> y la dirección del delta.

---
> ## Sección 3 — Top (TOP) — basado en `TOP.md` (133 partidas)
>
> **Rol del jugador: Top (TOP)** — un coach senior de Top lane analiza
> este reporte. Las **3 dimensiones críticas** del rol son:
>
> 1. **Lane dominance** (gano el 1v1 y lo traduzco en oro/CS/plates).
> 2. **Splitpush + side-laning** (aplico presión cuando los teamfights no convienen).
> 3. **Tank value / sustain en teamfights largos** (sobrevivo y absorbo daño).
>
> **Recordatorio R2/R9**: el lector del PDF no ve archivos `.md` ni
> números de sección. Internamente los datos están en stats avanzadas,
> en Early/Mid/Late y en matchups del .md de Top, pero **en tu output
> NO menciones ni archivos ni números de sección**. Decí "tu data de
> Top", "en partidas largas", "vs Sion enemigo", etc.
>
> **A) Score 1-5 por stat core** — TABLA OBLIGATORIA:
>
> | Stat core | Valor | Score 1-5 | Lectura (1 oración) |
> |-----------|------:|----------:|---------------------|
> | Gold diff @15 | ... | ... | ... |
> | Lane phase WR @14 + lead | ... | ... | Target: ~50% y lead positivo. <40% = problema de matchup/ejecución |
> | Solo kills + quick solo kills | ... | ... | ... |
> | Plates + daño a torres | ... | ... | ... |
> | Daño mitigado | ... | ... | ... |
> | Splitpush Index | ... | ... | Rango splitpushers 0.4-0.6 |
> | KDA en partidas largas | ... | ... | Indica capacidad de cierre tardío |
>
> Si una stat tiene n=0, poner "no medido aún" en valor y "N/A" en score.
>
> **B) 3 fortalezas TOP-específicas + 3 debilidades TOP-específicas** —
> prosa corta (1 oración cada una). No genéricas tipo "tenés bajo KDA";
> sí específicas tipo "tu Splitpush Index está bajo para los champs
> (Fiora/Camille) que esperan side-laning".
>
> **C) 3 acciones concretas para la próxima semana** — prosa, imperativa,
> contextualizada al rol Top.
>
> **D) Fase del juego más fuerte y más débil** — 2-3 oraciones citando
> score y métrica que más arrastra para abajo en la peor fase.
>
> **E1) Top 3-5 PEORES matchups en lane Top** — TABLA OBLIGATORIA + 1
> párrafo de drill-down:
>
> | Champ enemigo | Games | WR vs él | Stat clave que se cae | Acción (ban / counter / runas) |
> |---------------|------:|---------:|------------------------|--------------------------------|
> | ... | ... | ...% | ... | ... |
>
> Filtrar a los matchups que tengan al menos 3 games (declarar sample).
> Bajo la tabla, **párrafo de 2-4 oraciones** explicando el peor matchup
> en profundidad: por qué se pierde la lane (mecanismo causal: trade
> patterns, all-in timing, scaling), qué champ propio funciona mejor
> contra él (si la data lo permite), y por qué la acción sugerida lo
> resuelve.
>
> **E2) Top 3 MEJORES matchups en lane Top** — TABLA OBLIGATORIA:
>
> | Champ enemigo | Games | WR vs él | Stat que sube | Acción (priorizar / first-pick contra él) |
> |---------------|------:|---------:|----------------|--------------------------------------------|
> | ... | ... | ...% | ... | ... |
>
> Sin párrafo extra (la tabla es suficiente para los buenos matchups,
> que no requieren intervención).
>
> **F) Champ pool propio en Top** — TABLA OBLIGATORIA + 1-2 párrafos:
>
> | Champ propio | Games | WR | KDA | CS/m o DPM | Recomendación (priorizar / mantener / sacar) |
> |--------------|------:|---:|----:|-----------:|----------------------------------------------|
> | ... | ... | ...% | ... | ... | ... |
>
> Bajo la tabla, **1-2 párrafos cortos** que profundicen en:
>
> - Top 1 a priorizar: por qué (mecanismo: identidad de carry, ratio
>   WR/games, ajuste a tu late game). Si va con counter pickeo o
>   matchups buenos, mencionarlo.
> - Top 1 a sacar: por qué (WR bajo con sample sólido, contradicción
>   con tus fortalezas, dependencia de skill que no tenés calibrada).
>
> **G) Conclusión general en 1 oración** sintetizando A-F.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí
> "insuficiente data" o "no medido aún".
>
> **Sub-sección extra (obligatoria) — Conexión con tu overall**:
> TABLA con ≥3 métricas clave del rol (KDA, CS/m, DPM, Vision/min,
> y/o cualquier stat avanzada relevante) vs tu promedio cross-role:
>
> | Métrica | Este rol | Tu overall | Δ% | Lectura |
> |---------|---------:|-----------:|---:|---------|
> | ...     | ...      | ...        | ...| ...     |
>
> En la columna Lectura: 1 oración por fila declarando si el rol
> es **+** sobre tu media (rol natural / fortaleza) o **-** bajo
> tu media (estás peor acá que en otros roles). NO menciones
> archivos ni secciones (R2 + R9). Lenguaje humano: "este rol",
> "tu overall", "baseline del rank".
>
> **Profundidad estadística esperada**: mínimo 800 palabras
> para esta sección, distribuidas entre tablas y párrafos cortos
> (R6). Incluí siempre el delta vs baseline del rank correspondiente
> y la dirección del delta.

---
> ## Sección 4 — Support (UTILITY) — basado en `UTILITY.md` (72 partidas)
>
> **Rol del jugador: Support (UTILITY/SUPPORT)** — coach senior de
> Support. **4 dimensiones críticas**:
>
> 1. **Vision** (control + dominance — el rol más responsable del mapa).
> 2. **Engage / disengage** (CC chains, saves, picks).
> 3. **Enable** (heal+shield + facilitar al ADC).
> 4. **Roam impact** (presión en otras lanes cuando bot farmea).
>
> **Recordatorio R2/R9**: el lector del PDF no ve archivos `.md` ni
> números de sección. Internamente los datos vienen del .md de Support,
> pero **en tu output NO menciones ni archivos ni números de sección**.
> Decí "tu data de Support", "vs Pyke enemigo", "con Aphelios como ADC",
> etc.
>
> **A) Score 1-5 por stat core** — TABLA OBLIGATORIA:
>
> | Stat core | Valor | Score 1-5 | Lectura (1 oración) |
> |-----------|------:|----------:|---------------------|
> | Vision/min + advantage vs sup rival | ... | ... | Baseline Diamond Sup ~2.6 |
> | Cobertura wards en río/jungla enemiga | ... | ... | ... |
> | Heal+shield efectivo + saves | ... | ... | ... |
> | CC sobre enemigos + picks coordinados | ... | ... | ... |
> | Vision Dominance Ratio | ... | ... | Target Diamond+ >1.3 |
> | Roam impact (takedowns otras lanes) | ... | ... | ... |
> | Quest del support item a tiempo | ... | ... | ... |
>
> **B) Identificación del arquetipo + 3 fortalezas + 3 debilidades** —
> prosa corta:
>
> - Primero declarar el arquetipo dominante (engage / enchanter / pick)
>   según el champ pool y los stats.
> - Luego evaluar si el pool actual coincide con el arquetipo.
> - 3 fortalezas SUP-específicas + 3 debilidades SUP-específicas.
>
> Ejemplos: "Arquetipo engage (Leona/Naut, immobilizations 18.3) pero
> pickKillWithAlly 4.1 — el CC va a aire, problema de comm o ADC pool".
>
> **C) 3 acciones concretas para la próxima semana** — prosa imperativa.
>
> **D) Fase del juego más fuerte y más débil** — 2-3 oraciones.
>
> **E1) Top 3-5 PEORES matchups vs sup enemigo** — TABLA OBLIGATORIA + 1
> párrafo:
>
> | Sup enemigo | Games | WR vs él | Stat clave que se cae | Acción (ban / counter / con qué ADC sí) |
> |-------------|------:|---------:|------------------------|------------------------------------------|
>
> Filtrar a ≥3 games (declarar sample). Bajo la tabla, **párrafo de 2-4
> oraciones** profundizando en el peor matchup: por qué pierde el 2v2
> (engage vs enchanter, range vs poke, level 6 timing), y qué sup propio
> tuyo se le pega mejor.
>
> **E2) Top 3 MEJORES matchups vs sup enemigo** — TABLA OBLIGATORIA:
>
> | Sup enemigo | Games | WR vs él | Stat que sube | Acción (priorizar / con qué ADC) |
> |-------------|------:|---------:|----------------|----------------------------------|
>
> **F) Champ pool propio (sups) por arquetipo** — TABLA OBLIGATORIA + 1-2
> párrafos:
>
> | Sup propio | Arquetipo | Games | WR | KDA | Vision/min | Recomendación |
> |------------|-----------|------:|---:|----:|-----------:|---------------|
>
> Bajo la tabla, profundizar en:
>
> - Top 1 a priorizar dentro de tu arquetipo dominante.
> - Top 1 a sacar (mismo motivo: WR bajo con sample sólido o
>   contradicción con tu arquetipo).
> - Si tu arquetipo cambia según el ADC, mencionarlo.
>
> **G) Sinergias con ADC duo** — TABLA OBLIGATORIA:
>
> | ADC duo | Games | WR juntos | Δpp vs WR sin él | Acción |
> |---------|------:|----------:|------------------:|--------|
>
> Identificar mejor ADC duo (mayor Δpp con sample útil) y peor útil
> (Δpp negativo con ≥10 games).
>
> **H) Conclusión general en 1 oración** sintetizando A-G.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí
> "insuficiente data" o "no medido aún".
>
> **Sub-sección extra (obligatoria) — Conexión con tu overall**:
> TABLA con ≥3 métricas clave del rol (KDA, CS/m, DPM, Vision/min,
> y/o cualquier stat avanzada relevante) vs tu promedio cross-role:
>
> | Métrica | Este rol | Tu overall | Δ% | Lectura |
> |---------|---------:|-----------:|---:|---------|
> | ...     | ...      | ...        | ...| ...     |
>
> En la columna Lectura: 1 oración por fila declarando si el rol
> es **+** sobre tu media (rol natural / fortaleza) o **-** bajo
> tu media (estás peor acá que en otros roles). NO menciones
> archivos ni secciones (R2 + R9). Lenguaje humano: "este rol",
> "tu overall", "baseline del rank".
>
> **Profundidad estadística esperada**: mínimo 800 palabras
> para esta sección, distribuidas entre tablas y párrafos cortos
> (R6). Incluí siempre el delta vs baseline del rank correspondiente
> y la dirección del delta.

---
> ## Sección 5 — Mid (MIDDLE) — basado en `MIDDLE.md` (35 partidas)
>
> **Rol del jugador: Mid (MIDDLE)** — coach senior de Mid lane.
> **4 dimensiones críticas**:
>
> 1. **Lane priority** (gano la lane y libero al jungla).
> 2. **Roam impact** (visito side lanes y abro el mapa).
> 3. **Damage output en teamfights** (% del daño del equipo).
> 4. **Snowball capacity** (aces tempranos, mejais a tiempo).
>
> **Recordatorio R2/R9**: el lector del PDF no ve archivos `.md` ni
> números de sección. Internamente los datos vienen del .md de Mid,
> pero **en tu output NO menciones ni archivos ni números de sección**.
> Decí "tu data de Mid", "en partidas largas", "vs Yasuo enemigo", etc.
>
> **A) Score 1-5 por stat core** — TABLA OBLIGATORIA:
>
> | Stat core | Valor | Score 1-5 | Lectura (1 oración) |
> |-----------|------:|----------:|---------------------|
> | Lane phase WR @14 + lead | ... | ... | Target ~50% y lead positivo. <40% o lead <-500 = problema serio |
> | Max CS lead + level lead | ... | ... | ... |
> | Takedowns en otras lanes | ... | ... | Roam presence |
> | % daño del equipo + DPM | ... | ... | DPM baseline Diamond ~857 |
> | Aces antes del 15' | ... | ... | Snowball collective |
> | Solo kills | ... | ... | Threat individual en mid |
> | Roam Conversion Rate | ... | ... | WR con ≥2 roams vs WR con 0 roams |
> | Synergy WR con jungla | ... | ... | WR con tu jungler vs WR sin él |
>
> **B) 3 fortalezas MID-específicas + 3 debilidades MID-específicas** —
> prosa corta. Ejemplos:
>
> - "DPM 520 lejos del baseline 857 pero teamDmg% 22% — pegás poco aunque
>   las partidas duran; problema de positioning/build."
> - "Roam impact 4.2 arriba del baseline, pero WR con ≥3 roams es 45% vs
>   62% sin roams — roameás en momentos malos."
>
> **C) 3 acciones concretas para la próxima semana** — prosa imperativa.
>
> **D) Fase del juego más fuerte y más débil** — 2-3 oraciones.
>
> **E1) Top 3-5 PEORES matchups en lane Mid** — TABLA OBLIGATORIA + 1
> párrafo:
>
> | Champ enemigo | Games | WR vs él | Stat clave que se cae | Acción (ban / counter / runas) |
> |---------------|------:|---------:|------------------------|--------------------------------|
> | ... | ... | ...% | ... | ... |
>
> Filtrar matchups con ≥3 games (declarar sample). Bajo la tabla,
> **párrafo de 2-4 oraciones** profundizando en el peor matchup:
> mecanismo (range, all-in, scaling), qué champ propio funciona contra
> él, y por qué la acción sugerida lo resuelve.
>
> **E2) Top 3 MEJORES matchups en lane Mid** — TABLA OBLIGATORIA:
>
> | Champ enemigo | Games | WR vs él | Stat que sube | Acción (priorizar / first-pick contra él) |
> |---------------|------:|---------:|----------------|--------------------------------------------|
>
> **F) Champ pool propio (mids)** — TABLA OBLIGATORIA + 1-2 párrafos:
>
> | Champ propio | Games | WR | KDA | DPM | Recomendación |
> |--------------|------:|---:|----:|----:|---------------|
>
> Bajo la tabla, profundizar en top 1 a priorizar y top 1 a sacar.
> Identificar arquetipo (roamer agresivo Twisted Fate/Talon/Galio vs
> farmer Azir/Cassio/Vex vs assassin Zed/Akali) y validar con la data.
>
> **G) Conclusión general en 1 oración**.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí
> "insuficiente data" o "no medido aún".
>
> **Sub-sección extra (obligatoria) — Conexión con tu overall**:
> TABLA con ≥3 métricas clave del rol (KDA, CS/m, DPM, Vision/min,
> y/o cualquier stat avanzada relevante) vs tu promedio cross-role:
>
> | Métrica | Este rol | Tu overall | Δ% | Lectura |
> |---------|---------:|-----------:|---:|---------|
> | ...     | ...      | ...        | ...| ...     |
>
> En la columna Lectura: 1 oración por fila declarando si el rol
> es **+** sobre tu media (rol natural / fortaleza) o **-** bajo
> tu media (estás peor acá que en otros roles). NO menciones
> archivos ni secciones (R2 + R9). Lenguaje humano: "este rol",
> "tu overall", "baseline del rank".
>
> **Profundidad estadística esperada**: mínimo 800 palabras
> para esta sección, distribuidas entre tablas y párrafos cortos
> (R6). Incluí siempre el delta vs baseline del rank correspondiente
> y la dirección del delta.

---
> ## Sección 6 — ADC (BOTTOM) — basado en `BOTTOM.md` (22 partidas)
>
> **Rol del jugador: ADC (BOTTOM/ADC)** — coach senior de ADC.
> **4 dimensiones críticas**:
>
> 1. **Sustained DPS** (DPM + % daño del equipo en teamfights).
> 2. **Positioning** (ratio damage out / damage in — la regla #1).
> 3. **Scaling** (KDA crece en partidas largas si llevás scaling carries).
> 4. **Lane priority + plates con sup** (presión bot temprana).
>
> **Recordatorio R2/R9**: el lector del PDF no ve archivos `.md` ni
> números de sección. Internamente los datos vienen del .md de ADC,
> pero **en tu output NO menciones ni archivos ni números de sección**.
> Decí "tu data de ADC", "vs Lucian enemigo", "con Nami como sup", etc.
>
> **A) Score 1-5 por stat core** — TABLA OBLIGATORIA:
>
> | Stat core | Valor | Score 1-5 | Lectura (1 oración) |
> |-----------|------:|----------:|---------------------|
> | DPM + % daño del equipo | ... | ... | DPM baseline Diamond ~921 |
> | Positioning Index | ... | ... | Target Diamond ~1.0-1.4 (DPS dado / daño recibido) |
> | Plates / first turret | ... | ... | ... |
> | Items legendarios por partida | ... | ... | Refleja farm + spike timing |
> | Scaling Score | ... | ... | KDA partidas largas vs cortas |
> | Lane phase WR @14 + lead | ... | ... | El rival es el ADC enemigo. Target ~50%, lead positivo |
> | Muertes antes del 25' | ... | ... | <2 ideal; >4 = positioning roto |
> | Synergy WR con tu sup | ... | ... | WR con tu sup vs WR sin él |
>
> **B) 3 fortalezas ADC-específicas + 3 debilidades ADC-específicas** —
> prosa corta. Ejemplos:
>
> - "Positioning Index 0.75 (target ~1.1) — peleás con poco margen,
>   recibís más daño del que repartís."
> - "Scaling Score 0.9 con Vayne — perdés partidas largas con un champ
>   que debería favorecer late game."
>
> **C) 3 acciones concretas para la próxima semana** — prosa imperativa.
>
> **D) Fase del juego más fuerte y más débil** — 2-3 oraciones. Un ADC
> con Late score bajo es señal roja grande.
>
> **E1) Top 3-5 PEORES matchups vs ADC enemigo** — TABLA OBLIGATORIA +
> 1 párrafo:
>
> | ADC enemigo | Games | WR vs él | Stat clave que se cae | Acción (ban / counter pick / sup combo) |
> |-------------|------:|---------:|------------------------|------------------------------------------|
>
> Filtrar a ≥3 games (declarar sample). Bajo la tabla, **párrafo de 2-4
> oraciones** profundizando en el peor matchup: por qué se pierde la
> lane (range, all-in, sustain), qué ADC propio se le pega mejor, y qué
> sup combo tuyo lo neutraliza.
>
> **E2) Top 3 MEJORES matchups vs ADC enemigo** — TABLA OBLIGATORIA:
>
> | ADC enemigo | Games | WR vs él | Stat que sube | Acción (priorizar / first-pick contra él) |
> |-------------|------:|---------:|----------------|--------------------------------------------|
>
> **F) Champ pool propio (ADCs)** — TABLA OBLIGATORIA + 1-2 párrafos:
>
> | ADC propio | Games | WR | KDA | DPM | Recomendación |
> |------------|------:|---:|----:|----:|---------------|
>
> Bajo la tabla, profundizar en top 1 a priorizar y top 1 a sacar.
> Vincular el champ pool con el sup pool: qué ADC va con qué sup
> según las sinergias que existen en tu data.
>
> **G) Sinergias con sup duo** — TABLA OBLIGATORIA:
>
> | Sup duo | Games | WR juntos | Δpp vs WR sin él | Acción |
> |---------|------:|----------:|------------------:|--------|
>
> Identificar el mejor sup duo (mayor Δpp con sample útil) y el peor
> útil (Δpp negativo con ≥10 games).
>
> **H) Conclusión general en 1 oración** sintetizando A-G.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí
> "insuficiente data" o "no medido aún".
>
> **Sub-sección extra (obligatoria) — Conexión con tu overall**:
> TABLA con ≥3 métricas clave del rol (KDA, CS/m, DPM, Vision/min,
> y/o cualquier stat avanzada relevante) vs tu promedio cross-role:
>
> | Métrica | Este rol | Tu overall | Δ% | Lectura |
> |---------|---------:|-----------:|---:|---------|
> | ...     | ...      | ...        | ...| ...     |
>
> En la columna Lectura: 1 oración por fila declarando si el rol
> es **+** sobre tu media (rol natural / fortaleza) o **-** bajo
> tu media (estás peor acá que en otros roles). NO menciones
> archivos ni secciones (R2 + R9). Lenguaje humano: "este rol",
> "tu overall", "baseline del rank".
>
> **Profundidad estadística esperada**: mínimo 800 palabras
> para esta sección, distribuidas entre tablas y párrafos cortos
> (R6). Incluí siempre el delta vs baseline del rank correspondiente
> y la dirección del delta.

---
> ## Sección 7 — Ranking final + Plan de acción (Coach Jefe)
>
> Como **cierre del análisis**, sintetizá las 6 secciones
> previas en **dos tablas markdown** + un párrafo final del coach jefe.
> Esta sección es el TL;DR ejecutivo: si el jugador solo lee esto, debe
> entender qué rol jugar y qué atacar primero.
>
> **7.1 Ranking de roles (mejor → peor fit estratégico)**
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
> | 1 | Top | 245 | 51.8% | 5.4 / 5.1 / 7.0 | Tu rol natural — late game sólido sostenido por scaling champs. | WR 51.8%, Late 7.0/10, Mordekaiser 64% WR en 59 games |
> | 2 | ... | ... | ...% | x.x / x.x / x.x | ... | ... |
>
> **Reglas de llenado** (estrictas):
>
> - **Justificación**: máx. 25 palabras, declarando el "por qué" del fit
>   (o de la falta de fit). En lenguaje humano (sin "[TOP.md sec. X]").
> - **Datos clave**: 2-3 métricas con valor numérico, separadas por comas.
>   En lenguaje humano: "WR 51.8%", "Mordekaiser 64% WR en 59 games",
>   "Late game 7.0/10". **No incluir referencias a archivos ni secciones**.
> - **Orden**: roles con sample <5 partidas van al final con flag
>   "sample insuficiente"; no se les asigna ranking comparativo.
> - **Consistencia**: el orden debe ser consistente con la recomendación
>   estratégica del overview (sub-sección 1.5). Si hay conflicto, se
>   prioriza este ranking y se aclara la actualización al final.
>
> **7.2 Top 5 acciones accionables cross-role (priorizadas)**
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
> | 1 | Subir CS@10 a 70+ | CS@10 = 58 vs baseline 72 (-19%) en tus 4 lanes principales; hábito mecánico | Top, Mid, ADC | Alto |
> | 2 | ... | ... | ... | Bajo/Medio/Alto |
>
> **Reglas de llenado**:
>
> - **Acción**: imperativa y concreta (ej. "Comprá control ward antes
>   de cada drake", NO "mejorá vision").
> - **Por qué**: SIEMPRE incluir el número exacto que motiva la acción
>   integrado en lenguaje humano (sin "[ARCHIVO.md sec. X]"). Sin
>   número → la acción no entra en el top 5.
> - **Roles afectados**: cuáles de los roles analizados se beneficiarían
>   (puede ser "Todos" si es transversal).
> - **Esfuerzo**: Bajo (queue/champ pick/duo), Medio (mecánica
>   replicable), Alto (cambio de hábito o pool nuevo).
> - **Diversidad**: que las 5 acciones no sean todas del mismo eje
>   (ej. no las 5 sobre CS); buscá mezclar mecánica + macro + draft.
>
> **7.3 Cierre del coach jefe** (1 párrafo, 4-6 oraciones,
> ≤120 palabras)
>
> Sintetizá en prosa:
>
> 1. **Rol primario** recomendado para ranked (con LP-ganancia esperada
>    estimada en %).
> 2. **Rol secundario** sano para flex queue / fill (si lo hay).
> 3. **Rol(es) a NO tocar** en ranked (con sample y WR para justificar).
> 4. **Palanca humana #1**: el mejor duo partner identificado y por qué
>    (cita WR juntos vs WR solo, en lenguaje humano).
> 5. **Compromiso de la semana**: la acción #1 de la tabla 7.2
>    + métrica de seguimiento concreta (ej. "el sábado que viene
>    re-medimos CS@10 en últimas 20 partidas").
>
> **Reglas globales de esta sección**:
>
> - **Cero invenciones**: si una métrica no aparece en los datos, no se
>   usa. Mejor menos puntos sustentados que más puntos vacíos.
> - **Cero referencias a archivos o secciones** (R2 + R9): nada de
>   "[GLOBAL.md sec. X]", "(sec. 12)", "según TOP.md". Lenguaje humano.
> - **Coherencia interna**: las recomendaciones de cierre (7.3)
>   deben derivarse de las tablas 7.1 y 7.2 — no
>   pueden contradecirlas.
> - **Sin emojis**.

---

## Cierre

Cuando termines, **escribí el output a `reports/esteban_bullrich-pes6/COACH_ANALYSIS.md`** (un solo archivo con las 7 secciones). El archivo final debería rondar las 5600-10500 palabras totales y tener tablas markdown para los scores 1-5, para las comparativas de métricas entre archivos, y para el ranking final + plan de acción de la sección 7.
