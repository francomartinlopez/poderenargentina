# Quinta tanda de actores (corte del 20/11/2026, pedido de Franco: «aplica todo» sobre las sugerencias del 20/11).
# Intendentes de las capitales y de las dos ciudades bonaerenses más grandes fuera del conurbano (con la regla
# única de ejes por población de scripts/puntaje.py), empresas que dominan las «ciudades de empresa»,
# referentes que faltaban y dueños de medios. Mismo formato que fuente/actores_mas.py.
# Resguardos: de las personas vivas, solo cargos, hechos públicos y lo que estableció un tribunal u organismo oficial.

from actores_mas import S, CABA
from ciudades_fichas import INTENDENTES

ACTORES, FICHAS, RELACIONES = [], {}, []

# --- Intendentes: los datos (nombre, partido, fuente) salen de fuente/ciudades_fichas.py, ya verificados («V»).
CAPITALES = {
    "La Plata": ("int_laplata", "06"), "Santa Fe": ("int_santafe", "82"), "Mendoza": ("int_mendoza", "50"),
    "San Miguel de Tucumán": ("int_tucuman", "90"), "Salta": ("int_salta", "66"), "Paraná": ("int_parana", "30"),
    "Posadas": ("int_posadas", "54"), "Resistencia": ("int_resistencia", "22"), "Corrientes": ("int_corrientes", "18"),
    "Santiago del Estero": ("int_sde", "86"), "San Juan": ("int_sanjuan", "70"), "San Salvador de Jujuy": ("int_jujuy", "38"),
    "Viedma": ("int_viedma", "62"), "Neuquén": ("int_neuquen", "58"), "Formosa": ("int_formosa", "34"),
    "Rawson": ("int_rawson", "26"), "San Luis": ("int_sanluis", "74"), "San Fernando del Valle de Catamarca": ("int_catamarca", "10"),
    "La Rioja": ("int_larioja", "46"), "Santa Rosa": ("int_santarosa", "42"), "Río Gallegos": ("int_riogallegos", "78"),
    "Ushuaia": ("int_ushuaia", "94"), "Mar del Plata": ("int_mdp", "06"), "Bahía Blanca": ("int_bahia", "06"),
}
BLOQUE_FAM = {"Peronismo": "P", "Radicalismo": "I", "PRO": "T", "La Libertad Avanza": "T", "Provincial": "I"}
PARTIDO = {"Peronismo": "pj", "Radicalismo": "ucr", "PRO": "pro"}
# Intendentes del mismo frente que el gobernador (según el partido declarado en la fuente).
FRENTE_GOB = {"Viedma": "gob_rionegro", "San Juan": "gob_sanjuan", "Santiago del Estero": "zamora"}
for ciudad, (aid, prov) in CAPITALES.items():
    n, par, fam, ver, url, nota = INTENDENTES[ciudad]
    assert ver == "V" and url, ciudad
    capital = ciudad not in ("Mar del Plata", "Bahía Blanca")
    cargo = "intendente interino" if "interino" in nota else "intendente"
    ACTORES.append((aid, f"{n} ({cargo} de {ciudad})", "Líder político", ciudad, "M", BLOQUE_FAM.get(fam, "I"), 2,
                    S(ter=1, red=1, apo=1, coh=1, reg=1), "D", "", 2))
    FICHAS[aid] = dict(res=(f"Intendente de {ciudad}" + (", capital provincial" if capital else "") + f". Fuerza política: {par}." + (" " + nota if nota else "")),
                       manda=n + ".", fuentes=[("Intendente y partido", url)])
    if fam in PARTIDO:
        RELACIONES.append((aid, PARTIDO[fam], "Alianza", f"Intendente por {par}.", 1, url))
    if ciudad in FRENTE_GOB:
        RELACIONES.append((aid, FRENTE_GOB[ciudad], "Alianza", f"Integra el frente del gobierno provincial ({par}).", 2, url))

# --- Política y Justicia
HOYDIA_BORN = "https://hoydia.com.ar/politica/nacional/larina-milei-diputados-bornoroni-jefe-de-bloque/"
LETRAP_BORN = "https://www.letrap.com.ar/politica/el-crupier-cordobes-javier-milei-diputados-n5405859"
ROSENK_IP = "https://www.iprofesional.com/legales/457356-gobierno-javier-milei-quiere-reformar-proceso-para-nombrar-jueces-corte-suprema"
ROSENK_VICE = "https://www.sitioandino.com.ar/politica/horacio-rosatti-fue-reelegido-como-presidente-la-corte-suprema-n5684597"
ROSENK_PROY = "https://hoydia.com.ar/politica/nacional/la-corte-presenta-formalmente-su-proyecto-para-la-eleccion-de-nuevos-jueces/"
ISHII_LP = "https://www.letrap.com.ar/politica/buenos-aires-mario-ishii-eligio-una-sanitarista-su-reemplazo-y-congelo-la-pelea-la-sucesion-n5420710"
ISHII_LPO = "https://www.lapoliticaonline.com/conurbano/ishii-volvio-a-cruzar-a-kicillof-por-la-inseguridad-y-reclama-que-se-trate-su-proyecto/"
ACTORES += [
    ("bornoroni", "Gabriel Bornoroni (jefe del bloque de La Libertad Avanza en Diputados)", "Líder político", "Córdoba", "N", "T", 2,
     S(adq=1, pro=1, red=2, apo=1, coh=2, reg=1, pri=1), "D", "", 2),
    ("rosenkrantz", "Carlos Rosenkrantz (vicepresidente de la Corte Suprema)", "Justicia", CABA, "N", "I", 1,
     S(adq=1, pro=1, red=2, apo=1, coh=1, reg=2, pri=3), "D", "", 3),
    ("ishii", "Mario Ishii (senador bonaerense; intendente de José C. Paz con licencia)", "Líder político", "dep:06412", "P", "P", 1,
     S(ter=1, red=2, apo=1, coh=2, reg=1), "D", "", 2),
]
FICHAS.update({
    "bornoroni": dict(res="Diputado por Córdoba y dueño de estaciones de servicio; preside desde 2024 el bloque de La Libertad Avanza en Diputados, cargo en el que Karina Milei lo confirmó para el período que empezó en diciembre de 2025.",
                      manda="Gabriel Bornoroni.",
                      fuentes=[("Hoy Día Córdoba: Karina Milei confirmó a Bornoroni", HOYDIA_BORN), ("Letra P: perfil de Bornoroni", LETRAP_BORN)]),
    "rosenkrantz": dict(res="Juez de la Corte Suprema desde 2016 y su vicepresidente; la presidió entre 2018 y 2021. La Corte funciona con tres de sus cinco integrantes: Rosatti, Rosenkrantz y Lorenzetti.",
                        manda="Carlos Rosenkrantz.",
                        fuentes=[("iProfesional: la Corte con tres jueces", ROSENK_IP), ("Sitio Andino: Rosenkrantz sigue como vicepresidente", ROSENK_VICE)]),
    "ishii": dict(res="Intendente de José C. Paz desde 2015 (antes, entre 1999 y 2013). En diciembre de 2025 juró como senador bonaerense por Fuerza Patria y dejó a cargo a Lorena Espina; el tope a las reelecciones le impide volver a competir por la intendencia en 2027. Cuestiona al gobernador por la seguridad.",
                  manda="Mario Ishii.",
                  fuentes=[("Letra P: Ishii eligió a una sanitarista en su reemplazo", ISHII_LP), ("La Política Online: Ishii volvió a cruzar a Kicillof", ISHII_LPO)]),
})
RELACIONES += [
    ("bornoroni", "lla", "Alianza", "Preside el bloque de diputados del partido.", 3, HOYDIA_BORN),
    ("karina", "bornoroni", "Alianza", "Lo confirmó como jefe del bloque para el período iniciado en diciembre de 2025.", 2, HOYDIA_BORN),
    ("bornoroni", "m_menem", "Alianza", "Llegó a la jefatura del bloque en 2024 con el respaldo de Martín Menem y Karina Milei.", 2, "https://viapais.com.ar/politica/la-libertad-avanza-desplazo-al-jefe-del-bloque-de-diputados-asume-el-cordobes-bornoroni/"),
    ("rosenkrantz", "csjn", "Alianza", "Vicepresidente del tribunal, que funciona con tres jueces.", 3, ROSENK_VICE),
    ("rosenkrantz", "lorenzetti", "Alianza", "Firmaron juntos el proyecto de la Corte para seleccionar jueces (marzo de 2026).", 1, ROSENK_PROY),
    ("ishii", "int_jcpaz", "Alianza", "Eligió a Espina para reemplazarlo durante su licencia.", 3, ISHII_LP),
    ("ishii", "gob_pba", "Ambigua", "Del mismo frente, cuestiona a Kicillof por la seguridad y reclama que se trate su proyecto en la Legislatura.", 2, ISHII_LPO),
]

# --- Medios
TELEFE_LP = "https://www.letrap.com.ar/medios/gustavo-scaglione-cerro-paramount-y-entro-telefe-sociedad-manzano-n5419721"
TELEFE_EE = "https://eleconomista.com.ar/negocios/quien-nuevo-dueno-telefe-cuanto-pago-quedarse-canal-lider-n89794"
TELEFE_FB = "https://www.forbesargentina.com/negocios/quien-gustavo-scaglione-empresario-rosarino-compro-telefe-paramount-us-100-millones-n80323"
SCAG_LPO = "https://www.lapoliticaonline.com/medios/figoli-y-scaglione-pujan-por-la-compra-del-grupo-america/"
ACTORES += [
    ("scaglione", "Gustavo Scaglione (Televisión Litoral, Telefe y La Capital)", "Empresario", "Rosario", "N", "I", 1,
     S(din=1, mod=2, cul=1, red=2, coh=2), "D", "", 0),
    ("telefe", "Telefe (canal líder de la televisión abierta)", "Medio de comunicación", CABA, "N", "I", 2,
     S(cap=1, mod=2, cul=2, red=1, coh=2), "D", "scaglione", 0),
]
FICHAS.update({
    "scaglione": dict(res="Empresario rosarino, dueño de Televisión Litoral (Canal 3, Radio 2, Rosario3) y de La Capital. En octubre de 2025 compró Telefe a Paramount, con José Luis Manzano como socio en la operación, y sumó las señales de Telefe en Córdoba, Rosario y Santa Fe.",
                      manda="Gustavo Scaglione.",
                      fuentes=[("Letra P: Scaglione cerró con Paramount, en sociedad con Manzano", TELEFE_LP), ("El Economista: quién es el nuevo dueño de Telefe", TELEFE_EE),
                               ("La Política Online: el propietario de La Capital puja por el Grupo América", SCAG_LPO)]),
    "telefe": dict(res="El canal de televisión abierta más visto del país, con señales propias en Córdoba, Rosario y Santa Fe. Paramount lo vendió en octubre de 2025 al grupo de Gustavo Scaglione.",
                   manda="Gustavo Scaglione; Darío Turovelzky sigue como director ejecutivo.",
                   fuentes=[("Letra P: Scaglione entró a Telefe", TELEFE_LP), ("Forbes: la compra estructurada por Integra Capital, de Manzano", TELEFE_FB)]),
})
RELACIONES += [
    ("scaglione", "telefe", "Propiedad", "Lo compró a Paramount en octubre de 2025.", 3, TELEFE_LP),
    ("scaglione", "la_capital", "Propiedad", "Dueño del diario rosarino.", 3, SCAG_LPO),
    ("vila_manzano", "telefe", "Alianza", "Integra Capital, el fondo de Manzano, estructuró la compra y Manzano es socio en la operación.", 2, TELEFE_FB),
]

# --- Empresas que dominan ciudades del mapa
IPAUTOS = "https://www.iprofesional.com/autos/466280-que-marcas-y-modelos-de-autos-se-fabrican-en-argentina"
TOYOTA = "https://www.noticiasnqn.com.ar/noticias/2026/11/16/361038-toyota-fabricara-la-tacoma-hibrida-en-argentina-producira-50000-unidades"
FORD = "https://www.canal26.com/economia/2026/09/17/cae-la-produccion-desaparecen-modelos-y-crecen-las-importaciones-argentina-dejara-de-fabricar-autos/"
SIDERCA = "https://www.cronista.com/brand-strategy/la-empresa-argentina-que-empezo-como-un-sueno-y-hoy-es-la-principal-proveedora-del-sector-energetico-a-nivel-mundial/"
TENARIS_CEO = "https://www.infobae.com/economia/2026/05/06/tras-el-fuerte-cruce-con-milei-paolo-rocca-deja-de-ser-ceo-de-la-empresa-de-techint-que-fabrica-canos-petroleros/"
TERNIUM = "https://www.lacapital.com.ar/negocios/ternium-expoagro-la-apuesta-la-industria-que-impulsa-la-fuerza-del-campo-n10248412.html"
TERNIUM_RAM = "https://www.iprofesional.com/impuestos/443080-techint-tasa-municipal-ramallo-clausura-planta-y-juez-interviene"
ARAUCO = "https://www.iprofesional.com/negocios/467460-arauco-habilita-venta-de-activos-en-argentina-y-reordena-sus-negocios"
ARAUCO_EMP = "https://economis.com.ar/arauco-pone-en-marcha-una-nueva-planta-de-energia-renovable-en-misiones/"
TABACAL = "https://bichosdecampo.com/quien-es-seaboard-corporation-el-gigante-agroindustrial-de-estados-unidos-que-produce-azucar-bioetanol-y-energia-en-salta/"
SANCOR = "https://www.cadena3.com/noticia/sancor-seguros/sancor-seguros-celebra-sus-80-anos-alentando-un-nuevo-sueno-mundialista_559258"
BCR_PUERTOS = "https://bcr.com.ar/es/print/pdf/node/73051"
AGROEXP = "https://www.infocampo.com.ar/?p=594711"
CIARA_W = "https://es.wikipedia.org/wiki/C%C3%A1mara_de_la_Industria_Aceitera_de_la_Rep%C3%BAblica_Argentina"
VICENTIN_LR = "https://www.larepublica.co/globoeconomia/grassi-supera-el-obstaculo-para-adquirir-el-gigante-argentino-de-la-soja-en-dificultades-4295220"
ZIJIN = "https://www.infobae.com/economia/2026/07/29/el-gobierno-aprobo-un-nuevo-proyecto-rigi-que-invertira-usd-709-millones-para-producir-litio-en-catamarca/"
ZIJIN_MULTA = "https://www.iprofesional.com/negocios/453064-litio-toxico-minera-china-provoco-desastre-ambiental-en-argentina-y-afecto-a-un-pueblo"
GANFENG = "https://www.iprofesional.com/negocios/415286-litio-tras-la-fusion-de-rio-tinto-chinos-mueven-las-piezas-y-anticipan-mas-inversiones"
GANFENG_SALTA = "https://www.iprofesional.com/negocios/422902-argentina-consolida-su-liderazgo-en-litio-con-inauguracion-de-la-planta-de-ganfeng-lithium"
EXAR_JEMSE = "https://www.todojujuy.com/pais/litio-jujuy-salta-y-catamarca-cuales-son-los-proyectos-mas-importantes-esta-region-n286652"
MCEWEN = "https://www.mining-technology.com/news/argentina-approves-mcewens-2-7bn-copper-project-rigi/"
VELADERO = "https://mase.lmneuquen.com/mineria/argentina-uno-uno-los-proyectos-mineros-que-ya-estan-construccion-n1246226"
ADECO_BL = "https://www.bloomberglinea.com/latinoamerica/argentina/adecoagro-compro-el-50-de-profertil-y-sera-socio-de-ypf-que-tiene-la-otra-mitad/"
ADECO_YPF = "https://www.novacana.com/noticias/adecoagro-oferta-us-600-milhoes-ypf-50-restantes-empresa-argentina-profertil-021225"
ADECO_FIN = "https://www.barchart.com/story/news/36620209/adecoagro-completes-the-acquisition-of-profertil"
ACTORES += [
    ("toyota", "Toyota Argentina (planta de Zárate)", "Empresa industrial", "Zárate", "N", "X", 2,
     S(cap=2, prd=2, mov=1, gan=1, inn=1, mie=1, red=1, coh=2), "D", "", 0),
    ("ford", "Ford Argentina (planta de General Pacheco)", "Empresa industrial", "General Pacheco", "N", "X", 2,
     S(cap=2, prd=1, gan=1, inn=1, mie=1, red=1, coh=2), "D", "", 0),
    ("volkswagen", "Volkswagen Argentina (planta de General Pacheco)", "Empresa industrial", "General Pacheco", "N", "X", 2,
     S(cap=2, prd=1, inn=1, mie=1, red=1, coh=2), "D", "", 0),
    ("tenaris", "Tenaris Siderca (Techint, Campana)", "Empresa industrial", "Campana", "N", "T", 2,
     S(cap=2, prd=2, gan=2, inn=1, mie=1, red=1, coh=3), "D", "techint", 0),
    ("ternium", "Ternium Argentina (Techint, planta General Savio de San Nicolás)", "Empresa industrial", "San Nicolás de los Arroyos", "N", "T", 2,
     S(cap=2, prd=2, gan=1, inn=1, mie=1, red=1, coh=3), "D", "techint", 0),
    ("arauco", "Arauco Argentina (celulosa y madera en Misiones)", "Recursos primarios", "Puerto Piray", "R", "X", 2,
     S(rec=2, cap=2, prd=2, ter=1, mie=1, red=1, coh=2), "D", "", 0),
    ("tabacal", "Tabacal Agroindustria (Seaboard, ingenio de Orán)", "Recursos primarios", "San Ramón de la Nueva Orán", "P", "X", 2,
     S(rec=1, cap=1, prd=1, ter=1, mie=1, coh=2), "D", "", 0),
    ("sancor_seguros", "Grupo Sancor Seguros (Sunchales)", "Empresa financiera", "Sunchales", "N", "I", 1,
     S(din=2, gan=1, adq=1, mie=1, red=1, coh=2), "D", "", 0),
    ("ldc", "Louis Dreyfus Company (terminal de Timbúes)", "Recursos primarios", "Timbúes", "R", "X", 2,
     S(rec=1, cap=2, prd=2, mov=2, pro=1, red=1, coh=2), "D", "", 0),
    ("bunge", "Bunge (con Viterra; terminales de Puerto General San Martín)", "Recursos primarios", "Puerto General San Martín", "R", "X", 2,
     S(rec=1, cap=2, prd=2, mov=2, pro=1, red=1, coh=2), "D", "", 0),
    ("zijin", "Zijin-Liex (litio de Tres Quebradas, Fiambalá)", "Recursos primarios", "Fiambalá", "P", "E", 2,
     S(rec=2, cap=2, prd=1, ext=1, red=1), "D", "", 0),
    ("ganfeng", "Ganfeng Lithium (Minera Exar y proyectos en Salta)", "Recursos primarios", "Susques", "R", "E", 2,
     S(rec=2, cap=2, prd=2, red=1), "D", "", 0),
    ("mcewen", "McEwen Copper (Los Azules, Calingasta)", "Recursos primarios", "Calingasta", "P", "T", 2,
     S(rec=2, cap=1, red=1), "D", "", 0),
    ("barrick", "Barrick y Shandong Gold (Veladero)", "Recursos primarios", "San José de Jáchal", "P", "X", 2,
     S(rec=2, cap=2, prd=2, red=1), "D", "", 0),
    ("adecoagro", "Adecoagro (Tether) y Profertil", "Recursos primarios", "Bahía Blanca", "N", "X", 2,
     S(rec=2, cap=2, prd=2, din=1, red=1, coh=2), "D", "", 0),
]
FICHAS.update({
    "toyota": dict(res="Fabrica en Zárate desde 1997 (Hilux, SW4, Hiace) y es la automotriz que más produce y exporta del país; anunció la producción de la Tacoma híbrida.",
                   manda="Toyota Motor Corporation (Japón).", fuentes=[("Noticias NQN: Toyota fabricará la Tacoma híbrida en Zárate", TOYOTA), ("iProfesional: qué autos se fabrican en la Argentina", IPAUTOS)]),
    "ford": dict(res="Su planta de General Pacheco es su principal centro industrial del país; invirtió USD 700 millones para la nueva Ranger.",
                 manda="Ford Motor Company (EE.UU.).", fuentes=[("Canal 26: la producción automotriz en 2026", FORD)]),
    "volkswagen": dict(res="Produce la Amarok en General Pacheco.", manda="Grupo Volkswagen (Alemania).",
                       fuentes=[("iProfesional: qué autos se fabrican en la Argentina", IPAUTOS)]),
    "tenaris": dict(res="La planta de tubos sin costura de Campana, fundada en 1954, es la base argentina de Tenaris, líder mundial en caños para la industria petrolera. En mayo de 2026 Paolo Rocca dejó de ser su director ejecutivo (sigue como presidente) tras perder ante la india Welspun la provisión de caños para el gasoducto de GNL.",
                    manda="Grupo Techint (familia Rocca); director ejecutivo, Gabriel Podskubka.",
                    fuentes=[("El Cronista: 70 años de la planta de Campana", SIDERCA), ("Infobae: Rocca deja de ser CEO de Tenaris", TENARIS_CEO)]),
    "ternium": dict(res="Principal siderúrgica de aceros planos del país; su planta de San Nicolás produce unos 2,6 millones de toneladas de acero líquido al año y abastece a unas 900 pymes. Mantiene un conflicto judicial con el municipio de Ramallo por una tasa.",
                    manda="Grupo Techint (familia Rocca).",
                    fuentes=[("La Capital: Ternium en Expoagro", TERNIUM), ("iProfesional: la disputa con Ramallo", TERNIUM_RAM)]),
    "arauco": dict(res="El grupo chileno controla la mayor planta de celulosa del país (Puerto Esperanza) y el complejo de Puerto Piray; es el principal empleador privado de Misiones. En 2026 invierte unos USD 200 millones en modernización y habilitó la venta de parte de sus activos.",
                   manda="Arauco (grupo Angelini, Chile).", fuentes=[("iProfesional: Arauco reordena sus negocios", ARAUCO), ("Economis: principal empleador privado de Misiones", ARAUCO_EMP)]),
    "tabacal": dict(res="El ingenio San Martín del Tabacal, en Orán, produce azúcar, bioetanol y energía; pertenece a la estadounidense Seaboard Corporation, controlada por la familia Bresky.",
                    manda="Seaboard Corporation (EE.UU.).", fuentes=[("Bichos de Campo: quién es Seaboard", TABACAL)]),
    "sancor_seguros": dict(res="Nacida en 1945 como cooperativa en Sunchales, donde mantiene su casa central, es el primer grupo asegurador del país, con más del 12 % del mercado; tiene banco propio y opera en Uruguay, Paraguay, Brasil y Colombia.",
                           manda="Sancor Cooperativa de Seguros (presidente, Carlos Casto).", fuentes=[("Cadena 3: los 80 años de Sancor Seguros", SANCOR)]),
    "ldc": dict(res="Una de las cuatro mayores agroexportadoras del país, con complejo portuario e industrial en Timbúes. Compitió con Molinos Agro en el salvataje de Vicentin e impugnó el acuerdo de Grassi.",
                manda="Louis Dreyfus Company (Países Bajos, de origen francés).",
                fuentes=[("Infocampo: ranking de agroexportadoras", AGROEXP), ("BCR: terminales del Gran Rosario", BCR_PUERTOS), ("La República: las objeciones de Louis Dreyfus en Vicentin", VICENTIN_LR)]),
    "bunge": dict(res="Junto con Viterra, que absorbió, lidera la agroexportación desde las terminales del Gran Rosario (Pampa y Dempa, en Puerto General San Martín).",
                  manda="Bunge Global (EE.UU.).", fuentes=[("Infocampo: ranking de agroexportadoras", AGROEXP), ("BCR: terminales del Gran Rosario", BCR_PUERTOS)]),
    "zijin": dict(res="La minera china opera el proyecto de litio Tres Quebradas y su planta de carbonato en Fiambalá, aprobada en el RIGI. En marzo de 2026 un vuelco de salmuera cerca del pueblo terminó en una multa del Ministerio de Minería de Catamarca.",
                  manda="Zijin Mining (China).", fuentes=[("Infobae: proyectos de litio aprobados en el RIGI", ZIJIN), ("iProfesional: el vuelco de salmuera", ZIJIN_MULTA)]),
    "ganfeng": dict(res="Controla Minera Exar (Cauchari-Olaroz, 46,7 %) junto con Lithium Americas y la empresa jujeña JEMSE, e inauguró en Salta una planta de USD 980 millones (Mariana).",
                    manda="Ganfeng Lithium (China).", fuentes=[("iProfesional: litio tras la fusión de Rio Tinto", GANFENG), ("iProfesional: la planta de Ganfeng en Salta", GANFENG_SALTA)]),
    "mcewen": dict(res="La canadiense desarrolla Los Azules, proyecto de cobre de USD 2.700 millones en Calingasta aprobado en el RIGI; Rio Tinto, por su firma Nuton, tiene una participación.",
                   manda="McEwen Mining (Canadá).", fuentes=[("Mining Technology: Los Azules en el RIGI", MCEWEN)]),
    "barrick": dict(res="Barrick y Shandong Gold operan en sociedad la mina de oro Veladero, en el departamento Iglesia; su peso en el empleo y el uso del agua la ponen en el centro del debate en Jáchal.",
                    manda="Barrick (Canadá) y Shandong Gold (China), en partes iguales.", fuentes=[("LM Neuquén: los proyectos mineros en construcción", VELADERO)]),
    "adecoagro": dict(res="Agroindustrial de origen argentino controlada desde 2025 por Tether, la emisora de la stablecoin USDT. En diciembre de 2025 completó la compra de Profertil, la mayor productora de urea del país (planta en Bahía Blanca), con la ACA como socia minoritaria.",
                      manda="Tether (Juan Sartori preside el directorio; Mariano Bosch, director ejecutivo).",
                      fuentes=[("Bloomberg Línea: Adecoagro compró el 50 % de Profertil", ADECO_BL), ("Barchart: Adecoagro completa la compra de Profertil", ADECO_FIN)]),
})
RELACIONES += [
    ("techint", "tenaris", "Propiedad", "Empresa de tubos del grupo; Rocca sigue como presidente.", 3, TENARIS_CEO),
    ("techint", "ternium", "Propiedad", "Siderúrgica del grupo.", 3, "https://eleconomista.com.ar/negocios/lo-estan-haciendo-centro-utn-alumnos-secundaria-pasa-casi-ningun-lugar-pais-n94326"),
    ("tenaris", "welspun", "Enfrentamiento", "Welspun le ganó la provisión de 480 km de caños para el gasoducto de GNL con una oferta 25 % más baja.", 2, TENARIS_CEO),
    ("ldc", "ciara", "Alianza", "Socia de la cámara de aceiteras y exportadoras.", 2, CIARA_W),
    ("bunge", "ciara", "Alianza", "Socia de la cámara de aceiteras y exportadoras.", 2, CIARA_W),
    ("ldc", "agd", "Enfrentamiento", "Compitió por Vicentin y objetó el acuerdo de Grassi, ganador del salvataje.", 1, VICENTIN_LR),
    ("economia", "zijin", "Contrato", "Aprobó su proyecto de litio en el RIGI.", 2, ZIJIN),
    ("gob_catamarca", "zijin", "Enfrentamiento", "Multa del Ministerio de Minería por el vuelco de salmuera de marzo de 2026.", 1, ZIJIN_MULTA),
    ("ganfeng", "jemse", "Alianza", "Socias en Minera Exar (Cauchari-Olaroz).", 2, EXAR_JEMSE),
    ("economia", "mcewen", "Contrato", "Aprobó Los Azules en el RIGI.", 2, MCEWEN),
    ("tether", "adecoagro", "Propiedad", "Controla la empresa desde 2025, con alrededor del 70 % de las acciones.", 3, ADECO_BL),
    ("ypf", "adecoagro", "Contrato", "Le vendió su 50 % de Profertil, que Adecoagro completó en diciembre de 2025.", 2, ADECO_YPF),
]

# Relaciones para actores que estaban sin vínculos (corte del 20/11/2026)
SUR_BL = "https://www.bloomberglinea.com/latinoamerica/argentina/las-tres-empresas-detras-de-la-mega-inversion-de-data-centers-en-argentina-respaldada-por-openai/"
TOYOTA_FB = "https://www.forbesargentina.com/negocios/toyota-anuncio-mayor-inversion-historia-automotriz-argentina-fabricar-primera-pick-up-hibrida-n102678"
VELADERO_RIGI = "https://www.baenegocios.com/amp/aprueban-proyecto-minero-por-usd-380-millones-con-beneficios-del-rigi/"
VELADERO_ORR = "https://www.diariodecuyo.com.ar/politica/orrego-celebro-el-rigi-veladero-san-juan-sigue-consolidando-su-segunda-gran-etapa-minera-n6567032"
CONADI = "https://www.c5n.com/politica/abuelas-plaza-mayo-alerto-un-posible-desmantelamiento-la-conadi-clave-la-busqueda-nietos-n163530/amp"
RELACIONES += [
    ("satellogic", "sur_energy", "Alianza", "Emiliano Kargieman, fundador y CEO de Satellogic, cofundó y conduce Sur Energy, socia de OpenAI en Stargate Argentina.", 2, SUR_BL),
    ("sur_energy", "openai", "Contrato", "Carta de intención (octubre de 2025) para un centro de datos de hasta 500 MW y USD 25.000 millones; OpenAI sería compradora de la capacidad.", 2, SUR_BL),
    ("toyota", "milei", "Alianza", "Presentó en la Casa Rosada (16/11/2026) una inversión de USD 1.300 millones en Zárate dentro del RIGI.", 2, TOYOTA_FB),
    ("economia", "barrick", "Contrato", "Aprobó en el RIGI la ampliación de Veladero por USD 380 millones (Resolución 413/2026).", 2, VELADERO_RIGI),
    ("gob_sanjuan", "barrick", "Alianza", "Orrego celebró la aprobación del RIGI de Veladero.", 1, VELADERO_ORR),
    ("milei", "abuelas", "Enfrentamiento", "El Gobierno eliminó la unidad especial de la CONADI que investigaba la apropiación de niños; Abuelas lo denunció.", 2, CONADI),
]
