# Cambios

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
