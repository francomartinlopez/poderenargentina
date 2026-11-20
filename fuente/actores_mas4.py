# Cuarta tanda de actores (corte del 19/11/2026, pedido de Franco: completar las categorías con pocos actores
# —Ejército, inteligencia, logística, tecnología, fuerzas de seguridad, empresarios y partidos— y sumar
# referentes políticos que faltaban). Mismo formato y ejes que fuente/actores_mas.py.
# Resguardos: de las personas vivas, solo cargos, hechos públicos y lo que estableció un tribunal u organismo oficial.
# Una investigación en curso se dice como investigación; una disputa entre accionistas, como disputa.
# Quedaron afuera, por no tener hoy cargo ni estructura propia: Facundo Manes y Florencio Randazzo (sin banca desde
# diciembre de 2025) y Manuel Adorni (renunció a la Jefatura de Gabinete el 27/06/2026).

from actores_mas import S, CABA

AVELLANEDA_BA = "dep:06035"

# Fuentes que se repiten
CUPULA = "https://www.canal26.com/politica/2025/12/04/uno-por-uno-quienes-formaran-la-nueva-cupula-de-las-fuerzas-armadas-de-la-argentina/"
CUPULA_DEC = "https://www.canal12misiones.com/?p=616506"
CUPULA_LPO = "https://www.lapoliticaonline.com/politica/cambio-fuerzas-armadas/"
REFORMA_FFSS = "https://www.lanacion.com.ar/politica/el-gobierno-oficializo-los-cambios-en-las-cuatro-fuerzas-de-seguridad-federales-nid08072025/"
REFORMA_CRON = "https://www.cronista.com/economia-politica/el-gobierno-cambia-por-decreto-a-gendarmeria-prefectura-y-la-psa-las-5-claves-de-la-reforma-de-milei"
CC_SALIDA = "https://www.parlamentario.com/2026/05/07/ruptura-en-diputados-la-coalicion-civica-abandono-el-interbloque-unidos-y-le-dejo-un-mensaje-a-los-que-responden-a-sus-gobernadores/"
CC_BAE = "https://www.baenegocios.com/politica/la-coalicion-civica-rompio-con-interbloque-unidos-y-quedara-como-una-bancada-independiente/"
CC_FERRARO = "https://ellitoral.com/politica/coalicion-civica-santa-fe-lucila-lehmann-politica_0_N7wOFWUOPC.amp.html"
CARRIO_NOT = "https://noticias.perfil.com/noticias/politica/elisa-carrio-saliendo-del-modo-hibernacion.phtml"
CARRIO_ANC = "https://www.elancasti.com.ar/politica-y-economia/carrio-relanza-su-actividad-una-asociacion-civil-y-critico-milei-n613277"
LARRETA_IP = "https://www.iprofesional.com/politica/467679-larreta-acuerdo-peronismo-interna-cambia-futuro-politico-ciudad"
LARRETA_EE = "https://eleconomista.com.ar/politica/mientras-primos-macri-pelean-larreta-busca-votos-peronistas-n99328"
LARRETA_LC = "https://www.letrap.com.ar/estallo-la-interna-del-peronismo-porteno-larreta-la-campora-lo-desafia-competir-las-paso-n5427499"
LOUSTEAU_PU = "https://noticias.perfil.com/noticias/politica/radicales-en-peligro-de-extincion-quienes-quedan-en-diputados-dela-ucr.phtml"
LOUSTEAU_UCR = "https://www.mdzol.com/el-bloque-llamado-ucr-diputados-conservara-su-nombre-pesar-del-reclamo-provincias-unidas-n1428554"
JUEZ_LLA = "https://www.cronista.com/economia-politica/luis-juez-se-suma-a-la-libertad-avanza-en-el-senado-que-cambia-en-el-mapa-legislativo"
JUEZ_PERFIL = "https://www.perfil.com/noticias/cordoba/juez-se-suma-a-lla-milei-aprendio-a-usar-el-freno-de-mano-y-hoy-es-un-presidente-mas-politico.phtml"
JUEZ_BAE = "https://www.baenegocios.com/politica/la-libertad-avanza-sumo-un-nuevo-senador-a-su-bloque-5977/"
JUEZ_QUINTEROS = "https://hoydia.com.ar/politica/tras-las-acusaciones-de-la-oposicion-quinteros-defendio-su-gestion-y-aseguro-que-no-renunciara/"
BREGMAN_ATLAS = "https://www.tiempodesanjuan.com/politica/myriam-bregman-encabeza-el-ranking-imagen-positiva-varios-puestos-encima-milei-n429164"
BREGMAN_EE = "https://eleconomista.com.ar/politica/la-izquierda-avanza-encuestas-mientras-corrupcion-escala-como-principal-problema-n94569"
BREGMAN_JUN = "https://www.perfil.com/noticias/politica/bullrich-y-bregman-quedaron-por-encima-de-milei-en-una-encuesta-sobre-imagen-de-dirigentes-politicos.phtml"
MORALES_LPO = "https://www.lapoliticaonline.com/politica/gerardo-morales-se-fue-a-vivir-a-china-3488/"
MORALES_NOT = "https://noticias.perfil.com/noticias/politica/las-razones-por-las-que-gerardo-morales-se-mudo-a-china.phtml"
GEBEL_PERFIL = "https://www.perfil.com/noticias/politica/consolidacion-argentina-el-espacio-de-gebel-busca-volumen-para-2027.phtml"
GEBEL_IP = "https://www.iprofesional.com/politica/450640-dante-gebel-no-fue-lanzamiento-de-espacio-que-conto-con-peronistas-y-exlibertarios"
GEBEL_EE = "https://eleconomista.com.ar/politica/gebel-2027-respuesta-sus-dos-armadores-n92400"
GEBEL_LP = "https://www.letrap.com.ar/politica/dante-gebel-espera-una-senal-divina-decidir-si-es-candidato-n5427866"
GEBEL_LLARYORA = "https://www.perfil.com/noticias/politica/dante-gebel-se-reunio-con-referentes-de-la-cgt-y-llaryora-de-cara-al-2027.phtml"
FERRARESI_LPO = "https://www.lapoliticaonline.com/provincia/ferraresi-deja-la-intendencia-para-lanzarse-a-la-pelea-por-la-gobernacion-y-posicionar-a-sierra-en-avellaneda/"
FERRARESI_PERFIL = "https://www.perfil.com/noticias/politica/ferraresi-se-despega-de-cristina-y-juega-sus-cartas-para-la-gobernacion-con-kicillof-ella-eligio-no-conducirme.phtml"
FERRARESI_CARGO = "https://www.perfil.com/noticias/politica/a-un-mes-de-renunciar-a-la-intendencia-jorge-ferraresi-volvio-a-avellaneda-con-un-cargo-millonario-y-mira-a-2027.phtml"
FERRARESI_LARROQUE = "https://www.letrap.com.ar/politica/jorge-ferraresi-arranco-la-carrera-la-gobernacion-larroque-como-primer-aliado-n5425299"
FP_INSCRIPCION = "https://www.diariodecuyo.com.ar/argentina/el-pj-bonaerense-inscribio-la-alianza-fuerza-patria-para-competir-con-lista-de-unidad-1747960.html"
FP_BAT = "https://batimes.com.ar/news/argentina/peronism-closes-ranks-in-buenos-aires-province-launches-fuerza-patria.phtml"
FP_LISTAS = "https://www.cronista.com/economia-politica/kicillof-vs-la-campora-una-interna-a-cielo-abierto-que-tuvo-un-ganador-preliminar"
MDF_EE = "https://eleconomista.com.ar/politica/se-rompio-unidad-kicillof-encara-su-propio-armado-nacional-2027-n90057"
PJBA_KICILLOF = "https://www.letrap.com.ar/politica/axel-kicillof-presidente-el-gobernador-ya-conduce-un-pj-viejo-y-estragado-la-interna-n5423404"
PJBA_LACAPITAL = "https://www.lacapital.com.ar/c10256042"
MPN_2027 = "https://www.letrap.com.ar/politica/el-mpn-se-aleja-las-urnas-primera-vez-60-anos-no-presentara-candidaturas-provinciales-2027-n5426346"
MPN_LISTA = "https://www.letrap.com.ar/politica/neuquen-el-mpn-esquiva-su-interna-no-ira-las-urnas-y-se-alinea-rolando-figueroa-n5425839"
EM_AMBITO = "https://www.ambito.com/ambito-nacional/hugo-passalacqua-renuncio-al-partido-carlos-rovira-y-se-agudiza-la-interna-misiones-n6306612"
EM_MDZ = "https://www.mdzol.com/politica/rovira-no-sere-candidato-ningun-cargo-electivo-el-2027-n1527791"
EM_CLOSS = "https://misionesonline.net/2026/08/04/tras-la-desafiliacion-de-hugo-passalacqua-a-encuentro-misionero-el-exgobernador-maurice-closs-tambien-se-alejo-del-partido-de-carlos-rovira/"
EM_CRON = "https://www.cronista.com/economia-politica/rebelion-contra-rovira-por-la-interna-con-passalacqua-y-bloqueo-de-renuncias-masivo-en-la-legislatura/"
UIF_BO = "https://www.boletinoficial.gob.ar/detalleAviso/primera/341274/20260429"
UIF_CRON = "https://www.cronista.com/economia-politica/la-uif-tiene-nuevo-presidente-el-gobierno-designo-a-matias-alvarez-al-frente-del-organismo/"
UIF_VICE = "https://www.argentina.gob.ar/noticias/michlig-nuevo-vicepresidente-de-uif"
UIF_A24 = "https://www.a24.com/politica/mahiques-designo-matias-gabriel-alvarez-al-frente-la-uif-n1534329"
HIDROVIA_EE = "https://eleconomista.com.ar/economia/la-privatizacion-mas-grande-era-milei-ya-tiene-dueno-cambia-ahora-hidrovia-n95924"
HIDROVIA_LP = "https://www.letrap.com.ar/economia/hidrovia-la-privatizacion-mas-importante-javier-milei-deja-el-negocio-del-dragado-jan-nul-n5424607"
HIDROVIA_BL = "https://www.bloomberglinea.com/latinoamerica/argentina/hidrovia-argentina-preadjudica-contrato-para-excavar-la-via-navegable-de-us10000-millones/"
HIDROVIA_DH = "https://dolarhoy.com/economia/jan-de-nul-y-servimagnus-preadjudicadas-para-gestionar-la-hidrovia-nbsp--202665113759"
BCYL_PERFIL = "https://perfil.com/economia/el-gobierno-postergo-la-licitacion-de-belgrano-cargas-y-flexibilizo-los-requisitos-aHMoh4T4QfoX"
BCYL_ELSOL = "https://www.elsol.com.ar/?p=2277743"
BCYL_CRON = "https://www.cronista.com/economia-politica/privatizaciones-asoma-un-gigante-mexicano-y-se-calienta-la-disputa-por-trenes-de-carga"
BCYL_LMN = "https://mase.lmneuquen.com/privatizacion-belgrano-cargas-mineria-litio-licitacion-2026/amp"
BCYL_BDC = "https://bichosdecampo.com/se-ilusionan-las-cerealeras-la-sorpresiva-salida-del-grupo-mexico-deja-al-holding-agroexportador-en-carrera-para-controlar-el-belgrano-cargas-por-el-proximo-medio-siglo/"
JETSMART_FORBES = "https://www.forbesargentina.com/negocios/jetsmart-anuncia-inversion-us-550-millones-argentina-amplia-flota-suma-rutas-n92609"
JETSMART_EMOL = "https://www.emol.com/noticias/Economia/2026/06/18/1203245/jetsmart-inversion-argentina.html"
JETSMART_CRON = "https://www.cronista.com/negocios/jetsmart-acelera-contra-flybondi-us-500-millones-23-aviones-y-nuevas-rutas/"
FLYBONDI_FORBES = "https://www.forbesargentina.com/negocios/flybondi-pidio-concurso-preventivo-acreedores-ahogada-sus-deudas-n99473"
FLYBONDI_ANB = "https://www.anbariloche.com.ar/noticias/2026/10/06/119181-el-colapso-de-flybondi-derivo-en-un-concurso-judicial-para-evitar-la-quiebra"
FLYBONDI_EE = "https://eleconomista.com.ar/economia/flybondi-pidio-concurso-acreedores-n98643"
MP_IP = "https://www.iprofesional.com/finanzas/467849-que-cambiara-para-los-usuarios-si-mercado-pago-se-convierte-en-banco"
MP_BL = "https://www.bloomberglinea.com/latinoamerica/argentina/mercado-pago-y-revolut-obtendran-licencia-bancaria-antes-de-2027-dice-director-del-bcra/"
SATL_FORBES = "https://www.forbesargentina.com/daily-cover/satellogic-trepa-400-wall-street-apuesta-ia-plan-emiliano-kargieman-subirse-boom-space-economy-n93534"
SATL_MERCADO = "https://mercado.com.ar/economia-del-espacio/satellogic-suma-a-un-general-de-lockheed-martin-a-su-directorio-y-profundiza-su-apuesta-de-defensa"
SATL_BL = "https://www.bloomberglinea.com/latinoamerica/argentina/por-que-vuela-satellogic-el-paper-de-ia-que-inspiro-a-milei-y-la-apuesta-de-kargieman-con-openai/"
BIOCERES_IP = "https://www.iprofesional.com/negocios/449354-la-justicia-decreto-la-quiebra-de-bioceres-un-gigante-del-agro-argentino"
BIOCERES_EE = "https://eleconomista.com.ar/agro/bioceres-quiebra-estalla-guerra-sus-accionistas-n93075"
BIOCERES_LC = "https://www.lacapital.com.ar/c10250087"
PCIUDAD_BA = "https://buenosaires.gob.ar/noticias/nuevas-autoridades-de-la-policia-de-la-ciudad"
PCIUDAD_MDZ = "https://www.mdzol.com/politica/dura-advertencia-jorge-macri-contra-axel-kicillof-si-del-otro-lado-reina-el-caos-vamos-ser-un-muro-contra-la-barbarie-n1535301"
PCIUDAD_EE = "https://eleconomista.com.ar/politica/la-ciudad-sumo-600-policias-jorge-macri-apunto-pseudo-progres-n98816"
PSF_C5N = "https://www.c5n.com/politica/protesta-policial-santa-fe-sanciones-efectivos-10-febrero-2026"
PSF_BAE = "https://www.baenegocios.com/amp/protesta-policial-en-santa-fe-levantan-sanciones-y-prometen-mejoras-salariales-7992/"
PSF_IP = "https://www.iprofesional.com/politica/448016-maximiliano-pullaro-anuncio-aumento-sueldo-para-policia-y-se-levanto-protesta-en-provincia"
PCBA_LV = "https://www.lavozdesanjusto.com.ar/la-policia-de-cordoba-retiro-de-circulacion-mas-de-340000-dosis-de-droga-en-el-primer-semestre-de-2026"
PCBA_HD = "https://hoydia.com.ar/politica/quinteros-y-gutierrez-recibieron-a-la-secretaria-de-seguridad-de-la-nacion-alejandra-monteoliva/"
PCBA_OP = "https://www.lavozdesanjusto.com.ar/cordoba-desarticulo-organizacion-criminal-y-quinteros-afirmo-es-una-de-las-mas-sofisticadas-que-hemos-investigado"
NCAPUTO_BL = "https://bloomberglinea.com/english/reports/bloomberg-linea-characters/nicolas-caputo"
NCAPUTO_BAT = "https://www.batimes.com.ar/news/argentina/the-caputo-clan-a-family-linked-to-politics-and-power-in-argentina.phtml"
SIGMAN_BL = "https://www.bloomberglinea.com/english/reports/bloomberg-linea-characters/hugo-sigman/"
SIGMAN_CRON = "https://www.cronista.com/negocios/elea-compra-un-gigante-brasileno-de-medicamentos-de-venta-libre-estimado-en-us-300-millones/"
SIGMAN_LPO = "https://www.lapoliticaonline.com/politica/hugo-sigman-aporto-4-millones-de-pesos-a-la-campana-de-milei/"
COSTANTINI_IP = "https://www.iprofesional.com/negocios/435007-el-dueno-de-nordelta-cambia-su-estrategia-para-el-negocio-del-real-estate"
COSTANTINI_URU = "https://www.iprofesional.com/realestate/459706-costantini-avanza-en-uruguay-con-proyecto-inmobiliario-por-1250-millones-de-dolares"
COSTANTINI_CRON = "https://www.cronista.com/negocios/costantini-se-queda-con-otro-megaterreno-de-la-inmobiliaria-de-milei-hara-un-nuevo-quartier-en-belgrano"
COSTANTINI_FORBES = "https://www.forbesargentina.com/summit/eduardo-costantini-ano-elecciones-si-cambia-va-todo-demonio-n101796"

RANK_INT = "https://www.perfil.com/noticias/politica/encuesta-cuales-son-los-intendentes-del-conurbano-con-mejor-imagen.phtml"
PESO_INT = "https://www.perfil.com/noticias/amp/politica/encuesta-el-peso-de-los-intendentes-bonaerenses-en-el-calendario-electoral-2027.phtml"
GHI_LP = "https://www.letrap.com.ar/buenos-aires-quienes-son-los-11-intendentes-peronistas-del-conurbano-que-pasaron-del-triunfo-la-derrota-n5419854"
SUCESIONES_LP = "https://www.letrap.com.ar/politica/sucesiones-buenos-aires-quienes-reemplazan-los-intendentes-que-asumen-cargos-legislativos-n5417488"
LIGA_INT = "https://www.canal26.com/politica/2026/03/28/otermin-granados-achaval-y-mantegazza-encabezaron-un-encuentro-de-intendentes/"
NEUSS_LP = "https://www.letrap.com.ar/economia/los-hermanos-neuss-los-nuevos-duenos-la-energia-electrica-n5424183"
NEUSS_IP = "https://www.iprofesional.com/energia/453654-transener-cambio-manos-falta-inversores-extranjeros-energia"
NEUSS_PERFIL = "https://www.perfil.com/noticias/sociedad/a-solo-3-meses-de-comprar-transener-los-neuss-ya-lograron-recuperar-mas-del-66-de-lo-que-pagaron-por-la-empresa.phtml"
NEUSS_CRON = "https://www.cronista.com/negocios/alta-tension-la-formula-de-los-hermanos-neuss/"
NEUSS_NIHUILES = "https://www.lapoliticaonline.com/energia/mindlin-y-los-neuss-se-disputan-los-nihuiles-en-una-licitacion-rodeada-de-sospechas/"
NEUSS_AYSA = "https://www.canal26.com/economia/2026/09/15/polemica-en-la-privatizacion-de-aysa-los-hermanos-neuss-se-metieron-en-la-pelea-tras-la-baja-de-jose-luis-manzano/"
ICBC_BL = "https://www.bloomberglinea.com/latinoamerica/argentina/exclusiva-china-fuera-de-argentina-habla-el-ceo-local-de-icbc-tras-criticas-de-bessent-y-quirno/"
ICBC_MERC = "https://mercado.com.ar/finanzas/icbc-coloco-una-obligacion-negociable-por-68-500-millones-con-demanda-de-69-000-millones"
DEPOSITOS = "https://finanzasdigital.com/estadisticas/ar/financieras/ban/tabla/depositos"
PRESTAMOS = "https://finanzasdigital.com/estadisticas/ar/financieras/ban/tabla/prestamos"
RANKIA = "https://www.rankia.com.ar/blog/mejores-plazos-fijos/3447565-mejores-bancos-argentina"
SOCIOS_BANCOS = "https://mercado.com.ar/revista/numero-974/socios-principales-de-los-40-mayores-bancos/"

ACTORES = [
    # Referentes políticos que faltaban
    ("carrio", "Elisa Carrió (fundadora de la Coalición Cívica)", "Líder político", CABA, "N", "I", 1,
     S(con=1, cul=1, red=1, apo=1, coh=1), "D", "", 0),
    ("larreta", "Horacio Rodríguez Larreta (legislador porteño, Metrópolis)", "Líder político", CABA, "R", "I", 1,
     S(red=1, apo=1, coh=1, reg=1), "D", "", 1),
    ("lousteau", "Martín Lousteau (diputado, Provincias Unidas)", "Líder político", CABA, "N", "I", 1,
     S(red=1, apo=1, coh=1, reg=1), "D", "", 1),
    ("juez", "Luis Juez (senador por Córdoba, bloque LLA)", "Líder político", "Córdoba", "R", "T", 1,
     S(red=1, apo=1, coh=1, reg=1), "D", "", 1),
    ("bregman", "Myriam Bregman (diputada, Frente de Izquierda)", "Líder político", CABA, "N", "I", 1,
     S(cul=1, red=1, apo=2, coh=1), "D", "", 1),
    ("g_morales", "Gerardo Morales (exgobernador de Jujuy)", "Líder político", "San Salvador de Jujuy", "R", "P", 1,
     S(adq=1, red=1, coh=1), "D", "", 0),
    ("gebel", "Dante Gebel (pastor; Consolidación Argentina)", "Líder político", CABA, "N", "I", 1,
     S(cul=1, red=1, apo=1), "D", "", 0),
    ("ferraresi", "Jorge Ferraresi (exintendente de Avellaneda)", "Líder político", AVELLANEDA_BA, "P", "P", 1,
     S(red=1, apo=1, coh=1), "D", "", 0),
    # Partidos y frentes
    ("coalicion_civica", "Coalición Cívica ARI (Maximiliano Ferraro)", "Partido en sistema competitivo", CABA, "N", "I", 1,
     S(red=1, apo=1, coh=1), "D", "carrio", 1),
    ("fuerza_patria", "Fuerza Patria (frente del peronismo bonaerense)", "Partido en sistema competitivo", "La Plata", "P", "P", 1,
     S(red=1, apo=2, coh=1, reg=1), "D", "", 1),
    ("mdf", "Movimiento Derecho al Futuro (Axel Kicillof)", "Partido en sistema competitivo", "La Plata", "P", "P", 1,
     S(red=1, apo=1, coh=2), "D", "gob_pba", 1),
    ("consolidacion_arg", "Consolidación Argentina (Juan Pablo Brey y Eugenio Casielles)", "Partido en sistema competitivo", CABA, "N", "I", 1,
     S(red=1, apo=1), "D", "gebel", 0),
    ("mpn", "Movimiento Popular Neuquino (Gabriel Álamo)", "Partido en sistema competitivo", "Neuquén", "P", "I", 2,
     S(red=1, coh=1), "D", "", 1),
    ("encuentro_misionero", "Encuentro Misionero (Carlos Rovira)", "Partido en sistema competitivo", "Posadas", "P", "I", 1,
     S(red=1, apo=1, coh=1, reg=1), "D", "", 1),
    # Fuerzas Armadas (dependen del Ministerio de Defensa)
    ("ejercito", "Ejército Argentino (Gral. Oscar Santiago Zarich)", "Ejército", CABA, "N", "T", 3,
     S(rec=1, cap=2, prd=1, mov=2, coe=3, ter=1, adq=1, con=1, mie=2, cul=1, apo=1, coh=2, pri=1), "D", "ffaa", 2),
    ("armada", "Armada Argentina (Vicealte. Juan Carlos Romay)", "Ejército", CABA, "N", "T", 3,
     S(cap=2, mov=2, coe=2, ter=1, adq=1, con=1, mie=1, coh=2, pri=1), "D", "ffaa", 2),
    ("fuerza_aerea", "Fuerza Aérea Argentina (Brig. My. Gustavo Valverde)", "Ejército", CABA, "N", "T", 3,
     S(cap=2, mov=2, coe=2, adq=1, con=1, inn=1, mie=1, coh=2, pri=1), "D", "ffaa", 2),
    ("emco", "Estado Mayor Conjunto (Vicealte. Marcelo Dalle Nogare)", "Ejército", CABA, "N", "T", 3,
     S(coe=1, adq=1, coh=1, reg=1), "D", "ffaa", 2),
    # Inteligencia financiera
    ("uif", "UIF (Unidad de Información Financiera, Matías Álvarez)", "Servicio de inteligencia", CABA, "N", "T", 2,
     S(din=1, adq=2, reg=1), "D", "min_justicia", 2),
    # Logística y transporte
    ("jan_de_nul", "Jan De Nul y Servimagnus (concesión de la hidrovía)", "Logística y transporte", CABA, "N", "T", 1,
     S(cap=2, prd=1, mov=2, ter=1, con=1, red=1), "D", "", 0),
    ("belgrano_cargas", "Belgrano Cargas y Logística (en privatización)", "Logística y transporte", CABA, "N", "T", 3,
     S(cap=1, mov=1, ter=1), "D", "economia", 1),
    ("jetsmart", "JetSMART (segunda aerolínea del país)", "Logística y transporte", CABA, "N", "T", 1,
     S(cap=1, mov=1, red=1), "D", "", 0),
    ("flybondi", "Flybondi (en concurso preventivo)", "Logística y transporte", CABA, "N", "I", 1,
     S(mov=1), "D", "", 0),
    # Tecnología
    ("mercado_pago", "Mercado Pago (Mercado Libre)", "Empresa tecnológica", CABA, "N", "T", 2,
     S(cap=2, din=2, adq=2, inn=1, red=1), "D", "meli", 0),
    ("satellogic", "Satellogic (Emiliano Kargieman)", "Empresa tecnológica", CABA, "N", "T", 1,
     S(cap=1, adq=1, inn=2, red=1), "D", "", 0),
    ("bioceres", "Bioceres SA (en quiebra) y Bioceres Crop Solutions", "Empresa tecnológica", "Rosario", "N", "I", 1,
     S(prd=1, inn=1), "D", "", 0),
    # Fuerzas de seguridad
    ("policia_ciudad", "Policía de la Ciudad (jefe Diego Casaló; ministro Horacio Giménez)", "Fuerza de seguridad", CABA, "P", "I", 3,
     S(coe=2, ter=2, adq=1, coh=1), "D", "gob_caba", 2),
    ("policia_santafe", "Policía de Santa Fe (jefe Luis Maldonado; ministro Pablo Cococcioni)", "Fuerza de seguridad", "Santa Fe", "P", "I", 3,
     S(coe=2, ter=2, adq=1, coh=1), "D", "gob_santafe", 2),
    ("policia_cordoba", "Policía de Córdoba (ministro Juan Pablo Quinteros)", "Fuerza de seguridad", "Córdoba", "P", "P", 3,
     S(coe=2, ter=2, adq=1, coh=1), "D", "gob_cordoba", 2),
    ("psa", "Policía de Seguridad Aeroportuaria", "Fuerza de seguridad", CABA, "N", "T", 3,
     S(coe=1, ter=1, adq=1, mov=1), "D", "seguridad", 2),
    ("spf", "Servicio Penitenciario Federal", "Fuerza de seguridad", CABA, "N", "T", 3,
     S(coe=2, ter=1), "D", "seguridad", 2),
    # Empresarios
    ("n_caputo", "Nicolás «Nicky» Caputo (Grupo Caputo, Mirgor)", "Empresario", CABA, "N", "T", 1,
     S(cap=2, prd=1, con=1, red=2), "D", "", 0),
    ("sigman", "Hugo Sigman y Silvia Gold (Grupo Insud)", "Empresario", CABA, "N", "X", 1,
     S(cap=2, prd=1, inn=1, cul=1, red=1), "D", "", 0),
    ("costantini", "Eduardo Costantini (Consultatio, Nordelta)", "Empresario", CABA, "N", "T", 1,
     S(cap=2, ter=1, cul=1, red=1), "D", "", 0),
    # Grupo Neuss y bancos (pedido de Franco del 19/11/2026)
    ("neuss", "Patricio y Juan Neuss (Edison Energía)", "Empresario", CABA, "N", "I", 1,
     S(cap=2, prd=2, ter=1, con=1, red=1), "D", "", 0),
    ("icbc", "ICBC Argentina (banco del Estado chino)", "Empresa financiera", CABA, "N", "E", 2,
     S(cap=2, din=2, ext=1, con=1, red=1), "D", "", 0),
    ("credicoop", "Banco Credicoop Cooperativo", "Empresa financiera", CABA, "N", "I", 1,
     S(cap=1, din=1, apo=1, red=1), "D", "", 0),
    ("banco_ciudad", "Banco Ciudad de Buenos Aires", "Empresa financiera", CABA, "P", "I", 3,
     S(cap=1, din=1), "D", "gob_caba", 1),
    ("supervielle", "Grupo Supervielle", "Empresa financiera", CABA, "N", "I", 1,
     S(cap=1, din=1), "D", "", 0),
    # Intendentes del conurbano que faltaban
    ("int_echeverria", "Fernando Gray (intendente de Esteban Echeverría)", "Líder político", "dep:06260", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_escobar", "Ariel Sujarchuk (intendente de Escobar)", "Líder político", "dep:06252", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_malvinas", "Leonardo Nardini (intendente de Malvinas Argentinas)", "Líder político", "dep:06515", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_sanmiguel", "Jaime Méndez (intendente de San Miguel)", "Líder político", "dep:06760", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_brown", "Juan José Fabiani (intendente de Almirante Brown)", "Líder político", "dep:06028", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_tigre", "Julio Zamora (intendente de Tigre)", "Líder político", "dep:06805", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_vlopez", "Soledad Martínez (intendente de Vicente López)", "Líder político", "dep:06861", "M", "T", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_jcpaz", "Lorena Espina (intendenta interina de José C. Paz)", "Líder político", "dep:06412", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_ezeiza", "Gastón Granados (intendente de Ezeiza)", "Líder político", "dep:06270", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_varela", "Andrés Watson (intendente de Florencio Varela)", "Líder político", "dep:06274", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_merlo", "Gustavo Menéndez (intendente de Merlo)", "Líder político", "dep:06539", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_sanisidro", "Ramón Lanús (intendente de San Isidro)", "Líder político", "dep:06756", "M", "T", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_sanmartin", "Fernando Moreira (intendente de General San Martín)", "Líder político", "dep:06371", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_moron", "Lucas Ghi (intendente de Morón)", "Líder político", "dep:06568", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_3f", "Rodrigo «Roco» Aybar Perlender (intendente a cargo de Tres de Febrero)", "Líder político", "dep:06840", "M", "T", 2,
     S(ter=1, red=1, coh=1), "D", "", 2),
]

FICHAS = {
    "carrio": dict(res="Fundadora de la Coalición Cívica, retirada de la política partidaria y sin cargo. En mayo de 2026 anunció una asociación civil «no política» contra la corrupción, con colaboradores históricos de la CC, y desde allí critica al Gobierno de Milei y a Mauricio Macri. La CC la sigue presentando como su líder.",
                   manda="Elisa Carrió; la conducción formal del partido es de Maximiliano Ferraro.",
                   fuentes=[("Noticias: Carrió sale del modo «hibernación»", CARRIO_NOT),
                            ("El Ancasti: la asociación civil y las críticas a Milei", CARRIO_ANC),
                            ("Contexto Tucumán: «A Macri no le hablo nunca más»", "https://www.contextotucuman.com/nota/210062/carrio-a-macri-no-le-hablo-nunca-mas.html")]),
    "larreta": dict(res="Exjefe de Gobierno porteño (2015-2023), hoy legislador de la Ciudad. Lanzó en marzo de 2026 su espacio, Metrópolis, confirmó que será candidato a jefe de Gobierno en 2027 y no descarta un acuerdo con el peronismo porteño, lo que abrió una interna en el PJ de la Ciudad. Obtuvo el 8% en 2025.",
                    manda="Horacio Rodríguez Larreta.",
                    fuentes=[("iProfesional: candidato en 2027 y no descarta acuerdo con el peronismo", LARRETA_IP),
                             ("El Economista: Larreta busca votos peronistas", LARRETA_EE),
                             ("Letra P: La Cámpora lo desafía a competir en las PASO", LARRETA_LC)]),
    "lousteau": dict(res="Diputado nacional por la Ciudad desde diciembre de 2025; juró por Provincias Unidas y no por la UCR, partido que presidió hasta fines de 2025, cuando lo sucedió Leonel Chiarella. Los radicales de Provincias Unidas reclamaron que el bloque oficial de la UCR dejara de usar el sello.",
                     manda="Martín Lousteau.",
                     fuentes=[("Noticias: Lousteau juró por Provincias Unidas", LOUSTEAU_PU),
                              ("MDZ: la disputa por el sello de la UCR", LOUSTEAU_UCR)]),
    "juez": dict(res="Senador nacional por Córdoba hasta 2027. Dejó el PRO en diciembre de 2025, armó el monobloque Frente Cívico dentro del interbloque libertario y el 23 de febrero de 2026 se sumó formalmente al bloque de La Libertad Avanza que conduce Patricia Bullrich. Aspira a ser el candidato de Milei a gobernador de Córdoba en 2027 y apoya su reelección.",
                 manda="Luis Juez.",
                 fuentes=[("El Cronista: Juez se suma al bloque de LLA", JUEZ_LLA),
                          ("Perfil: trabaja para la reelección de Milei", JUEZ_PERFIL),
                          ("BAE Negocios: la bienvenida de Bullrich (23/02/2026)", JUEZ_BAE)]),
    "bregman": dict(res="Diputada nacional del Frente de Izquierda-Unidad (PTS). En abril de 2026 la encuesta Atlas Intel-Bloomberg la ubicó como la única dirigente con imagen positiva mayor que la negativa (47% contra 46%); en junio quedó detrás de Bullrich y por delante de Milei. En la izquierda se la menciona como candidata presidencial para 2027.",
                    manda="Myriam Bregman.",
                    fuentes=[("Tiempo de San Juan: encabeza el ranking de imagen (Atlas Intel)", BREGMAN_ATLAS),
                             ("El Economista: la izquierda avanza en las encuestas", BREGMAN_EE),
                             ("Perfil: la medición de junio", BREGMAN_JUN)]),
    "g_morales": dict(res="Gobernador de Jujuy (2015-2023) y expresidente de la UCR; antecesor de Carlos Sadir. En 2026 se mudó a Shenzhen, China, donde armó una consultora que asesora a empresas y gobiernos en proyectos de energía solar con China, continuidad de los vínculos de su gestión (Parque Solar Cauchari). Según la prensa, no se retiró de la política jujeña.",
                      manda="Gerardo Morales.",
                      fuentes=[("La Política Online: Morales se fue a vivir a China", MORALES_LPO),
                               ("Noticias: las razones de la mudanza", MORALES_NOT)]),
    "gebel": dict(res="Pastor evangélico, conferencista y conductor de televisión que vive en EE.UU. Consolidación Argentina, armado de Juan Pablo Brey y Eugenio Casielles con sindicalistas, peronistas y exlibertarios, impulsa su candidatura presidencial para 2027; él no la confirmó. Se reunió con el gobernador Llaryora y con dirigentes de la CGT. Las primeras encuestas le dan entre 0,7% y 1,8%.",
                  manda="Dante Gebel.",
                  fuentes=[("Perfil: Consolidación Argentina busca volumen para 2027", GEBEL_PERFIL),
                           ("iProfesional: el lanzamiento en Lanús", GEBEL_IP),
                           ("El Economista: las primeras mediciones", GEBEL_EE),
                           ("Letra P: Gebel todavía no decide", GEBEL_LP)]),
    "ferraresi": dict(res="Intendente de Avellaneda durante cuatro mandatos; renunció en julio de 2026 para recorrer la provincia como precandidato a gobernador en 2027, con la candidatura presidencial de Kicillof. Lo sucedió su esposa, Magdalena Sierra, que luego lo designó al frente de un área del municipio. Se alejó de Cristina Kirchner («ella eligió no conducirme»); Andrés Larroque lo apoya.",
                      manda="Jorge Ferraresi.",
                      fuentes=[("La Política Online: deja la intendencia para pelear la gobernación", FERRARESI_LPO),
                               ("Perfil: «ella eligió no conducirme»", FERRARESI_PERFIL),
                               ("Perfil: el nuevo cargo en Avellaneda", FERRARESI_CARGO),
                               ("Letra P: Larroque, primer aliado", FERRARESI_LARROQUE)]),
    "coalicion_civica": dict(res="Partido fundado por Elisa Carrió y presidido por Maximiliano Ferraro. Tiene dos diputados nacionales, Ferraro y Mónica Frade, con mandato hasta 2027. El 7 de mayo de 2026 dejaron el interbloque Unidos (Provincias Unidas y Encuentro Federal) por la negativa a interpelar al entonces jefe de Gabinete Manuel Adorni, investigado por presunto enriquecimiento ilícito.",
                             manda="Maximiliano Ferraro (presidente); Elisa Carrió como referente.",
                             fuentes=[("Parlamentario: la CC abandona el interbloque Unidos", CC_SALIDA),
                                      ("BAE Negocios: bancada independiente de dos miembros", CC_BAE),
                                      ("El Litoral: Ferraro, ratificado como presidente", CC_FERRARO)]),
    "fuerza_patria": dict(res="Frente electoral del peronismo bonaerense inscripto en julio de 2025 por el PJ provincial, el Movimiento Derecho al Futuro de Kicillof, La Cámpora y el Frente Renovador de Massa. Ganó la elección provincial de septiembre de 2025 y perdió la nacional de octubre. En el armado de listas Kicillof se quedó con las candidaturas de mayor peso y La Cámpora con más lugares.",
                          manda="Conducción compartida; el PJ bonaerense lo preside Axel Kicillof.",
                          fuentes=[("Diario de Cuyo: el PJ bonaerense inscribe la alianza", FP_INSCRIPCION),
                                   ("Buenos Aires Times: quiénes la firman", FP_BAT),
                                   ("El Cronista: Kicillof contra La Cámpora en las listas", FP_LISTAS)]),
    "mdf": dict(res="Espacio político del gobernador Axel Kicillof, con la mayoría de los intendentes bonaerenses. Integra Fuerza Patria, pero desde la derrota de octubre de 2025 prepara una alternativa nacional para 2027 con independencia de La Cámpora. En 2026 Kicillof pasó a presidir el PJ bonaerense, en reemplazo de Máximo Kirchner.",
                manda="Axel Kicillof.",
                fuentes=[("El Economista: Kicillof encara su propio armado nacional", MDF_EE),
                         ("Letra P: Kicillof conduce el PJ bonaerense", PJBA_KICILLOF),
                         ("Buenos Aires Times: el MDF en Fuerza Patria", FP_BAT)]),
    "consolidacion_arg": dict(res="Movimiento que impulsa la candidatura presidencial de Dante Gebel para 2027, conducido por el sindicalista Juan Pablo Brey y el legislador porteño Eugenio Casielles. Se lanzó en el microestadio de Lanús con peronistas, exlibertarios y enviados del gobernador de Córdoba, y arma mesas regionales en todo el país.",
                              manda="Juan Pablo Brey y Eugenio Casielles.",
                              fuentes=[("Perfil: el lanzamiento y las mesas regionales", GEBEL_PERFIL),
                                       ("iProfesional: «tenemos la misión de convencer a Dante»", GEBEL_IP),
                                       ("Perfil: Gebel con la CGT y Llaryora", GEBEL_LLARYORA)]),
    "mpn": dict(res="Partido que ganó todas las elecciones ejecutivas de Neuquén hasta 2023, cuando lo derrotó Rolando Figueroa, salido de sus filas. En 2026 eligió por lista única una conducción alineada con Figueroa (Gabriel Álamo) y resolvió no presentar candidaturas propias en 2027, por primera vez en 60 años; sus dirigentes trabajan por la reelección del gobernador.",
                manda="Gabriel Álamo, presidente.",
                fuentes=[("Letra P: el MPN no presentará candidaturas en 2027", MPN_2027),
                         ("Letra P: lista única alineada con Figueroa", MPN_LISTA)]),
    "encuentro_misionero": dict(res="Nuevo nombre que Carlos Rovira dio en 2026 al Partido de la Concordia Social, base del Frente Renovador que gobierna Misiones desde 2003. El gobernador Hugo Passalacqua y el exgobernador Maurice Closs se desafiliaron, y buena parte de los intendentes y legisladores siguió al gobernador. Rovira, diputado provincial, dijo que no será candidato en 2027.",
                                manda="Carlos Rovira.",
                                fuentes=[("Ámbito: Passalacqua renuncia al partido de Rovira", EM_AMBITO),
                                         ("MDZ: «La Renovación caducó, hoy somos Encuentro Misionero»", EM_MDZ),
                                         ("Misiones Online: también se va Closs", EM_CLOSS),
                                         ("El Cronista: el bloque de Rovira en la Legislatura", EM_CRON)]),
    "ejercito": dict(res="Fuerza terrestre. Su jefe de Estado Mayor General es el general de división Oscar Santiago Zarich (Decreto 888/2025), que sucedió al teniente general Carlos Presti cuando este pasó al Ministerio de Defensa en diciembre de 2025.",
                     manda="Gral. Div. Oscar Santiago Zarich.",
                     fuentes=[("Canal 26: la nueva cúpula, uno por uno", CUPULA),
                              ("Canal 12 Misiones: los decretos de designación", CUPULA_DEC)]),
    "armada": dict(res="Fuerza naval, a cargo del vicealmirante Juan Carlos Romay desde diciembre de 2025. Controla el Atlántico Sur y la Antártida junto con la Prefectura.",
                   manda="Vicealte. Juan Carlos Romay.",
                   fuentes=[("Canal 26: la nueva cúpula, uno por uno", CUPULA),
                            ("La Política Online: la renovación de la cúpula", CUPULA_LPO)]),
    "fuerza_aerea": dict(res="Fuerza aérea, conducida por el brigadier mayor Gustavo Valverde, el único jefe ratificado en la renovación de diciembre de 2025. Incorpora los cazas F-16 comprados a Dinamarca.",
                         manda="Brig. My. Gustavo Valverde.",
                         fuentes=[("Canal 26: Valverde, ratificado", CUPULA),
                                  ("DEF: el nuevo jefe del Ejército y la llegada de los F-16", "https://defonline.com.ar/defensa/asumio-el-nuevo-jefe-del-ejercito-argentino-quien-es-y-que-relacion-tiene-con-el-ministro-de-defensa/")]),
    "emco": dict(res="Órgano que coordina la acción operacional de las tres fuerzas. Lo conduce el vicealmirante Marcelo Alejandro Dalle Nogare desde diciembre de 2025, en reemplazo del brigadier general Xavier Isaac; fue director general de Inteligencia del Estado Mayor Conjunto.",
                 manda="Vicealte. Marcelo Alejandro Dalle Nogare.",
                 fuentes=[("Canal 26: la nueva cúpula, uno por uno", CUPULA),
                          ("Canal 12 Misiones: los decretos de designación", CUPULA_DEC)]),
    "uif": dict(res="Organismo de inteligencia financiera contra el lavado de activos y el financiamiento del terrorismo, con autonomía y autarquía en la órbita del Ministerio de Justicia. Desde abril de 2026 la preside el fiscal federal Matías Gabriel Álvarez (Decreto 291/2026), propuesto por el ministro Mahiques, con experiencia en la Procuraduría de Narcocriminalidad; el vicepresidente es Patricio Michlig (Decreto 534/2026).",
                manda="Matías Gabriel Álvarez, presidente.",
                fuentes=[("Boletín Oficial: Decreto 291/2026", UIF_BO),
                         ("El Cronista: Álvarez, nuevo presidente", UIF_CRON),
                         ("Argentina.gob.ar: Michlig, vicepresidente", UIF_VICE)]),
    "jan_de_nul": dict(res="Consorcio de la belga Jan De Nul (60%) y la argentina Servimagnus (40%), adjudicatario en 2026 de la concesión por 25 años de la Vía Navegable Troncal (hidrovía Paraná-Paraguay), por donde sale cerca del 80% de las exportaciones. Le ganó a la belga DEME por puntaje técnico; los socios estadounidenses de DEME lo acusaron de tener respaldo chino y el consorcio lo negó. Jan De Nul draga el Paraná desde los años noventa.",
                       manda="Vía Navegable Argentina (Jan De Nul y Servimagnus).",
                       fuentes=[("El Economista: la privatización más grande de la era Milei", HIDROVIA_EE),
                                ("Letra P: tres décadas en la hidrovía", HIDROVIA_LP),
                                ("Bloomberg Línea: las acusaciones de influencia china", HIDROVIA_BL),
                                ("Dólar Hoy: participación de cada socio", HIDROVIA_DH)]),
    "belgrano_cargas": dict(res="Empresa estatal de trenes de carga (líneas Belgrano, San Martín y Urquiza) en proceso de privatización por 50 años. La apertura de ofertas se postergó al 21 de diciembre de 2026 tras la salida del Grupo México; las cerealeras del Gran Rosario preparan una oferta conjunta y Rio Tinto sigue el proceso. Tras la adjudicación, la empresa será disuelta.",
                            manda="Ministerio de Economía, hasta la adjudicación.",
                            fuentes=[("Perfil: la postergación hasta diciembre", BCYL_PERFIL),
                                     ("El Sol: la salida de Grupo México", BCYL_ELSOL),
                                     ("El Cronista: oferta conjunta de las cerealeras", BCYL_CRON),
                                     ("LM Neuquén: cerealeras, Rio Tinto y el litio", BCYL_LMN)]),
    "jetsmart": dict(res="Aerolínea de bajo costo de origen chileno, controlada por el fondo estadounidense Indigo Partners. Es la segunda operadora del país (24,4% del mercado en mayo de 2026) y en junio anunció una inversión de US$ 550 millones para llegar a 23 aviones en enero de 2027 y ocupar rutas que dejó Flybondi.",
                     manda="Estuardo Ortiz, CEO y fundador.",
                     fuentes=[("Forbes Argentina: inversión de US$ 550 millones", JETSMART_FORBES),
                              ("Emol: controlada por Indigo Partners", JETSMART_EMOL),
                              ("El Cronista: JetSMART acelera contra Flybondi", JETSMART_CRON)]),
    "flybondi": dict(res="Aerolínea de bajo costo que llegó a tener el 17% del mercado. Tras meses de cancelaciones (unos 2.400 vuelos y 383.000 pasajeros afectados en 2026) dejó de volar y en octubre de 2026 pidió el concurso preventivo de acreedores, con un pasivo estimado en US$ 120 millones; su participación cayó al 0,1%.",
                     manda="Su controlante, COC Global, bajo supervisión del Juzgado Comercial N° 24.",
                     fuentes=[("Forbes Argentina: el pedido de concurso", FLYBONDI_FORBES),
                              ("ANBariloche: del 17% al 0,1% del mercado", FLYBONDI_ANB),
                              ("El Economista: deuda de US$ 120 millones", FLYBONDI_EE)]),
    "mercado_pago": dict(res="Brazo financiero de Mercado Libre y la mayor billetera virtual del país. En octubre de 2026 el BCRA aprobó la instancia técnica de su licencia bancaria; el directorio del Central anticipó que la tendrá antes de fin de año, lo que le permitirá tomar depósitos y prestar con ellos.",
                         manda="Mercado Libre (Marcos Galperin).",
                         fuentes=[("iProfesional: aprobación técnica del BCRA", MP_IP),
                                  ("Bloomberg Línea: licencia antes de 2027, según el BCRA", MP_BL)]),
    "satellogic": dict(res="Empresa de satélites de observación de la Tierra fundada en 2010 por Emiliano Kargieman y Gerardo Richarte, que cotiza en el Nasdaq. Diseña e investiga en la Argentina, fabrica en Montevideo y apunta a contratos de defensa e inteligencia; en 2026 su acción multiplicó por cinco su valor. Nació con apoyo del INVAP y del Ministerio de Ciencia.",
                       manda="Emiliano Kargieman, CEO.",
                       fuentes=[("Forbes Argentina: el plan de Kargieman", SATL_FORBES),
                                ("Mercado: la apuesta de defensa", SATL_MERCADO),
                                ("Bloomberg Línea: contratos de defensa e inteligencia", SATL_BL)]),
    "bioceres": dict(res="Empresa de biotecnología agrícola fundada en 2001 por productores de Rosario, origen del grupo que cotiza en el Nasdaq (Bioceres Crop Solutions, BIOX). En marzo de 2026 el juez civil y comercial de Rosario Fernando Mecoli decretó la quiebra de Bioceres SA, a pedido de su controlante Moolec, en medio de una disputa entre accionistas por el control de BIOX.",
                     manda="Sindicatura de la quiebra; disputa entre los accionistas.",
                     fuentes=[("iProfesional: la Justicia decretó la quiebra", BIOCERES_IP),
                              ("El Economista: la disputa entre accionistas", BIOCERES_EE),
                              ("La Capital: la pelea societaria sigue", BIOCERES_LC)]),
    "policia_ciudad": dict(res="Policía porteña, dependiente del jefe de Gobierno a través del Ministerio de Seguridad (Horacio Giménez). La conduce el comisario Diego Casaló desde diciembre de 2024, tras la fuga de 17 presos de una comisaría de Liniers. El Gobierno porteño prevé haber incorporado más de 6.200 oficiales al cierre de 2026.",
                           manda="Diego Casaló, jefe; Horacio Giménez, ministro de Seguridad.",
                           fuentes=[("Buenos Aires: nuevas autoridades de la Policía", PCIUDAD_BA),
                                    ("MDZ: 6.200 oficiales incorporados", PCIUDAD_MDZ),
                                    ("El Economista: 600 nuevos policías", PCIUDAD_EE)]),
    "policia_santafe": dict(res="Policía provincial, bajo el Ministerio de Justicia y Seguridad de Pablo Cococcioni; su jefe es Luis Maldonado. En febrero de 2026 hubo protestas salariales con acuartelamientos en Rosario y otras ciudades: unos 20 efectivos pasaron a disponibilidad, las sanciones se levantaron y el gobernador Pullaro fijó un piso salarial.",
                            manda="Pablo Cococcioni, ministro; Luis Maldonado, jefe.",
                            fuentes=[("C5N: 20 efectivos pasados a disponibilidad", PSF_C5N),
                                     ("BAE Negocios: se levantan las sanciones", PSF_BAE),
                                     ("iProfesional: Pullaro anuncia el aumento", PSF_IP)]),
    "policia_cordoba": dict(res="Policía provincial, bajo el ministro de Seguridad Juan Pablo Quinteros. Firmó convenios de colaboración con el Ministerio de Seguridad nacional y opera en conjunto con las policías de Santa Fe y Buenos Aires. La oposición, con el respaldo de Luis Juez y Rodrigo de Loredo, pidió el juicio político de Quinteros tras la detención de un subjefe de policía.",
                            manda="Juan Pablo Quinteros, ministro de Seguridad.",
                            fuentes=[("La Voz de San Justo: resultados del primer semestre de 2026", PCBA_LV),
                                     ("Hoy Día Córdoba: convenios con la Nación", PCBA_HD),
                                     ("La Voz de San Justo: operativo con Santa Fe y Buenos Aires", PCBA_OP),
                                     ("Hoy Día Córdoba: el pedido de juicio político", JUEZ_QUINTEROS)]),
    "psa": dict(res="Fuerza federal a cargo de la seguridad de los aeropuertos. El Decreto 456/2025 amplió sus facultades frente a delitos complejos y la puso bajo el Ministerio de Seguridad Nacional.",
                manda="Ministerio de Seguridad Nacional.",
                fuentes=[("La Nación: la reforma de las cuatro fuerzas federales", REFORMA_FFSS),
                         ("Boletín Oficial: Decreto 456/2025", "https://www.boletinoficial.gob.ar/detalleAviso/primera/328024/1")]),
    "spf": dict(res="Fuerza que custodia las cárceles federales. El Decreto 455/2025 le dio un nuevo estatuto, que reemplaza a la ley orgánica de 1967, y confirmó su paso del Ministerio de Justicia al de Seguridad.",
                manda="Ministerio de Seguridad Nacional.",
                fuentes=[("La Nación: la reforma de las cuatro fuerzas federales", REFORMA_FFSS),
                         ("El Cronista: el traspaso al Ministerio de Seguridad", REFORMA_CRON)]),
    "n_caputo": dict(res="Empresario de la tercera generación de la constructora familiar Caputo SA (1938). En 1983 fundó Mirgor con Mauricio Macri como director; es primo del ministro de Economía Luis Caputo y tío segundo del asesor Santiago Caputo.",
                     manda="Nicolás Caputo.",
                     fuentes=[("Bloomberg Línea: perfil de Nicolás Caputo", NCAPUTO_BL),
                              ("Buenos Aires Times: el clan Caputo", NCAPUTO_BAT),
                              ("La Nación: el amigo de Macri desde el colegio", "https://www.lanacion.com.ar/opinion/nicolas-caputo-el-asesor-que-mas-influye-en-las-decisiones-de-macri-nid1330758")]),
    "sigman": dict(res="Hugo Sigman y Silvia Gold conducen el Grupo Insud (Chemo, mAbxience, Exeltis), conglomerado farmacéutico con presencia en agroforestación, cine y edición. Insud produce vacunas y biosimilares para laboratorios globales; en 2026 su laboratorio Elea compró una firma brasileña de venta libre. Según La Política Online, Sigman aportó $4 millones a la campaña de Milei de 2023 a través de Chemotécnica.",
                   manda="Hugo Sigman y Silvia Gold.",
                   fuentes=[("Bloomberg Línea: perfil de Hugo Sigman", SIGMAN_BL),
                            ("El Cronista: los dueños de Elea compran Cellera Farma (2026)", SIGMAN_CRON),
                            ("La Política Online: el aporte a la campaña de Milei", SIGMAN_LPO)]),
    "costantini": dict(res="Fundador y accionista mayoritario de Consultatio (1991), la desarrolladora de Nordelta en Tigre, con proyectos en la Argentina, Uruguay y EE.UU.; también fundó el MALBA. En 2025 sumó a Argencons (Quartier), que compró terrenos subastados por el Estado nacional; en 2026 lanzó un proyecto de US$ 1.250 millones en Montevideo.",
                       manda="Eduardo Costantini.",
                       fuentes=[("iProfesional: Consultatio y Nordelta", COSTANTINI_IP),
                                ("iProfesional: el proyecto en Montevideo", COSTANTINI_URU),
                                ("El Cronista: el terreno subastado por el Estado", COSTANTINI_CRON),
                                ("Forbes Argentina: Costantini en el Real Estate Summit 2026", COSTANTINI_FORBES)]),
    "neuss": dict(res="Herederos de una fortuna hecha con sodas y jugos en el conurbano (Pomona). Con Inverlat (Havanna) y los dueños de Newsan armaron en 2025 Edison Energía, que en un año y medio compró represas y distribuidoras y, con Genneia, ganó en 2026 la privatización del paquete estatal de Transener por US$ 356 millones. Tres meses después, el nuevo directorio repartió dividendos acumulados por $253.536 millones. Compiten por Los Nihuiles y la privatización de AySA.",
                  manda="Patricio y Juan Neuss.",
                  fuentes=[("Letra P: los nuevos dueños de la energía eléctrica", NEUSS_LP),
                           ("iProfesional: Genneia y Edison se quedan con Transener", NEUSS_IP),
                           ("Perfil: los dividendos de Transener", NEUSS_PERFIL),
                           ("El Cronista: la fórmula de los hermanos Neuss", NEUSS_CRON),
                           ("Canal 26: los Neuss en la privatización de AySA", NEUSS_AYSA)]),
    "icbc": dict(res="Filial del Industrial and Commercial Bank of China, el mayor banco del mundo por activos y controlado por el Estado chino; llegó en 2012 con la compra del Standard Bank. Atiende a más de un millón de hogares y 40.000 empresas, y la Argentina es su mayor operación fuera de China. En 2025 el secretario del Tesoro de EE.UU., Scott Bessent, y el hoy canciller Pablo Quirno lo criticaron; el banco anunció que financiará proyectos por US$ 2.000 millones.",
                 manda="Andrés Lozano, gerente general; casa matriz en Pekín.",
                 fuentes=[("Bloomberg Línea: habla el CEO local tras las críticas de Bessent y Quirno", ICBC_BL),
                          ("Mercado: un millón de hogares y 40.000 empresas", ICBC_MERC)]),
    "credicoop": dict(res="El mayor banco cooperativo del país, entre los diez primeros por activos y el mejor valorado por sus clientes según el ranking de Rankia.",
                      manda="Su consejo de administración, elegido por los asociados.",
                      fuentes=[("Rankia: los mayores bancos de la Argentina", RANKIA)]),
    "banco_ciudad": dict(res="Banco público porteño, cien por ciento del Gobierno de la Ciudad; décimo del sistema por préstamos y agente financiero de la Ciudad.",
                         manda="Gobierno de la Ciudad de Buenos Aires.",
                         fuentes=[("Mercado: socios principales de los 40 mayores bancos", SOCIOS_BANCOS),
                                  ("Finanzas Digital: ranking de préstamos (BCRA)", PRESTAMOS)]),
    "supervielle": dict(res="Grupo financiero de capital argentino que cotiza en Nueva York; noveno banco del sistema por préstamos en 2026.",
                        manda="Familia Supervielle (Julio Patricio Supervielle).",
                        fuentes=[("Finanzas Digital: ranking de préstamos (BCRA)", PRESTAMOS)]),
    "int_echeverria": dict(res="Intendente de Esteban Echeverría, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Fernando Gray.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_escobar": dict(res="Intendente de Escobar, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Ariel Sujarchuk.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_malvinas": dict(res="Intendente de Malvinas Argentinas, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Leonardo Nardini.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_sanmiguel": dict(res="Intendente de San Miguel, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Jaime Méndez.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_brown": dict(res="Intendente de Almirante Brown, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Juan José Fabiani.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_tigre": dict(res="Intendente de Tigre, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Julio Zamora.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_vlopez": dict(res="Intendente de Vicente López, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Soledad Martínez.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_jcpaz": dict(res="Intendenta interina de José C. Paz desde diciembre de 2025, cuando Mario Ishii juró como senador bonaerense por Fuerza Patria y pidió licencia. Licenciada en Salud Pública, era directora de Epidemiología del municipio. Ishii no puede volver a ser candidato a intendente en 2027 por el tope a las reelecciones; Roberto Caggiano y Mansilla se disputan la sucesión.",
                manda="Lorena Espina, a cargo; Mario Ishii sigue como referente del distrito.",
                fuentes=[("Letra P: Ishii eligió a una sanitarista en su reemplazo", "https://www.letrap.com.ar/politica/buenos-aires-mario-ishii-eligio-una-sanitarista-su-reemplazo-y-congelo-la-pelea-la-sucesion-n5420710"),
                         ("Letra P: quiénes reemplazan a los intendentes que asumieron bancas", "https://www.letrap.com.ar/politica/sucesiones-buenos-aires-quienes-reemplazan-los-intendentes-que-asumieron-cargos-legislativos-n5420690"),
                         ("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT)]),
    "int_ezeiza": dict(res="Intendente de Ezeiza, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Gastón Granados.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_varela": dict(res="Intendente de Florencio Varela, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Andrés Watson.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_merlo": dict(res="Intendente de Merlo, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Gustavo Menéndez.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_sanisidro": dict(res="Intendente de San Isidro, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Ramón Lanús.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_sanmartin": dict(res="Intendente de General San Martín, uno de los 24 partidos del conurbano bonaerense, que reúnen cerca de una cuarta parte de los votos del país. Figura en la medición mensual de imagen de los intendentes del GBA (octubre de 2026).",
                manda="Fernando Moreira.",
                fuentes=[("Perfil: ranking de intendentes del conurbano, octubre de 2026", RANK_INT),
                         ("Perfil: el peso de los intendentes en 2027", PESO_INT)]),
    "int_moron": dict(res="Intendente de Morón. En la elección nacional de octubre de 2025 La Libertad Avanza ganó en el distrito por 43,2% contra 38,1% de Fuerza Patria.",
                manda="Lucas Ghi.",
                fuentes=[("Letra P: los intendentes peronistas que pasaron del triunfo a la derrota", GHI_LP)]),
    "int_3f": dict(res="Quedó a cargo de Tres de Febrero en diciembre de 2025, cuando el intendente Diego Valenzuela asumió como senador bonaerense tras encabezar la lista de La Libertad Avanza en la Primera sección.",
                manda="Rodrigo Aybar Perlender, a cargo; Diego Valenzuela, intendente con licencia.",
                fuentes=[("Letra P: quiénes reemplazan a los intendentes que asumen cargos legislativos", SUCESIONES_LP),
                         ("Perfil: Aybar intendente y Valenzuela, senador con licencia (2026)", "https://www.perfil.com/noticias/amp/empresas-y-protagonistas/incentivo-a-las-inversiones-que-municipio-lidera-el-ranking-nacional-para-habilitar-comercios-e-industrias.phtml")]),
}

RELACIONES = [
    # Referentes políticos
    ("carrio", "coalicion_civica", "Gobierna", "Fundadora y referente; la conducción formal es de Ferraro.", 2, CC_FERRARO),
    ("carrio", "milei", "Enfrentamiento", "Desde su asociación civil critica al Gobierno y el caso Adorni.", 2, CARRIO_ANC),
    ("carrio", "macri", "Enfrentamiento", "Ruptura personal y política con su exaliado.", 1, "https://www.contextotucuman.com/nota/210062/carrio-a-macri-no-le-hablo-nunca-mas.html"),
    ("coalicion_civica", "prov_unidas", "Ambigua", "Dejó el interbloque Unidos en mayo de 2026, pero mantiene el diálogo.", 1, CC_BAE),
    ("larreta", "gob_caba", "Enfrentamiento", "Competirá con Jorge Macri por la Jefatura de Gobierno en 2027.", 2, LARRETA_IP),
    ("larreta", "pj", "Ambigua", "No descarta un acuerdo con el peronismo porteño para 2027.", 1, LARRETA_EE),
    ("larreta", "la_campora", "Enfrentamiento", "La Cámpora lo desafía a competir en las PASO con Mariano Recalde.", 1, LARRETA_LC),
    ("lousteau", "prov_unidas", "Alianza", "Juró como diputado por Provincias Unidas.", 2, LOUSTEAU_PU),
    ("lousteau", "ucr", "Ambigua", "Expresidente del partido; su sector reclamó el sello al bloque oficial de la UCR.", 1, LOUSTEAU_UCR),
    ("juez", "lla", "Alianza", "Integra desde febrero de 2026 el bloque de LLA en el Senado.", 3, JUEZ_LLA),
    ("juez", "bullrich", "Alianza", "Bullrich, jefa del bloque, oficializó su incorporación.", 2, JUEZ_BAE),
    ("juez", "gob_cordoba", "Enfrentamiento", "Opositor a Llaryora; respaldó el pedido de juicio político a su ministro de Seguridad.", 2, JUEZ_QUINTEROS),
    ("bregman", "fit_u", "Alianza", "Diputada y principal figura del Frente de Izquierda.", 3, BREGMAN_ATLAS),
    ("bregman", "milei", "Enfrentamiento", "Opositora; protagonizó un cruce con Milei en el Congreso (abril de 2026).", 2, BREGMAN_EE),
    ("g_morales", "gob_jujuy", "Ambigua", "Antecesor de Sadir; desde China sigue en la política jujeña.", 2, MORALES_LPO),
    ("g_morales", "ucr", "Alianza", "Expresidente del partido.", 1, MORALES_NOT),
    ("gebel", "consolidacion_arg", "Alianza", "El espacio impulsa su candidatura presidencial para 2027.", 3, GEBEL_PERFIL),
    ("consolidacion_arg", "gob_cordoba", "Alianza", "Llaryora envió un funcionario al lanzamiento y se reunió con Gebel.", 1, GEBEL_LLARYORA),
    ("consolidacion_arg", "cgt_arg", "Alianza", "Dirigentes de la CGT participan del armado.", 1, GEBEL_LLARYORA),
    ("ferraresi", "gob_pba", "Alianza", "Respalda la candidatura presidencial de Kicillof y busca sucederlo.", 3, FERRARESI_PERFIL),
    ("ferraresi", "cfk", "Enfrentamiento", "Se alejó de Cristina Kirchner, que tiene otro candidato en Avellaneda.", 1, FERRARESI_PERFIL),
    ("ferraresi", "mdf", "Alianza", "Fue anfitrión del plenario del MDF en Avellaneda.", 2, FERRARESI_PERFIL),
    # Partidos y frentes
    ("mdf", "gob_pba", "Alianza", "Es el espacio político del gobernador.", 3, MDF_EE),
    ("mdf", "la_campora", "Enfrentamiento", "Disputa la conducción del peronismo bonaerense y la candidatura de 2027.", 2, MDF_EE),
    ("mdf", "fuerza_patria", "Alianza", "Firmante de la alianza electoral.", 2, FP_BAT),
    ("pj", "fuerza_patria", "Alianza", "El PJ bonaerense inscribió el frente en julio de 2025.", 3, FP_INSCRIPCION),
    ("la_campora", "fuerza_patria", "Alianza", "Integra el frente y disputa las listas con Kicillof.", 2, FP_LISTAS),
    ("massa", "fuerza_patria", "Alianza", "El Frente Renovador es parte del frente.", 2, FP_BAT),
    ("gob_pba", "pj", "Alianza", "Kicillof preside el PJ bonaerense desde 2026, en reemplazo de Máximo Kirchner.", 2, PJBA_LACAPITAL),
    ("mpn", "gob_neuquen", "Alianza", "Conducción alineada con Figueroa; no presentará candidatos en 2027.", 2, MPN_2027),
    ("encuentro_misionero", "gob_misiones", "Enfrentamiento", "Passalacqua se desafilió y rompió con Rovira.", 3, EM_AMBITO),
    # Fuerzas Armadas
    ("ffaa", "ejercito", "Gobierna", "Zarich, designado por el Decreto 888/2025.", 3, CUPULA_DEC),
    ("ffaa", "armada", "Gobierna", "Romay, designado en diciembre de 2025.", 3, CUPULA),
    ("ffaa", "fuerza_aerea", "Gobierna", "Valverde, ratificado en diciembre de 2025.", 3, CUPULA),
    ("ffaa", "emco", "Gobierna", "Dalle Nogare, designado en diciembre de 2025.", 3, CUPULA_DEC),
    # Inteligencia financiera
    ("min_justicia", "uif", "Gobierna", "Mahiques propuso a Álvarez, designado por el Decreto 291/2026.", 3, UIF_BO),
    # Logística
    ("economia", "jan_de_nul", "Contrato", "Concesión de la hidrovía por 25 años, adjudicada en 2026.", 3, HIDROVIA_EE),
    ("economia", "belgrano_cargas", "Gobierna", "Conduce la privatización; postergó la apertura de ofertas al 21/12/2026.", 3, BCYL_PERFIL),
    ("cargill", "belgrano_cargas", "Ambigua", "Las cerealeras del Gran Rosario preparan una oferta conjunta por el tren.", 1, BCYL_CRON),
    ("agd", "belgrano_cargas", "Ambigua", "Integra el grupo de cerealeras interesadas en el tren.", 1, BCYL_BDC),
    ("riotinto", "belgrano_cargas", "Ambigua", "Interesada en el tren por el litio del norte.", 1, BCYL_LMN),
    ("jetsmart", "flybondi", "Enfrentamiento", "Ocupa las rutas que dejó Flybondi.", 2, JETSMART_CRON),
    ("jetsmart", "aerolineas", "Enfrentamiento", "Segunda operadora del mercado, compite con la línea de bandera.", 2, JETSMART_FORBES),
    # Tecnología
    ("meli", "mercado_pago", "Propiedad", "Brazo financiero de Mercado Libre.", 3, MP_IP),
    ("bcra", "mercado_pago", "Ambigua", "Aprobó la instancia técnica de la licencia bancaria; falta el directorio.", 2, MP_BL),
    # Seguridad
    ("gob_caba", "policia_ciudad", "Gobierna", "Depende del jefe de Gobierno a través del Ministerio de Seguridad.", 3, PCIUDAD_BA),
    ("gob_santafe", "policia_santafe", "Gobierna", "Bajo el ministro Cococcioni; protesta salarial en febrero de 2026.", 3, PSF_C5N),
    ("gob_cordoba", "policia_cordoba", "Gobierna", "Bajo el ministro Quinteros.", 3, PCBA_LV),
    ("policia_cordoba", "seguridad", "Alianza", "Convenios de colaboración con el Ministerio de Seguridad nacional.", 1, PCBA_HD),
    ("policia_cordoba", "policia_santafe", "Alianza", "Operativos conjuntos contra bandas interprovinciales.", 1, PCBA_OP),
    ("seguridad", "psa", "Gobierna", "El Decreto 456/2025 la pone bajo el Ministerio de Seguridad.", 3, REFORMA_FFSS),
    ("seguridad", "spf", "Gobierna", "El Decreto 455/2025 confirma su traspaso desde Justicia.", 3, REFORMA_CRON),
    # Empresarios
    ("n_caputo", "macri", "Alianza", "Compañeros de colegio desde los seis años y socios: fundaron juntos Mirgor en 1983.", 3, NCAPUTO_BL),
    ("n_caputo", "mirgor", "Propiedad", "Fundador y accionista de Mirgor.", 3, NCAPUTO_BL),
    ("sigman", "milei", "Financiamiento", "Aportó $4 millones a la campaña de 2023 a través de Chemotécnica S.A.", 1, SIGMAN_LPO),
    # Grupo Neuss, bancos e intendentes
    ("neuss", "brito", "Alianza", "Edison y Genneia (familia Brito) compraron juntos el paquete de Transener.", 2, NEUSS_IP),
    ("economia", "neuss", "Contrato", "Ganaron la privatización de la participación estatal en Transener (US$ 356 millones).", 2, NEUSS_PERFIL),
    ("neuss", "mindlin", "Enfrentamiento", "Disputan la concesión de Los Nihuiles en Mendoza.", 1, NEUSS_NIHUILES),
    ("tesoro_eeuu", "icbc", "Enfrentamiento", "Bessent criticó al banco chino en 2025.", 1, ICBC_BL),
    ("gob_caba", "banco_ciudad", "Propiedad", "La Ciudad tiene el 100% del banco.", 3, SOCIOS_BANCOS),
    ("int_ezeiza", "gob_pba", "Alianza", "Granados integra la Liga de Intendentes del peronismo bonaerense.", 2, LIGA_INT),
    ("int_3f", "lla", "Alianza", "Reemplaza a Valenzuela, que encabezó la lista libertaria en la Primera sección.", 2, SUCESIONES_LP),
]

# --- Intendentes del conurbano: espacio político de cada uno y los cuatro que faltaban (pedido del 19/11/2026) ---
CARTOGRAFIA_PJ = "https://www.letrap.com.ar/politica/la-nueva-cartografia-del-peronismo-bonaerense-cuatro-espacios-disputan-la-sucesion-axel-kicillof-n5425393"
PRIMERA_SECCION = "https://www.letrap.com.ar/politica/primera-seccion-mano-mano-ocho-bancas-del-senado-y-un-peronista-al-que-javier-milei-le-prende-velas-n5418299"
LIGA_LP = "https://www.letrap.com.ar/intendentes-vienen-marchando-el-peronismo-antigrieta-se-amplia-mientras-cfk-y-kicillof-siguen-guerra-n5423629"
UNION_FEDERAL = "https://www.iprofesional.com/politica/435449-los-barones-del-conurbano-rompen-con-cristina-kirchner-y-arman-lista-propia"
CFK_PJ_LP = "https://www.letrap.com.ar/politica/cfk-vs-quintela-como-se-reparten-los-apoyos-los-intendentes-del-conurbano-n5411778"
NARDINI_MDF = "https://www.letrap.com.ar/politica/intendentes-del-mdf-ceden-el-desdoblamiento-favorecer-kicillof-su-estrategia-nacional-n5427767"
ZAMORA_SOMOS = "https://www.letrap.com.ar/politica/san-fernando-la-disputa-local-replica-la-pulseada-julio-zamora-y-malena-galmarini-tigre-n5417685"
MENENDEZ_CRON = "https://www.cronista.com/economia-politica/la-otra-cara-de-la-interna-peronista-a-quien-responden-los-intendentes-con-peores-resultados"
PRO_BASTIONES = "https://www.lapoliticaonline.com/provincia/vicente-lopez-y-san-isidro-los-bastiones-del-pro-que-resistieron-la-ola-peronista/"
LANUS_PRO = "https://www.letrap.com.ar/conurbano/rebelion-el-pro-intendentes-pegan-el-portazo-y-abandonan-el-frente-libertario-n5417262"
SELCI_LP = "https://www.letrap.com.ar/politica/hurlingham-el-peronismo-se-encamina-una-nueva-disputa-selci-zabaleta-n5427352"
SELCI_GBA = "https://www.gba.gob.ar/node/52345"
DESCALZO_PERFIL = "https://www.perfil.com/noticias/modo-fontevecchia/intendente-de-ituzaingo-explica-por-que-defiende-la-candidatura-de-kicillof-modf.phtml"
BALOR_C26 = "https://www.canal26.com/politica/2025/11/25/muerte-de-juan-jose-mussi-quien-sera-el-nuevo-intendente-de-berazategui/"
BALOR_BO = "https://berazategui.gob.ar/descargas/boletin/boletin-158.pdf"
ANDREOTTI_LP = "https://www.letrap.com.ar/politica/sergio-massa-lo-empuja-la-carrera-la-gobernacion-pero-andreotti-no-se-mueve-san-fernando-n5424565"
ANDREOTTI_SUC = "https://www.letrap.com.ar/politica/san-fernando-eva-andreotti-se-encamina-suceder-su-hermano-n5425156"

ESPACIO = {
    "int_echeverria": ("En 2025 encabezó Unión Federal, una lista propia de intendentes por fuera de Fuerza Patria y del PJ conducido por Cristina Kirchner.", "iProfesional: los intendentes arman lista propia (Unión Federal)", UNION_FEDERAL),
    "int_escobar": ("Integra el Movimiento Derecho al Futuro de Kicillof.", "Letra P: la nueva cartografía del peronismo bonaerense", CARTOGRAFIA_PJ),
    "int_malvinas": ("Peronista; no integra el MDF, pero acompaña actos de Kicillof; en 2024 apoyó la candidatura de Cristina Kirchner a la presidencia del PJ.", "Letra P: Nardini y el MDF", NARDINI_MDF),
    "int_sanmiguel": ("Vecinalista.", "Letra P: los intendentes de la Primera sección", PRIMERA_SECCION),
    "int_brown": ("A cargo mientras Mariano Cascallares, del MDF, está en uso de licencia como legislador bonaerense.", "Letra P: la nueva cartografía del peronismo bonaerense", CARTOGRAFIA_PJ),
    "int_tigre": ("Peronista; en 2025 jugó con Somos Buenos Aires y mantiene una rivalidad con el massismo (le ganó la interna de 2023 a Malena Galmarini).", "Letra P: Zamora, Somos y la pulseada con Galmarini", ZAMORA_SOMOS),
    "int_vlopez": ("PRO, alineada con Jorge Macri; vicepresidenta del partido.", "La Política Online: los bastiones del PRO", PRO_BASTIONES),
    "int_ezeiza": ("Integra la Liga de Intendentes peronistas, que juega entre Cristina Kirchner y Kicillof.", "Letra P: crece la Liga de Intendentes", LIGA_LP),
    "int_varela": ("Integra el Movimiento Derecho al Futuro de Kicillof.", "Letra P: la nueva cartografía del peronismo bonaerense", CARTOGRAFIA_PJ),
    "int_merlo": ("Peronista cercano a Cristina y Máximo Kirchner; se acercó a la Liga de Intendentes y aspira a la gobernación.", "El Cronista: a quién responden los intendentes", MENENDEZ_CRON),
    "int_sanisidro": ("PRO, alineado con el Gobierno nacional.", "Letra P: los intendentes del PRO y el frente libertario", LANUS_PRO),
    "int_sanmartin": ("Integra el Movimiento Derecho al Futuro de Kicillof.", "Letra P: la nueva cartografía del peronismo bonaerense", CARTOGRAFIA_PJ),
    "int_moron": ("Integra el Movimiento Derecho al Futuro de Kicillof.", "Letra P: la nueva cartografía del peronismo bonaerense", CARTOGRAFIA_PJ),
}
for _i, (_txt, _t, _u) in ESPACIO.items():
    FICHAS[_i] = dict(FICHAS[_i], res=FICHAS[_i]["res"] + " " + _txt, fuentes=list(FICHAS[_i]["fuentes"]) + [(_t, _u)])

ACTORES += [
    ("int_hurlingham", "Damián Selci (intendente de Hurlingham)", "Líder político", "dep:06408", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_ituzaingo", "Pablo Descalzo (intendente de Ituzaingó)", "Líder político", "dep:06410", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_berazategui", "Carlos Balor (intendente de Berazategui)", "Líder político", "dep:06091", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
    ("int_sanfernando", "Juan Andreotti (intendente de San Fernando)", "Líder político", "dep:06749", "M", "P", 2,
     S(ter=1, red=1, apo=1, coh=1), "D", "", 2),
]
FICHAS.update({
    "int_hurlingham": dict(res="Intendente de Hurlingham desde diciembre de 2023 y dirigente de La Cámpora; le ganó la interna de 2023 al entonces intendente Juan Zabaleta, con quien la disputa sigue rumbo a 2027.",
                           manda="Damián Selci.",
                           fuentes=[("Letra P: Selci y Zabaleta, nueva disputa", SELCI_LP),
                                    ("Gobierno bonaerense: Katopodis y Selci recorren obras", SELCI_GBA)]),
    "int_ituzaingo": dict(res="Intendente de Ituzaingó desde diciembre de 2023; sucedió a su padre, Alberto Descalzo, que gobernó el distrito desde su creación en 1995. Integra el Movimiento Derecho al Futuro y defiende la candidatura presidencial de Kicillof.",
                          manda="Pablo Descalzo.",
                          fuentes=[("Perfil: Descalzo defiende la candidatura de Kicillof", DESCALZO_PERFIL),
                                   ("Letra P: la nueva cartografía del peronismo bonaerense", CARTOGRAFIA_PJ)]),
    "int_berazategui": dict(res="Completa hasta 2027 el mandato de Juan José Mussi, intendente durante seis períodos, que murió en noviembre de 2025. Integra el Movimiento Derecho al Futuro.",
                            manda="Carlos «Turco» Balor.",
                            fuentes=[("Canal 26: quién reemplaza a Mussi", BALOR_C26),
                                     ("Boletín Oficial de Berazategui: autoridades (agosto de 2026)", BALOR_BO),
                                     ("Letra P: la nueva cartografía del peronismo bonaerense", CARTOGRAFIA_PJ)]),
    "int_sanfernando": dict(res="Intendente de San Fernando desde 2019, sucesor de su padre, Luis Andreotti, y dirigente del Frente Renovador de Sergio Massa. No puede ir por un tercer mandato en 2027; su hermana Eva aparece como posible sucesora.",
                            manda="Juan Andreotti.",
                            fuentes=[("Letra P: Massa lo empuja a la gobernación", ANDREOTTI_LP),
                                     ("Letra P: Eva Andreotti se encamina a suceder a su hermano", ANDREOTTI_SUC)]),
})
RELACIONES += [
    ("int_escobar", "mdf", "Alianza", "Integra el MDF.", 2, CARTOGRAFIA_PJ),
    ("int_varela", "mdf", "Alianza", "Integra el MDF.", 2, CARTOGRAFIA_PJ),
    ("int_sanmartin", "mdf", "Alianza", "Integra el MDF.", 2, CARTOGRAFIA_PJ),
    ("int_moron", "mdf", "Alianza", "Integra el MDF.", 2, CARTOGRAFIA_PJ),
    ("int_ituzaingo", "mdf", "Alianza", "Integra el MDF y defiende la candidatura de Kicillof.", 2, DESCALZO_PERFIL),
    ("int_berazategui", "mdf", "Alianza", "Integra el MDF.", 2, CARTOGRAFIA_PJ),
    ("int_echeverria", "fuerza_patria", "Enfrentamiento", "En 2025 encabezó Unión Federal, por fuera de Fuerza Patria.", 2, UNION_FEDERAL),
    ("int_malvinas", "cfk", "Alianza", "Apoyó su candidatura a la presidencia del PJ en 2024.", 1, CFK_PJ_LP),
    ("int_merlo", "maximo", "Alianza", "Uno de los dirigentes territoriales más cercanos a Máximo Kirchner.", 2, CFK_PJ_LP),
    ("int_tigre", "massa", "Enfrentamiento", "Rivalidad con el massismo; le ganó la interna de 2023 a Malena Galmarini.", 2, ZAMORA_SOMOS),
    ("int_vlopez", "pro", "Alianza", "Intendenta y vicepresidenta del PRO.", 3, PRO_BASTIONES),
    ("int_vlopez", "gob_caba", "Alianza", "Alineada con Jorge Macri.", 2, PRO_BASTIONES),
    ("int_sanisidro", "pro", "Alianza", "Intendente del PRO, alineado con el Gobierno nacional.", 2, LANUS_PRO),
    ("int_hurlingham", "la_campora", "Alianza", "Dirigente de La Cámpora.", 3, SELCI_LP),
    ("int_sanfernando", "massa", "Alianza", "Una de las apuestas de Massa en la Primera sección.", 2, ANDREOTTI_LP),
]

# José C. Paz (corte del 20/11/2026)
RELACIONES += [
    ("int_jcpaz", "gob_pba", "Ambigua", "Del mismo frente, Espina le exigió a Kicillof reforzar la seguridad en el distrito tras un homicidio; Ishii cuestiona al gobernador en la Legislatura.", 1,
     "https://www.lapoliticaonline.com/conurbano/ishii-volvio-a-cruzar-a-kicillof-por-la-inseguridad-y-reclama-que-se-trate-su-proyecto/"),
]
