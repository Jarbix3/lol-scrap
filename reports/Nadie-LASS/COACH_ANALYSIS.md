# COACH 360° — Análisis cross-role para Nadie#LASS

Generado a partir de `GLOBAL.md`, `BOTTOM.md`, `JUNGLE.md`, `TOP.md`, `MIDDLE.md` y `UTILITY.md`. Regla usada en todo el análisis: cuando el reporte no mide una stat, se declara `insuficiente data` o `no medido aún`; cuando el sample es menor a 5 partidas, se marca como sample chico y direccional, no concluyente.

## Sección 1 — Overview Cross-Role

### 1.1 Identificación del rol natural

| Rol | Games | WR | KDA | CS/m | DPM | Vision |
|---|---:|---:|---:|---:|---:|---:|
| ADC | 430 | 58.1% | 2.60 | 6.69 | 974 | 35.1 |
| Jungla | 71 | 40.8% | 2.41 | 5.31 | 880 | 36.3 |
| Top | 44 | 40.9% | 1.73 | 5.54 | 783 | 30.9 |
| Mid | 32 | 46.9% | 2.28 | 5.60 | 1023 | 35.9 |
| Support | 25 | 44.0% | 2.12 | 1.25 | 562 | 73.2 |

La tabla muestra un rol natural muy claro: ADC tiene 430 partidas, 58.1% WR, KDA 2.60, 6.69 CS/min y 974 DPM [GLOBAL.md sec. 3]. Es el mejor WR con muestra válida porque supera el mínimo de 10 partidas por mucho: 430 games [GLOBAL.md sec. 3]. También es el mejor KDA, con 2.60 frente a Jungla 2.41, Mid 2.28, Support 2.12 y Top 1.73 [GLOBAL.md sec. 3]. El mecanismo es simple: cuando el rol te permite farmear y convertir recursos en daño sostenido, la muerte media baja a 6.4 en ADC frente a 6.7 global, y eso empuja el KDA de 2.60 vs 2.46 global [BOTTOM.md sec. 1; GLOBAL.md sec. 1].

El peor WR absoluto es Jungla con 40.8% en 71 partidas, aunque Top queda prácticamente igual con 40.9% en 44 partidas [GLOBAL.md sec. 3]. La diferencia entre Jungla 40.8% y Top 40.9% es de solo 0.1pp, así que no es significativa; ambos son samples sólidos por ser mayores a 10, pero el rendimiento estratégico es igualmente bajo [GLOBAL.md sec. 3]. Mid tiene el mejor DPM absoluto con 1023 DPM en 32 partidas, pero el mejor DPM relativo a baseline es Support: 527 DPM vs baseline 409, +28.9% [GLOBAL.md sec. 4]. Como Support solo tiene 25 partidas y WR 44.0%, ese daño relativo no compensa la falta de conversión en victoria [GLOBAL.md sec. 3; GLOBAL.md sec. 4].

Comparando contra baseline por rol, ADC produce 939 DPM vs baseline 921, +2.0%, con 1.11 vision/min vs baseline 0.68, +62.8% [GLOBAL.md sec. 4]. Mid produce 1001 DPM vs baseline 857, +16.9%, y 1.06 vision/min vs baseline 0.75, +40.7% [GLOBAL.md sec. 4]. El problema transversal es que el farmeo temprano cae en todos los roles: ADC CS@10 61.0 vs 75.1, -18.8%; Jungla 49.9 vs 68.0, -26.7%; Top 49.2 vs 70.3, -29.9%; Mid 55.9 vs 75.8, -26.3%; Support 11.7 vs 14.4, -18.9% [GLOBAL.md sec. 4].

### 1.2 Inversión de tiempo vs WR

El rol más jugado sí es el de mejor WR: ADC representa 430 de 602 partidas, 71.4% del pool, y gana 58.1% [BOTTOM.md sec. 1; GLOBAL.md sec. 3]. Eso significa que no hay misalignment principal entre inversión de tiempo y rol óptimo; la inversión grande está en el rol correcto. El problema está en el 28.6% restante del pool: 172 partidas fuera de ADC, con 73 wins reales entre Jungla 29W, Top 18W, Mid 15W y Support 11W [JUNGLE.md sec. 1; TOP.md sec. 1; MIDDLE.md sec. 1; UTILITY.md sec. 1]. A WR de ADC 58.1%, esas 172 partidas proyectan 99.9 wins, o +26.9 victorias frente a las 73 reales; el LP exacto es insuficiente data porque los reportes no incluyen LP ganado/perdido por partida, pero la oportunidad medible es +15.7pp de WR sobre el bloque off-role [BOTTOM.md sec. 1; JUNGLE.md sec. 1; TOP.md sec. 1; MIDDLE.md sec. 1; UTILITY.md sec. 1].

Si el objetivo es subir, cada cola off-role tiene que justificarse. Mid es el único secundario con señal aceptable: 46.9% WR en 32 partidas y 1023 DPM [GLOBAL.md sec. 3]. Sigue bajo el 58.1% de ADC por -11.2pp, pero sus fases Early 6.0/10 y Mid 6.8/10 muestran una estructura jugable [MIDDLE.md sec. 5]. Jungla queda -17.3pp contra ADC, Top -17.2pp y Support -14.1pp [GLOBAL.md sec. 3]. Con samples de 71, 44 y 25 respectivamente, no estamos frente a ruido pequeño: son roles que hoy cuestan partidas.

### 1.3 Sinergias humanas globales

La mejor sinergia global por WR con sample útil es ZondaMC#LAS: 51 games juntos, 56.9% WR [GLOBAL.md sec. 11]. El baseline global del jugador es 53.7%, así que el delta es +3.2pp [GLOBAL.md sec. 1; GLOBAL.md sec. 11]. Manuchito#LAS tiene más volumen, 135 games, 56.3% WR, +2.6pp vs 53.7% global [GLOBAL.md sec. 1; GLOBAL.md sec. 11]. La palanca más rentable por combinación de volumen y especialización, sin embargo, es Manuchito en ADC: 73 games, 67.1% WR, mientras ADC total es 58.1%, delta +9.0pp [BOTTOM.md sec. 1; BOTTOM.md sec. 12].

La peor sinergia global con sample útil es PifiKing10#LAS1: 13 games, 46.2% WR, -7.5pp vs el 53.7% global [GLOBAL.md sec. 1; GLOBAL.md sec. 11]. Entre los duos grandes, DRX BeryL#LASS tiene 64 games, 50.0% WR, -3.7pp, y zPikA#UwU tiene 159 games, 50.3% WR, -3.4pp [GLOBAL.md sec. 1; GLOBAL.md sec. 11]. El patrón por rol es claro: te potencian más aliados que estabilizan la frontline o el mapa para ADC. En ADC, Manuchito#LAS aparece con Ornn 9, Kayle 9 y Mordekaiser 9 como top campeones, y gana 67.1% en 73 partidas [BOTTOM.md sec. 12]. ZondaMC#LAS gana 65.2% en 23 partidas ADC con Poppy 5 y Thresh 5 entre top campeones [BOTTOM.md sec. 12]. En cambio, en Support la sinergia con Manuchito baja a 30.0% en 10 games y con zPikA a 38.9% en 18 games [UTILITY.md sec. 12], señal de que el valor humano aparece cuando vos sos carry bot, no cuando delegás la conversión.

### 1.4 Patrones cruzados de fortalezas/debilidades

El patrón transversal más importante es CS temprano bajo. ADC tiene CS@10 61.00 vs 75.10, -18.8%; Jungla 49.87 vs 68.00, -26.7%; Top 49.25 vs 70.30, -29.9%; Mid 55.88 vs 75.80, -26.3%; Support 11.68 vs 14.40, -18.9% [BOTTOM.md sec. 4; JUNGLE.md sec. 4; TOP.md sec. 4; MIDDLE.md sec. 4; UTILITY.md sec. 4]. Como se repite en los cinco roles, no es solo matchup ni pool: es una fuga de recursos por tempo, recall, wave management o pathing. El mecanismo causal es que el déficit de CS fuerza a compensar con kills; cuando las kills no aparecen, el rol cae de golpe. Top lo muestra con CS@10 -29.9%, gold diff @15 -714 y lane phase WR 36.4% [TOP.md sec. 4; TOP.md sec. 5]. Jungla lo muestra con CS@10 -26.7%, gold diff @15 -177 y level 6 promedio 477s [JUNGLE.md sec. 4; JUNGLE.md sec. 6].

La segunda fortaleza transversal es daño y presencia de mid game. Globalmente el Mid game es 6.2/10, con damage/min 898 vs target 867 y vision/min 1.16 vs target 0.81 [GLOBAL.md sec. 5]. ADC sube esto a Mid 6.7/10 con DPM 939 vs 921 y vision/min 1.12 vs 0.68 [BOTTOM.md sec. 5]. Mid lo replica con Mid 6.8/10, DPM 1001 vs 857 y vision/min 1.07 vs 0.75 [MIDDLE.md sec. 5]. Esto indica que el jugador entiende peleas, rotaciones y ventanas de daño cuando llega con recursos mínimos; el cuello de botella está antes.

La tercera debilidad es muerte temprana o conversión negativa fuera de ADC. ADC muere 4.54 veces antes del 25' de promedio, target <3 para ADC, aunque mantiene WR 58.1% [BOTTOM.md sec. 6; BOTTOM.md sec. 1]. Top tiene 1.36 muertes antes del 10', target <0.5, y early score 3.4/10 [TOP.md sec. 6; TOP.md sec. 5]. Support tiene 8.2 deaths promedio y en derrotas sube a 9.43, mientras el WR general del rol es 44.0% [UTILITY.md sec. 1; UTILITY.md sec. 8]. En wins globales las deaths bajan a 5.48 y en losses suben a 8.16, delta -2.68 [GLOBAL.md sec. 7]. El mecanismo: tus victorias no dependen tanto de KP, porque KP solo cambia +0.7pp entre wins y losses, sino de vivir lo suficiente para convertir daño y objetivos [GLOBAL.md sec. 7].

### 1.5 Recomendación estratégica de priorización

Priorizá ADC: tiene 430 games, 58.1% WR, KDA 2.60 y +4.5pp sobre tu WR global de 53.7% [BOTTOM.md sec. 1]. Limitá Jungla y Top en ranked: Jungla tiene 71 games con 40.8% WR y late 4.1/10, Top tiene 44 games con 40.9% WR y early 3.4/10 [JUNGLE.md sec. 1; JUNGLE.md sec. 5; TOP.md sec. 1; TOP.md sec. 5]. Mid puede ser secundario sano para flex/fill porque tiene 46.9% WR, Early 6.0/10 y Mid 6.8/10, aunque su CS@10 está -26.3% vs baseline [MIDDLE.md sec. 1; MIDDLE.md sec. 4; MIDDLE.md sec. 5]. La palanca humana más rentable es queue ADC con Manuchito#LAS: 73 games, 67.1% WR, +9.0pp sobre tu ADC 58.1% y +13.4pp sobre global 53.7% [BOTTOM.md sec. 1; BOTTOM.md sec. 12; GLOBAL.md sec. 1].

## Sección 2 — ADC (BOTTOM)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia | Lectura coach |
|---|---:|---|---|
| DPM + % daño equipo | 4 | DPM 939 y 24.5% del daño del equipo [BOTTOM.md sec. 6]; DPM 939 vs baseline 921, +2.0% [BOTTOM.md sec. 4] | Daño sólido, no hiper-dominante, pero suficiente para sostener 58.1% WR. |
| Positioning Index | 4 | Positioning Index 1.30, target Diamond ADC ~1.0-1.4, n=430 [BOTTOM.md sec. 6] | Estás dentro del rango óptimo: pegás más de lo que recibís sin ser excesivamente pasivo. |
| Torres antes de plates / first turret | 2 | Torres antes de plates 0.10 y first turret rápida total 2 en 430 games [BOTTOM.md sec. 6] | Presión temprana a torre baja para el volumen de ADC. |
| Items legendarios completados | 1 | Items legendarios completados 0.12 por partida, n=430 [BOTTOM.md sec. 6] | La métrica existe pero luce anormalmente baja; se usa como señal direccional, no como diagnóstico aislado. |
| Scaling Score | 2 | KDA largas 3.08 en 256 games vs KDA cortas 5.15 en 63 games; ratio 0.60 [BOTTOM.md sec. 6.1] | El rendimiento cae cuando la partida exige front-to-back late. |
| Lane phase WR + lead @14 | 3 | Lane phase WR 50.9%, lane lead +35, n=430 [BOTTOM.md sec. 5] | Lane aceptable: no aplastás, pero salís levemente arriba. |
| Muertes antes del 25' | 2 | 4.54 deaths antes del 25', target ADC <3 [BOTTOM.md sec. 6] | Llegás a spikes con demasiadas muertes tempranas. |
| Synergy WR con Support | 4 | Con zPikA#UwU 61.6% WR en 73 games vs 57.4% sin él, +4.22pp [BOTTOM.md sec. 6.1] | Duo support rentable, aunque no tan fuerte como Manuchito por persona global ADC. |

### B) Fortalezas y debilidades ADC-específicas

Tu primera fortaleza ADC es que el rol convierte en victoria. ADC tiene 430 de 602 partidas, 71.4% del pool, con 58.1% WR frente a 53.7% global, +4.5pp [BOTTOM.md sec. 1; GLOBAL.md sec. 1]. Ese volumen vuelve el sample sólido y reduce la probabilidad de que el WR sea casual. El mecanismo causal es que ADC combina tus mejores métricas estables: KDA 2.60 vs 2.46 global, CS/min 6.69 vs 6.15 global y daño/min 974 vs 934 global [BOTTOM.md sec. 1]. Cuando el rol te da oro y rango para pegar, tus deaths bajan de 6.7 global a 6.4 ADC, y esa reducción de 0.3 deaths sostiene peleas largas [BOTTOM.md sec. 1; GLOBAL.md sec. 1].

La segunda fortaleza es positioning dentro del rango Diamond. Positioning Index 1.30, n=430, cae justo en el target Diamond ADC ~1.0-1.4 [BOTTOM.md sec. 6]. Esto importa porque ADC no solo necesita DPM; necesita que el daño salga sin regalar shutdown. Con 939 DPM y 24.5% del daño del equipo, el 1.30 indica que no estás comprando daño a costa de morir de frente [BOTTOM.md sec. 6]. La tercera fortaleza es el mid/late general del rol: Mid 6.7/10 y Late 7.2/10, con KDA en largas 3.35 vs target 2.30 y WR largas 56.4% vs target 50.0% [BOTTOM.md sec. 5]. Aunque el Scaling Score cruzado cae vs partidas cortas, tu late ADC filtrado sigue siendo tu mejor fase por rol.

La primera debilidad es el farm temprano. CS@10 61.0 vs baseline 75.1, -18.8%, y CS@15 95.7 vs 114.9, -16.7% [BOTTOM.md sec. 4]. El lane lead +35 y lane WR 50.9% muestran que no estás perdiendo bot por oro+exp total, pero sí estás dejando minions que te retrasan spikes [BOTTOM.md sec. 5]. El mecanismo causal: cuando un ADC llega tarde a segundo/tercer ítem, cada pelea de dragón se juega con menos DPS real aunque el positioning sea correcto.

La segunda debilidad es presión de placas/turret. Torres destruidas antes de caer plates promedian 0.10, y first turret rápida aparece 2 veces en 430 games [BOTTOM.md sec. 6]. Con 50.9% lane phase WR y +35 lead @14, deberías traducir más lanes neutrales-ganadas en plates. La tercera debilidad es muerte antes del spike: 4.54 muertes antes del 25' vs target <3 [BOTTOM.md sec. 6]. Esto explica por qué el KDA en partidas cortas es 5.15 pero baja a 3.08 en largas; si el mid game te cobra shutdowns o tempo, tu scaling pierde valor [BOTTOM.md sec. 6.1].

### C) Acciones concretas para la próxima semana

1. En ADC, jugá ranked con pool reducido `Kaisa` / `Aphelios` / `Jinx` salvo draft extremo: Kaisa tiene 99 games, 62.6% WR; Aphelios 72 games, 59.7% WR; Jinx 59 games, 59.3% WR [BOTTOM.md sec. 2]. El mecanismo es que los tres tienen sample sólido y superan tu WR global 53.7% [GLOBAL.md sec. 1].
2. Durante los primeros 10 minutos, fijá objetivo mínimo de 68 CS antes de pensar en rotar: tu CS@10 real es 61.0 vs baseline 75.1, -18.8% [BOTTOM.md sec. 4]. No hace falta llegar al baseline Diamond completo en una semana; subir 7 minions reduce la pérdida sin cambiar pool.
3. Con ventaja bot, priorizá plate antes que roam o pelea sin wave: tenés lane WR 50.9% y lead +35 @14, pero solo 0.10 torres antes de plates por partida [BOTTOM.md sec. 5; BOTTOM.md sec. 6]. Si ganás la wave y no pegás torre, el valor de lane queda en el aire.

### D) Fases del juego

La fase más fuerte de ADC es Late: 7.2/10, con WR en partidas largas 56.4% y KDA largas 3.35 [BOTTOM.md sec. 5]. La fase más débil es Early: 5.1/10, arrastrada por CS@10 61.00 vs target 75.10 con score 3.6 [BOTTOM.md sec. 5]. El ADC no está roto en lane porque lane WR 50.9% y lead +35 son positivos, pero la baja de CS reduce la velocidad de spikes [BOTTOM.md sec. 5].

### E) Champ pool ideal

Pool ideal principal: Kaisa, Aphelios y Jinx. Kaisa tiene 99 games, 62.6% WR, KDA 2.86; Aphelios 72 games, 59.7% WR, KDA 2.42; Jinx 59 games, 59.3% WR, KDA 2.14 [BOTTOM.md sec. 2]. Pool de burst situacional: Samira tiene 19 games, 73.7% WR y 1242 DPM, sample sólido para pickear con engage claro [BOTTOM.md sec. 2]. Sacaría o limitaría Lucian porque tiene 5 games, 0.0% WR y KDA 1.95, sample moderado por estar entre 5 y 10 pero señal negativa fuerte [BOTTOM.md sec. 8]. Tristana tiene 9 games, 44.4% WR y 28.8% dmg share, sample moderado y WR bajo [BOTTOM.md sec. 2]. Ashe tiene 25 games, 48.0% WR, por debajo de tu ADC 58.1%, aunque su KDA 2.65 no es mala [BOTTOM.md sec. 2; BOTTOM.md sec. 1].

### F) Duo, matchups y sinergias

Mejor support duo medido por 6.1 es zPikA#UwU: 61.6% WR en 73 ADC games vs 57.4% sin él, +4.22pp [BOTTOM.md sec. 6.1]. Mejor persona para ADC por sec. 12 es Manuchito#LAS: 73 games, 67.1% WR, con Ornn/Kayle/Mordekaiser como picks frecuentes [BOTTOM.md sec. 12]. Mejor matchup con sample útil: Kaisa vs Caitlyn tiene 7 games, 100.0% WR, KDA 3.81 y 934 DPM [BOTTOM.md sec. 9]. Jinx vs Twitch también tiene 6 games, 100.0% WR, KDA 2.50 y 807 DPM [BOTTOM.md sec. 9]. Peor matchup útil: Jinx vs MissFortune tiene 6 games, 16.7% WR y KDA 1.54; Kaisa vs Yunara tiene 5 games, 20.0% WR y KDA 1.68 [BOTTOM.md sec. 9]. Ante MissFortune/Jhin, la adaptación es draft defensivo o evitar Jinx si no hay frontline, porque Jinx vs Jhin tiene 6 games, 33.3% WR y KDA 1.79 [BOTTOM.md sec. 9].

### G) Conclusión ADC

ADC es tu rol primario: 58.1% WR en 430 games, late 7.2/10 y Positioning Index 1.30 sostienen el carry, pero CS@10 -18.8% y 4.54 muertes antes del 25' limitan cuánto escalás [BOTTOM.md sec. 1; BOTTOM.md sec. 4; BOTTOM.md sec. 5; BOTTOM.md sec. 6].

### Conexión con GLOBAL

ADC está +4.5pp WR sobre global: 58.1% vs 53.7% [BOTTOM.md sec. 1; GLOBAL.md sec. 1]. Está +5.7% en CS/min relativo: 6.69 vs 6.15, delta +0.54 CS/min [BOTTOM.md sec. 1; GLOBAL.md sec. 1]. Está +4.3% en daño/min: 974 vs 934, delta +40 [BOTTOM.md sec. 1; GLOBAL.md sec. 1]. El único indicador global donde ADC cae es vision avg, 35.1 vs 36.6, delta -1.5, pero ADC no necesita igualar al promedio global contaminado por Support 73.2 vision [BOTTOM.md sec. 1; GLOBAL.md sec. 3]. En resumen, ADC está sobre tu media en WR, KDA, CS y daño: es tu rol natural.

## Sección 3 — Jungla (JUNGLE)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia | Lectura coach |
|---|---:|---|---|
| Jungle CS antes del 10' | 2 | 54.01 CS jungla antes del 10', n=71 [JUNGLE.md sec. 6]; CS@10 49.87 vs baseline 68.00, -26.7% [JUNGLE.md sec. 4] | Clear bajo para Diamond. |
| Counter-jungle ratio | 1 | Ratio 0.08, CS enemiga 5.34 vs propia 65.49 [JUNGLE.md sec. 6] | Jungla muy pasiva en invade/starve. |
| Takedowns otras lanes early | N/M | N=0, no medido aún [JUNGLE.md sec. 6] | Insuficiente data específica de ganks a lanes. |
| Drakes + heralds + barones | 3 | Drakes 1.70, heraldos 0.42, barones 0.32 por partida [JUNGLE.md sec. 6] | Objetivos existen, pero no cierran soul. |
| Cobertura río/jungla enemiga | 4 | 61.0% cobertura, n=66 [JUNGLE.md sec. 6] | Buena base de información territorial. |
| Tempo a level 6 | 2 | Level 6 promedio 477s, n=71 [JUNGLE.md sec. 6] | Lento para junglas de tempo agresivo; aceptable solo para picks scaling. |
| Soul Rate | 1 | Soul en 5/62 partidas largas, 8% [JUNGLE.md sec. 6.1] | Control de win condition de dragón muy bajo. |
| Gank-to-Death ratio | N/M | N=0, no medido aún [JUNGLE.md sec. 6] | No se puede evaluar ratio gank/death. |

### B) Fortalezas y debilidades JUNGLE-específicas

La primera fortaleza de Jungla es que, cuando peleás, aportás daño y participación. KP 54.6% vs baseline 52.1%, +4.8%, y DPM 838 vs baseline 734, +14.2% [JUNGLE.md sec. 4]. En Mid game eso se traduce en score 5.9/10, con damage/min 838 vs target 734 y vision/min 1.13 vs target 0.96 [JUNGLE.md sec. 5]. El mecanismo causal es que el rol no falla por ausencia total en peleas: tus kills promedio son 8.7 y assists 10.0, por encima de global en kills +0.4 y assists +1.8 [JUNGLE.md sec. 1; GLOBAL.md sec. 1].

La segunda fortaleza es cobertura de visión de jungla/río: 61.0% en 66 partidas [JUNGLE.md sec. 6]. Para jungla, esa cobertura debería habilitar invades o setups de dragón. La tercera fortaleza es que el primer scuttle y scuttle total son medidos con 1.07 scuttles iniciales y 3.54 scuttles totales por partida [JUNGLE.md sec. 6]. No hay baseline directo en el reporte, pero muestra que interactuás con río; el problema es convertir eso en soul.

La primera debilidad es pathing efficiency. CS@10 49.87 vs 68.00, -26.7%, y CS@15 78.79 vs 104.30, -24.5% [JUNGLE.md sec. 4]. Además, level 6 llega a 477s [JUNGLE.md sec. 6]. Si un jungla llega tarde a level 6 y además no invade, pierde ventanas de tempo para primer Herald, segundo dragón y dives. La segunda debilidad es counter-jungle casi inexistente: CS enemiga 5.34, propia 65.49 y Counter-jungle ratio 0.08 [JUNGLE.md sec. 6]. Como el reporte define <0.3 como pasivo, 0.08 es extremadamente bajo [JUNGLE.md sec. 6]. El mecanismo causal es que el rival conserva camps, niveles y rutas, entonces tu cobertura de visión no genera castigo.

La tercera debilidad es objective conversion. Drakes 1.70 por partida no está mal como conteo bruto, pero Soul Rate 8% en 62 partidas largas es muy bajo [JUNGLE.md sec. 6; JUNGLE.md sec. 6.1]. El WR en partidas largas de Jungla es 38.7% vs target 50.0%, score 3.3, y el Late total es 4.1/10 [JUNGLE.md sec. 5]. Esto indica que llegar a late como jungla no te favorece: cedés soul o no armás condición de cierre.

### C) Acciones concretas para la próxima semana

1. No pickees LeeSin en ranked hasta corregir el plan de early: LeeSin tiene 10 games, 20.0% WR y KDA 2.10 [JUNGLE.md sec. 2; JUNGLE.md sec. 8]. Si querés usarlo, la condición debe ser un plan explícito de tempo, porque tu CS@10 está -26.7% y tu counter-jungle ratio es 0.08 [JUNGLE.md sec. 4; JUNGLE.md sec. 6].
2. Antes de minuto 4:30, jugá cada path con salida hacia dragón o reset para visión: Soul Rate 8% en 62 partidas largas y WR largas 38.7% muestran que la partida se cae por objetivos acumulativos [JUNGLE.md sec. 6.1; JUNGLE.md sec. 5].
3. Subí invade mínimo a 10 CS enemiga promedio cuando tengas prio: hoy tenés 5.34 CS de jungla enemiga y 65.49 de propia, ratio 0.08 [JUNGLE.md sec. 6]. No se trata de invadir a ciegas; tu cobertura río/jungla enemiga 61.0% ya da base para hacerlo [JUNGLE.md sec. 6].

### D) Fases del juego

La fase más fuerte es Mid game con 5.9/10, sostenida por KP 54.6%, DPM 838 y vision/min 1.13 [JUNGLE.md sec. 5]. La más débil es Late con 4.1/10, arrastrada por WR largas 38.7% vs target 50.0% [JUNGLE.md sec. 5]. Early también está bajo con 4.7/10, especialmente por CS@10 49.87 vs target 68.00 [JUNGLE.md sec. 5]. La lectura: no estás tan lejos en peleas de minuto 15-25, pero entrás con menos recursos y cerrás mal por soul.

### E) Champ pool ideal

Con los datos disponibles, el único jungla con >=55% WR y mínimo 5 partidas es Ambessa: 5 games, 60.0% WR, KDA 2.66; sample moderado, direccional pero no concluyente [JUNGLE.md sec. 7]. Evelynn tiene 6 games, 50.0% WR y KDA 2.49; sample moderado y neutral [JUNGLE.md sec. 2]. Zac tiene 5 games, 40.0% WR pero KDA 3.07; sample moderado con WR bajo [JUNGLE.md sec. 2]. Evitaría LeeSin, 10 games, 20.0% WR, y MasterYi, 7 games, 28.6% WR [JUNGLE.md sec. 8]. Khazix tiene 5 games, 40.0% WR y 1104 DPM, sample moderado pero sin conversión suficiente [JUNGLE.md sec. 2]. No hay datos suficientes para recomendar tres junglas "ideales" con confianza fuerte; el reporte solo sostiene Ambessa como señal positiva moderada [JUNGLE.md sec. 7].

### F) Conclusión Jungla

Jungla no debería ser ranked primario: 40.8% WR en 71 games, CS@10 -26.7%, counter-jungle ratio 0.08 y Soul Rate 8% muestran que el rol pierde por tempo y objetivos, aunque el daño de mid game esté +14.2% sobre baseline [JUNGLE.md sec. 1; JUNGLE.md sec. 4; JUNGLE.md sec. 6; JUNGLE.md sec. 6.1].

### Conexión con GLOBAL

Jungla está -12.8pp WR bajo global: 40.8% vs 53.7% [JUNGLE.md sec. 1; GLOBAL.md sec. 1]. KDA casi empata, 2.41 vs 2.46, delta -0.05, pero eso oculta deaths más altas: 7.8 vs 6.7, +1.1 [JUNGLE.md sec. 1; GLOBAL.md sec. 1]. CS/min cae a 5.31 vs 6.15, delta -0.85, y DPM cae a 880 vs 934, delta -54 [JUNGLE.md sec. 1; GLOBAL.md sec. 1]. El rol no es desastroso por manos en pelea, porque DPM vs baseline jungla está +14.2%, pero sí está por debajo de tu media cross-role en resultado y recursos [JUNGLE.md sec. 4].

## Sección 4 — Top (TOP)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia | Lectura coach |
|---|---:|---|---|
| Gold diff @15 | 1 | -714 vs rival [TOP.md sec. 4] | Lane queda demasiado atrás para Top. |
| Lane WR + lead @14 | 1 | Lane WR 36.4%, lane lead -923 [TOP.md sec. 5] | Problema serio de laning. |
| Solo kills + quick solo kills | 4 | Solo kills 2.00 por partida, quick solo kills 0.00 [TOP.md sec. 6] | Hay capacidad de kill, pero no snowball instantáneo. |
| Plates + daño a torres | 4 | Plates 4.57 y daño a torres 5813 [TOP.md sec. 6] | Cuando llegás a pegar torre, generás estructura. |
| Daño mitigado | 4 | Daño mitigado 39590 promedio [TOP.md sec. 6] | Buen valor de aguante, aunque sin baseline directo. |
| Splitpush Index | 2 | 0.23, n=44; teamfighters ~0.15-0.25 y splitpushers ~0.4-0.6 [TOP.md sec. 6] | Correcto para tanques, bajo para Camille/Jax/Ambessa. |
| KDA partidas largas | 4 | KDA largas 2.10 vs target 1.81, score 6.2 [TOP.md sec. 5] | Si sobrevivís a lane, late KDA no es el problema principal. |

### B) Fortalezas y debilidades TOP-específicas

La fortaleza más concreta en Top es la capacidad de generar acciones individuales: 2.00 solo kills por partida en 44 games [TOP.md sec. 6]. Eso indica que no estás completamente pasivo en el 1v1. Además, max CS lead vs rival +17.5 y max level lead +1.4 muestran que en algunas ventanas sí abrís ventaja puntual [TOP.md sec. 6]. El problema es que esas ventajas no dominan el promedio de lane: gold diff @15 es -714 y lane lead @14 es -923 [TOP.md sec. 4; TOP.md sec. 5]. El mecanismo causal es inconsistencia: encontrás kills, pero el costo en wave/deaths/tempo supera el premio.

La segunda fortaleza es valor de estructura cuando podés jugar side. Plates tomadas 4.57 por partida y daño a torres 5813 son altos como output bruto [TOP.md sec. 6]. Sin embargo, el Splitpush Index 0.23 ubica tu perfil más cerca de teamfighter/tank que de splitpusher puro, porque el propio reporte marca 0.15-0.25 para teamfighters y 0.4-0.6 para splitpushers [TOP.md sec. 6]. Eso significa que si elegís Camille/Jax/Ambessa esperando side-lane permanente, tus números no acompañan todavía. La tercera fortaleza es aguante: daño mitigado 39590 y KDA largas 2.10 vs target 1.81 [TOP.md sec. 6; TOP.md sec. 5]. Como Top suele absorber presión, ese KDA late decente sugiere que el error no es solo teamfight.

La primera debilidad es la lane. Early 3.4/10, CS@10 49.25 vs 70.30, gold diff @15 -714, lane WR 36.4% y lane lead -923 son cinco señales alineadas [TOP.md sec. 5]. Con 44 partidas, sample sólido. El mecanismo causal: Top es un rol de isla; si salís -923 oro+exp @14, tu jungla pierde Herald, tu mid pierde presión de side y tu ADC recibe menos frontline. La segunda debilidad es muerte temprana: 1.36 deaths antes del 10' vs target <0.5 [TOP.md sec. 6]. Eso explica parte del -714 @15 y hace que tus 2.00 solo kills no se conviertan en ventaja neta [TOP.md sec. 4; TOP.md sec. 6].

La tercera debilidad es pool. Ambessa tiene 10 games, 20.0% WR y KDA 1.34 [TOP.md sec. 2; TOP.md sec. 8]. Es el único campeón Top con sample >=10 y sale muy negativo. Gnar tiene 5 games, 60.0% WR y KDA 2.17, pero sample moderado; es dirección positiva, no prueba definitiva [TOP.md sec. 7]. Como los demás picks tienen 3 games o menos, son sample chico y no concluyentes [TOP.md sec. 2].

### C) Acciones concretas para la próxima semana

1. Sacá Ambessa Top de ranked hasta tener plan de lane: 10 games, 20.0% WR, KDA 1.34 [TOP.md sec. 8]. Tu early Top ya es 3.4/10 y Ambessa amplifica un perfil que necesita ventaja mecánica [TOP.md sec. 5].
2. Primer objetivo Top: no morir antes de 10'. Hoy tenés 1.36 deaths antes del 10' vs target <0.5 [TOP.md sec. 6]. Bajar eso ataca directamente el gold diff @15 de -714 [TOP.md sec. 4].
3. Jugá Gnar como pick de estabilización si vas Top: 5 games, 60.0% WR, KDA 2.17, sample moderado [TOP.md sec. 7]. No lo tomes como "main definitivo", pero sí como prueba controlada frente a Ambessa.

### D) Fases del juego

La fase más fuerte es Mid game con 5.4/10, sostenida por KP 37.2% vs target 35.9 y vision/min 0.99 vs target 0.80 [TOP.md sec. 5]. La más débil es Early con 3.4/10, arrastrada por CS@10 49.25 vs target 70.30, gold diff @15 -714, lane WR 36.4% y lane lead -923 [TOP.md sec. 5]. Late queda 4.9/10, no excelente pero menos grave que lane, con KDA largas 2.10 vs target 1.81 y WR largas 40.5% [TOP.md sec. 5].

### E) Matchups

El reporte declara `sin matchups con muestra suficiente` para Top, mínimo 3 enfrentamientos [TOP.md sec. 9]. Por lo tanto, no hay mejor matchup ni peor matchup confiable. La adaptación recomendada no puede ser ban por matchup específico; debe ser ban o dodge por condición de campeón propio. En ranked, el ajuste sustentado es evitar Ambessa Top por 10 games, 20.0% WR, y preferir Gnar cuando el draft lo permite por 5 games, 60.0% WR [TOP.md sec. 8; TOP.md sec. 7].

### F) Conclusión Top

Top hoy es rol a evitar en ranked: 40.9% WR en 44 games, Early 3.4/10, gold diff @15 -714 y lane lead -923 pesan más que las 2.00 solo kills y el KDA late 2.10 [TOP.md sec. 1; TOP.md sec. 4; TOP.md sec. 5; TOP.md sec. 6].

### Conexión con GLOBAL

Top está -12.7pp WR bajo global: 40.9% vs 53.7% [TOP.md sec. 1; GLOBAL.md sec. 1]. KDA cae de 2.46 global a 1.73 Top, delta -0.73, una baja de -29.7% relativa [TOP.md sec. 1; GLOBAL.md sec. 1]. CS/min baja de 6.15 a 5.54, delta -0.61, y daño/min cae de 934 a 783, delta -151 [TOP.md sec. 1; GLOBAL.md sec. 1]. Comparado con la distribución global, Top también tiene vision 30.9 vs global 36.6, -5.7 [TOP.md sec. 1; GLOBAL.md sec. 1]. La conclusión cross-role es dura: Top no es representativo de tu nivel ADC; es un off-role que te baja resultado y economía.

## Sección 5 — Mid (MIDDLE)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia | Lectura coach |
|---|---:|---|---|
| Lane phase WR + lead @14 | 5 | Lane WR 64.5%, lane lead +535, gold diff @15 +207 [MIDDLE.md sec. 5] | Tu mejor laning off-role. |
| Max CS + level lead | 4 | Max CS lead +30.4 y max level lead +1.8 [MIDDLE.md sec. 6] | Abrís ventanas claras de ventaja. |
| Roam impact | 1 | Takedowns en otras lanes 0.34 [MIDDLE.md sec. 6] | Roam bajo y poco convertido. |
| % daño equipo + DPM | 5 | 25.4% daño equipo y DPM 1001 [MIDDLE.md sec. 6]; DPM +16.9% vs baseline [MIDDLE.md sec. 4] | Perfil de daño real. |
| Aces antes del 15' | 1 | 0.00 por partida, n=32 [MIDDLE.md sec. 6] | Sin snowball explosivo medido. |
| Solo kills | 5 | 2.97 por partida, n=32 [MIDDLE.md sec. 6] | Mucha amenaza individual. |
| Roam Conversion Rate | N/M | Con >=2 roams: 0.0% WR, n=1; sample chico [MIDDLE.md sec. 6.1] | No concluyente, pero señal negativa. |
| Synergy WR con Jungla | 5 | Con Juampi 66.7% en 12 games vs 35.0% sin él, +31.67pp [MIDDLE.md sec. 6.1] | Duo jungla muy rentable. |

### B) Fortalezas y debilidades MID-específicas

Mid es tu mejor off-role por estructura de fase. Tiene 46.9% WR en 32 games, todavía bajo tu global 53.7%, pero muestra Early 6.0/10 y Mid 6.8/10 [MIDDLE.md sec. 1; GLOBAL.md sec. 1; MIDDLE.md sec. 5]. La primera fortaleza es lane priority: lane phase WR 64.5%, lane lead +535 y gold diff @15 +207 [MIDDLE.md sec. 5; MIDDLE.md sec. 4]. A diferencia de Top, acá sí ganás oro+exp temprano. El mecanismo causal es que tus kills y presión se convierten en ventaja de lane, no solo en peleas aisladas.

La segunda fortaleza es daño. DPM 1001 vs baseline 857, +16.9%, y 25.4% del daño del equipo [MIDDLE.md sec. 4; MIDDLE.md sec. 6]. Mid tiene el DPM absoluto más alto de todos tus roles, 1023 en el resumen del rol frente a ADC 974 [GLOBAL.md sec. 3]. Esto sugiere que, si llegás a mid game con recursos, sí podés cargar teamfights desde mid. La tercera fortaleza es amenaza individual: solo kills 2.97 por partida, max CS lead +30.4 y max level lead +1.8 [MIDDLE.md sec. 6]. Ese conjunto habla de trading y ventanas de kill reales.

La primera debilidad es CS estructural. Aunque ganás lane por oro+exp, CS@10 está 55.88 vs baseline 75.80, -26.3%, y CS@15 88.75 vs 115.30, -23.0% [MIDDLE.md sec. 4]. El mecanismo causal es que ganás por kills o presión, pero perdés minions; contra mids más limpios, esa ventaja se evapora. La segunda debilidad es roam. Takedowns en otras lanes 0.34 por partida es bajo [MIDDLE.md sec. 6]. El Roam Conversion Rate muestra 0.0% WR con >=2 roams en 1 game vs 50.0% con 0 roams en 22 games, pero ese n=1 es sample chico y no concluyente [MIDDLE.md sec. 6.1]. Aun así, la dirección encaja: si tenés lane ganada pero roameás mal, cedés farm y no convertís sides.

La tercera debilidad es cierre. Late score 5.3/10 está bien, pero WR largas 48.4% vs target 50.0% y KDA largas 2.51 vs target 2.27 muestran que no se cae por KDA, sino por conversión de mapa [MIDDLE.md sec. 5]. Además, aces antes del 15' y Mejais full stack a tiempo son 0.00 en 32 games [MIDDLE.md sec. 6]. No estás snowballeando el mapa temprano aunque ganes lane.

### C) Acciones concretas para la próxima semana

1. Si jugás Mid, hacelo con Juampi Torryco#LAS de jungla cuando sea posible: 66.7% WR en 12 games con él vs 35.0% sin él, +31.67pp [MIDDLE.md sec. 6.1]. Es sample sólido por estar >=10.
2. Convertí lane ganada en plates/farm antes de roam: tenés lane WR 64.5% y lead +535, pero CS@10 -26.3% y roam impact 0.34 [MIDDLE.md sec. 5; MIDDLE.md sec. 4; MIDDLE.md sec. 6]. El primer objetivo no es moverte más; es moverte después de wave crash.
3. Reducí Mid pool a campeones con señal positiva aunque el sample sea chico: Yasuo 4 games, 75.0% WR; Irelia 3 games, 100.0% WR; TwistedFate 3 games, 66.7% WR [MIDDLE.md sec. 2]. Todos son sample chico, así que esto es direccional; no hay campeón Mid con >=5 games y >=55% WR [MIDDLE.md sec. 7].

### D) Fases del juego

La fase más fuerte es Mid game, 6.8/10, con KP 48.5% vs target 43.6, DPM 1001 vs target 857 y vision/min 1.07 vs target 0.75 [MIDDLE.md sec. 5]. Early también es fuerte con 6.0/10, especialmente lane WR 64.5% y lane lead +535 [MIDDLE.md sec. 5]. La fase más débil es Late con 5.3/10, arrastrada por WR largas 48.4% vs target 50.0% [MIDDLE.md sec. 5]. No es un late malo, pero no cierra la ventaja temprana.

### E) Champ pool ideal

No hay pool ideal con alta confianza porque el reporte indica que no hay campeones Mid con >=55% WR y muestra mínima de 5 [MIDDLE.md sec. 7]. Con caveat de sample chico, los mejores candidatos son Yasuo 4 games, 75.0% WR; Irelia 3 games, 100.0% WR; TwistedFate 3 games, 66.7% WR [MIDDLE.md sec. 2]. Vladimir tiene 3 games, 33.3% WR pero 1655 DPM y 37.1% dmg share, muestra de daño alto sin conversión, sample chico [MIDDLE.md sec. 2]. Evitaría Galio 2 games, 0.0% WR, Veigar 2 games, 0.0% WR, y Katarina 3 games, 33.3% WR; todos son sample chico, por lo que la recomendación es direccional [MIDDLE.md sec. 2].

### F) Conclusión Mid

Mid es el secundario más sano: 46.9% WR en 32 games no supera tu global, pero Early 6.0/10, Mid 6.8/10, DPM +16.9% y duo Jungla +31.67pp con Juampi lo hacen el mejor plan de flex/fill [MIDDLE.md sec. 1; MIDDLE.md sec. 4; MIDDLE.md sec. 5; MIDDLE.md sec. 6.1].

### Conexión con GLOBAL

Mid está -6.8pp WR contra global: 46.9% vs 53.7% [MIDDLE.md sec. 1; GLOBAL.md sec. 1]. KDA está -0.18, 2.28 vs 2.46, y CS/min está -0.56, 5.60 vs 6.15 [MIDDLE.md sec. 1; GLOBAL.md sec. 1]. Pero daño/min está +89 sobre global: 1023 vs 934, +9.5% relativo [MIDDLE.md sec. 1; GLOBAL.md sec. 1]. Además, Mid DPM vs baseline está +16.9%, mejor que ADC +2.0% [MIDDLE.md sec. 4; BOTTOM.md sec. 4]. La lectura cross-role: Mid no es tu rol natural por WR, pero sí es tu mejor laboratorio de carry off-role.

## Sección 6 — Support (UTILITY)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia | Lectura coach |
|---|---:|---|---|
| Vision/min + adv rival | 3 | Vision/min 2.27, diff vs sup rival +0.0; baseline 2.60, -13.4% [UTILITY.md sec. 6; UTILITY.md sec. 4] | Volumen aceptable, por debajo de Diamond baseline. |
| Cobertura control wards río/jungla | 4 | Cobertura 55.4%, n=22 [UTILITY.md sec. 6] | Buena presencia territorial. |
| Heal+shield + saves | 3 | Heals+shields 5373 y saves 0.36 [UTILITY.md sec. 6] | Enable medido, pero saves bajos. |
| CC + picks coordinados | 5 | CC 45.32, picks coordinados 14.24, CC+kill 9.04 [UTILITY.md sec. 6] | Perfil fuerte de engage/pick. |
| Vision Dominance Ratio | 3 | Ratio 1.04, target >1.3 [UTILITY.md sec. 6] | Apenas por encima del rival, no dominante. |
| Roam impact | 1 | 0.04 takedowns en otras lanes [UTILITY.md sec. 6] | Roam casi inexistente. |
| Quest support a tiempo | 4 | 0.76 rate, 19/25 [UTILITY.md sec. 6] | Buen cumplimiento de quest. |

### B) Fortalezas y debilidades SUP-específicas

El arquetipo medido es engage/pick más que enchanter puro. CC sobre enemigos 45.32, picks coordinados 14.24 y CC+kill con aliado 9.04 son los números más fuertes del rol [UTILITY.md sec. 6]. El pool también apunta a engage/pick: Rakan 4 games, Alistar 3, Pyke 3, Thresh 2, Leona 1, Pantheon 1 [UTILITY.md sec. 2]. La primera fortaleza es esa capacidad de iniciar y conectar CC. El mecanismo causal es que si generás 14.24 picks coordinados, tu equipo recibe ventanas de kill sin depender solo de daño bruto [UTILITY.md sec. 6].

La segunda fortaleza es control territorial razonable. Control wards 4.04 por partida, stealth wards 23.88 y wards enemigas eliminadas 7.20 [UTILITY.md sec. 6]. La cobertura de wards en río/jungla enemiga es 55.4% en 22 partidas [UTILITY.md sec. 6]. Eso es una base útil para dragones y picks, aunque Vision Dominance Ratio 1.04 queda lejos del target >1.3 [UTILITY.md sec. 6]. La tercera fortaleza es quest: support item a tiempo 0.76, 19 de 25 [UTILITY.md sec. 6]. Completar quest abre más wards; sin esa base, el rol no funciona.

La primera debilidad es que la visión no domina al rival. Vision/min 2.25 vs baseline 2.60, -13.4%, y Vision Dominance Ratio 1.04 vs target >1.3 [UTILITY.md sec. 4; UTILITY.md sec. 6]. Aunque el volumen bruto 73.2 vision avg supera global 36.6 por la naturaleza del rol, contra el estándar de Support Diamond estás abajo [UTILITY.md sec. 1; GLOBAL.md sec. 1; UTILITY.md sec. 4]. El mecanismo causal es que en Support no alcanza con wardear mucho; necesitás negar y mover la línea de visión antes de objetivos.

La segunda debilidad es roaming. Roam impact 0.04 takedowns en otras lanes, con nota de que engage/pick sups deberían estar >2 y enchanters 0-1 [UTILITY.md sec. 6]. Si tu arquetipo es engage/pick, 0.04 significa que casi todo tu impacto queda encerrado en bot. La tercera debilidad es survivability y conversión: Support tiene 44.0% WR, KDA 2.12 y deaths promedio 8.2 [UTILITY.md sec. 1]. En derrotas, deaths suben a 9.43 y assists bajan a 11.14; en victorias, deaths 6.55 y assists 17.55 [UTILITY.md sec. 8]. El mecanismo es que cuando morís de más, tus wards desaparecen del mapa y tus engages no se transforman en segunda oleada de visión.

### C) Acciones concretas para la próxima semana

1. Antes de cada dragón, reseteá para control ward y sweep: tenés 4.04 control wards por partida y 55.4% cobertura río/jungla, pero Vision Dominance Ratio 1.04 vs target >1.3 [UTILITY.md sec. 6]. El objetivo no es poner más por poner; es subir dominio frente al support rival.
2. Si jugás engage, roameá solo después de crash bot y con timer de jungla/mid: roam impact 0.04 es demasiado bajo para CC 45.32 y picks 14.24 [UTILITY.md sec. 6]. Tenés herramientas para crear picks, pero no las estás llevando a otras lanes.
3. Priorizá Alistar/Rakan como test, no Pyke/Thresh en ranked: Alistar tiene 3 games, 100.0% WR y KDA 4.75, Rakan 4 games, 50.0% WR y KDA 2.35, Pyke 3 games, 33.3% WR y Thresh 2 games, 0.0% WR [UTILITY.md sec. 2]. Todos son sample chico, así que la recomendación es direccional y debe re-medirse.

### D) Fases del juego

La fase más fuerte es Mid game con 5.2/10, sostenida por damage/min 527 vs target 409, score 7.2 [UTILITY.md sec. 5]. Early y Late empatan como más débiles con 4.3/10 [UTILITY.md sec. 5]. Early cae por lane WR 40.0%, lane lead -251 y CS@10 11.68 vs target 14.40 [UTILITY.md sec. 5]. Late cae por WR largas 36.8% vs target 50.0%, aunque KDA largas 2.87 vs target 2.65 es aceptable [UTILITY.md sec. 5].

### E) Duo y matchups

Mejor duo humano en Support es DRX BeryL#LASS con 6 games, 50.0% WR; sample moderado y solo +6.0pp sobre tu Support 44.0% [UTILITY.md sec. 12; UTILITY.md sec. 1]. Juampi Torryco#LAS tiene 13 games, 46.2% WR; MAXI SALAS 7#LAS2 tiene 14 games, 42.9%; zPikA#UwU 18 games, 38.9%; Manuchito#LAS 10 games, 30.0% [UTILITY.md sec. 12]. El reporte no tiene aliados frecuentes con muestra suficiente para Support [UTILITY.md sec. 10]. Tampoco hay matchups vs campeones con muestra suficiente, mínimo 3 enfrentamientos [UTILITY.md sec. 9]. Por lo tanto, mejor ADC duo y mejores/peores matchups son `insuficiente data`.

### F) Champ pool ideal por arquetipo

Por arquetipo, el pool medido favorece engage/pick. Con caveat de sample chico, los tres picks a testear son Alistar, Rakan y Leona: Alistar 3 games, 100.0% WR, KDA 4.75; Rakan 4 games, 50.0% WR, KDA 2.35; Leona 1 game, 100.0% WR, KDA 6.00 [UTILITY.md sec. 2]. Leona es n=1, sample chico y no concluyente [UTILITY.md sec. 2]. Si el objetivo es enchanter, Janna tiene 1 game, 100.0% WR y Karma 1 game, 100.0% WR, pero ambos son sample chico e insuficientes para recomendación fuerte [UTILITY.md sec. 2]. Evitaría Thresh y Swain en ranked hasta más práctica: Thresh 2 games, 0.0% WR; Swain 2 games, 0.0% WR, ambos sample chico [UTILITY.md sec. 2].

### G) Conclusión Support

Support tiene herramientas de engage reales, con CC 45.32 y picks 14.24, pero 44.0% WR, Vision/min -13.4%, roam impact 0.04 y WR largas 36.8% lo dejan como rol de flex, no ranked principal [UTILITY.md sec. 1; UTILITY.md sec. 4; UTILITY.md sec. 5; UTILITY.md sec. 6].

### Conexión con GLOBAL

Support está -9.7pp WR bajo global: 44.0% vs 53.7% [UTILITY.md sec. 1; GLOBAL.md sec. 1]. KDA está 2.12 vs 2.46, delta -0.34, y deaths suben a 8.2 vs 6.7, +1.4 [UTILITY.md sec. 1; GLOBAL.md sec. 1]. Daño/min baja a 562 vs 934, delta -372, normal por rol pero relevante para carry agency [UTILITY.md sec. 1; GLOBAL.md sec. 1]. Vision avg sube a 73.2 vs 36.6, +36.7, pero vision/min del rol está 2.25 vs baseline 2.60, -13.4% [UTILITY.md sec. 1; GLOBAL.md sec. 1; UTILITY.md sec. 4]. La lectura cross-role: Support aumenta visión bruta, pero baja WR y KDA; no compensa frente a ADC.

## Sección 7 — Ranking final + Plan de acción

### 7.1 Ranking de roles (mejor → peor fit estratégico)

| # | Rol | Games | WR | E / M / L | Justificación | Datos clave |
|---:|---|---:|---:|---:|---|---|
| 1 | ADC | 430 | 58.1% | 5.1 / 6.7 / 7.2 | Tu rol natural: volumen masivo, WR alto y late sólido. | KDA 2.60 [BOTTOM.md sec. 1], Positioning 1.30 [BOTTOM.md sec. 6], Late 7.2 [BOTTOM.md sec. 5] |
| 2 | Mid | 32 | 46.9% | 6.0 / 6.8 / 5.3 | Mejor secundario: gana lane y hace daño, aunque no cierra igual que ADC. | Lane WR 64.5% [MIDDLE.md sec. 5], DPM +16.9% [MIDDLE.md sec. 4], Juampi +31.67pp [MIDDLE.md sec. 6.1] |
| 3 | Support | 25 | 44.0% | 4.3 / 5.2 / 4.3 | Flex situacional: engage útil, pero sin dominio de visión ni roam. | CC 45.32 [UTILITY.md sec. 6], Vision/min -13.4% [UTILITY.md sec. 4], Roam 0.04 [UTILITY.md sec. 6] |
| 4 | Jungla | 71 | 40.8% | 4.7 / 5.9 / 4.1 | Daño aceptable, pero pathing, invade y soul rate cuestan partidas. | CS@10 -26.7% [JUNGLE.md sec. 4], Counter ratio 0.08 [JUNGLE.md sec. 6], Soul 8% [JUNGLE.md sec. 6.1] |
| 5 | Top | 44 | 40.9% | 3.4 / 5.4 / 4.9 | Peor fit práctico: lane cae demasiado antes de que tus fortalezas aparezcan. | Gold@15 -714 [TOP.md sec. 4], Lane WR 36.4% [TOP.md sec. 5], Ambessa 20.0% WR [TOP.md sec. 8] |

Top y Jungla tienen WR casi idéntico, 40.9% vs 40.8%, diferencia 0.1pp [GLOBAL.md sec. 3]. El ranking pone Jungla arriba de Top solo porque Jungla tiene Mid 5.9/10 y DPM +14.2% vs baseline, mientras Top tiene Early 3.4/10 y gold diff @15 -714 [JUNGLE.md sec. 4; JUNGLE.md sec. 5; TOP.md sec. 4; TOP.md sec. 5].

### 7.2 Top 5 acciones accionables cross-role

| # | Acción | Por qué (evidencia con número) | Roles afectados | Esfuerzo |
|---:|---|---|---|---|
| 1 | Queueá ADC como rol primario y evitá off-role en ranked. | ADC 58.1% WR en 430 games vs off-role combinado 73 wins en 172 games; oportunidad +26.9 wins si el bloque off-role igualara ADC [BOTTOM.md sec. 1; JUNGLE.md sec. 1; TOP.md sec. 1; MIDDLE.md sec. 1; UTILITY.md sec. 1] | Todos | Bajo |
| 2 | Subí CS@10 con objetivo mínimo semanal por rol. | CS@10 bajo en ADC -18.8%, Jungla -26.7%, Top -29.9%, Mid -26.3%, Support -18.9% [GLOBAL.md sec. 4] | ADC, Mid, Top, Jungla | Alto |
| 3 | Jugá ADC con Manuchito#LAS cuando puedas. | ADC con Manuchito 67.1% WR en 73 games vs ADC total 58.1%, +9.0pp [BOTTOM.md sec. 12; BOTTOM.md sec. 1] | ADC | Bajo |
| 4 | Si jugás Mid, hacelo con Juampi y no roamees sin wave crash. | Con Juampi 66.7% WR en 12 games vs 35.0% sin él; roam >=2 tiene 0.0% WR en n=1, sample chico [MIDDLE.md sec. 6.1] | Mid | Medio |
| 5 | Eliminá picks de bajo WR con sample útil: LeeSin, Ambessa Top y Lucian ADC. | LeeSin 20.0% WR en 10 JG games, Ambessa Top 20.0% en 10 games, Lucian ADC 0.0% en 5 games [JUNGLE.md sec. 8; TOP.md sec. 8; BOTTOM.md sec. 8] | ADC, Top, Jungla | Bajo |

### 7.3 Cierre del coach jefe

Tu rol primario para ranked debe ser ADC: 58.1% WR en 430 games y +4.5pp sobre el global 53.7% proyectan la mejor ganancia de WR/LP disponible [BOTTOM.md sec. 1; GLOBAL.md sec. 1]. El secundario sano es Mid en flex/fill, especialmente con Juampi, porque tiene Early 6.0/10, Mid 6.8/10 y 66.7% WR con él en 12 games [MIDDLE.md sec. 5; MIDDLE.md sec. 6.1]. No toques Top ni Jungla en ranked por ahora: Top 40.9% en 44 games y Jungla 40.8% en 71 games están demasiado lejos de ADC [TOP.md sec. 1; JUNGLE.md sec. 1; BOTTOM.md sec. 1]. La palanca humana #1 es Manuchito en ADC: 67.1% WR juntos en 73 games vs 58.1% ADC total [BOTTOM.md sec. 12; BOTTOM.md sec. 1]. Compromiso de la semana: subir CS@10 ADC de 61.0 hacia 68+ y re-medir las próximas 20 partidas [BOTTOM.md sec. 4].
# COACH 360° — Análisis cross-role para Nadie#LASS

_Generado por panel de coaches senior (uno por rol + coach jefe cross-role).
Basado en `GLOBAL.md`, `BOTTOM.md`, `JUNGLE.md`, `TOP.md`, `MIDDLE.md`,
`UTILITY.md` (carpeta `reports/Nadie-LASS/`)._

_Reglas: cada número incluye archivo y sección de origen. No se inventan
datos: cuando una métrica tiene `n=0` o sample <5 se declara explícitamente._

---

## Sección 1 — Overview Cross-Role (basado en GLOBAL.md)

### 1.1 Identificación del rol natural

El jugador acumula **602 partidas analizadas** con **53.7% WR global** y
**KDA 2.46 (8.3/6.7/8.2)** [GLOBAL.md sec. 1 — Resumen]. El rendimiento
no es uniforme: hay un rol claramente dominante y cuatro roles secundarios
con WR bajo el 47%.

| Rol | Games | WR | KDA | CS/m | DPM | Vision | Sample |
|---|---:|---:|---:|---:|---:|---:|---|
| **ADC (BOTTOM)** | 430 | **58.1%** | **2.60** | **6.69** | 974 | 35.1 | sólido |
| Jungla | 71 | 40.8% | 2.41 | 5.31 | 880 | 36.3 | sólido |
| Top | 44 | 40.9% | 1.73 | 5.54 | 783 | 30.9 | sólido |
| Mid | 32 | 46.9% | 2.28 | 5.60 | **1023** | 35.9 | sólido |
| Support | 25 | 44.0% | 2.12 | 1.25 | 562 | 73.2 | sólido (≥10) |

_Fuente: GLOBAL.md sec. 3 — Distribución por rol._

- **Mejor WR (mín. 10 partidas):** **ADC con 58.1% en 430 partidas**
  [GLOBAL.md sec. 3]. La distancia al segundo mejor (Mid 46.9%) es de
  **+11.2 pp**, lo cual con 430 vs 32 partidas es estadísticamente
  contundente.
- **Peor WR (sample válido):** **Jungla 40.8% en 71 partidas** y **Top
  40.9% en 44 partidas** [GLOBAL.md sec. 3]. Ambos comparten KDA bajo
  (2.41 y 1.73 respectivamente). Diferencia entre Jungla y Top de
  apenas 0.1pp con n=71 vs n=44 → **no estadísticamente significativa**;
  pero ambos están **~13pp debajo del global y ~17pp debajo de ADC**.
- **Mejor KDA:** ADC 2.60 [GLOBAL.md sec. 3], coincide con el mejor WR.
  Coherente con un perfil de jugador de carry sostenido.
- **Mejor DPM relativo a baseline:** Support con **+28.9%** (527 vs 409)
  [UTILITY.md sec. 4 Playstyle], seguido por **Mid +16.9%** (1001 vs 857)
  [MIDDLE.md sec. 4] y **Jungla +14.2%** (838 vs 734) [JUNGLE.md sec. 4].
  Caveat: el DPM elevado en Support se explica porque varios juegos los
  hace con sup carries (Brand, Swain, Pantheon — ver UTILITY.md sec. 2),
  no con enchanters; no es un indicador puro de "eficiencia" del rol.

**Conclusión 1.1:** el rol natural es **ADC**, sin ambigüedad. Es el
único rol con WR positivo respecto al global (+4.4 pp) y representa el
71.4% de la muestra [BOTTOM.md sec. 1].

### 1.2 Inversión de tiempo vs WR — ¿hay misalignment?

**No hay misalignment estructural**: la mayor inversión de tiempo
(71.4% en ADC) coincide con el mejor WR (58.1%). El jugador está
correctamente identificado en su rol natural [BOTTOM.md sec. 1].

| Rol | % de partidas | WR | Δ WR vs ADC |
|---|---:|---:|---:|
| ADC | 71.4% | 58.1% | — |
| Jungla | 11.8% | 40.8% | -17.3 pp |
| Top | 7.3% | 40.9% | -17.2 pp |
| Mid | 5.3% | 46.9% | -11.2 pp |
| Support | 4.2% | 44.0% | -14.1 pp |

_Fuente: %s calculados desde sample sizes de GLOBAL.md sec. 3 / sec. 1._

Sin embargo, hay una **tasa de oportunidad perdida medible** dentro de las
**172 partidas no-ADC**. El WR agregado fuera de ADC es
(29+18+15+11)/172 = **42.4%**, contra los 58.1% de ADC. Si esas 172
partidas se hubieran jugado en ADC con el WR observado, las victorias
esperadas habrían sido **172 × 0.581 ≈ 100**, contra las **73 reales**:
**~27 victorias perdidas**. Asumiendo ~17 LP por win en Diamond/Emerald,
eso son **~459 LP** dejados en la mesa, equivalente a aproximadamente
**3-4 divisiones**. Mensaje práctico: **autofill o secondary debería ser
lo único que saque al jugador del bot**.

### 1.3 Sinergias humanas globales (sec. 12 GLOBAL.md = sec. 11 GLOBAL)

Top 7 duos globales [GLOBAL.md sec. 11 — Sinergias con personas]:

| Aliado | Games | WR | Δ WR vs global (53.7%) | Sample |
|---|---:|---:|---:|---|
| ZondaMC#LAS | 51 | 56.9% | +3.2 pp | sólido |
| **Manuchito#LAS** | 135 | **56.3%** | **+2.6 pp** | sólido |
| MAXI SALAS 7#LAS2 | 198 | 53.5% | -0.2 pp | sólido |
| Juampi Torryco#LAS | 148 | 52.0% | -1.7 pp | sólido |
| zPikA#UwU | 159 | 50.3% | -3.4 pp | sólido |
| DRX BeryL#LASS | 64 | 50.0% | -3.7 pp | sólido |
| PifiKing10#LAS1 | 13 | 46.2% | -7.5 pp | sólido (≥10) |

- **Mejor sinergia rentable (a sample sólido):** **Manuchito#LAS — 135
  games, 56.3% WR vs 53.7% baseline → +2.6 pp**. Aunque ZondaMC tiene
  +3.2 pp, lo hace en menos de la mitad de partidas (51 vs 135), lo que
  hace de **Manuchito la palanca más rentable y estable** del set.
  **Crítico**: filtrando solo a ADC, **Manuchito sube a 67.1% WR en
  73 partidas** [BOTTOM.md sec. 12], el mejor duo absoluto cuando se
  juega el rol natural.
- **Peor sinergia con sample útil (≥10 games):** **PifiKing10#LAS1 —
  13 games, 46.2% WR → -7.5 pp**. En sample chico, pero suficiente
  para reducir frecuencia. Caveat: los top campeones que aparecen
  con él son sups enchanters (Braum, Lulu, Milio); el problema podría
  ser composiciones donde el jugador hace ADC sin agresividad.
- **Patrones de roles aliados:** los mejores duos del jugador
  (Manuchito, ZondaMC, MAXI SALAS) llevan **top/jungla bruisers/duelists**
  (Mordekaiser, Kayle, Vayne, Poppy, Jax, LeeSin, Jayce — cf. GLOBAL.md
  sec. 11). El perfil ideal del aliado es **un top/jungla con presión
  sólida**, lo cual encaja con un ADC que necesita farm protegido. En
  cambio, los duos con **mids no-snowballers** (Heimerdinger, Ziggs en
  GLOBAL.md sec. 9 — top 5 peores aliados) generan WR ≤14%.

### 1.4 Patrones cruzados de fortalezas y debilidades

Comparando archivo por archivo, hay **un patrón sistémico** de
debilidades y otro de fortalezas. La estructura es la siguiente:

#### CS@10 — debilidad mecánica transversal

| Rol | CS@10 real | Baseline | Δ |
|---|---:|---:|---:|
| ADC | 61.0 | 75.1 | -18.8% [BOTTOM.md sec. 4] |
| Jungla | 49.9 | 68.0 | -26.7% [JUNGLE.md sec. 4] |
| Top | 49.2 | 70.3 | -29.9% [TOP.md sec. 4] |
| Mid | 55.9 | 75.8 | -26.3% [MIDDLE.md sec. 4] |
| Support | 11.7 | 14.4 | -18.9% [UTILITY.md sec. 4] |

**Todos** los roles muestran CS@10 entre **-18.8% y -29.9%** del baseline
del propio rol. Esto **no es problema de rol específico**: es **un déficit
mecánico de farming en laning phase** que se traslada con el jugador.
La diferencia se acentúa fuera de ADC (donde es 18.8%) hacia Top y
Jungla (29.9% y 26.7%) — lo que sugiere que cuanto más confortable es el
rol, mejor compensa, pero el problema base persiste.

#### Won laning rate — debilidad transversal aún más severa

| Rol | Won laning rate | Target |
|---|---:|---:|
| ADC | 10.0% [BOTTOM.md sec. 5] | 50.0% |
| Jungla | 4.3% [JUNGLE.md sec. 5] | 50.0% |
| Top | 9.5% [TOP.md sec. 5] | 50.0% |
| Mid | 12.9% [MIDDLE.md sec. 5] | 50.0% |
| Support | 12.0% [UTILITY.md sec. 5] | 50.0% |

**Cero rol** supera el 13% de "won laning". Score 1.0/10 en los cinco.
Causa raíz probable: el jugador **gana KDA en mid/late** (todas las
fases mid score ≥5.2 [varios sec. 5]), pero **no convierte la fase 0-15'
en oro+exp positivo**. Esto explica la paradoja "buen KDA, mal WR fuera
de ADC": en ADC el carry late compensa; en Top/Jungla no hay carry
late de rol y el déficit de laning se convierte en derrota.

#### Vision — fortaleza transversal (con una excepción)

| Rol | Vision/min real | Baseline | Δ |
|---|---:|---:|---:|
| ADC | 1.11 | 0.68 | **+62.8%** [BOTTOM.md sec. 4] |
| Jungla | 1.11 | 0.96 | +15.9% [JUNGLE.md sec. 4] |
| Top | 0.97 | 0.80 | +21.3% [TOP.md sec. 4] |
| Mid | 1.06 | 0.75 | +40.7% [MIDDLE.md sec. 4] |
| **Support** | **2.25** | **2.60** | **-13.4%** [UTILITY.md sec. 4] |

**Paradoja crítica**: el jugador **sobreperforma vision en cada rol que
no es support**, pero **subperforma cuando le toca ser support**. Cuando
no se le exige vision, la entrega; cuando se la exigen, baja un 13.4%
contra baseline. Causa probable: en Support el ward route es
*proactivo* (deep wards, drake control), no *reactivo* (un ADC con
1.11 vpm en bushes laterales es elite; un sup que solo wardea bot lane
está bajo). El bajo Vision Dominance Ratio de **1.04 (target >1.3)**
en UTILITY.md sec. 6 confirma el diagnóstico.

#### Deaths antes del 25' — debilidad ADC

ADC reporta 4.54 muertes antes del 25' [BOTTOM.md sec. 6], muy por
encima del target <3 declarado en las notas del propio archivo. En los
otros roles esta métrica específica no aparece, pero los Δ Deaths
victorias-vs-derrotas confirman patrón: **2.5+ deaths más en derrotas
en cada rol** (ADC -2.52, Jungla -4.19, Top -2.24 — secciones 8 de
cada archivo). El jugador muere demasiado, especialmente en partidas
que pierde.

### 1.5 Recomendación estratégica de priorización

**Priorizá ADC al 90%+ de tu pool en solo/duo**. Es el único rol con WR
positivo y la inversión actual del 71.4% deja **~27 LP-victorias en la
mesa** sobre las 172 partidas no-ADC. **Abandoná Top como queue regular**
(40.9% WR sobre 44 games, KDA 1.73, déficit de oro@15 de -714 vs rival
[TOP.md sec. 4] — el rol más antitético a tu perfil). El **rol secundario
sano para flex queue es Mid** (46.9% WR, DPM 1023 que es +16.9% sobre
baseline [MIDDLE.md sec. 4]); solo 6.8 pp debajo del global, sample
moderado-sólido (n=32) y palanca clara: **Juampi Torryco#LAS como
jungla en Mid +31.7 pp WR** [MIDDLE.md sec. 6.1]. La **palanca humana
más rentable** es **duear con Manuchito#LAS jugando ADC**: 73 games,
**67.1% WR** [BOTTOM.md sec. 12] vs 58.1% WR ADC sin duo — un
**+9 pp** que vale la pena buscar activamente cualquier noche.

---

## Sección 2 — ADC (BOTTOM) — basado en BOTTOM.md (430 partidas, sample sólido)

**Coach senior de ADC.** Las 4 dimensiones críticas son sustained DPS,
positioning, scaling, y lane priority + plates. Este es el rol natural
del jugador y el reporte más exhaustivo, así que las conclusiones
son las más confiables.

### A) Score 1-5 por stat core

| Stat | Valor | Referencia / Target | Score | Fuente |
|---|---:|---|---:|---|
| DPM | 939 | baseline 921 (+2.0%) | **3** | BOTTOM.md sec. 4 / sec. 6 |
| % daño del equipo | 24.5% | target ~25-30% | **3** | BOTTOM.md sec. 6 |
| Positioning Index | **1.30** | target Diamond 1.0-1.4 | **4** | BOTTOM.md sec. 6 |
| Torres antes de plates | 0.10 | bajísimo (presión bot pobre) | **2** | BOTTOM.md sec. 6 |
| First turret rápida (rate) | 0.00 (2/430) | virtualmente nulo | **1** | BOTTOM.md sec. 6 |
| Items legendarios completados / partida | 0.12 | extremadamente bajo (avg coach esperaría 2.5+) | **1** | BOTTOM.md sec. 6 |
| Scaling Score (KDA largas / cortas) | **0.60** | target ≥1.0 (scaling carry) | **2** | BOTTOM.md sec. 6.1 |
| Ventaja oro+exp end of laning | 10.0% | target >50% | **1** | BOTTOM.md sec. 6 |
| Muertes antes del 25' | **4.54** | target <3 | **2** | BOTTOM.md sec. 6 |
| Synergy WR con Support (zPikA) | 61.6% (n=73) vs 57.4% sin él | +4.2 pp | **3** | BOTTOM.md sec. 6.1 |

**Notas críticas:** el campo "Items legendarios completados (por
partida)" tiene avg 0.12 [BOTTOM.md sec. 6] — esto es un **artefacto del
challenge de Riot** (cuenta partidas que terminan con 6 ítems
legendarios completos a tiempo, no ítems generales). No interpretar como
"el jugador no compra ítems"; interpretar como "el ritmo de oro no
permite completar el build full ítem". Esto **es consistente con
Won-laning rate 10.0% y CS@10 -18.8%** [BOTTOM.md sec. 4].

### B) 3 fortalezas y 3 debilidades ADC-específicas

**Fortalezas**

1. **Positioning correcto en mid/late.** Positioning Index 1.30
   [BOTTOM.md sec. 6] está adentro del rango target (1.0-1.4) — el
   jugador **reparte más daño del que recibe** en peleas. Lo confirma
   el Δ damage recibido entre wins y losses: -4177 menos daño recibido
   en victorias [BOTTOM.md sec. 8]. **No** es un ADC que pelea de
   adelante; es un ADC posicional disciplinado, lo cual es la regla #1
   del rol.

2. **Champion pool deep + estable.** Kaisa 99g 62.6%, Aphelios 72g
   59.7%, Jinx 59g 59.3%, Yunara 33g 60.6%, Samira 19g 73.7%, MissFortune
   14g 57.1%, Varus 12g 58.3% — **siete picks con ≥55% WR y ≥10 games**
   [BOTTOM.md sec. 7]. El jugador **no depende de un campeón**, lo cual
   reduce el riesgo de bans en draft.

3. **Late-game KDA elite.** En partidas largas (≥30'), KDA 3.08 sobre
   256 games con 54.3% WR [BOTTOM.md sec. 6.1]. Score de Late-game
   7.2/10 [BOTTOM.md sec. 5]. Cuando el juego dura, el jugador es el
   carry esperado.

**Debilidades**

1. **Won-laning rate catastrófico (10.0%).** Solo 1 de cada 10 partidas
   termina laning con ventaja oro+exp [BOTTOM.md sec. 5 / sec. 6]; el
   target es 50%. CS@10 61.0 vs baseline 75.1 (-18.8%) y CS@15 95.7 vs
   114.9 (-16.7%) [BOTTOM.md sec. 4]. **Causa mecánica:** waves no
   freezadas o trades que no convierten. Aunque el WR final es 58.1%,
   este flowdown impide que el ADC llegue a su power spike (IE+PD)
   antes que el enemigo, y la única razón por la que sigue ganando es
   que **el equipo tipo se cura solo en mid-game**.

2. **Scaling Score invertido (0.60).** KDA en partidas largas
   (3.08, n=256) es **inferior** al de partidas cortas (5.15, n=63)
   [BOTTOM.md sec. 6.1]. Para un pool dominado por Kaisa, Aphelios,
   Jinx, Vayne, Yunara — todos **scaling carries** — el ratio
   esperaba ser ≥1.0. El 0.60 sugiere **dos problemas combinados**:
   (a) reaperturas tardías (deaths antes 25' = 4.54), y (b) build
   sub-óptimo para el champ (Aphelios y Jinx escalan duro, deberían
   tener mejor KDA largas). El "reset por morir" en mid-game está
   evaporando ventajas.

3. **Muertes antes del 25' (4.54) por encima del target <3.**
   [BOTTOM.md sec. 6]. Esto cuenta los suicidios antes del power
   spike. La cuenta es **51% más alta** que el target. Se conecta con
   el Positioning 1.30 (no es bajo, pero **está justo en el techo
   del rango target sano**, lo que indica que cuando el ADC pelea
   con margen, lo hace bien; cuando muere, es por overcommit de un
   teammate, no por mal positioning del propio).

### C) 3 acciones concretas para la próxima semana

1. **No banear, no rechazar Manuchito como duo en ADC.** WR con él
   en ADC = **67.1% en 73 games** [BOTTOM.md sec. 12], el mejor del
   reporte. Es **+9 pp** vs WR ADC global. Si está online, dueá.

2. **Eliminar Lucian del rotation.** 5 games, **0.0% WR, KDA 1.95**
   [BOTTOM.md sec. 8]. Sample chico (caveat: 5 games no es estadística,
   pero **un 0/5 con KDA <2 es signal direccional fuerte**). Reemplazar
   por Vayne o Nilah (ambos 9g, 66.7% WR, KDA 2.14 / 3.17 [BOTTOM.md
   sec. 7]) cuando el draft pida hyper-carry.

3. **Comprar Stopwatch / componente defensivo antes del 2do ítem
   ofensivo cuando enfrentés Jhin o MissFortune.** Tu peor matchup
   con sample: Jinx vs MissFortune 16.7% WR (n=6), Kaisa vs Jhin 25%
   WR (n=4), Jinx vs Jhin 33.3% WR (n=6) [BOTTOM.md sec. 9]. Patrón:
   **ADCs lane-bullies con poke + ult global te sacan del laning antes
   del power spike** y eso aplasta tu Won-laning rate. Stopwatch+Maw
   o priorizar Bloodthirster antes de PD reduce ese gap.

### D) Fase del juego más fuerte / más débil

| Fase | Score | Métrica que más arrastra |
|---|---:|---|
| Late game (25'+) | **7.2 / 10** ← MEJOR | KDA largas 3.35 vs target 2.30 |
| Mid game (15-25') | 6.7 / 10 | DPM 939 vs 921 (apenas baseline) |
| Early game (0-15') | **3.9 / 10** ← PEOR | **Won laning rate 10.0% vs 50%** (score 1.0) |

[Fuentes: BOTTOM.md sec. 5]. El late es la fortaleza estructural;
el early es la barrera. La métrica killer en early es Won-laning
con score 1.0/10 — cualquier mejora ahí mueve la aguja.

### E) Champ pool ideal

**Mantener (top 3 ADCs que maximizan rendimiento, sample sólido):**

1. **Kaisa** — 99g, 62.6% WR, KDA 2.86, 23.8% dmg share [BOTTOM.md
   sec. 2]. El pick #1 sin discusión.
2. **Samira** — 19g, **73.7% WR**, KDA 3.03, 29.2% dmg share [BOTTOM.md
   sec. 2]. WR más alto del pool con sample sólido. Si está open, pickear.
3. **Aphelios** — 72g, 59.7% WR, DPM 1020 [BOTTOM.md sec. 2]. La
   alternativa scaling cuando Kaisa está baneada.

**Sacar (3 ADCs que perjudican):**

1. **Lucian** — 5g, 0% WR [BOTTOM.md sec. 8]. Reemplazar por Nilah
   o Tristana en match-ups que pidan early dueling.
2. **Ashe** — 25g, 48.0% WR, KDA 2.65 [BOTTOM.md sec. 2]. Sample
   sólido, performance debajo del resto del pool. No es "mala", es
   relativamente peor que tus 7 picks viables.
3. **Tristana** — 9g, 44.4% WR [BOTTOM.md sec. 2]. Caveat: sample
   chico-moderado. Direccional, no concluyente. Dejar en banco.

### F) Mejor sup duo + mejor / peor matchup vs duo enemigo

- **Mejor sup duo (humano):** **Manuchito#LAS** — 73 games, 67.1% WR
  [BOTTOM.md sec. 12]. _Caveat:_ Manuchito juega top en gran parte (sus
  campeones top: Ornn, Kayle, Mordekaiser), no es necesariamente el sup
  del bot — pero la sinergia humana en partidas ADC del jugador es la
  más rentable.
- **Mejor sup duo (champ pareja):** **Samira+Leona** 6 games 100% WR,
  **Aphelios+Anivia** 5g 100%, **Kaisa+Swain** 5g 100% [BOTTOM.md
  sec. 13]. Caveat: samples chicos pero todos exhiben el mismo
  patrón — **Samira/Aphelios/Kaisa con frontline engage o magic
  damage support** es la receta ganadora.
- **Mejor matchup vs ADC enemigo:** **Kaisa vs Caitlyn** — 7g 100% WR,
  KDA 3.81 [BOTTOM.md sec. 9]. Picker gana ante poker.
- **Peor matchup vs ADC enemigo:** **Varus vs Jhin** 0% (n=3, sample
  chico — direccional), **Jinx vs MissFortune** 16.7% en 6 games
  [BOTTOM.md sec. 9]. Patrón: cuando llevás scaler ADC contra
  early-pressure ADC sin sup engage, la lane se rompe.

### G) Conclusión general

**El jugador es un ADC posicional, scaling, con late-game elite
(KDA largas 3.35) pero un déficit mecánico crónico de laning phase
(Won-laning 10.0%, CS@10 -18.8%) que solo se compensa porque su pool
de campeones (Kaisa/Aphelios/Samira) y un duo Manuchito a 67% WR le
cubren el early; arreglar ese laning es el upside #1 del jugador.**

### Conexión con GLOBAL

| Métrica | ADC (BOTTOM.md) | Global (GLOBAL.md sec. 1) | Δ | Interpretación |
|---|---:|---:|---:|---|
| WR | 58.1% | 53.7% | **+4.4 pp** | ADC está sobre la media |
| KDA | 2.60 | 2.46 | +0.14 (+5.7%) | ADC está sobre la media |
| CS/min | 6.69 | 6.15 | +0.54 (+8.8%) | ADC está sobre la media |
| DPM | 974 | 934 | +40 (+4.3%) | ADC está sobre la media |
| Vision | 35.1 | 36.6 | -1.5 (-4.1%) | Levemente debajo (sup infla el global) |

[Fuentes: BOTTOM.md sec. 1 (Comparativa) + GLOBAL.md sec. 1].

**Lectura:** ADC está **+5.7% en KDA, +8.8% en CS/m, +4.4 pp en WR**
sobre la media cross-role del jugador. **Es claramente su rol natural
y debería ser el rol primario en solo/duo y flex.** La única métrica
debajo es vision, pero el global está inflado por las 25 partidas
de support con 73.2 vision avg [GLOBAL.md sec. 3].

---

## Sección 3 — Jungla (JUNGLE) — basado en JUNGLE.md (71 partidas, sample sólido)

**Coach senior de Jungla.** 4 dimensiones críticas: pathing efficiency,
counter-jungle, gank impact, objective control. Sample n=71 — sólido para
conclusiones agregadas.

### A) Score 1-5 por stat core

| Stat | Valor | Referencia / Target | Score | Fuente |
|---|---:|---|---:|---|
| Jungle CS antes del 10' | 54.01 (jungle CS) / 49.87 (CS total @10) | baseline rol 68.0 (-26.7%) | **2** | JUNGLE.md sec. 4 + sec. 6 |
| Counter-jungle ratio | **0.08** | balanceado 0.5-0.8; <0.3 = pasivo | **1** | JUNGLE.md sec. 6 |
| Takedowns en otras lanes (early) | **n=0 — no medido aún** | requiere timelines | **N/A** | JUNGLE.md sec. 6 |
| Drakes / partida | 1.70 | aceptable (3 drakes para soul → 1.7 ≈ medio camino) | **3** | JUNGLE.md sec. 6 |
| Heraldos / partida | 0.42 | bajo (target ≥0.6) | **2** | JUNGLE.md sec. 6 |
| Barones / partida | 0.32 | normal (1 baron por partida es alto) | **3** | JUNGLE.md sec. 6 |
| Cobertura wards en río/jungla enemiga | 61.0% | razonable (target 60-70%) | **3** | JUNGLE.md sec. 6 |
| Tempo Index (tiempo a level 6) | **477 s (≈7:57)** | LeeSin reference 7:30, Karthus 8:30 | **3** | JUNGLE.md sec. 6 |
| Soul Rate | **0.08 (5 / 62)** | target >0.30 | **1** | JUNGLE.md sec. 6.1 |
| Gank-to-Death ratio | **n=0 — no medido aún** | requiere timelines | **N/A** | JUNGLE.md sec. 6 |

### B) 3 fortalezas y 3 debilidades JUNGLE-específicas

**Fortalezas**

1. **Vision en jungla — tienes el mapa.** Cobertura wards en río/jungla
   enemiga 61.0% [JUNGLE.md sec. 6] está dentro del rango sano del rol.
   Vision/min 1.13 vs baseline 0.96 (+15.9%) [JUNGLE.md sec. 4]. Esto
   convierte tus invades en menos blind y reduce camp punishments, pero
   aún así no traduce en counter-jungle (problema de ejecución, no de
   info — ver debilidad #1).

2. **Damage output decente como jungla.** DPM 838 vs baseline 734
   (+14.2%) [JUNGLE.md sec. 4]; KP 54.6% vs 52.1% (+4.8%). Estás
   **presente** en las kills, no eres un AFK farmer. Mid-game score
   5.9/10 [JUNGLE.md sec. 5] con DMG/min 6.1 — decente.

3. **Takedowns tempranos competitivos.** 6.30 takedowns en los
   primeros 14' vs target 5.56 [JUNGLE.md sec. 5] — 13% sobre baseline.
   Cuando estás en una pelea early, sumás. El problema es que esto
   **no se traduce en won-laning rate** (4.3%, score 1.0/10), lo que
   sugiere que **estás farmeando peleas sueltas, no cerrando lanes**
   para tus laners.

**Debilidades**

1. **Counter-jungle inexistente (0.08).** [JUNGLE.md sec. 6]. CS de
   jungla enemiga 5.34 vs CS de propia jungla 65.49 → ratio 0.08.
   Cualquier valor <0.3 indica un jungla **puramente reactivo, nunca
   invader**. Combinado con tiempo a level 6 = 477s (≈7:57'), estás
   pateando tu propia jungla y llegando a level 6 estándar, pero **no
   robás camps al rival**. Esto explica por qué tu Lee Sin/Master Yi
   van mal: ambos son **invader-junglers** que **dependen de starvear
   al rival** para funcionar.

2. **Soul rate catastrófico (8%).** Solo 5 de 62 partidas largas
   terminan con soul tomada [JUNGLE.md sec. 6.1]. WR en partidas largas
   38.7% (score 3.3/10 [JUNGLE.md sec. 5]). El target Diamond es ≥30%
   de soul rate. Mecanismo: drakes/partida 1.70 está OK, **pero los
   3 primeros drakes no se están convirtiendo en el 4to** — significa
   que el jugador toma drakes pero **no controla soul point** (5° drake
   spawn ≈ 35'+, fase donde KDA largas 2.75 [JUNGLE.md sec. 5] no
   alcanza para cerrar).

3. **Pool tóxico para el perfil del jugador.** Lee Sin **10g 20% WR,
   KDA 2.10** y MasterYi **7g 28.6% WR, KDA 2.06** [JUNGLE.md sec. 8]
   son los dos picks más jugados después de las pruebas, **ambos
   perdiendo masivamente**. Lee Sin necesita early invades + cheese ganks
   antes del 8' para funcionar — exactamente lo que el counter-jungle
   ratio 0.08 indica que **no estás haciendo**. MasterYi necesita
   carrys protegidos en ADC y vision pre-baron, contradiciendo tu
   bajo soul rate. **El pool elegido no concuerda con tu estilo de
   farm-and-gank pasivo.**

### C) 3 acciones concretas para la próxima semana

1. **Sacar Lee Sin del rotation hasta que tu counter-jungle ratio
   suba a >0.3.** 10g 20% WR es signal sólido. **Reemplazar por
   Ambessa (5g 60% WR, KDA 2.66) o Shyvana (3g 66.7% WR, sample chico
   pero direccional)** [JUNGLE.md sec. 7 / sec. 2]. Ambessa especialmente
   funciona porque **no necesita counter-jungle para operar** — escala
   en farm propio.

2. **Comprar Sweeper desde el 8' antes de cada drake spawn.** Tu
   cobertura wards en río 61% es buena, pero el **soul rate 8%** dice
   que **el control wards en drake pit no está saliendo**. Forzar
   compra de pink antes del 4:30 + intervalo 5 min duplicaría tu
   soul control sin requerir cambios mecánicos.

3. **Buscar Manuchito#LAS o ZondaMC#LAS como duo cuando juegues
   jungla.** Sinergias humanas en JUNGLE.md sec. 12: DRX BeryL 18g
   50% (sample sólido) y ZondaMC 13g 46.2% (sólido) son los menos
   tóxicos. **Evitar Juampi Torryco como duo en jungla**: 37g 35.1%
   WR [JUNGLE.md sec. 12] (vs sus 67% en Mid [MIDDLE.md sec. 6.1]) —
   buen duo en mid, malo en jungla. Caveat: la asimetría sugiere
   que cuando él hace mid y vos jungla, no lograste pop-offs (Zilean
   no es un mid pop-off champ).

### D) Fase del juego más fuerte / más débil

| Fase | Score | Métrica que más arrastra |
|---|---:|---|
| Mid game (15-25') | **5.9 / 10** ← MEJOR | DMG/min 838 vs 734 (score 6.1) |
| Late game (25'+) | 4.1 / 10 | WR partidas largas 38.7% (score 3.3) |
| Early game (0-15') | **3.7 / 10** ← PEOR | **Won-laning rate 4.3%** (score 1.0) |

[Fuentes: JUNGLE.md sec. 5]. La métrica killer en early es el mismo
patrón que en ADC: el jugador no está cerrando lanes con presión de
jungla (won-laning del *equipo* es 4.3% — peor de los 5 roles).

### E) Champ pool ideal Jungla

**Mantener / probar más:**
1. **Ambessa** — 5g 60% WR, KDA 2.66 [JUNGLE.md sec. 7]. Caveat:
   sample chico-moderado, dirección positiva.
2. **Evelynn** — 6g 50%, KDA 2.49, DPM 944 [JUNGLE.md sec. 2].
   Pick que se adapta a tu pasividad pre-6 (invisible, no requiere
   counter-jungle).
3. **Shyvana** — 3g 66.7%, CS/m 6.35 (mejor del jungle pool)
   [JUNGLE.md sec. 2]. Sample chico, dirección direccional. Tu
   farm efficiency mejora con power-farmers.

**Evitar:**
1. **Lee Sin** — 10g 20% WR [JUNGLE.md sec. 8].
2. **MasterYi** — 7g 28.6% WR [JUNGLE.md sec. 8].
3. **Shaco** — 2g 0% (sample chico) [JUNGLE.md sec. 2]. Direccional;
   y conceptualmente inconsistente con tu Counter-jungle ratio 0.08
   — Shaco *vive* del counter-jungling.

### F) Conclusión general

**Sos un jungla farm-and-gank pasivo (Counter-jungle ratio 0.08, Soul
rate 8%) jugando un pool de invaders agresivos (Lee Sin 20%, MasterYi
28.6%) — el mismatch entre estilo y pool, sumado a CS@10 -26.7% y
won-laning 4.3%, te deja en 40.8% WR; switchear a Ambessa/Evelynn/Shyvana
y tomar baron/soul a tiempo con Sweeper en pit son las palancas inmediatas.**

### Conexión con GLOBAL

| Métrica | Jungla (JUNGLE.md) | Global | Δ | Interpretación |
|---|---:|---:|---:|---|
| WR | 40.8% | 53.7% | **-12.8 pp** | -23.8% bajo la media |
| KDA | 2.41 | 2.46 | -0.05 (-2.0%) | Levemente bajo |
| CS/min | 5.31 | 6.15 | -0.84 (-13.7%) | Bajo la media |
| DPM | 880 | 934 | -54 (-5.8%) | Levemente bajo |
| Vision | 36.3 | 36.6 | -0.3 (-0.8%) | En la media |

[Fuentes: JUNGLE.md sec. 1 (Comparativa) + GLOBAL.md sec. 1].

**Lectura:** Jungla está **-12.8 pp WR, -13.7% CS/m** debajo de tu
media cross-role. **Estás claramente peor en jungla que en otros roles.**
La preservación del KDA (-2%) y el vision (-0.8%) sugieren que **no es
que no entiendes el rol** — es que las dimensiones que define un
jungla winning (CS@10, counter-jungle, soul) no están siendo ejecutadas.
**Recomendación: limitar Jungla a autofills o flex. No es queue
primaria.**

---

## Sección 4 — Top (TOP) — basado en TOP.md (44 partidas, sample sólido)

**Coach senior de Top lane.** 3 dimensiones críticas: lane dominance,
splitpush + side-laning, tank value en teamfights. Sample n=44 — sólido.

### A) Score 1-5 por stat core

| Stat | Valor | Referencia / Target | Score | Fuente |
|---|---:|---|---:|---|
| Gold diff @15 vs rival | **-714** | target +0 | **1** | TOP.md sec. 4 |
| Solo kills / partida | 2.00 | promedio top | **3** | TOP.md sec. 6 |
| Solo kills rápidos / partida | 0.00 (0/44) | nulo | **1** | TOP.md sec. 6 |
| Plates tomadas / partida | 4.57 | aceptable (target 5+) | **3** | TOP.md sec. 6 |
| Daño a torres (avg) | 5813 | bajo para top splitpush (target 8000+) | **2** | TOP.md sec. 6 |
| Daño mitigado (avg) | 39590 | razonable para tank/bruiser top | **3** | TOP.md sec. 6 |
| Splitpush Index | **0.23** | splitpushers 0.4-0.6; teamfighters 0.15-0.25 | **3** | TOP.md sec. 6 |
| KDA partidas largas (late_kda) | 2.10 | target 1.81 (+16%) | **3** | TOP.md sec. 5 |
| Muertes antes del 10' | 1.36 | target <0.5 → muy alto | **1** | TOP.md sec. 6 |

### B) 3 fortalezas y 3 debilidades TOP-específicas

**Fortalezas**

1. **Daño mitigado decente para el tipo de pool.** 39590 avg
   [TOP.md sec. 6] indica que cuando llegás a teamfight, **absorbés
   daño**, no estás escondido. Combinado con late_kda 2.10 (vs target
   1.81) [TOP.md sec. 5], en partidas largas convertís el rol de tanque
   correctamente.

2. **Vision/min positiva en top (+21.3%).** 0.97 vs baseline 0.80
   [TOP.md sec. 4]. **Tu macro de vision se mantiene incluso fuera
   de tu rol natural** — sos un jugador con awareness de mapa
   transferible.

3. **Champion pool con un par de picks viables.** Jax 3g 100% WR
   (sample chico, direccional), Kayle 3g 66.7%, Gnar 5g 60% [TOP.md
   sec. 2 / sec. 7]. Cuando spame Gnar (sample sólido), ganás 60%.

**Debilidades**

1. **Gold diff @15 catastrófico (-714).** [TOP.md sec. 4]. Es **el
   peor número** del reporte completo del jugador — ningún otro rol
   muestra un diferencial tan negativo. Causa raíz: **Won-laning rate
   9.5%** (score 1.0) [TOP.md sec. 5]. Significa que en 15 minutos
   estás casi 1 ítem detrás del top rival. Para un rol que **gana
   por 1v1 y splitpush**, ir 1 ítem atrás es game-over por draft.

2. **Muertes antes del 10' (1.36).** [TOP.md sec. 6]. Target <0.5.
   Eso es **2.7x el target**. Combinado con KP 37.2% [TOP.md sec. 4],
   el patrón es claro: **te suicidás temprano intentando trades que
   no son favorables**, lo que arruina la lane y obliga al jungla a
   gankear top a costa de side priority.

3. **Pool dominante perdedor: Ambessa.** 10 games, **20% WR, KDA
   1.34** [TOP.md sec. 8]. Ambessa es un melee assassin top que
   **necesita ganar lane temprano** — tu Gold diff @15 -714 indica
   que no podés hacerlo. Es el **mismo problema de mismatch champ-vs-estilo
   que en jungla con Lee Sin**: el pool no encaja con la realidad
   mecánica del jugador.

### C) 3 acciones concretas para la próxima semana

1. **Bannear Ambessa hasta tener ≥10 games con Gnar/Jax.** El pool
   actual sostiene 20% WR en Ambessa con sample sólido (10g)
   [TOP.md sec. 8]. **Reemplazar con Gnar (5g 60%) o Jax (3g 100%,
   sample chico → direccional)** [TOP.md sec. 7 / sec. 2]. Gnar tiene
   la ventaja extra de **escalar bien** y reducir el riesgo de muerte
   temprana — cubre tu debilidad #2 (deaths <10').

2. **No regroupear post-drake si tu late_kda <2.5; forzá side-laning.**
   Tu Splitpush Index 0.23 [TOP.md sec. 6] está al límite del rango
   "teamfighter" (0.15-0.25). Si llevás Camille (3g 33.3%, 0.78 max
   splitpush en sample chico) o Jax (splitpushers naturales), **cambiá
   side cuando el equipo busque baron** — ya que tu mid-game score
   5.4/10 [TOP.md sec. 5] indica que en teamfight 5v5 no estás
   convirtiendo.

3. **Reducir Top a 1-2 partidas/semana en flex queue.** Sample
   sólido n=44, WR 40.9%, KDA 1.73 (-30% vs media cross-role).
   **Es el peor rol del jugador en KDA**. Hasta que el Won-laning
   rate suba, no es queue rentable.

### D) Fase del juego más fuerte / más débil

| Fase | Score | Métrica que más arrastra |
|---|---:|---|
| Mid game (15-25') | **5.4 / 10** ← MEJOR | DMG/min 737 vs 830 (score 4.2) — solo OK porque vision/min 0.99 sube el score |
| Late game (25'+) | 4.9 / 10 | WR partidas largas 40.5% (score 3.6) |
| Early game (0-15') | **3.0 / 10** ← PEOR | **CS@10 49.25 vs 70.30 (score 2.8) + Gold diff @15 -714 (score 3.4)** |

[Fuentes: TOP.md sec. 5]. El early game 3.0/10 es **el peor score
de fase de todo el reporte** (peor que ADC 3.9, Jungla 3.7, Mid 4.3,
Sup 3.5). El roll early del jugador en Top es desastroso.

### E) Mejor / peor matchup

**Sin matchups con muestra suficiente (mín. 3 enfrentamientos)** —
declarado explícitamente en TOP.md sec. 9. **Insuficientes datos**
para identificar matchup específicos. Recomendación substituta: usar
patrones de pool (ban Ambessa-counters, priorizar Gnar/Jax si están
abiertos) y **runas adaptativas** (Conqueror para sustain en lane
contra bruisers, Grasp si llevás Cho'gath/Maokai).

### F) Conclusión general

**Top lane es el peor rol del jugador (40.9% WR, KDA 1.73, Gold diff
@15 -714 — el peor del reporte): el problema raíz es que el pool de
melee skirmishers (Ambessa 20% sobre 10g) requiere ganar lane y el
jugador no la gana, mientras que sus picks viables (Gnar, Jax) están
sub-utilizados; recomendación es jugar Top solo en autofill, banear
Ambessa, y subir Gnar a main pick.**

### Conexión con GLOBAL

| Métrica | Top (TOP.md) | Global | Δ | Interpretación |
|---|---:|---:|---:|---|
| WR | 40.9% | 53.7% | **-12.7 pp** | -23.6% bajo la media |
| KDA | 1.73 | 2.46 | -0.73 (-29.7%) | Bajísimo |
| CS/min | 5.54 | 6.15 | -0.61 (-9.9%) | Bajo |
| DPM | 783 | 934 | -151 (-16.2%) | Bajo |
| Vision | 30.9 | 36.6 | -5.7 (-15.6%) | Bajo |

[Fuentes: TOP.md sec. 1 (Comparativa) + GLOBAL.md sec. 1].

**Lectura:** Top está **-29.7% en KDA** y **-12.7 pp WR** debajo de
tu media. **Estás dramáticamente peor en Top que en cualquier otro
rol** (incluso peor que jungla en KDA). **Es el rol con peor
performance estadística del reporte y debería ser limitado a autofills
forzados o evitado por completo.**

---

## Sección 5 — Mid (MIDDLE) — basado en MIDDLE.md (32 partidas, sample sólido)

**Coach senior de Mid lane.** 4 dimensiones críticas: lane priority,
roam impact, damage output, snowball capacity. Sample n=32 — sólido.

### A) Score 1-5 por stat core

| Stat | Valor | Referencia / Target | Score | Fuente |
|---|---:|---|---:|---|
| Ventaja oro+exp end of laning | 12.9% | target >50% | **1** | MIDDLE.md sec. 6 |
| Max CS lead vs rival (avg) | +30.4 | bueno (target +20-40) | **4** | MIDDLE.md sec. 6 |
| Max level lead vs rival (avg) | +1.8 | bueno (target +1.5+) | **4** | MIDDLE.md sec. 6 |
| Takedowns en otras lanes (roams) | 0.34 | bajo (target 1.5+ para roamers) | **2** | MIDDLE.md sec. 6 |
| % daño del equipo | 25.4% | target ~25-30% | **3** | MIDDLE.md sec. 6 |
| DPM | 1001 | baseline 857 (+16.9%) | **4** | MIDDLE.md sec. 4 / sec. 6 |
| Aces antes del 15' / partida | 0.00 (0/32) | snowball mid casi nulo | **1** | MIDDLE.md sec. 6 |
| Solo kills / partida | 2.97 | bueno (mid baseline ~2) | **4** | MIDDLE.md sec. 6 |
| Roam Conversion Rate | **WR roams ≥2: 0% (n=1) — sample chico** | declarar caveat | **N/A** | MIDDLE.md sec. 6.1 |
| Synergy WR con Jungla (Juampi) | **66.7% (n=12) vs 35.0% sin él (n=20)** | Δ +31.7 pp | **5** | MIDDLE.md sec. 6.1 |

### B) 3 fortalezas y 3 debilidades MID-específicas

**Fortalezas**

1. **Damage output elite (DPM 1001 vs 857 baseline = +16.9%).**
   [MIDDLE.md sec. 4]. Combined con % del daño del equipo 25.4%
   [MIDDLE.md sec. 6], el jugador **pega como debe** en Mid. **El
   problema no es output, es lane priority.**

2. **Solo kills 2.97/partida.** [MIDDLE.md sec. 6]. Por encima del
   baseline mid típico (~2). En 32 partidas, esto representa **95
   solo kills totales**. Mecánicamente sabés ejecutar el 1v1 cuando
   se da la oportunidad.

3. **Sinergia con Juampi#LAS como jungla = +31.7 pp WR.** Con él:
   66.7% en 12 games. Sin él: 35.0% en 20 games [MIDDLE.md sec. 6.1].
   **Es la palanca humana más extrema del reporte completo del jugador**.
   Esto sugiere que tu mid funciona cuando un jungla compatible te
   gankea. Sin esa sinergia, el rol colapsa.

**Debilidades**

1. **Won-laning rate 12.9%, CS@10 -26.3%.** [MIDDLE.md sec. 4].
   Mismo patrón que el resto: CS@10 55.88 vs 75.80, won-laning
   score 1.0/10 [MIDDLE.md sec. 5]. Aunque tu Gold diff @15 sale
   **+207** (positivo!) [MIDDLE.md sec. 4], el laning no se cierra
   con priority — es 1.0/10 en "ventaja oro+exp al final del laning".

2. **Roam impact pésimo (0.34 takedowns) + Roam Conversion Rate
   negativa.** Solo 0.34 takedowns en otras lanes/partida [MIDDLE.md
   sec. 6]. Y cuando roameas ≥2 veces, WR es 0% (n=1, sample chico
   pero direccional) vs 50% sin roams (n=22) [MIDDLE.md sec. 6.1].
   **Caveat fuerte:** n=1 en el grupo de "roams" no permite conclusión
   estadística, pero la dirección es clara — **no estás extrayendo
   valor de roams**. Probablemente roameás en momentos malos (waves
   pushadas hacia ti, perdiendo CS@15).

3. **Aces antes del 15' = 0 en 32 games.** [MIDDLE.md sec. 6]. Snowball
   capacity nulo. Esto se conecta con el champion pool: Yasuo (4g 75%)
   y Irelia (3g 100%) son **late-game scalers**, no early-snowballers
   tipo Talon o Zed. **Tu pool no busca el ace temprano.**

### C) 3 acciones concretas para la próxima semana

1. **Buscar Juampi#LAS como duo cuando juegues Mid.** Es la palanca
   más rentable: **+31.7 pp WR** [MIDDLE.md sec. 6.1]. Si está online,
   queueá juntos. Sin él, Mid baja al 35%.

2. **Rolar a Irelia + TwistedFate como mains.** Irelia 3g 100% WR,
   KDA 2.90 (sample chico, direccional) y TwistedFate 3g 66.7%, KDA
   3.19 [MIDDLE.md sec. 2]. Yasuo (4g 75%) también es viable. **Sacar
   Vladimir (3g 33.3%), Katarina (3g 33.3%) y Galio (2g 0%, sample
   chico) del rotation** — todos por debajo del 50%.

3. **No roamear antes del 8' a menos que tengás ventaja de wave clara.**
   Tu Gold diff @15 +207 es positivo → estás ganando lane. **Pero
   tu won-laning rate 12.9% indica que no convertís esa ventaja en
   priority de lane**. La explicación más probable: estás roameando
   cuando deberías push-recall o stack-plates. Mantené wave bajo torre,
   stackeá plates antes de roamear.

### D) Fase del juego más fuerte / más débil

| Fase | Score | Métrica que más arrastra |
|---|---:|---|
| Mid game (15-25') | **6.8 / 10** ← MEJOR | Vision/min 1.07 (score 8.2) + DMG/min 1001 (score 6.3) |
| Late game (25'+) | 5.3 / 10 | WR partidas largas 48.4% (score 4.8) |
| Early game (0-15') | **4.3 / 10** ← PEOR | **Won-laning rate 12.9% (score 1.0) + CS@10 55.88 vs 75.80 (score 3.0)** |

[Fuentes: MIDDLE.md sec. 5]. Mid-game es **la fase más fuerte del
jugador en cualquier rol** (6.8/10 supera al ADC 6.7/10). El problema
es que **el late no traduce: 48.4% WR partidas largas significa que
incluso ganando mid-game, perdés late** — falta de cierre.

### E) Champ pool ideal Mid

**Mantener / spamear:**
1. **Irelia** — 3g 100% WR, KDA 2.90, CS/m 7.78, DPM 1175 [MIDDLE.md
   sec. 2]. Sample chico. Direccional positiva.
2. **Yasuo** — 4g 75% WR, KDA 1.93, vision 44.0 [MIDDLE.md sec. 2].
   Sample chico-moderado.
3. **TwistedFate** — 3g 66.7% WR, KDA 3.19 [MIDDLE.md sec. 2]. **Y
   tiene roam global con ult — podría arreglar tu roam impact.**

**Evitar:**
1. **Galio** — 2g 0% WR (sample chico, direccional) [MIDDLE.md sec. 2].
2. **Vladimir** — 3g 33.3% WR (sample chico) [MIDDLE.md sec. 2].
3. **Veigar** — 2g 0% WR, DPM 1030 (alto pero perdiendo) [MIDDLE.md
   sec. 2].

### F) Conclusión general

**Sos un mid de damage output (+16.9% DPM) y solo kills (2.97/partida)
con un mid-game score 6.8/10 elite, pero el laning no convierte
(won-laning 12.9%, aces<15'=0) y los roams perjudican (-50 pp con
n chico) — la palanca clave es duear con Juampi (+31.7 pp WR) y
spamear Irelia/TF/Yasuo en lugar de Vladimir/Katarina.**

### Conexión con GLOBAL

| Métrica | Mid (MIDDLE.md) | Global | Δ | Interpretación |
|---|---:|---:|---:|---|
| WR | 46.9% | 53.7% | **-6.8 pp** | -12.7% bajo la media |
| KDA | 2.28 | 2.46 | -0.18 (-7.3%) | Bajo |
| CS/min | 5.60 | 6.15 | -0.55 (-8.9%) | Bajo |
| DPM | **1023** | 934 | **+89 (+9.5%)** | **Sobre la media** |
| Vision | 35.9 | 36.6 | -0.7 (-1.9%) | En la media |

[Fuentes: MIDDLE.md sec. 1 (Comparativa) + GLOBAL.md sec. 1].

**Lectura:** Mid está **-6.8 pp WR** debajo de la media pero **+9.5%
DPM sobre la media** — la única dimensión donde sobreperformás.
Es **el segundo rol más viable después de ADC** y cumple las
condiciones para **rol secundario sano en flex queue**: WR sólo
6.8 pp debajo del global con sample n=32 (sólido) y con palanca
clara (Juampi como jungla). No abandonarlo, mejorarlo.

---

## Sección 6 — Support (UTILITY) — basado en UTILITY.md (25 partidas, sample sólido)

**Coach senior de Support.** 4 dimensiones críticas: vision (más
responsable del mapa), engage/disengage, enable, roam impact. Sample
n=25 — sólido pero al límite (≥10).

### Identificación de arquetipo

Mirando el champion pool [UTILITY.md sec. 2]: **Rakan (4g), Pyke (3g),
Thresh (2g), Alistar (3g), Leona (1g), Pantheon (1g)** son **engage/pick
sups**; **Rakan, Janna, Karma, Senna, Morgana** son **enchanters/utility**.
La distribución es **mixta engage-pick** (60% del pool). Los stats
confirman:

- CC sobre enemigos / partida: **45.32** [UTILITY.md sec. 6] — alto
  para engage profile (target enchanter <30, engage >40).
- Picks coordinados / partida: **14.24** [UTILITY.md sec. 6] — alto
  (engage / pick).
- CC + kill con aliado: **9.04** — alto.
- Heals + shields efectivos: **5373** — relativamente bajo (enchanters
  típicamente 8000-15000).

**Arquetipo confirmado: ENGAGE / PICK**, no enchanter.

### A) Score 1-5 por stat core

| Stat | Valor | Referencia / Target | Score | Fuente |
|---|---:|---|---:|---|
| Vision/min | **2.27** | baseline 2.60 (-13.4%) | **2** | UTILITY.md sec. 4 / sec. 6 |
| Diff vision vs sup rival | +0.0 (rango -0.5 a +0.6) | en empate | **3** | UTILITY.md sec. 6 |
| Cobertura wards río/jungla enemiga | 55.4% | target 60-70% | **3** | UTILITY.md sec. 6 |
| Heals + shields efectivos | 5373 | bajo para enchanter (5+); medio para engage | **3** | UTILITY.md sec. 6 |
| Saves de aliados / partida | 0.36 | bajo (target 1+) | **2** | UTILITY.md sec. 6 |
| CC sobre enemigos | 45.32 | alto (engage profile) | **4** | UTILITY.md sec. 6 |
| Picks coordinados | 14.24 | alto | **4** | UTILITY.md sec. 6 |
| Vision Dominance Ratio | **1.04** | target Diamond+ >1.3 | **2** | UTILITY.md sec. 6 |
| Roam impact (TKD otras lanes) | **0.04 (1/25)** | engage/pick target >2 | **1** | UTILITY.md sec. 6 |
| Quest support a tiempo (rate) | **0.76** | target ~0.85 | **3** | UTILITY.md sec. 6 |

### B) 3 fortalezas y 3 debilidades SUP-específicas

**Fortalezas**

1. **CC + picks como engage sup.** CC 45.32 [UTILITY.md sec. 6] y
   picks coordinados 14.24 son consistentes con un perfil de
   engage/playmaker. Cuando llevás Alistar (3g 100% WR, KDA 4.75
   [UTILITY.md sec. 2]), traducís el CC en kills.

2. **DPM sobre baseline (+28.9%).** 527 vs 409 [UTILITY.md sec. 4].
   _Caveat:_ esto está inflado por el pool — Brand 1g, Pantheon 1g,
   Swain 2g (todos sup carries). No es una "fortaleza pura" del rol
   sup, es un sesgo del pool. Pero **sí indica que cuando llevás
   damage sup, pegás**.

3. **Quest support a tiempo 76%.** [UTILITY.md sec. 6]. Decente —
   significa que **conocés las mecánicas básicas del item de support**.
   No es elite (target 85%), pero está dentro de rango aceptable.

**Debilidades**

1. **Vision/min DEBAJO de baseline (-13.4%).** [UTILITY.md sec. 4].
   **Esta es la métrica más importante del rol y la única donde estás
   debajo del baseline en TODOS los roles**, como muestra el cross-cut
   de la Sección 1. Vision Dominance Ratio 1.04 vs target >1.3
   [UTILITY.md sec. 6] confirma. Causa probable: arquetipo engage
   prioriza re-engage sobre vision sweeping. Pero **es exactamente
   esa priorización la que te limita a un sup mediocre, no elite**.

2. **Roam impact NULO (0.04 takedowns/partida).** [UTILITY.md sec. 6].
   Para un sup engage/pick, target >2. Estás 50x debajo. Esto significa
   que **cuando bot farmea, te quedás con tu ADC en vez de presionar
   side lanes con el pick threat de Pyke/Pantheon/Leona**. **Es el
   stat más anti-arquetipo del jugador** — engage sin roam = engage sin
   tempo lateral.

3. **Pool de ADCs no encaja con tu engage estilo.** Solo 11W/14L
   (44.0% WR) en 25 games [UTILITY.md sec. 1] sugiere que el ADC
   asignado random no es compatible. Combinado con Saves 0.36
   [UTILITY.md sec. 6] (target 1+) → cuando tu ADC se sobreextiende,
   no podés salvarlo. Tu KDA 2.12 con K/D/A 3.4/8.2/14.0 [UTILITY.md
   sec. 1]: alto en assists pero **deaths 8.2/partida**, lo que
   significa **engages malos o engages bien hechos sin follow-up**.

### C) 3 acciones concretas para la próxima semana

1. **Subí Vision/min a >2.6 antes de cualquier otro cambio.** Comprá
   control ward antes de cada drake (4:30 + intervalo 5 min). Cobertura
   wards río 55.4% [UTILITY.md sec. 6] vs target 65%. **Esta es la
   palanca #1: el rol depende de vision y vos estás bajo baseline**.

2. **Spame Alistar como engage sup.** 3g 100% WR, KDA 4.75 [UTILITY.md
   sec. 2]. Sample chico, direccional. Alistar combina **engage + saves
   (W+R combo)** — atacaría tu debilidad #2 (Saves 0.36) y #3
   (engage profile). **Sacar Pyke** (3g 33.3% WR) — Pyke necesita
   roams (que vos no hacés, 0.04) para funcionar. **Sacar Thresh**
   (2g 0% WR, sample chico).

3. **Cuando lleves Naut/Leona/Alistar, queueá con Manuchito** o el
   ADC más compatible con engage early. Caveat: la sinergia humana
   en sup es débil (mejor: DRX BeryL 6g 50% [UTILITY.md sec. 12],
   sample chico). **Insuficientes datos para ranking de sup duos**;
   pero el patrón general (Manuchito 67.1% WR en ADC del jugador)
   sugiere que cuando vos sos sup y él hace top/jungla, el equipo
   tiene presión bilateral — útil para tu engage profile.

### D) Fase del juego más fuerte / más débil

| Fase | Score | Métrica que más arrastra |
|---|---:|---|
| Mid game (15-25') | **5.2 / 10** ← MEJOR | DMG/min 527 (score 7.2) + KP 50.9% (score 4.5) |
| Late game (25'+) | 4.3 / 10 | WR largas 36.8% (score 3.0) |
| Early game (0-15') | **3.5 / 10** ← PEOR | **Won-laning 12.0% (score 1.0) + CS@10 11.68 (score 3.6)** |

[Fuentes: UTILITY.md sec. 5]. La WR partidas largas 36.8% [UTILITY.md
sec. 5] es **el peor número del jugador en partidas largas en
cualquier rol** (ADC 56.4%, Mid 48.4%, Top 40.5%, Jungla 38.7%, Sup
36.8%). En late game, el sup engage **debe convertirse en peeler/iniciador
de teamfight**. El jugador no lo está logrando.

### E) Mejor ADC duo + mejor / peor matchup

- **Mejor ADC duo (humano):** **DRX BeryL#LASS** — 6g 50% WR
  [UTILITY.md sec. 12]. **Caveat: sample chico (n<10), no concluyente**.
  El "mejor" del set tiene apenas 50%. Mensaje: **ningún duo en sup
  es WR-positivo**. Esto sugiere que cuando jugás sup, no es un
  problema del partner sino del rol mismo.
- **Mejor matchup vs sup enemigo:** **Insuficiente data** — UTILITY.md
  sec. 9 declara "Sin matchups con muestra suficiente". No hay
  matchup-level data en sup.
- **Peor matchup vs sup enemigo:** **Insuficiente data** — misma fuente.

### F) Champ pool ideal por arquetipo

Arquetipo confirmado **engage/pick**. Recomendación:

**3 sups engage para spamear:**
1. **Alistar** — 3g 100% WR, KDA 4.75 [UTILITY.md sec. 2]. Sample chico
   pero direccional fuerte.
2. **Leona** — 1g 100% WR, KDA 6.00 [UTILITY.md sec. 2]. Sample muy
   chico, no concluyente — pero es el engage clásico que encaja con
   tus stats CC 45.32.
3. **Rakan** — 4g 50% WR (sample chico-moderado) [UTILITY.md sec. 2].
   Es engage + dis-engage, encaja con tu necesidad de Saves 0.36.

**3 sups a evitar:**
1. **Pyke** — 3g 33.3% WR, KDA 1.30 [UTILITY.md sec. 2]. Pyke
   necesita roam (0.04 actual), no encaja.
2. **Thresh** — 2g 0% WR (sample chico) [UTILITY.md sec. 2].
3. **Swain** — 2g 0% WR, KDA 1.47 [UTILITY.md sec. 2]. Swain sup
   carry, conflicto con tu ADC.

### G) Conclusión general

**Sos un sup engage/pick (CC 45.32, picks 14.24) que sub-performa la
dimensión núcleo del rol — vision (vpm 2.27 vs 2.60, dominance 1.04
vs 1.3+) y roam impact (0.04, target >2) — convirtiendo a Support en
tu rol con peor late-game WR (36.8%); el camino es Alistar como main,
control wards en drake pit, y limitar la queue.**

### Conexión con GLOBAL

| Métrica | Sup (UTILITY.md) | Global | Δ | Interpretación |
|---|---:|---:|---:|---|
| WR | 44.0% | 53.7% | **-9.7 pp** | -18.1% bajo la media |
| KDA | 2.12 | 2.46 | -0.34 (-13.8%) | Bajo |
| CS/min | 1.25 | 6.15 | — | (no comparable: rol diferente) |
| DPM | 562 | 934 | -372 (-39.8%) | (no comparable) |
| Vision | **73.2** | 36.6 | **+36.6 (+100%)** | El doble — rol específico |

[Fuentes: UTILITY.md sec. 1 (Comparativa) + GLOBAL.md sec. 1].

**Lectura:** Sup está **-9.7 pp WR, -13.8% KDA** debajo de la media,
**peor que Mid (-6.8 pp) pero mejor que Top/Jungla (-12.7/-12.8 pp)**.
La métrica vision +100% es esperable (es el rol cuyo job es vision).
Pero el dato crítico es que **el WR sup 44% es peor que el WR cross-role
53.7%, y el sample (n=25) es suficiente para considerar que el jugador
no es naturalmente sup.** Recomendación: **mantener como tercer rol
en flex queue solo cuando se requiera**, mejorar vision metrics, y
no priorizarlo por encima de Mid (46.9%) o ADC (58.1%).

---

## Cierre del análisis

**Síntesis ejecutiva en 5 puntos:**

1. **Rol primario claro: ADC** (430g, 58.1% WR, KDA 2.60, +5.7%
   sobre la media cross-role) [BOTTOM.md sec. 1].
2. **Rol secundario sano: Mid** (32g, 46.9% WR, DPM +9.5% sobre la
   media — el único otro rol con upside) [MIDDLE.md sec. 1].
3. **Rol a abandonar: Top** (44g, 40.9% WR, KDA -29.7% bajo la media,
   Gold diff @15 -714) [TOP.md sec. 4].
4. **Palanca humana clave: Manuchito#LAS jugando con vos en ADC**
   (73g, 67.1% WR — +9 pp sobre tu ADC base) [BOTTOM.md sec. 12].
   Para Mid, **Juampi#LAS** como jungla (12g, 66.7% WR, +31.7 pp)
   [MIDDLE.md sec. 6.1].
5. **Debilidad mecánica transversal: laning phase**. Won-laning rate
   <13% en TODOS los roles, CS@10 -19% a -30% en TODOS los roles
   [BOTTOM/JUNGLE/TOP/MIDDLE/UTILITY sec. 4]. **Trabajar la fase
   0-15' es el upside #1 del jugador a nivel sistémico**, más
   importante que cualquier cambio de pool de un rol específico.

_Generado el 2026-05-08 a partir de los reportes de
`reports/Nadie-LASS/`. Toda afirmación cita el archivo y sección
fuente. Métricas con `n=0` o sample <5 declaradas explícitamente
como "no medido aún" o "sample chico, direccional"._
