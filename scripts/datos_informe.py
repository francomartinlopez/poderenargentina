"""Arma datos-informe.json (raíz del sitio) para la web de informes de Plexum.

Especificación: «Datos que cada web publica para la web de informes de Plexum», versión 1.2 (25/11/2026),
parte común y apartado 4 (Mapa del Poder Argentino, eje «Política nacional»).
Lo llama scripts/generar_datos.py con los mismos datos de data/territorio.json; no cambia nada visible del sitio.

- novedades «norma»: las normas de fuente/normas.py con fecha en los últimos 90 días.
- novedades «otro»: cambios de autoridades de fuente/normas.py (ASUNCIONES) en los últimos 90 días.
- agenda: elecciones provinciales confirmadas de fuente/elecciones.py en los próximos 60 días. El sitio no muestra
  sesiones del Congreso, legislaturas ni concejos, así que no se publican.
- indicadores y faltantes: el apartado 4 no pide indicadores; van vacíos.
"""
import datetime as dt
import json
import os
import re

WEB = "Mapa del Poder Argentino"
EJE = "Política nacional"
SITIO = "https://francomartinlopez.github.io/poderenargentina/"
RUBROS = {"ind": "Industria", "agro": "Agro", "min": "Minería", "ene": "Energía", "cons": "Construcción", "com": "Comercio y servicios"}
PROV_NOMBRE = {"02": "CABA", "94": "Tierra del Fuego"}  # el resto coincide con la lista cerrada
TZ = dt.timezone(dt.timedelta(hours=-3))


def _alcance(nivel, provincia="", localidad=""):
    return dict(nivel=nivel, provincia=provincia, localidad=localidad, pais="Argentina")


def _rubros(lista):
    # Lista vacía = todos los rubros.
    return [] if set(lista) >= set(RUBROS) else [RUBROS[r] for r in lista]


def _depnom(raiz, cod):
    with open(os.path.join(raiz, "data", "dep", cod[:2] + ".json"), encoding="utf-8") as fh:
        topo = json.load(fh)
    for o in topo["objects"].values():
        for g in o["geometries"]:
            if g.get("properties", {}).get("id") == cod:
                return g["properties"]["nombre"]
    raise KeyError(f"Departamento sin nombre: {cod}")


def escribir(T, raiz, hoy=None):
    ahora = dt.datetime.now(TZ).replace(microsecond=0)
    hoy = hoy or ahora.date()
    desde, hasta = hoy - dt.timedelta(days=90), hoy + dt.timedelta(days=60)
    prov = {p["id"]: PROV_NOMBRE.get(p["id"], p["n"]) for p in T["provincias"]}
    ciu = {c["s"]: c for c in T["ciudades"]}

    def lugar(l):
        if l == "AR":
            return "Nación", _alcance("nacional")
        if l.startswith("c:"):
            c = ciu[l[2:]]
            return c["n"], _alcance("localidad", prov[c["prov"]], c["n"])
        if l.startswith("d:"):
            cod = l[2:]
            d = T["deps"].get(cod)
            nom = d["n"] if d else _depnom(raiz, cod)
            return nom, _alcance("localidad", prov[cod[:2]], nom)
        return prov[l], _alcance("provincia", prov[l])

    def fecha(f):
        # «AAAA-MM» cuenta desde el último día del mes; nunca se inventa el día.
        if re.fullmatch(r"\d{4}-\d{2}", f):
            y, m = map(int, f.split("-"))
            return (dt.date(y + m // 12, m % 12 + 1, 1) - dt.timedelta(days=1))
        return dt.date.fromisoformat(f)

    novedades = []
    for n in T["normas"]:
        if not (desde <= fecha(n["f"]) <= hoy):
            continue
        nom, alc = lugar(n["l"])
        if n["em"].startswith("Concejo Deliberante de ") and alc["nivel"] == "localidad":
            nom = alc["localidad"] = n["em"][len("Concejo Deliberante de "):]  # el municipio que dictó la norma
        num = n["num"].replace(" (sin número publicado)", "")
        res = f'{n["x"].rstrip(".")}. Emisor: {n["em"]}.'
        if "(sin número publicado)" in n["num"]:
            res += " Sin número publicado todavía."
        assert len(res.split()) <= 60, f"Resumen largo: {n['id']}"
        novedades.append(dict(id=f'{n["f"]}-{n["id"]}', fecha_dato=n["f"], titulo=f"{nom}: {num}", resumen=res, tipo="norma",
                              eje=EJE, alcance=alc, rubros=_rubros(n["r"]), subrubros=[], exposicion=[], url=n["u"]))
    for pid, lista in T["funcionarios"].items():
        for f in lista:
            if "d" not in f or not (desde <= dt.date.fromisoformat(f["d"]) <= hoy):
                continue
            quien = f["n"] or f["c"]
            cargo = f["c"][0].lower() + f["c"][1:] if f["n"] else "responsable del área"
            res = f'{quien} asumió como {cargo} de {prov[pid]}. {f.get("dn", "")}'.strip()
            novedades.append(dict(id=f'{f["d"]}-autoridad-{pid}-{f["a"].lower()}', fecha_dato=f["d"],
                                  titulo=f'{prov[pid]}: cambio en {f["a"]}', resumen=res, tipo="otro", eje=EJE,
                                  alcance=_alcance("provincia", prov[pid]), rubros=[], subrubros=[], exposicion=[], url=f["u"]))
    novedades.sort(key=lambda z: (z["fecha_dato"], z["id"]), reverse=True)

    agenda = []
    for pid, e in sorted(T["elecciones"]["prov"].items()):
        if e.get("f") and hoy <= dt.date.fromisoformat(e["f"]) <= hasta:
            agenda.append(dict(fecha=e["f"], evento=f"Elecciones provinciales en {prov[pid]}", eje=EJE,
                               alcance=_alcance("provincia", prov[pid]), rubros=[], url=e["u"]))
    agenda.sort(key=lambda z: z["fecha"])

    out = dict(web=WEB, version="1.0", generado=ahora.isoformat(), indicadores=[], novedades=novedades, agenda=agenda, faltantes=[])
    with open(os.path.join(raiz, "datos-informe.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print(f"datos-informe.json: {len(novedades)} novedades y {len(agenda)} eventos de agenda.")
