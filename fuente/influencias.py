# Influencias mundiales por territorio (parte 3 del paso 2, 19/11/2026).
# Cada potencia se puntúa de 0 a 3 en cinco canales, con fuente obligatoria.
# Territorio: "AR" (Estado nacional) o id IGN de provincia ("82").
#
# Comercio («com») no se carga a mano: lo calcula scripts/generar_datos.py con los destinos de fuente/economia.py
# (participación en las exportaciones de la provincia: 40% o más = 3; 20% a 40% = 2; 8% a 20% = 1).
# Cuando el INDEC informa un bloque, se toma como aproximación: USMCA → EE.UU. y Mercosur → Brasil.
# India, ASEAN, Chile, Suiza y el resto de la ALADI no están en la lista de potencias y no suman.
#
# Escala de los otros canales:
#   3 = la potencia controla el recurso, la deuda o la presencia principal de la provincia.
#   2 = actor de primer orden entre varios.
#   1 = presencia relevante pero acotada.

POTENCIAS = ["EE.UU.", "China", "Unión Europea", "Reino Unido", "Brasil", "Rusia", "Israel", "Golfo",
             "Canadá y Australia", "Japón y Corea", "FMI, BM y BID"]
CANALES = {
    "com": "Comercio",
    "inv": "Inversión",
    "deu": "Deuda y finanzas",
    "pre": "Presencia física o de seguridad",
    "pol": "Influencia política y cultural",
}
APROX_COMERCIO = {"EE.UU.": "EE.UU.", "USMCA": "EE.UU.", "China": "China", "UE": "Unión Europea",
                  "Mercosur": "Brasil", "Brasil": "Brasil"}

MEKOROT = "https://www.iprofesional.com/actualidad/453665-soberania-hidrica-en-riesgo-firma-mekorot-hizo-acuerdos-con-12-provincias-sin-control"
MK = "Mekorot, la empresa estatal de agua de Israel, elabora el plan maestro hídrico o da asistencia técnica a la provincia."
BONOS = "https://www.iprofesional.com/finanzas/460685-neuquen-regreso-wall-street-ola-inversiones-dolares.amp"

# (territorio, potencia, canal, intensidad 0-3, descripción, fuente)
INFLUENCIAS = [
    # Estado nacional
    ("AR", "FMI, BM y BID", "deu", 3, "Acuerdo de Facilidades Extendidas por USD 20.000 millones firmado en abril de 2025; la Argentina es el mayor deudor del FMI.",
     "https://finanzasdigital.com/fmi-argentina-segunda-revision-2026/"),
    ("AR", "EE.UU.", "deu", 2, "Swap del Tesoro de EE.UU. por hasta USD 20.000 millones (octubre de 2025); el tramo usado de USD 2.500 millones se canceló en diciembre de ese año.",
     "https://www.cronista.com/finanzas-mercados/bcra-dio-detalles-del-swap-con-eeuu-cuanto-pago-de-intereses-por-los-us-2500-millones/"),
    ("AR", "EE.UU.", "pol", 3, "Alineamiento del Gobierno nacional con EE.UU.; presión de Washington para reducir el uso del swap chino.",
     "https://www.iprofesional.com/finanzas/454968-javier-milei-pago-deuda-swap-china-y-dejo-en-minimos-historicos-por-presion-donald-trump"),
    ("AR", "China", "deu", 2, "Swap de monedas por 130.000 millones de yuanes (unos USD 20.000 millones) renovado en agosto de 2026 hasta 2031.",
     "https://www.forbesargentina.com/money/el-banco-central-extendio-swap-china-otros-5-anos-n94855"),
    ("AR", "Unión Europea", "inv", 2, "La belga Jan De Nul, con la argentina Servimagnus, ganó la concesión por 25 años de la Hidrovía Paraná-Paraguay, por donde sale cerca del 80% del comercio exterior.",
     "https://eleconomista.com.ar/economia/la-privatizacion-mas-grande-era-milei-ya-tiene-dueno-cambia-ahora-hidrovia-n95924"),
    ("AR", "China", "deu", 1, "ICBC, banco del Estado chino, tiene en la Argentina su mayor operación fuera de China: más de un millón de hogares y 40.000 empresas, y un plan de financiamiento de proyectos por US$ 2.000 millones.",
     "https://www.bloomberglinea.com/latinoamerica/argentina/exclusiva-china-fuera-de-argentina-habla-el-ceo-local-de-icbc-tras-criticas-de-bessent-y-quirno/"),
    ("AR", "EE.UU.", "inv", 1, "JetSMART, controlada por el fondo estadounidense Indigo Partners, es la segunda aerolínea del país e invierte US$ 550 millones.",
     "https://www.emol.com/noticias/Economia/2026/06/18/1203245/jetsmart-inversion-argentina.html"),
    ("AR", "Reino Unido", "pre", 3, "Ocupa las Islas Malvinas, cuya soberanía reclama la Argentina, con una guarnición permanente en Monte Agradable.",
     "https://www.baenegocios.com/mundo/Reino-Unido-ratifica-la-presencia-militar-en-las-Malvinas-tras-las-crecientes-amenazas-20250624-0075.html"),

    # Buenos Aires
    ("06", "Japón y Corea", "inv", 2, "Toyota fabrica en Zárate la Hilux, la camioneta más vendida del país.",
     "https://www.iprofesional.com/autos/466280-que-marcas-y-modelos-de-autos-se-fabrican-en-argentina.amp"),
    ("06", "EE.UU.", "inv", 2, "Ford invirtió USD 700 millones en su planta de General Pacheco para la nueva Ranger.",
     "https://www.canal26.com/economia/2026/09/17/cae-la-produccion-desaparecen-modelos-y-crecen-las-importaciones-argentina-dejara-de-fabricar-autos/"),
    ("06", "Unión Europea", "inv", 1, "Volkswagen produce la Amarok en General Pacheco y Stellantis tiene su planta de El Palomar.",
     "https://www.iprofesional.com/autos/466280-que-marcas-y-modelos-de-autos-se-fabrican-en-argentina"),
    # CABA
    ("02", "EE.UU.", "deu", 1, "Colocó USD 600 millones en bonos bajo ley de Nueva York en noviembre de 2025.", BONOS),
    # Catamarca
    ("10", "China", "inv", 3, "Zijin Mining desarrolla el proyecto de litio Tres Quebradas, en Fiambalá, con una planta de carbonato de litio.",
     "https://www.iprofesional.com/negocios/358452-como-es-el-negocio-del-litio-y-20-proyectos-activos-en-argentina"),
    ("10", "Canadá y Australia", "inv", 2, "Rio Tinto (anglo-australiana) opera Fénix en el salar del Hombre Muerto; la australiana Galan desarrolla Hombre Muerto Oeste.",
     "https://chequeado.com/el-explicador/litio-en-jujuy-salta-y-catamarca-cuales-son-los-proyectos-mas-importantes-en-esta-region/"),
    ("10", "Japón y Corea", "inv", 1, "La coreana POSCO amplía Sal de Oro en el salar del Hombre Muerto.",
     "https://www.panorama-minero.com/en/news/argentina-s-56-lithium-projects-set-to-drive-record-investment-and-production"),
    ("10", "Israel", "pol", 1, MK, MEKOROT),
    # Córdoba
    ("14", "Unión Europea", "inv", 2, "Stellantis fabrica en Ferreyra (Fiat Cronos, Fiat Titano, Ram Dakota) y abrirá allí una planta de motores; Renault produce en Santa Isabel.",
     "https://www.iprofesional.com/autos/466280-que-marcas-y-modelos-de-autos-se-fabrican-en-argentina"),
    ("14", "EE.UU.", "deu", 2, "Colocó USD 725 millones en 2025 y USD 800 millones en enero de 2026 en el mercado internacional.",
     "https://www.tiempoar.com.ar/ta_article/otra-cara-del-ajuste-las-provincias-vuelven-a-endeudarse-en-dolares/amp/"),
    # Chubut
    ("26", "EE.UU.", "deu", 1, "Colocó USD 650 millones en bonos bajo ley de Nueva York, a diez años.",
     "https://www.iprofesional.com/finanzas/453234-chubut-coloco-deuda-por-650-millones-dolares-y-se-sumo-a-otras-provincias"),
    ("26", "Reino Unido", "inv", 1, "BP participa en el negocio petrolero a través de su alianza con Pan American Energy.",
     "https://www.perfil.com/noticias/economia/el-club-de-superpetroleras-globales-esquiva-la-argentina-y-no-entra-en-vaca-muerta.phtml"),
    # Entre Ríos
    ("30", "EE.UU.", "deu", 1, "Colocó USD 300 millones en el mercado internacional en febrero de 2026.", BONOS),
    # Formosa
    ("34", "Israel", "pol", 1, MK, MEKOROT),
    # Jujuy
    ("38", "China", "inv", 3, "Minera Exar, controlada por la china Ganfeng con la canadiense Lithium Americas, opera Cauchari-Olaroz.",
     "https://www.iprofesional.com/negocios/358452-como-es-el-negocio-del-litio-y-20-proyectos-activos-en-argentina"),
    ("38", "Canadá y Australia", "inv", 2, "Rio Tinto compró Arcadium Lithium, dueña de Olaroz; Lithium Americas es socia de Ganfeng en Exar.",
     "https://www.iprofesional.com/negocios/415286-litio-tras-la-fusion-de-rio-tinto-chinos-mueven-las-piezas-y-anticipan-mas-inversiones"),
    ("38", "Israel", "pol", 1, MK, MEKOROT),
    # La Rioja
    ("46", "Israel", "pol", 1, MK, MEKOROT),
    # Mendoza
    ("50", "Unión Europea", "pre", 1, "La Agencia Espacial Europea opera la antena de espacio profundo DSA 3 en Malargüe.",
     "https://www.argentina.gob.ar/node/309133"),
    ("50", "Israel", "pol", 1, MK, MEKOROT),
    # Neuquén
    ("58", "China", "pre", 3, "Estación de Espacio Lejano en la Pampa de Pilmatué (paraje Quintuco, departamento Loncopué, al norte de Bajada del Agrio), operada por la CLTC, que depende del Ejército Popular de Liberación; acuerdo por 50 años.",
     "https://chequeado.com/el-explicador/que-se-sabe-sobre-la-base-espacial-china-ubicada-en-neuquen/"),
    ("58", "EE.UU.", "inv", 2, "Chevron es la primera operadora extranjera de Vaca Muerta, cuarta en producción de petróleo.",
     "https://mase.lmneuquen.com/vaca-muerta/petroleras-vaca-muerta-el-top-five-del-primer-semestre-n1248407/amp"),
    ("58", "Reino Unido", "inv", 1, "Shell opera en bloques no convencionales de Vaca Muerta.",
     "https://www.perfil.com/noticias/economia/el-club-de-superpetroleras-globales-esquiva-la-argentina-y-no-entra-en-vaca-muerta.phtml"),
    ("58", "Unión Europea", "inv", 1, "La francesa TotalEnergies opera en Vaca Muerta.",
     "https://www.perfil.com/noticias/economia/el-club-de-superpetroleras-globales-esquiva-la-argentina-y-no-entra-en-vaca-muerta.phtml"),
    ("58", "EE.UU.", "deu", 1, "Volvió a Nueva York en julio de 2026 con USD 500 millones a siete años.", BONOS),
    ("58", "Israel", "pol", 1, "Figueroa firmó un convenio con Mekorot para estudiar los ríos de la provincia.",
     "https://www.rionegro.com.ar/?p=3504538"),
    # Río Negro
    ("62", "Reino Unido", "inv", 1, "Harbour Energy tiene el 15% de Southern Energy, el consorcio que exportará GNL desde el golfo San Matías.",
     "https://econojournal.com.ar/energia/energia-autorizo-la-primera-exportacion-anual-en-firme-de-gnl-durante-los-365-dias-del-ano/"),
    ("62", "Unión Europea", "inv", 1, "La italiana ENI es socia de YPF en Argentina LNG; la alemana SEFE compró 2 millones de toneladas anuales de GNL de Southern Energy.",
     "https://mase.lmneuquen.com/gas/del-subsuelo-al-oceano-como-avanzan-los-proyectos-gnl-n1216636"),
    ("62", "Golfo", "inv", 1, "XRG, brazo internacional de ADNOC (Emiratos Árabes Unidos), es socia de YPF en Argentina LNG.",
     "https://mase.lmneuquen.com/gas/del-subsuelo-al-oceano-como-avanzan-los-proyectos-gnl-n1216636"),
    ("62", "Israel", "pol", 1, MK, MEKOROT),
    # Salta
    ("66", "China", "inv", 3, "Ganfeng inauguró una planta de USD 980 millones y opera Mariana, Pozuelos-Pastos Grandes e Incahuasi.",
     "https://www.iprofesional.com/negocios/422902-argentina-consolida-su-liderazgo-en-litio-con-inauguracion-de-la-planta-de-ganfeng-lithium"),
    ("66", "Canadá y Australia", "inv", 2, "Rio Tinto amplía el proyecto de litio Rincón por USD 2.744 millones.",
     "https://www.todojujuy.com/pais/litio-jujuy-salta-y-catamarca-cuales-son-los-proyectos-mas-importantes-esta-region-n286652"),
    ("66", "Unión Europea", "inv", 1, "La francesa Eramet construye instalaciones en Centenario-Ratones.",
     "https://www.iprofesional.com/negocios/358452-como-es-el-negocio-del-litio-y-20-proyectos-activos-en-argentina"),
    ("66", "Japón y Corea", "inv", 1, "La coreana POSCO invierte en Sal de Oro.",
     "https://www.panorama-minero.com/en/news/argentina-s-56-lithium-projects-set-to-drive-record-investment-and-production"),
    # San Juan
    ("70", "Canadá y Australia", "inv", 3, "BHP (Australia) y Lundin (Canadá) desarrollan Vicuña, con una inversión inicial de USD 9.700 millones; la canadiense McEwen, Los Azules; la canadiense Barrick, Veladero.",
     "https://mase.lmneuquen.com/mineria/argentina-uno-uno-los-proyectos-mineros-que-ya-estan-construccion-n1246226"),
    ("70", "China", "inv", 1, "Shandong Gold es socia de Barrick en Veladero.",
     "https://mase.lmneuquen.com/mineria/argentina-uno-uno-los-proyectos-mineros-que-ya-estan-construccion-n1246226"),
    ("70", "Israel", "pol", 1, MK, MEKOROT),
    # Santa Cruz
    ("78", "EE.UU.", "inv", 2, "Newmont opera Cerro Negro, la mayor mina de oro de la provincia.",
     "https://mase.lmneuquen.com/minas-santa-cruz-oro-record"),
    ("78", "China", "inv", 2, "La china Gezhouba construye las represas del río Santa Cruz con financiamiento de bancos chinos; las obras se reactivaron en 2026.",
     "https://www.iprofesional.com/energia/468445-reactivan-las-represas-del-rio-santa-cruz-y-se-generaran-4-000-empleos"),
    ("78", "Reino Unido", "inv", 1, "Hochschild Mining controla San José.",
     "https://mase.lmneuquen.com/mineria/oro-y-plata-retroceso-cae-179-la-mineria-metalifera-y-patagonia-mira-sus-reservas-n1257092"),
    ("78", "Canadá y Australia", "inv", 1, "Pan American Silver opera Cerro Moro; McEwen tiene el 49% de San José.",
     "https://mase.lmneuquen.com/mineria/oro-precio-record-argentina-activa-proyectos-clave-exportar-us-5000-millones-n1224470"),
    ("78", "Israel", "pol", 1, MK, MEKOROT),
    # Santa Fe
    ("82", "EE.UU.", "inv", 2, "Bunge (con Viterra) y Cargill lideran la agroexportación desde las terminales del Gran Rosario.",
     "https://www.infocampo.com.ar/?p=594711"),
    ("82", "China", "inv", 2, "COFCO es la tercera agroexportadora del país.",
     "https://www.ellitoral.com/campolitoral/bunge-cargill-cofco-maiz-soja-trigo-girasol-bolsa-comercio-rosario-secretaria-agricultura-declaraciones-juradas-ventas-exterior_0_cq6O9cMO0q.html"),
    ("82", "Unión Europea", "inv", 1, "La francesa Louis Dreyfus Company está entre las cuatro mayores agroexportadoras.",
     "https://www.infocampo.com.ar/?p=594711"),
    ("82", "Unión Europea", "pre", 1, "La belga Jan De Nul draga y opera por 25 años el tramo santafesino de la hidrovía, frente a las terminales del Gran Rosario.",
     "https://eleconomista.com.ar/economia/la-privatizacion-mas-grande-era-milei-ya-tiene-dueno-cambia-ahora-hidrovia-n95924"),
    ("82", "EE.UU.", "deu", 1, "Colocó USD 800 millones a nueve años en diciembre de 2025.", BONOS),
    ("82", "Israel", "pol", 1, "Firmó acuerdos con Mekorot.", MEKOROT),
    # Santiago del Estero
    ("86", "Israel", "pol", 1, "Firmó acuerdos con Mekorot.", MEKOROT),
    # Tierra del Fuego
    ("94", "EE.UU.", "pre", 2, "El Comando Sur visitó Ushuaia en 2024 y 2025 y EE.UU. busca participar en la Base Naval Integrada; el Gobierno gestiona su financiamiento con Washington.",
     "https://www.perfil.com/noticias/politica/la-base-naval-integrada-de-ushuaia-el-proyecto-que-defensa-impulsa-desde-hace-decadas-y-que-milei-busca-reactivar.phtml"),
    ("94", "Reino Unido", "pre", 3, "Las Islas Malvinas, parte de la provincia según la ley argentina, están ocupadas por el Reino Unido, con presencia militar permanente.",
     "https://www.canal26.com/internacionales/2026/01/22/el-reino-unido-desafia-a-argentina-reafirma-la-defensa-de-su-soberania-en-las-islas-malvinas-al-desplegar-cazas-eurofighter/"),
]

# --- Ciudades (paso 4): influencias que llegan por las empresas y proyectos de cada ciudad. Clave "c:<slug>".
INFLUENCIAS += [
    ("c:zarate", "Japón y Corea", "inv", 3, "Toyota produce en Zárate desde 1997 (Hilux, SW4, Hiace), con la mayor producción y exportación automotriz del país; en 2026 anunció otra planta por 1.341 millones de dólares.", "https://www.noticiasnqn.com.ar/noticias/2026/11/16/361038-toyota-fabricara-la-tacoma-hibrida-en-argentina-producira-50000-unidades"),
    ("c:general-pacheco", "EE.UU.", "inv", 3, "Planta de Ford en General Pacheco, su principal centro industrial en el país.", "https://es.wikipedia.org/wiki/Ford_Argentina"),
    ("c:villa-constitucion", "Unión Europea", "inv", 3, "Acindar, la mayor siderúrgica de aceros largos del país, pertenece a ArcelorMittal, con sede en Luxemburgo.", "https://es.wikipedia.org/wiki/Acindar"),
    ("c:timbues", "China", "inv", 2, "Terminal y planta de COFCO, una de las mayores del Gran Rosario.", "https://www.magyp.gob.ar/sitio/areas/ss_mercados_agropecuarios/infraestructura/_archivos/000010_Puertos/_capacidad_almacenaje.php"),
    ("c:timbues", "Unión Europea", "inv", 2, "Complejo portuario e industrial de Louis Dreyfus Company, de origen francés y sede en Países Bajos.", "https://bcr.com.ar/es/print/pdf/node/73051"),
    ("c:puerto-general-san-martin", "EE.UU.", "inv", 2, "Terminales de Cargill (Quebracho), Bunge (Pampa y Dempa) y ADM (El Tránsito).", "https://bcr.com.ar/es/print/pdf/node/73051"),
    ("c:puerto-general-san-martin", "China", "inv", 2, "Terminal de COFCO (ex Nidera).", "https://bcr.com.ar/es/print/pdf/node/73051"),
    ("c:malargue", "Unión Europea", "pre", 3, "Estación de espacio profundo DSA 3 de la Agencia Espacial Europea.", "https://es.wikipedia.org/wiki/Malarg%C3%BCe"),
    ("c:estacion-de-espacio-lejano-quintuco", "China", "pre", 3, "Estación operada por la CLTC, que depende del Ejército Popular de Liberación, en un predio cedido por 50 años.", "https://www.a24.com/politica/el-gobierno-analiza-pedir-una-inspeccion-tecnica-la-base-espacial-china-neuquen-n1308479/amp"),
    ("c:susques", "China", "inv", 2, "Ganfeng Lithium tiene el 46,7 % de Cauchari-Olaroz.", "https://www.iprofesional.com/negocios/415286-litio-tras-la-fusion-de-rio-tinto-chinos-mueven-las-piezas-y-anticipan-mas-inversiones"),
    ("c:susques", "Reino Unido", "inv", 2, "Rio Tinto, anglo-australiana, opera Olaroz tras comprar Arcadium Lithium.", "https://mase.lmneuquen.com/mineria/litio-el-rigi-destraba-la-mayor-expansion-rio-tinto-fenix-n1233035"),
    ("c:fiambala", "China", "inv", 3, "Zijin Mining opera Tres Quebradas y su planta de carbonato de litio, aprobada en el RIGI por 709 millones de dólares.", "https://www.infobae.com/economia/2026/07/29/el-gobierno-aprobo-un-nuevo-proyecto-rigi-que-invertira-usd-709-millones-para-producir-litio-en-catamarca/"),
    ("c:antofagasta-de-la-sierra", "Reino Unido", "inv", 3, "Rio Tinto, anglo-australiana, opera Fénix y desarrolla Sal de Vida en el salar del Hombre Muerto.", "https://www.iprofesional.com/energia/451115-la-provincia-argentina-que-se-consolida-como-nuevo-polo-del-litio"),
    ("c:antofagasta-de-la-sierra", "Canadá y Australia", "inv", 2, "La australiana Galan Lithium opera la planta Hombre Muerto Oeste desde abril de 2026.", "https://www.infobae.com/economia/2026/07/29/el-gobierno-aprobo-un-nuevo-proyecto-rigi-que-invertira-usd-709-millones-para-producir-litio-en-catamarca/"),
    ("c:calingasta", "Canadá y Australia", "inv", 2, "La canadiense McEwen Copper desarrolla Los Azules, aprobado en el RIGI en 2025.", "https://www.mining-technology.com/news/argentina-approves-mcewens-2-7bn-copper-project-rigi/"),
    ("c:calingasta", "Reino Unido", "inv", 1, "Rio Tinto, por su firma Nuton, tiene el 17,2 % de Los Azules.", "https://skillings.net/mining-news-rio-tinto-explores-increased-stake-in-los-azules-copper-project"),
    ("c:anelo", "EE.UU.", "inv", 2, "Chevron, socia de YPF en Loma Campana, y otras petroleras estadounidenses en Vaca Muerta.", "https://es.wikipedia.org/wiki/Yacimiento_petrol%C3%ADfero_Vaca_Muerta"),
    ("c:anelo", "Reino Unido", "inv", 1, "Shell opera áreas en Vaca Muerta.", "https://es.wikipedia.org/wiki/Yacimiento_petrol%C3%ADfero_Vaca_Muerta"),
    ("c:anelo", "Unión Europea", "inv", 1, "TotalEnergies opera áreas en Vaca Muerta.", "https://es.wikipedia.org/wiki/Yacimiento_petrol%C3%ADfero_Vaca_Muerta"),
    ("c:embalse", "Canadá y Australia", "inv", 1, "La central nuclear usa un reactor CANDU de diseño canadiense.", "https://es.wikipedia.org/wiki/Central_nuclear_Embalse"),
]
