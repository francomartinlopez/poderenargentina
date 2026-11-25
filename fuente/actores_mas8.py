# Octava tanda de actores (25/11/2026, pedido de Franco: más actores y división por bloque internacional).
# CLTC (estación china de Neuquén), Edesur (Enel), El Tribuno (Salta) y Fundar. Mismo formato que fuente/actores_mas.py.
# El bloque de cada uno se explica en fuente/bloques.py (MOTIVOS).
# Resguardos: de las personas vivas, solo cargos, hechos públicos y lo que estableció un tribunal u organismo oficial.

from actores_mas import S, CABA

ACTORES = [
    ("cltc", "CLTC (agencia china de seguimiento satelital, Estación de Espacio Lejano)", "Organismo de gobierno",
     "Estación de Espacio Lejano (Quintuco)", "P", "E", 2, S(cap=1, inn=2, red=1, pri=1), "D", "", 2),
    ("edesur", "Edesur (distribuidora eléctrica, grupo Enel)", "Recursos primarios", CABA, "R", "T", 2,
     S(cap=2, prd=1, red=1, reg=1), "D", "", 1),
    ("el_tribuno", "El Tribuno (Horizontes S.A., familia Romero)", "Medio de comunicación", "Salta", "P", "I", 1,
     S(mod=1, cul=1, red=1), "D", "", 0),
    ("fundar", "Fundar (think tank de políticas públicas)", "ONG, fundación o think tank", CABA, "N", "I", 1,
     S(cul=1, red=1, apo=1), "D", "", 0),
]

CLTC_CRONISTA = "https://www.cronista.com/economia-politica/los-secretos-en-torno-a-la-base-china-en-argentina-que-generan-tension-con-eeuu"
CHEQUEADO_CLTC = "https://chequeado.com/el-explicador/que-se-sabe-sobre-la-base-espacial-china-ubicada-en-neuquen/"

FICHAS = {
    "cltc": dict(res="Agencia estatal china que opera la Estación de Espacio Lejano de Bajada del Agrio (Neuquén), en un predio de 200 hectáreas cedido por 50 años según acuerdos de 2012 y 2014 con la CONAE y la provincia. Da soporte de telemetría y control al programa lunar chino; depende del Ejército Popular de Liberación, y EE.UU. objeta su posible uso dual.",
                 manda="El Estado chino.",
                 fuentes=[("Chequeado: qué se sabe de la base", CHEQUEADO_CLTC),
                          ("El Cronista: la dependencia del Ejército chino", CLTC_CRONISTA),
                          ("Argentina.gob.ar: la estación CLTC-CONAE-Neuquén", "https://www.argentina.gob.ar/node/375905")]),
    "edesur": dict(res="Distribuidora eléctrica del sur del AMBA, con más de 2,5 millones de usuarios, controlada por el grupo italiano Enel. Enel la puso en venta en 2022 y en 2024 le confirmó al Gobierno que se queda en el país, mientras vendía sus centrales Costanera y Dock Sud.",
                   manda="El grupo Enel.",
                   fuentes=[("iProfesional: Enel suspende la venta de Edesur", "https://www.iprofesional.com/negocios/402320-la-italiana-enel-suspendio-la-venta-de-edesur-que-pasara-con-la-distribuidora"),
                            ("El Cronista: Enel vende Costanera y Dock Sud", "https://www.cronista.com/negocios/la-duena-de-edesur-inicia-su-salida-de-la-argentina-con-una-venta-de-mas-de-us-100-millones")]),
    "el_tribuno": dict(res="Principal diario de Salta, con edición en Jujuy, fundado en 1949 por Roberto Romero. Lo publica Horizontes S.A., de la familia del exgobernador y exsenador Juan Carlos Romero; en 2024 la empresa inició un procedimiento preventivo de crisis.",
                       manda="La familia Romero.",
                       fuentes=[("Letra P: el procedimiento de crisis de Horizontes", "https://www.letrap.com.ar/medios/salta-juan-carlos-romero-pone-sus-medios-al-borde-la-quiebra-evadir-obligaciones-laborales-n5407765"),
                                ("El Tribuno (Wikipedia)", "https://en.wikipedia.org/wiki/El_Tribuno")]),
    "fundar": dict(res="Centro de estudios de políticas públicas fundado en 2020 por Sebastián Ceria, que lo preside; su director ejecutivo es Martín Reydó. Trabaja en desarrollo productivo, minería, energía, inteligencia artificial y Estado; en 2026 cuestionó el Súper RIGI por no exigir empleo, proveedores locales ni divisas.",
                   manda="Sebastián Ceria (presidente).",
                   fuentes=[("Fundar: quiénes somos", "https://fund.ar/en/about-fundar/"),
                            ("El Economista: Fundar y el Súper RIGI", "https://eleconomista.com.ar/economia/fundar-cuestiona-super-rigi-que-gana-argentina-n95844")]),
}

RELACIONES = [
    ("embajada_china", "cltc", "Alianza", "La agencia depende del Estado chino; la embajada defendió la estación como civil.", 2, CLTC_CRONISTA),
    ("gob_neuquen", "cltc", "Contrato", "Firmó con la CLTC y la CONAE el acuerdo que cede el predio por 50 años.", 2, CHEQUEADO_CLTC),
    ("embajada_eeuu", "cltc", "Enfrentamiento", "EE.UU. objeta que fuerzas armadas chinas operen la estación de Neuquén.", 2,
     "https://www.iprofesional.com/actualidad/403170-ee-uu-critico-la-base-china-en-neuquen-y-el-gobierno-le-respondio"),
    ("economia", "edesur", "Contrato", "Concesionaria nacional de la distribución eléctrica; Enel le confirmó al Gobierno que se queda.", 2,
     "https://www.iprofesional.com/negocios/402320-la-italiana-enel-suspendio-la-venta-de-edesur-que-pasara-con-la-distribuidora"),
    ("el_tribuno", "gob_salta", "Ambigua", "Tirantez entre la familia Romero, dueña del diario, y el gobernador Sáenz.", 1,
     "https://www.letrap.com.ar/politica/salta-juan-carlos-romero-apuesta-un-triunfo-libertario-ahuyentar-el-fin-ciclo-n5418572/amp"),
    ("fundar", "economia", "Ambigua", "Cuestionó el Súper RIGI impulsado por el Gobierno.", 1,
     "https://eleconomista.com.ar/economia/fundar-cuestiona-super-rigi-que-gana-argentina-n95844"),
]
