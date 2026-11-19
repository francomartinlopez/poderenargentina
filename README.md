# El mapa del poder argentino

**El país real, sin máscaras.** Quién tiene el poder real en la Argentina y quién solo lo aparenta, provincia por provincia, departamento por departamento y ciudad por ciudad: sus actores, quién manda de verdad y qué potencias extranjeras pesan en cada territorio.

Proyecto hermano de [El mapa del poder global](https://francomartinlopez.github.io/podermundial/), con la misma base técnica y el mismo método. Sitio estático (HTML, CSS y JavaScript, sin dependencias salvo d3-geo, d3-array y topojson-client). Se publica con GitHub Pages desde la rama `main`: https://francomartinlopez.github.io/poderenargentina/

## Secciones
- **Mapa:** las 24 jurisdicciones con zoom a departamentos (partidos y comunas) y ciudades. Rutas: `#prov-<provincia>`, `#d-<id IGN del departamento>`, `#c-<ciudad>`.
- **Provincias:** quién gobierna cada una.
- **Ciudades:** las ciudades del mapa con el motivo por el que entran.
- **Plan:** qué está hecho y qué falta.

## Estado
Paso 1 de 5 (esqueleto): cartografía, navegación, ciudades y gobernadores. Próximos pasos: fichas de las 24 provincias con alineamiento, recursos e influencias mundiales; actores núcleo nacionales; fichas de ciudades; actores provinciales y municipales y puntos de fricción.

## Datos
- `fuente/provincias.py`: gobernadores (fuente editorial).
- `fuente/ciudades.py`: ciudades, coordenadas (Georef), motivos, fuentes y población.
- `fuente/influencias.py` y `fuente/actores.py`: estructura de los pasos 2 y 3, todavía sin cargar.
- `scripts/generar_datos.py`: genera `data/territorio.json`.
- `scripts/validate.js`: controla provincias, ciudades, departamentos y el vencimiento del corte.
- `scripts/cartografia.sh`: regenera `data/provincias.json`, `data/antartida.json` y `data/dep/*.json` desde el IGN (vía Georef, datos.gob.ar).
- `scripts/ubicar_ciudad.py`: ubica una localidad en Georef para sumarla a `fuente/ciudades.py`.
- `vendor/`: d3-array, d3-geo y topojson-client (licencia ISC).

## Actualización
El sitio se revisa cada tres meses (23 de febrero, mayo, agosto y noviembre), una semana después del mapa global. Cada corte queda etiquetado en git y registrado en `CHANGELOG.md`.

```
python3 scripts/generar_datos.py
node scripts/validate.js
```
