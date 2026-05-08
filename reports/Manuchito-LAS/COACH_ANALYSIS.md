# COACH 360° — Análisis cross-role para Manuchito#LAS

_Basado exclusivamente en los reportes de `reports/Manuchito-LAS/`. Cuando una métrica no existe en los `.md`, se declara como insuficiente data o no medido aún. Citas preservadas por archivo y sección._

## Sección 1 — Overview Cross-Role

### 1.1 Identificación del rol natural

| Rol | Games | WR | KDA | CS/m | DPM | Vision |
|---|---:|---:|---:|---:|---:|---:|
| Mid | 268 | 50.0% | 2.19 | 6.47 | 918 | 21.0 |
| Top | 245 | 49.8% | 2.05 | 7.19 | 822 | 24.7 |
| Jungla | 126 | 50.8% | 2.57 | 6.12 | 635 | 24.8 |
| ADC | 38 | 34.2% | 1.95 | 6.60 | 843 | 21.4 |
| Support | 28 | 28.6% | 2.34 | 1.39 | 372 | 54.6 |

El mejor WR con mínimo 10 partidas es Jungla: 50.8% en 126 games, sample sólido [GLOBAL.md sec. 3]. El peor WR con sample útil es Support: 28.6% en 28 games, sample sólido mínimo [GLOBAL.md sec. 3]. El mejor KDA también es Jungla con 2.57 [GLOBAL.md sec. 3], pero no debe leerse aislado: su DPM es 607 vs baseline 734 (-17.4%), su CS@10 es 53.2 vs 68.0 (-21.7%) y su Vision/min es 0.83 vs 0.96 (-13.9%) [JUNGLE.md sec. 4]. Es decir, muere menos y asiste más, pero no domina el mapa ni el daño al estándar Diamond.

El mejor DPM relativo al baseline es Mid: 889 vs 857 (+3.8%) [MIDDLE.md sec. 4], y también es el mayor DPM bruto por rol con 918 [GLOBAL.md sec. 3]. Top no lidera WR ni KDA, pero tiene el CS/m más alto con 7.19 [GLOBAL.md sec. 3], un late game de 7.1/10 y KDA en partidas largas 2.76 vs target 1.81 [TOP.md sec. 5]. Por eso el rol natural competitivo se divide en dos: Mid como rol de carry por daño y lane priority, Top como rol estratégico por economía, escalado y estabilidad.

### 1.2 Inversión de tiempo vs WR

El rol más jugado es Mid: 268 de 705 partidas, 38.0% del pool [MIDDLE.md sec. 1], con 50.0% WR [GLOBAL.md sec. 3]. El mejor WR es Jungla con 50.8% en 126 partidas [GLOBAL.md sec. 3]. La diferencia Mid vs Jungla es +0.8pp, sample sólido en ambos casos, pero estratégicamente pequeña: 268 partidas * 0.008 = 2.14 wins brutas extra. Si usamos una hipótesis simple de ±25 LP por win/loss, el swing neto aproximado sería 2.14 * 2 * 25 = 107 LP en 268 games. Caveat: no es una predicción exacta, sólo una tasa de oportunidad bajo mismo MMR, mismos duos y mismo nivel de ejecución.

El misalignment real está en ADC y Support. ADC tiene 38 games, 34.2% WR y -14.2pp vs global 48.4% [BOTTOM.md sec. 1]. Support tiene 28 games, 28.6% WR y -19.8pp vs global 48.4% [UTILITY.md sec. 1]. Frente a Mid 50.0% [GLOBAL.md sec. 3], ADC deja 38 * 0.158 = 6.0 wins brutas; Support deja 28 * 0.214 = 6.0 wins brutas. Con la misma hipótesis de ±25 LP, cada rol bot ronda 300 LP de swing neto potencial. La conclusión no es "main Jungla"; es "no regalar partidas en roles bot hasta resolver sus fallas".

### 1.3 Sinergias humanas globales

La mejor sinergia global por equilibrio entre WR y volumen es Neshy Fox#LAS: 135 games, 56.3% WR [GLOBAL.md sec. 11]. Contra el WR global 48.4% [GLOBAL.md sec. 1], es +7.9pp. ZondaMC#LAS tiene 71.4% WR, pero sólo 7 games [GLOBAL.md sec. 11], sample moderado y direccional. Dënnis Rødman#LAS marca 57.1% en 14 games [GLOBAL.md sec. 11], sample sólido mínimo y +8.7pp vs global, pero mucho menos volumen que Neshy.

La peor sinergia con sample útil es HumbertoCastagna#LAS: 89 games, 34.8% WR [GLOBAL.md sec. 11], -13.6pp vs global. Z3RØ #LAS también es señal roja: 71 games, 40.8% WR [GLOBAL.md sec. 11], y en Mid específicamente 41.7% con Z3RØ como jungla (n=60) vs 52.4% sin él (n=208), delta -10.74pp [MIDDLE.md sec. 6.1]. El mecanismo importa: Mid gana lane con 61.6% Lane phase WR y +652 @14 [MIDDLE.md sec. 5], pero si la dupla jungla no convierte ese prio, la ventaja muere en roams y fights mal armados.

Por rol aliado, Top aparece muy bien con duos de presión o carries: DRX BeryL#LASS da 65.1% WR en 43 Top games, Neshy Fox#LAS 59.5% en 74 y MAXI SALAS 7#LAS2 59.1% en 93 [TOP.md sec. 12]. En Jungla, Deuda externa#LAS da 69.6% WR en 23 games [JUNGLE.md sec. 12]. En ADC, LuchiTruchi#arg da 60.0% WR en 5 games vs 30.3% sin él [BOTTOM.md sec. 6.1], sample moderado: útil si se insiste en ADC, no suficiente para recomendar el rol.

### 1.4 Patrones cruzados de fortalezas/debilidades

El patrón transversal más fuerte es CS temprano bajo vs baseline. Mid tiene CS@10 61.8 vs 75.8 (-18.5%) [MIDDLE.md sec. 4], Top 61.1 vs 70.3 (-13.1%) [TOP.md sec. 4], Jungla 53.2 vs 68.0 (-21.7%) [JUNGLE.md sec. 4], ADC 56.9 vs 75.1 (-24.2%) [BOTTOM.md sec. 4] y Support 12.4 vs 14.4 (-14.2%) [UTILITY.md sec. 4]. Como aparece en todos los roles, no es matchup-specific: es un hábito de sacrificar recursos por trade, pelea, roam o reset incompleto. La diferencia es que Mid compensa con Gold diff @15 +430 y Lane win 61.6% [MIDDLE.md sec. 4, sec. 5], mientras ADC no compensa: Gold diff @15 -83, Lane win 42.1% [BOTTOM.md sec. 4, sec. 5].

El segundo patrón es mid game vulnerable. Global Mid game es 4.7/10, con Damage/min 779 vs target 811 y Vision/min 0.79 vs 0.87 [GLOBAL.md sec. 5]. Jungla cae a 4.1/10 con DPM 606 vs 734 y Vision/min 0.84 vs 0.96 [JUNGLE.md sec. 5]. Support cae a 3.7/10 por Vision/min 1.67 vs 2.60 [UTILITY.md sec. 5]. El mecanismo causal: ganás o igualás lanes, pero entre 15-25' faltan visión útil, daño sostenido o setups de objetivo para convertir.

La fortaleza transversal es que las lanes principales sí tienen base. Global Early es 5.4/10, Lane win 55.3% y Lane lead +294 [GLOBAL.md sec. 5]. Mid sube a Early 6.1/10, Lane win 61.6% y lead +652 [MIDDLE.md sec. 5]. Top queda en Early 5.2/10, Lane win 53.1% y lead +166 [TOP.md sec. 5]. La lectura de coach jefe: no falta talento inicial; falta disciplina de recursos y mapa después de la ventaja.

### 1.5 Recomendación estratégica

Priorizá Top/Mid para ranked. Top tiene 245 games, 49.8% WR, CS/m 7.19 y Late 7.1/10 [TOP.md sec. 1, sec. 5]. Mid tiene 268 games, 50.0% WR, Lane win 61.6% y DPM +3.8% vs baseline [MIDDLE.md sec. 1, sec. 4, sec. 5]. Jungla queda como secundario sano por 50.8% WR y KDA 2.57 [JUNGLE.md sec. 1], pero no como prioridad hasta mejorar CS@10 -21.7%, DPM -17.4% y Soul Rate 24% [JUNGLE.md sec. 4, sec. 6.1]. Abandoná o limitá ADC/Support en ranked: 34.2% WR en 38 games y 28.6% WR en 28 games [BOTTOM.md sec. 1; UTILITY.md sec. 1]. La palanca humana #1 global es Neshy Fox#LAS: 56.3% WR en 135 games vs 48.4% global [GLOBAL.md sec. 11, sec. 1].

Nota estadística para leer todo el documento: Mid, Top y Jungla tienen sample sólido por volumen (268, 245 y 126 games) [GLOBAL.md sec. 3], así que las diferencias internas de fase y baseline son más confiables que cualquier lectura de un matchup puntual. ADC y Support también superan el umbral mínimo de 10 partidas (38 y 28 games) [GLOBAL.md sec. 3], por lo que su WR bajo no puede descartarse como simple varianza; lo que sí requiere caveat son sus sub-splits, como LuchiTruchi#arg en ADC con 5 games y 60.0% WR [BOTTOM.md sec. 6.1] o Janna Support con 6 games y 66.7% WR [UTILITY.md sec. 2]. En esos casos se usa "sample moderado": sirven para orientar pruebas, no para reordenar el plan central. Matchups de 3-4 games, como Vayne vs Lucian 3 games [BOTTOM.md sec. 9] o algunos duelos Top de 3-4 games [TOP.md sec. 9], son sólo direccionales. La regla de decisión es conservadora: cuando un rol tiene volumen sólido y varias métricas alineadas (Top: CS/m 7.19, Late 7.1/10, Kayle 66.7% WR [TOP.md sec. 1, sec. 5, sec. 2]), pesa más que un WR apenas superior pero con fundamentos débiles (Jungla: 50.8% WR, pero CS@10 -21.7% y DPM -17.4% [JUNGLE.md sec. 1, sec. 4]). También se separan métricas de resultado de métricas de proceso: WR/KDA ordenan el impacto final, mientras CS@10, Vision/min, muertes tempranas y Soul Rate explican qué hábito empuja ese resultado y, por lo tanto, qué acción semanal tiene más probabilidad de mover el WR.

## Sección 2 — Mid (MIDDLE)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia |
|---|---:|---|
| Lane phase WR + lead @14 | 5 | 61.6% Lane win, +652 @14, Early 6.1/10 [MIDDLE.md sec. 5] |
| Max CS lead + level lead | 4 | +33.6 CS lead y +1.8 level lead, n=267 [MIDDLE.md sec. 6] |
| Takedowns en otras lanes | 2 | 0.41 roams por partida [MIDDLE.md sec. 6] |
| Team damage + DPM | 4 | 25.2% daño equipo, DPM 889; baseline 857 (+3.8%) [MIDDLE.md sec. 6, sec. 4] |
| Aces antes del 15' | 1 | 0.01 por partida, total 3 [MIDDLE.md sec. 6] |
| Solo kills | 5 | 3.18 por partida, total 851 [MIDDLE.md sec. 6] |
| Roam Conversion Rate | 1 | >=2 roams: 27.3% WR (n=22) vs 0 roams: 49.7% (n=195) [MIDDLE.md sec. 6.1] |
| Synergy WR con Jungla | 2 | Con Z3RØ 41.7% (n=60) vs sin él 52.4% (n=208) [MIDDLE.md sec. 6.1] |

Mid es tu rol de carry más claro. La muestra es sólida: 268 partidas, 50.0% WR, KDA 2.19, CS/m 6.47, DPM 918 y Vision avg 21.0 [MIDDLE.md sec. 1]. El punto más fuerte es lane priority: 61.6% de Lane phase win rate, +652 de lead promedio @14 y 4.97 takedowns en los primeros 14' vs target 4.09 [MIDDLE.md sec. 5]. Eso significa que no sólo sobrevivís mid; generás ventaja temprana. También hay evidencia de amenaza individual: 3.18 solo kills por partida y max CS lead +33.6 [MIDDLE.md sec. 6].

La contradicción es que ganás lane con farm absoluto bajo. CS@10 es 61.8 vs baseline 75.8 (-18.5%) y CS@15 99.5 vs 115.3 (-13.7%) [MIDDLE.md sec. 4], pero Gold diff @15 es +430 y CS diff @15 +7 [MIDDLE.md sec. 4]. Mecanismo: castigás al rival con kills/trades y aun así quedás arriba del oponente directo, pero el estándar Diamond espera más recursos absolutos. Contra mids que escalan o limpian mejor, ese déficit se vuelve visible si no convertís temprano.

Fortalezas Mid-específicas: primero, lane dominance real por 61.6% Lane win y +652 @14 [MIDDLE.md sec. 5]. Segundo, daño de carry: DPM 889 vs baseline 857 (+3.8%) y 25.2% del daño del equipo [MIDDLE.md sec. 4, sec. 6]. Tercero, pool con identidad: Akshan tiene 135 games, 56.3% WR y DPM 1024; Orianna tiene 13 games, 69.2% WR, KDA 3.29 y CS/m 7.17, sample sólido mínimo y muy buena dirección [MIDDLE.md sec. 2].

Debilidades: primero, roam mal convertido. Con >=2 roams ganás 27.3% (n=22), con 0 roams 49.7% (n=195), delta -22.47pp [MIDDLE.md sec. 6.1]. Esto indica salidas sin wave crash, sin jungla visible o hacia sides que no pueden cerrar. Segundo, snowball colectivo bajo: aces antes del 15' son 0.01 por partida, total 3 en 268 games [MIDDLE.md sec. 6]. Tercero, visión de mid insuficiente: Vision/min 0.66 vs 0.75 (-11.8%) [MIDDLE.md sec. 4], y en fase media 0.68 vs 0.75, score 4.3 [MIDDLE.md sec. 5]. Si ganás mid pero no wardéas profundo, tus roams son apuestas.

Acciones semanales: 1) no roamees antes de crash completo salvo kill garantizada; el split de roams es -22.47pp [MIDDLE.md sec. 6.1]. 2) Objetivo mínimo de CS@10: subir de 61.8 a 68 antes de perseguir 75.8 [MIDDLE.md sec. 4]. 3) Con Z3RØ #LAS como jungla, jugá waveclear/daño estable y no picks dependientes de coordinación, porque el WR cae a 41.7% juntos vs 52.4% sin él [MIDDLE.md sec. 6.1].

Fase más fuerte: Early 6.1/10, por Lane win 61.6% y +652 @14 [MIDDLE.md sec. 5]. Fase más débil relativa: Mid game 5.1/10, arrastrada por Vision/min 0.68 vs 0.75 [MIDDLE.md sec. 5]. Pool ideal: Akshan, Orianna y Zoe; Zoe tiene 61 games, 49.2% WR, KDA 2.50 y sample sólido [MIDDLE.md sec. 2]. Evitá Aurelion Sol (18 games, 33.3% WR), Twisted Fate (5 games, 0.0% WR, sample moderado) y Qiyana por sample chico de 3 games [MIDDLE.md sec. 2, sec. 8].

### Conexión con GLOBAL

Mid está +1.6pp sobre global: 50.0% vs 48.4% [MIDDLE.md sec. 1]. KDA es idéntico: 2.19 vs 2.19 [MIDDLE.md sec. 1]. CS/m casi igual: 6.47 vs 6.45 (+0.02), pero DPM sube 918 vs 808 (+110, +13.6%) [MIDDLE.md sec. 1]. Además, el DPM filtrado está +3.8% vs baseline Diamond Mid [MIDDLE.md sec. 4]. Conclusión: Mid es rol natural de carry si convertís lane priority en visión y tempo selectivo, no en roams de bajo porcentaje.

## Sección 3 — Top (TOP)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia |
|---|---:|---|
| Gold diff @15 | 3 | -17 vs rival, prácticamente even [TOP.md sec. 4] |
| Lane phase WR + lead @14 | 4 | 53.1% Lane win, +166 @14 [TOP.md sec. 5] |
| Solo kills + quick solo kills | 4 | 2.71 solo kills, 0.04 quick solo kills [TOP.md sec. 6] |
| Plates + daño a torres | 5 | 10.03 plates, 9987 daño a torres [TOP.md sec. 6] |
| Daño mitigado | 5 | 37005 promedio, n=245 [TOP.md sec. 6] |
| Splitpush Index | 4 | 0.44; rango splitpushers 0.4-0.6 [TOP.md sec. 6] |
| KDA en partidas largas | 5 | 2.76 vs target 1.81, score 9.0 [TOP.md sec. 5] |

Top es el rol más estable para ranked sostenido. Tiene 245 partidas, 49.8% WR, KDA 2.05, CS/m 7.19, DPM 822 y Vision avg 24.7 [TOP.md sec. 1]. Aunque no supera a Jungla en WR bruto, su perfil es más repetible: CS/m +0.74 sobre global, DPM +14 sobre global y Vision +0.4 sobre global [TOP.md sec. 1]. Además, su late game es el mejor de todos los roles principales: 7.1/10, con WR en partidas largas 51.7% y KDA 2.76 vs target 1.81 [TOP.md sec. 5].

La lane no es aplastante, pero es suficiente. Gold diff @15 es -17 [TOP.md sec. 4], Lane win 53.1% y lead +166 @14 [TOP.md sec. 5]. CS@10 está 61.1 vs baseline 70.3 (-13.1%) [TOP.md sec. 4], pero CS diff @15 es +2 [TOP.md sec. 4]. Eso significa que el ritmo absoluto de farm está bajo, aunque el rival directo tampoco te supera. El mecanismo probable es que jugás trades largos o resets imperfectos, pero mantenés presión por matchup o kills.

Fortalezas Top-específicas: primero, escalado. Late 7.1/10 y KDA larga 2.76 vs 1.81 [TOP.md sec. 5] sostienen que tu toma de decisiones mejora post-25. Segundo, presión estructural: 10.03 plates por partida, 9987 daño a torres y Splitpush Index 0.44 [TOP.md sec. 6]. Tercero, valor de front y sustain: 37005 daño mitigado promedio [TOP.md sec. 6]. El pool acompaña: Mordekaiser 59 games, 55.9% WR, KDA 2.48; Kayle 27 games, 66.7% WR; Akshan Top 10 games, 60.0% WR [TOP.md sec. 2].

Debilidades: primero, muertes tempranas. 1.65 muertes antes del 10' por partida con target <0.5 [TOP.md sec. 6] es el leak más caro: una muerte antes de que la wave rebote entrega placas, tempo de jungla y TP defensivo. Segundo, DPM bajo para el baseline del rol: 792 vs 830 (-4.6%) [TOP.md sec. 4], con Mid game Damage/min 792 vs target 830 [TOP.md sec. 5]. Tercero, campeones que contradicen tu identidad: Sion 26 games, 38.5% WR, KDA 1.20; Tryndamere 5 games, 20.0% WR, sample moderado [TOP.md sec. 2]. Si tu late es fuerte y tus muertes tempranas son altas, esos picks amplifican el problema.

Acciones semanales: 1) regla de supervivencia hasta minuto 10: bajar de 1.65 muertes tempranas hacia <1 antes de buscar el target <0.5 [TOP.md sec. 6]. 2) Priorizá Mordekaiser/Kayle: 55.9% WR en 59 y 66.7% en 27 [TOP.md sec. 2], con Late 7.1/10 [TOP.md sec. 5]. 3) Contra Sion enemigo, prepará ban/counter: Mordekaiser vs Sion tiene 16.7% WR en 6 games, sample moderado [TOP.md sec. 9].

Fase más fuerte: Late 7.1/10, por KDA larga 2.76 vs 1.81 [TOP.md sec. 5]. Fase más débil: Mid game 5.0/10, arrastrada por Damage/min 792 vs 830 [TOP.md sec. 5]. Mejor matchup con sample moderado: Akshan vs Gangplank, 5 games, 100.0% WR, KDA 2.80, DPM 1133 [TOP.md sec. 9]. Peor matchup útil: Mordekaiser vs Sion, 6 games, 16.7% WR [TOP.md sec. 9]. Pool ideal: Mordekaiser, Kayle, Ornn/Singed según draft. Evitá Sion, Tryndamere y limitá Jax hasta mejorar 40.0% WR en 15 games [TOP.md sec. 2].

### Conexión con GLOBAL

Top está +1.4pp sobre global: 49.8% vs 48.4% [TOP.md sec. 1]. KDA está -0.14: 2.05 vs 2.19 [TOP.md sec. 1], pero CS/m está +0.74 (+11.5%) y DPM +14 [TOP.md sec. 1]. Frente al baseline del rol, DPM queda -4.6% y CS@10 -13.1% [TOP.md sec. 4]. Conclusión: Top es tu rol natural estratégico por economía y late, siempre que reduzcas muertes antes del 10'.

## Sección 4 — Jungla (JUNGLE)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia |
|---|---:|---|
| Jungle CS antes del 10' | 3 | 57.13, pero CS@10 rol 53.2 vs 68.0 (-21.7%) [JUNGLE.md sec. 6, sec. 4] |
| Counter-jungle ratio | 1 | 0.09; enemy jungle CS 6.02 vs propia 70.21 [JUNGLE.md sec. 6] |
| Takedowns en otras lanes early | 0 | No medido aún, N=0 [JUNGLE.md sec. 6] |
| Drakes + Heralds + Barones | 4 | 2.34 drakes, 0.47 heraldos, 0.48 barones [JUNGLE.md sec. 6] |
| Cobertura río/jungla enemiga | 4 | 62.8%, n=59 [JUNGLE.md sec. 6] |
| Tempo level 6 | 4 | 466s promedio; referencia Lee Sin diamond ~450s [JUNGLE.md sec. 6] |
| Soul Rate | 2 | 23/97 partidas largas, 24% [JUNGLE.md sec. 6.1] |
| Gank-to-Death ratio | 0 | No medido aún, N=0 [JUNGLE.md sec. 6] |

Jungla tiene el mejor WR bruto: 50.8% en 126 games, sample sólido [JUNGLE.md sec. 1]. También tiene el mejor KDA: 2.57 (5.8/5.7/8.8) [JUNGLE.md sec. 1]. Pero el resto del perfil baja la recomendación: CS@10 53.2 vs 68.0 (-21.7%), CS@15 84.5 vs 104.3 (-19.0%), KP 48.3% vs 52.1% (-7.3%), DPM 607 vs 734 (-17.4%) y Vision/min 0.83 vs 0.96 (-13.9%) [JUNGLE.md sec. 4]. Ganás algunas partidas, pero no por dominio sistemático del rol.

El pathing tiene una base recuperable. CS de jungla antes del 10' es 57.13 [JUNGLE.md sec. 6], y el tiempo a level 6 es 466s [JUNGLE.md sec. 6], cercano a la referencia Lee Sin diamond ~450s y mejor que Karthus ~510s [JUNGLE.md sec. 6]. Eso indica que el primer clear no está roto. El problema aparece en el mapa posterior: Mid game 4.1/10, con Damage/min 606 vs 734 y Vision/min 0.84 vs 0.96 [JUNGLE.md sec. 5].

Fortalezas: primero, objetivos básicos: 2.34 drakes, 0.47 heraldos y 0.48 barones por partida [JUNGLE.md sec. 6]. Segundo, cobertura en zonas de objetivo: 62.8% wards en río/jungla enemiga, n=59, sample sólido [JUNGLE.md sec. 6]. Tercero, duos/picks con señal: Deuda externa#LAS da 69.6% WR en 23 games [JUNGLE.md sec. 12], y Zac + Lulu tiene 87.5% WR en 8 games, sample moderado [JUNGLE.md sec. 13].

Debilidades: Counter-jungle ratio 0.09 es muy bajo [JUNGLE.md sec. 6]. Son 6.02 CS de jungla enemiga vs 70.21 de propia [JUNGLE.md sec. 6], lo que te vuelve predecible si no gankeás más que el rival. Gank impact temprano está no medido (N=0) y Gank-to-Death ratio también no medido (N=0) [JUNGLE.md sec. 6], así que no se puede afirmar que estés compensando con ganks. Soul Rate 24% en 97 partidas largas [JUNGLE.md sec. 6.1] confirma que el control de dragones no termina en cierre de soul.

Acciones semanales: 1) objetivo de 60+ jungle CS antes del 10', desde el valor actual 57.13 [JUNGLE.md sec. 6]. 2) Jugá Shyvana como identidad principal: 43 games, 53.5% WR, CS/m 7.43, DPM 709 [JUNGLE.md sec. 2]. 3) Planificá dragón desde 4:30 con reset y visión, porque Soul Rate es 24% [JUNGLE.md sec. 6.1]. No invento gank ratio: está no medido aún por N=0 [JUNGLE.md sec. 6].

Fase más fuerte: Late 5.5/10, KDA larga 3.30 vs target 2.78 [JUNGLE.md sec. 5]. Fase más débil: Mid game 4.1/10, por DPM 606 vs 734 y Vision/min 0.84 vs 0.96 [JUNGLE.md sec. 5]. Pool ideal: Shyvana, Zac y Nunu/Brand sólo como pruebas, porque Nunu y Brand tienen 4 games cada uno, sample chico [JUNGLE.md sec. 2]. Evitá Lillia (5 games, 0.0% WR) y Volibear (8 games, 37.5% WR), samples moderados con mala señal [JUNGLE.md sec. 2].

### Conexión con GLOBAL

Jungla está +2.4pp sobre global: 50.8% vs 48.4% [JUNGLE.md sec. 1]. KDA sube 2.57 vs 2.19 (+0.37, +16.9%) [JUNGLE.md sec. 1]. Pero CS/m baja 6.12 vs 6.45 (-0.33) y DPM cae 635 vs 808 (-173, -21.4%) [JUNGLE.md sec. 1]. Contra baseline, además, DPM es -17.4% y CS@10 -21.7% [JUNGLE.md sec. 4]. Conclusión: Jungla es secundario sano, no rol primario todavía.

## Sección 5 — ADC (BOTTOM)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia |
|---|---:|---|
| DPM + % daño equipo | 2 | DPM 812, 21.6% daño; DPM -11.8% vs baseline [BOTTOM.md sec. 6, sec. 4] |
| Positioning Index | 3 | 0.99; target Diamond ~1.0-1.4 [BOTTOM.md sec. 6] |
| Torres/first turret rápida | 1 | 0.00 y 0.00 [BOTTOM.md sec. 6] |
| Items legendarios | 1 | 0.08 por partida, total 3 [BOTTOM.md sec. 6] |
| Scaling Score | 1 | KDA largas 2.44 vs cortas 3.31, ratio 0.74 [BOTTOM.md sec. 6.1] |
| Lane phase WR + lead @14 | 2 | 42.1% Lane win, -29 @14 [BOTTOM.md sec. 5] |
| Muertes antes del 25' | 1 | 5.87 por partida, target <3 [BOTTOM.md sec. 6] |
| Synergy WR con Support | 4 | LuchiTruchi 60.0% (n=5) vs 30.3% sin él [BOTTOM.md sec. 6.1] |

ADC debe evitarse en ranked salvo condición de duo. Tiene 38 partidas, 34.2% WR, KDA 1.95, CS/m 6.60, DPM 843 y Vision 21.4 [BOTTOM.md sec. 1]. Algunos brutos parecen aceptables: CS/m +0.15 y DPM +35 sobre global [BOTTOM.md sec. 1]. Pero contra el rol, el reporte cae fuerte: CS@10 56.9 vs 75.1 (-24.2%), CS@15 91.9 vs 114.9 (-20.0%), KP 44.4% vs 48.5% (-8.4%) y DPM 813 vs 921 (-11.8%) [BOTTOM.md sec. 4]. En ADC, estar bien contra tu promedio global no alcanza porque el rival directo escala con los mismos recursos.

La falla principal es llegar tarde o muerto al spike. Items legendarios completados por partida es 0.08, total 3 en 38 games [BOTTOM.md sec. 6]. Muertes antes del 25' son 5.87 por partida, con target <3 [BOTTOM.md sec. 6]. El mecanismo es directo: cada muerte temprana quita waves, placas, reset y presencia en dragón; por eso el late no aparece. Positioning Index 0.99 está casi en el piso del target Diamond 1.0-1.4 [BOTTOM.md sec. 6], así que no es sólo pasividad: hay peleas con margen muy fino.

Fortalezas: primero, DPM bruto 812 y 21.6% del daño del equipo [BOTTOM.md sec. 6], aunque bajo baseline. Segundo, con LuchiTruchi#arg el WR sube a 60.0% en 5 games vs 30.3% sin él, delta +29.70pp [BOTTOM.md sec. 6.1], sample moderado. Tercero, skillshots dodgeados 2.24 y Positioning Index 0.99 [BOTTOM.md sec. 6] sugieren que hay base mecánica, pero no convertida en macro de carry.

Debilidades: Vayne concentra 26 games con 34.6% WR, KDA 2.16, CS/m 6.37 y DPM 892 [BOTTOM.md sec. 2]. Vayne debería pagar en late, pero el rol tiene Late 3.5/10, WR en largas 31.4% y KDA larga 2.26 vs target 2.30 [BOTTOM.md sec. 5]. Scaling Score confirma caída: KDA largas 2.44 vs cortas 3.31, ratio 0.74 [BOTTOM.md sec. 6.1]. También falta lane priority: Lane win 42.1%, lead -29 @14 y CS@10 -24.2% [BOTTOM.md sec. 5, sec. 4]. Por último, presión estructural nula: torres antes de plates 0.00 y first turret rápida 0.00 [BOTTOM.md sec. 6].

Acciones semanales: 1) ADC sólo con LuchiTruchi#arg o soporte coordinado, por 60.0% con él vs 30.3% sin él [BOTTOM.md sec. 6.1]. 2) Sacá Vayne de ranked una semana: 26 games, 34.6% WR y Scaling Score 0.74 [BOTTOM.md sec. 2, sec. 6.1]. 3) Medí muertes antes del 25': bajar de 5.87 a menos de 4 antes de buscar DPM; el target del reporte es <3 [BOTTOM.md sec. 6].

Fase más fuerte por descarte: Early 4.7/10 [BOTTOM.md sec. 5]. Fase más débil: Late 3.5/10, con WR largas 31.4% vs target 50.0% [BOTTOM.md sec. 5]. Pool ideal con evidencia suficiente no existe: Varus tiene 4 games y 75.0% WR, sample chico; Kai'Sa 1 game, sample insuficiente; Lucian 4 games y 0.0% WR, sample chico [BOTTOM.md sec. 2]. Si se testea, Varus puede ser prueba controlada, pero Vayne/Lucian deben salir de ranked. Mejor matchup reportado: Vayne vs Lucian 66.7% en 3 games, sample chico; la tabla de peor matchup repite el mismo dato, así que insuficiente data para peor matchup distinto [BOTTOM.md sec. 9].

### Conexión con GLOBAL

ADC está -14.2pp bajo global: 34.2% vs 48.4% [BOTTOM.md sec. 1]. KDA está -0.24: 1.95 vs 2.19 [BOTTOM.md sec. 1]. CS/m está +0.15 sobre global, pero contra baseline ADC el CS@10 está -24.2% [BOTTOM.md sec. 4]. DPM está +35 sobre global, pero -11.8% vs baseline ADC [BOTTOM.md sec. 1, sec. 4]. Conclusión: ADC está peor que tu media real de victoria y peor que el estándar del rol; no es ranked-safe ahora.

## Sección 6 — Support (UTILITY)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia |
|---|---:|---|
| Vision/min + diff rival | 2 | 1.67, diff -0.3; baseline 2.60 (-36.3%) [UTILITY.md sec. 6, sec. 4] |
| Cobertura río/jungla enemiga | 4 | 63.5%, n=20 [UTILITY.md sec. 6] |
| Heal+shield + saves | 4 | 5762 heals+shields, 1.68 saves [UTILITY.md sec. 6] |
| CC + picks | 5 | 33.79 CC, 13.18 picks coordinados [UTILITY.md sec. 6] |
| Vision Dominance Ratio | 2 | 0.75, target >1.3 [UTILITY.md sec. 6] |
| Roam impact | 1 | 0.11 takedowns en otras lanes [UTILITY.md sec. 6] |
| Quest support a tiempo | 4 | 0.79 rate, 22/28 [UTILITY.md sec. 6] |

Support tiene buenas piezas de micro, pero mal resultado competitivo. Son 28 partidas, 28.6% WR, KDA 2.34, CS/m 1.39, DPM 372 y Vision avg 54.6 [UTILITY.md sec. 1]. Contra global, el KDA sube +0.14 y Vision avg +30.3 [UTILITY.md sec. 1], pero WR cae -19.8pp [UTILITY.md sec. 1]. Eso significa que la visión bruta o la supervivencia no están transformándose en mapa ganador.

El arquetipo más respaldado es enchanter/disengage. Janna tiene 6 games, 66.7% WR, KDA 5.40 y Vision 53.7, sample moderado positivo [UTILITY.md sec. 2]. Thresh tiene 3 games, 66.7% WR, sample chico y no concluyente [UTILITY.md sec. 2]. Las stats avanzadas muestran buena utilidad en pelea: heals+shields 5762, saves 1.68, CC 33.79, picks 13.18 y CC+kill con aliado 6.32 [UTILITY.md sec. 6]. Cuando la pelea ocurre frente a vos, aportás. El problema es elegir y preparar mejores peleas.

La debilidad crítica es visión relativa. Vision/min 1.67 [UTILITY.md sec. 6] está por debajo del baseline 2.60 (-36.3%) [UTILITY.md sec. 4]. Diff de visión vs support rival es -0.3 y Vision Dominance Ratio 0.75, cuando el target del reporte es >1.3 [UTILITY.md sec. 6]. El mecanismo: si el rival controla más visión, tus CC/saves llegan a peleas que el enemigo ya decidió. Esto hunde el Mid game: 3.7/10, con Vision/min 1.67 vs 2.60, score 2.3 [UTILITY.md sec. 5].

Fortalezas: Early 5.7/10, Lane win 67.9% y lead +279 @14 [UTILITY.md sec. 5]; utilidad de combate alta por CC 33.79 y picks 13.18 [UTILITY.md sec. 6]; quest support a tiempo 0.79, 22 de 28 [UTILITY.md sec. 6]. Debilidades: Vision/min -36.3% vs baseline [UTILITY.md sec. 4], roam impact 0.11 [UTILITY.md sec. 6] y WR en partidas largas 32.0% pese a KDA larga 3.52 vs target 2.65 [UTILITY.md sec. 5]. Eso último indica que sobrevivís y asistís, pero no cerrás mapa.

Acciones semanales: 1) control ward antes de cada dragón y reset de bot; tenés 1.86 control wards por partida y Vision/min -36.3% vs baseline [UTILITY.md sec. 6, sec. 4]. 2) Janna como pick principal si vas support: 6 games, 66.7% WR, KDA 5.40 [UTILITY.md sec. 7]. 3) No roamees sin crash o recall coordinado; roam impact 0.11 [UTILITY.md sec. 6] no justifica abandonar bot sin información.

Fase más fuerte: Early 5.7/10 [UTILITY.md sec. 5]. Fase más débil: Mid game 3.7/10, por Vision/min 1.67 vs 2.60 [UTILITY.md sec. 5]. Mejor duo persona para Support: Neshy Fox#LAS, 50.0% WR en 14 games [UTILITY.md sec. 12], mejor que Juampi 33.3% en 18 y zPikA 26.7% en 15 [UTILITY.md sec. 12]. No hay matchups con muestra suficiente, así que mejor/peor matchup es insuficiente data [UTILITY.md sec. 9]. Pool ideal: Janna; Lulu/Nami sólo práctica por 2 games y 0.0% WR; Thresh sólo prueba no ranked por 3 games, sample chico [UTILITY.md sec. 2].

### Conexión con GLOBAL

Support está -19.8pp bajo global: 28.6% vs 48.4% [UTILITY.md sec. 1]. KDA sube 2.34 vs 2.19 (+0.14), pero no se convierte en WR [UTILITY.md sec. 1]. Vision avg sube 54.6 vs 24.3, pero Vision/min contra baseline cae 1.66 vs 2.60 (-36.3%) [UTILITY.md sec. 1, sec. 4]. DPM 372 vs 808 global es esperable por rol, pero también está -10.2% vs baseline Support [UTILITY.md sec. 1, sec. 4]. Conclusión: Support no es ranked-safe hasta arreglar visión relativa y mid game.

## Sección 7 — Ranking final + Plan de acción

### 7.1 Ranking de roles (mejor → peor fit estratégico)

| # | Rol | Games | WR | E / M / L | Justificación (1 oración, ≤25 palabras) | Datos clave (2-3 stats con valor) |
|---:|---|---:|---:|---:|---|---|
| 1 | Top | 245 | 49.8% | 5.2 / 5.0 / 7.1 | Rol natural estratégico: economía sana, late fuerte y pool ganador. | CS/m 7.19 [TOP.md sec. 1], Late 7.1/10 [TOP.md sec. 5], Kayle 66.7% WR [TOP.md sec. 2] |
| 2 | Mid | 268 | 50.0% | 6.1 / 5.1 / 5.5 | Mejor rol de carry, pero roams mal convertidos limitan el techo. | Lane win 61.6% [MIDDLE.md sec. 5], DPM +3.8% [MIDDLE.md sec. 4], roam delta -22.47pp [MIDDLE.md sec. 6.1] |
| 3 | Jungla | 126 | 50.8% | 4.6 / 4.1 / 5.5 | Mejor WR bruto, pero pathing, DPM y soul rate no son repetibles. | KDA 2.57 [JUNGLE.md sec. 1], CS@10 -21.7% [JUNGLE.md sec. 4], Soul 24% [JUNGLE.md sec. 6.1] |
| 4 | ADC | 38 | 34.2% | 4.7 / 4.4 / 3.5 | Rol a evitar salvo duo: muertes tempranas niegan scaling. | Deaths<25 5.87 [BOTTOM.md sec. 6], Late 3.5/10 [BOTTOM.md sec. 5], WR 34.2% [BOTTOM.md sec. 1] |
| 5 | Support | 28 | 28.6% | 5.7 / 3.7 / 4.9 | Early aceptable, pero visión relativa y mid game hunden impacto. | Vision/min -36.3% [UTILITY.md sec. 4], VDR 0.75 [UTILITY.md sec. 6], WR 28.6% [UTILITY.md sec. 1] |

El ranking prioriza Top sobre Mid aunque Mid tenga +0.2pp WR porque Top tiene Late 7.1/10, CS/m 7.19 y pool más consistente [TOP.md sec. 1, sec. 2, sec. 5]. La diferencia Top/Mid es chica y ambos son roles recomendados; el cambio grande es sacar ADC/Support.

### 7.2 Top 5 acciones accionables cross-role

| # | Acción | Por qué (evidencia con número) | Roles afectados | Esfuerzo |
|---:|---|---|---|---|
| 1 | Subí CS@10 antes de forzar roams o trades largos | Mid 61.8 vs 75.8, Top 61.1 vs 70.3, ADC 56.9 vs 75.1 [GLOBAL.md sec. 4] | Mid, Top, ADC, Jungla | Alto |
| 2 | Jugá ranked sólo en Top/Mid esta semana | ADC 34.2% WR y Support 28.6% WR vs Top 49.8% y Mid 50.0% [GLOBAL.md sec. 3] | Todos | Bajo |
| 3 | Reducí muertes tempranas en Top y ADC | Top muertes<10 1.65 vs target <0.5; ADC muertes<25 5.87 vs target <3 [TOP.md sec. 6; BOTTOM.md sec. 6] | Top, ADC | Alto |
| 4 | Priorizá duo con Neshy Fox#LAS o DRX BeryL#LASS en Top | Neshy 56.3% WR en 135 global; DRX BeryL 65.1% WR en 43 Top [GLOBAL.md sec. 11; TOP.md sec. 12] | Top, Mid | Bajo |
| 5 | Colocá visión antes de objetivos, no después | Support Vision/min 1.66 vs 2.60 (-36.3%); Jungla Soul Rate 24% [UTILITY.md sec. 4; JUNGLE.md sec. 6.1] | Support, Jungla, Mid | Medio |

### 7.3 Cierre del coach jefe

Tu ranked debe concentrarse en Top como primario y Mid como co-primario: Top tiene 245 games, Late 7.1/10 y CS/m 7.19, mientras Mid tiene 268 games, 50.0% WR y DPM +3.8% vs baseline [TOP.md sec. 1, sec. 5; MIDDLE.md sec. 1, sec. 4]. La ganancia esperada no viene de cambiar Mid por Jungla (+0.8pp), sino de sacar ADC/Support: pasar de 34.2%/28.6% WR a ~50% equivale a +16-21pp por partida [GLOBAL.md sec. 3]. Jungla queda como secundario sano por 50.8% WR, pero limitado por CS@10 -21.7% y Soul Rate 24% [JUNGLE.md sec. 4, sec. 6.1]. No toques ADC ni Support en ranked salvo duo específico; la palanca humana #1 global es Neshy Fox#LAS, 56.3% WR en 135 games vs 48.4% global [GLOBAL.md sec. 11, sec. 1]. Compromiso semanal: subir CS@10 en Top/Mid y re-medimos las últimas 20 partidas contra 61.1 Top y 61.8 Mid [TOP.md sec. 4; MIDDLE.md sec. 4]. Si el CS sube sin bajar WR de lane, el plan se mantiene. Si baja, priorizá wave control sobre trades y resets.
