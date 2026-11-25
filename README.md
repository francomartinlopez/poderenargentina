# El mapa del poder argentino

**El país real, sin máscaras.** Quién tiene el poder real en la Argentina y quién solo lo aparenta, provincia por provincia, departamento por departamento y ciudad por ciudad: sus actores, quién manda de verdad y qué potencias extranjeras pesan en cada territorio.

Proyecto hermano de [El mapa del poder global](https://francomartinlopez.github.io/podermundial/), con la misma base técnica y el mismo método. Sitio estático (HTML, CSS y JavaScript, sin dependencias salvo d3-geo, d3-array y topojson-client). Se publica con GitHub Pages desde la rama `main`: https://francomartinlopez.github.io/poderenargentina/

## Secciones
- **Mapa:** las 24 jurisdicciones con zoom a departamentos (partidos y comunas) y ciudades. Rutas: `#prov-<provincia>`, `#d-<id IGN del departamento>`, `#c-<ciudad>`.
- **Provincias:** quién gobierna cada una.
- **Ciudades:** las ciudades del mapa con el motivo por el que entran.
- **Plan:** qué está hecho y qué falta.

## Estado
Los cinco pasos están hechos: cartografía, ciudades, gobernadores, fichas de las 24 provincias (población, economía, quién manda, alineamiento e influencias mundiales) y los actores núcleo nacionales medidos en 21 ejes, con sus relaciones; fichas de ciudades con intendente, influencias propias y conflictos; actores provinciales y municipales (65 en total), puntos de fricción y zonas liberadas documentadas. Se actualiza cada trimestre.

## Datos
- `fuente/provincias.py`: gobernadores (fuente editorial).
- `fuente/ciudades.py`: ciudades, coordenadas (Georef), motivos, fuentes y población.
- `fuente/poblacion.py`: Censo 2022 por provincia y departamento (generado por `scripts/importar_censo.py`).
- `fuente/economia.py`: exportaciones, destinos y rubro (INDEC) y recursos propios (ASAP).
- `fuente/alineamiento.py`: quién manda y alineamiento con la Nación, con fuentes.
- `fuente/elecciones.py`: calendario de las elecciones de 2027 por provincia (página «Elecciones»).
- `fuente/normas.py`: normas que afectan a las empresas en Nación, provincias y localidades (página «Normas», con filtros por lugar y rubro) y los funcionarios que regulan cada rubro por provincia.
- `fuente/influencias.py`: influencias de 12 potencias en cinco canales, con fuentes.
- `fuente/actores_mas.py`, `fuente/actores_mas2.py`, `fuente/actores_mas3.py`, `fuente/actores_mas4.py`, `fuente/actores_mas5.py`, `fuente/actores_mas6.py` y `fuente/actores_mas7.py`; `fuente/presencia.py`: provincias donde opera cada actor fuera de su sede: actores por categoría (políticos, empresas, familias, sindicatos, bandas y barras con condena, Justicia, fuerzas armadas y de seguridad, inteligencia, religiosos, ONG, medios, clubes, embajadas, bancos, cámaras, intendentes del conurbano); 362 en total, con 543 relaciones con fuente. Un actor puede tener sede en un partido («dep:<código>»).
- `fuente/departamentos.py`: fichas de los partidos y departamentos relevantes.
- `fuente/actores.py`: actores núcleo, fichas y relaciones; `fuente/ejes.py`: ejes, pesos y categorías; `scripts/puntaje.py`: fórmula del puntaje.
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
