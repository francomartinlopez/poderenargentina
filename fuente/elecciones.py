# Elecciones de 2027 (corte del 20/11/2026).
# Presidenciales: 24 de octubre de 2027. Por provincia: fecha de la elección provincial si está fijada, si se separa
# de la nacional (S = desdobla, N = vota con la Nación, None = sin definir), qué se elige y la fuente.
# Se revisa en cada corte y después de cada convocatoria; solo fechas confirmadas por la provincia o por la prensa con fuente.

PRESIDENCIAL = ("2027-10-24", "https://www.c5n.com/politica/elecciones-2027-que-provincias-ya-confirmaron-el-desdoblamiento-sus-comicios-n254537")

C5N = "https://www.c5n.com/politica/elecciones-2027-que-provincias-ya-confirmaron-el-desdoblamiento-sus-comicios-n254537"
AMBITO = "https://www.ambito.com/politica/elecciones-2027-que-provincias-desdoblaran-sus-comicios-y-cuando-iran-las-urnas-n6345937"
EQS = "https://www.eqsnotas.com/politica/-elecciones-2027-provincias-desdoblamiento-paso-calendario_a6af99f63783432aefd46c322"
MIRADOR = "https://www.miradorprovincial.com/2026/11/12/calendario-electoral-2027-las-provincias-definen-fechas-de-votacion-a-la-espera-de-distritos-clave/"
UNO = "https://www.unoentrerios.com.ar/el-pais/elecciones-2027-que-provincias-desdoblaron-su-calendario-electoral-n10292136.html"

# id IGN: (fecha o None, desdobla, nota, fuente)
PROVINCIAS = {
    "58": ("2027-02-14", "S", "Gobernador, Legislatura y municipios. Abre el calendario.", C5N),
    "82": ("2027-06-13", "S", "Primarias el 18 de abril; gobernador, vice, Legislatura e intendentes.", AMBITO),
    "90": ("2027-05-09", "S", "Elecciones provinciales separadas de las nacionales.", C5N),
    "66": ("2027-05-16", "S", "Elecciones provinciales separadas de las nacionales.", AMBITO),
    "30": (None, "S", "Según trascendidos, Frigerio convocaría para el 6 de junio; sin confirmación oficial.", UNO),
    "54": (None, "S", "Passalacqua resolvió desdoblar; la fecha sería en abril o mayo.", MIRADOR),
    "18": (None, "S", "Desdobla, pero no elige gobernador: lo hizo en 2025.", MIRADOR),
    "26": (None, "S", "Torres anunció elecciones provinciales y municipales separadas.", EQS),
    "62": (None, "S", "Anunció el desdoblamiento; fecha sin fijar.", EQS),
    "22": (None, "S", "Anunció el desdoblamiento; fecha sin fijar.", EQS),
    "50": (None, "S", "Cornejo anticipó elecciones desdobladas; fecha sin fijar.", EQS),
    "38": (None, "S", "Anunció el desdoblamiento; fecha sin fijar.", EQS),
    "14": (None, None, "Se estima que separará su calendario; sin anuncio oficial.", UNO),
}
