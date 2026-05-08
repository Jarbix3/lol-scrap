# COACH 360° — Análisis cross-role para Juampi Torryco#LAS

Generado a partir de `GLOBAL.md`, `UTILITY.md`, `TOP.md`, `MIDDLE.md`, `BOTTOM.md` y `JUNGLE.md`. Regla de lectura: cuando una métrica no existe en los reportes, queda marcada como **insuficiente data** o **no medido aún**.

## Sección 1 — Overview Cross-Role

### 1.1 Identificación del rol natural

| Rol | Games | WR | KDA | CS/m | DPM | Vision | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| Support | 108 | 47.2% | 3.14 | 1.04 | 333 | 52.6 | Rol más jugado, KDA más alto, WR bajo la media global [GLOBAL.md sec. 3] |
| Top | 88 | 51.1% | 2.35 | 5.84 | 791 | 27.5 | Mejor DPM relativo al baseline: 772 vs 830, -7.0% [GLOBAL.md sec. 3, sec. 4] |
| Mid | 75 | 46.7% | 2.42 | 5.34 | 671 | 25.9 | Peor WR entre roles con sample sólido [GLOBAL.md sec. 3] |
| ADC | 64 | 51.6% | 2.93 | 5.67 | 786 | 20.0 | Mejor WR absoluto con 64 games, sample sólido [GLOBAL.md sec. 3] |
| Jungla | 64 | 46.9% | 2.36 | 4.74 | 460 | 27.6 | WR bajo y DPM más castigado vs baseline: 447 vs 734, -39.2% [GLOBAL.md sec. 3, sec. 4] |

El rol con mejor WR es **ADC**, con 51.6% en 64 partidas, sample sólido por estar sobre 10 games [GLOBAL.md sec. 3]. Top queda prácticamente empatado con 51.1% en 88 partidas, pero la diferencia entre ADC y Top es de apenas +0.5pp; con ambos samples sólidos, la señal existe pero no es grande [GLOBAL.md sec. 3]. El peor WR es **Mid**, con 46.7% en 75 partidas, apenas por debajo de Jungla 46.9% en 64 partidas; la diferencia Mid vs Jungla es -0.2pp y no debe leerse como separación real [GLOBAL.md sec. 3].

El mejor KDA no coincide con el mejor WR: Support tiene 3.14 KDA, pero solo 47.2% WR, mientras ADC tiene 2.93 KDA y 51.6% WR [GLOBAL.md sec. 3]. La causa probable es estructural: en Support acumulás assists y menos kills, lo que sube KDA, pero el rol también está -38.2% en Vision/min vs baseline y -20.2% en DPM, así que la supervivencia no se traduce automáticamente en control de mapa o daño útil [GLOBAL.md sec. 4]. En cambio, ADC convierte mejor el resultado aunque tenga KDA menor que Support: 51.6% WR, 786 DPM y 5.67 CS/m, contra 47.2% WR, 333 DPM y 1.04 CS/m en Support [GLOBAL.md sec. 3].

El mejor DPM relativo a baseline es **Top**, no ADC. Top tiene 772 DPM vs baseline 830, delta -7.0%, mientras ADC tiene 743 vs 921, delta -19.3%, Mid 657 vs 857, delta -23.3%, Support 327 vs 409, delta -20.2%, y Jungla 447 vs 734, delta -39.2% [GLOBAL.md sec. 4]. Esto importa porque Top es el único rol donde el daño queda cerca del estándar Diamond y, además, tiene Vision/min positiva: 0.85 vs baseline 0.80, +5.8% [GLOBAL.md sec. 4]. Si el criterio es "fit competitivo sostenible", Top tiene menos techo bruto de WR que ADC por 0.5pp, pero mejores fundamentos relativos.

### 1.2 Inversión de tiempo vs WR

El rol más jugado es Support: 108 de 399 partidas, 27.1% del pool, con 47.2% WR [UTILITY.md sec. 1]. No es el rol de mejor WR; ADC tiene 51.6% en 64 partidas y Top 51.1% en 88 partidas [GLOBAL.md sec. 3]. Hay un misalignment estratégico porque estás invirtiendo más volumen en el rol que está -1.4pp por debajo de tu WR global 48.6%, mientras el ADC está +2.9pp sobre global y Top +2.5pp sobre global [UTILITY.md sec. 1; BOTTOM.md sec. 1; TOP.md sec. 1].

La tasa de oportunidad perdida, usando WR como proxy porque el reporte no trae LP ganado/perdido por partida, es clara: mover 108 partidas de Support 47.2% al rendimiento ADC 51.6% equivale a +4.4pp WR, o **+4.75 victorias esperadas cada 108 games** [UTILITY.md sec. 1; BOTTOM.md sec. 1]. Frente a Top, el mismo volumen sería +3.9pp, o **+4.21 victorias esperadas cada 108 games** [UTILITY.md sec. 1; TOP.md sec. 1]. LP exacto es **insuficiente data** porque ningún archivo informa LP promedio por win/loss; la lectura responsable es en victorias esperadas, no en LP inventado.

### 1.3 Sinergias humanas globales

| Partner | Games | WR juntos | Delta vs WR global 48.6% | Lectura |
|---|---:|---:|---:|---|
| Maldito Makelele#Fancy | 10 | 80.0% | +31.4pp | Mejor palanca, sample sólido mínimo; casi todo MasterYi (9) [GLOBAL.md sec. 11] |
| edenja#LAS | 7 | 71.4% | +22.8pp | Sample moderado, dirección positiva pero menos concluyente [GLOBAL.md sec. 11] |
| Reventon95#LAS | 74 | 56.8% | +8.2pp | Mejor señal robusta por volumen [GLOBAL.md sec. 11] |
| Neshy Fox#LAS | 148 | 52.0% | +3.4pp | Sólido y estable, mejora moderada [GLOBAL.md sec. 11] |
| MAXI SALAS 7#LAS2 | 239 | 50.2% | +1.6pp | Mucho volumen, mejora chica [GLOBAL.md sec. 11] |

La mejor sinergia pura es **Maldito Makelele#Fancy**: 10 games juntos, 80.0% WR, contra tu 48.6% global; eso es +31.4pp y sample sólido por llegar a 10 [GLOBAL.md sec. 11; GLOBAL.md sec. 1]. El caveat es de rol/patrón: sus top campeones son MasterYi (9) y Shaco (1), así que la señal parece de jungla carry que simplifica tu rol de daño/side o de front-to-back [GLOBAL.md sec. 11]. La sinergia más rentable por volumen es **Reventon95#LAS**, con 74 games y 56.8% WR, +8.2pp sobre tu global; si hay que elegir una palanca replicable, esta pesa más que un 10-game spike [GLOBAL.md sec. 11].

El peor partner con sample útil es **Red Khiedis#LAS**: 14 games, 14.3% WR, -34.3pp vs tu WR global 48.6%, con Morgana (6), Ekko (3), Caitlyn (2) como campeones frecuentes [GLOBAL.md sec. 11; GLOBAL.md sec. 1]. También aparece LuchiTruchi#arg con 13 games y 38.5% WR, -10.1pp [GLOBAL.md sec. 11]. Si el objetivo es ranked eficiente, Red Khiedis queda como flag de evitar/reducir; no porque "juegue mal" según data no disponible, sino porque la combinación concreta jugador+partner tiene una tasa de conversión muy inferior.

El patrón por roles aliados favorece junglas carries y mids/AP de control. Maldito Makelele trae MasterYi en 9 de 10 games y 80.0% WR; Reventon95 trae Heimerdinger (21), Veigar (18), Shen (5) y 56.8% WR; Neshy aporta Jinx/Samira/Kaisa con 52.0% WR [GLOBAL.md sec. 11]. Traducido a macro: rendís mejor cuando otro jugador puede cargar daño sostenido o presión de mapa mientras vos jugás una identidad clara, especialmente Top/ADC o picks de utilidad.

### 1.4 Patrones cruzados de fortalezas y debilidades

El patrón transversal más fuerte es el **CS temprano bajo en todos los roles de farm**. Top tiene CS@10 53.26 vs 70.30, -24.2%; Mid 52.04 vs 75.80, -31.3%; ADC 52.73 vs 75.10, -29.8%; Jungla 45.91 vs 68.00, -32.5% [TOP.md sec. 4; MIDDLE.md sec. 4; BOTTOM.md sec. 4; JUNGLE.md sec. 4]. Incluso Support está 12.38 vs 14.40, -14.0%, aunque en support el CS tiene otro significado [UTILITY.md sec. 4]. El mecanismo causal es directo: menos CS@10 baja oro base, retrasa primer componente y te obliga a compensar con peleas; por eso también aparecen gold diff negativos a 15 en Top -151, Mid -302, ADC -125 y Jungla -579 [TOP.md sec. 4; MIDDLE.md sec. 4; BOTTOM.md sec. 4; JUNGLE.md sec. 4].

El segundo patrón es que el **DPM está bajo baseline en todos los roles**, aunque con gravedad distinta. Top es el mejor relativo con 772 vs 830, -7.0%; ADC cae a 743 vs 921, -19.3%; Support 327 vs 409, -20.2%; Mid 657 vs 857, -23.3%; Jungla 447 vs 734, -39.2% [GLOBAL.md sec. 4]. Como el daño bajo aparece junto con CS bajo, el problema no parece solo de positioning en peleas: nace antes, en economía y tempo. La excepción parcial es Top, donde el daño queda cerca del baseline y el WR acompaña.

La **fase de línea** también confirma un patrón: Support gana 38.9% de lanes con lead -183; Top gana 48.9% con lead -104; Mid gana 40.0% con lead -554; ADC gana 42.2% con lead -276; Jungla aparece con 25.0% y lead -980 en la métrica equivalente de early [UTILITY.md sec. 5; TOP.md sec. 5; MIDDLE.md sec. 5; BOTTOM.md sec. 5; JUNGLE.md sec. 5]. Top es el único rol cercano al target 50%, y Jungla es el mayor outlier. El mecanismo es que entrás al mid game con menos oro/exp y necesitás late-game KDA para estabilizar; de hecho tu late global es 6.5/10, bastante mejor que early 4.1/10 y mid 3.8/10 [GLOBAL.md sec. 5].

Vision es mixta. Top supera baseline: 0.85 vs 0.80, +5.8%; Mid también: 0.79 vs 0.75, +5.1% [GLOBAL.md sec. 4]. Pero Support está 1.61 vs 2.60, -38.2%; ADC 0.62 vs 0.68, -8.3%; Jungla 0.87 vs 0.96, -9.7% [GLOBAL.md sec. 4]. La conclusión no es "no wardeás": en solo lanes sí estás sobre baseline. El problema es de roles donde la vision decide objetivos: Support y Jungla, justamente los dos que deberían sostener control de mapa, están bajo baseline.

### 1.5 Recomendación estratégica de priorización

Para ranked, priorizaría **Top como rol primario competitivo** y **ADC como secundario de WR**, no Support. ADC tiene mejor WR bruto, 51.6% en 64 games, pero Top tiene 51.1% en 88 games, mejor DPM relativo al baseline (-7.0% vs -19.3% de ADC) y mejores fases integrales: 4.6/5.1/7.0 contra ADC 4.6/4.4/7.6 [BOTTOM.md sec. 1, sec. 4, sec. 5; TOP.md sec. 1, sec. 4, sec. 5]. Limitaría Support por volumen mal invertido: 108 games, 47.2% WR, Vision/min -38.2% vs baseline y mid game 3.4/10 [UTILITY.md sec. 1, sec. 4, sec. 5]. La palanca humana #1 es Reventon95#LAS para volumen (74 games, 56.8%, +8.2pp) y Maldito Makelele#Fancy para sesiones puntuales si está disponible (10 games, 80.0%, +31.4pp) [GLOBAL.md sec. 11].

## Sección 2 — Support (UTILITY)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia |
|---|---:|---|
| Vision/min + advantage vs sup rival | 2/5 | Vision/min 1.62, diff de vision vs sup rival -0.2, N=108/107; además 1.61 vs baseline 2.60, -38.2% [UTILITY.md sec. 6; UTILITY.md sec. 4] |
| Cobertura de control wards en río/jungla enemiga | 4/5 | Control wards 3.32 por partida y cobertura río/jungla enemiga 52.3%, N=73; sample sólido [UTILITY.md sec. 6] |
| Heal+shield efectivo + saves | 4/5 | Heals+shields 4388 promedio y saves 2.88 por partida, N=108; sin baseline directo, score inferido por volumen [UTILITY.md sec. 6] |
| CC + picks coordinados | 4/5 | CC sobre enemigos 36.27, picks coordinados 14.31, CC+kill con aliado 6.49, N=108 [UTILITY.md sec. 6] |
| Vision Dominance Ratio | 2/5 | VDR 0.80, target reportado >1.3; N=108 [UTILITY.md sec. 6] |
| Roam impact | 1/5 | Takedowns en otras lanes 0.04 por partida, N=108; target del reporte para engage/pick >2 y enchanters 0-1 [UTILITY.md sec. 6] |
| Quest support a tiempo | 2/5 | Quest support a tiempo 0.53, N=108; completa a tiempo solo en 53% [UTILITY.md sec. 6] |

### B) Fortalezas y debilidades específicas

Tu arquetipo medido no es engage puro: es **utility/enchanter-pick centrado en Zilean**. El campeón más jugado es Zilean con 50 games, 48.0% WR, KDA 3.41, DPM 320 y vision 52.2 [UTILITY.md sec. 2]. Milio aparece como enchanter fuerte pero con sample moderado: 9 games, 66.7% WR, KDA 4.18, vision 55.0 [UTILITY.md sec. 2]. Nautilus es el único engage con muestra mínima: 5 games, 60.0% WR, KDA 2.79, vision 61.0; es sample moderado, direccional pero no concluyente [UTILITY.md sec. 2].

Fortaleza 1: **habilidad de enable y peel medible**. Tus heals+shields efectivos son 4388 por partida, saves 2.88 y KDA support 3.14, por encima del KDA global 2.66 [UTILITY.md sec. 6; UTILITY.md sec. 1]. El mecanismo es que Zilean/Milio suben valor por vida extra, velocidad, resurrección o escudos; eso reduce deaths promedio en Support a 5.3 contra 5.7 global y sube assists a 14.9 contra 10.0 global [UTILITY.md sec. 1]. No es casualidad que el KDA suba: el rol te permite participar sin exponerte igual que en Mid/Jungla.

Fortaleza 2: **buena cantidad de interacción cuando decidís pelear**. CC sobre enemigos 36.27, picks coordinados 14.31 y CC+kill con aliado 6.49 son números sólidos por N=108 [UTILITY.md sec. 6]. Eso significa que no estás jugando support "invisible"; sí generás ventanas de catch. El problema no es falta de botones, sino conversión macro: con KP 50.4% vs baseline 54.8%, -8.0%, el CC no está entrando en suficientes kills del equipo [UTILITY.md sec. 4].

Fortaleza 3: **sinergía con carries de reset/entrada**. Como support, tus mejores aliados frecuentes incluyen Samira 5 games, 80.0% WR; Darius 9 games, 77.8%; Sett 9 games, 66.7%; Akshan 9 games, 66.7%; y Kaisa 6 games, 66.7% [UTILITY.md sec. 10]. Samira y Kaisa son samples moderados, pero apuntan a una lectura útil: cuando tu utilidad sostiene un carry que entra y remata, tu aporte de CC/saves se convierte mejor en win condition.

Debilidad 1: **vision insuficiente para el rol**. Vision/min 1.61 vs baseline 2.60, -38.2%, y Vision Dominance Ratio 0.80 vs target >1.3 indican que el mapa se juega con menos información que el support rival [UTILITY.md sec. 4; UTILITY.md sec. 6]. Aunque ponés 3.32 control wards y 12.67 stealth wards por partida, el diff vs sup rival queda -0.2, así que el volumen no se convierte en ventaja relativa [UTILITY.md sec. 6]. El mecanismo probable es timing/ubicación: wards tarde, wards defensivas o resets sin setup previo de objetivo.

Debilidad 2: **roam casi inexistente**. Roam impact es 0.04 takedowns en otras lanes por partida, N=108 [UTILITY.md sec. 6]. Para un Zilean/Milio esto no sería grave si bot se estabilizara, pero tu lane phase win rate es 38.9% y tu lane lead promedio @14 es -183 [UTILITY.md sec. 5]. Es decir: no ganás bot lo suficiente como para justificar quedarte, y tampoco transformás recalls en presión mid/jungla.

Debilidad 3: **mid game flojo por visión y daño**. El mid game support tiene 3.4/10, arrastrado por Vision/min score 2.2 y Damage/min 326 vs target 409, score 3.5 [UTILITY.md sec. 5]. En wins tu vision es 53.71 y en losses 51.60, delta +2.11; existe señal de que wardear mejor acompaña victorias, pero la diferencia no es enorme [UTILITY.md sec. 8]. La prioridad no es solo comprar wards, sino entrar a objetivos con 45-60 segundos de anticipación.

### C) 3 acciones concretas para la próxima semana

1. **Comprá y colocá control ward antes de cada dragón y heraldo, con recall 70-90 segundos antes del spawn.** Tu Vision/min es 1.61 vs baseline 2.60, -38.2%, y tu VDR es 0.80 vs target >1.3 [UTILITY.md sec. 4; UTILITY.md sec. 6]. El objetivo semanal es subir de 1.62 a 1.80 Vision/min, mínimo del rango ideal support citado por el reporte [UTILITY.md sec. 6].

2. **Jugá Zilean/Milio cuando tu carry sea de DPS sostenido o reset, y Nautilus solo con ADC/comp que pueda cerrar CC.** Zilean tiene 50 games y 48.0% WR, Milio 9 games y 66.7%, Nautilus 5 games y 60.0%; Samira contigo como aliado marca 5 games y 80.0%, Kaisa 6 games y 66.7% [UTILITY.md sec. 2; UTILITY.md sec. 10]. No es una regla universal de campeones, es una regla de este reporte: tu CC/enable gana cuando otro remata.

3. **Hacé un roam controlado por cada dos recalls de bot si la wave queda empujada o neutral.** Tu roam impact actual es 0.04, y tu lane phase win rate es 38.9% con lead -183 [UTILITY.md sec. 6; UTILITY.md sec. 5]. La meta no es roamear por roamear: es convertir 1 roam cada 2 recalls en ward profunda, hover mid o defensa de jungla, sin abandonar waves grandes.

### D) Fase fuerte y débil

Tu fase más fuerte como Support es late: 6.6/10, con KDA en partidas largas 3.98 vs target 2.65 y score 8.8 [UTILITY.md sec. 5]. La más débil es mid game: 3.4/10, especialmente por Vision/min 1.62 vs 2.60 y score 2.2 [UTILITY.md sec. 5]. El mecanismo es coherente con tu arquetipo: sobrevivís y escalás utilidad, pero perdés control de objetivos entre 15-25 cuando el soporte debería mandar el mapa.

### E) Mejor duo, matchups y lectura de sample

Mejor ADC/carry aliado medido: **Samira**, 5 games, 80.0% WR, sample moderado; Kaisa también muestra 6 games, 66.7% WR [UTILITY.md sec. 10]. En personas, el mejor duo dentro del reporte support es un empate de WR entre MAXI SALAS 7#LAS2 74 games, 50.0%, Neshy Fox#LAS 30 games, 50.0% y Reventon95#LAS 12 games, 50.0%; ninguno supera fuerte tu media support 47.2% salvo por +2.8pp [UTILITY.md sec. 12; UTILITY.md sec. 1]. Mejor matchup: Zilean vs Thresh, 6 games, 66.7% WR, sample moderado [UTILITY.md sec. 9]. Peor matchup: Zilean vs Alistar y Zilean vs Leona, ambos 3 games y 0.0% WR; sample chico, direccional pero no concluyente [UTILITY.md sec. 9].

### F) Champ pool ideal

Pool medido recomendado: **Milio**, **Nautilus** y **Zilean**. Milio tiene el mejor rendimiento con sample moderado: 9 games, 66.7% WR, KDA 4.18 [UTILITY.md sec. 2]. Nautilus tiene 5 games, 60.0% WR, KDA 2.79, sample moderado y te da engage real [UTILITY.md sec. 2]. Zilean es tu main de volumen, 50 games, 48.0% WR, KDA 3.41; no es el mejor WR, pero es la base más entrenada [UTILITY.md sec. 2]. No hay suficiente data para afirmar que Pyke, Bard, Senna, Lulu u otros no medidos sean mejores.

### G) Conclusión

Support es jugable como rol de utilidad, pero no debería ser tu rol primario de ranked mientras Vision/min 1.61 vs 2.60 y mid game 3.4/10 sigan por debajo del estándar [UTILITY.md sec. 4; UTILITY.md sec. 5].

### Conexión con GLOBAL

Support está -1.4pp en WR frente a global: 47.2% vs 48.6%, pero +0.48 KDA: 3.14 vs 2.66 [UTILITY.md sec. 1]. También está -258 DPM: 333 vs 591, y +19.8 vision promedio: 52.6 vs 32.8 [UTILITY.md sec. 1]. La lectura es que Support mejora tus métricas de supervivencia/participación, pero no tu conversión a victoria. Frente a la distribución global, es el rol más jugado con 108 games, pero queda detrás de ADC 51.6% y Top 51.1% [GLOBAL.md sec. 3]. Por eso no lo llamaría rol natural competitivo: lo llamaría rol confortable de utilidad con déficit de mapa.

## Sección 3 — Top (TOP)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia |
|---|---:|---|
| Gold diff @15 vs rival | 3/5 | -151 gold @15; negativo pero no catastrófico [TOP.md sec. 4] |
| Lane phase WR + lane lead @14 | 4/5 | 48.9% lane win rate, lead -104; cerca del target 50% [TOP.md sec. 5] |
| Solo kills + quick solo kills | 4/5 | 1.75 solo kills por partida, quick solo kills 0.00, N=88 [TOP.md sec. 6] |
| Plates + daño a torres | 5/5 | 7.30 plates por partida y 6149 daño a torres, N=88 [TOP.md sec. 6] |
| Daño mitigado | 4/5 | 32146 daño mitigado promedio, N=88 [TOP.md sec. 6] |
| Splitpush Index | 3/5 | 0.26, N=88; superior a teamfighter puro 0.15-0.25, bajo para splitpushers 0.4-0.6 [TOP.md sec. 6] |
| KDA en partidas largas | 5/5 | Late KDA 2.74 vs target 1.81, score 8.9; late 7.0/10 [TOP.md sec. 5] |

### B) Fortalezas y debilidades específicas

Top es el rol que mejor combina fundamentos con resultado. Tiene 51.1% WR en 88 games, sample sólido, y un perfil de fases 4.6 early / 5.1 mid / 7.0 late [TOP.md sec. 1; TOP.md sec. 5]. El WR queda apenas -0.5pp por debajo de ADC 51.6%, pero con más partidas y un DPM mucho más cercano a baseline: 772 vs 830, -7.0%, contra ADC 743 vs 921, -19.3% [TOP.md sec. 4; BOTTOM.md sec. 4].

Fortaleza 1: **late game top realmente fuerte**. Tu late score es 7.0/10 y tu KDA en partidas largas es 2.74 vs target 1.81, score 8.9 [TOP.md sec. 5]. Además, 74 de 88 partidas llegaron a 25'+, 84.1%, así que no es un dato marginal [TOP.md sec. 5]. El mecanismo es que campeones como Kayle 23 games, 69.6% WR, y Nasus 5 games, 60.0%, convierten partidas largas si no se rompen antes [TOP.md sec. 2].

Fortaleza 2: **presión estructural a torres**. Tenés 7.30 plates por partida y 6149 daño a torres, N=88 [TOP.md sec. 6]. Aunque el Splitpush Index es 0.26, no 0.4-0.6 de splitpusher puro, el daño a estructuras muestra que sí cobrás cuando ganás ventanas [TOP.md sec. 6]. Esto encaja con Kayle/Urgot/Nasus/Malphite: no necesitás ser Fiora de side eterno para convertir, pero sí necesitás farmear y tocar torre cuando el rival rota mal.

Fortaleza 3: **visión y mid game por encima del estándar del rol**. Vision/min 0.85 vs baseline 0.80, +5.8%, y KP 36.6% vs 35.9%, +2.0%, sostienen un mid game de 5.1/10 [TOP.md sec. 4; TOP.md sec. 5]. En wins, tu vision promedio sube a 29.98 contra 24.88 en losses, delta +5.09 [TOP.md sec. 8]. El mecanismo es simple: top con visión no regala side, ve flancos y llega mejor a objetivos.

Debilidad 1: **CS bajo para el rol aunque ganes suficiente**. CS@10 53.26 vs baseline 70.30, -24.2%, y CS@15 84.99 vs 111.00, -23.4% [TOP.md sec. 4]. Lo importante es que, pese a eso, lane phase win rate es 48.9% y lead promedio -104 [TOP.md sec. 5]. Esto sugiere que no perdés lane por duelo puro, sino por eficiencia de last hit/wave management. Estás cerca de empatar oro, pero con menos CS del ideal; eso reduce consistencia y obliga a que el late compense.

Debilidad 2: **muertes tempranas demasiado altas**. El reporte trae 1.24 muertes antes del 10' por partida y target <0.5 [TOP.md sec. 6]. Esa métrica es grave porque Top es un rol de snowball lateral: morir antes de 10 no solo da oro, también rompe wave, placas y tempo de TP. Con campeones de scaling como Kayle, cada muerte pre-10 retrasa el punto en que tu late score 7.0/10 puede importar [TOP.md sec. 2; TOP.md sec. 5].

Debilidad 3: **pool desbalanceado por Gnar/Illaoi**. Gnar es tu top más jugado con 25 games, 40.0% WR, KDA 2.25, DPM 909; hace daño, pero no convierte [TOP.md sec. 2]. Illaoi tiene 5 games, 0.0% WR, KDA 2.10, sample moderado y muy mala señal [TOP.md sec. 2; TOP.md sec. 8]. Kayle, en cambio, tiene 23 games, 69.6% WR [TOP.md sec. 2]. El mecanismo es draft/ejecución: tu mejor top es scaling con win condition clara; tus picks de presión lateral irregular no están cerrando partidas.

### C) 3 acciones concretas para la próxima semana

1. **Priorizar Kayle/Urgot/Malphite y limitar Gnar/Illaoi en ranked.** Kayle tiene 23 games, 69.6% WR; Urgot 5 games, 60.0%; Malphite 5 games, 60.0%; Gnar 25 games, 40.0%; Illaoi 5 games, 0.0% [TOP.md sec. 2]. La acción de draft es de bajo esfuerzo y alto impacto porque cambia el pool hacia campeones que ya convierten.

2. **Entrenar 10 minutos diarios de last hit bajo torre y freeze/slow push para subir CS@10.** Tu CS@10 es 53.26 vs 70.30, -24.2%, y CS@15 84.99 vs 111.00, -23.4% [TOP.md sec. 4]. Meta semanal realista: +5 CS@10, no igualar Diamond de golpe. Con 88 games de sample, el problema es sólido, no ruido.

3. **Regla anti-muerte pre-10: ward 2:45/3:15 y no tradear sin wave favorable antes de primer recall.** Tenés 1.24 muertes antes del 10' por partida, contra target <0.5 [TOP.md sec. 6]. Como tu late KDA es 2.74 vs target 1.81, proteger los primeros 10 minutos aumenta la frecuencia con que llegás a tu fase fuerte [TOP.md sec. 5].

### D) Fase fuerte y débil

Tu fase más fuerte en Top es late: 7.0/10, con KDA largas 2.74 vs 1.81 y score 8.9 [TOP.md sec. 5]. La más débil es early: 4.6/10, arrastrada por CS@10 score 3.2 y gold diff @15 -151 [TOP.md sec. 5]. El mid game está sano en 5.1/10, con KP 36.6% vs target 35.9 y vision/min 0.86 vs 0.80 [TOP.md sec. 5]. Esto confirma que el rol no se cae por macro medio, sino por economía temprana y algunas muertes.

### E) Matchups

El reporte solo trae Gnar vs Sion con 3 games, 33.3% WR, KDA 1.72, DPM 873, CS/m 5.26, y aparece tanto en mejores como peores porque no hay más muestra [TOP.md sec. 9]. Es **sample chico**, direccional pero no concluyente. No hay base estadística suficiente para declarar un ban prioritario de Sion; la adaptación responsable es no blindear Gnar si esperás tanque de escalado y preferir Kayle/Malphite/Nasus según draft, porque esos picks sí tienen señales positivas en tu pool [TOP.md sec. 2].

### F) Conclusión

Top es tu rol primario recomendado: 51.1% WR, DPM solo -7.0% vs baseline, mid 5.1/10 y late 7.0/10, con el plan centrado en CS temprano y reducción de muertes pre-10 [TOP.md sec. 1; TOP.md sec. 4; TOP.md sec. 5; TOP.md sec. 6].

### Conexión con GLOBAL

Top está +2.5pp sobre tu WR global: 51.1% vs 48.6% [TOP.md sec. 1]. En KDA está -0.31: 2.35 vs 2.66, pero eso no invalida el rol porque Top tiene menos assists estructurales que Support y menos KDA inflado por utilidad [TOP.md sec. 1]. En CS/m está +1.59 sobre global: 5.84 vs 4.25, y en DPM +200: 791 vs 591 [TOP.md sec. 1]. Frente al promedio cross-role, Top baja vision promedio 27.5 vs 32.8, -5.3, pero en su baseline específico la Vision/min es positiva: 0.85 vs 0.80, +5.8% [TOP.md sec. 1; TOP.md sec. 4]. La conclusión cruzada es fuerte: Top no lidera KDA, pero sí lidera fit por daño relativo, WR sólido y fases más equilibradas.

## Sección 4 — Mid (MIDDLE)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia |
|---|---:|---|
| Lane phase WR + lead @14 | 2/5 | 40.0% lane win rate y -554 lead @14; serious laning issue según criterio del prompt [MIDDLE.md sec. 5] |
| Max CS lead + max level lead | 4/5 | Max CS lead +19.2 y max level lead +1.2, N=75 [MIDDLE.md sec. 6] |
| Roam impact | 2/5 | 0.29 takedowns en otras lanes, N=75 [MIDDLE.md sec. 6] |
| % daño equipo + DPM | 2/5 | 16.9% daño equipo y 657 DPM vs baseline 857, -23.3% [MIDDLE.md sec. 6; MIDDLE.md sec. 4] |
| Aces antes del 15 | 1/5 | 0.00 por partida, N=75 [MIDDLE.md sec. 6] |
| Solo kills | 3/5 | 0.95 solo kills por partida, N=75 [MIDDLE.md sec. 6] |
| Roam Conversion Rate | 2/5 | WR con >=2 roams 40.0% (n=5) vs 45.8% con 0 roams (n=59), delta -5.76pp [MIDDLE.md sec. 6.1] |
| Synergy WR con Jungla | 4/5 | Con MAXI SALAS 7#LAS2 50.9% (n=55) vs 35.0% sin él (n=20), +15.91pp [MIDDLE.md sec. 6.1] |

### B) Fortalezas y debilidades específicas

Mid muestra talento parcial, pero no consistencia de rol primario. El WR es 46.7% en 75 games, -2.0pp vs global 48.6%, y la fase de línea es 40.0% con lead -554 [MIDDLE.md sec. 1; MIDDLE.md sec. 5]. No es sample chico: 75 games es sólido. La lectura de coach es que tenés campeones y jugadas que funcionan, pero el rol te castiga mucho por tempo, waves y daño efectivo.

Fortaleza 1: **Lissandra y Yone dan una identidad ganadora**. Lissandra tiene 12 games, 66.7% WR, KDA 2.79, DPM 773; Yone 6 games, 66.7% WR, KDA 2.32 [MIDDLE.md sec. 2]. Lissandra además aparece en sinergia de campeón con Mordekaiser: 5 games, 100.0% WR, sample moderado [MIDDLE.md sec. 13]. El mecanismo es claro: Lissandra reduce la carga de lane perfecta porque aporta engage, CC y setup; Yone aporta amenaza lateral y pick, aunque con sample menor.

Fortaleza 2: **capacidad de sacar ventajas máximas aunque el promedio sea malo**. Max CS lead vs rival +19.2 y max level lead +1.2, N=75 [MIDDLE.md sec. 6]. Esto parece contradictorio con CS@10 52.04 vs 75.80, -31.3%, pero no lo es [MIDDLE.md sec. 4]. Significa que en algunas partidas sí encontrás ventanas grandes, pero no las repetís como patrón base. Tenés picos de ventaja, no piso estable.

Fortaleza 3: **con el jungla correcto el rol mejora mucho**. Con MAXI SALAS 7#LAS2 en Jungla tenés 50.9% WR en 55 games; sin él, 35.0% en 20 games, delta +15.91pp [MIDDLE.md sec. 6.1]. Es sample sólido para el grupo con MAXI y sólido mínimo para el grupo sin él. El mecanismo probable es coordinación de presión mid-jungla: si tu early lane es frágil, un jungla conocido corrige timings de hover, skirmish y objetivo.

Debilidad 1: **lane priority insuficiente**. Lane phase win rate 40.0%, lane lead -554, gold diff @15 -302 y CS diff @15 -12 [MIDDLE.md sec. 5; MIDDLE.md sec. 4]. En mid, perder prioridad no solo afecta tu torre: encierra al jungla, cede cangrejos, da primeros movimientos a bot/top y hace que tus roams sean tarde. Esto conecta con tu Roam Conversion Rate negativo.

Debilidad 2: **roameás poco y cuando lo hacés no sube el WR**. Takedowns en otras lanes 0.29 por partida, N=75 [MIDDLE.md sec. 6]. En partidas con >=2 roams, el WR es 40.0% (n=5), contra 45.8% con 0 roams (n=59), delta -5.76pp [MIDDLE.md sec. 6.1]. El sample de roams >=2 es moderado mínimo, pero la dirección coincide con el diagnóstico: roam sin wave/tempo te cuesta recursos y no compensa en mapa.

Debilidad 3: **daño de mid bajo para rol carry**. DPM 657 vs baseline 857, -23.3%, y % de daño del equipo 16.9% [MIDDLE.md sec. 4; MIDDLE.md sec. 6]. En losses hacés 23225 daño a campeones contra 20665 en wins, pero morís 7.42 en losses contra 4.57 en wins [MIDDLE.md sec. 8]. El mecanismo no es "pegás poco siempre"; es que cuando el daño llega en derrotas, llega con exposición y deaths, no como presión eficiente.

### C) 3 acciones concretas para la próxima semana

1. **Bloqueá el pool a Lissandra/Yone y dejá AurelionSol fuera de ranked.** Lissandra tiene 12 games, 66.7% WR; Yone 6 games, 66.7%; AurelionSol 10 games, 20.0% WR y KDA 1.85 [MIDDLE.md sec. 2; MIDDLE.md sec. 8]. AurelionSol puede escalar en teoría, pero en tu data actual no convierte.

2. **No roamees antes del minuto 8 si no tenés wave empujada y visión del jungla rival.** Tu WR con >=2 roams es 40.0% (n=5) vs 45.8% con 0 roams (n=59), delta -5.76pp [MIDDLE.md sec. 6.1]. Tu CS@10 está -31.3% vs baseline, así que cada roam malo agrava el déficit económico [MIDDLE.md sec. 4].

3. **Jugá Mid en duo con MAXI SALAS 7#LAS2 si vas a usarlo en ranked.** Con él tenés 50.9% WR en 55 games; sin él, 35.0% en 20 games [MIDDLE.md sec. 6.1]. La acción es de queue, no mecánica, y ataca el mayor delta positivo medido del rol.

### D) Fase fuerte y débil

La fase más fuerte es late con 5.4/10, sostenida por KDA largas 2.84 vs target 2.27, score 6.9 [MIDDLE.md sec. 5]. La más débil es early con 4.1/10, arrastrada por CS@10 52.04 vs 75.80, score 2.6, y lane lead -554 [MIDDLE.md sec. 5]. Mid game queda en 4.4/10, con vision bien 0.80 vs 0.75, score 5.5, pero damage/min 657 vs 857, score 3.3 [MIDDLE.md sec. 5].

### E) Champ pool ideal

Pool recomendado medido: **Lissandra**, **Yone**, y como tercer pick solo con caveat **Mel/Orianna** según necesidad de práctica, no por WR fuerte. Lissandra tiene 12 games, 66.7% WR [MIDDLE.md sec. 2]. Yone tiene 6 games, 66.7%, sample moderado [MIDDLE.md sec. 2]. Mel tiene 10 games, 40.0%, pero DPM 872 y daño share 20.7%; Orianna tiene 7 games, 42.9% y vision 31.9 [MIDDLE.md sec. 2]. No hay suficiente data para afirmar un tercer mid claramente ganador. Evitaría **AurelionSol** por 10 games, 20.0% WR; **Malzahar** por 4 games, 25.0%, sample chico; y **Vex** por 3 games, 0.0%, sample chico [MIDDLE.md sec. 2].

### F) Conclusión

Mid solo es recomendable como rol condicionado a pool corto y duo jungla: sin eso, 46.7% WR, lane lead -554 y DPM -23.3% vs baseline lo dejan por debajo de Top/ADC [MIDDLE.md sec. 1; MIDDLE.md sec. 4; MIDDLE.md sec. 5].

### Conexión con GLOBAL

Mid está -2.0pp de WR frente a global: 46.7% vs 48.6%, y -0.24 KDA: 2.42 vs 2.66 [MIDDLE.md sec. 1]. En CS/m está +1.09 sobre global, 5.34 vs 4.25, y en DPM +80, 671 vs 591 [MIDDLE.md sec. 1]. Pero esa mejora vs global es engañosa porque el baseline del rol exige más: DPM 657 vs 857 es -23.3%, y CS@10 52.04 vs 75.80 es -31.3% [MIDDLE.md sec. 4]. En otras palabras, Mid se ve mejor que global bruto porque global mezcla Support/Jungla, pero contra mids Diamond estás atrás en economía y daño.

## Sección 5 — ADC (BOTTOM)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia |
|---|---:|---|
| DPM + % daño equipo | 3/5 | 743 DPM, 20.6% daño equipo; DPM 743 vs baseline 921, -19.3% [BOTTOM.md sec. 6; BOTTOM.md sec. 4] |
| Positioning Index | 4/5 | 1.17, target Diamond ~1.0-1.4, N=64 [BOTTOM.md sec. 6] |
| Torres antes de plates / first turret rápida | 1/5 | 0.06 torres antes de plates y first turret rápida 0.00, N=64 [BOTTOM.md sec. 6] |
| Items legendarios completados | 1/5 | 0.11 por partida, N=64; métrica muy baja, sin baseline directo [BOTTOM.md sec. 6] |
| Scaling Score | 3/5 | KDA largas 3.84 (n=34) vs cortas 4.71 (n=13), ratio 0.82; WR largas 61.8% [BOTTOM.md sec. 6.1] |
| Lane phase WR + lead @14 | 3/5 | 42.2% lane WR, lead -276; gold diff @15 -125 [BOTTOM.md sec. 5; BOTTOM.md sec. 4] |
| Muertes antes del 25 | 2/5 | 4.03 por partida, target <3 [BOTTOM.md sec. 6] |
| Synergy WR con Support | 4/5 | BryanKearney#1515: 58.3% (n=24) vs 47.5% sin él (n=40), +10.83pp [BOTTOM.md sec. 6.1] |

### B) Fortalezas y debilidades específicas

ADC tiene el mejor WR bruto de todos tus roles: 51.6% en 64 games, sample sólido [BOTTOM.md sec. 1]. También está +2.9pp sobre global 48.6%, con KDA 2.93 vs global 2.66 y DPM 786 vs global 591 [BOTTOM.md sec. 1]. Sin embargo, el análisis fino muestra por qué no lo pondría automáticamente por encima de Top: su DPM contra baseline Diamond cae -19.3%, su mid game es 4.4/10 y su pressure de plates/turret es muy bajo [BOTTOM.md sec. 4; BOTTOM.md sec. 5; BOTTOM.md sec. 6].

Fortaleza 1: **late ADC muy fuerte en resultado**. Late game es 7.6/10, el mejor late de todos tus roles, con KDA largas 3.73 vs target 2.30 y score 9.7 [BOTTOM.md sec. 5]. Además, en el split de scaling, las partidas largas >=30 tienen 61.8% WR y KDA 3.84 en 34 games, sample sólido [BOTTOM.md sec. 6.1]. Aunque el KDA ratio largas/cortas es 0.82, el WR sube, lo que sugiere que aunque tu KDA baje frente a stomp cortos, sí cerrás mejor cuando el ADC llega a items.

Fortaleza 2: **Positioning Index sano**. Tu Positioning Index es 1.17, dentro del target Diamond ~1.0-1.4 [BOTTOM.md sec. 6]. Esto descarta la lectura simple de "morís por mal posicionamiento todo el tiempo". En realidad, el problema es más temporal: 4.03 muertes antes del 25' contra target <3 te impiden llegar limpio a power spikes [BOTTOM.md sec. 6]. Cuando llegás, el late score 7.6/10 muestra que podés ejecutar.

Fortaleza 3: **picks de DPS/scaling con señales positivas**. Jinx tiene 15 games, 53.3% WR, DPM 868 y 23.1% daño share; Smolder 11 games, 54.5% WR, DPM 1052 y 25.1% daño share [BOTTOM.md sec. 2]. Ambos son sample sólido o sólido mínimo y explican por qué el rol funciona: son campeones que convierten si el juego no explota antes.

Debilidad 1: **early bot no genera suficiente presión de torre**. Torres destruidas antes de caer plates 0.06 y first turret rápida 0.00 son prácticamente nulas en 64 games [BOTTOM.md sec. 6]. Lane phase win rate 42.2% y lane lead -276 confirman que no estás ganando bot de forma consistente [BOTTOM.md sec. 5]. El mecanismo es importante: si jugás Jinx/Smolder, podés aceptar lane neutral; si jugás Jhin/Lucian/Draven, la falta de plates reduce demasiado el valor del pick.

Debilidad 2: **DPM bajo para ADC Diamond aunque el WR acompañe**. DPM 743 vs baseline 921, -19.3%, y % daño equipo 20.6% [BOTTOM.md sec. 4; BOTTOM.md sec. 6]. Como Jinx/Smolder tienen DPM alto individual, la caída puede venir de partidas con Jhin 16 games, 37.5% WR y DPM 626 [BOTTOM.md sec. 2]. Tu ADC no necesita más KDA, necesita más uptime de DPS antes de minuto 25.

Debilidad 3: **Jhin es una fuga de WR**. Es tu ADC más jugado con 16 games, 37.5% WR, KDA 3.11, CS/m 5.05 y DPM 626 [BOTTOM.md sec. 2]. Contrasta con Jinx 15 games, 53.3%, y Smolder 11 games, 54.5% [BOTTOM.md sec. 2]. El mecanismo es de identidad: Jhin aporta pick/utility y cuarto disparo, pero si no dominás lane ni tomás torre temprano, su menor DPS sostenido deja al equipo sin carry consistente.

### C) 3 acciones concretas para la próxima semana

1. **Reducí Jhin y jugá Jinx/Smolder como núcleo de ranked ADC.** Jhin tiene 16 games, 37.5% WR; Jinx 15 games, 53.3%; Smolder 11 games, 54.5% [BOTTOM.md sec. 2]. Es una acción de draft directa: cambia volumen desde un pick negativo hacia dos picks positivos.

2. **Queueá ADC con BryanKearney#1515 como support cuando sea posible.** Con BryanKearney#1515 tenés 58.3% WR en 24 games; sin él, 47.5% en 40 games, delta +10.83pp [BOTTOM.md sec. 6.1]. El reporte también muestra Bryan como persona en ADC con 24 games y 58.3% WR [BOTTOM.md sec. 12].

3. **Plan de lane: no pelear 2v2 extendido sin wave o spike, y priorizar llegar vivo a 25'.** Tenés 4.03 muertes antes del 25' contra target <3, pero late 7.6/10 y WR largas 52.9% en partidas >=25 [BOTTOM.md sec. 6; BOTTOM.md sec. 5]. La métrica a bajar es deaths pre-25, no KDA final.

### D) Fase fuerte y débil

Tu fase fuerte es late: 7.6/10, KDA largas 3.73 vs 2.30 y score 9.7 [BOTTOM.md sec. 5]. La fase débil es mid game: 4.4/10, arrastrada por Damage/min 743 vs 921, score 3.6 [BOTTOM.md sec. 5]. Early también queda en 4.6/10, con CS@10 score 2.8 y lane WR 42.2% [BOTTOM.md sec. 5]. Un ADC con late alto no es red flag; el red flag sería late bajo. Acá el riesgo está en morir o ceder demasiada presión antes de llegar a ese late.

### E) Champ pool ideal

Pool ideal medido: **Smolder**, **Jinx** y **Lucian solo con caveat de sample chico**. Smolder tiene 11 games, 54.5% WR, DPM 1052 y 25.1% daño share [BOTTOM.md sec. 2]. Jinx tiene 15 games, 53.3%, DPM 868 y 23.1% share [BOTTOM.md sec. 2]. Lucian tiene 3 games, 66.7%, KDA 4.45, sample chico; no es concluyente pero puede ser pick de práctica [BOTTOM.md sec. 2]. Sacaría de ranked **Jhin** por 16 games, 37.5%; **Ezreal** por 3 games, 0.0%, sample chico; y **Tristana** por 3 games, 33.3%, sample chico [BOTTOM.md sec. 2].

### F) Mejor duo y matchups

Mejor support humano medido: **BryanKearney#1515**, 24 games, 58.3% WR, +10.83pp vs sin él [BOTTOM.md sec. 6.1]. Como aliado campeón, **Nautilus** destaca con 7 games, 85.7% WR, sample moderado, y Veigar tiene 6 games, 83.3% [BOTTOM.md sec. 10]. Matchups: Jhin vs Draven tiene 3 games, 66.7% WR, sample chico; Jinx vs Xayah tiene 4 games, 50.0%, sample chico [BOTTOM.md sec. 9]. No hay peor matchup concluyente porque los samples son 3-4 games.

### G) Conclusión

ADC es tu mejor secundario y posible rol primario por WR bruto, pero necesita reducir Jhin, muertes pre-25 y falta de presión de plates para superar a Top como opción estable [BOTTOM.md sec. 1; BOTTOM.md sec. 2; BOTTOM.md sec. 6].

### Conexión con GLOBAL

ADC está +2.9pp sobre global en WR: 51.6% vs 48.6%, +0.28 KDA: 2.93 vs 2.66, +1.42 CS/m: 5.67 vs 4.25, y +195 DPM: 786 vs 591 [BOTTOM.md sec. 1]. También tiene -12.8 vision promedio: 20.0 vs 32.8, esperado por rol pero relevante para supervivencia [BOTTOM.md sec. 1]. Contra baseline específico, sin embargo, ADC sigue -29.8% en CS@10 y -19.3% en DPM [BOTTOM.md sec. 4]. La lectura cruzada es positiva pero con deuda técnica: ganás más como ADC que tu media, aunque todavía no pegás/farmeás al estándar del rol.

## Sección 6 — Jungla (JUNGLE)

### A) Score 1-5 por stat core

| Stat core | Score | Evidencia |
|---|---:|---|
| Jungle CS antes del 10 | 2/5 | 49.63 jungle CS antes del 10; en playstyle CS@10 45.91 vs baseline 68.00, -32.5% [JUNGLE.md sec. 6; JUNGLE.md sec. 4] |
| Counter-jungle ratio | 1/5 | 0.10; nota del reporte: <0.3 = pasivo [JUNGLE.md sec. 6] |
| Takedowns en otras lanes early | No medido aún | N=0 [JUNGLE.md sec. 6] |
| Drakes + Heralds + Barones | 3/5 | Drakes 2.16, Heraldos 0.58, Barones 0.41 por partida, N=64 [JUNGLE.md sec. 6] |
| Cobertura wards río/jungla enemiga | 4/5 | 67.7%, N=61, sample sólido [JUNGLE.md sec. 6] |
| Tempo a level 6 | 3/5 | Tiempo a level 6 500s, N=64; nota: Lee Sin Diamond ~450s, Karthus ~510s [JUNGLE.md sec. 6] |
| Soul Rate | 2/5 | Soul 10/51 partidas largas, 20%, WR largas 49% [JUNGLE.md sec. 6.1] |
| Gank-to-Death ratio | No medido aún | N=0 [JUNGLE.md sec. 6] |

### B) Fortalezas y debilidades específicas

Jungla es el rol más preocupante por fundamentos tempranos. Tiene 46.9% WR en 64 games, -1.7pp vs global 48.6%, KDA 2.36 vs global 2.66 y DPM 460 vs global 591 [JUNGLE.md sec. 1]. El early score es 3.0/10 y el mid 3.3/10, ambos los peores del set [JUNGLE.md sec. 5]. El late sube a 5.9/10, pero jungla no puede vivir solo de late porque los objetivos y tempo se deciden antes.

Fortaleza 1: **Dr. Mundo jungla funciona en tu data**. DrMundo tiene 9 games, 77.8% WR, KDA 4.33, CS/m 5.22, DPM 683 y vision 30.7 [JUNGLE.md sec. 2]. Es sample moderado y muy positivo. En un rol donde tu DPM promedio es 460, Mundo aporta daño y aguante suficientes para simplificar peleas [JUNGLE.md sec. 1; JUNGLE.md sec. 2].

Fortaleza 2: **control de zona con wards en río/jungla enemiga**. Cobertura wards en río/jungla enemiga es 67.7%, N=61 [JUNGLE.md sec. 6]. Eso está mejor que tu Vision/min agregada sugiere, porque Vision/min queda 0.87 vs baseline 0.96, -9.7% [JUNGLE.md sec. 4]. El mecanismo es que cuando sí jugás alrededor de entradas al río, tenés información; el problema es convertirla en invades, ganks y objetivos.

Fortaleza 3: **objetivos neutrales aceptables en volumen bruto**. Drakes 2.16, Heraldos 0.58 y Barones 0.41 por partida no son números vacíos [JUNGLE.md sec. 6]. Sin embargo, hay que leerlos junto con Soul Rate 20%, porque tomar algunos drakes no equivale a cerrar alma [JUNGLE.md sec. 6.1]. La fortaleza es que participás en objetivos; la debilidad es el encadenamiento objetivo a objetivo.

Debilidad 1: **pathing/clear inicial muy por debajo**. CS@10 45.91 vs baseline 68.00, -32.5%, y CS@15 71.95 vs 104.30, -31.0% [JUNGLE.md sec. 4]. Jungle CS antes del 10 es 49.63, N=64 [JUNGLE.md sec. 6]. El mecanismo es severo: si salís del primer ciclo abajo, llegás tarde a level 6, perdés prioridad de cangrejo/dragón y quedás forzado a ganks de recuperación.

Debilidad 2: **invade demasiado pasivo**. Counter-jungle ratio 0.10 y CS de jungla enemiga 5.44 vs propia 55.53 [JUNGLE.md sec. 6]. El propio reporte define <0.3 como pasivo [JUNGLE.md sec. 6]. Esto no sería grave si tu gank impact compensara, pero takedowns en otras lanes early y Gank-to-Death ratio tienen N=0, no medido aún [JUNGLE.md sec. 6]. Por lo tanto no hay evidencia de que estés sacrificando camps por presión exitosa.

Debilidad 3: **objetivos no se transforman en soul**. Soul tomada en 10/51 partidas largas, rate 0.20, con WR largas 49% [JUNGLE.md sec. 6.1]. El reporte interpreta explícitamente que cedés la soul y recomienda priorizar ward de drake desde 4:30 y rotar bot [JUNGLE.md sec. 6.1]. El mecanismo es que tomar 2.16 drakes por partida no alcanza si los setups de tercer/cuarto drake llegan sin visión, sin tempo o con lanes perdiendo.

### C) 3 acciones concretas para la próxima semana

1. **Elegí DrMundo como jungla base y dejá Nocturne fuera de ranked.** DrMundo tiene 9 games, 77.8% WR y KDA 4.33; Nocturne tiene 9 games, 33.3% WR y KDA 2.21 [JUNGLE.md sec. 2; JUNGLE.md sec. 8]. Ambos son sample moderado; la diferencia es enorme y accionable.

2. **Practicá clear hasta level 6 con cronómetro: meta inicial 500s -> 470s.** Tu tiempo a level 6 es 500s, mientras la nota del reporte ubica Lee Sin Diamond ~450s y Karthus ~510s [JUNGLE.md sec. 6]. Como tu CS@10 está -32.5%, mejorar el clear ataca el problema más basal [JUNGLE.md sec. 4].

3. **Setup de dragón desde 4:30: reset, control ward/sweeper y ping de bot-mid.** Soul Rate 20% en 51 partidas largas y el propio reporte dice que cedés la soul [JUNGLE.md sec. 6.1]. La meta no es "tomar más drakes" en bruto, porque ya tenés 2.16 por partida; la meta es convertir cadena de drakes en alma [JUNGLE.md sec. 6].

### D) Fase fuerte y débil

La fase más fuerte es late con 5.9/10, KDA largas 3.53 vs target 2.78 y score 7.0 [JUNGLE.md sec. 5]. La más débil es early con 3.0/10, arrastrada por lane phase win rate equivalente 25.0%, lane lead -980 y CS@10 score 2.6 [JUNGLE.md sec. 5]. Mid también está mal con 3.3/10, especialmente Damage/min 446 vs 734, score 2.1 [JUNGLE.md sec. 5]. Jungla no está fallando solo una cosa: falla clear, tempo y conversión de daño.

### E) Champ pool ideal

Pool medido recomendado: **DrMundo** como prioridad, **Darius** solo como pick de práctica por sample chico, y **Skarner** solo como pick de práctica por sample chico. DrMundo tiene 9 games, 77.8% WR, sample moderado [JUNGLE.md sec. 2]. Darius tiene 4 games, 100.0%, y Skarner 3 games, 100.0%; ambos son sample chico y no concluyentes [JUNGLE.md sec. 2]. Evitaría **Nocturne** por 9 games, 33.3%; **LeeSin** por 4 games, 25.0%, sample chico; y **Zac/Jax** por 3 games, 0.0%, sample chico [JUNGLE.md sec. 2].

### F) Conclusión

Jungla debe quedar como rol a evitar en ranked hasta corregir clear y objetivos: 46.9% WR, early 3.0/10, CS@10 -32.5%, DPM -39.2% y Soul Rate 20% son demasiadas fugas simultáneas [JUNGLE.md sec. 1; JUNGLE.md sec. 4; JUNGLE.md sec. 5; JUNGLE.md sec. 6.1].

### Conexión con GLOBAL

Jungla está -1.7pp de WR vs global: 46.9% vs 48.6%, -0.29 KDA: 2.36 vs 2.66, y -131 DPM: 460 vs 591 [JUNGLE.md sec. 1]. En CS/m está +0.49 sobre global, 4.74 vs 4.25, pero esa comparación bruta no sirve para validar el rol porque su baseline específico está muy por encima: CS@10 45.91 vs 68.00, -32.5% [JUNGLE.md sec. 1; JUNGLE.md sec. 4]. Frente al promedio cross-role, Jungla no aporta ni WR ni daño, y frente al baseline de rol queda atrás en clear, KP y DPM [JUNGLE.md sec. 4]. Es el rol con mayor distancia entre responsabilidad macro y ejecución medida.

## Sección 7 — Ranking final + Plan de acción

### 7.1 Ranking de roles (mejor → peor fit estratégico)

| # | Rol | Games | WR | E / M / L | Justificación | Datos clave |
|---:|---|---:|---:|---:|---|---|
| 1 | Top | 88 | 51.1% | 4.6 / 5.1 / 7.0 | Fit más estable: WR alto, daño cercano a baseline y late fuerte. | DPM -7.0% [TOP.md sec. 4], Late 7.0/10 [TOP.md sec. 5], Kayle 69.6% WR [TOP.md sec. 2] |
| 2 | ADC | 64 | 51.6% | 4.6 / 4.4 / 7.6 | Mejor WR bruto, pero depende de reducir Jhin y muertes pre-25. | WR 51.6% [BOTTOM.md sec. 1], Positioning 1.17 [BOTTOM.md sec. 6], Jhin 37.5% WR [BOTTOM.md sec. 2] |
| 3 | Support | 108 | 47.2% | 4.4 / 3.4 / 6.6 | Confort y KDA altos, pero vision/mid game no sostienen ranked. | KDA 3.14 [UTILITY.md sec. 1], Vision/min -38.2% [UTILITY.md sec. 4], VDR 0.80 [UTILITY.md sec. 6] |
| 4 | Mid | 75 | 46.7% | 4.1 / 4.4 / 5.4 | Solo viable con Lissandra/Yone y duo jungla; laning cae demasiado. | Lane lead -554 [MIDDLE.md sec. 5], DPM -23.3% [MIDDLE.md sec. 4], MAXI +15.91pp [MIDDLE.md sec. 6.1] |
| 5 | Jungla | 64 | 46.9% | 3.0 / 3.3 / 5.9 | Demasiada deuda de clear, tempo y soul para ranked consistente. | CS@10 -32.5% [JUNGLE.md sec. 4], Soul Rate 20% [JUNGLE.md sec. 6.1], DPM -39.2% [JUNGLE.md sec. 4] |

Nota de consistencia: ADC tiene +0.5pp WR sobre Top, pero Top queda #1 porque su DPM relativo es mucho mejor (-7.0% vs -19.3%), tiene 24 games más de sample y un mid game más sano (5.1 vs 4.4) [TOP.md sec. 4, sec. 5; BOTTOM.md sec. 4, sec. 5].

### 7.2 Top 5 acciones accionables cross-role

| # | Acción | Por qué (evidencia con número) | Roles afectados | Esfuerzo |
|---:|---|---|---|---|
| 1 | Subí CS@10 con práctica diaria de last hit/clear. | Top -24.2%, Mid -31.3%, ADC -29.8%, Jungla -32.5% vs baseline [GLOBAL.md sec. 4] | Top, Mid, ADC, Jungla | Alto |
| 2 | Mové volumen de Support/Jhin hacia Top Kayle/Urgot/Malphite y ADC Jinx/Smolder. | Support 47.2% con 108 games; Kayle Top 69.6%, Jinx 53.3%, Smolder 54.5%, Jhin 37.5% [UTILITY.md sec. 1; TOP.md sec. 2; BOTTOM.md sec. 2] | Top, ADC, Support | Bajo |
| 3 | Queueá con Reventon95#LAS o Maldito Makelele#Fancy cuando busques LP. | Reventon95 74 games, 56.8%, +8.2pp; Maldito Makelele 10 games, 80.0%, +31.4pp [GLOBAL.md sec. 11] | Todos, especialmente Top/ADC | Bajo |
| 4 | Prepará visión de objetivo 70-90s antes, no al spawn. | Support Vision/min 1.61 vs 2.60, -38.2%; Jungla Soul Rate 20% en 51 largas [UTILITY.md sec. 4; JUNGLE.md sec. 6.1] | Support, Jungla, Top | Medio |
| 5 | Reducí muertes tempranas con reglas por rol. | Top muertes antes del 10: 1.24 vs target <0.5; ADC muertes antes del 25: 4.03 vs target <3 [TOP.md sec. 6; BOTTOM.md sec. 6] | Top, ADC, Mid, Jungla | Alto |

### 7.3 Cierre del coach jefe

Tu rol primario recomendado para ranked es **Top**: aunque ADC tiene 51.6% WR, Top combina 51.1% WR, 88 games, DPM solo -7.0% vs baseline y late 7.0/10, por lo que la ganancia esperada frente a seguir jugando Support es +3.9pp WR, o +4.21 victorias cada 108 games como proxy de LP [TOP.md sec. 1, sec. 4, sec. 5; UTILITY.md sec. 1]. El secundario sano es **ADC**, especialmente Jinx/Smolder y con BryanKearney#1515 como support: 58.3% WR juntos vs 47.5% sin él [BOTTOM.md sec. 6.1]. Evitá Jungla y Mid en ranked salvo plan específico: Jungla 46.9% con early 3.0/10, Mid 46.7% con lane lead -554 [JUNGLE.md sec. 1, sec. 5; MIDDLE.md sec. 1, sec. 5]. La palanca humana #1 de volumen es Reventon95#LAS, 74 games y 56.8% WR vs 48.6% global [GLOBAL.md sec. 11; GLOBAL.md sec. 1]. Compromiso semanal: subir CS@10; el próximo corte debe medir últimas 20 partidas y buscar +5 CS@10 en Top/ADC.
