# Cambios

## 2026-11-19 (d) · Paso 3: actores núcleo nacionales

- 42 actores nacionales (`fuente/actores.py`) medidos en los 21 ejes con la fórmula del mapa global (`fuente/ejes.py`, `scripts/puntaje.py`): conducción del Ejecutivo, Economía, BCRA, ARCA, Banco Nación, SIDE, Fuerzas Armadas, fuerzas federales, Corte, Comodoro Py, Congreso, los cuatro gobiernos provinciales de mayor peso nacional, partidos, Cristina Fernández de Kirchner, grandes grupos, cámaras empresarias, CGT, Camioneros, UTEP, Iglesia, AFA y Los Monos. Como en el mapa global, el Estado no figura como bloque formal sino a través de quienes ejercen el poder.
- Cada actor con ficha (qué es, quién manda), fuentes, puntaje de poder, poder oculto, autonomía, alcance y dependencias; acción fuera de la ley solo con condena judicial (causa Vialidad, Los Monos).
- 48 relaciones con fuente, incluidas las que cruzan con actores del mapa global (FMI, Tesoro de EE.UU., Banco Popular de China, Casa Blanca, CIA, Santa Sede, FIFA).
- Sitio: página Actores con ranking, filtro por tipo, red de relaciones y método; ficha de cada actor (`#a-<id>`); capa Actores en el mapa; actores con sede en las fichas de provincia y ciudad. Validador ampliado. Vista previa para redes regenerada.
- Cabos sueltos: fuente para las 67 ciudades que no la tenían; Junín y Goya vuelven por decisión de Franco (excepción al umbral de 100.000 habitantes, registrada en `fuente/ciudades.py`); población de Timbúes (5.406), La Quiaca (22.078), Salvador Mazza (2010) y Jáchal (2010).

## 2026-11-19 (c) · Población de ciudades y estación china

- Población de cada ciudad (`fuente/poblacion_ciudades.py`): la del aglomerado urbano del INDEC cuando la ciudad forma parte de uno (Censo 2022, con el dato de 2010), y la de la localidad sola para las ciudades chicas, con el año del dato (2022, 2010, 2001 o estimación). Cuando un aglomerado une varias localidades (Neuquén-Plottier-Cipolletti, Gran Rosario, Santiago del Estero-La Banda y otros), la cifra es la del conjunto. Faltan Timbúes y Salvador Mazza.
- El criterio «más de 100.000 habitantes» se mide sobre el aglomerado y el validador lo controla. Siete ciudades no llegaban: Puerto Madryn, Gualeguaychú, Venado Tuerto, Orán, Río Grande, Oberá y Sáenz Peña siguen por otro motivo (empresa o cluster, puerto o frontera); Junín y Goya, que solo entraban por población, salen del mapa. Quedan 97 ciudades.
- Estación de Espacio Lejano de China: ubicada en la Pampa de Pilmatué, paraje Quintuco, al norte de Bajada del Agrio (departamento Loncopué, −38,1914; −70,1495). Reemplaza el punto provisorio en Bajada del Agrio.

## 2026-11-19 (b) · Paso 2: las 24 provincias

- Población del Censo 2022 (INDEC, resultados definitivos) por provincia y por departamento: 45.892.285 habitantes. `fuente/poblacion.py` se genera con `scripts/importar_censo.py`.
- Economía y recursos (`fuente/economia.py`): exportaciones, destinos y rubro principal de cada provincia (INDEC, origen provincial de las exportaciones, primer semestre de 2026) y recursos propios sobre el total de ingresos (ASAP, 2025; La Pampa sin datos).
- Quién manda de verdad y alineamiento con la Nación (`fuente/alineamiento.py`): 5 aliados, 10 dialoguistas, 3 independientes y 6 opositores al 19/11/2026, con el grupo que gobierna, desde cuándo y fuentes. Misiones: ruptura de Passalacqua con Carlos Rovira en 2026.
- Influencias mundiales (`fuente/influencias.py`): 11 potencias en cinco canales, con fuente. El comercio se calcula con los destinos de exportación; inversión, deuda, presencia e influencia política se cargan dato por dato. Potencia dominante por provincia, con empates marcados.
- Mapa: capas de alineamiento, influencias (dominante o una potencia) y economía (exportaciones o recursos propios). Fichas de provincia, departamento y ciudad con población; tabla de Provincias ampliada.
- Validador: controla población, alineamiento, exportaciones y fuentes de cada influencia.

## 2026-11-19 · Paso 1: esqueleto

- Mapa de las 24 jurisdicciones con la cartografía del IGN (vía Georef): zoom de país a provincia, departamento (528 departamentos, partidos y comunas) y ciudad, con rutas propias (`#prov-`, `#d-`, `#c-`). Malvinas en el mapa principal y la Antártida Argentina en un recuadro.
- 99 ciudades ubicadas con Georef, cada una con su motivo: capitales, ciudades grandes, sedes de empresas y clusters aunque sean chicas (General Deheza, Armstrong, Las Parejas, Arroyito, Sunchales y otras), puertos, energía, minería, frontera y defensa. Filtrables por motivo en el mapa.
- Gobernadores al 19 de noviembre de 2026 (Corrientes: Juan Pablo Valdés y Santiago del Estero: Elías Suárez, desde diciembre de 2025).
- Escritorio: panel lateral de la misma altura que el mapa con lo principal y los bloques de detalle debajo, a lo ancho.
- Símbolo propio (silueta de la Argentina dentro del círculo del mapa global) e imagen de vista previa para WhatsApp y X.
- Pendientes: población del Censo 2022 de las ciudades grandes, fuentes de cada ciudad y ubicación exacta de la estación espacial china de Neuquén.
