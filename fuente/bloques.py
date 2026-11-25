"""Inclinación internacional de los actores: hacia qué bloque del mapa global se inclina cada uno.

Bloques (los del mapa global): T Transoceánico (EE.UU. y sus aliados), E Euroasiático (China y Rusia),
P Pendular (acuerdos de peso con los dos), I Independiente (sin inclinación documentada hacia ninguno),
X Transnacional (redes que operan por encima de los Estados: crimen organizado, comercializadoras globales, religiones).

Regla (25/11/2026, pedido de Franco):
1. Un actor que también está en el mapa global lleva el bloque que tiene allá (GLOBAL; el generador lo controla).
2. Filiales de empresas extranjeras y representaciones de Estados: el bloque del país del capital o del Estado.
3. Actores políticos, sociales y económicos argentinos: el bloque hacia el que muestran acuerdos, alianzas o posiciones
   documentadas (con fuente en MOTIVOS o en sus relaciones con actores del mapa global). Sin eso, I.
El bloque no es un juicio: registra con quién tiene vínculos de peso cada actor. Mismo trato para oficialismo y oposición.
"""

GLOBAL_URL = "https://francomartinlopez.github.io/podermundial/#o-"

# Mismo id y misma entidad en el mapa global → mismo bloque. (bcr y cac son otras entidades en el mapa global: no cuentan.)
GLOBAL = {
    "milei": "T", "techint": "T", "ypf": "T", "side": "T", "clarin": "T", "ciara": "X", "bcra": "T", "eurnekian": "X",
    "cgt_arg": "P", "bulgheroni": "T", "aea": "T", "toyota": "T", "icbc": "E", "bbva": "T", "santander": "T", "cofco": "E",
    "cargill": "T", "chevron": "T", "bunge": "T", "los_monos": "X", "riotinto": "T", "zijin": "E",
}

# Bloque de los actores externos (EXTERNOS de actores.py) para leer las relaciones de cada actor argentino con potencias.
EXT_BLOQUE = {
    "fmi": "T", "tesoro_eeuu": "T", "casablanca": "T", "pboc": "E", "cia": "T", "santasede": "X", "fifa": "X", "pentagono": "T",
    "jpmorgan": "T", "blackrock": "T", "openai": "T", "glencore": "X", "spacex": "T", "shell": "T", "bp": "T", "totalenergies": "T",
    "bhp": "T", "bm": "T", "eni": "T", "doj": "T", "huawei": "E", "icbc_china": "E", "burford": "T", "navitas": "T",
    "rockhopper": "T", "gezhouba": "E", "welspun": "I", "tether": "X", "ustr": "T", "cnooc": "E", "sur_energy": "T",
    "america_movil": "I", "copec": "T", "moolec": "T", "seaboard": "T",
}

# Por qué: (bloque, motivo en una línea, fuente). Si el bloque difiere del cargado en la tanda, este manda.
MOTIVOS = {
    # Euroasiático
    "embajada_china": ("E", "Representa a la República Popular China.", None),
    "embajada_rusia": ("E", "Representa a la Federación de Rusia.", None),
    "icbc": ("E", "Filial del banco estatal chino ICBC; también figura así en el mapa global.", None),
    "ganfeng": ("E", "Capital chino: la controla Ganfeng Lithium.", None),
    "zijin": ("E", "Capital chino: la controla Zijin Mining; también figura así en el mapa global.", None),
    "cofco": ("E", "Capital estatal chino; también figura así en el mapa global.", None),
    "cltc": ("E", "Agencia del Estado chino dependiente del Ejército Popular de Liberación.",
             "https://www.cronista.com/economia-politica/los-secretos-en-torno-a-la-base-china-en-argentina-que-generan-tension-con-eeuu"),
    # Transoceánico
    "faro": ("T", "Coorganiza eventos de la CPAC y vínculos con el gobierno de Orbán; Laje expone en la CPAC desde 2021.",
             "https://chequeado.com/nota/milei-viaja-a-hungria-para-la-cpac-que-se-sabe-sobre-los-vinculos-de-fundacion-faro-con-el-gobierno-de-orban"),
    "milei": ("T", "Alineamiento explícito con EE.UU. e Israel; acuerdo con el Tesoro de EE.UU. Así figura en el mapa global.", None),
    "embajada_eeuu": ("T", "Representa a EE.UU.", None),
    "embajada_israel": ("T", "Representa a Israel.", None),
    "embajada_ru": ("T", "Representa al Reino Unido.", None),
    "embajada_espana": ("T", "Representa a España, miembro de la OTAN y la Unión Europea.", None),
    "edesur": ("T", "Capital italiano: la controla el grupo Enel.",
               "https://www.iprofesional.com/negocios/402320-la-italiana-enel-suspendio-la-venta-de-edesur-que-pasara-con-la-distribuidora"),
    "la_voz": ("T", "Lleva el bloque del Grupo Clarín, que la controla.",
               "https://argentina.mom-rsf.org/en/media/detail/outlet/la-voz-del-interior/"),
    # Pendular
    "cgt_arg": ("P", "Así figura en el mapa global.", None),
    # Transnacional (mapa global)
    "eurnekian": ("X", "Corporación América opera aeropuertos en varios continentes; así figura en el mapa global.", None),
    "los_monos": ("X", "Red criminal con conexiones fuera del país; así figura en el mapa global.", None),
    # Independiente
    "embajada_brasil": ("I", "Brasil figura como independiente en el mapa global.", None),
    "claro": ("I", "Capital mexicano (América Móvil); México no integra ninguno de los dos bloques en el mapa global.", None),
}

# Decisión de Franco (25/11/2026): queda como está. Los dirigentes, sindicatos e intendentes peronistas siguen como
# pendulares por su partido; los gobernadores, según su propia posición (varios peronistas, independientes). No se unifica.
