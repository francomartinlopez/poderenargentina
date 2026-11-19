# Actores provinciales y municipales (paso 5, corte del 19/11/2026).
# Los gobiernos provinciales se puntúan con una plantilla a partir de datos duros, con ajustes editoriales escritos abajo:
#   recursos naturales: 2 en las provincias de hidrocarburos o minería de escala (las provincias son dueñas del subsuelo), 1 en el resto;
#   coerción, dominio territorial y miembros: 2 si la provincia supera 1,5 M de habitantes (policía y planta estatal grandes), 1 si no;
#   cohesión: 3 en las provincias con hegemonía de un mismo grupo por décadas, 1 donde el oficialismo se partió;
#   moderación de información: 2 donde el oficialismo provincial domina la agenda local por décadas;
#   regulación y privilegio legal: 2 en todas (leyes provinciales, policía, concesiones).
# Las relaciones con la Nación salen del alineamiento de fuente/alineamiento.py, con su fuente.
from provincias import PROVINCIAS
from alineamiento import PROVINCIAS as ALI

IDS = {"02": "gob_caba", "10": "gob_catamarca", "18": "gob_corrientes", "22": "gob_chaco", "26": "gob_chubut", "30": "gob_entrerios",
       "34": "gob_formosa", "38": "gob_jujuy", "42": "gob_lapampa", "46": "gob_larioja", "50": "gob_mendoza", "54": "gob_misiones",
       "62": "gob_rionegro", "66": "gob_salta", "70": "gob_sanjuan", "74": "gob_sanluis", "78": "gob_santacruz", "86": "gob_sde",
       "90": "gob_tucuman", "94": "gob_tdf"}
# Gobiernos que ya estaban entre los actores núcleo (paso 3).
YA = {"06": "gob_pba", "14": "gob_cordoba", "82": "gob_santafe", "58": "gob_neuquen"}

REC2 = {"26", "78", "50", "66", "38", "10", "70", "62"}   # hidrocarburos, litio, cobre u oro
HEGEMONIA = {"34", "86", "46"}                           # Formosa, Santiago del Estero, La Rioja
PARTIDO = {"54"}                                         # Misiones: ruptura de 2026
POB = {"02": 3121707, "10": 429562, "18": 1212696, "22": 1129606, "26": 592621, "30": 1425578, "34": 607419, "38": 811611,
       "42": 361859, "46": 383865, "50": 2043540, "54": 1278873, "62": 750768, "66": 1441351, "70": 822853, "74": 542069,
       "78": 337226, "86": 1060906, "90": 1731820, "94": 185732}
SEDE = {"02": "Ciudad Autónoma de Buenos Aires", "10": "San Fernando del Valle de Catamarca", "18": "Corrientes", "22": "Resistencia",
        "26": "Rawson", "30": "Paraná", "34": "Formosa", "38": "San Salvador de Jujuy", "42": "Santa Rosa", "46": "La Rioja",
        "50": "Mendoza", "54": "Posadas", "62": "Viedma", "66": "Salta", "70": "San Juan", "74": "San Luis", "78": "Río Gallegos",
        "86": "Santiago del Estero", "90": "San Miguel de Tucumán", "94": "Ushuaia"}


def plantilla(pid):
    g = 2 if POB[pid] > 1500000 else 1
    rec = 0 if pid == "02" else (2 if pid in REC2 else 1)
    cap = 2 if pid == "02" else 1
    mov = 2 if pid == "02" else 1
    din = 2 if pid == "02" else 1
    mod = 2 if pid in HEGEMONIA else 1
    coh = 3 if pid in HEGEMONIA else (1 if pid in PARTIDO else 2)
    inn = 1 if pid == "02" else 0
    #        rec cap prd mov gan din coe ter ext adq pro mod con inn mie cul red apo coh reg pri
    sc = [rec, cap, 1, mov, 0, din, g, g, 0, 1, 1, mod, 1, inn, g, 1, 2, 2, coh, 2, 2]
    return "".join(map(str, sc))


ACTORES = []
FICHAS = {}
RELACIONES = []
W = "https://es.wikipedia.org/wiki/"
for pid, aid in IDS.items():
    slug, corto, gob, par, desde = PROVINCIAS[pid]
    a = ALI[pid]
    nombre = ("Gobierno de la Ciudad de Buenos Aires" if pid == "02" else f"Gobierno de {corto}") + f" ({gob})"
    ACTORES.append((aid, nombre, "Gobierno", SEDE[pid], "P", "I", 1, plantilla(pid), "D", "", 2))
    FICHAS[aid] = dict(res=f"Gobierno provincial. Gobierna: {a['grupo']}. {a['manda']}",
                       manda=f"{gob}, {'jefe de Gobierno' if pid == '02' else 'gobernador'} desde {desde[:4]} ({par}).",
                       fuentes=[("Alineamiento y quién manda: " + u.split("/")[2].replace("www.", ""), u) for u in a["fuentes"]])

TEXTO = {"A": ("jgm", "Alianza", "Acuerdo electoral con La Libertad Avanza; negocia con la Jefatura de Gabinete.", 2),
         "D": ("jgm", "Ambigua", "Dialoguista: negocia votos y fondos con la Nación sin acuerdo electoral pleno.", 2),
         "I": ("jgm", "Ambigua", "Espacio propio que compite con La Libertad Avanza (Provincias Unidas); negocia por fondos y leyes.", 1),
         "O": ("milei", "Enfrentamiento", "Opositor al Gobierno nacional.", 2)}
for pid, aid in {**IDS, **YA}.items():
    a = ALI[pid]
    con, tipo, txt, n = TEXTO[a["ali"]]
    RELACIONES.append((aid, con, tipo, txt, n, a["fuentes"][0]))

# Poder real que no coincide con el cargo formal
ACTORES += [
    ("zamora", "Gerardo Zamora (Frente Cívico por Santiago)", "Líder político", "Santiago del Estero", "P", "I", 1,
     "100001110011101121321", "D", "", 1),
    ("muni_rosario", "Municipalidad de Rosario (Pablo Javkin)", "Gobierno", "Rosario", "M", "I", 1, "010101010011101111222", "D", "", 1),
    ("muni_cordoba", "Municipalidad de Córdoba (Daniel Passerini)", "Gobierno", "Córdoba", "M", "I", 2, "010101010011101111221", "D", "gob_cordoba", 1),
]
FICHAS.update({
    "zamora": dict(res="Gobernó Santiago del Estero, solo o con su esposa, desde 2005; hoy es senador nacional y conduce el Frente Cívico, que en agosto de 2026 ganó las 26 intendencias en juego, incluida La Banda por primera vez.",
                   manda="Gerardo Zamora; el gobernador Elías Suárez fue durante veinte años su jefe de Gabinete.",
                   fuentes=[("La Nación: Zamora se queda con todos los municipios", "https://www.lanacion.com.ar/politica/zamora-consigue-la-hegemonia-absoluta-en-santiago-y-se-queda-con-todos-los-municipios-nid02082026/"),
                            ("Fuente del alineamiento", ALI["86"]["fuentes"][0])]),
    "muni_rosario": dict(res="Gobierna la mayor ciudad de Santa Fe y el centro del complejo agroexportador; la seguridad frente a las bandas narcocriminales ordena su agenda junto con la provincia.",
                         manda="Pablo Javkin, intendente (Creo, dentro de Unidos para Cambiar Santa Fe).",
                         fuentes=[("Infobae: intendentes de 2026", "https://www.infobae.com/politica/2026/08/17/cual-es-el-perfil-sociologico-de-los-intendentes-en-argentina/")]),
    "muni_cordoba": dict(res="Gobierna la segunda ciudad del país, dentro del peronismo cordobés que conduce la provincia.",
                         manda="Daniel Passerini, intendente (Hacemos Unidos por Córdoba).",
                         fuentes=[("Ranking federal de intendentes, abril de 2026", "https://eduardogerman.com/wp-content/uploads/2026/04/ABRIL-2026-%E2%80%93-RANKING-CB-DE-GOBERNADORES-RANKING-FEDERAL-CB-DE-INTENDENTES.pdf")]),
})
RELACIONES += [
    ("zamora", "gob_sde", "Gobierna", "El gobernador Elías Suárez fue su jefe de Gabinete durante veinte años; Zamora conduce el Frente Cívico.", 3, ALI["86"]["fuentes"][0]),
    ("gob_santafe", "muni_rosario", "Alianza", "Ambos integran Unidos para Cambiar Santa Fe y coordinan la política de seguridad en Rosario.", 2, "https://www.infobae.com/politica/2026/08/17/cual-es-el-perfil-sociologico-de-los-intendentes-en-argentina/"),
    ("gob_cordoba", "muni_cordoba", "Alianza", "El intendente pertenece a Hacemos Unidos por Córdoba, el frente del gobernador.", 2, ALI["14"]["fuentes"][0]),
    ("muni_rosario", "los_monos", "Enfrentamiento", "La violencia de las bandas narcocriminales es el centro de la agenda de seguridad de la ciudad.", 2, "https://www.lacapital.com.ar/policiales/confirmaron-condena-guille-cantero-ataques-contra-objetivos-judiciales-n10034583.html"),
]
