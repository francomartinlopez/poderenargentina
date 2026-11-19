"""Puntos de fricción y zonas liberadas (paso 5).

Punto de fricción: un lugar donde dos o más actores del mapa, o una potencia y el
Estado argentino, disputan el control de un recurso, un territorio o una regla.
Cada punto lleva actores (ids del mapa o EXTERNOS), potencias de influencias.py,
hitos fechados y al menos una fuente por hito.

Intensidad:
  3 = hay violencia, enfrentamientos con fuerzas de seguridad o presencia militar extranjera
  2 = disputa abierta (judicial, diplomática, licitatoria o política)
  1 = disputa latente o localizada

Zonas liberadas: solo las que un organismo oficial describió como fuera del control
del Estado, o donde la autoridad documentó pasos o circuitos ilegales operando a la
vista. Sin fuente oficial o periodística que lo establezca, no entra. Se dice el
estado actual (si el Estado recuperó el control, se registra).
Sin nombres de personas vivas vinculadas a delitos salvo condena firme.
"""

W = "https://es.wikipedia.org/wiki/"

# (id, nombre, tipo, provincia, ciudad (slug o None), lon, lat, intensidad, estado,
#  actores, potencias, texto, hitos [(AAAA-MM, texto, url)], fuentes [(título, url)])
FRICCION = [
    ("malvinas", "Islas Malvinas", "Soberanía", "94", None, -59.0, -51.7, 3, "Activa",
     ["milei", "ffaa"], ["Reino Unido"],
     "La Argentina reclama la soberanía de las islas, ocupadas por el Reino Unido desde 1833, que mantiene una guarnición permanente en Monte Agradable. El reclamo es política de Estado y figura en la Constitución.",
     [("1833-01", "El Reino Unido ocupa las islas.", W + "Cuesti%C3%B3n_de_las_islas_Malvinas"),
      ("1982-04", "Guerra de Malvinas; la Argentina se rinde el 14 de junio.", W + "Guerra_de_las_Malvinas"),
      ("2025-06", "El Reino Unido ratifica su presencia militar en las islas.", "https://www.baenegocios.com/mundo/Reino-Unido-ratifica-la-presencia-militar-en-las-Malvinas-tras-las-crecientes-amenazas-20250624-0075.html"),
      ("2026-01", "Despliegue de cazas Eurofighter en las islas.", "https://www.canal26.com/internacionales/2026/01/22/el-reino-unido-desafia-a-argentina-reafirma-la-defensa-de-su-soberania-en-las-islas-malvinas-al-desplegar-cazas-eurofighter/")],
     [("Cuestión de las islas Malvinas (Wikipedia)", W + "Cuesti%C3%B3n_de_las_islas_Malvinas")]),

    ("estacion_china", "Estación de Espacio Lejano (Neuquén)", "Geopolítica", "58", "estacion-de-espacio-lejano-quintuco", -70.1495, -38.1914, 2, "Activa",
     ["milei", "gob_neuquen", "ffaa"], ["China", "EE.UU."],
     "Estación de seguimiento espacial operada por la agencia china CLTC, dependiente del Ejército Popular de Liberación, en un predio cedido por 50 años. EE.UU. objeta su posible uso militar y el Gobierno nacional evaluó pedir una inspección técnica.",
     [("2014-04", "Acuerdo entre la Argentina y China para instalar la estación, con cesión del predio por 50 años.", "https://chequeado.com/el-explicador/que-se-sabe-sobre-la-base-espacial-china-ubicada-en-neuquen/"),
      ("2026", "El Gobierno analiza pedir una inspección técnica de la base.", "https://www.a24.com/politica/el-gobierno-analiza-pedir-una-inspeccion-tecnica-la-base-espacial-china-neuquen-n1308479/amp")],
     [("Chequeado: qué se sabe de la base", "https://chequeado.com/el-explicador/que-se-sabe-sobre-la-base-espacial-china-ubicada-en-neuquen/"),
      ("A24: inspección técnica", "https://www.a24.com/politica/el-gobierno-analiza-pedir-una-inspeccion-tecnica-la-base-espacial-china-neuquen-n1308479/amp")]),

    ("hidrovia", "Hidrovía Paraná-Paraguay", "Geopolítica", "82", "rosario", -60.45, -33.25, 2, "Adjudicada; con reclamos",
     ["milei", "economia", "gob_santafe", "ciara"], ["EE.UU.", "China", "Unión Europea"],
     "Por el Paraná sale la mayor parte de las exportaciones argentinas. La licitación del dragado excluyó a empresas controladas por Estados, lo que dejó fuera a la china CCCC. La ganó la belga Jan De Nul con la argentina Servimagnus; la competidora DEME, con socios estadounidenses, denunció sesgo ante el gobierno de EE.UU.",
     [("2025-02", "El Gobierno anula la primera licitación, con una sola oferta.", "https://elheraldo.com.ar/noticias/interes-general/el-estado-nacional-anulo-la-licitacion-de-la-hidrovia"),
      ("2026-06", "Preadjudicación a Jan De Nul (66,20 puntos) frente a DEME (42,14).", "https://www.lacapital.com.ar/economia/la-licitacion-la-hidrovia-entro-la-recta-final-y-se-anuncio-la-preadjudicacion-n10262951.html/amp"),
      ("2026-07", "Jan De Nul afirma que no habrá participación china; el congresista Brian Mast había alertado al Departamento de Estado.", "https://www.lapoliticaonline.com/santa-fe/jan-de-nul-se-reunio-con-el-embajador-de-estados-unidos-y-niega-vinculos-con-china/"),
      ("2026", "Adjudicación a Jan De Nul y Servimagnus por 25 años.", "https://www.lacapitalmdp.com/el-gobierno-adjudico-a-jan-de-nul-la-concesion-de-la-hidrovia-parana-paraguay-por-25-anos/")],
     [("Bloomberg Línea: exclusión de empresas estatales", "https://www.bloomberglinea.com/latinoamerica/argentina/hidrovia-megalicitacion-por-negocio-de-us300m-entra-en-recta-final-entre-tensiones-geopoliticas/"),
      ("El Economista: la privatización ya tiene dueño", "https://eleconomista.com.ar/economia/la-privatizacion-mas-grande-era-milei-ya-tiene-dueno-cambia-ahora-hidrovia-n95924")]),

    ("ushuaia_base", "Base Naval Integrada de Ushuaia", "Geopolítica", "94", "ushuaia", -68.3038, -54.8074, 2, "En obra",
     ["milei", "ffaa", "gob_tdf"], ["EE.UU.", "China", "Reino Unido"],
     "Base proyectada sobre el canal Beagle como puerta a la Antártida. El Gobierno busca financiamiento y participación de EE.UU.; antes, una propuesta de polo logístico con fondos chinos había quedado sin avanzar.",
     [("2024-04", "Milei anuncia en Ushuaia, con la jefa del Comando Sur, que la base será un proyecto conjunto con EE.UU.", "https://www.perfil.com/noticias/politica/la-base-naval-integrada-de-ushuaia-el-proyecto-que-defensa-impulsa-desde-hace-decadas-y-que-milei-busca-reactivar.phtml"),
      ("2026-09", "Defensa reactiva el proyecto.", "https://www.perfil.com/noticias/politica/la-base-naval-integrada-de-ushuaia-el-proyecto-que-defensa-impulsa-desde-hace-decadas-y-que-milei-busca-reactivar.phtml")],
     [("Perfil: la Base Naval Integrada", "https://www.perfil.com/noticias/politica/la-base-naval-integrada-de-ushuaia-el-proyecto-que-defensa-impulsa-desde-hace-decadas-y-que-milei-busca-reactivar.phtml"),
      ("Base Naval Ushuaia (Wikipedia)", W + "Base_Naval_Ushuaia")]),

    ("rosario_narco", "Violencia narco en Rosario", "Seguridad", "82", "rosario", -60.6332, -32.9472, 3, "Contenida con fuerzas federales",
     ["los_monos", "muni_rosario", "gob_santafe", "seguridad", "comodoro_py"], [],
     "Bandas como Los Monos disputan el narcomenudeo y atacaron edificios judiciales. Desde diciembre de 2023 la Nación y la provincia despliegan fuerzas federales con el Plan Bandera; la justicia confirmó la condena de Ariel «Guille» Cantero por los ataques.",
     [("2023-12", "Comienza el Plan Bandera con fuerzas federales.", "https://www.lacapital.com.ar/policiales/confirmaron-condena-guille-cantero-ataques-contra-objetivos-judiciales-n10034583.html"),
      ("2024-11", "Guille Cantero, preso desde 2013, acumula condenas.", "https://www.lanacion.com.ar/seguridad/esta-en-prision-desde-2013-con-otra-condena-por-venta-de-drogas-guille-cantero-acumula-simbolicas-nid30112024/")],
     [("La Capital: condena confirmada", "https://www.lacapital.com.ar/policiales/confirmaron-condena-guille-cantero-ataques-contra-objetivos-judiciales-n10034583.html")]),

    ("triple_frontera", "Triple Frontera", "Seguridad", "54", "puerto-iguazu", -54.5772, -25.5972, 2, "Activa",
     ["seguridad", "gob_misiones"], ["EE.UU.", "Israel"],
     "Frontera con Brasil y Paraguay. El Departamento de Estado de EE.UU. ofrece desde mayo de 2025 hasta 10 millones de dólares por información sobre las redes financieras de Hezbolá en la zona.",
     [("2025-05", "EE.UU. ofrece una recompensa de hasta US$ 10 millones por datos sobre las finanzas de Hezbolá en la Triple Frontera.", "https://www.abc.com.py/internacionales/2025/05/19/eeuu-ofrece-hasta-us-10-millones-por-informacion-sobre-hizbula-en-triple-frontera/")],
     [("Perfil: recompensa de EE.UU.", "https://www.perfil.com/noticias/internacional/bc-eeuu-ofrece-recompensa-por-pistas-sobre-redes-financieras-de-hezbola-en-america-latina.phtml"),
      ("ABC Color: recompensa de EE.UU.", "https://www.abc.com.py/internacionales/2025/05/19/eeuu-ofrece-hasta-us-10-millones-por-informacion-sobre-hizbula-en-triple-frontera/")]),

    ("litio_puna", "Litio en la Puna", "Recursos y ambiente", "10", "fiambala", -67.6191, -27.6895, 1, "Activa",
     ["gob_catamarca", "gob_salta", "gob_jujuy"], ["China", "Reino Unido", "EE.UU."],
     "Catamarca, Salta y Jujuy concentran los proyectos de litio, con capitales chinos, angloaustralianos (Rio Tinto) y estadounidenses. Las comunidades discuten el uso del agua; en Fiambalá, un vuelco de salmuera de Zijin-Liex en 2026 terminó en multa provincial y reclamo vecinal.",
     [("2026-03", "Vuelco de salmuera de Zijin-Liex cerca de Fiambalá; multa del Ministerio de Minería de Catamarca.", "https://www.iprofesional.com/negocios/453064-litio-toxico-minera-china-provoco-desastre-ambiental-en-argentina-y-afecto-a-un-pueblo")],
     [("Chequeado: los proyectos de litio", "https://chequeado.com/el-explicador/litio-en-jujuy-salta-y-catamarca-cuales-son-los-proyectos-mas-importantes-en-esta-region/"),
      ("openDemocracy: litio, agua y RIGI", "https://www.opendemocracy.net/es/argentina-litio-mineria-rio-tinto-catamarca-gas-natural-agua-rigi/")]),

    ("reforma_laboral", "CGT frente a la reforma laboral", "Laboral", "02", "ciudad-autonoma-de-buenos-aires", -58.39, -34.62, 2, "Ley vigente; disputa judicial y sindical",
     ["milei", "congreso", "cgt_arg", "camioneros", "gob_pba"], [],
     "El Congreso sancionó en febrero de 2026 la reforma laboral (Ley 27.802). La CGT, con nueva conducción, busca revertirla junto a Kicillof.",
     [("2026-02", "Sanción de la Ley 27.802.", "https://abogados.com.ar/argentina-sanciona-la-ley-de-modernizacion-laboral/38623"),
      ("2026", "La CGT elige nueva conducción y se pone en alerta.", "https://www.lacapital.com.ar/politica/la-cgt-eligio-nueva-conduccion-y-se-pone-alerta-la-reforma-laboral-milei-n10228233.html/amp")],
     [("Letra P: la hoja de ruta de la CGT", "https://www.letrap.com.ar/politica/la-hoja-ruta-la-cgt-torcer-la-reforma-laboral-y-volver-al-centro-del-ring-junto-axel-kicillof-n5420929")]),

    ("aguas_blancas", "Frontera Aguas Blancas–Bermejo", "Seguridad", "66", "aguas-blancas", -64.3533, -22.7371, 3, "Bajo el Plan Güemes",
     ["seguridad", "gob_salta"], [],
     "Paso con Bolivia sobre el río Bermejo, con contrabando y narcotráfico por pasos no habilitados. El municipio está intervenido; la Nación y Salta lanzaron el Plan Güemes, levantaron un cerco en la ribera y Prefectura patrulla el río.",
     [("2024-12", "Lanzamiento del Plan Güemes en Aguas Blancas.", "https://en.mercopress.com/2024/12/09/argentine-pna-to-patrol-bolivia-bordering-river"),
      ("2025-01", "Convenio para un cerco de 200 metros en la ribera del Bermejo.", "https://misionesonline.net/2025/01/27/respaldo-del-gobierno-nacional-construccion-del-alambrado-en-salta/"),
      ("2026-07", "Gendarmería cierra un paso ilegal en una finca privada de Aguas Blancas.", "https://www.todojujuy.com/politica/gendarmeria-nacional-cerro-el-paso-ilegal-finca-karina-n277352"),
      ("2026-09", "Enfrentamiento entre Prefectura y bagayeros.", "https://www.perfil.com/noticias/policia/detonaciones-corridas-y-caos-violento-choque-entre-prefectura-y-contrabandistas-en-la-frontera-con-bolivia.phtml")],
     [("MercoPress: el Plan Güemes", "https://en.mercopress.com/2025/01/28/argentina-to-build-fence-along-bolivian-border")]),

    ("dock_sud", "Puerto de Dock Sud", "Infraestructura", "06", None, -58.345, -34.648, 2, "Activa; obra frenada por la Justicia",
     ["gob_pba", "milei"], [],
     "Principal puerto bonaerense, administrado por un consorcio de la provincia y operado por Exolgan, que mueve más del 40% de los contenedores del país. La ampliación del muelle por iniciativa privada enfrenta a la provincia con municipios vecinos y con la Nación, que reclama la deuda por el dragado de los canales de acceso.",
     [("2026", "La Nación reclama judicialmente a la provincia la deuda por el dragado de los canales del Río de la Plata.", "https://www.letrap.com.ar/economia/javier-milei-le-apunta-otro-puerto-provincial-ahora-axel-kicillof-n5421859/amp"),
      ("2026", "El municipio de Lanús demanda a Exolgan y a las empresas del puerto por el daño del tránsito pesado.", "https://www.letrap.com.ar/economia/puertos-bonaerenses-festival-denuncias-y-reclamos-deudas-dock-sud-n5422064"),
      ("2026", "La Justicia bonaerense ordena paralizar la obra de ensanche del canal y del muelle.", "https://www.letrap.com.ar/economia/puertos-bonaerenses-la-justicia-freno-una-obra-dock-sud-y-habilito-el-reclamo-lanus-las-empresas-n5422305")],
     [("Letra P: la Justicia frenó una obra en Dock Sud", "https://www.letrap.com.ar/economia/puertos-bonaerenses-la-justicia-freno-una-obra-dock-sud-y-habilito-el-reclamo-lanus-las-empresas-n5422305"),
      ("Letra P: Exolgan concentra más del 40% de los contenedores", "https://www.letrap.com.ar/economia/puertos-monica-litza-mantiene-frenada-la-definicion-el-dragado-dock-sud-n5421098/amp")]),

    ("andalgala_mara", "Andalgalá y el proyecto MARA", "Socioambiental", "10", "andalgala", -66.3154, -27.583, 3, "Activa",
     ["gob_catamarca"], ["Canadá y Australia"],
     "Conflicto entre asambleas ambientalistas y vecinos de Choya, por un lado, y el proyecto de cobre Minera Agua Rica-Alumbrera (MARA, de capital canadiense) y el gobierno provincial, por el otro. En 2026 hubo cortes en el camino al proyecto e incidentes con heridos entre manifestantes y la policía; el intendente pidió frenar tareas y más control ambiental.",
     [("2026", "Incidentes con heridos entre la policía y ambientalistas en el camino al proyecto.", "https://www.elancasti.com.ar/edicion-impresa/violentos-incidentes-la-policia-y-ambientalistas-un-camino-andalgala-n496853"),
      ("2026", "El intendente de Andalgalá exige por carta documento el cese de tareas en Agua Rica.", "https://www.elancasti.com.ar/edicion-impresa/conflicto-minero-intendente-andalgala-exigio-al-cese-tareas-agua-rica-n494945"),
      ("2026", "La Justicia rechaza desalojar el acampe de vecinos de Choya.", "https://www.elancasti.com.ar/edicion-impresa/justicia-no-hizo-lugar-pedido-desalojo-vecinos-choya-n496584")],
     [("El Ancasti: Eduardo Córdoba y las garantías ambientales", "https://www.elancasti.com.ar/politica-y-economia/eduardo-cordoba-hoy-la-provincia-carece-garantias-ambientales-n495920"),
      ("Pan American Silver adquirió el accionista principal de MARA", "https://nuevaregion.com/la-megamineria-ha-demostrado-el-fracaso-en-toda-la-argentina")]),

    ("aceiteros_gr", "Paros aceiteros en el Gran Rosario", "Laboral", "82", "san-lorenzo", -60.7369, -32.7448, 2, "Acuerdo salarial vigente; conflicto latente",
     ["soea_sl", "ciara", "cgt_arg"], ["China", "EE.UU."],
     "Los gremios aceiteros pueden detener las terminales del cordón San Lorenzo-Timbúes, que despachan más de la mitad de las exportaciones agroindustriales del país (entre ellas las de Cofco, Cargill y Bunge). En mayo de 2026 lanzaron un paro por tiempo indeterminado y la Nación dictó la conciliación obligatoria.",
     [("2026-05", "Paro nacional aceitero y conciliación obligatoria.", "https://www.lacapital.com.ar/economia/paro-y-conciliacion-obligatoria-aceiteros-san-lorenzo-afirman-que-la-lucha-continua-n10261593.html/amp"),
      ("2026-06", "Acuerdo de aumento del 29,5% para todo el año.", "https://www.infocampo.com.ar/tag/soea/")],
     [("BCR: récord de embarques de 2025 por puerto", "https://www.bcr.com.ar/es/print/pdf/node/114028"),
      ("La Capital: aceiteros frenan los puertos", "https://www.lacapital.com.ar/aceiteros-lanzan-un-paro-y-se-frenan-los-puertos-del-gran-rosario-n10261479.html/amp")]),

    ("vaca_muerta_trabajo", "Salarios y tarifas en Vaca Muerta", "Laboral", "58", "anelo", -68.788, -38.354, 1, "Latente",
     ["petroleros_nqn", "ypf", "gob_neuquen"], ["EE.UU."],
     "El sindicato petrolero negocia con las operadoras y las empresas de servicios en cada paritaria bajo amenaza de paro. En septiembre de 2026 rechazó el pedido de Halliburton de bajar 23% las tarifas a sus proveedores locales.",
     [("2026-01", "Aumento salarial y bono; alerta por la reforma laboral.", "https://www.noticiasnqn.com.ar/noticias/2026/01/23/327062-rucci-anuncio-aumentos-salariales-un-bono-de-500000-y-alerto-por-una-posible-reforma-laboral"),
      ("2026-09", "Rechazo al recorte de tarifas de Halliburton a las pymes.", "https://www.noticiasnqn.com.ar/amp/noticias/2026/09/08/351608-rucci-rechazo-el-ajuste-de-halliburton-a-las-pymes-de-vaca-muerta")],
     [("LM Neuquén: Rucci y las paritarias", "https://mase.lmneuquen.com/marcelo-rucci-a9825/2")]),

    ("acindar_vc", "Acindar en Villa Constitución", "Industrial", "82", "villa-constitucion", -60.3297, -33.2273, 1, "Latente",
     ["uom_vc"], ["Unión Europea"],
     "La planta principal de Acindar (ArcelorMittal, con sede en Luxemburgo) produce la mitad que en 2024; la empresa alterna paradas y suspensiones y el gremio local negocia salarios con amenazas de paro.",
     [("2026-05", "La UOM cierra un aumento y levanta el paro.", "https://www.iprofesional.com/economia/454009-aumento-salarial-en-acindar-y-suspension-del-paro-a-cuanto-se-fue-el-sueldo-promedio"),
      ("2026-06", "Acindar frena la producción por falta de ventas.", "https://www.lacapital.com.ar/economia/acindar-decidio-frenar-la-produccion-villa-constitucion-falta-ventas-n10263980.html")],
     [("La Capital: Acindar frena la producción", "https://www.lacapital.com.ar/economia/acindar-decidio-frenar-la-produccion-villa-constitucion-falta-ventas-n10263980.html")]),
]

# (id, nombre, provincia, ciudad, lon, lat, estado, texto, fuentes)
ZONAS = [
    ("zl_bermejo", "Ribera del Bermejo en Aguas Blancas", "66", "aguas-blancas", -64.3533, -22.7371,
     "Recuperada parcialmente desde diciembre de 2024",
     "El Ministerio de Seguridad de la Nación describió el cruce como «tierra de nadie» antes del Plan Güemes: pasos no habilitados sobre el río para contrabando y droga. Desde entonces hay fuerzas federales, un cerco en la ribera y cierres de pasos ilegales, pero siguen los enfrentamientos.",
     [("El Doce: comunicado del Ministerio de Seguridad", "https://eldoce.tv/politica/2025/01/27/el-gobierno-defendio-el-cerco-en-la-frontera-de-salta-con-bolivia-se-encontraba-completamente-descontrolada"),
      ("TodoJujuy: cierre del paso ilegal en una finca", "https://www.todojujuy.com/politica/gendarmeria-nacional-cerro-el-paso-ilegal-finca-karina-n277352"),
      ("Perfil: choque con contrabandistas (sep. 2026)", "https://www.perfil.com/noticias/policia/detonaciones-corridas-y-caos-violento-choque-entre-prefectura-y-contrabandistas-en-la-frontera-con-bolivia.phtml")]),
]
