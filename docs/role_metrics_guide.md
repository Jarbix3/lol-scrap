# Guía de stats por rol — LoL Coaching

> Catálogo de las métricas más informativas para evaluar el rendimiento de un jugador en su rol específico, con un prompt LLM por rol al final que reemplaza al prompt genérico actual de `Sección 12. Conclusión rápida` cuando se usa el flag `--role`.

## 1. Introducción

Las métricas globales (KDA, WR, kills/deaths/assists) miden **resultados**, no proceso. Para coachear, necesitamos métricas que respondan **"¿hizo lo que su rol exige?"** — y eso cambia drásticamente entre Top/Jungla/Mid/ADC/Sup. Un Sup con 0 kills puede haber ganado la partida (vision dominante, peels perfectos), y un ADC con 15 kills puede haberla perdido (sobreextensión, no scaling).

Cada sección de esta guía:

1. Resume las **dimensiones críticas** del rol (3-4 ejes que definen "jugar bien" ese rol).
2. Lista **stats core** (5-6 métricas indispensables para evaluar al jugador en ese rol).
3. Lista **stats contextuales** (5-8 métricas secundarias útiles para matizar).
4. Cierra con un **prompt LLM específico** que el LLM (Cursor/Claude/GPT) ejecuta sobre el reporte coach generado por `python main.py ... --role <ROL>`.

## 2. Convenciones

Cada métrica tiene un **estado** que indica si está disponible hoy o requiere trabajo:

| Etiqueta | Significado |
|---|---|
| `existente` | Ya se computa por el script. Al lado se cita el archivo donde vive. |
| `derivable` | Se calcula con campos que ya tenemos (`participants[i]` o `participants[i].challenges`). Fórmula clara, no requiere data nueva. Suele ser ~5 líneas de código en `lol_scrap/analytics/role_advanced.py`. |
| `propuesta` | Requiere fuente nueva (timeline frames con resolución por minuto, datos externos, o cálculos no triviales). Indicado en cada caso qué falta. |

Las métricas se nombran con su **key Riot** cuando aplica (ej. `challenges.soloKills`) para que sean trazables al payload de match-v5.

---

## 3. TOP

**Dimensiones críticas del rol**:

1. **Lane dominance**: ganar el 1v1 en isla, traducir presencia en CS/oro/exp/plates.
2. **Splitpush + side-laning**: aplicar presión en los flancos cuando los teamfights no convienen.
3. **Tank value / sustain**: absorber daño y peelear/engagear en pelas largas.
4. **1v1 outplay**: capacidad de matar al rival directamente sin gank.

### 3.1 Stats core

#### `Gold diff @ 15 vs lane opponent` `existente`

- **Definición**: oro propio menos oro del rival directo a los 15 minutos. Requiere timeline.
- **Por qué importa**: traduce la lane phase en ventaja medible. Si Top no convierte el matchup en oro, la presión de splitpush late se diluye.
- **Fuente**: `lol_scrap/analytics/playstyle.py` (`gold_diff15`); `lol_scrap/analytics/game_phases.py` también lo agrega como métrica de Early.

#### `Solo Kills + quickSoloKills` `existente`

- **Definición**: kills 1v1 en lane sin asistencia de jungla/aliados (`quickSoloKills` = los rápidos, antes del minuto 8).
- **Por qué importa**: indicador puro de outplay individual y conocimiento del matchup. Top sin solo kills suele ser pasivo o farmeador puro.
- **Fuente**: `lol_scrap/config.py` `ROLE_ADVANCED_METRICS["TOP"]` → `challenges.soloKills`, `challenges.quickSoloKills`.

#### `Plates tomadas + damageDealtToTurrets` `existente`

- **Definición**: plates que tomé (15 oro c/u + bounty hasta el min 14) y daño total a estructuras.
- **Por qué importa**: traducción de ventaja de lane a objetivo permanente. Top que gana lane y no toma plates no monetiza la ventaja.
- **Fuente**: `lol_scrap/config.py` `ROLE_ADVANCED_METRICS["TOP"]` → `challenges.turretPlatesTaken`, `damageDealtToTurrets`.

#### `damageSelfMitigated / partida` `existente`

- **Definición**: daño absorbido por escudos, armaduras activas, % reducciones (Cho Feast, Mundo passive, Maokai pasiva, etc.).
- **Por qué importa**: en tanks/bruisers es proxy directo de "valor en teamfights". Mitigated alto = el equipo pega detrás de un frontline real.
- **Fuente**: `lol_scrap/config.py` `ROLE_ADVANCED_METRICS["TOP"]` → `damageSelfMitigated`.

#### `Splitpush Index` `derivable`

- **Definición**: ratio `damageDealtToTurrets / max(totalDamageDealtToChampions, 1)`. Cuanto más alto, más oriento mi daño a presión de mapa vs. a teamfights.
- **Por qué importa**: distingue entre Top "splitpusher" (Camille, Fiora, Trynda, Jax → ratio alto, ej. 0.4-0.6) y Top "teamfighter" (Ornn, Mao, K'Sante → ratio bajo, ej. 0.15-0.25). Mismatch entre champ jugado y ratio típico es señal de ejecución incorrecta.
- **Fórmula**: por partida, dividir los dos campos top-level del participant. Promediar sobre la muestra. Implementación: ~5 líneas en `lol_scrap/analytics/role_advanced.py` agregando una entry computada (no una key directa de challenges).

#### `late_kda` (KDA en partidas largas) `existente`

- **Definición**: KDA agregado solo en partidas que llegaron a 25+ minutos. Mide si Top contribuye en teamfights tardíos o si se cae al teamfight quinto.
- **Por qué importa**: muchos Top farmean bien en lane pero pierden teamfights por mal posicionamiento. Esta métrica los expone.
- **Fuente**: `lol_scrap/analytics/game_phases.py` (sección Late).

### 3.2 Stats contextuales

#### `laningPhaseGoldExpAdvantage` `existente`

- **Definición**: rate (0-1) de partidas en las que cierro laning phase con ventaja de oro+exp combinada.
- **Por qué importa**: complemento al gold diff @15: evalúa si la dominación de lane se sostiene hasta el cierre (no solo al @15).
- **Fuente**: `lol_scrap/config.py` → `challenges.laningPhaseGoldExpAdvantage`.

#### `maxCsAdvantageOnLaneOpponent` + `maxLevelLeadLaneOpponent` `existente`

- **Definición**: mayor diferencia de CS (y de level) que tuviste sobre tu rival directo en la partida (peak, no promedio).
- **Por qué importa**: si los maxes son altos pero el gold diff @15 es bajo, significa que lograste leads pero los perdiste por morir / regresar mal. Útil para diagnosticar "lo abre pero no lo cierra".
- **Fuente**: `lol_scrap/config.py` → `challenges.maxCsAdvantageOnLaneOpponent`, `challenges.maxLevelLeadLaneOpponent`.

#### `survivedSingleDigitHpCount` + `tookLargeDamageSurvived` `existente`

- **Definición**: veces que sobreviviste con HP de 1 dígito o resistiendo un burst grande.
- **Por qué importa**: cifra alta = jugás filo (TP/cleanse/heal cycle). Cifra baja en tank = vivís safe sin aprovechar tu rango de HP. Hay que cruzarla con champ jugado.
- **Fuente**: `lol_scrap/config.py` → `challenges.survivedSingleDigitHpCount`, `challenges.tookLargeDamageSurvived`.

#### `won_laning_rate` (proxy de laningPhaseGoldExpAdvantage) `existente`

- **Definición**: rate de laning phase ganada (oro+exp). Aparece como métrica de Early en `game_phases.py`.
- **Por qué importa**: target conceptual = 50% (vs pares del mismo tier). Por encima → estás arriba en lane consistentemente; por debajo → tu rol depende del jungle.
- **Fuente**: `lol_scrap/analytics/game_phases.py` (Early `Won laning rate`).

#### `objective_presence_late` `derivable`

- **Definición**: rate de partidas largas donde participaste en `baronTakedowns >= 1` o `dragonTakedowns >= 3` (una soul al menos).
- **Por qué importa**: top tiende a ausentarse en objetivos late por estar splitpusheando. Esta métrica revela si tu side-laning tradeó bien por objetivos del equipo o no (incluyendo hacer presión que abrió los objetivos).
- **Fórmula**: filtra partidas con `gameDuration >= 25*60`, contá las que tienen baron o soul takedown, dividí por total. Requiere agregación nueva.

#### `Early death rate (<10 min)` `derivable`

- **Definición**: % de partidas donde moriste antes del minuto 10. Requiere timeline para precisión, pero `firstBloodKill` y `challenges.deathsByEnemyChamps` (full game) más timeline pueden derivarlo.
- **Por qué importa**: detecta sobreextensión recurrente o gankeos no respetados. Es la causa #1 de losses en TOP elo Iron-Plat.
- **Fórmula**: del timeline buscar primer `CHAMPION_KILL` event con victim = jugador y timestamp < 600000 ms. Requiere parser de timeline events (no solo frames).

### 3.3 Prompt LLM — TOP

> **Rol del jugador: TOP** — un coach senior de Top lane analiza este reporte. Las **3 dimensiones críticas** del rol son:
>
> 1. **Lane dominance** (gano el 1v1 y lo traduzco en oro/CS/plates).
> 2. **Splitpush + side-laning** (aplico presión cuando los teamfights no convienen).
> 3. **Tank value / sustain en teamfights largos** (sobrevivo y absorbo daño).
>
> Basándote **exclusivamente en los datos del reporte abierto**, hacé lo siguiente:
>
> **A) Score 1-5 por stat core** (1=Pésimo, 2=Bajo, 3=Promedio del tier, 4=Bueno, 5=Excelente). Para cada uno citá el número exacto del reporte:
>
> - Gold diff @ 15 vs rival.
> - Solo kills + quick solo kills.
> - Plates tomadas + daño a torres.
> - Daño mitigado.
> - Splitpush ratio (si existe en el reporte; si no, decí "no medido aún").
> - KDA en partidas largas (`late_kda`).
>
> **B) 3 fortalezas Top-específicas** y **3 debilidades Top-específicas** (no genéricas tipo "tenés bajo KDA" — sí específicas tipo "tu Splitpush ratio es bajo para tus champs (Fiora, Camille) que esperan side-laning agresivo").
>
> **C) 3 acciones concretas para la próxima semana**, contextualizadas al rol Top. Ejemplos del estilo esperado:
>
> - "Cuando lleves Camille/Fiora con `late_kda` < 2, fuerza side-laning después del primer drake en lugar de regroupar; tu winrate cae cuando peleás teamfights largos en estos champs."
> - "Tu `damageSelfMitigated` con Mundo está debajo del baseline Diamond TOP — está construyendo Force of Nature antes que items con health stack que escalan tu pasiva."
>
> **D) Fase del juego más fuerte y más débil** (early/mid/late, según los scores de la sección "Análisis por fase"). Citá el score y la métrica que más arrastra para abajo en la peor fase.
>
> **E) Mejor matchup y peor matchup** (de la sección "Matchups vs campeones"). Sugerí qué hacer ante el peor: ban prioritario, swap a un counter pick, o adaptación de runas.
>
> **F) Conclusión general en 1 oración** sintetizando A-E.
>
> **Regla de oro**: no inventes datos. Si una stat no está en el reporte, decí "insuficiente data".

---

## 4. JUNGLE

**Dimensiones críticas del rol**:

1. **Pathing efficiency**: clear rápido, scuttle control, tempo a level 6.
2. **Counter-jungle**: invade jungla rival, deja al jungler enemigo CS-starved.
3. **Gank impact**: convertís presencia en otras lanes en takedowns/objetivos.
4. **Objective control**: drakes/heralds/barons + soul rate, especialmente en partidas largas.

### 4.1 Stats core

#### `jungleCsBefore10Minutes` `existente`

- **Definición**: monstruos de jungla que kileé antes del minuto 10.
- **Por qué importa**: target Diamond ~50-60. Jungla con `<45` está pateando camps; con `>65` es eficiente o counter-jungleó. Es el pulso del clear.
- **Fuente**: `lol_scrap/config.py` → `challenges.jungleCsBefore10Minutes`.

#### `enemyJungleMonsterKills / alliedJungleMonsterKills` `derivable`

- **Definición**: ratio entre CS de jungla enemiga vs propia. >1 = invader puro; ~0.5-0.8 = balanceado; <0.3 = pasivo.
- **Por qué importa**: distingue entre jungla "carry" (Lee, Kha'Zix, Nidalee → ratio alto) y jungla "tank/setup" (Sejuani, Maokai → ratio bajo). Mismatch champ ↔ ratio = mala ejecución.
- **Fórmula**: dividir los dos campos `challenges.enemyJungleMonsterKills` y `challenges.alliedJungleMonsterKills` por partida, promediar.
- **Fuente**: ambos campos ya están en `lol_scrap/config.py` `ROLE_ADVANCED_METRICS["JUNGLE"]`. Falta el ratio computado.

#### `killsOnOtherLanesEarlyJungleAsLaner` `existente`

- **Definición**: takedowns en otras lanes durante early game (gank impact).
- **Por qué importa**: target Diamond ~3-5 por partida. Jungla con `<2` no está ganando partidas a través de aliados (camps puros) — es un perfil viable solo en champs scaling como Karthus.
- **Fuente**: `lol_scrap/config.py` → `challenges.killsOnOtherLanesEarlyJungleAsLaner`.

#### `dragonTakedowns + riftHeraldTakedowns + baronTakedowns` `existente`

- **Definición**: participación en objetivos épicos por partida.
- **Por qué importa**: jungla es el principal smitor: si tu equipo no toma drakes/herald/baron es responsabilidad tuya orquestar set-ups. Target Diamond combinado: ~6-7 takedowns de objetivos por partida.
- **Fuente**: `lol_scrap/config.py` `ROLE_ADVANCED_METRICS["JUNGLE"]`.

#### `Objective Steal Rate` `derivable`

- **Definición**: `epicMonsterSteals / total_games_in_jungle` — fracción de partidas con al menos un robo de objetivo épico (drake/baron) al rival.
- **Por qué importa**: indica timing de smite y reading del enemigo. Stealer alto = jugada agresiva tipo Lee/Kindred. Stealer 0 con champs como Lee es señal de no jugarlos por su fuerte.
- **Fórmula**: contar partidas con `challenges.epicMonsterSteals >= 1`, dividir por total.
- **Fuente**: `challenges.epicMonsterSteals` ya está en `ROLE_ADVANCED_METRICS["JUNGLE"]`. Falta el rate computado.

#### `controlWardTimeCoverageInRiverOrEnemyHalf` `existente`

- **Definición**: % del tiempo de partida con control wards activos en río o jungla enemiga.
- **Por qué importa**: jungla pro tiene `>30%`. Bajo coverage = invade ciega y muere a counter-ganks. Alta correlación con el winrate.
- **Fuente**: `lol_scrap/config.py` → `challenges.controlWardTimeCoverageInRiverOrEnemyHalf`.

### 4.2 Stats contextuales

#### `takedownsBeforeJungleMinionSpawn` + `initialCrabCount` `existente`

- **Definición**: lvl 2/3 invades exitosos y scuttles iniciales.
- **Por qué importa**: definen el opening del juego. Junglers como Lee/Elise viven de esto; si ambos están en 0, no estás ejecutando esos champs por su fuerte.
- **Fuente**: `lol_scrap/config.py` `ROLE_ADVANCED_METRICS["JUNGLE"]`.

#### `Tempo Index — tiempo a level 6` `propuesta`

- **Definición**: minuto promedio en que llegás al level 6.
- **Por qué importa**: junglers diferencian su momento de ganks/objetivos por timing del 6. Target Diamond Lee Sin: ~7:30 min; Karthus: ~8:30 min. Tempo lento (>9 min) = clear ineficiente.
- **Falta**: parser de timeline events (`SKILL_LEVEL_UP` events o `LEVEL_UP`) — Riot da el array de levels por frame, hay que detectar primer frame con level=6.

#### `Gank-to-Death ratio (early)` `derivable`

- **Definición**: `killsOnOtherLanesEarlyJungleAsLaner / deaths_before_15min`. Cuántos ganks lográs por cada muerte temprana propia.
- **Por qué importa**: junglers que mueren mucho gankeando (Lee con flash agresivo) suelen perder más juegos que los que ganan slow. Ratio >1.5 = eficiente; <0.7 = sobreextiende.
- **Fórmula**: contar deaths antes del 15 desde timeline events; dividir por killsOnOtherLanes early. Requiere parser de timeline.

#### `Soul rate` `derivable`

- **Definición**: % de partidas largas (>=25 min) donde tomé soul (4 drakes).
- **Por qué importa**: la soul es el mayor drop de objetivo del juego. Junglers con `>50%` controlan el bot side; con `<25%` lo ceden.
- **Fórmula**: filtrar partidas largas, contar las que tienen `dragonTakedowns >= 4`, dividir.

### 4.3 Prompt LLM — JUNGLE

> **Rol del jugador: JUNGLE** — un coach senior de Jungla analiza este reporte. Las **4 dimensiones críticas** son:
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
> - Jungle CS antes del 10' (`challenges.jungleCsBefore10Minutes`).
> - Counter-jungle ratio (CS de jungla enemiga ÷ propia).
> - Takedowns en otras lanes early.
> - Drakes + Heralds + Barones por partida (suma).
> - Cobertura de control wards en río/jungla enemiga.
> - Robos de objetivos épicos (rate).
>
> **B) 3 fortalezas Jungle-específicas** y **3 debilidades Jungle-específicas**. Ejemplos buenos:
>
> - "Tu jungle CS @10' (52) está debajo del Diamond baseline (58) → estás pateando camps en favor de ganks, pero tu gank impact (2.1) tampoco está arriba — pathing ineficiente."
> - "Vision en río baja (18%) → tus invades son ciegos y eso explica tus deaths early."
>
> **C) 3 acciones concretas para la próxima semana**, contextualizadas al rol. Estilo esperado:
>
> - "Andá a Lee Sin/Elise sólo si vas a hacer al menos 1 invade y 2 ganks antes del 8'; tu winrate con Lee sin esos comportamientos cae al X%."
> - "Comprá Sweeper desde el 8' antes de cada drake; tu vision dominance se duplicaría."
>
> **D) Fase del juego más fuerte y más débil**. Citá scores de la sección "Análisis por fase".
>
> **E) Champ pool ideal**: dado los datos, ¿qué 3 junglers maximizan tus fortalezas y qué 3 deberías evitar (alta tasa de pérdida en tus dimensiones débiles)?
>
> **F) Conclusión general en 1 oración**.
>
> **Regla de oro**: no inventes datos. Si una stat no está en el reporte, decí "insuficiente data".

---

## 5. MIDDLE

**Dimensiones críticas del rol**:

1. **Lane priority** (presión constante para liberar al jungla).
2. **Roam impact** (visitar side lanes y abrir el mapa).
3. **Damage output / teamfight** (porción del daño del equipo en peleas).
4. **Snowball capacity** (convertir leads en aces tempranos / mejais full).

### 5.1 Stats core

#### `laningPhaseGoldExpAdvantage` `existente`

- **Definición**: rate de cierre de laning phase con ventaja oro+exp.
- **Por qué importa**: mid es el rol con mayor variance de matchups. Si laningAdvantage está debajo de 50%, el champ pool no está adaptado al meta o hay drafting issues (last-pick vs counter).
- **Fuente**: `lol_scrap/config.py` → `challenges.laningPhaseGoldExpAdvantage`.

#### `maxCsAdvantageOnLaneOpponent + maxLevelLeadLaneOpponent` `existente`

- **Definición**: peak de leads en CS y level vs rival directo.
- **Por qué importa**: en mid, lograr 1 level de ventaja es lo que abre ventanas para roams. Champs como Akali/Talon dependen de level 6 antes que el rival.
- **Fuente**: `lol_scrap/config.py` → ambos campos.

#### `killsOnOtherLanesEarlyJungleAsLaner` (ROAM impact) `existente`

- **Definición**: takedowns que conseguiste fuera de tu propia lane (roams a top/bot).
- **Por qué importa**: target Diamond Mid ~3-4. Si está cerca de 0, sos farmer puro (tipo Azir/Cassio); si >5, sos roam-heavy (Twisted Fate, Galio, Talon). Cruzá con champ pool.
- **Fuente**: `lol_scrap/config.py` `ROLE_ADVANCED_METRICS["MIDDLE"]`.

#### `teamDamagePercentage + damagePerMinute` `existente`

- **Definición**: % del daño del equipo + DPM absoluto.
- **Por qué importa**: mid debe ser top-2 del equipo en %. teamDmg <25% en partidas perdidas = no estás haciendo el carry expected. DPM por debajo de baseline diamond mid (857) cuando llevás Syndra/Orianna = build problemática o no peleás teamfights.
- **Fuente**: `lol_scrap/config.py` → ambos campos.

#### `acesBefore15Minutes` `existente`

- **Definición**: aces (5 kills del equipo) antes del 15'.
- **Por qué importa**: snowball capacity. 1 ace en 15' suele cerrar partidas. Mid es el rol que más facilmente las inicia (con jungla).
- **Fuente**: `lol_scrap/config.py` → `challenges.acesBefore15Minutes`.

#### `Roam Conversion Rate` `derivable`

- **Definición**: `killsOnOtherLanesEarlyJungleAsLaner / total_games_mid` ponderado por WR. Cuántos roams convertís por partida y si correlacionan con victoria.
- **Por qué importa**: roamear sin convertir = perdés gold/exp en lane. Una métrica tipo "WR cuando hago >2 roams vs WR cuando hago 0 roams" diagnostica si tu roam helps o hurts.
- **Fórmula**: dividir takedowns en otras lanes por número de partidas. Bonus: split por `win == True` vs `win == False`.

### 5.2 Stats contextuales

#### `mejaisFullStackInTime` `existente`

- **Definición**: rate de partidas donde llegás a Mejais con stacks llenos a tiempo (cuando es óptimo).
- **Por qué importa**: indicador de que estás snowball-aware. Subóptimo en escala absoluta pero fuerte signal cualitativo en mids assassin/burst (Katarina, Akali, LeBlanc).
- **Fuente**: `lol_scrap/config.py` → `challenges.mejaisFullStackInTime`.

#### `multiKillOneSpell` `existente`

- **Definición**: multikills logrados con un solo skill (ej. Syndra W, Velkoz R).
- **Por qué importa**: skill expression en champs que la valoran. Útil para detectar "estás jugando bien la fantasy" en champs como Syndra/Lux.
- **Fuente**: `lol_scrap/config.py` → `challenges.multiKillOneSpell`.

#### `solo Kills` `existente`

- **Definición**: kills 1v1 sin asistencia de jungla.
- **Por qué importa**: en mid es proxy del outplay individual. Diff entre solo kills altos pero gold lead bajos = matás pero perdés CS por morir/recall mal.
- **Fuente**: `lol_scrap/config.py` → `challenges.soloKills`.

#### `Vision presence en enemy half` `derivable`

- **Definición**: para mids con prio, deeper wards (en jungla enemiga). Aproximable con `controlWardTimeCoverageInRiverOrEnemyHalf` (que existe en jungla pero está disponible para mid también).
- **Por qué importa**: mid con prio + vision deep = facilita objetivos. Mid sin prio que igual sale a wardear muere a invades.
- **Fórmula**: ya existe el campo en challenges, falta agregarlo al `ROLE_ADVANCED_METRICS["MIDDLE"]`.

#### `Mid-Jungle synergy WR` `derivable`

- **Definición**: WR cuando jugás con tu jungla más frecuente vs WR sin él.
- **Por qué importa**: mid es el rol más codependiente del jungla. Si tu WR cae 15% sin tu duo de jungla, tu rol independiente es débil.
- **Fórmula**: ya existe la sección de Duo partners en el reporte; falta cruzar con `teamPosition == JUNGLE` para el aliado más frecuente.

### 5.3 Prompt LLM — MIDDLE

> **Rol del jugador: MIDDLE** — coach senior de Mid lane. **4 dimensiones críticas**:
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
> - Ventaja oro+exp al final del laning.
> - Max CS lead + max level lead vs rival.
> - Takedowns en otras lanes (roam impact).
> - % del daño del equipo + DPM.
> - Aces antes del 15'.
> - Solo kills.
>
> **B) 3 fortalezas Mid-específicas** y **3 debilidades Mid-específicas**. Estilo esperado:
>
> - "Tu damagePerMinute (520) está cerca del baseline Diamond Mid (857), pero tu teamDmg% es 22% — significa que pegás poco aunque tus partidas duren mucho; problema de positioning/build."
> - "Roam impact (4.2) está arriba del baseline, pero tu WR en partidas con 3+ roams es 45% vs 62% sin roams → estás roameando en momentos malos."
>
> **C) 3 acciones concretas para la próxima semana**:
>
> - "Si llevás Syndra/Orianna, no roamees antes del minuto 8 a menos que tengas ventaja de wave; estás perdiendo CS @15."
> - "Compra Hexdrinker antes que Sorcerer Boots cuando hay Zed/Talon en banda enemiga — tu survivedSingleDigitHpCount sugiere que necesitás más MR temprano."
>
> **D) Fase del juego más fuerte y más débil**.
>
> **E) Champ pool ideal**: 3 mids que potencian tus fortalezas (si sos roamer agresivo → Twisted Fate, Talon, Galio; si sos farmer → Azir, Cassio, Vex) y 3 que debés evitar.
>
> **F) Conclusión general en 1 oración**.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí "insuficiente data".

---

## 6. BOTTOM (ADC)

**Dimensiones críticas del rol**:

1. **Sustained DPS en teamfights** (DPM + % daño del equipo).
2. **Positioning** (no morir es la regla #1; ratio damage out / damage in).
3. **Scaling** (KDA en partidas largas debe crecer si llevás scaling carries).
4. **Lane priority + plates con sup** (traduce los matchups bot en oro temprano).

### 6.1 Stats core

#### `damagePerMinute + teamDamagePercentage` `existente`

- **Definición**: DPM absoluto + porción del daño del equipo (target ADC: 28-32%).
- **Por qué importa**: ADC sin DPM alto está perdiendo el rol. teamDmg <25% en ADC = no estás haciendo el output expected (suelen ser muertes tempranas en peleas).
- **Fuente**: `lol_scrap/config.py` `ROLE_ADVANCED_METRICS["BOTTOM"]` → `challenges.damagePerMinute`, `challenges.teamDamagePercentage`.

#### `Positioning Index` `derivable`

- **Definición**: ratio `damageDealtToChampions / max(totalDamageTaken, 1)` por partida, promediado.
- **Por qué importa**: la métrica clave del rol — un ADC bien posicionado pega mucho sin recibir tanto. Target Diamond ADC: ~1.0-1.4 (Cait/Jinx/Aphelios). Por debajo de 0.7 = peleás de adelante (mal); por encima de 1.6 = sin riesgo (capaz pasivo).
- **Fórmula**: por partida calcular `participants[i].totalDamageDealtToChampions / max(participants[i].totalDamageTaken, 1)`. Promediar. Implementación: ~5 líneas en `role_advanced.py`.

#### `kTurretsDestroyedBeforePlatesFall + quickFirstTurret` `existente`

- **Definición**: torres tomadas antes que caigan plates (alto valor de oro) + first turret rápida (rate).
- **Por qué importa**: el bot duo (ADC+sup) es el principal tomador de plates. Primera torre bot da bounty grande al ADC. Métrica directa de presión bot.
- **Fuente**: `lol_scrap/config.py` `ROLE_ADVANCED_METRICS["BOTTOM"]`.

#### `legendaryCount` `existente`

- **Definición**: items legendarios completos por partida (avg).
- **Por qué importa**: ADC scaling depende de items completos. Target Diamond por partida promedio ~3.0-3.5. Por debajo de 2.5 = morís mucho o tu equipo ducmanea sin esperar tu spike.
- **Fuente**: `lol_scrap/config.py` → `challenges.legendaryCount`.

#### `Scaling Score` `derivable`

- **Definición**: `KDA en partidas >=30min / KDA en partidas <25min`. Mide cuánto te beneficia la duración del juego.
- **Por qué importa**: ADCs scaling (Vayne, Kog, Twitch) deberían tener scaling >1.5; si está cerca de 1, no estás aprovechando late game (build subóptimo o teamfights antes que tus items spike). ADCs early (Draven, Lucian, Kalista) lo invertido — scaling <1 es esperado pero requiere snowball temprano.
- **Fórmula**: separar partidas en buckets short/long, calcular KDA por bucket, dividir.

#### `laningPhaseGoldExpAdvantage` `existente`

- **Definición**: rate de cierre de laning bot con ventaja oro+exp combinada (vos + tu sup vs el otro duo).
- **Por qué importa**: bot lane es 2v2, así que esta métrica refleja sinergia con tu sup. Si está debajo de 50%, falla el lane pairing o el matchup vs el otro duo.
- **Fuente**: `lol_scrap/config.py` → `challenges.laningPhaseGoldExpAdvantage`.

### 6.2 Stats contextuales

#### `goldPerMinute + survivedSingleDigitHpCount` `existente`

- **Definición**: GPM agregado + veces que sobreviviste con HP de 1 dígito.
- **Por qué importa**: GPM bajo = no estás tomando suficiente CS para tu rol. survivedSingleDigit alto = tenés cleanse/heal cycle bueno o jugás con sup que peelea (Lulu, Janna, Yuumi, Renata).
- **Fuente**: `lol_scrap/config.py` → ambos campos.

#### `dodgeSkillShotsSmallWindow + landSkillShotsEarlyGame` `existente`

- **Definición**: skillshots dodgeados en ventana corta + skillshots conectados early (más relevante para ADCs con skillshot key como Ezreal/Caitlyn/Varus).
- **Por qué importa**: skill expression. ADCs que no esquivan los Q de Blitz/Naut pierden lane phase; los que landean Q de Ezreal scaling traduce a oro extra.
- **Fuente**: `lol_scrap/config.py` → ambos campos.

#### `Death rate antes del 25'` `derivable`

- **Definición**: deaths promedio antes del minuto 25.
- **Por qué importa**: ADCs que mueren mucho early no llegan a su power spike (Phantom Dancer + IE / Eclipse + Collector). Target: <3 deaths antes del 25.
- **Fórmula**: del timeline events, contar muertes con timestamp < 1500000 ms. Requiere timeline parser.

#### `ADC-Sup synergy WR` `derivable`

- **Definición**: WR con tu sup más frecuente vs WR sin él.
- **Por qué importa**: ADCs son el rol más codependiente de sup en lane. Si tu WR cae 20% sin tu duo, no tenés rol independiente.
- **Fórmula**: ya existe la sección de Duo partners en el reporte. Cross con teamPosition == UTILITY.

### 6.3 Prompt LLM — BOTTOM (ADC)

> **Rol del jugador: BOTTOM (ADC)** — coach senior de ADC. **4 dimensiones críticas**:
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
> - DPM + % del daño del equipo (combinar en un solo score).
> - Positioning Index (si está en el reporte; si no, decí "no medido aún" y usá `damageTaken` agregado como proxy).
> - Torres antes de plates / first turret rápida.
> - Items legendarios completados por partida.
> - Scaling Score (si está; si no, comparar KDA en partidas largas vs cortas a ojo).
> - Ventaja oro+exp en laning bot.
>
> **B) 3 fortalezas ADC-específicas** y **3 debilidades ADC-específicas**. Estilo esperado:
>
> - "Tu Positioning Index es 0.75 (target Diamond ~1.1) → estás peleando con poco margen, recibís más daño del que repartís en teamfights."
> - "Llevás Vayne pero tu Scaling Score es 0.9 — estás perdiendo partidas largas con un champ que se suponía favorecía late."
>
> **C) 3 acciones concretas para la próxima semana**:
>
> - "Cuando lleves Cait/Jinx, no peleés antes de Phantom Dancer + IE; mová a side push si tu equipo engagea sin tu spike."
> - "Comprá Stopwatch antes de Phage si hay Malzahar/Zed; tu survivedSingleDigitHpCount es bajo y morís en la primera engage."
> - "Andá a Lucian solo si tenés Nami como sup en el draft (tu mejor synergy según el reporte); WR con otros sups cae al 40%."
>
> **D) Fase del juego más fuerte y más débil**. Citá scores de la sección "Análisis por fase" — un ADC con late score bajo es un sign rojo grande.
>
> **E) Champ pool ideal**: 3 ADCs que maximizan tu rendimiento (basado en sus dimensiones críticas y en los stats de la sección "Champion pool" del reporte) y 3 que deberías sacar.
>
> **F) Mejor sup duo + mejor matchup vs duo enemigo + peor matchup vs duo enemigo**.
>
> **G) Conclusión general en 1 oración**.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí "insuficiente data".

---

## 7. UTILITY (SUPPORT)

**Dimensiones críticas del rol**:

1. **Vision** (control + dominance — el rol más responsable del mapa).
2. **Engage / disengage** (CC chains + saves + picks).
3. **Enable** (heal+shield + facilitar a tu ADC en lane y teamfights).
4. **Roam impact** (presión en otras lanes cuando bot está farmeando).

### 7.1 Stats core

#### `visionScorePerMinute + visionScoreAdvantageLaneOpponent` `existente`

- **Definición**: vision/min absoluto + diff vs sup rival.
- **Por qué importa**: target ADC sup Diamond: 2.0-2.6+ vision/min. visionScoreAdvantage <0 = el otro sup está dominando el mapa, eso explica losses.
- **Fuente**: `lol_scrap/config.py` `ROLE_ADVANCED_METRICS["UTILITY"]`.

#### `controlWardTimeCoverageInRiverOrEnemyHalf` `existente`

- **Definición**: % del tiempo con control wards activos en río o jungla enemiga.
- **Por qué importa**: vision donde más importa (no en base ni en torreta). Sup pro: >25%. Sup pasivo: <10%.
- **Fuente**: `lol_scrap/config.py` → `challenges.controlWardTimeCoverageInRiverOrEnemyHalf`.

#### `effectiveHealAndShielding + saveAllyFromDeath` `existente`

- **Definición**: heal+shield efectivo (no overheal) + saves de aliados de la muerte.
- **Por qué importa**: el "trabajo silencioso" del enchanter sup. Saves alto = peelás bien al carry; bajo = sos engage sup pero entonces deberías tener pickKillWithAlly alto en cambio.
- **Fuente**: `lol_scrap/config.py` → ambos campos.

#### `enemyChampionImmobilizations + pickKillWithAlly` `existente`

- **Definición**: CC sobre enemigos (stuns/snares/roots/airborne) + picks coordinados con aliado.
- **Por qué importa**: indicador del setup engage. Sups engage (Naut, Leona, Pyke, Rakan) deben tener `>15` immobilizations por partida; sups enchanter (Sona, Yuumi, Soraka) menos pero mayor heal/shield.
- **Fuente**: `lol_scrap/config.py` → ambos campos.

#### `Vision Dominance Ratio` `derivable`

- **Definición**: `visionScore_propio / max(visionScore_opp_sup, 1)` por partida. Promediar.
- **Por qué importa**: target sup pro: >1.3. Métrica más directa que `visionScoreAdvantage` porque normaliza por la duración del juego.
- **Fórmula**: encontrar al sup rival (`teamPosition == UTILITY` && `teamId != mine`), tomar su `visionScore`, dividir el mío. Promediar. ~10 líneas.

#### `completeSupportQuestInTime` `existente`

- **Definición**: rate de partidas donde completás la quest del support item antes del corner óptimo.
- **Por qué importa**: timing del Bandle Glaive / Black Mist Scythe / Bloodsong / Solstice impacta directamente tu gold income mid-game. Rate <50% = mala mecánica de stacks o match-up que no permite tradear.
- **Fuente**: `lol_scrap/config.py` → `challenges.completeSupportQuestInTime`.

### 7.2 Stats contextuales

#### `controlWardsPlaced + stealthWardsPlaced` `existente`

- **Definición**: wards puestos por partida (control y stealth/yellow).
- **Por qué importa**: control wards target Diamond Sup: ~3-5 por partida; stealth wards: ~12-18. Si stealth está en 8, estás warding sólo en lane y no jugando objetivos.
- **Fuente**: `lol_scrap/config.py` → ambos campos.

#### `wardTakedowns + wardTakedownsBefore20M` `existente`

- **Definición**: wards enemigas eliminadas + las eliminadas antes del 20'.
- **Por qué importa**: vision war. WardTakedowns altos = tenés Sweeper y lo usás. Bajos = comprás solo Faerie / no tradés vision.
- **Fuente**: `lol_scrap/config.py` → ambos campos.

#### `immobilizeAndKillWithAlly` `existente`

- **Definición**: CC + kill confirmado por aliado por partida.
- **Por qué importa**: métrica de "tu CC se convierte en kills". Si immobilizations altos pero confirma bajo, estás CCeando solo (sin follow-up del equipo) o el CC es por error.
- **Fuente**: `lol_scrap/config.py` → `challenges.immobilizeAndKillWithAlly`.

#### `Roam impact (sup)` `derivable`

- **Definición**: `killsOnOtherLanesEarlyJungleAsLaner` para sup (existe el campo, no está en `ROLE_ADVANCED_METRICS["UTILITY"]`).
- **Por qué importa**: roams sup (post drake bot, recall coordinado al min 8) decisivos. Sups roam (Bard, Pyke, Rakan) deberían tener >2; sups enchanter quizás 0-1.
- **Fórmula**: agregar la entry al `ROLE_ADVANCED_METRICS["UTILITY"]`. Sin nuevo cálculo.

### 7.3 Prompt LLM — UTILITY (SUPPORT)

> **Rol del jugador: UTILITY (SUPPORT)** — coach senior de Support. **4 dimensiones críticas**:
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
> - Vision/min + advantage vs sup rival.
> - Cobertura de control wards en río/jungla enemiga.
> - Heal+shield efectivo + saves de aliados.
> - CC sobre enemigos + picks coordinados.
> - Vision Dominance Ratio (si está; si no, usar advantage como proxy).
> - Rate de quest del support item completada a tiempo.
>
> **B) 3 fortalezas Sup-específicas** y **3 debilidades Sup-específicas**. Identificá primero el **arquetipo del jugador** (engage / enchanter / pick) según los stats y luego evaluá si el champ pool y los números coinciden. Estilo esperado:
>
> - "Sos arquetipo engage (Leona/Naut, immobilizations 18.3) pero tu pickKillWithAlly es 4.1 — el CC va a aire, tu ADC no cierra; es problema de comm o ADC pool."
> - "Vision/min (1.3) está debajo del baseline Diamond Sup (2.6) — no comprás suficientes wards o no los tirás bien al recall; asciende rápido si abres trinket sweeper a partir del minuto 9."
>
> **C) 3 acciones concretas para la próxima semana**:
>
> - "Comprá control ward antes de cada drake (timer en 4:30 + intervalo 5 min); tu drake side vision coverage está en 12% (target 30%)."
> - "Cuando lleves Naut/Leona, ahead solo si tu ADC es Lucian/Draven/Kalista (early-game ADCs); con Cait/Jinx vas a perder lane phase porque ellos quieren stack pasivo."
> - "Practicá Lulu — tu ADC pool está dominado por scalers (Vayne, Jinx) y tu currente sup pool no incluye enchanters fuertes."
>
> **D) Fase del juego más fuerte y más débil**.
>
> **E) Mejor ADC duo + mejor matchup vs sup enemigo + peor matchup vs sup enemigo**.
>
> **F) Champ pool ideal por arquetipo**: si el jugador rinde mejor como engage → 3 sups engage; si como enchanter → 3 enchanters; si como pick → 3 picks (Pyke, Bard, Senna).
>
> **G) Conclusión general en 1 oración**.
>
> **Regla de oro**: no inventes datos. Si una stat no está, decí "insuficiente data".

---

## 8. Métricas universales (apéndice)

Estas aplican a todos los roles y suelen aparecer en la sección 1 (Resumen) y 2 (Champion pool) del reporte. Sirven para grounding pero **no diferencian rol** (ej. KDA alto no te dice si jugaste bien tu rol, solo que no moriste mucho).

| Métrica | Estado | Fuente |
|---|---|---|
| Winrate global | `existente` | `lol_scrap/analytics/champion_pool.py`, sección 1 del reporte |
| KDA agregado | `existente` | `champion_pool.py` |
| Kill participation (KP) | `existente` | `lol_scrap/analytics/playstyle.py`, `game_phases.py` |
| Gold/min (GPM) | `existente` | `playstyle.py` (campo `goldPerMinute` de challenges también) |
| Deaths por partida | `existente` | `lol_scrap/analytics/weaknesses.py` (cross win vs loss) |
| CS/min (global, no @10/@15) | `existente` | `champion_pool.py` |
| Vision score (sin /min) | `existente` | `champion_pool.py` |
| Total damage to champions | `existente` | `champion_pool.py` (campo top-level) |
| Long games winrate (>=25 min) | `existente` | `lol_scrap/analytics/game_phases.py` Late |
| Won laning rate | `existente` | `game_phases.py` Early (target conceptual = 0.5) |

## 9. Roadmap de implementación de stats `derivable`

Si en algún momento querés ampliar el reporte para que estas métricas calculadas estén pre-cocinadas (en lugar de que el LLM tenga que computarlas a ojo desde otros números), este es el orden recomendado por costo/beneficio:

### Tier S — alto impacto, bajo costo (~5 líneas cada una)

1. **Positioning Index para BOTTOM** (`damageDealtToChampions / max(totalDamageTaken, 1)` por partida, mean). Es la métrica que el usuario pidió explícitamente y resume la dimensión más crítica del rol.
2. **Splitpush Index para TOP** (`damageDealtToTurrets / max(totalDamageDealtToChampions, 1)`). Distingue archetipo splitpusher vs teamfighter.
3. **Counter-jungle ratio para JUNGLE** (`enemyJungleMonsterKills / max(alliedJungleMonsterKills, 1)`).
4. **Vision Dominance Ratio para UTILITY** (`visionScore_propio / max(visionScore_opp_sup, 1)` — requiere encontrar al sup rival en cada partida, ~15 líneas).
5. **Roam impact para UTILITY**: agregar `challenges.killsOnOtherLanesEarlyJungleAsLaner` al `ROLE_ADVANCED_METRICS["UTILITY"]`. 1 línea.

Implementación: agregar entries computadas a `lol_scrap/config.py:ROLE_ADVANCED_METRICS` (con un campo `compute` callable nuevo) o crear un módulo `lol_scrap/analytics/derived_metrics.py`. La segunda opción es más limpia.

### Tier A — alto impacto, costo medio (~30-50 líneas)

6. **Roam Conversion Rate para MIDDLE**: cross con WR del jugador en partidas con vs sin roams. Requiere split del champion pool por rate.
7. **Scaling Score para BOTTOM**: bucket de partidas short/long, KDA por bucket, ratio. Requiere agrupación nueva.
8. **Soul rate para JUNGLE**: filtrar partidas largas con `dragonTakedowns >= 4`.
9. **Mid-Jungle synergy WR para MIDDLE / ADC-Sup synergy WR para BOTTOM**: cross sección Duo partners con `teamPosition` del aliado más frecuente.

### Tier B — alto impacto, costo alto (requiere parser de timeline events)

10. **Tempo Index para JUNGLE** (tiempo a level 6).
11. **Early death rate para TOP** (deaths antes del minuto 10 desde timeline events).
12. **Death rate antes del 25' para BOTTOM** (idem).
13. **Gank-to-Death ratio para JUNGLE** (cross deaths early con gank impact).

Estas 4 requieren extender `lol_scrap/analytics/playstyle.py` o un módulo nuevo `lol_scrap/analytics/timeline_events.py` que parsea eventos `CHAMPION_KILL`, `LEVEL_UP`, etc., del payload de timeline-v5 (no solo frames).

### Cómo cablear cada métrica al reporte

Cuando esté implementada, agregar al `report.py` una sub-sección dentro de "Stats avanzadas del rol" (sección que ya aparece cuando se pasa `--role`). El prompt LLM rol-específico de esta guía ya está escrito asumiendo que las métricas pueden estar o no en el reporte (cada bloque dice "si está; si no, decí 'no medido aún'" o "como proxy usá X").

### Cómo usar los prompts LLM hoy

Mientras estas métricas no estén en el reporte:

1. Generá el reporte con `python main.py 'TuNick#TAG' --region las --role <ROL>`.
2. Abrí el `.md` en Cursor.
3. En lugar de pegar el prompt genérico de la sección 12, pegá el prompt rol-específico de esta guía (sección 3.3 / 4.3 / 5.3 / 6.3 / 7.3).
4. El LLM va a contextualizar todo al rol y usar las stats que sí están, marcando explícitamente cuáles faltan.

A medida que vayas implementando las métricas del roadmap, los prompts ganan precisión sin necesidad de reescribirlos — solo dejan de aparecer los avisos "no medido aún".
