"""Puntaje de los actores (paso 3): la misma fórmula que El mapa del poder global.

capacidad = suma ponderada de los 21 ejes (coerción, información y acción fuera de la ley valen 2; contactos y privilegio, 1,5)
autonomía real = factor de autonomía formal corregido por el poder duro (armas, secretos, acción fuera de la ley, contactos)
red = poder propio + la mitad de lo que se hereda de quienes dependen del actor
puntaje = media geométrica ponderada de categoría teórica, capacidad, alcance, autonomía y red, elevada a 3, con el mayor en 100
poder oculto = puntaje por la brecha entre el poder real y el formal, con el mayor en 100
"""
import math
from ejes import EJES, PESOS, AUTONOMIA_REAL, TEORICO, TIPO, PESO_FINAL, ESTIRAR, ALCANCE, AUTONOMIA, CERTEZA, BLOQUES, TIPOS_REL, PESO_REL, EXTERNOS, EXTERNOS_SIN_FICHA, GLOBAL_URL
from actores import ACTORES as _A, FICHAS as _F, RELACIONES as _R
import actores_provinciales as _P
import actores_mas as _M
import actores_mas2 as _M2
import actores_mas3 as _M3
import actores_mas4 as _M4
import actores_mas5 as _M5
import actores_mas6 as _M6
import actores_mas7 as _M7
import actores_mas8 as _M8
import actores_mas9 as _M9
import bloques as _BL
import json as _json
import os as _os
ACTORES = _A + _P.ACTORES + _M.ACTORES + _M2.ACTORES + _M3.ACTORES + _M4.ACTORES + _M5.ACTORES + _M6.ACTORES + _M7.ACTORES + _M8.ACTORES + _M9.ACTORES
# Actores de fuente/actores.py que suman en su nombre a quien los conduce (corte del 19/11/2026).
ACTORES = [(a[0], _M3.NOMBRES[a[0]][0]) + tuple(a[2:]) if a[0] in _M3.NOMBRES else a for a in ACTORES]
# Bloque internacional: los motivos de fuente/bloques.py mandan sobre lo cargado en cada tanda; el mapa global, sobre todo.
def _blo(a):
    m = _BL.MOTIVOS.get(a[0])
    assert not (m and a[0] in _BL.GLOBAL and m[0] != _BL.GLOBAL[a[0]]), f"Bloque de {a[0]}: el motivo contradice al mapa global"
    return _BL.GLOBAL.get(a[0]) or (m[0] if m else a[5])


ACTORES = [a[:5] + (_blo(a),) + tuple(a[6:]) for a in ACTORES]
FICHAS = {k: dict(v) for k, v in {**_F, **_P.FICHAS, **_M.FICHAS, **_M2.FICHAS, **_M3.FICHAS, **_M4.FICHAS, **_M5.FICHAS, **_M6.FICHAS, **_M7.FICHAS, **_M8.FICHAS, **_M9.FICHAS}.items()}
for _i, (_n, _fu) in _M3.NOMBRES.items():
    if _fu[1] not in [u for _, u in FICHAS[_i]["fuentes"]]:
        FICHAS[_i]["fuentes"] = list(FICHAS[_i]["fuentes"]) + [_fu]


def _nombre_dep(did):
    """Nombre de un partido o departamento según la cartografía del IGN (data/dep/<prov>.json)."""
    ruta = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data", "dep", did[:2] + ".json")
    topo = _json.load(open(ruta, encoding="utf-8"))
    return next(x["properties"]["nombre"] for x in topo["objects"]["dep"]["geometries"] if x["properties"]["id"] == did)
for _i, (_txt, _fu) in _M2.TEXTOS.items():
    assert _i in FICHAS, f"texto para actor inexistente: {_i}"
    FICHAS[_i]["txt"] = _txt
    if _fu[1] not in [u for _, u in FICHAS[_i]["fuentes"]]:
        FICHAS[_i]["fuentes"] = list(FICHAS[_i]["fuentes"]) + [_fu]
# Una sola relación por par de actores y tipo (la primera que aparece manda).
_vistos = {(frozenset((r[0], r[1])), r[2]) for r in _R}
RELACIONES = list(_R)
for r in _P.RELACIONES + _M.RELACIONES + _M2.RELACIONES + _M3.RELACIONES + _M4.RELACIONES + _M5.RELACIONES + _M6.RELACIONES + _M7.RELACIONES + _M8.RELACIONES + _M9.RELACIONES:
    k = (frozenset((r[0], r[1])), r[2])
    if k not in _vistos:
        _vistos.add(k)
        RELACIONES.append(r)

FAC = {1: 1, 2: .75, 3: .5, 4: .25}


def sc_intendente(sede, ciudades):
    """Regla única para los intendentes (corte del 20/11/2026): los ejes salen de la población del partido o departamento.
    Base: dominio territorial, contactos, apoyo, cohesión y normas locales en 1.
    300.000 habitantes o más: capital físico y miembros en 1 (presupuesto y planta municipal grandes).
    1 millón o más: contactos en 2 y moderación de la agenda en 1."""
    import poblacion
    did = sede[4:] if sede.startswith("dep:") else ciudades[sede]["dep"]
    pob = poblacion.DEPARTAMENTO[did]
    k = dict(ter=1, red=1, apo=1, coh=1, reg=1)
    if pob >= 300000:
        k.update(cap=1, mie=1)
    if pob >= 1000000:
        k.update(red=2, mod=1)
    return "".join(str(k.get(e[0], 0)) for e in EJES)


def calcular(ciudades_por_nombre):
    ejes = [e[0] for e in EJES]
    ids = [a[0] for a in ACTORES]
    assert len(set(ids)) == len(ids), "ids repetidos"
    peso = {k: PESOS.get(k, 1) for k in ejes}
    capmax = 3 * len(ejes)
    norma = capmax / sum(3 * w for w in peso.values())
    A = {}
    for i, n, cat, sede, alc, blo, aut, sc, cert, dep, formal in ACTORES:
        assert len(sc) == len(ejes) and sc.isdigit() and all(c in "0123" for c in sc), i
        assert cat in TEORICO and alc in ALCANCE and blo in BLOQUES and aut in AUTONOMIA and cert in CERTEZA and formal in (0, 1, 2, 3), i
        assert sede in ciudades_por_nombre or (sede.startswith("dep:") and _nombre_dep(sede[4:])), f"{i}: sede {sede} no está entre las ciudades"
        assert i in FICHAS and FICHAS[i]["fuentes"], f"{i}: falta ficha o fuentes"
        A[i] = dict(id=i, n=n, cat=cat, tipo=TIPO[cat], sede=sede, alc=alc, bloque=blo, aut=aut, cert=cert, formal=formal,
                    sc=[int(c) for c in sc], dep=[d for d in dep.split(",") if d])
        if i.startswith("int_"):
            A[i]["sc"] = [int(c) for c in sc_intendente(sede, ciudades_por_nombre)]
    for a in A.values():
        for d in a["dep"]:
            assert d in A, f"{a['id']} depende de {d}, que no existe"
    for a in A.values():
        sc = dict(zip(ejes, a["sc"]))
        a["cap"] = round(sum(sc[k] * peso[k] for k in ejes) * norma, 2)
        a["dur"] = min(1, (sc["coe"] + sc["adq"] + sc["ext"] + sc["red"]) / 12)
        a["fr"] = FAC[a["aut"]] + (1 - FAC[a["aut"]]) * a["dur"] * AUTONOMIA_REAL
        a["pe"] = a["cap"] * a["fr"]
    memo = {}

    def red(i, pila=()):
        if i in memo:
            return memo[i]
        if i in pila:
            raise SystemExit(f"Ciclo de dependencias en {i}")
        v = A[i]["pe"] + .5 * sum(red(j, pila + (i,)) * (1 - AUTONOMIA_REAL * A[j]["dur"]) / len(A[j]["dep"]) for j in A if i in A[j]["dep"])
        memo[i] = v
        return v
    for i in A:
        A[i]["red"] = red(i)
    rel = []
    vistos = set()
    for o, d, t, x, n, u in RELACIONES:
        for z in (o, d):
            assert z in A or z in EXTERNOS, f"relación con actor desconocido: {z}"
        assert t in TIPOS_REL and n in (1, 2, 3) and u.startswith("http"), (o, d, t)
        k = (o, d, t)
        assert k not in vistos, f"relación repetida {k}"
        vistos.add(k)
        rel.append(dict(o=o, d=d, t=t, x=x, n=n, u=u))
    # Puntaje real de categoría (informativo, no entra en la fórmula), como en el mapa global
    sale = {i: 0.0 for i in A}
    entra = {i: 0.0 for i in A}
    for r in rel:
        w = PESO_REL.get(r["t"])
        if w and r["o"] in A:
            sale[r["o"]] += w
        if w and r["d"] in A:
            entra[r["d"]] += w
    for a in A.values():
        for d in a["dep"]:
            sale[d] += 1
            entra[a["id"]] += 1
    # Categoría relevada en el mapa argentino (corte del 20/11/2026, decisión de Franco):
    # por actor, 50 % autonomía, 30 % dominio en sus relaciones, 20 % dependientes (tope 3) y +15 % si enfrenta a su jefe formal.
    # El promedio de la categoría se lleva a la escala 3-9 del teórico y se promedia 50/50 con él.
    AUTREL = {1: 1, 2: .67, 3: .33, 4: 0}
    depn = {i: sum(1 for b in A.values() if i in b["dep"]) for i in A}
    def releva(a):
        s_, e_ = sale[a["id"]], entra[a["id"]]
        dom = s_ / (s_ + e_) if s_ + e_ else .5
        v = .5 * AUTREL[a["aut"]] + .3 * dom + .2 * min(depn[a["id"]], 3) / 3
        if any(r["t"] in ("Enfrentamiento", "Ambigua") and {r["o"], r["d"]} == {a["id"], j} for j in a["dep"] for r in rel):
            v += .15
        return min(v, 1)
    porcat = {}
    for a in A.values():
        porcat.setdefault(a["cat"], []).append(releva(a))
    bruto_c = {c: 10 * sum(v) / len(v) for c, v in porcat.items()}
    lo, hi = min(bruto_c.values()), max(bruto_c.values())
    REL_CAT = {c: round(3 + 6 * (v - lo) / ((hi - lo) or 1), 1) for c, v in bruto_c.items()}
    CAT_FINAL = {c: round((TEORICO[c] + REL_CAT[c]) / 2, 2) for c in REL_CAT}
    her = {i: A[i]["red"] - A[i]["pe"] for i in A}
    hmax = max(her.values()) or 1
    amax = max(v for v, _ in ALCANCE.values())

    def comp(a):
        return {"ct": CAT_FINAL[a["cat"]] / 10, "cap": max(a["cap"], .5) / capmax, "alc": ALCANCE[a["alc"]][0] / amax, "aut": a["fr"],
                "red": .5 + .5 * math.log1p(her[a["id"]]) / math.log1p(hmax)}
    bruto = {i: math.prod(v ** PESO_FINAL[k] for k, v in comp(a).items()) for i, a in A.items()}
    bmax = max(bruto.values())
    for i, a in A.items():
        a["pt"] = round(100 * (bruto[i] / bmax) ** ESTIRAR, 1)
        a["cp"] = [round(comp(a)[k], 3) for k in PESO_FINAL]
        a["brecha"] = round((3 - a["formal"]) / 3, 3)
    omax = max(a["pt"] * a["brecha"] for a in A.values()) or 1
    for a in A.values():
        a["oculto"] = round(100 * a["pt"] * a["brecha"] / omax, 1)
        f = FICHAS[a["id"]]
        a.update(res=f["res"], manda=f["manda"], fu=[list(x) for x in f["fuentes"]], txt=f.get("txt", ""))
        if a["sede"].startswith("dep:"):
            # Sede en un partido o departamento sin ciudad propia en el mapa.
            a["sd"] = a["sede"][4:]
            a["prov"], a["cs"], a["sede"] = a["sd"][:2], "", _nombre_dep(a["sd"])
        else:
            a["prov"] = ciudades_por_nombre[a["sede"]]["prov"]
            a["cs"] = ciudades_por_nombre[a["sede"]]["s"]
        for k in ("dur", "pe"):
            a[k] = round(a[k], 3)
        a["fr"] = round(a["fr"], 3)
        a["red"] = round(a["red"], 2)

    actores = sorted(A.values(), key=lambda a: (-a["pt"], a["n"]))
    meta = dict(ejes=[dict(k=e[0], n=e[1], g=e[2], d=e[3], a=list(e[4])) for e in EJES], pesos=PESOS, teorico=TEORICO,
                alcance={k: v[1] for k, v in ALCANCE.items()}, autonomia=AUTONOMIA, certeza=CERTEZA, bloques=BLOQUES,
                peso_final=PESO_FINAL, estirar=ESTIRAR, cat_relevada=REL_CAT, cat_final=CAT_FINAL, externos=EXTERNOS, sin_ficha=list(EXTERNOS_SIN_FICHA), global_url=GLOBAL_URL, tipos_rel=TIPOS_REL)
    return actores, rel, meta
