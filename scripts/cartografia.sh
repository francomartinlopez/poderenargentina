#!/usr/bin/env bash
# Regenera la cartografía desde el IGN (vía Georef, datos.gob.ar). Solo hace falta si el IGN cambia límites.
# Requiere: npm i -g mapshaper
set -euo pipefail
cd "$(dirname "$0")/.."
T=$(mktemp -d)
curl -sL -o $T/provincias.geojson https://infra.datos.gob.ar/georef/provincias.geojson
curl -sL -o $T/departamentos.geojson https://infra.datos.gob.ar/georef/departamentos.geojson
# Continente, Tierra del Fuego y Malvinas (las Georgias, las Sandwich del Sur y la Antártida quedan afuera del mapa principal).
mapshaper $T/provincias.geojson -clip bbox=-74.5,-56,-53,-21 -simplify interval=350 keep-shapes -filter-fields id,nombre \
  -rename-layers provincias -o format=topojson quantization=1e5 data/provincias.json
# Sector antártico para el recuadro (la app corrige el sentido de los anillos si hace falta).
mapshaper $T/provincias.geojson -filter "id=='94'" -clip bbox=-74,-90,-25,-60 -simplify 2% keep-shapes -filter-fields id \
  -o format=geojson precision=0.01 data/antartida.json
# Departamentos, uno por provincia (sin el departamento Antártida Argentina, 94028).
python3 - "$T" <<'PY'
import json, subprocess, sys
T = sys.argv[1]
d = json.load(open(f"{T}/departamentos.geojson"))
for pid in sorted({f["properties"]["provincia"]["id"] for f in d["features"]}):
    fc = dict(type="FeatureCollection", features=[dict(type="Feature", geometry=f["geometry"],
        properties=dict(id=f["properties"]["id"], nombre=f["properties"]["nombre"], cat=f["properties"]["categoria"]))
        for f in d["features"] if f["properties"]["provincia"]["id"] == pid and f["properties"]["id"] != "94028"])
    json.dump(fc, open(f"{T}/d{pid}.geojson", "w"))
    pct = "8%" if pid == "06" else "12%"
    subprocess.run(["mapshaper", f"{T}/d{pid}.geojson", "-clip", "bbox=-74.5,-56,-53,-21", "-simplify", pct, "keep-shapes",
                    "-rename-layers", "dep", "-o", "format=topojson", "quantization=1e5", f"data/dep/{pid}.json"], check=True)
PY
echo "Cartografía regenerada."
