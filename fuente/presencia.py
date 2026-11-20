# Presencia de actores fuera de la provincia de su sede (corte del 20/11/2026, pedido de Franco).
# Casi todos los actores nacionales tienen sede en CABA; la presencia dice dónde operan. El generador la arma de tres fuentes:
# 1) los puntos de fricción de fuente/friccion.py (cada actor que figura en un punto está presente en esa provincia);
# 2) las relaciones con actores provinciales o municipales (gobiernos, intendentes, empresas locales);
# 3) esta lista, para lo que no sale de lo anterior: una entrada por dato, con fuente.
# Los líderes políticos, partidos, gobiernos y organismos nacionales no reciben presencia derivada (estarían en todas partes);
# solo la que se cargue acá a mano.

EXCLUIDAS = {"Líder político", "Gobierno", "Partido en sistema competitivo", "Organismo de gobierno", "Banco central",
             "Ejército", "Servicio de inteligencia", "Fuerza de seguridad", "Justicia"}

PRESENCIA = {
    "pecom": [("26", "Opera Manantiales Behr y El Trébol–Escalante",
               "https://www.iprofesional.com/index.php/energia/448988-pecom-escala-su-produccion-de-crudo-y-se-mete-en-el-top5-de-las-mayores-petroleras"),
              ("42", "Opera El Corcobo, entre La Pampa y Mendoza",
               "https://eleconomista.com.ar/energia/mientras-ypf-concentra-vaca-muerta-pecom-acelera-su-expansion-toma-control-corcobo-n97206"),
              ("50", "Opera El Corcobo, entre La Pampa y Mendoza",
               "https://eleconomista.com.ar/energia/mientras-ypf-concentra-vaca-muerta-pecom-acelera-su-expansion-toma-control-corcobo-n97206")],
    "central_puerto": [("58", "Central hidroeléctrica Piedra del Águila",
                        "https://www.centralpuerto.com/wp-content/uploads/2026/03/20260304-4T25-ESP-Resultados-CEPU-1.pdf"),
                       ("18", "Campos forestales",
                        "https://www.iprofesional.com/negocios/453303-la-mayor-generadora-de-electricidad-busca-u$s70-millones-para-su-plan-de-expansion"),
                       ("30", "Campos forestales",
                        "https://www.iprofesional.com/negocios/453303-la-mayor-generadora-de-electricidad-busca-u$s70-millones-para-su-plan-de-expansion")],
    "tgs": [("58", "Gasoducto Perito Moreno desde Tratayén",
             "https://mase.lmneuquen.com/gas/tgs-presento-la-unica-oferta-la-licitacion-ampliar-el-gasoducto-perito-moreno-n1201663/amp"),
            ("06", "Gasoducto Perito Moreno hasta Salliqueló",
             "https://mase.lmneuquen.com/gas/tgs-presento-la-unica-oferta-la-licitacion-ampliar-el-gasoducto-perito-moreno-n1201663/amp")],
    "globant": [("94", "Oficina y convenio de capacitación con la provincia",
                 "https://www.iprofesional.com/management/340535-el-gobierno-firmo-un-acuerdo-con-globant-y-tierra-del-fuego"),
                ("22", "Oficina en el Parque Tecnológico de Chaco",
                 "https://mercado.com.ar/protagonistas/globant-anuncia-la-contrataciones-e-inversion-por-800-millones-en-chaco"),
                ("90", "Equipos que trabajan para clientes globales desde la provincia",
                 "https://www.lagaceta.com.ar/nota/1128974/economia/lejos-ser-amenaza-para-humanos-ia-sera-reinvencion-nuestro-trabajo-afirmo-ceo-globant.html")],
    "somu": [("26", "Paritaria de la flota langostinera (Puerto Madryn)",
              "https://cholilaonline.ar/2026/04/zapata-aseguro-no-estan-lejos-acuerdo-empresas-pesqueras.html")],
    "smata": [("06", "Plantas de Mirgor en Garín y Baradero",
               "https://www.mdzol.com/dinero/reforma-laboral-smata-y-mirgor-ponen-marcha-el-primer-banco-horas-n1539562")],
}
