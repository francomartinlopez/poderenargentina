#!/usr/bin/env python3
"""Descarga la población por departamento del Censo 2022 (INDEC, resultados definitivos, cuadro 2.x de cada provincia)
y escribe fuente/poblacion.py. No editar fuente/poblacion.py a mano.
Uso: python3 scripts/importar_censo.py
"""
import io, os, re, urllib.request
import openpyxl
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# número de cuadro INDEC y nombre del archivo, en el orden del INDEC
ARCH = ["caba", "bsas", "catamarca", "chaco", "chubut", "cordoba", "corrientes", "entrerios", "formosa", "jujuy", "lapampa",
        "larioja", "mendoza", "misiones", "neuquen", "rionegro", "salta", "sanjuan", "sanluis", "santacruz", "santafe",
        "santiago", "tdf", "tucuman"]
URL = "https://www.indec.gob.ar/ftp/cuadros/poblacion/c2022_{}_est_c2_{}.xlsx"
dep = {}
for n, nom in enumerate(ARCH, 1):
    data = urllib.request.urlopen(URL.format(nom, n), timeout=60).read()
    ws = openpyxl.load_workbook(io.BytesIO(data), read_only=True, data_only=True).worksheets[-1]
    for r in ws.iter_rows(values_only=True):
        if not r or len(r) < 4 or not isinstance(r[3], (int, float)):
            continue
        c = str(r[0]).strip() if r[0] is not None else ""
        if re.fullmatch(r"\d{4,5}", c):
            dep[c.zfill(5)] = int(r[3])
# id de provincia a partir de los códigos de departamento
tot_id = {}
for k, v in dep.items():
    tot_id[k[:2]] = tot_id.get(k[:2], 0) + v
with open(os.path.join(RAIZ, "fuente", "poblacion.py"), "w") as f:
    f.write("# Generado por scripts/importar_censo.py. No editar a mano.\n")
    f.write("# Fuente: INDEC, Censo Nacional de Población, Hogares y Viviendas 2022, resultados definitivos (cuadro 2 de cada provincia).\n")
    f.write("FUENTE = \"https://www.indec.gob.ar/ftp/cuadros/poblacion/c2022_cordoba_est_c2_6.xlsx\"\n")
    f.write("PROVINCIA = " + repr(dict(sorted(tot_id.items()))) + "\n")
    f.write("DEPARTAMENTO = " + repr(dict(sorted(dep.items()))) + "\n")
print(len(tot_id), "provincias,", len(dep), "departamentos,", sum(tot_id.values()), "habitantes")
