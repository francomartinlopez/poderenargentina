"""Puntaje de los actores (paso 3): la misma fórmula que El mapa del poder global.

capacidad = suma ponderada de los 21 ejes (coerción, información y acción fuera de la ley valen 2; contactos y privilegio, 1,5)
autonomía real = factor de autonomía formal corregido por el poder duro (armas, secretos, acción fuera de la ley, contactos)
red = poder propio + la mitad de lo que se hereda de quienes dependen del actor
puntaje = media geométrica ponderada de categoría teórica, capacidad, alcance, autonomía y red, elevada a 3, con el mayor en 100
poder oculto = puntaje por la brecha entre el poder real y el formal, con el mayor en 100
"""
import math
from ejes import EJES, PESOS, AUTONOMIA_REAL, TEORICO, TIPO, PESO_FINAL, ESTIRAR, ALCANCE, AUTONOMIA, CERTEZA, BLOQUES, TIPOS_REL, PESO_REL, EXTERNOS, GLOBAL_URL
from actores import ACTORES as _A, FICHAS as _F, RELACIONES as _R
import actores_provinciales as _P
ACTORES = _A + _P.ACTORES
FICHAS = {**_F, **_P.FICHAS}
_pares = {frozenset((r[0], r[1])) for r in _R}
RELACIONES = _R + [r for r in _P.RELACIONES if frozenset((r[0], r[1])) not in _pares]

FAC = {1: 1, 2: .75, 3: .5, 4: .25}


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
        assert sede in ciudades_por_nombre, f"{i}: sede {sede} no está entre las ciudades"
        assert i in FICHAS and FICHAS[i]["fuentes"], f"{i}: falta ficha o fuentes"
        A[i] = dict(id=i, n=n, cat=cat, tipo=TIPO[cat], sede=sede, alc=alc, bloque=blo, aut=aut, cert=cert, formal=formal,
                    sc=[int(c) for c in sc], dep=[d for d in dep.split(",") if d])
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
    her = {i: A[i]["red"] - A[i]["pe"] for i in A}
    hmax = max(her.values()) or 1
    amax = max(v for v, _ in ALCANCE.values())

    def comp(a):
        return {"ct": TEORICO[a["cat"]] / 10, "cap": max(a["cap"], .5) / capmax, "alc": ALCANCE[a["alc"]][0] / amax, "aut": a["fr"],
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
        a.update(res=f["res"], manda=f["manda"], fu=[list(x) for x in f["fuentes"]])
        a["prov"] = ciudades_por_nombre[a["sede"]]["prov"]
        a["cs"] = ciudades_por_nombre[a["sede"]]["s"]
        for k in ("dur", "pe"):
            a[k] = round(a[k], 3)
        a["fr"] = round(a["fr"], 3)
        a["red"] = round(a["red"], 2)

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
    actores = sorted(A.values(), key=lambda a: (-a["pt"], a["n"]))
    meta = dict(ejes=[dict(k=e[0], n=e[1], g=e[2], d=e[3], a=list(e[4])) for e in EJES], pesos=PESOS, teorico=TEORICO,
                alcance={k: v[1] for k, v in ALCANCE.items()}, autonomia=AUTONOMIA, certeza=CERTEZA, bloques=BLOQUES,
                peso_final=PESO_FINAL, estirar=ESTIRAR, externos=EXTERNOS, global_url=GLOBAL_URL, tipos_rel=TIPOS_REL)
    return actores, rel, meta
