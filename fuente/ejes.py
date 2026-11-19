# Ejes, categorías y fórmula del puntaje (paso 3, 19/11/2026).
# Mismo método que El mapa del poder global (podermundial): 21 ejes de 0 a 3, categoría teórica, autonomía real,
# red heredada y alcance. Diferencia de escala: aquí el 3 es dominio a escala nacional, no mundial.

# Orden de los 21 dígitos de cada actor en fuente/actores.py.
EJES = [
    ("rec", "Recursos naturales", "Materia", "Posesión o control directo de tierra, energía, minerales, agua o alimentos.",
     ("Controla un recurso estratégico a escala nacional (por ejemplo, la mayor parte de Vaca Muerta)", "Recursos de peso en una provincia grande o en un sector", "Recursos relevantes en lo local")),
    ("cap", "Capital físico", "Materia", "Propiedad de infraestructura, plantas, equipos, flotas o redes.",
     ("Infraestructura crítica a escala nacional", "Plantas o redes de primer orden en su sector", "Instalaciones relevantes")),
    ("prd", "Producción material", "Materia", "Volumen y peso estratégico de lo que fabrica o extrae.",
     ("Líder nacional en un bien estratégico", "Entre los primeros del país en su rubro", "Productor relevante")),
    ("mov", "Movilidad y transporte", "Materia", "Capacidad de mover o frenar bienes, personas o fuerzas.",
     ("Controla nodos logísticos nacionales (puertos, aeropuertos, cargas)", "Red propia de alcance nacional o regional", "Alcance local")),
    ("gan", "Generación de ganancia", "Dinero", "Flujo anual de excedente económico propio.",
     ("Entre las mayores ganancias del país", "Ganancias de primer orden en su sector", "Rentable")),
    ("din", "Dinero neto", "Dinero", "Stock de riqueza, activos administrados o capacidad de emitir.",
     ("Emisión de moneda o los mayores activos del país", "Activos de primer orden", "Activos relevantes")),
    ("coe", "Coerción violenta", "Fuerza", "Capacidad propia de usar o amenazar con violencia organizada.",
     ("Fuerza armada de alcance nacional", "Fuerza capaz de operar en varias provincias", "Capacidad armada local")),
    ("ter", "Dominio territorial", "Fuerza", "Control efectivo de un territorio y su población.",
     ("Gobierna el país", "Una provincia grande o varias provincias", "Una provincia chica, una ciudad o enclaves")),
    ("ext", "Acción fuera de la ley", "Fuerza", "Corrupción, crimen organizado u operaciones ilegales, solo con un hecho documentado por un tribunal u organismo oficial.",
     ("Crimen o corrupción a escala nacional, sostenidos, con impunidad de hecho", "Prácticas ilegales graves o repetidas establecidas por tribunales", "Un hecho ilegal documentado por un tribunal u organismo oficial")),
    ("adq", "Adquisición de información", "Información", "Capacidad de obtener datos, secretos o vigilancia.",
     ("Vigila u obtiene datos de buena parte de la población", "Alcance nacional en un sector", "Alcance limitado")),
    ("pro", "Procesamiento de información", "Información", "Capacidad de analizar y convertir datos en decisiones.",
     ("La mayor capacidad analítica del país", "Capacidad alta", "Capacidad relevante")),
    ("mod", "Moderación de información", "Información", "Poder de decidir qué circula, qué se amplifica y qué se calla.",
     ("Fija la agenda nacional", "Pesa en la agenda nacional o domina la de una provincia", "Pesa en un sector o en una región")),
    ("con", "Conocimiento", "Información", "Saber experto acumulado, técnico o institucional.",
     ("Referencia nacional en su campo", "Referencia sectorial", "Saber especializado")),
    ("inn", "Innovación", "Información", "Capacidad de crear tecnología, métodos o productos nuevos.",
     ("Innovación de frontera desde la Argentina", "Innova dentro de su sector", "Adopta y adapta")),
    ("mie", "Miembros humanos", "Personas", "Cantidad de personas que integran, obedecen o siguen a la organización.",
     ("Más de 1 M de integrantes, afiliados o fieles", "Más de 50.000", "Más de 5.000")),
    ("cul", "Influencia cultural", "Personas", "Capacidad de moldear ideas, creencias, gustos o identidades.",
     ("Moldea ideas o identidades a escala nacional", "En una región o en un sector amplio", "En un ámbito acotado")),
    ("red", "Contactos y relaciones", "Personas", "Densidad y altura de su red con otros centros de poder.",
     ("Acceso directo al presidente, a los gobernadores y a la cúpula económica", "Red de alto nivel sectorial o provincial", "Red relevante")),
    ("apo", "Apoyo popular", "Personas", "Respaldo o legitimidad pública: votos, aprobación, fieles o prestigio.",
     ("Respaldo de la mayoría del país", "Mayoría en su ámbito o una minoría nacional amplia", "Apoyo relevante pero minoritario")),
    ("coh", "Cohesión interna", "Personas", "Unidad de mando frente a facciones o pujas internas.",
     ("Mando único sin pujas visibles", "Pujas contenidas que no frenan sus decisiones", "Facciones abiertas que traban o dividen sus decisiones")),
    ("reg", "Regulación normativa", "Norma", "Capacidad de dictar o imponer reglas que otros deben cumplir.",
     ("Dicta normas para todo el país", "Regula una provincia o un sector entero", "Normas propias o locales")),
    ("pri", "Privilegio legal", "Norma", "Lo que la ley le permite y a otros no: inmunidad, veto, secreto, monopolio legal, uso legal de la fuerza.",
     ("Privilegios máximos en el país: emisión de moneda, veto o indulto, última palabra judicial", "Uso legal de la fuerza, secreto sin control externo o monopolio legal de un mercado nacional", "Concesiones o exenciones especiales")),
]

# Pesos fijos por eje (los mismos del mapa global; el resto vale 1).
PESOS = {"coe": 2, "adq": 2, "ext": 2, "red": 1.5, "pri": 1.5}
AUTONOMIA_REAL = 0.6

# Puntaje teórico de cada categoría (0 a 10), copiado del mapa global (fuente/categorias.py).
TEORICO = {
    "Servicio de inteligencia": 9, "Ejército": 8, "Fuerza de seguridad": 7, "Gobierno": 6, "Banco central": 6,
    "Justicia": 5, "Partido en sistema competitivo": 5, "Organismo de gobierno": 6,
    "Empresa financiera": 7, "Familia y oficina patrimonial": 7, "Empresa tecnológica": 7, "Recursos primarios": 6,
    "Empresa industrial": 5, "Logística y transporte": 4,
    "Líder político": 8, "Empresario": 6,
    "Organización criminal": 8,
    "Organización religiosa": 5, "Federación empresaria": 5, "ONG, fundación o think tank": 4, "Organización deportiva": 4, "Sindicato": 4,
    "Medio de comunicación": 4,
}
TIPO = {
    "Servicio de inteligencia": "Estado", "Ejército": "Estado", "Fuerza de seguridad": "Estado", "Gobierno": "Estado",
    "Banco central": "Estado", "Justicia": "Estado", "Partido en sistema competitivo": "Estado", "Organismo de gobierno": "Estado",
    "Empresa financiera": "Capital", "Familia y oficina patrimonial": "Capital", "Empresa tecnológica": "Capital",
    "Recursos primarios": "Capital", "Empresa industrial": "Capital", "Logística y transporte": "Capital",
    "Líder político": "Persona", "Empresario": "Persona", "Organización criminal": "Sombra",
    "Organización religiosa": "Influencia", "Federación empresaria": "Influencia", "ONG, fundación o think tank": "Influencia",
    "Organización deportiva": "Influencia", "Sindicato": "Influencia", "Medio de comunicación": "Información",
}

# Puntaje final: media geométrica ponderada (categoría teórica 40 %, capacidad 30 %, alcance 20 %, autonomía 5 %, red 5 %),
# elevada a 3 antes de llevar el mayor a 100.
PESO_FINAL = {"ct": .40, "cap": .30, "alc": .20, "aut": .05, "red": .05}
ESTIRAR = 3

# Alcance efectivo dentro del país: N nacional, R varias provincias, P una provincia, M un municipio.
ALCANCE = {"N": (.60, "Nacional"), "R": (.25, "Regional (varias provincias)"), "P": (.15, "Provincial"), "M": (.10, "Municipal")}

AUTONOMIA = {1: "Decide solo", 2: "Aliado con criterio propio", 3: "Subordinado", 4: "Fachada"}
CERTEZA = {"D": "Documentado", "E": "Estimado"}
BLOQUES = {"T": "Transoceánico", "E": "Euroasiático", "I": "Independiente", "P": "Pendular", "X": "Transnacional"}
TIPOS_REL = ["Gobierna", "Propiedad", "Financiamiento", "Alianza", "Enfrentamiento", "Ambigua", "Contrato", "Abastecimiento", "Puerta giratoria"]
# Relaciones que cuentan para el puntaje real de categoría (informativo).
PESO_REL = {"Gobierna": 1, "Propiedad": 1, "Financiamiento": 1, "Abastecimiento": .5, "Puerta giratoria": .5}

# Actores del mapa global con los que se cruzan relaciones (no se puntúan aquí; enlazan a podermundial).
GLOBAL_URL = "https://francomartinlopez.github.io/podermundial/"
EXTERNOS = {
    "fmi": "Fondo Monetario Internacional", "tesoro_eeuu": "Tesoro de EE.UU.", "casablanca": "Casa Blanca (EE.UU.)",
    "pboc": "Banco Popular de China", "cia": "CIA", "santasede": "Santa Sede", "fifa": "FIFA",
}
