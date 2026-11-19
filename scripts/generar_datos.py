#!/usr/bin/env python3
"""Genera data/territorio.json a partir de fuente/*.py y de la cartografía de data/.

Uso: python3 scripts/generar_datos.py
Después: node scripts/validate.js
"""
import json, os, re, sys, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "fuente"))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
from provincias import PROVINCIAS  # noqa: E402
from ciudades import CIUDADES, EXCEPCIONES  # noqa: E402
import poblacion, poblacion_ciudades, economia, alineamiento, influencias, ciudades_fichas  # noqa: E402

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
        if n in EXCEPCIONES:
            c["exc"] = EXCEPCIONES[n]
        pc = poblacion_ciudades.CIUDADES.get(n, {})
        if pob or pc.get("pob"):
            c["pob"] = pob or pc["pob"]
            c["anio"] = pc.get("anio", 2022)
            if pc.get("estimada"):
                c["est"] = True
            if pc.get("fuente_pob"):
                c["fpob"] = pc["fuente_pob"]
            if pc.get("proy"):
                c.update(proy=pc["proy"], proya=pc["proy_anio"], proyn=pc["proy_nota"], fproy=pc["fuente_proy"])
        if pc.get("aglo"):
            c.update(ag=pc["aglo"], agpob=pc["aglo_pob"], agpob10=pc.get("aglo_pob10"), fag=pc.get("fuente_aglo"))
        ciudades.append(c)

    cap = {c["prov"]: c["s"] for c in ciudades if "cap" in c["mot"]}

    # Influencias: comercio calculado desde las exportaciones; el resto, de fuente/influencias.py.
    POT, CAN = influencias.POTENCIAS, list(influencias.CANALES)
    inf = {}
    for t, pot, can, n, txt, url in influencias.INFLUENCIAS:
        assert pot in POT and can in CAN and can != "com" and 0 <= n <= 3 and url.startswith("http"), (t, pot, can)
        inf.setdefault(t, []).append(dict(p=pot, c=can, n=n, x=txt, u=url))
    for pid, e in economia.PROVINCIAS.items():
        agg = {}
        for nombre, monto in e["dest"]:
            pot = influencias.APROX_COMERCIO.get(nombre)
            if pot:
                agg.setdefault(pot, []).append((nombre, monto))
        for pot, items in agg.items():
            propio = [m for x, m in items if x == pot]
            monto = propio[0] if propio else max(m for _, m in items)  # si el INDEC da el país, vale el país y no el bloque
            items = [(x, m) for x, m in items if x == pot] or items
            sh = monto / e["exp"]
            n = 3 if sh >= .40 else 2 if sh >= .20 else 1 if sh >= .08 else 0
            if n:
                nombres = " y ".join(dict.fromkeys(x for x, _ in items))
                aprox = "" if pot in [x for x, _ in items] or (pot == "Unión Europea") else f" ({nombres}, tomado como {pot})"
                inf.setdefault(pid, []).append(dict(p=pot, c="com", n=n, u=economia.FUENTE_EXPORTACIONES,
                    x=f"{round(sh * 100)}% de las exportaciones de la provincia en el {economia.PERIODO_EXPORTACIONES}{aprox}."))

    def dominante(lista):
        tot = {}
        for i in lista:
            tot[i["p"]] = tot.get(i["p"], 0) + i["n"]
        if not tot:
            return None, {}
        mx = max(tot.values())
        top = [p for p in POT if tot.get(p) == mx]
        return (top[0] if len(top) == 1 else None), tot
    provincias = []
    for pid, (s, corto, gob, par, desde) in PROVINCIAS.items():
        provincias.append(dict(
            id=pid, s=s, n=ign[pid], c=corto, gob=gob, par=par, desde=desde,
            cat="Ciudad Autónoma" if pid == "02" else "Provincia",
            ndep=ndep[pid], cap=cap.get(pid), pob=poblacion.PROVINCIA[pid],
            eco=economia.PROVINCIAS[pid], ali=alineamiento.PROVINCIAS[pid],
            inf=sorted(inf.get(pid, []), key=lambda i: (-i["n"], POT.index(i["p"]))),
            dom=dominante(inf.get(pid, []))[0], tot=dominante(inf.get(pid, []))[1],
            emp=[q for q in POT if dominante(inf.get(pid, []))[1] and dominante(inf.get(pid, []))[1].get(q) == max(dominante(inf.get(pid, []))[1].values())],
        ))
    provincias.sort(key=lambda p: p["n"])

    # Fichas de ciudades (paso 4)
    nombres = {c["n"] for c in ciudades}
    for k in list(ciudades_fichas.INTENDENTES) + list(ciudades_fichas.MANDA) + [x[0] for x in ciudades_fichas.CONFLICTOS]:
        assert k in nombres, f"Ficha de ciudad inexistente: {k}"
    for c in ciudades:
        it = ciudades_fichas.INTENDENTES.get(c["n"])
        if it:
            c["int"] = dict(n=it[0], par=it[1], fam=it[2], ver=it[3], u=it[4], nota=it[5])
        if ciudades_fichas.MANDA.get(c["n"]):
            c["manda"] = ciudades_fichas.MANDA[c["n"]]
        cf = [dict(t=t, x=x, u=u) for n, t, x, u in ciudades_fichas.CONFLICTOS if n == c["n"]]
        if cf:
            c["conf"] = cf
        li = inf.get("c:" + c["s"], [])
        if li:
            d, tot = dominante(li)
            c.update(inf=sorted(li, key=lambda i: (-i["n"], POT.index(i["p"]))), dom=d, tot=tot,
                     emp=[q for q in POT if tot.get(q) == max(tot.values())])
    for k in inf:
        if k.startswith("c:"):
            assert any("c:" + c["s"] == k for c in ciudades), f"Influencia para una ciudad inexistente: {k}"

    pais = dict(pob=sum(poblacion.PROVINCIA.values()), inf=sorted(inf.get("AR", []), key=lambda i: (-i["n"], POT.index(i["p"]))))
    meta = dict(potencias=POT, canales=influencias.CANALES, alineamiento=alineamiento.ALINEAMIENTO,
                fuente_censo=poblacion.FUENTE, fuente_exp=economia.FUENTE_EXPORTACIONES, periodo_exp=economia.PERIODO_EXPORTACIONES,
                fuente_propios=economia.FUENTE_RECURSOS_PROPIOS, fuente_ali=alineamiento.FUENTE_MAPA)
    from puntaje import calcular
    actores, relaciones, meta_act = calcular({c["n"]: c for c in ciudades})
    meta["act"] = meta_act
    import friccion
    slugs = {c["s"] for c in ciudades}
    ids = {a["id"] for a in actores} | set(meta_act["externos"])
    fr = []
    for (i, n, tipo, prov, cs, lon, lat, nv, est, act, pots, x, hitos, fu) in friccion.FRICCION:
        assert prov in ign and (cs is None or cs in slugs), f"Fricción {i}: provincia o ciudad inexistente"
        assert all(a in ids for a in act), f"Fricción {i}: actor desconocido"
        assert all(q in POT for q in pots), f"Fricción {i}: potencia desconocida"
        assert nv in (1, 2, 3) and fu and all(h[2] for h in hitos), f"Fricción {i}: falta intensidad o fuente"
        fr.append(dict(id=i, n=n, tipo=tipo, prov=prov, cs=cs, lon=lon, lat=lat, nv=nv, est=est, act=act, pot=pots, x=x,
                       hit=[dict(f=h[0], x=h[1], u=h[2]) for h in hitos], fu=[dict(t=t, u=u) for t, u in fu]))
    zonas = []
    for (i, n, prov, cs, lon, lat, est, x, fu) in friccion.ZONAS:
        assert prov in ign and (cs is None or cs in slugs) and fu, f"Zona {i}: datos o fuente faltantes"
        zonas.append(dict(id=i, n=n, prov=prov, cs=cs, lon=lon, lat=lat, est=est, x=x, fu=[dict(t=t, u=u) for t, u in fu]))
    out = dict(corte=CORTE, proxima=PROXIMA, meta=meta, pais=pais, provincias=provincias, ciudades=ciudades,
               deppob=poblacion.DEPARTAMENTO, actores=actores, relaciones=relaciones, friccion=fr, zonas=zonas)
    with open(os.path.join(RAIZ, "data", "territorio.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print(f"data/territorio.json: {len(provincias)} provincias, {sum(ndep.values())} departamentos, {len(ciudades)} ciudades, {len(actores)} actores y {len(relaciones)} relaciones, {len(fr)} puntos de fricción y {len(zonas)} zona(s) liberada(s). Corte {CORTE}.")


if __name__ == "__main__":
    main()
