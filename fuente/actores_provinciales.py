# Actores provinciales y municipales (paso 5, corte del 19/11/2026).
# Los gobiernos provinciales se puntúan con una plantilla a partir de datos duros, con ajustes editoriales escritos abajo:
#   recursos naturales: 2 en las provincias de hidrocarburos o minería de escala (las provincias son dueñas del subsuelo), 1 en el resto;
#   coerción, dominio territorial y miembros: 2 si la provincia supera 1,5 M de habitantes (policía y planta estatal grandes), 1 si no;
#   cohesión: 3 en las provincias con hegemonía de un mismo grupo por décadas, 1 donde el oficialismo se partió;
#   moderación de información: 2 donde el oficialismo provincial domina la agenda local por décadas;
#   regulación y privilegio legal: 2 en todas (leyes provinciales, policía, concesiones);
#   dinero: 2 si los recursos propios superan la mitad de los ingresos (ASAP, fuente/economia.py), 1 si no (corte del 20/11/2026).
# Las relaciones con la Nación salen del alineamiento de fuente/alineamiento.py, con su fuente.
from provincias import PROVINCIAS
from alineamiento import PROVINCIAS as ALI
from economia import PROVINCIAS as ECO

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
    din = 2 if (ECO[pid].get("propios") or 0) >= 50 else 1
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

# Sindicatos regionales y empresas provinciales (corte del 19/11/2026).
ACTORES += [
    ("petroleros_nqn", "Sindicato de Petroleros Privados de Neuquén, Río Negro y La Pampa (Marcelo Rucci)", "Sindicato", "Neuquén", "R", "I", 1,
     "110201000000001120201", "D", "", 0),
    ("soea_sl", "Sindicato de Obreros y Empleados Aceiteros de San Lorenzo (SOEA)", "Sindicato", "San Lorenzo", "R", "I", 1,
     "010201000000001020201", "D", "", 0),
    ("uom_vc", "UOM seccional Villa Constitución", "Sindicato", "Villa Constitución", "M", "I", 1,
     "000101000000001020101", "D", "", 0),
    ("smata_cba", "SMATA Córdoba", "Sindicato", "Córdoba", "R", "I", 1,
     "000101000000001020201", "D", "", 0),
    ("gyp_nqn", "Gas y Petróleo del Neuquén (GyP)", "Recursos primarios", "Neuquén", "P", "I", 3,
     "210110000110100010211", "D", "gob_neuquen", 1),
    ("jemse", "Jujuy Energía y Minería Sociedad del Estado (JEMSE)", "Recursos primarios", "San Salvador de Jujuy", "P", "I", 3,
     "210110000110100010211", "D", "gob_jujuy", 1),
]
FICHAS.update({
    "petroleros_nqn": dict(res="Gremio de los trabajadores petroleros de la cuenca neuquina, con más de 20.000 afiliados; puede detener Vaca Muerta y en 2026 lanzó su propio partido, Fuerza Neuquina y Federal.",
                           manda="Marcelo Rucci, secretario general, reelecto en 2025 hasta 2029 con lista única.",
                           fuentes=[("LM Neuquén: Rucci inicia un nuevo período", "https://mase.lmneuquen.com/vaca-muerta/marcelo-rucci-inicio-un-nuevo-periodo-frente-al-sindicato-petroleros-privados-n1217890/amp"),
                                    ("LM Neuquén: el partido de Petroleros", "https://mase.lmneuquen.com/marcelo-rucci-a9825/1"),
                                    ("Noticias NQN: Rucci contra el ajuste de Halliburton", "https://www.noticiasnqn.com.ar/amp/noticias/2026/09/08/351608-rucci-rechazo-el-ajuste-de-halliburton-a-las-pymes-de-vaca-muerta")]),
    "soea_sl": dict(res="Sindicato de los aceiteros del departamento San Lorenzo, el mayor polo de molienda de soja del mundo; sus paros frenan los puertos del Gran Rosario y la liquidación de divisas. No integra la Federación Aceitera, con la que suele actuar en conjunto.",
                    manda="Su conducción, encabezada por Daniel Succi.",
                    fuentes=[("La Capital: aceiteros frenan los puertos (mayo de 2026)", "https://www.lacapital.com.ar/aceiteros-lanzan-un-paro-y-se-frenan-los-puertos-del-gran-rosario-n10261479.html/amp"),
                             ("La Capital: los paros calientan el conflicto aceitero", "https://www.lacapital.com.ar/politica/los-paros-trasfondo-politico-calientan-el-conflicto-aceitero-n10263210.html/amp"),
                             ("AgroLatam: el SOEA no es parte de la Federación", "https://www.agrolatam.com/actualidad/la-agroindustria-denuncio-que-el-sindicato-aceitero-lanzo-otro-paro-por-un-conflicto-en-una-empresa")]),
    "uom_vc": dict(res="Seccional metalúrgica de Villa Constitución, donde Acindar (ArcelorMittal) tiene su planta principal; negocia suspensiones y salarios en una planta que produce la mitad que en 2024.",
                   manda="Pablo González, secretario general de la seccional.",
                   fuentes=[("iProfesional: UOM y Acindar cierran aumento (mayo de 2026)", "https://www.iprofesional.com/economia/454009-aumento-salarial-en-acindar-y-suspension-del-paro-a-cuanto-se-fue-el-sueldo-promedio"),
                            ("La Capital: Acindar frena la producción (junio de 2026)", "https://www.lacapital.com.ar/economia/acindar-decidio-frenar-la-produccion-villa-constitucion-falta-ventas-n10263980.html")]),
    "smata_cba": dict(res="Seccional cordobesa del gremio mecánico, con unos 15.000 afiliados en Fiat (Stellantis), Renault y Volkswagen; en 2026 acordó con Renault un banco de horas para 1.200 operarios.",
                      manda="Maximiliano Ponce, secretario general.",
                      fuentes=[("Perfil Córdoba: banco de horas en Renault", "https://perfil.com/cordoba/banco-de-horas-en-renault-cordoba-la-jugada-que-avalo-pettovello-pero-que-genera-fuerte-malestar-gremial-aPFAs2e4VIB1"),
                               ("InfoNegocios: afiliados del SMATA en Córdoba", "https://infonegocios.info/plus/desmienten-que-los-despidos-en-renault-sean-masivos-ajustes-de-personal-son-normales")]),
    "gyp_nqn": dict(res="Empresa petrolera de la provincia del Neuquén, titular de las áreas reservadas; en 2026 licitó 15 áreas de Vaca Muerta (Ronda 1) y recibió ofertas por más de 410 millones de dólares, con participación propia de 10% a 20%.",
                    manda="El gobierno de Rolando Figueroa, a través del Ministerio de Energía y Recursos Naturales.",
                    fuentes=[("iProfesional: Neuquén licita 15 áreas", "https://www.iprofesional.com/energia/450998-neuquen-licita-15-areas-en-vaca-muerta-para-acelerar-inversiones"),
                             ("El Economista: pliego de la Ronda 1/2026", "https://eleconomista.com.ar/energia/neuquen-licita-quince-areas-hidrocarburiferas-vaca-muerta-como-participar-n95178"),
                             ("LM Neuquén: ofertas de la Ronda 1", "https://mase.lmneuquen.com/vaca-muerta/areas-petroleras-vaca-muerta-quienes-lideran-las-ofertas-la-ronda-1-gyp-n1253992/amp")]),
    "jemse": dict(res="Empresa minera y energética de Jujuy; es socia de Minera Exar en Cauchari-Olaroz (8,5%) junto a Ganfeng y Lithium Argentina, y por ella la provincia actúa como regulador y socio a la vez.",
                  manda="El gobierno de Carlos Sadir.",
                  fuentes=[("TodoJujuy: JEMSE entra al directorio de Exar", "https://www.todojujuy.com/jujuy/minera-exar-incorpora-jemse-al-directorio-la-empresa-n201950"),
                           ("TodoJujuy: proyectos de litio en el NOA", "https://www.todojujuy.com/pais/litio-jujuy-salta-y-catamarca-cuales-son-los-proyectos-mas-importantes-esta-region-n286652")]),
})
RELACIONES += [
    ("petroleros_nqn", "gob_neuquen", "Alianza", "Acompaña al gobernador en las misiones a inversores y en el Instituto Vaca Muerta.", 1, "https://www.noticiasnqn.com.ar/noticias/2026/03/16/329551-marcelo-rucci-celebro-la-inauguracion-del-instituto-vaca-muerta-y-pidio-una-formacion-con-mirada-federal"),
    ("petroleros_nqn", "ypf", "Ambigua", "Negocia salarios y empleo con las operadoras de Vaca Muerta, con amenazas de paro en cada paritaria.", 2, "https://mase.lmneuquen.com/marcelo-rucci-a9825/2"),
    ("petroleros_nqn", "milei", "Enfrentamiento", "Rechazó la reforma laboral del Gobierno nacional.", 1, "https://www.letrap.com.ar/politica/neuquen-marcelo-rucci-abrio-el-paraguas-y-se-planto-contra-la-reforma-laboral-javier-milei-n5420250"),
    ("soea_sl", "ciara", "Enfrentamiento", "Paros por salarios en las aceiteras y terminales; en mayo de 2026 la Nación dictó la conciliación obligatoria y en junio se cerró un aumento.", 2, "https://www.lacapital.com.ar/economia/paro-y-conciliacion-obligatoria-aceiteros-san-lorenzo-afirman-que-la-lucha-continua-n10261593.html/amp"),
    ("soea_sl", "cgt_arg", "Alianza", "Adhirió al paro general de la CGT contra la reforma laboral y paralizó 17 terminales.", 1, "https://www.agrolatam.com/argentina/actualidad/paro-en-17-puertos-el-conflicto-que-frena-las-exportaciones-del-agro-3608/"),
    ("smata_cba", "gob_cordoba", "Ambigua", "Negocia con las automotrices radicadas en la provincia bajo la mirada del gobierno provincial.", 1, "https://perfil.com/cordoba/banco-de-horas-en-renault-cordoba-la-jugada-que-avalo-pettovello-pero-que-genera-fuerte-malestar-gremial-aPFAs2e4VIB1"),
    ("gob_neuquen", "gyp_nqn", "Propiedad", "Empresa del Estado neuquino; licita las áreas reservadas de Vaca Muerta.", 3, "https://www.iprofesional.com/energia/450998-neuquen-licita-15-areas-en-vaca-muerta-para-acelerar-inversiones"),
    ("gob_jujuy", "jemse", "Propiedad", "Empresa del Estado jujeño; socia en Cauchari-Olaroz.", 3, "https://www.todojujuy.com/pais/litio-jujuy-salta-y-catamarca-cuales-son-los-proyectos-mas-importantes-esta-region-n286652"),
]
