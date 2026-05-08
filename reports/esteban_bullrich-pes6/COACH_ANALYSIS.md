# COACH 360° — Análisis cross-role para esteban bullrich#pes6

Generado a partir de `GLOBAL.md`, `JUNGLE.md`, `TOP.md`, `UTILITY.md`, `MIDDLE.md` y `BOTTOM.md`. Regla aplicada en todo el documento: cuando una métrica no aparece o tiene `N=0`, se declara como insuficiente data o no medido aún.

## Sección 1 — Overview Cross-Role

### 1.1 Identificación del rol natural

| Rol | Games | WR | KDA | CS/m | DPM | Vision |
|---|---:|---:|---:|---:|---:|---:|
| Jungla | 198 | 51.0% | 2.60 | 5.85 | 841 | 33.7 |
| Top | 133 | 50.4% | 1.79 | 6.49 | 931 | 28.4 |
| Support | 72 | 56.9% | 2.28 | 1.07 | 526 | 75.1 |
| Mid | 35 | 40.0% | 2.09 | 5.74 | 950 | 31.0 |
| ADC | 22 | 63.6% | 2.37 | 6.09 | 875 | 25.4 |

La foto transversal muestra una tensión clara: el rol más jugado es Jungla con 198/460 partidas, 43.0% del pool, pero no es el rol de mayor WR: Jungla queda en 51.0% WR, mientras ADC marca 63.6% en 22 partidas y Support 56.9% en 72 partidas [GLOBAL.md sec. 3; JUNGLE.md sec. 1; BOTTOM.md sec. 1; UTILITY.md sec. 1]. ADC tiene sample sólido según la regla de `>=10` partidas, pero todavía mucho menor que Jungla y Support; por eso lo tomo como señal fuerte, no como veredicto definitivo. Support, en cambio, combina sample sólido de 72 partidas, WR 56.9% y late game 60.0% en partidas largas [UTILITY.md sec. 1; UTILITY.md sec. 5], por lo que es el mejor candidato a rol primario competitivo si el objetivo es maximizar WR inmediato.

El rol con mejor WR válido por muestra mínima de 10 partidas es ADC: 63.6% en 22 games [GLOBAL.md sec. 3]. El segundo mejor WR es Support: 56.9% en 72 games [GLOBAL.md sec. 3]. El peor WR es Mid: 40.0% en 35 games, sample sólido y por lo tanto accionable, no una anomalía de 3-4 partidas [GLOBAL.md sec. 3; MIDDLE.md sec. 1]. El mejor KDA es Jungla con 2.60, por encima del global 2.26 por +0.35 [JUNGLE.md sec. 1]; esto no coincide con el mejor WR porque Jungla convierte supervivencia y participación en una tasa de victoria apenas normal, 51.0%, probablemente por el cuello de botella de objetivos: soul rate 0.23 y WR de partidas largas 48.6% [JUNGLE.md sec. 6.1; JUNGLE.md sec. 5].

En DPM relativo al baseline del rol, la mejor señal no es el DPM bruto más alto. Mid tiene el DPM bruto más alto con 950 [GLOBAL.md sec. 3], pero su DPM de timeline es 933 vs baseline Diamond 857, +8.8% [GLOBAL.md sec. 4]. Support tiene DPM 505 vs baseline 409, +23.4%, el mayor delta positivo relativo al rol [GLOBAL.md sec. 4]. Jungla también está positivo, 815 vs 734, +10.9%; Top está 907 vs 830, +9.2%; ADC está negativo, 837 vs 921, -9.2% [GLOBAL.md sec. 4]. Esto importa porque el sistema de baseline corrige expectativa por rol: hacer 526 DPM como Support no supera a 950 de Mid en bruto, pero sí indica que el Support está aportando más daño del esperado para su función.

Conclusión de rol natural: por volumen y KDA, Jungla es el rol más natural en hábitos actuales; por fit estratégico y WR ajustado, Support es el rol más rentable y estable; ADC es el techo de WR pero requiere más muestra y corrección de mid game antes de declararlo rol principal [GLOBAL.md sec. 3; UTILITY.md sec. 5; BOTTOM.md sec. 5].

### 1.2 Inversión de tiempo vs WR

Hay misalignment estratégico. El 43.0% del pool está invertido en Jungla, 198 de 460 partidas, con 51.0% WR [JUNGLE.md sec. 1], mientras Support ocupa 15.7% del pool, 72 de 460 partidas, y gana 56.9% [UTILITY.md sec. 1]. El delta Support vs Jungla es +5.9pp de WR. Si esas 198 partidas de Jungla se hubieran jugado al WR de Support, la expectativa de victorias subiría en 198 x 0.059 = 11.7 victorias netas. No convierto eso a LP exactos porque el reporte no mide LP por victoria/derrota; como proxy competitivo, son 11.7 resultados más favorables sobre el mismo volumen [JUNGLE.md sec. 1; UTILITY.md sec. 1].

Si se compara contra ADC, el delta es mayor: ADC 63.6% vs Jungla 51.0%, +12.6pp, que sobre 198 partidas equivale a 24.9 victorias esperadas adicionales [BOTTOM.md sec. 1; JUNGLE.md sec. 1]. Caveat: ADC tiene 22 partidas, sample sólido pero mucho menor que las 198 de Jungla y 72 de Support. Por eso el plan no debe ser "abandonar todo y spamear ADC" de inmediato; debe ser subir volumen controlado en ADC mientras Support funciona como rol primario de WR y Jungla queda como rol de comodidad.

Top también concentra 133 partidas, 28.9% del pool, con 50.4% WR [TOP.md sec. 1]. Frente a Support, el delta es +6.5pp a favor de Support; sobre 133 partidas, la oportunidad perdida es 8.6 victorias esperadas [TOP.md sec. 1; UTILITY.md sec. 1]. Mid es el mayor costo: 35 partidas, 40.0% WR, -11.5pp contra el global 51.5% y -16.9pp contra Support [MIDDLE.md sec. 1; GLOBAL.md sec. 1; UTILITY.md sec. 1]. Con esa muestra, Mid no debería entrar en SoloQ si el objetivo es ganar LP.

### 1.3 Sinergias humanas globales

| Aliado | Games | WR juntos | Delta vs WR global 51.5% | Lectura |
|---|---:|---:|---:|---|
| DRX BeryL#LASS | 74 | 58.1% | +6.6pp | Mejor palanca global con sample sólido |
| Manuchito#LAS | 175 | 55.4% | +3.9pp | Muy buen volumen y WR estable |
| Neshy Fox#LAS | 192 | 53.1% | +1.6pp | Leve positivo, sample enorme |
| Juampi Torryco#LAS | 189 | 52.9% | +1.4pp | Leve positivo, sample enorme |
| zPikA#UwU | 197 | 50.8% | -0.7pp | Neutro-negativo pese a mucho volumen |

La mejor sinergia humana global es DRX BeryL#LASS: 74 games, 58.1% WR, +6.6pp sobre tu WR global 51.5% [GLOBAL.md sec. 11; GLOBAL.md sec. 1]. Es sample sólido y además no es una señal marginal: +6.6pp en 74 partidas equivale a 4.9 victorias esperadas por encima de tu media. La segunda palanca es Manuchito#LAS: 175 games, 55.4% WR, +3.9pp sobre global [GLOBAL.md sec. 11; GLOBAL.md sec. 1]. Tiene menos diferencial que DRX, pero más del doble de volumen, así que como hábito de queue es muy confiable.

La peor sinergia dentro del top 5 de volumen es zPikA#UwU: 197 games, 50.8% WR, -0.7pp vs global [GLOBAL.md sec. 11]. No es un desastre, pero sí es una señal de oportunidad: es el aliado con más partidas y no mejora tu WR. Fuera del top 5, LuchiTruchi#arg tiene 12 games, 41.7% WR, -9.8pp vs global; sample sólido por la regla de `>=10`, pero muy bajo volumen comparado con zPikA [GLOBAL.md sec. 11]. Si hay que elegir una alerta práctica, reducir zPikA en ranked por volumen y evitar LuchiTruchi cuando el objetivo sea LP.

Sobre patrones por rol del aliado, el archivo lista campeones principales, no roles exactos, así que no invento posiciones fijas. DRX BeryL#LASS aparece con Akali (21), Sylas (9), Leblanc (4), perfil de carries AP/asesinos de mid [GLOBAL.md sec. 11]. Manuchito#LAS aparece con Vayne (21), Mordekaiser (17), Kayle (15), perfil de scalers o side-laners [GLOBAL.md sec. 11]. Neshy Fox#LAS aparece con Kaisa (23), Jinx (20), Aphelios (15), perfil de ADCs de DPS [GLOBAL.md sec. 11]. La lectura causal: tus mejores resultados globales salen cuando alguien aporta amenaza de carry clara, ya sea desde mid/AP o scaling DPS, lo que encaja con tus roles de Jungle/Support porque podés habilitar mapa, engage o frontline sin ser la única condición de daño.

### 1.4 Patrones cruzados de fortalezas y debilidades

El patrón transversal más fuerte es CS temprano bajo baseline en todos los roles. Jungla tiene CS@10 56.6 vs baseline 68.0, -16.8%, y CS@15 87.6 vs 104.3, -16.0% [GLOBAL.md sec. 4]. Top tiene CS@10 61.1 vs 70.3, -13.1%, y CS@15 99.5 vs 111.0, -10.4% [GLOBAL.md sec. 4]. Support también aparece bajo en sus métricas de rol: CS@10 12.3 vs 14.4, -14.3%, y CS@15 18.0 vs 20.7, -12.9% [GLOBAL.md sec. 4]. Mid es el peor: CS@10 58.9 vs 75.8, -22.4%, y CS@15 90.6 vs 115.3, -21.4% [GLOBAL.md sec. 4]. ADC cierra el patrón con CS@10 61.1 vs 75.1, -18.6%, y CS@15 97.3 vs 114.9, -15.3% [GLOBAL.md sec. 4]. Causalmente, esto reduce margen de error: aunque ganes oro por kills o peleas, entrás a mid game con menos recursos estables, lo que obliga a convertir escaramuzas para no quedarte atrás.

El segundo patrón es que la producción de pelea está bien o muy bien salvo en ADC. Jungla tiene DPM 815 vs baseline 734, +10.9%; Top 907 vs 830, +9.2%; Support 505 vs 409, +23.4%; Mid 933 vs 857, +8.8%; ADC 837 vs 921, -9.2% [GLOBAL.md sec. 4]. La mecánica causal es clara: en cuatro roles, tu daño relativo al rol sostiene la partida incluso con CS bajo; en ADC, el rol que más exige DPS sostenido, estás por debajo del baseline. Por eso ADC gana por lane/WR actual, pero su mid game tiene riesgo estructural.

El tercer patrón es vision generalmente útil fuera de Support. Jungla tiene Vision/min 1.06 vs 0.96, +10.3%; Top 0.87 vs 0.80, +9.3%; Mid 0.92 vs 0.75, +22.3%; ADC 0.79 vs 0.68, +16.5% [GLOBAL.md sec. 4]. Support queda negativo: Vision/min 2.36 vs baseline 2.60, -9.2%, y Vision Dominance Ratio 1.02 contra target support pro/diamond+ >1.3 [GLOBAL.md sec. 4; UTILITY.md sec. 6]. Esto explica por qué Support gana pese a no dominar visión: aporta CC, picks y late, pero deja LP en el mapa por no aplastar al support rival en control.

El cuarto patrón es que el early no es el problema general, salvo Top/Support lane. Jungla tiene lane phase win rate 60.6% y lead +286 @14 [JUNGLE.md sec. 5]. Mid tiene 65.7% y +601 [MIDDLE.md sec. 5]. ADC tiene 59.1% y +474 [BOTTOM.md sec. 5]. Top baja a 47.4% y -100 [TOP.md sec. 5]. Support baja a 47.2% y -64 [UTILITY.md sec. 5]. Causalmente, cuando jugás roles con iniciativa individual o daño propio, abrís el early; cuando el rol depende del 2v2 o del matchup largo, el lane state cae debajo de 50%.

### 1.5 Recomendación estratégica de priorización

Priorizaría Support como rol primario de ranked: 72 games, 56.9% WR, +5.4pp vs global 51.5%, late game 60.0% WR en 60 partidas largas y KDA late 3.05 [UTILITY.md sec. 1; UTILITY.md sec. 5]. ADC es el experimento de techo: 22 games, 63.6% WR y lane phase 59.1%, pero DPM 837 vs baseline 921 (-9.2%) y muertes antes del 25' 5.64 lo hacen menos estable [BOTTOM.md sec. 1; BOTTOM.md sec. 4; BOTTOM.md sec. 6]. Jungla debe quedar como secundario de comodidad: 198 games, 51.0% WR, KDA 2.60 y level 6 a 428s, pero soul rate 0.23 limita cierre [JUNGLE.md sec. 1; JUNGLE.md sec. 6; JUNGLE.md sec. 6.1]. Abandonaría Mid en ranked por ahora: 35 games, 40.0% WR, late WR 37.9% y roam conversion -17.31pp [MIDDLE.md sec. 1; MIDDLE.md sec. 5; MIDDLE.md sec. 6.1].

## Sección 2 — Jungla (JUNGLE)

### A) Score 1-5 por stat core

| Stat core | Valor | Score | Evidencia |
|---|---:|---:|---|
| Jungle CS antes del 10' | 60.01 avg | 3/5 | Challenge avg 60.01; CS@10 timeline 56.6 vs baseline 68.0, -16.8% [JUNGLE.md sec. 6; JUNGLE.md sec. 4] |
| Counter-jungle ratio | 0.15 | 2/5 | Ratio 0.15; nota del reporte: <0.3 = pasivo [JUNGLE.md sec. 6] |
| Takedowns en otras lanes early | no medido aún | N/A | N=0 [JUNGLE.md sec. 6] |
| Drakes + Heralds + Barones | 3.35 por partida | 4/5 | Drakes 2.35, Heraldos 0.43, Barones 0.57 [JUNGLE.md sec. 6] |
| Wards río/jungla enemiga | 66.5% | 4/5 | Cobertura 66.5%, N=184 [JUNGLE.md sec. 6] |
| Tempo Index level 6 | 428s | 4/5 | Level 6 avg 428s; nota Lee Sin Diamond ~450s, Karthus ~510s [JUNGLE.md sec. 6] |
| Soul Rate | 0.23 | 2/5 | Soul en 40/175 largas, rate 0.23 [JUNGLE.md sec. 6.1] |
| Gank-to-Death ratio | no medido aún | N/A | N=0 [JUNGLE.md sec. 6] |

Sample: Jungla tiene 198 partidas, sample sólido [JUNGLE.md sec. 1]. Las métricas avanzadas principales tienen N=198 salvo cobertura de wards, N=184, y tiempo a level 6, N=197; por lo tanto son conclusivas [JUNGLE.md sec. 6]. Las dos métricas de gank explícitas, takedowns en otras lanes early y gank-to-death ratio, tienen N=0, así que no medido aún [JUNGLE.md sec. 6].

### B) Fortalezas y debilidades específicas

Fortaleza 1: tu tempo inicial es bueno. Llegás a level 6 en 428 segundos, mejor que la referencia escrita en el reporte para Lee Sin Diamond (~450s) y mucho mejor que Karthus (~510s) [JUNGLE.md sec. 6]. Eso indica que, aunque el CS@10 de timeline esté bajo baseline, no sos lento por defecto: podés activar ultimate temprano. El mecanismo causal es que un jungla con level 6 antes o cerca de 7:08 puede forzar primer dragón, dive bot o pelea de cangrejo con ventaja de spell, siempre que no haya regalado camps.

Fortaleza 2: tenés presión de pelea y participación suficiente. El KP es 53.4% vs baseline 52.1%, +2.6%, y el DPM es 815 vs 734, +10.9% [JUNGLE.md sec. 4]. Además, el early tiene 6.88 takedowns antes del minuto 14 vs target 5.56, score 6.8 [JUNGLE.md sec. 5]. Esto sostiene la hipótesis de jungla proactivo: estás cerca de las jugadas y convertís peleas en daño.

Fortaleza 3: el pool probado tiene picks ganadores. Lee Sin tiene 85 games, 60.0% WR y KDA 2.82; Ekko tiene 11 games, 90.9% WR y KDA 3.07; Gragas tiene 11 games, 63.6% WR y KDA 4.41 [JUNGLE.md sec. 2]. Los tres tienen sample sólido o moderado y cubren estilos distintos: playmaker early, asesino AP y utility AP/tank.

Debilidad 1: el clear deja oro estable sin capturar. CS@10 está 56.6 vs baseline 68.0 (-16.8%) y CS@15 87.6 vs 104.3 (-16.0%) [JUNGLE.md sec. 4]. El challenge de CS de jungla antes del 10' marca 60.01 avg [JUNGLE.md sec. 6], pero el baseline timeline sigue diciendo que estás por debajo del estándar Diamond. Causalmente, si gankeás sin matar o sin objetivo, pagás el costo dos veces: menos camps propios y menos control del respawn enemigo.

Debilidad 2: el counter-jungle es pasivo. Tu counter-jungle ratio es 0.15, y el reporte define <0.3 como pasivo [JUNGLE.md sec. 6]. Además, tenés 9.47 CS de jungla enemiga avg contra 68.18 de tu propia jungla [JUNGLE.md sec. 6]. Eso significa que tu ventaja de tempo no se transforma en starve al rival. Si llegás a level 6 rápido pero no invadís cuando tenés prioridad, el jungla enemigo conserva recursos y puede contestar dragones.

Debilidad 3: el cierre por objetivos es bajo para un jungla con buen early. Tomás 2.35 drakes, 0.43 heraldos y 0.57 barones por partida [JUNGLE.md sec. 6], pero el soul rate es solo 0.23: soul en 40/175 partidas largas [JUNGLE.md sec. 6.1]. La contradicción es importante: estás tocando dragones, pero no encadenás la condición de soul. El late WR de Jungla es 48.6% en partidas >=25' [JUNGLE.md sec. 5], lo que sugiere que los objetivos se toman de forma aislada, no como plan de cierre.

### C) Acciones concretas de la próxima semana

1. Jugá Lee Sin, Ekko o Gragas solo con ruta escrita de primer clear + primer objetivo: Lee Sin 85 games 60.0%, Ekko 11 games 90.9% y Gragas 11 games 63.6% son tus mejores muestras [JUNGLE.md sec. 2]. La métrica a subir es CS@10 de 56.6 hacia 68.0 baseline y CS@15 de 87.6 hacia 104.3 [JUNGLE.md sec. 4].

2. Después de cada gank exitoso, invadí un camp si tenés prioridad: tu ratio de counter-jungle 0.15 está en zona pasiva y el reporte marca <0.3 como pasivo [JUNGLE.md sec. 6]. Objetivo semanal: subir CS de jungla enemiga de 9.47 avg a una meta interna de revisión; el número objetivo exacto no está medido como baseline, así que no invento threshold externo [JUNGLE.md sec. 6].

3. Tratá los dragones como serie, no como evento. Tenés 2.35 drakes por partida, pero solo 0.23 soul rate [JUNGLE.md sec. 6; JUNGLE.md sec. 6.1]. La acción es ward de río/entrada enemiga antes de cada spawn y reset 45 segundos antes; la cobertura ya es 66.5%, así que el problema no parece colocar wards sino convertir esa visión en secuencia de soul [JUNGLE.md sec. 6].

### D) Fase más fuerte y más débil

La fase más fuerte es early: 5.9/10, con lane phase win rate 60.6%, lead +286 @14 y 6.88 takedowns antes del 14 [JUNGLE.md sec. 5]. La más débil es late: 5.5/10, empujada hacia abajo por WR en partidas largas 48.6% pese a KDA late 3.20 [JUNGLE.md sec. 5]. El mecanismo causal es clásico: sobrevivís y participás, pero la condición de cierre no se asegura; el soul rate 0.23 confirma que falta transformar ventaja temprana en objetivo final [JUNGLE.md sec. 6.1].

### E) Matchups y pool ideal

Mejores matchups: Lee Sin vs Graves, 5 games, 100.0% WR, KDA 4.88; Lee Sin vs Shaco, 6 games, 83.3% WR, KDA 4.19; Lee Sin vs Shen, 5 games, 80.0% WR, KDA 3.10 [JUNGLE.md sec. 9]. Peores matchups: Lee Sin vs Diana, 4 games, 0.0% WR, sample chico; Lee Sin vs Fiddlesticks, 4 games, 25.0%, sample chico; Lee Sin vs Briar, 3 games, 33.3%, sample chico [JUNGLE.md sec. 9]. Por sample chico, no son bans obligatorios, pero Diana/Fiddlesticks merecen plan específico: tracking de primer full clear y no pelear sin visión.

Pool ideal: Lee Sin, Ekko, Gragas [JUNGLE.md sec. 2]. Evitar o limitar: Viego, 11 games, 27.3% WR; Talon, 5 games, 20.0% WR; Karthus, 24 games, 45.8% WR, no es desastre pero está por debajo de tus picks top y requiere corregir CS/objetivos [JUNGLE.md sec. 2]. No invento un tercer "malísimo" con sample sólido debajo de 40 fuera de Viego/Talon.

### F) Conexión con GLOBAL

Jungla está apenas por debajo de tu WR global: 51.0% vs 51.5%, -0.5pp [JUNGLE.md sec. 1; GLOBAL.md sec. 1]. Está por encima en KDA: 2.60 vs 2.26, +15.0% relativo aproximadamente, y en CS/min: 5.85 vs 5.30, +10.4% [JUNGLE.md sec. 1; GLOBAL.md sec. 1]. En DPM está casi igual: 841 vs 829, +1.4% [JUNGLE.md sec. 1; GLOBAL.md sec. 1]. La lectura: Jungla es tu rol de comodidad y volumen, pero no tu mayor palanca de LP porque su ventaja individual se queda en KDA/tempo y se diluye en soul/cierre.

### G) Conclusión

Jungla es jugable y natural por volumen, pero para volverlo rol principal de LP tenés que convertir level 6 rápido y buen KP en counter-jungle y soul rate, no en peleas sueltas.

## Sección 3 — Top (TOP)

### A) Score 1-5 por stat core

| Stat core | Valor | Score | Evidencia |
|---|---:|---:|---|
| Gold diff @15 | +33 | 3/5 | Positivo pero pequeño [TOP.md sec. 4] |
| Lane phase WR + lead @14 | 47.4%, -100 | 2/5 | Bajo 50% y lead negativo [TOP.md sec. 5] |
| Solo kills + quick solo kills | 2.54, 0.04 | 4/5 | Mucha kill 1v1, pocos snowballs instantáneos [TOP.md sec. 6] |
| Plates + daño a torres | 9.31, 8943 | 4/5 | Buena traducción a estructuras [TOP.md sec. 6] |
| Daño mitigado | 48222 | 4/5 | Alto valor de frontline/tank [TOP.md sec. 6] |
| Splitpush Index | 0.32 | 3/5 | Entre teamfighter y splitpusher; Fiora/Trynda/Camille esperados 0.4-0.6 [TOP.md sec. 6] |
| KDA en partidas largas | 2.12 | 4/5 | 2.12 vs target 1.81, score 6.3/10 [TOP.md sec. 5] |

Top tiene 133 partidas, sample sólido [TOP.md sec. 1]. Es un rol estable pero no ganador por sí mismo: 50.4% WR, apenas -1.1pp vs global 51.5% [TOP.md sec. 1; GLOBAL.md sec. 1]. El perfil es teamfighter/tank con capacidad de matar, no splitpusher puro.

### B) Fortalezas y debilidades específicas

Fortaleza 1: tu mejor top laner es claramente Ornn. Tiene 20 games, 80.0% WR, KDA 2.31, CS/m 6.49 y DPM 798 [TOP.md sec. 2]. Esto calza con tus métricas de rol: daño mitigado 48222 avg y late KDA 2.12 [TOP.md sec. 6; TOP.md sec. 5]. El mecanismo causal es que Ornn no necesita snowballear lane para aportar valor; aunque tu lane phase WR sea 47.4%, su escalado de upgrades, engage y frontline convierte partidas largas.

Fortaleza 2: cuando peleás, aportás más que el baseline del rol. Top tiene KP 40.7% vs 35.9%, +13.5%, DPM 907 vs 830, +9.2%, y Vision/min 0.87 vs 0.80, +9.3% [TOP.md sec. 4]. Esto es relevante porque un top que participa demasiado puede sacrificar side, pero en tu caso el DPM y late score 5.8 sostienen que la participación tiene valor [TOP.md sec. 5].

Fortaleza 3: el daño a estructuras está presente. Plates tomadas 9.31 por partida y daño a torres 8943 avg [TOP.md sec. 6] sugieren que cuando generás ventana, sí la convertís. El Splitpush Index 0.32 no es de hard splitpusher, pero para pool de Ornn/Malphite/Garen/Jayce indica presión mixta aceptable [TOP.md sec. 2; TOP.md sec. 6].

Debilidad 1: la lane no es dominante. Lane phase win rate 47.4% y lane lead promedio -100 @14 te dejan debajo del target de 50% y lead positivo [TOP.md sec. 5]. Aunque Gold diff @15 sea +33 [TOP.md sec. 4], el oro+exp @14 negativo indica que parte de la recuperación llega después o por kills, no por control limpio de wave. Causalmente, eso vuelve matchups de bruiser más frágiles: si no ganás los primeros tres waves, entrás en trades obligados.

Debilidad 2: morís demasiado temprano. Muertes antes del 10' avg 1.70, con target escrito <0.5 [TOP.md sec. 6]. Esta es una alarma específica de Top: morir antes de 10 no solo entrega oro, también rompe wave state, teleport timing y plates. Explica por qué podés tener solo kills 2.54 por partida y aun así lane phase bajo 50% [TOP.md sec. 6; TOP.md sec. 5].

Debilidad 3: tu pool de carries top no acompaña tus resultados. Garen tiene 18 games, 38.9% WR, KDA 1.58; Jayce 14 games, 35.7% WR, KDA 1.60; Aatrox 8 games, 37.5% WR, KDA 1.44 [TOP.md sec. 2; TOP.md sec. 8]. Son samples sólidos o moderados y todos debajo de 40%. El mecanismo causal: esos campeones necesitan lane más limpia que 47.4% WR y menos muertes tempranas que 1.70 antes del 10' [TOP.md sec. 5; TOP.md sec. 6].

### C) Acciones concretas de la próxima semana

1. En ranked, jugá Top solo si el pick es Ornn o Malphite: Ornn 20 games 80.0% WR y Malphite 10 games 60.0% WR son tus únicos top con >=55% WR y muestra mínima de 5 [TOP.md sec. 7]. La acción reduce exposición a Garen/Jayce/Aatrox, que juntos muestran WR debajo de 40% [TOP.md sec. 8].

2. Primer objetivo de lane: cero muertes antes de 10. Tu métrica actual es 1.70 muertes antes del 10' y el target del reporte es <0.5 [TOP.md sec. 6]. La regla práctica es no usar all-in sin wave bounce o visión de jungla; la métrica de seguimiento es bajar ese 1.70 en las próximas 20 partidas de Top.

3. Si el matchup no permite matar, jugá por plates y teamfight. Tenés plates 9.31 y daño a torres 8943 [TOP.md sec. 6], pero lane lead -100 [TOP.md sec. 5]. Eso pide una decisión: no forzar la lane para arreglar la estadística; con Ornn/Malphite, sobrevivir y llegar a late KDA 2.12 ya es una condición ganadora [TOP.md sec. 5].

### D) Fase más fuerte y más débil

La fase más fuerte es mid game: 5.9/10, con KP 40.7% vs target 35.9, daño/min 906 vs target 830 y vision/min 0.89 vs target 0.80 [TOP.md sec. 5]. Late está cerca, 5.8/10, con WR en partidas largas 51.7% y KDA 2.12 [TOP.md sec. 5]. La fase débil es early: 5.0/10, arrastrada por CS@10 61.11 vs baseline 70.30, lane phase WR 47.4% y lead -100 @14 [TOP.md sec. 5]. La causa no es falta de pelea, porque hay 2.54 solo kills [TOP.md sec. 6]; es inconsistencia de wave y supervivencia.

### E) Matchups y pool ideal

Mejor matchup reportado: Urgot vs Darius, 3 games, 100.0% WR, KDA 2.67, sample chico [TOP.md sec. 9]. Peor matchup reportado: Sion vs Chogath, 3 games, 33.3% WR, KDA 0.83, sample chico [TOP.md sec. 9]. Como todos los matchups de sec. 9 tienen 3 games, son direccionales pero no concluyentes. Ante Chogath, la adaptación recomendada no es ban obligatorio por datos insuficientes; es evitar Sion ciego y priorizar Ornn/Malphite si necesitás frontline.

Pool ideal: Ornn, Malphite y Gragas/Urgot como tercer pick con caveat de sample chico (Gragas 4 games 75.0%, Urgot 4 games 75.0%) [TOP.md sec. 2]. Evitar: Garen, Jayce y Aatrox por WR 38.9%, 35.7% y 37.5% respectivamente [TOP.md sec. 8].

### F) Conexión con GLOBAL

Top está -1.1pp de WR contra global: 50.4% vs 51.5% [TOP.md sec. 1; GLOBAL.md sec. 1]. KDA cae fuerte: 1.79 vs global 2.26, -20.8% relativo aprox. [TOP.md sec. 1; GLOBAL.md sec. 1]. CS/min sube: 6.49 vs 5.30, +22.5%, y DPM sube: 931 vs 829, +12.3% [TOP.md sec. 1; GLOBAL.md sec. 1]. La lectura es que Top mejora farmeo/daño bruto, pero baja supervivencia y conversión a victoria. Es rol secundario viable con pool tanque, no rol de carry abierto.

### G) Conclusión

Top funciona si lo convertís en rol de frontline disciplinado con Ornn/Malphite, pero no como laboratorio de bruisers/carries mientras la lane phase y las muertes antes de 10 sigan castigando.

## Sección 4 — Support (UTILITY)

### A) Score 1-5 por stat core

| Stat core | Valor | Score | Evidencia |
|---|---:|---:|---|
| Vision/min + advantage vs rival | 2.38, +0.0 | 3/5 | Vision/min 2.38; diff vs sup rival +0.0; baseline 2.60, -9.2% [UTILITY.md sec. 6; UTILITY.md sec. 4] |
| Cobertura río/jungla enemiga | 67.6% | 4/5 | N=69 [UTILITY.md sec. 6] |
| Heal+shield + saves | 3347, 0.65 | 3/5 | Heals+shields 3347; saves 0.65 [UTILITY.md sec. 6] |
| CC + picks coordinados | 59.15, 16.54 | 4/5 | CC 59.15; picks 16.54; CC+kill 10.36 [UTILITY.md sec. 6] |
| Vision Dominance Ratio | 1.02 | 2/5 | Target del reporte >1.3 [UTILITY.md sec. 6] |
| Roam impact | 0.08 | 1/5 | Engage/pick sups esperados >2; enchanters 0-1 [UTILITY.md sec. 6] |
| Quest support a tiempo | 0.74 | 3/5 | Quest a tiempo 0.74 [UTILITY.md sec. 6] |

Support tiene 72 partidas, sample sólido, y es el rol con mejor fit ajustado por estabilidad: 56.9% WR, +5.4pp vs global 51.5% [UTILITY.md sec. 1; GLOBAL.md sec. 1]. No es perfecto: la visión no domina al rival y el roam es casi nulo. Pero gana más que tus roles de volumen y tiene late fuerte.

### B) Arquetipo, fortalezas y debilidades específicas

Arquetipo: híbrido engage/enchanter con mejores resultados en enchanter puntual y engage disciplinado. Milio tiene 6 games, 100.0% WR, KDA 5.55; Leona 6 games, 66.7%, KDA 3.50; Thresh 6 games, 66.7%, KDA 3.07 [UTILITY.md sec. 2]. Pyke es el pick más jugado con 12 games, pero solo 41.7% WR y KDA 1.69 [UTILITY.md sec. 2]. Los números avanzados apoyan más engage/control que pick assassin: CC 59.15, picks coordinados 16.54 y CC+kill con aliado 10.36 [UTILITY.md sec. 6].

Fortaleza 1: ganás partidas desde late. Support tiene late score 6.3/10, WR en partidas largas 60.0% y KDA late 3.05 [UTILITY.md sec. 5]. En un rol donde muchas partidas se deciden por visión de baron/soul y peel, ese late positivo es una señal de toma de decisiones decente en cierres.

Fortaleza 2: tu producción de daño para support está muy arriba del baseline. DPM 505 vs baseline 409, +23.4%, el mejor delta relativo entre roles [UTILITY.md sec. 4]. Esto puede venir de Pyke/Lux/Xerath/Maokai o de engages frecuentes, pero el mecanismo es el mismo: no sos un support pasivo que solo wardea; aportás presión real en peleas.

Fortaleza 3: el control activo existe. Control wards 5.39 por partida, wards stealth 24.21, wards enemigas eliminadas 5.96 y cobertura río/jungla enemiga 67.6% [UTILITY.md sec. 6]. Aunque Vision Dominance Ratio no alcance target, el volumen de interacción con visión es alto y puede escalar rápido con mejor timing.

Debilidad 1: no dominás la visión del matchup. Vision/min 2.38 está por debajo del baseline 2.60, -9.2%, y el diff vs support rival es +0.0 [UTILITY.md sec. 4; UTILITY.md sec. 6]. El VDR 1.02 queda lejos del target >1.3 [UTILITY.md sec. 6]. Causalmente, esto significa que colocás suficientes wards para jugar, pero no negás información al rival con ventaja sostenida; por eso una buena cobertura puede no traducirse en picks antes de objetivo.

Debilidad 2: roam impact casi inexistente. Roam impact es 0.08 takedowns en otras lanes [UTILITY.md sec. 6]. El reporte dice que engage/pick sups deberían estar >2 y enchanters 0-1 [UTILITY.md sec. 6]. Como tu pool incluye Pyke, Thresh, Leona y Nautilus [UTILITY.md sec. 2], 0.08 es bajo para el arquetipo. El mecanismo causal es que quedarte bot puede sostener lane, pero deja a mid/jungla sin números en ventanas de río.

Debilidad 3: Pyke/Nautilus no están pagando el riesgo. Pyke tiene 12 games, 41.7% WR, KDA 1.69; Nautilus 5 games, 40.0% WR, KDA 2.16 [UTILITY.md sec. 2]. Si el pick exige snowball y tu roam impact es 0.08, el riesgo del campeón no se convierte en mapa. En cambio, Milio/Leona/Thresh sí convierten con samples moderados [UTILITY.md sec. 2].

### C) Acciones concretas de la próxima semana

1. Convertí cada reset de objetivo en negación, no solo ward. Tu Vision/min es 2.38 vs baseline 2.60 y VDR 1.02 vs target >1.3 [UTILITY.md sec. 4; UTILITY.md sec. 6]. Acción: antes de dragón/baron, entrar con sweeper + control ward y salir con al menos una ward enemiga eliminada; ya eliminás 5.96 por partida, así que medí si sube el VDR, no solo la cantidad [UTILITY.md sec. 6].

2. Si jugás Leona/Thresh, roameá en la primera ventana post-recall. Roam impact 0.08 es incompatible con engage/pick support [UTILITY.md sec. 6]. La condición es que bot wave no quede freezable; si no hay ventana, no fuerces. El objetivo no es inventar roams, es capturar 1-2 jugadas por partida que hoy no existen.

3. Sacá Pyke de ranked por una semana y subí Milio/Leona/Thresh. Pyke tiene 12 games 41.7% WR; Milio 6 games 100.0%, Leona 6 games 66.7%, Thresh 6 games 66.7% [UTILITY.md sec. 2]. Milio es sample moderado, no sentencia eterna, pero la diferencia es lo bastante grande como para probar bloque de 10 partidas.

### D) Fase más fuerte y más débil

La fase más fuerte es late: 6.3/10, con WR en largas 60.0% y KDA 3.05 [UTILITY.md sec. 5]. Early y mid empatan en 5.3/10 [UTILITY.md sec. 5]. El peor arrastre específico en mid es Vision/min 2.38 vs target 2.60, score 4.4, y KP 53.5% vs 54.8, score 4.8 [UTILITY.md sec. 5]. En early, lane phase WR 47.2% y lead -64 @14 muestran que el 2v2 no gana de forma consistente [UTILITY.md sec. 5].

### E) Mejor duo, matchup y pool ideal

Mejor aliado tipo ADC reportado en sec. 10: Jhin, 6 games, 83.3% WR y tu KDA 3.54; Kaisa 10 games, 60.0% WR; Jinx 6 games, 33.3% WR [UTILITY.md sec. 10]. Como persona, DRX BeryL#LASS tiene 8 games, 62.5% WR, sample moderado, y Manuchito#LAS 34 games, 58.8% WR, sample sólido [UTILITY.md sec. 12]. Mejor y peor matchup vs support enemigo no se puede separar: el único matchup con muestra aparece como Lulu vs Thresh, 3 games, 33.3% WR, sample chico; insuficiente data para un ranking real [UTILITY.md sec. 9].

Pool ideal por arquetipo: Milio como enchanter, Leona como engage simple, Thresh como pick/peel flexible [UTILITY.md sec. 2]. Evitar por ahora: Pyke, Nautilus y Maokai/Lulu solo como hipótesis de sample chico; Pyke y Nautilus sí tienen muestra mínima y WR bajo, 41.7% y 40.0% [UTILITY.md sec. 2].

### F) Conexión con GLOBAL

Support está +5.4pp sobre global: 56.9% vs 51.5% [UTILITY.md sec. 1; GLOBAL.md sec. 1]. KDA está casi igual: 2.28 vs 2.26, +0.9% relativo [UTILITY.md sec. 1; GLOBAL.md sec. 1]. Vision avg duplica la media: 75.1 vs 38.0, +37.0 puntos [UTILITY.md sec. 1; GLOBAL.md sec. 1]. DPM cae en bruto, 526 vs 829, pero por baseline del rol está +23.4% [UTILITY.md sec. 1; UTILITY.md sec. 4]. Esto confirma que Support es el mejor rol estratégico: no gana por stats cosméticas, gana porque sus indicadores de rol convierten en WR.

### G) Conclusión

Support es tu rol primario recomendado: gana con muestra sólida, escala bien al late y solo necesita convertir volumen de visión en dominancia real y roams medidos.

## Sección 5 — Mid (MIDDLE)

### A) Score 1-5 por stat core

| Stat core | Valor | Score | Evidencia |
|---|---:|---:|---|
| Lane phase WR + lead @14 | 65.7%, +601 | 5/5 | Muy arriba del target 50% y lead positivo [MIDDLE.md sec. 5] |
| Max CS lead + max level lead | +25.9, +1.6 | 4/5 | Ventajas máximas sólidas [MIDDLE.md sec. 6] |
| Roam impact | 0.43 | 2/5 | Bajo volumen de roams [MIDDLE.md sec. 6] |
| Team damage + DPM | 24.5%, 933 | 4/5 | DPM 933; baseline 857, +8.8% [MIDDLE.md sec. 6; MIDDLE.md sec. 4] |
| Aces antes del 15' | 0.00 | 1/5 | Snowball explosivo no aparece [MIDDLE.md sec. 6] |
| Solo kills | 2.63 | 4/5 | Buena amenaza 1v1 [MIDDLE.md sec. 6] |
| Roam Conversion Rate | 25.0% vs 42.3% | 1/5 | >=2 roams n=4, sample chico; delta -17.31pp [MIDDLE.md sec. 6.1] |
| Synergy WR con Jungla | 44.0% vs 30.0% | 3/5 | Mejor con Neshy, +14pp, pero WR absoluto bajo [MIDDLE.md sec. 6.1] |

Mid tiene 35 partidas, sample sólido, y el resultado global es malo: 40.0% WR, -11.5pp vs global 51.5% [MIDDLE.md sec. 1; GLOBAL.md sec. 1]. Lo raro es que las métricas de lane son excelentes, así que el problema no es ganar prioridad inicial; es convertirla.

### B) Fortalezas y debilidades específicas

Fortaleza 1: ganás la lane en métricas objetivas. Lane phase WR 65.7%, lead +601 @14, Gold diff @15 +344 y takedowns primeros 14' 5.51 vs target 4.09 [MIDDLE.md sec. 5; MIDDLE.md sec. 4]. Esto es muy fuerte para Mid. Causalmente, significa que tenés prioridad para mover primero, ayudar río o castigar resets.

Fortaleza 2: hay amenaza individual. Solo kills 2.63 por partida, max CS lead +25.9 y max level lead +1.6 [MIDDLE.md sec. 6]. No es un mid que pierde mecánicamente. El problema aparece después: si ese lead no se transforma en torres, dragones o control lateral, la ventaja se evapora.

Fortaleza 3: el daño relativo acompaña. DPM 933 vs baseline 857, +8.8%, y % del daño del equipo 24.5% [MIDDLE.md sec. 4; MIDDLE.md sec. 6]. Eso indica que pegás lo suficiente para ser amenaza real. Además, Vision/min 0.92 vs baseline 0.75, +22.3%, sugiere que no estás completamente ciego al mapa [MIDDLE.md sec. 4].

Debilidad 1: el roam te está bajando WR. Con >=2 roams tenés 25.0% WR en n=4, sample chico; con 0 roams tenés 42.3% WR en n=26, sample sólido [MIDDLE.md sec. 6.1]. El delta es -17.31pp [MIDDLE.md sec. 6.1]. Por muestra chica, no concluye que "roamear siempre es malo", pero sí que tus roams actuales no convierten. Causalmente, podés estar saliendo sin wave crash, perdiendo plates/CS, o llegando tarde a side lanes.

Debilidad 2: el late destruye la partida. Early es 6.3/10 y mid 6.1/10, pero late cae a 4.5/10 [MIDDLE.md sec. 5]. WR en partidas largas es 37.9% vs target 50.0%, score 3.2, aunque KDA late 2.49 vs 2.27 no está mal [MIDDLE.md sec. 5]. Esto apunta a toma de decisiones y cierre, no solamente mecánica: sobrevivís razonablemente, pero no ganás las partidas que pasan de 25'.

Debilidad 3: el pool no tiene ancla ganadora con muestra. No hay campeones con >=55% WR y muestra mínima de 5 [MIDDLE.md sec. 7]. Fizz, tu único campeón con sample >=5, tiene 6 games, 33.3% WR, KDA 1.77 [MIDDLE.md sec. 8]. Hwei, Anivia, Lux y otros muestran señales mejores, pero con samples chicos de 2-4 partidas [MIDDLE.md sec. 2]. Sin un pick ancla, el buen early se reparte en demasiados estilos.

### C) Acciones concretas de la próxima semana

1. No roamees antes de crash completo de wave. La evidencia: WR con >=2 roams 25.0% en n=4 vs 42.3% con 0 roams en n=26, delta -17.31pp [MIDDLE.md sec. 6.1]. La regla no es "nunca roam"; es que el roam debe salir de prioridad real, no de impulso.

2. Elegí un bloque de control mages y jugalo 10 partidas antes de volver a asesinos. Hwei tiene 4 games, 50.0% WR y KDA 4.90; Lux 2 games, 50.0% WR y KDA 5.57; Anivia 3 games, 33.3% WR pero DPM 1118 [MIDDLE.md sec. 2]. Samples chicos, no concluyentes, pero son mejores candidatos de estructura que Fizz 6 games 33.3% [MIDDLE.md sec. 8].

3. Tu métrica semanal es late WR, no kills. Ya tenés solo kills 2.63 y lane WR 65.7% [MIDDLE.md sec. 6; MIDDLE.md sec. 5]. La métrica que mata el rol es WR en largas 37.9% [MIDDLE.md sec. 5]. En revisión, marcá cada muerte o pelea tomada sin visión después del minuto 25; el reporte no da esa stat exacta, así que se debe medir manualmente.

### D) Fase más fuerte y más débil

La fase más fuerte es early: 6.3/10, empujada por lane phase WR 65.7%, lead +601 y takedowns early 5.51 [MIDDLE.md sec. 5]. Mid game también es bueno: 6.1/10, con KP 48.6% vs target 43.6, DPM 932 vs target 857 y Vision/min 0.93 vs target 0.75 [MIDDLE.md sec. 5]. La fase débil es late: 4.5/10, con WR en largas 37.9% [MIDDLE.md sec. 5]. El problema causal es conversión: si ganás early y seguís perdiendo late, estás regalando tempo en roams, sides o setups de objetivo.

### E) Champ pool ideal

Pool a probar, con caveat de sample chico: Hwei, Lux y Anivia [MIDDLE.md sec. 2]. No los declaro probados porque Hwei tiene 4 games, Lux 2 y Anivia 3; son direccionales, no concluyentes. Pool a evitar por ahora: Fizz, 6 games, 33.3% WR; Syndra, 2 games, 0.0% WR, sample chico; Zed, 3 games, 33.3%, sample chico [MIDDLE.md sec. 2; MIDDLE.md sec. 8]. Si jugás Mid en flex, que sea para construir muestra, no para ranked serio.

### F) Conexión con GLOBAL

Mid está -11.5pp contra global: 40.0% vs 51.5% [MIDDLE.md sec. 1; GLOBAL.md sec. 1]. KDA está por debajo: 2.09 vs 2.26, -7.5% relativo [MIDDLE.md sec. 1; GLOBAL.md sec. 1]. CS/min está +0.43 sobre global, 5.74 vs 5.30, y DPM está +121, 950 vs 829 [MIDDLE.md sec. 1; GLOBAL.md sec. 1]. Es la señal más peligrosa: las stats brutas parecen buenas, pero el WR es el peor de todos los roles. Eso casi siempre significa mala conversión macro o pool equivocado.

### G) Conclusión

Mid muestra buen laning y daño, pero con 40.0% WR y late 4.5/10 debe salir de ranked hasta que tus roams y cierres de partida dejen de convertir ventajas en derrotas.

## Sección 6 — ADC (BOTTOM)

### A) Score 1-5 por stat core

| Stat core | Valor | Score | Evidencia |
|---|---:|---:|---|
| DPM + % daño equipo | 836, 21.9% | 2/5 | DPM timeline 837 vs baseline 921, -9.2% [BOTTOM.md sec. 6; BOTTOM.md sec. 4] |
| Positioning Index | 1.09 | 4/5 | Target Diamond ADC ~1.0-1.4 [BOTTOM.md sec. 6] |
| Torres antes de plates / first turret | 0.05, 0.00 | 1/5 | Casi sin presión de torre temprana [BOTTOM.md sec. 6] |
| Items legendarios | 0.09 | 1/5 | 0.09 por partida [BOTTOM.md sec. 6] |
| Scaling Score | 0.68 | 2/5 | KDA largas/cortas 0.68 [BOTTOM.md sec. 6.1] |
| Lane phase WR + lead @14 | 59.1%, +474 | 4/5 | Buen 2v2/lane contra ADC rival [BOTTOM.md sec. 5] |
| Muertes antes del 25' | 5.64 | 1/5 | Target <3 por partida [BOTTOM.md sec. 6] |
| Synergy WR con Support | 56.2% vs 83.3% sin él | 2/5 | zPikA 16 games 56.2%, sin él 83.3%, delta -27.08pp [BOTTOM.md sec. 6.1] |

ADC tiene 22 partidas, sample sólido pero todavía pequeño frente a Support/Jungla/Top [BOTTOM.md sec. 1]. El WR 63.6% es el mayor del perfil [BOTTOM.md sec. 1], pero las métricas internas tienen banderas rojas: DPM bajo baseline, 5.64 muertes antes del 25 y scaling ratio 0.68 [BOTTOM.md sec. 4; BOTTOM.md sec. 6; BOTTOM.md sec. 6.1].

### B) Fortalezas y debilidades específicas

Fortaleza 1: ganás lane como ADC. Lane phase WR 59.1%, lead +474 @14, Gold diff @15 +395 y CS diff @15 +6 [BOTTOM.md sec. 5; BOTTOM.md sec. 4]. Esto es relevante porque ADC depende de soporte y wave control; aun así, el reporte te da ventaja objetiva temprana. El mecanismo causal es que llegás a mid game con oro suficiente para pelear si no morís de más.

Fortaleza 2: el posicionamiento medido está dentro del rango target. Positioning Index 1.09, con target Diamond ADC ~1.0-1.4 [BOTTOM.md sec. 6]. No hay señal de "pelea de adelante" por ratio daño hecho/recibido. Caveat: al mismo tiempo tenés 5.64 muertes antes del 25 [BOTTOM.md sec. 6], así que el problema puede no ser exclusivamente positioning en teamfight, sino peleas tomadas antes de spike, catches o resets malos.

Fortaleza 3: Draven funciona como identidad inicial. Draven tiene 8 games, 62.5% WR, KDA 1.89, DPM 840 y damage share 21.6% [BOTTOM.md sec. 2]. Sample moderado, pero es tu único ADC con muestra >=5 y WR >=55 [BOTTOM.md sec. 7]. Encaja con el patrón de lane fuerte y scaling flojo: ganar temprano, cobrar ventaja y cerrar antes de que el ratio largo/corto caiga.

Debilidad 1: el DPS sostenido está bajo baseline para ADC. DPM 837 vs baseline 921, -9.2%, y en sec. 6 DPM avg 836 con team damage 21.9% [BOTTOM.md sec. 4; BOTTOM.md sec. 6]. En ADC, esto es más grave que en otros roles porque tu función principal es daño sostenido. Si ganás lane pero tu DPM queda bajo, el equipo no recibe el payoff esperado en mid game.

Debilidad 2: morís demasiado antes de spike. Muertes antes del 25' avg 5.64, target <3 [BOTTOM.md sec. 6]. Esa stat explica por qué el DPM cae: cada muerte temprana elimina waves, plates, tempo de item y presencia en dragón. También explica por qué el Scaling Score es 0.68: KDA largas 2.44 en n=13 vs KDA cortas 3.60 en n=4 [BOTTOM.md sec. 6.1].

Debilidad 3: no convertís lane en torres. Torres destruidas antes de caer plates 0.05 y first turret rápida 0.00 [BOTTOM.md sec. 6]. Esto contradice lane phase 59.1% y lead +474 [BOTTOM.md sec. 5]. El mecanismo causal probable es que la ventaja de bot se usa para kills o recalls, pero no para placa/first turret, entonces el mapa no se abre.

### C) Acciones concretas de la próxima semana

1. Jugá Draven solo con plan de placa/first turret. Tu Draven tiene 8 games 62.5% WR [BOTTOM.md sec. 2], pero la cuenta global de ADC marca first turret rápida 0.00 y torres pre-plates 0.05 [BOTTOM.md sec. 6]. La meta no es solo matar: si ganás lane, tenés que romper bot o rotar primero.

2. No pelees objetivos si moriste dos veces antes de minuto 14. La stat de muertes antes del 25 es 5.64 contra target <3 [BOTTOM.md sec. 6]. Como tu lane lead es +474 y WR de lane 59.1% [BOTTOM.md sec. 5], el mayor leak no es empezar la partida, es regalar el lead en la transición.

3. Evitá queuear ADC con zPikA como Support si el objetivo es maximizar WR. El análisis cruzado marca zPikA#UwU como mejor duo Support por identificación del reporte, pero con él el WR es 56.2% en n=16 y sin él 83.3% en n=6, delta -27.08pp [BOTTOM.md sec. 6.1]. Caveat: sin él es sample moderado de 6, no concluyente; aun así, no hay evidencia de sinergia positiva.

### D) Fase más fuerte y más débil

La fase más fuerte es late por score: 6.8/10, con WR en partidas largas 66.7% y KDA late 2.62 [BOTTOM.md sec. 5]. Sin embargo, el Scaling Score de sec. 6.1 dice que en partidas >=30' el KDA baja a 2.44 contra 3.60 en partidas cortas, ratio 0.68 [BOTTOM.md sec. 6.1]. Esto no es contradicción total: el late >=25 del reporte es bueno, pero el tramo >=30 muestra caída individual. La fase más débil es mid: 5.2/10, arrastrada por DPM 836 vs target 921, score 4.3 [BOTTOM.md sec. 5]. El problema de ADC es convertir lane fuerte en DPS sostenido sin morir.

### E) Champ pool ideal

Pool que maximiza tus datos actuales: Draven como pick principal por 8 games 62.5% WR; Kaisa como hipótesis de alto techo con 2 games 100.0%, KDA 3.33 y DPM 1192, sample chico; Varus/Ziggs como hipótesis de utilidad/poke con 1 game cada uno, sample insuficiente [BOTTOM.md sec. 2]. Evitar o pausar: Tristana, 1 game 0.0%, sample insuficiente; Jhin, 7 games 42.9%, sample moderado; cualquier scaling carry sin plan de seguridad hasta bajar muertes antes del 25 de 5.64 [BOTTOM.md sec. 2; BOTTOM.md sec. 6].

### F) Mejor duo y matchups

Como persona en ADC, Neshy Fox#LAS tiene 10 games y 70.0% WR; Juampi Torryco#LAS 14 games 64.3%; Manuchito#LAS 16 games 62.5% [BOTTOM.md sec. 12]. Como support específico identificado por el cruce, zPikA#UwU tiene 16 games 56.2%, pero el WR sin él es 83.3% en 6 games, delta -27.08pp [BOTTOM.md sec. 6.1]. Matchups vs duo enemigo: insuficiente data, porque sec. 9 dice sin matchups con muestra suficiente [BOTTOM.md sec. 9]. Aliados support por campeón: Lux 5 games 60.0%, Leona 5 games 60.0%, Xerath 5 games 40.0% [BOTTOM.md sec. 10].

### G) Conexión con GLOBAL

ADC está +12.1pp sobre global: 63.6% vs 51.5% [BOTTOM.md sec. 1; GLOBAL.md sec. 1]. KDA está 2.37 vs 2.26, +4.9% relativo [BOTTOM.md sec. 1; GLOBAL.md sec. 1]. CS/min está 6.09 vs 5.30, +14.9%, y DPM 875 vs 829, +5.5% bruto [BOTTOM.md sec. 1; GLOBAL.md sec. 1]. Pero por baseline ADC, DPM está -9.2% [BOTTOM.md sec. 4]. Lectura: ADC gana mucho en el dataset, pero todavía no cumple el estándar del rol en daño sostenido; es un secundario de alto techo hasta ampliar muestra.

### H) Conclusión

ADC es tu rol de mayor techo de WR, pero antes de volverlo primario tenés que bajar muertes pre-25 y transformar lane lead en torres y DPM.

## Sección 7 — Ranking final + Plan de acción

### 7.1 Ranking de roles (mejor → peor fit estratégico)

| # | Rol | Games | WR | E / M / L | Justificación | Datos clave |
|---:|---|---:|---:|---:|---|---|
| 1 | Support | 72 | 56.9% | 5.3 / 5.3 / 6.3 | Mejor fit estable: WR alto, late fuerte y sample sólido pese a visión mejorable. | WR 56.9% [UTILITY.md sec. 1], Late 6.3/10 [UTILITY.md sec. 5], DPM +23.4% [UTILITY.md sec. 4] |
| 2 | ADC | 22 | 63.6% | 6.0 / 5.2 / 6.8 | Mayor techo de WR, pero sample menor y DPM/muertes impiden hacerlo primario aún. | WR 63.6% [BOTTOM.md sec. 1], DPM -9.2% [BOTTOM.md sec. 4], deaths<25 5.64 [BOTTOM.md sec. 6] |
| 3 | Jungla | 198 | 51.0% | 5.9 / 5.6 / 5.5 | Rol natural por volumen y KDA, limitado por counter-jungle pasivo y soul baja. | KDA 2.60 [JUNGLE.md sec. 1], level 6 428s [JUNGLE.md sec. 6], soul rate 0.23 [JUNGLE.md sec. 6.1] |
| 4 | Top | 133 | 50.4% | 5.0 / 5.9 / 5.8 | Viable con tanques, pero lane débil y pool carry pierde demasiado. | Ornn 80.0% WR [TOP.md sec. 2], lane WR 47.4% [TOP.md sec. 5], deaths<10 1.70 [TOP.md sec. 6] |
| 5 | Mid | 35 | 40.0% | 6.3 / 6.1 / 4.5 | Buen laning, peor WR global por rol y conversión late deficiente. | WR 40.0% [MIDDLE.md sec. 1], lane WR 65.7% [MIDDLE.md sec. 5], late WR 37.9% [MIDDLE.md sec. 5] |

Actualización de coherencia: aunque ADC tiene el WR más alto, el ranking prioriza Support por sample 72 vs 22 y porque ADC tiene DPM -9.2% y 5.64 muertes antes del 25 [BOTTOM.md sec. 4; BOTTOM.md sec. 6]. Por eso Support queda primero como fit estratégico, ADC como techo a validar.

### 7.2 Top 5 acciones accionables cross-role

| # | Acción | Por qué (evidencia con número) | Roles afectados | Esfuerzo |
|---:|---|---|---|---|
| 1 | Queueá Support como rol primario durante 20 partidas | Support gana 56.9% en 72 games vs global 51.5%, +5.4pp [UTILITY.md sec. 1; GLOBAL.md sec. 1] | Support, ranked plan | Bajo |
| 2 | Subí CS@10 con bloques de práctica por rol | Todos los roles están bajo baseline: Jungla -16.8%, Top -13.1%, Mid -22.4%, ADC -18.6% [GLOBAL.md sec. 4] | Jungla, Top, Mid, ADC | Alto |
| 3 | Comprá y usá visión para dominar, no empatar | Support Vision/min 2.38 vs baseline 2.60 y VDR 1.02 vs target >1.3 [UTILITY.md sec. 4; UTILITY.md sec. 6] | Support, Jungla | Medio |
| 4 | Cerrá dragones como serie de soul | Jungla toma 2.35 drakes por partida pero soul rate solo 0.23 [JUNGLE.md sec. 6; JUNGLE.md sec. 6.1] | Jungla, Support, ADC | Medio |
| 5 | Sacá Mid de ranked hasta corregir roams/lategame | Mid tiene 40.0% WR, late WR 37.9% y roams >=2 con 25.0% WR vs 42.3% sin roams [MIDDLE.md sec. 1; MIDDLE.md sec. 5; MIDDLE.md sec. 6.1] | Mid, ranked plan | Bajo |

### 7.3 Cierre del coach jefe

Tu rol primario recomendado para ranked es Support: 56.9% WR en 72 partidas contra 51.5% global, una mejora esperada de +5.4pp de WR; LP exacto no está medido en los reportes [UTILITY.md sec. 1; GLOBAL.md sec. 1]. El secundario sano es Jungla por comodidad, 198 games y KDA 2.60, o ADC como experimento controlado por su 63.6% WR en 22 games [JUNGLE.md sec. 1; BOTTOM.md sec. 1]. No toques Mid en ranked: 35 games, 40.0% WR y late WR 37.9% [MIDDLE.md sec. 1; MIDDLE.md sec. 5]. Tu mejor palanca humana global es DRX BeryL#LASS: 74 games, 58.1% WR vs 51.5% global, +6.6pp [GLOBAL.md sec. 11; GLOBAL.md sec. 1]. Compromiso semanal: 20 partidas de Support, midiendo Vision Dominance Ratio desde 1.02 hacia >1.3 y revisando el sábado si el WR se mantiene sobre 56.9% [UTILITY.md sec. 6].
