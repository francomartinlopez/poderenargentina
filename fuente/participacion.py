# Participación electoral en las elecciones nacionales, 1946–2025 (serie armada por Franco, 27/11/2026).
# Por elección: etiqueta, tipo, % del padrón que votó y % del padrón que votó por algún candidato
# (participación × (1 − blanco y nulo)). Tipos: P presidencial (1.ª vuelta), B balotaje, L legislativa de medio
# término, PP primaria presidencial, PL primaria legislativa. Las legislativas que coinciden con una presidencial
# no van aparte. Se agrega cada elección nacional nueva en el corte siguiente.

TIPOS = {"P": "Presidencial", "B": "Balotaje", "L": "Legislativa", "PP": "PASO presidencial", "PL": "PASO legislativa"}

SERIE = [
    ("1946", "P", 81.2, 79.2), ("1951", "P", 88.0, 86.6), ("1954", "L", 86.0, 84.3), ("1958", "P", 90.9, 82.5),
    ("1960", "L", 86.9, 65.0), ("1962", "L", 85.7, 82.6), ("1963", "P", 85.5, 67.3), ("1965", "L", 83.5, 80.0),
    ("1973", "P", 85.9, 83.6), ("1973 sep", "P", 85.5, 84.4), ("1983", "P", 85.6, 83.2), ("1985", "L", 83.8, 82.1),
    ("1987", "L", 84.7, 80.2), ("1989", "P", 85.3, 83.6), ("1991", "L", 79.9, 73.7), ("1993", "L", 79.7, 74.2),
    ("1995", "P", 82.1, 78.6), ("1997", "L", 78.2, 73.4), ("1999", "P", 82.3, 78.6), ("2001", "L", 75.5, 59.6),
    ("2003", "P", 78.2, 76.1), ("2005", "L", 73.3, 66.0), ("2007", "P", 76.2, 70.4), ("2009", "L", 73.3, 69.7),
    ("2011 PASO", "PP", 78.7, 75.0), ("2011", "P", 79.4, 75.8), ("2013 PASO", "PL", 77.4, 73.3), ("2013", "L", 77.6, 74.1),
    ("2015 PASO", "PP", 74.9, 70.3), ("2015", "P", 81.1, 78.4), ("2015 balotaje", "B", 80.8, 78.8),
    ("2017 PASO", "PL", 75.0, 70.7), ("2017", "L", 77.6, 74.4), ("2019 PASO", "PP", 76.4, 73.1), ("2019", "P", 80.4, 78.4),
    ("2021 PASO", "PL", 67.8, 63.5), ("2021", "L", 71.6, 68.0), ("2023 PASO", "PP", 69.0, 64.8), ("2023", "P", 77.0, 74.6),
    ("2023 balotaje", "B", 76.4, 73.9), ("2025", "L", 67.9, 64.4),
]

NOTAS = {
    "1958": "Peronismo proscripto. Perón ordenó votar a Frondizi, pero una parte votó en blanco (9 %).",
    "1960": "Peronismo proscripto, que votó en blanco por orden de Perón (25 %). Es el máximo de la serie.",
    "1963": "Peronismo proscripto otra vez y nuevo llamado a votar en blanco (21 %). Illia ganó con cerca de un cuarto de los votos.",
    "2001": "El «voto bronca», meses antes del estallido de diciembre (21 % de blanco y nulo).",
    "2005": "Legislativa poscrisis, con 10 % de votos en blanco y nulos.",
    "2007": "Récord de voto en blanco en presidenciales desde 1983 (6,4 %).",
    "2025": "La participación más baja de las elecciones generales desde 1946 (67,9 %), la primera con Boleta Única Papel y sin primarias. Con 5,2 % de blanco y nulo, el voto por algún candidato (64,4 % del padrón) fue el segundo más bajo de las generales, después de 2001. Solo la primaria de 2021 quedó apenas por debajo.",
}

SALVEDADES = ("Hasta 1946 solo votaban varones; 1951 fue la primera elección con voto femenino. Falta la legislativa de 1948 (sin dato confiable). "
              "En 1991 se usa el 79,9 % de Tula y otros en lugar del 89,7 % del IDEA. En 2003 no hubo balotaje y en 2025 no hubo primarias. "
              "El blanco y nulo de las primarias de 2011 y 2019 es una estimación propia y el de 2017 sale del escrutinio provisorio; "
              "las cifras de participación de las primarias varían entre fuentes.")

FUENTES = [
    ("IDEA Internacional, Voter Turnout Database: Argentina (1946–1973 y blanco y nulo de las generales)", "https://www.idea.int/data-tools/country-view/51/40"),
    ("Chequeado: participación 1983–2023 y presidenciales de 2023", "https://chequeado.com/el-explicador/elecciones-2023-la-participacion-fue-de-al-menos-el-74-la-mas-baja-en-una-eleccion-presidencial-desde-1983/"),
    ("Chequeado: legislativas de 2025", "https://chequeado.com/nota/la-participacion-electoral-de-este-domingo-fue-la-mas-baja-desde-1983"),
    ("Directorio Legislativo: informe poselectoral 2025 (blanco 2,74 % y nulo 2,46 %)", "https://directoriolegislativo.org/"),
    ("Participación histórica en las PASO (iProfesional, 2023)", "https://www.iprofesional.com/politica/386912-la-segunda-participacion-mas-baja-desde-que-se-votan-primarias"),
]
