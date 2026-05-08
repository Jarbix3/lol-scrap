# COACH 360° — Analisis cross-role para DRX BeryL#LASS

Generado a partir de los reportes en `reports/DRX_BeryL-LASS/`. Regla de lectura: cada diagnostico que usa numeros cita archivo y seccion; cuando no hay muestra suficiente, se declara como caveat.

## Seccion 1 — Overview Cross-Role

### 1.1 Identificacion del rol natural

| Rol | Games | WR | KDA | CS/m | DPM | Vision |
|---|---:|---:|---:|---:|---:|---:|
| Mid | 187 | 56.1% | 2.67 | 4.97 | 852 | 16.4 |
| Jungla | 95 | 43.2% | 2.33 | 4.87 | 537 | 21.3 |
| Support | 40 | 50.0% | 3.08 | 1.09 | 403 | 59.0 |
| ADC | 34 | 52.9% | 2.88 | 5.76 | 750 | 15.2 |
| Top | 23 | 65.2% | 2.62 | 5.54 | 862 | 14.5 |

La lectura transversal marca a **Top** como el mejor fit competitivo: 65.2% WR en 23 games, muestra solida por estar por encima de 10 partidas, contra 56.1% WR en Mid con 187 games y 52.5% WR global en 379 games [GLOBAL.md sec. 3; GLOBAL.md sec. 1]. El rol con mejor WR valido es Top, y el peor WR valido es Jungla con 43.2% en 95 games, tambien muestra solida [GLOBAL.md sec. 3]. El mejor KDA es Support con 3.08 en 40 games, pero no coincide con el mejor WR porque Support tiene menor carga de kills, 3.5 kills promedio en el reporte filtrado, y mayor volumen de asistencias, 16.6, lo que infla KDA sin traducir automaticamente en cierre de partida: su WR queda en 50.0% [UTILITY.md sec. 1; GLOBAL.md sec. 3]. En DPM bruto el mejor rol tambien es Top con 862 DPM, apenas por encima de Mid con 852 DPM [GLOBAL.md sec. 3]. Relativo al baseline Diamond, el mejor DPM es Mid: 832 vs 857, delta -3.0%, marginalmente mejor que Top 802 vs 830, delta -3.5%; ADC cae a 716 vs 921, delta -22.3%, y Jungla a 508 vs 734, delta -30.9% [GLOBAL.md sec. 4].

El rol natural no sale de una sola stat. Top gana por conversion de partidas: 65.2% WR, 9.6/10 late game, 77.8% WR en partidas largas y KDA largo 3.45 vs target 1.81 [TOP.md sec. 1; TOP.md sec. 5]. Mid es el rol principal operativo: 187 games, 49.3% del pool, 56.1% WR y DPM 852, con sample mas estable que Top [MIDDLE.md sec. 1]. La conclusion senior es: **Top es el rol natural por winrate y late conversion; Mid es el rol primario mas probado por volumen; Jungla es el rol a limitar en ranked**.

### 1.2 Inversion de tiempo vs WR

El rol mas jugado no es el de mejor WR. Mid ocupa 187/379 partidas, 49.3% del pool, con 56.1% WR; Top ocupa 23/379, 6.1% del pool, con 65.2% WR [MIDDLE.md sec. 1; TOP.md sec. 1]. Ese gap de 9.1 puntos porcentuales indica misalignment estrategico: estas invirtiendo casi la mitad del volumen en un rol fuerte, pero no en el de mayor conversion. Si se usa una estimacion simple de LP con +20/-20 por partida, mover las 187 partidas de Mid al rendimiento observado de Top implicaria 17.0 victorias extra esperadas: 187 * (65.2% - 56.1%) = 17.0; cada win extra reemplaza una loss y vale aproximadamente 40 LP de swing, lo que da unos 680 LP teoricos en 187 games [MIDDLE.md sec. 1; TOP.md sec. 1]. Como Top tiene solo 23 games, la direccion es fuerte pero no conviene extrapolar sin caveat: muestra solida, no enorme.

La oportunidad perdida mas clara no es Mid, sino Jungla. Jungla tiene 95 games, 25.1% del pool, y 43.2% WR; contra Top el delta es 22.0pp y contra Mid es 12.9pp [JUNGLE.md sec. 1; TOP.md sec. 1; MIDDLE.md sec. 1]. En terminos mecanicos, esos 95 games jugados al rendimiento Top serian 20.9 victorias extra esperadas, unos 836 LP teoricos con el mismo supuesto +20/-20; jugados al rendimiento Mid serian 12.3 victorias extra, unos 490 LP [JUNGLE.md sec. 1; MIDDLE.md sec. 1]. El mecanismo causal es claro: Jungla abre con early 2.9/10, lane phase win rate 26.3%, lane lead promedio -1251 y gold diff @15 -663; eso te pone detras antes de que tu KDA largo 3.35 pueda importar [JUNGLE.md sec. 5].

### 1.3 Sinergias humanas globales

En personas, el top 5 global no tiene una sinergia explosiva por encima de tu baseline global de 52.5% WR. MAXI SALAS 7#LAS2 aparece con 123 games y 52.0% WR, casi neutro contra tu 52.5% global, delta -0.5pp [GLOBAL.md sec. 11; GLOBAL.md sec. 1]. Neshy Fox#LAS tiene 63 games y 50.8% WR, delta -1.7pp; Manuchito#LAS tiene 111 games y 49.5% WR, delta -3.0pp; zPikA#UwU tiene 126 games y 47.6% WR, delta -4.9pp; Juampi Torryco#LAS tiene 127 games y 45.7% WR, delta -6.8pp [GLOBAL.md sec. 11; GLOBAL.md sec. 1]. La palanca humana global mas rentable por WR puro dentro del top 5 es MAXI, pero no es una ventaja real: es el menos malo, no un multiplicador.

El peor duo con sample util es Juampi Torryco#LAS: 127 games, 45.7% WR, -6.8pp contra 52.5% global [GLOBAL.md sec. 11; GLOBAL.md sec. 1]. El segundo flag es zPikA#UwU: 126 games, 47.6% WR, -4.9pp [GLOBAL.md sec. 11]. La lectura por rol matiza esto: en Top, zPikA#UwU sube a 71.4% WR en 14 games y Juampi Torryco#LAS a 66.7% WR en 15 games [TOP.md sec. 12]. En ADC, Juampi como Support cae a 33.3% WR en 9 games y sin el subis a 60.0%, delta -26.67pp; sample moderado, pero el mensaje es muy fuerte para bot lane [BOTTOM.md sec. 6.1]. En Support, caballo juan#juan da 66.7% WR en 9 games, sample moderado, y Manuchito 55.6% en 9 games [UTILITY.md sec. 12]. Patron: los duos que mas te potencian parecen funcionar cuando vos jugas Top con aliados de engage/utility, mientras bot lane y jungle sufren con varias combinaciones.

### 1.4 Patrones cruzados de fortalezas y debilidades

El problema transversal mas repetido es el CS temprano. Mid tiene CS@10 49.05 vs baseline 75.80, -35.3%; Jungla 42.58 vs 68.00, -37.4%; ADC 53.44 vs 75.10, -28.8%; Top 52.17 vs 70.30, -25.8%; Support 13.03 vs 14.40, -9.5% [MIDDLE.md sec. 4; JUNGLE.md sec. 4; BOTTOM.md sec. 4; TOP.md sec. 4; UTILITY.md sec. 4]. Como aparece en cuatro roles de farm y aun Support queda por debajo, no es solo matchup: es habito de wave/camp sequencing. El mecanismo causal es que llegas a minuto 15 con menos recursos: Mid CS@15 -33.1%, Jungla -34.4%, ADC -25.8% y Top -25.3% vs baseline [GLOBAL.md sec. 7]. Esa desventaja obliga a compensar con kills, y se ve en tus takedowns tempranos: Global 5.53 vs target 4.65, score 6.4, pero aun con eso el early global queda 4.3/10 y lane lead promedio -539 [GLOBAL.md sec. 5].

El segundo patron cruzado es vision por debajo del baseline. Mid registra Vision/min 0.53 vs 0.75, -29.9%; Jungla 0.70 vs 0.96, -26.8%; Support 1.84 vs 2.60, -29.3%; ADC 0.48 vs 0.68, -30.0%; Top 0.47 vs 0.80, -40.7% [GLOBAL.md sec. 4]. Esto explica por que tus fases medias no capitalizan del todo el buen kill participation: Global mid game tiene KP 51.2% vs target 46.9, score 5.7, pero Vision/min 0.72 vs 0.99, score 2.9, y el score de mid game cae a 4.2/10 [GLOBAL.md sec. 5]. La causa no es "falta de ganas de wardear"; es que tus ventanas de presion se hacen con niebla insuficiente, entonces invades, roams y side pressure cuestan deaths o no abren objetivo.

La fortaleza transversal es el late. Global late game es 7.1/10, con 52.6% WR en partidas >=25' y KDA largo 3.63 vs target 2.41 [GLOBAL.md sec. 5]. Top dispara esa identidad con late 9.6/10, 77.8% WR largo y KDA 3.45 vs target 1.81 [TOP.md sec. 5]. ADC tambien escala: late 7.9/10, 55.2% WR largo, KDA 4.00 vs target 2.30, y scaling score KDA largas/cortas 1.46 [BOTTOM.md sec. 5; BOTTOM.md sec. 6.1]. Support late 7.5/10 con KDA largo 4.23 vs target 2.65 confirma que cuando la partida pasa de 25', tu toma de peleas mejora [UTILITY.md sec. 5]. El problema no es cerrar late; el problema es entrar al late sin regalar demasiado en primeros 15-25 minutos.

### 1.5 Recomendacion estrategica

Prioriza Top y Mid: Top tiene 65.2% WR en 23 games y late 9.6/10, mientras Mid tiene 56.1% WR en 187 games y DPM 852, ambos por encima del WR global 52.5% [TOP.md sec. 1; TOP.md sec. 5; MIDDLE.md sec. 1; GLOBAL.md sec. 1]. Limita Jungla en ranked: 43.2% WR en 95 games, early 2.9/10 y lane lead promedio -1251 generan una perdida esperada de 12.3 victorias vs jugar Mid en el mismo volumen, unos 490 LP teoricos con supuesto +20/-20 [JUNGLE.md sec. 1; JUNGLE.md sec. 5; MIDDLE.md sec. 1]. El secundario sano es ADC si queres flexear, porque tiene 52.9% WR en 34 games y late 7.9/10, aunque DPM -22.3% vs baseline exige jugarlo como rol de scaling, no de lane stomp [BOTTOM.md sec. 1; BOTTOM.md sec. 4; BOTTOM.md sec. 5]. La palanca humana mas rentable no es global sino contextual: para Top, zPikA#UwU tiene 71.4% WR en 14 games y Juampi/MAXI 66.7% en 15 games; para ADC, evita Juampi support porque el split marca 33.3% con el vs 60.0% sin el [TOP.md sec. 12; BOTTOM.md sec. 6.1].

## Seccion 2 — Mid (MIDDLE)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia | Lectura coach |
|---|---:|---|---|
| Lane phase win rate + lead @14 | 3 | 43.9% lane WR, lane lead -287, early 5.0/10 [MIDDLE.md sec. 5] | Lane jugable pero no dominante; ganas por kills tempranas, no por economia limpia. |
| Max CS lead + max level lead | 4 | Max CS lead +13.4, max level lead +1.5, n=187 [MIDDLE.md sec. 6] | Hay ventanas de ventaja real cuando la lane se abre. |
| Takedowns en otras lanes | 3 | 0.64 roams por partida, total 120, n=187 [MIDDLE.md sec. 6] | Volumen moderado, no spam-roamer. |
| Team damage + DPM | 4 | 22.8% dano equipo, DPM 831; DPM 832 vs baseline 857, -3.0% [MIDDLE.md sec. 6; MIDDLE.md sec. 4] | Output casi Diamond pese al deficit de CS. |
| Aces antes del 15' | 1 | 0.01 por partida, total 2, n=187 [MIDDLE.md sec. 6] | Snowball explosivo temprano casi no medido en aces. |
| Solo kills | 5 | 2.43 solo kills por partida, total 455, n=187 [MIDDLE.md sec. 6] | 1v1 y castigo mecanico muy fuertes. |
| Roam Conversion Rate | 4 | >=2 roams: 66.7% WR, n=30; 0 roams: 57.0%, n=107; +9.66pp [MIDDLE.md sec. 6.1] | Cuando roameas bastante, el roam convierte. |
| Synergy WR con Jungla | 2 | Con MAXI 52.7%, n=74; sin MAXI 58.4%, n=113; -5.70pp [MIDDLE.md sec. 6.1] | La dupla de jungla mas frecuente no mejora tu Mid. |

### B) Fortalezas y debilidades Mid-especificas

La primera fortaleza Mid es la capacidad de matar y crear presion individual. Tus 2.43 solo kills por partida en 187 games y max level lead +1.5 muestran que, aun sin farmear al nivel del baseline, sabes encontrar ventanas de all-in [MIDDLE.md sec. 6]. El mecanismo es importante: una solo kill no solo suma oro, tambien fuerza reset enemigo, libera wave y habilita roam o vision; por eso tus takedowns en primeros 14' son 5.97 vs target 4.09, score 8.5 [MIDDLE.md sec. 5]. Esa es la razon de que el early Mid llegue a 5.0/10 pese a CS@10 49.05 vs 75.80, score 2.4 [MIDDLE.md sec. 5].

La segunda fortaleza es el dano relativo. Tenes 22.8% del dano del equipo y DPM 831 en stats avanzadas, con DPM 832 vs baseline 857, solo -3.0% [MIDDLE.md sec. 6; MIDDLE.md sec. 4]. Para un Mid con CS@15 77.16 vs 115.30, -33.1%, estar apenas -3.0% en DPM significa que convertis oro en dano con eficiencia alta [MIDDLE.md sec. 4]. El problema no es que no pegues; el problema es que llegas al spike con menos economia que un Diamond promedio y aun asi tratas de jugar como carry.

La tercera fortaleza es que el roam, cuando existe, gana partidas. Con >=2 roams tenes 66.7% WR y KDA 6.40 en 30 games; con 0 roams tenes 57.0% WR y KDA 3.39 en 107 games [MIDDLE.md sec. 6.1]. Sample solido para ambos grupos. El +9.66pp sugiere que tus mejores partidas de Mid no son de AFK farm, sino de push-kill-roam o kill-roam; el mecanismo es que tus solo kills y takedowns tempranos crean prioridad, y esa prioridad suma kills laterales.

Debilidad uno: el CS es demasiado bajo para Mid. CS@10 49.05 vs baseline 75.80 (-35.3%) y CS@15 77.16 vs 115.30 (-33.1%) son deficits enormes [MIDDLE.md sec. 4]. Como tu gold diff @15 es apenas -30, las kills estan tapando el problema, pero eso es volatil: si no aparece la pelea, entras a mid game sin item tempo. Debilidad dos: vision. Vision/min 0.53 vs 0.75 (-29.9%) y mid game vision 0.54 vs target 0.75, score 2.9 [MIDDLE.md sec. 4; MIDDLE.md sec. 5]. El mecanismo es directo: roamear sin vision baja la calidad del roam, y aunque el split >=2 roams sea bueno, tus partidas sin roam quedan mas dependientes de outplay mecanico. Debilidad tres: synergy con jungla. Con MAXI como jungla tenes 52.7% WR en 74 games y sin el 58.4% en 113, delta -5.70pp [MIDDLE.md sec. 6.1]. No significa que MAXI sea el problema absoluto, pero si que la dupla Mid-Jungle no esta convirtiendo tus ventanas de solo kill en control de mapa.

### C) Acciones concretas para la proxima semana

1. En Mid, tu KPI de semana es subir CS@10 de 49.05 a 60 antes de tocar picks nuevos; el baseline Diamond es 75.80 y el deficit -35.3% explica por que dependes de kills para no quedar atras [MIDDLE.md sec. 4].
2. Jugando Sylas/Akali, roam solo despues de crash o kill: tus partidas con >=2 roams tienen 66.7% WR vs 57.0% con 0 roams, pero el CS@15 -33.1% dice que el roam mal timedo te cobra oleadas [MIDDLE.md sec. 6.1; MIDDLE.md sec. 4].
3. Antes de minuto 8, wardea un lado y juga hacia ese lado: Vision/min 0.53 vs 0.75 (-29.9%) y synergy jungla -5.70pp indican que la conexion Mid-Jungla necesita vision y pings, no mas peleas ciegas [MIDDLE.md sec. 4; MIDDLE.md sec. 6.1].

### D) Fase fuerte y fase debil

Tu fase fuerte como Mid es late: 7.4/10, con 53.2% WR en partidas >=25' y KDA 3.59 vs target 2.27 [MIDDLE.md sec. 5]. Tu fase mas debil es mid game: 4.6/10, arrastrada por Vision/min 0.54 vs 0.75, score 2.9, y DPM 831 vs 857, score 4.8 [MIDDLE.md sec. 5]. Early queda 5.0/10, pero es enganoso: el CS@10 score 2.4 se compensa con takedowns tempranos score 8.5 [MIDDLE.md sec. 5].

### E) Champ pool ideal

El pool ideal debe potenciar asesinato, roams selectivos y late estable. Manteneria **Malzahar**, **Sylas** y **Ahri**: Malzahar tiene 18 games, 72.2% WR, KDA 3.35 y CS/m 6.80; Sylas tiene 65 games, 56.9% WR y es tu pick de mayor volumen; Ahri tiene 8 games, 75.0% WR y KDA 4.10, sample moderado pero perfil de pick/roam sano [MIDDLE.md sec. 2; MIDDLE.md sec. 7]. Como picks a limitar, sacaria **Irelia** en Mid por 20.0% WR en 5 games y KDA 1.67, **Syndra** por 40.0% WR en 10 games aunque DPM 1016 sea alto, y campeones de control que exigen CS perfecto si no estas dispuesto a entrenar wave management [MIDDLE.md sec. 2; MIDDLE.md sec. 8]. Syndra no es "mala" por dano, pero con tu CS@15 -33.1% el pick pierde su promesa de spike limpio [MIDDLE.md sec. 4].

### F) Conclusion

Mid es un rol ganador para vos por mecanica, solo kills y roam conversion, pero para transformarlo de "fuerte" a "rol principal de climb" tenes que farmear 10-15 minion waves mas por partida y wardear antes de moverte.

### Conexion con GLOBAL

| Metrica | Mid | Global | Delta | Lectura |
|---|---:|---:|---:|---|
| WR | 56.1% | 52.5% | +3.6pp | Mid esta sobre tu media y con sample enorme [MIDDLE.md sec. 1; GLOBAL.md sec. 1]. |
| KDA | 2.67 | 2.65 | +0.02 | Rendimiento representativo del jugador, no inflado [MIDDLE.md sec. 1; GLOBAL.md sec. 1]. |
| CS/m | 4.97 | 4.63 | +7.3% | Mejor que tu media, aun muy bajo vs baseline [MIDDLE.md sec. 1; MIDDLE.md sec. 4]. |
| DPM | 852 | 718 | +18.7% | Mid es una fuente real de dano en tu pool [MIDDLE.md sec. 1; GLOBAL.md sec. 1]. |

## Seccion 3 — Jungla (JUNGLE)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia | Lectura coach |
|---|---:|---|---|
| Jungle CS antes del 10' | 2 | 47.14 jungle CS @10; CS@10 timeline 42.58 vs 68.00, -37.4% [JUNGLE.md sec. 6; JUNGLE.md sec. 4] | Clear muy por debajo del ritmo Diamond. |
| Counter-jungle ratio | 1 | Ratio 0.03; enemy jungle CS 1.79 vs propia 44.57 [JUNGLE.md sec. 6] | No estas invadiendo ni starveando. |
| Takedowns en otras lanes early | N/A | n=0, no medido aun [JUNGLE.md sec. 6] | Insuficiente data para gank impact por Riot challenge. |
| Objetivos por partida | 4 | 2.06 drakes, 0.38 heraldos, 0.39 barones, 0.20 robos [JUNGLE.md sec. 6] | Volumen de objetivos decente, pero no alcanza para soul. |
| Cobertura wards rio/jungla enemiga | 3 | 42.5%, n=44 [JUNGLE.md sec. 6] | Muestra solida parcial; mejor que tu vision general de jungla, pero incompleta. |
| Tempo a level 6 | 2 | 517s avg, n=95; referencia nota: Lee Sin Diamond ~450s, Karthus ~510s [JUNGLE.md sec. 6] | Llegas tarde al primer spike. |
| Soul Rate | 1 | Soul 14/73 largas, 19%; WR largas 43.8% [JUNGLE.md sec. 6.1] | Cedes demasiadas souls. |
| Gank-to-Death ratio | N/A | n=0, no medido aun [JUNGLE.md sec. 6] | Insuficiente data. |

### B) Fortalezas y debilidades Jungla-especificas

La primera fortaleza de Jungla es que, cuando el juego llega largo, tu KDA no colapsa: late game 5.3/10, KDA largo 3.35 vs target 2.78 en 73 partidas largas [JUNGLE.md sec. 5]. Esto indica que no sos inutil en peleas tardias; el problema viene antes. La segunda fortaleza es Sejuani: 19 games, 68.4% WR, KDA 3.87, DPM 592, vision 26.9 [JUNGLE.md sec. 2; JUNGLE.md sec. 7]. Ese pick encaja con un perfil de jungla que no domina clear/invade pero si puede aportar engage, CC y teamfight. La tercera fortaleza es el volumen bruto de drakes: 2.06 por partida, con 196 drakes en 95 games [JUNGLE.md sec. 6]. No es suficiente para soul, pero muestra que no ignoras objetivos; el problema es secuencia y control, no ausencia total de foco.

La debilidad principal es pathing. CS@10 42.58 vs baseline 68.00 (-37.4%), CS@15 68.40 vs 104.30 (-34.4%), gold diff @10 -378 y gold diff @15 -663 te dejan sin tempo [JUNGLE.md sec. 4]. El mecanismo causal en jungla es mas duro que en lane: si llegas tarde al level 6, el mapa ya eligio donde pelear. Tu tiempo a level 6 es 517s; la nota del reporte ubica Lee Sin Diamond cerca de 450s y Karthus cerca de 510s, asi que tu promedio se parece mas a un clear de scaler lento que a un jungla de impacto temprano [JUNGLE.md sec. 6]. Esa lentitud se ve en early 2.9/10, lane phase win rate 26.3% y lane lead promedio -1251 [JUNGLE.md sec. 5].

La segunda debilidad es counter-jungle casi inexistente. El ratio 0.03, con 1.79 CS de jungla enemiga vs 44.57 de propia jungla, te define como jungla pasivo de territorio [JUNGLE.md sec. 6]. Si ademas el DPM esta en 508 vs baseline 734 (-30.9%) y KP 50.6% vs 52.1% (-2.9%), no estas compensando la falta de invade con ganks de alto impacto [JUNGLE.md sec. 4]. Takedowns en otras lanes early tiene n=0, asi que no se puede cuantificar ese gank impact desde Riot challenges; con la data disponible, la lectura segura es que no hay evidencia de que los ganks compensen el farm perdido [JUNGLE.md sec. 6].

La tercera debilidad es objective conversion. Drakes por partida 2.06 suena bien, pero Soul Rate es 19%: 14 souls en 73 partidas largas, con WR largas 43.8% [JUNGLE.md sec. 6; JUNGLE.md sec. 6.1]. El mecanismo es que tomar primeros drakes sin vision sostenida y sin bot/mid tempo no garantiza soul. Vision/min 0.70 vs 0.96 (-26.8%) y cobertura en rio/jungla enemiga 42.5% en 44 partidas explican por que los objetivos no se convierten en condicion de victoria [JUNGLE.md sec. 4; JUNGLE.md sec. 6].

### C) Acciones concretas para la proxima semana

1. Juga solo Sejuani/Gragas en Jungla esta semana: Sejuani tiene 68.4% WR en 19 games y Gragas 52.0% en 25, mientras Kindred cae a 20.0% en 20 y Viego a 20.0% en 5 [JUNGLE.md sec. 2; JUNGLE.md sec. 8].
2. Antes de minuto 10, tu objetivo no es gankear mas sino limpiar mejor: jungle CS @10 47.14 y CS@10 timeline 42.58 vs baseline 68.00 (-37.4%) piden rutas full-clear mas disciplinadas [JUNGLE.md sec. 6; JUNGLE.md sec. 4].
3. Desde el primer drake, compra y coloca vision con plan de soul: Soul Rate 19% y Vision/min 0.70 vs 0.96 (-26.8%) dicen que tu problema no es iniciar objetivos, sino sostener control de los siguientes [JUNGLE.md sec. 6.1; JUNGLE.md sec. 4].

### D) Fase fuerte y fase debil

La fase mas fuerte de Jungla es late, pero solo por comparacion interna: 5.3/10, KDA largo 3.35 vs target 2.78 y WR largo 43.8% [JUNGLE.md sec. 5]. La peor fase es early: 2.9/10, con CS@10 score 2.2, lane phase win rate 26.3% y lane lead promedio -1251 [JUNGLE.md sec. 5]. Esa early phase baja todo el rol porque jungla necesita tempo para decidir primeros objetivos y tu gold diff @15 -663 te obliga a pelear desde atras [JUNGLE.md sec. 4].

### E) Champ pool ideal

El pool ideal es **Sejuani**, **Gragas** y un tercer tanque/utility de bajo riesgo como **Zac** solo despues de tener mas muestra; la evidencia firme es Sejuani 68.4% WR en 19 games y Gragas 52.0% en 25 [JUNGLE.md sec. 2]. Como el reporte muestra Zac 0.0% en 1 game, eso es sample insuficiente, no una sentencia [JUNGLE.md sec. 2]. Evitaria **Kindred**, **Viego** y **JarvanIV**: Kindred 20.0% WR en 20 games, Viego 20.0% en 5, JarvanIV 37.5% en 8, todos con muestras al menos moderadas y Kindred sample solido [JUNGLE.md sec. 2; JUNGLE.md sec. 8]. La razon no es solo WR: Kindred exige counter-jungle, tracking e invades, justo donde tu ratio es 0.03 [JUNGLE.md sec. 6].

### F) Conclusion

Jungla debe salir de tu ranked pool hasta que el clear @10, el level 6 y la soul conversion suban, porque hoy el rol te cobra demasiadas partidas antes del minuto 15.

### Conexion con GLOBAL

| Metrica | Jungla | Global | Delta | Lectura |
|---|---:|---:|---:|---|
| WR | 43.2% | 52.5% | -9.3pp | Rol claramente bajo tu media [JUNGLE.md sec. 1; GLOBAL.md sec. 1]. |
| KDA | 2.33 | 2.65 | -0.32 | Menos conversion y menos margen en peleas [JUNGLE.md sec. 1; GLOBAL.md sec. 1]. |
| CS/m | 4.87 | 4.63 | +5.2% | Mejor que global por naturaleza del rol, pero -37.4% vs baseline @10 [JUNGLE.md sec. 1; JUNGLE.md sec. 4]. |
| DPM | 537 | 718 | -25.2% | Caida fuerte de impacto ofensivo [JUNGLE.md sec. 1; GLOBAL.md sec. 1]. |

## Seccion 4 — Support (UTILITY)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia | Lectura coach |
|---|---:|---|---|
| Vision/min + diff vs rival | 3 | Vision/min 1.86, diff -0.1; baseline 1.84 vs 2.60, -29.3% [UTILITY.md sec. 6; UTILITY.md sec. 4] | Volumen aceptable en bruto, bajo para Diamond. |
| Cobertura wards rio/jungla enemiga | 3 | 46.9%, n=32 [UTILITY.md sec. 6] | Muestra solida, cobertura util pero no dominante. |
| Heal+shield + saves | 4 | 10141 heals/shields, 2.92 saves por partida [UTILITY.md sec. 6] | Buen perfil de enable. |
| CC + picks coordinados | 4 | 30.60 CC, 16.52 picks, 8.72 CC+kill con aliado [UTILITY.md sec. 6] | Engage/pick con conversion razonable. |
| Vision Dominance Ratio | 2 | 0.92 vs target >1.3 [UTILITY.md sec. 6] | No dominas la guerra de vision. |
| Roam impact | 1 | 0.12 takedowns en otras lanes, total 5, n=40 [UTILITY.md sec. 6] | Roam casi inexistente. |
| Quest support a tiempo | 3 | 0.60 rate, 24/40 [UTILITY.md sec. 6] | Aceptable, pero 40% no llega a tiempo. |

### B) Fortalezas y debilidades Support-especificas

Tu arquetipo real parece mixto entre enchanter y engage. El pool tiene Sona 9 games, Janna 9, Leona 7 y Pyke 5 [UTILITY.md sec. 2]. Los mejores resultados vienen de Leona: 71.4% WR, KDA 3.82, muestra moderada de 7 games [UTILITY.md sec. 2; UTILITY.md sec. 7]. Pero tus stats avanzadas no son de support puramente pasivo: 30.60 CC sobre enemigos, 16.52 picks coordinados y 8.72 CC+kill con aliado por partida indican que cuando elegis iniciar, generas contacto [UTILITY.md sec. 6].

Fortaleza uno: enable defensivo. Heals+shields efectivos 10141 y saves 2.92 por partida en 40 games sostienen peleas largas, lo que encaja con KDA largo 4.23 vs target 2.65 y late 7.5/10 [UTILITY.md sec. 6; UTILITY.md sec. 5]. El mecanismo es que tus partidas ganadas tienen 21.10 assists vs 12.00 en derrotas y vision 62.90 vs 55.20, lo cual muestra que cuando estas activo alrededor del equipo, multiplicas peleas [UTILITY.md sec. 8]. Fortaleza dos: CC/pick. Leona 71.4% y los 30.60 CC por partida dicen que engage simple y frontal te funciona mejor que picks de ejecucion fina como Pyke 40.0% en 5 games [UTILITY.md sec. 2; UTILITY.md sec. 6]. Fortaleza tres: KP. Support tiene KP 59.2% vs baseline 54.8%, +8.0%, y mid game KP 59.2 vs target 54.8, score 5.6 [UTILITY.md sec. 4; UTILITY.md sec. 5]. Eso significa que estas en las peleas correctas cuando se arman.

Debilidad uno: vision no domina. Vision/min 1.84 vs baseline 2.60 (-29.3%), Vision Dominance Ratio 0.92 contra target >1.3 y diff de vision vs support rival -0.1 muestran que tu rol mas responsable del mapa no esta ganando ese eje [UTILITY.md sec. 4; UTILITY.md sec. 6]. El mecanismo es obvio: sin ventaja de vision, tu engage llega tarde o se hace sobre informacion incompleta. Debilidad dos: roam impact. Roam impact 0.12 takedowns en otras lanes, total 5 en 40 games, es bajisimo; la nota del reporte dice engage/pick supports >2 y enchanters 0-1 [UTILITY.md sec. 6]. Como tu pool incluye Leona/Pyke, esa falta de roams impide convertir bot pressure en mid/jungle. Debilidad tres: quest timing. Quest support a tiempo 0.60 significa que 16 de 40 partidas no llegan a tiempo [UTILITY.md sec. 6]. Eso retrasa wards evolucionadas y agrava el Vision Dominance Ratio 0.92 [UTILITY.md sec. 6].

### C) Acciones concretas para la proxima semana

1. Si jugas Support, prioriza Leona sobre Pyke/Sona/Janna en ranked: Leona tiene 71.4% WR en 7 games, mientras Sona y Janna estan en 44.4% en 9 games cada una y Pyke 40.0% en 5 [UTILITY.md sec. 2].
2. Compra control ward antes de cada drake y usa recall de minuto 4:30 como regla: Vision/min 1.84 vs 2.60 (-29.3%) y VDR 0.92 vs target >1.3 son el cuello de botella del rol [UTILITY.md sec. 4; UTILITY.md sec. 6].
3. Con Leona/Pyke, programa un roam mid despues de crash o reset: Roam impact 0.12 en 40 games esta muy bajo para engage/pick support, y tus picks coordinados 16.52 indican que si llegas, podes convertir [UTILITY.md sec. 6].

### D) Fase fuerte y fase debil

La fase fuerte es late: 7.5/10, WR largo 53.1% y KDA largo 4.23 vs target 2.65 [UTILITY.md sec. 5]. La fase debil es mid game: 4.4/10, arrastrada por Vision/min 1.86 vs 2.60, score 2.9 [UTILITY.md sec. 5]. Early queda 4.7/10, con lane phase 45.0% y lane lead -180, lo cual es casi estable pero no dominante [UTILITY.md sec. 5].

### E) Mejor duo, matchups y lectura bot

Mejor duo humano Support: caballo juan#juan con 66.7% WR en 9 games, sample moderado; Manuchito 55.6% en 9 y Juampi 54.5% en 11 tambien son jugables [UTILITY.md sec. 12]. Mejor ADC aliado por campeon frecuente: Smolder tiene 60.0% WR en 5 games con tu KDA 3.61, sample moderado; Jhin cae a 33.3% en 6 [UTILITY.md sec. 10]. Matchups de support enemigo tienen muestra insuficiente: solo Pyke vs Lulu aparece con 3 games, 33.3% WR, y el mismo par figura como mejor y peor por falta de mas datos [UTILITY.md sec. 9]. Por lo tanto, no hay base para declarar ban especifico de support enemigo; si aparece Lulu contra tu Pyke, el caveat es sample chico pero desfavorable.

### F) Champ pool ideal por arquetipo

El arquetipo recomendado es engage-enchanter simple, no pick de alto riesgo. Tres picks a maximizar: **Leona** por 71.4% WR en 7 games, **Janna** si queres jugar peel pero no como blind principal por 44.4% WR en 9, y **Sona** solo en composiciones de scaling donde el plan sea llegar a late 7.5/10 [UTILITY.md sec. 2; UTILITY.md sec. 5]. Si el objetivo es climb inmediato, Leona debe ser el ancla y los enchanters quedan como secundarios. A evitar: **Pyke** por 40.0% WR en 5 games y por exigir roam impact que hoy esta en 0.12, **Rakan** por 0.0% en 2 games con sample chico no concluyente, y cualquier support de pick si no vas a corregir vision/roams [UTILITY.md sec. 2; UTILITY.md sec. 6].

### G) Conclusion

Support es jugable como rol secundario de flex si lo enfocas en Leona/peel y corriges vision, pero hoy no es mejor que Mid o Top porque el rol pide dominio de mapa y tu VDR esta en 0.92.

### Conexion con GLOBAL

| Metrica | Support | Global | Delta | Lectura |
|---|---:|---:|---:|---|
| WR | 50.0% | 52.5% | -2.5pp | Ligeramente bajo tu media [UTILITY.md sec. 1; GLOBAL.md sec. 1]. |
| KDA | 3.08 | 2.65 | +0.44 | KDA mas alto por asistencias, no por mejor cierre [UTILITY.md sec. 1; GLOBAL.md sec. 1]. |
| DPM | 403 | 718 | -43.9% | Esperable por rol, pero tambien -4.0% vs baseline support [UTILITY.md sec. 1; UTILITY.md sec. 4]. |
| Vision avg | 59.0 | 21.9 | +169.4% | Bruto alto por rol, aunque Vision/min -29.3% vs Diamond [UTILITY.md sec. 1; UTILITY.md sec. 4]. |

## Seccion 5 — ADC (BOTTOM)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia | Lectura coach |
|---|---:|---|---|
| DPM + % dano equipo | 3 | DPM 716, team damage 20.0%; DPM baseline 716 vs 921, -22.3% [BOTTOM.md sec. 6; BOTTOM.md sec. 4] | Dano aceptable para tu pool, bajo para Diamond ADC. |
| Positioning Index | 4 | 1.02, target Diamond 1.0-1.4, n=34 [BOTTOM.md sec. 6] | Peleas en rango correcto, no hiper pasivo. |
| Torres/first turret | 1 | 0.03 torres antes de plates, first turret rapida 0.00 [BOTTOM.md sec. 6] | Casi no convertis lane en plates/torre. |
| Items legendarios | 1 | 0.09 por partida, total 3, n=34 [BOTTOM.md sec. 6] | Spike de items muy bajo en medicion. |
| Scaling Score | 4 | KDA largas 4.22, n=18; cortas 2.90, n=5; ratio 1.46 [BOTTOM.md sec. 6.1] | Escalas mejor cuando la partida dura. |
| Lane phase WR + lead @14 | 3 | 50.0% lane WR, lane lead -582, early 4.5/10 [BOTTOM.md sec. 5] | Ganas mitad de lanes, pero con deficit de oro+exp. |
| Muertes antes del 25' | 2 | 4.26 por partida, target <3 [BOTTOM.md sec. 6] | Moris demasiado antes del spike. |
| Synergy WR con Support | 1 | Con Juampi 33.3%, n=9; sin el 60.0%, n=25; -26.67pp [BOTTOM.md sec. 6.1] | Dupla bot frecuente perjudicial. |

### B) Fortalezas y debilidades ADC-especificas

Fortaleza uno: posicionamiento medible. Positioning Index 1.02 esta dentro del target Diamond ~1.0-1.4 [BOTTOM.md sec. 6]. Eso significa que no estas jugando peleas como melee carry ni quedandote tan atras que no pegues; el ratio dano hecho/dano recibido es sano. Fortaleza dos: scaling. En partidas largas >=30' tenes 66.7% WR, KDA 4.22 y n=18, contra partidas cortas <25' con 40.0% WR, KDA 2.90 y n=5; el KDA ratio es 1.46 [BOTTOM.md sec. 6.1]. Sample solido para largas y moderado para cortas. El mecanismo es que cuando llegas a items y peleas ordenadas, tu KDA mejora, lo que tambien aparece en late 7.9/10, WR largo 55.2% y KDA largo 4.00 vs target 2.30 [BOTTOM.md sec. 5]. Fortaleza tres: Ashe. Ashe tiene 9 games, 77.8% WR y KDA 3.20, sample moderado, y es tu unico ADC con >=55% WR y minimo 5 games [BOTTOM.md sec. 2; BOTTOM.md sec. 7].

Debilidad uno: sustained DPS por debajo de baseline. DPM 716 vs baseline 921, -22.3%, y team damage 20.0% en stats avanzadas [BOTTOM.md sec. 4; BOTTOM.md sec. 6]. Para ADC, eso es problema central: aunque el Positioning Index sea sano, si el DPM queda 205 puntos por debajo del baseline, estas sobreviviendo sin convertir suficiente presion de DPS. Debilidad dos: lane-to-tower conversion. Torres destruidas antes de plates 0.03 y first turret rapida 0.00 en 34 games indican que casi nunca convertis bot prior en placa/torre [BOTTOM.md sec. 6]. Eso se conecta con lane lead promedio -582 aunque lane phase WR sea 50.0% [BOTTOM.md sec. 5]. Podes empatar o ganar por kills, pero no estas saliendo de lane con oro estructural. Debilidad tres: muertes tempranas y duo support. Muertes antes del 25' 4.26 contra target <3 cortan spikes, y con Juampi Torryco#LAS como Support tenes 33.3% WR en 9 games vs 60.0% sin el en 25, delta -26.67pp [BOTTOM.md sec. 6; BOTTOM.md sec. 6.1]. El mecanismo es claro: si moris antes de dos items y ademas la lane duo no sincroniza, el scaling que mejor te queda no llega con suficiente oro.

### C) Acciones concretas para la proxima semana

1. En ADC, juega Ashe como pick default y limita Kai'Sa/Varus: Ashe 77.8% WR en 9 games, Kai'Sa 33.3% en 6 y Varus 40.0% en 10 [BOTTOM.md sec. 2; BOTTOM.md sec. 7; BOTTOM.md sec. 8].
2. Tu regla de lane es "no morir antes de primer item": muertes antes del 25' 4.26 vs target <3 y items legendarios 0.09 por partida muestran que estas retrasando spike [BOTTOM.md sec. 6].
3. Evita duo bot con Juampi Support en ranked hasta corregir patrones: con el 33.3% WR en 9 games, sin el 60.0% en 25, delta -26.67pp [BOTTOM.md sec. 6.1].

### D) Fase fuerte y fase debil

La fase fuerte es late: 7.9/10, con 55.2% WR largo y KDA largo 4.00 vs target 2.30 [BOTTOM.md sec. 5]. La fase debil es mid game: 3.9/10, arrastrada por DPM 715 vs target 921, score 3.3, y Vision/min 0.49 vs 0.68, score 2.9 [BOTTOM.md sec. 5]. Early es 4.5/10, con lane phase win rate 50.0% pero lane lead -582, asi que el problema no es perder siempre la lane sino perder demasiada economia incluso en lanes parejas [BOTTOM.md sec. 5].

### E) Champ pool ideal

Tres ADCs que maximizan tu rendimiento segun datos: **Ashe** por 77.8% WR en 9 games, **Xayah** como opcion direccional por 100.0% WR en 3 games pero sample chico, y **Jhin** como opcion de utilidad/dano por 100.0% en 1 game y DPM 1164, sample insuficiente [BOTTOM.md sec. 2]. Como el reporte no da mas ADCs con muestra suficiente positiva, no conviene inventar un pool cerrado. Tres a sacar o limitar: **Kai'Sa** por 33.3% WR en 6 games, **Varus** por 40.0% WR en 10 games, y **Samira** por 0.0% en 1 game con sample insuficiente pero perfil de alto riesgo para tus muertes antes del 25' [BOTTOM.md sec. 2; BOTTOM.md sec. 8].

### F) Mejor sup duo y matchups

No hay "mejor support duo" fuerte en personas: Manuchito#LAS tiene 40.0% WR en 5 games, caballo juan#juan 37.5% en 8, Juampi 33.3% en 9, zPikA 33.3% en 9 y Neshy 20.0% en 5 [BOTTOM.md sec. 12]. Por campeon aliado, Darius aparece 66.7% WR en 6 games con tu KDA 4.21, pero eso no identifica support, sino aliado de equipo [BOTTOM.md sec. 10]. Matchups bot tienen muestra insuficiente: Varus vs Tristana aparece con 3 games, 66.7% WR, y figura tanto como mejor como peor por falta de otros matchups [BOTTOM.md sec. 9]. No hay datos suficientes para ban de duo enemigo; si ves Tristana, la evidencia no es negativa, pero el sample es chico.

### G) Conclusion

ADC es un secundario sano si lo jugas a scaling y con Ashe, pero no deberia superar a Mid/Top porque tu DPM esta -22.3% vs baseline y tus muertes antes del 25' frenan el spike.

### Conexion con GLOBAL

| Metrica | ADC | Global | Delta | Lectura |
|---|---:|---:|---:|---|
| WR | 52.9% | 52.5% | +0.4pp | Practicamente tu media [BOTTOM.md sec. 1; GLOBAL.md sec. 1]. |
| KDA | 2.88 | 2.65 | +0.24 | Mejor supervivencia/participacion que global [BOTTOM.md sec. 1; GLOBAL.md sec. 1]. |
| CS/m | 5.76 | 4.63 | +24.4% | Natural por rol, pero CS@10 sigue -28.8% vs baseline [BOTTOM.md sec. 1; BOTTOM.md sec. 4]. |
| DPM | 750 | 718 | +4.3% | Levemente sobre global, aun -22.3% vs ADC Diamond [BOTTOM.md sec. 1; BOTTOM.md sec. 4]. |

## Seccion 6 — Top (TOP)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia | Lectura coach |
|---|---:|---|---|
| Gold diff @15 | 3 | -93 vs rival [TOP.md sec. 4] | Casi neutro, no dominante. |
| Lane phase WR + lead @14 | 3 | 43.5% lane WR, lane lead -206, early 4.9/10 [TOP.md sec. 5] | Lane estable, no stomp. |
| Solo kills + quick solo kills | 4 | 2.26 solo kills, 0.00 quick solo kills, n=23 [TOP.md sec. 6] | Buen 1v1 extendido, poca ejecucion instantanea. |
| Plates + dano torres | 4 | 2.04 plates, 4709 dano a torres [TOP.md sec. 6] | Buena conversion estructural. |
| Dano mitigado | 5 | 31530 mitigado promedio [TOP.md sec. 6] | Alto valor de front/sustain. |
| Splitpush Index | 2 | 0.16, n=23; splitpushers 0.4-0.6, teamfighters 0.15-0.25 [TOP.md sec. 6] | Perfil teamfighter, no splitpusher. |
| KDA partidas largas | 5 | 3.45 vs target 1.81, late score 10.0 en KDA [TOP.md sec. 5] | Late sobresaliente. |

### B) Fortalezas y debilidades Top-especificas

Fortaleza uno: conversion a victoria. Top tiene 65.2% WR en 23 games, +12.7pp contra tu global 52.5% [TOP.md sec. 1]. La muestra es solida, no enorme, pero suficiente para tratarla como direccion competitiva. El mecanismo esta en late: 9.6/10, 77.8% WR en partidas >=25' y KDA 3.45 vs target 1.81 [TOP.md sec. 5]. Eso significa que aunque la lane no explote, tus decisiones tardias como Top ganan partidas.

Fortaleza dos: Aatrox y teamfight bruiser. Aatrox tiene 13 games, 76.9% WR, KDA 3.08, DPM 893 y dmg share 23.0% [TOP.md sec. 2; TOP.md sec. 7]. Ese pick explica gran parte del fit: Aatrox permite sobrevivir, pelear extendido y absorber dano, que coincide con 31530 dano mitigado promedio y "toma dano grande y sobrevive" 0.30 por partida [TOP.md sec. 6]. Fortaleza tres: presion a estructuras razonable. Plates 2.04 por partida y dano a torres 4709 indican que no sos un Top que solo agrupa sin castigar side [TOP.md sec. 6]. Ademas, aunque el gold diff @15 sea -93, las 2.26 solo kills por partida muestran que encontrás kills aun en lanes no limpias [TOP.md sec. 4; TOP.md sec. 6].

Debilidad uno: no sos realmente splitpusher. Splitpush Index 0.16 esta en rango de teamfighters (0.15-0.25) y muy lejos del rango de splitpushers como Fiora/Trynda/Camille (0.4-0.6) [TOP.md sec. 6]. Si jugas Fiora, Camille o Irelia esperando ganar por side-lane puro, el dato no lo respalda. Irelia Top tiene 4 games, 50.0% WR, sample chico; Fiora tiene 1 game, 0.0%, sample insuficiente [TOP.md sec. 2]. Debilidad dos: CS y vision. CS@10 52.17 vs 70.30 (-25.8%), CS@15 82.96 vs 111.00 (-25.3%) y Vision/min 0.47 vs 0.80 (-40.7%) son gaps claros [TOP.md sec. 4; TOP.md sec. 8]. El mecanismo: si no wardear side y tampoco tenes splitpush index alto, tu side pressure puede volverse agrupamiento tardio forzado. Debilidad tres: early deaths. Muertes antes del 10' 1.00 por partida contra target <0.5 indican sobreextension recurrente [TOP.md sec. 6]. Eso explica por que lane phase win rate queda en 43.5% y lane lead -206, aun con gold diff @10 +154 [TOP.md sec. 5; TOP.md sec. 4].

### C) Acciones concretas para la proxima semana

1. Juga Aatrox como Top principal: 13 games, 76.9% WR, KDA 3.08 y DPM 893 son la evidencia mas fuerte de champion-role fit [TOP.md sec. 2; TOP.md sec. 7].
2. No blindees splitpushers hasta subir Splitpush Index de 0.16: el reporte dice splitpushers esperan 0.4-0.6, y tu valor encaja mas con teamfighter 0.15-0.25 [TOP.md sec. 6].
3. Tu regla antes de 10' es una muerte maxima cada dos partidas: hoy tenes 1.00 muerte antes del 10' por partida vs target <0.5, y eso arrastra lane phase a 43.5% [TOP.md sec. 6; TOP.md sec. 5].

### D) Fase fuerte y fase debil

La fase mas fuerte es late por mucho: 9.6/10, WR largo 77.8% y KDA largo 3.45 vs target 1.81 [TOP.md sec. 5]. La fase mas debil es mid game: 4.5/10, arrastrada por Vision/min 0.50 vs 0.80, score 2.1 [TOP.md sec. 5]. Early esta casi estable con 4.9/10, pero el CS@10 52.17 vs 70.30, score 3.1, y lane phase win rate 43.5% impiden llamarlo dominante [TOP.md sec. 5].

### E) Matchups

No hay matchups Top con muestra suficiente: la seccion 9 declara explicitamente "Sin matchups con muestra suficiente (min. 3 enfrentamientos)" [TOP.md sec. 9]. Por lo tanto, no corresponde inventar mejor o peor matchup. La recomendacion practica no es banear por data, sino banear por confort: si vas a blind Aatrox, prioriza bans contra campeones que te fuerzan side-lane o rango y adapta runas defensivas, pero eso queda como criterio de draft, no como conclusion estadistica del reporte.

### F) Conclusion

Top es tu mejor rol estrategico porque gana partidas tarde con Aatrox/teamfight, pero debes jugarlo como bruiser de peleas extendidas, no como splitpusher puro.

### Conexion con GLOBAL

| Metrica | Top | Global | Delta | Lectura |
|---|---:|---:|---:|---|
| WR | 65.2% | 52.5% | +12.7pp | Mejor rol por conversion [TOP.md sec. 1; GLOBAL.md sec. 1]. |
| KDA | 2.62 | 2.65 | -0.03 | Similar a global; gana por impacto, no KDA inflado [TOP.md sec. 1; GLOBAL.md sec. 1]. |
| CS/m | 5.54 | 4.63 | +19.7% | Mejor que media, pero -25.8% CS@10 vs baseline [TOP.md sec. 1; TOP.md sec. 4]. |
| DPM | 862 | 718 | +20.1% | Mejor dano cross-role y casi baseline Diamond (-3.5%) [TOP.md sec. 1; TOP.md sec. 4]. |

## Seccion 7 — Ranking final + Plan de accion

### 7.1 Ranking de roles (mejor a peor fit estrategico)

| # | Rol | Games | WR | E / M / L | Justificacion | Datos clave |
|---:|---|---:|---:|---:|---|---|
| 1 | Top | 23 | 65.2% | 4.9 / 4.5 / 9.6 | Tu mejor fit: late elite y Aatrox convierte aunque la lane no domine. | WR 65.2% [TOP.md sec. 1], Late 9.6/10 [TOP.md sec. 5], Aatrox 76.9% WR [TOP.md sec. 2] |
| 2 | Mid | 187 | 56.1% | 5.0 / 4.6 / 7.4 | Rol principal probado: alto volumen, buen WR y dano casi baseline. | WR 56.1% [MIDDLE.md sec. 1], DPM -3.0% vs baseline [MIDDLE.md sec. 4], solo kills 2.43 [MIDDLE.md sec. 6] |
| 3 | ADC | 34 | 52.9% | 4.5 / 3.9 / 7.9 | Secundario sano si jugas scaling y evitas duo support negativo. | WR 52.9% [BOTTOM.md sec. 1], Late 7.9/10 [BOTTOM.md sec. 5], Ashe 77.8% WR [BOTTOM.md sec. 2] |
| 4 | Support | 40 | 50.0% | 4.7 / 4.4 / 7.5 | Jugable en flex, pero vision no domina para un rol de mapa. | WR 50.0% [UTILITY.md sec. 1], VDR 0.92 [UTILITY.md sec. 6], Leona 71.4% WR [UTILITY.md sec. 2] |
| 5 | Jungla | 95 | 43.2% | 2.9 / 3.5 / 5.3 | Peor fit ranked: clear, tempo y soul rate pierden antes del late. | WR 43.2% [JUNGLE.md sec. 1], Early 2.9/10 [JUNGLE.md sec. 5], Soul Rate 19% [JUNGLE.md sec. 6.1] |

### 7.2 Top 5 acciones accionables cross-role

| # | Accion | Por que (evidencia con numero) | Roles afectados | Esfuerzo |
|---:|---|---|---|---|
| 1 | Subi CS@10 en roles de farm antes de agregar picks | Mid -35.3%, Jungla -37.4%, ADC -28.8%, Top -25.8% vs baseline [GLOBAL.md sec. 4] | Mid, Jungla, ADC, Top | Alto |
| 2 | Juga Top/Mid como cola principal y limita Jungla | Top 65.2% WR, Mid 56.1%, Jungla 43.2%; Jungla early 2.9/10 [GLOBAL.md sec. 3; JUNGLE.md sec. 5] | Todos | Bajo |
| 3 | Ward antes de moverte o pelear objetivo | Vision/min cae en todos los roles: Mid -29.9%, Jungla -26.8%, Support -29.3%, ADC -30.0%, Top -40.7% [GLOBAL.md sec. 4] | Todos | Medio |
| 4 | Fija pool ganador: Aatrox Top, Malzahar/Sylas Mid, Ashe ADC, Sejuani Jungla, Leona Support | Aatrox 76.9%, Malzahar 72.2%, Ashe 77.8%, Sejuani 68.4%, Leona 71.4% WR [TOP.md sec. 2; MIDDLE.md sec. 2; BOTTOM.md sec. 2; JUNGLE.md sec. 2; UTILITY.md sec. 2] | Todos | Bajo |
| 5 | Evita duos negativos por rol, especialmente ADC con Juampi Support | ADC con Juampi 33.3% WR en 9 vs 60.0% sin el en 25; global Juampi 45.7% en 127 [BOTTOM.md sec. 6.1; GLOBAL.md sec. 11] | ADC, Global | Bajo |

### 7.3 Cierre del coach jefe

Tu ranked debe concentrarse en Top como rol primario y Mid como rol de volumen: Top esta +12.7pp sobre tu WR global y Mid +3.6pp, mientras Jungla cae -9.3pp [TOP.md sec. 1; MIDDLE.md sec. 1; JUNGLE.md sec. 1]. La ganancia esperada de reemplazar Jungla por Mid ronda +12.3 victorias cada 95 games, unos +490 LP teoricos con supuesto +20/-20 [JUNGLE.md sec. 1; MIDDLE.md sec. 1]. ADC puede ser secundario de flex por 52.9% WR y late 7.9/10, pero evita ranked bot con Juampi Support por 33.3% WR vs 60.0% sin el [BOTTOM.md sec. 1; BOTTOM.md sec. 5; BOTTOM.md sec. 6.1]. La palanca humana #1 por rol es zPikA#UwU en Top: 71.4% WR en 14 games, aunque globalmente zPikA esta en 47.6% y debe usarse solo en ese contexto [TOP.md sec. 12; GLOBAL.md sec. 11]. Compromiso de la semana: subir CS@10 en Top/Mid/ADC y re-medir el sabado las ultimas 20 partidas contra los deficits actuales de -25.8%, -35.3% y -28.8% [GLOBAL.md sec. 4].
