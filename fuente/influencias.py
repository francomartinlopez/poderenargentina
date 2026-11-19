# Influencias mundiales por territorio (paso 2, todavía sin cargar).
# Cada potencia se puntúa de 0 a 3 en cinco canales, con fuente obligatoria.
# Territorio: "AR" (país), id IGN de provincia ("82"), de departamento ("82084") o slug de ciudad ("c:rosario").

POTENCIAS = ["EE.UU.", "China", "Unión Europea", "Reino Unido", "Brasil", "Rusia", "Israel", "Golfo",
             "Canadá y Australia", "Japón y Corea", "FMI, BM y BID"]
CANALES = {
    "com": "Comercio: destino de las exportaciones (INDEC, origen provincial de las exportaciones).",
    "inv": "Inversión: proyectos y dueños extranjeros (RIGI, minería, energía, puertos, tierras).",
    "deu": "Deuda: acreedores y ley de emisión de los bonos.",
    "pre": "Presencia física o de seguridad: bases, estaciones, cooperación militar y policial, agencias.",
    "pol": "Influencia política y cultural: acuerdos, financiamiento, diásporas, iglesias, medios.",
}
# (territorio, potencia, canal, intensidad 0-3, descripción, fuente URL)
INFLUENCIAS = [
]
