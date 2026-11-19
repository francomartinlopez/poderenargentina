#!/usr/bin/env python3
"""Genera data/territorio.json a partir de fuente/*.py y de la cartografía de data/.

Uso: python3 scripts/generar_datos.py
Después: node scripts/validate.js
"""
import json, os, re, sys, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "fuente"))
from provincias import PROVINCIAS  # noqa: E402
from ciudades import CIUDADES  # noqa: E402

# Corte trimestral: subir en cada actualización (CORTE = hoy, PROXIMA = dentro de tres meses).
CORTE = "2026-11-19"
PROXIMA = "2027-02-23"


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def main():
    topo = json.load(open(os.path.join(RAIZ, "data", "provincias.json")))
    ign = {g["properties"]["id"]: g["properties"]["nombre"] for g in topo["objects"]["provincias"]["geometries"]}
    ndep = {}
    for pid in ign:
        d = json.load(open(os.path.join(RAIZ, "data", "dep", pid + ".json")))
        ndep[pid] = len(d["objects"]["dep"]["geometries"])

    ciudades, vistos = [], set()
    for n, prov, dep, lon, lat, mot, nota, fuente, pob in CIUDADES:
        s = slug(n)
        if s in vistos:
            sys.exit(f"Ciudad repetida: {n}")
        vistos.add(s)
        c = dict(n=n, s=s, prov=prov, dep=dep, lon=lon, lat=lat, mot=mot.split(), nota=nota)
        if fuente:
            c["fuente"] = fuente
        if pob:
            c["pob"] = pob
        ciudades.append(c)

    cap = {c["prov"]: c["s"] for c in ciudades if "cap" in c["mot"]}
    provincias = []
    for pid, (s, corto, gob, par, desde) in PROVINCIAS.items():
        provincias.append(dict(
            id=pid, s=s, n=ign[pid], c=corto, gob=gob, par=par, desde=desde,
            cat="Ciudad Autónoma" if pid == "02" else "Provincia",
            ndep=ndep[pid], cap=cap.get(pid),
        ))
    provincias.sort(key=lambda p: p["n"])

    out = dict(corte=CORTE, proxima=PROXIMA, provincias=provincias, ciudades=ciudades)
    with open(os.path.join(RAIZ, "data", "territorio.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print(f"data/territorio.json: {len(provincias)} provincias, {sum(ndep.values())} departamentos, {len(ciudades)} ciudades. Corte {CORTE}.")


if __name__ == "__main__":
    main()
