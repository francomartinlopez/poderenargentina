#!/usr/bin/env python3
"""Busca una localidad en Georef y devuelve la línea lista para pegar en fuente/ciudades.py.
Uso: python3 scripts/ubicar_ciudad.py "General Deheza" "Córdoba"
"""
import json, sys, urllib.parse, urllib.request
nombre, provincia = sys.argv[1], sys.argv[2]
for exacto in ("true", "false"):
    q = urllib.parse.urlencode(dict(nombre=nombre, provincia=provincia, max=10, exacto=exacto))
    L = json.load(urllib.request.urlopen("https://apis.datos.gob.ar/georef/api/localidades?" + q, timeout=30))["localidades"]
    if L:
        break
if not L:
    sys.exit("No encontrada en Georef: cargar las coordenadas a mano con fuente.")
for x in L:
    c = x["centroide"]
    print(f'    ({nombre!r}, {x["provincia"]["id"]!r}, {x["departamento"]["id"]!r}, {round(c["lon"], 4)}, {round(c["lat"], 4)}, "MOTIVOS", "POR QUÉ", "FUENTE", None),'
          f'  # {x["nombre"]} · {x["departamento"]["nombre"]} · {x["categoria"]}')
