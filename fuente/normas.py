"""Normas que afectan a las empresas, en tres niveles: Nación, provincias y localidades.

Cada entrada: (id, número, fecha, emisor, lugar, rubros, resumen, fuente)
- fecha: 'AAAA-MM-DD' (publicación en el Boletín Oficial o, si no está, sanción); 'AAAA-MM' si solo se sabe el mes.
- lugar: 'AR' (Nación), código de provincia ('82'), 'c:<slug de ciudad>' o 'd:<código de partido o departamento>'.
- rubros: claves de RUBROS. Una norma general para todas las empresas lleva todos.
- número: el oficial. Si la norma todavía no tiene número publicado, se nombra y se agrega «(sin número publicado)» y se completa en el corte siguiente.
- resumen: una línea, sin adjetivos ni opinión.
- fuente: Boletín Oficial, organismo o, si no hay, un medio o estudio que cite la norma.

Cobertura de la primera etapa (25/11/2026): Nación; Santa Fe (Rosario, Gran Rosario y cordón industrial), Córdoba y Gran Córdoba,
AMBA (CABA y conurbano) y las provincias de energía y minería (Neuquén, Río Negro, Mendoza, San Juan, Catamarca, Salta, Jujuy,
Santa Cruz y Chubut). Localidades: solo las de más de 10.000 habitantes.
Carga: semanal para Nación y provincias; mensual para municipios (tareas programadas).
"""

RUBROS = {
    "ind": "Industria",
    "agro": "Agro",
    "min": "Minería",
    "ene": "Energía",
    "cons": "Construcción",
    "com": "Comercio y servicios",
}
TODOS = list(RUBROS)

NORMAS = [
    # ── Nación: Congreso ──
    ("ar-ley-27798", "Ley 27.798", "2026-01-02", "Congreso de la Nación", "AR", TODOS,
     "Presupuesto de la Administración Nacional para 2026.",
     "https://www.argentina.gob.ar/normativa/nacional/---422000/texto"),
    ("ar-ley-27799", "Ley 27.799", "2026-01-02", "Congreso de la Nación", "AR", TODOS,
     "Inocencia Fiscal: sube los umbrales del régimen penal tributario y crea un régimen simplificado de Ganancias.",
     "https://abogados.com.ar/nueva-ley-de-inocencia-fiscal-ley-27799/38286"),
    ("ar-ley-27802", "Ley 27.802", "2026-03-06", "Congreso de la Nación", "AR", TODOS,
     "Modernización laboral: cambia el régimen de contrato de trabajo y crea el RIMI y el Fondo de Asistencia Laboral (promulgada por Decreto 137/2026).",
     "https://kpmg.com/ar/es/home/media/novedades-tax/2026/03/9-de-marzo.html"),
    ("ar-ley-27804", "Ley 27.804", "2026-04-24", "Congreso de la Nación", "AR", ["min", "ene"],
     "Reforma de la ley de glaciares: las provincias definen las áreas periglaciares excluidas de la actividad minera.",
     "https://www.marval.com/publicacion/mining-news-abril-2026-17599"),
    # ── Nación: Poder Ejecutivo ──
    ("ar-dec-282-2026", "Decreto 282/2026", "2026-04-28", "Poder Ejecutivo Nacional", "AR", ["agro", "ind", "com"],
     "Medidas para la privatización de Belgrano Cargas y Logística.",
     "https://www.boletinoficial.gob.ar/pdf/aviso/primera/341224/20260428"),
    ("ar-dec-423-2026", "Decreto 423/2026", "2026-06-03", "Poder Ejecutivo Nacional", "AR", ["agro", "ene"],
     "Baja gradual de derechos de exportación de granos y biocombustibles hasta 2028; trigo y cebada al 5,5%.",
     "https://eleconomista.com.ar/economia/retenciones-gobierno-anuncio-una-baja-inmediata-elimino-impuestos-biodiesel-n95460"),
    ("ar-dnu-585-2026", "DNU 585/2026", "2026-07-13", "Poder Ejecutivo Nacional", "AR", ["ene"],
     "Prorroga la emergencia del sector energético hasta el 31 de diciembre de 2027.",
     "https://www.boletinoficial.gob.ar/detalleAviso/primera/344211/20260713"),
    ("ar-dec-1107-2026", "Decreto 1107/2026", "2026-09-28", "Poder Ejecutivo Nacional", "AR", ["ene"],
     "Autoriza la venta de la participación de Enarsa en las centrales térmicas Manuel Belgrano (Campana) y San Martín (Timbúes).",
     "https://eleconomista.com.ar/energia/el-gobierno-pone-venta-dos-gigantes-electricos-centrales-privatizara-cuanto-controla-estado-n98462"),
    # ── Nación: ARCA ──
    ("ar-rg-5824", "RG ARCA 5824/2026", "2026-02-13", "ARCA", "AR", ["com"],
     "Crea el comprobante de liquidación electrónica mensual.",
     "https://www.cronista.com/economia-politica/cambian-los-comprobantes-a-quienes-alcanza-la-nueva-normativa-de-arca-y-cuando-entra-en-vigencia"),
    ("ar-rgc-5849", "RG Conjunta 5849/2026", "2026-05-19", "ARCA, Secretaría de Agricultura y Secretaría de Energía", "AR", TODOS,
     "Reglamenta el RIMI: incentivos fiscales para inversiones de mipymes de USD 150.000 a 9 millones.",
     "https://www.argentina.gob.ar/node/501909"),
    ("ar-rg-5862", "RG ARCA 5862/2026", "2026-06-11", "ARCA", "AR", TODOS,
     "Reglamenta la promoción del empleo registrado del Título XXII de la Ley 27.802.",
     "https://www.boletinoficial.gob.ar/detalleAviso/primera/343004/20260611"),
    ("ar-rg-5872", "RG ARCA 5872/2026", "2026-07-03", "ARCA", "AR", ["agro", "ind", "min", "ene"],
     "Registro de contratos de exportación de bienes con cotización.",
     "https://kpmg.com/ar/es/tendencias/novedades-tax/2026/08/novedades-de-impuestos-y-legales.html"),
    ("ar-rg-5875", "RG ARCA 5875/2026", "2026-07-14", "ARCA", "AR", TODOS,
     "Plan de facilidades de pago para mipymes por deudas vencidas hasta el 30 de junio de 2026.",
     "https://www.boletinoficial.gob.ar/detalleAviso/primera/344290/20260714"),
    ("ar-rgc-5878", "RG Conjunta 5878/2026", "2026-07-23", "Secretaría de Minería y ARCA", "AR", ["min"],
     "Nuevo procedimiento para la devolución del IVA de la exploración minera.",
     "https://www.rsm.global/argentina/sites/default/files/media/documents/Boletin%20Informativo%202%C2%B0%20Julio%202026.pdf"),
    # ── Nación: BCRA ──
    ("ar-bcra-a8426", "Comunicación A 8426", "2026-04-23", "BCRA", "AR", ["ene", "min", "ind"],
     "Acceso al mercado de cambios para los proyectos adheridos al RIGI.",
     "https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8426.pdf"),
    ("ar-bcra-a8464", "Comunicación A 8464", "2026-08-06", "BCRA", "AR", TODOS,
     "Habilita el acceso al mercado de cambios para precancelar deuda y pagar primas desde el 10 de agosto.",
     "https://100seguro.com.ar/wp-content/uploads/2026/08/Comunicacion-BCRA-A-8464-2026.pdf"),
    ("ar-bcra-a8481", "Comunicación A 8481", "2026-09-14", "BCRA", "AR", TODOS,
     "Actualiza el texto ordenado de Exterior y Cambios.",
     "https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8481.pdf"),
    # ── Nación: Comercio e Industria, Energía y Minería ──
    ("ar-res-siyc-52", "Resolución SIyC 52/2026", "2026-02-27", "Secretaría de Industria y Comercio", "AR", ["ind", "com"],
     "Deroga la Resolución 171/2014 sobre importación temporaria.",
     "https://www.argentina.gob.ar/normativa/nacional/norma-423504/texto"),
    ("ar-res-se-400-2025", "Resolución SE 400/2025", "2025-10-21", "Secretaría de Energía", "AR", ["ene", "ind"],
     "Normaliza el Mercado Eléctrico Mayorista: contratos a término entre privados y menor rol de CAMMESA.",
     "https://www.marval.com/Publicacion/mercado-electrico-mayorista-normalizacion-y-modernizacion-17371"),
    ("ar-res-sm-68", "Resolución SM 68/2026", "2026-08-19", "Secretaría de Minería", "AR", ["min"],
     "Nuevos procedimientos del Régimen de Inversiones Mineras (Ley 24.196).",
     "https://www.estudio-ofarrell.com/?p=26752"),

    # ── Provincias ──
    # Santa Fe
    ("82-ley-14426", "Ley 14.426", "2025-12-23", "Legislatura de Santa Fe", "82", TODOS,
     "Código Fiscal e Impositiva 2026: deducción de Ingresos Brutos por sueldos de nuevos empleados y por hasta 30% del gasto en energía eléctrica.",
     "https://www.cpcesfe2.org.ar/tecnica/santa-fe-actualiza-su-codigo-fiscal-y-ley-impositiva-para-2026/"),
    # Córdoba
    ("14-ley-11160", "Ley 11.160", "2026-11-18", "Legislatura de Córdoba", "14", ["ind", "com", "agro"],
     "Régimen de incentivo a la inversión, la innovación y el empleo: exención de Ingresos Brutos, Sellos e Inmobiliario por diez años.",
     "https://web.cpcecba.org.ar/?p=70936"),
    # Buenos Aires
    ("06-ley-15558", "Ley 15.558", "2025-12-15", "Legislatura de Buenos Aires", "06", TODOS,
     "Ley Impositiva 2026 de la provincia: alícuotas de Ingresos Brutos, Sellos, Inmobiliario y Automotor.",
     "https://normas.gba.gob.ar/ar-b/ley/2025/15558/554025"),
    # CABA
    ("02-ley-6926", "Ley 6926", "2025-12-19", "Legislatura de la Ciudad de Buenos Aires", "02", TODOS,
     "Modificaciones al Código Fiscal de la Ciudad para 2026.",
     "https://boletinoficial.buenosaires.gob.ar/normativaba/norma/829856"),
    ("02-ley-6927", "Ley 6927", "2025-12-19", "Legislatura de la Ciudad de Buenos Aires", "02", TODOS,
     "Ley Impositiva 2026 (ex Ley Tarifaria): alícuotas de Ingresos Brutos y valores de tasas.",
     "https://www.colegio-escribanos.org.ar/noticias/2025_12_19_CABA-6927-LEY-TARIFARIA.pdf"),
    ("02-ley-6948", "Ley 6948", "2026-05-19", "Legislatura de la Ciudad de Buenos Aires", "02", ["com", "ind", "cons"],
     "Modifica las alícuotas de Ingresos Brutos por tramos de facturación.",
     "https://boletinoficial.buenosaires.gob.ar/normativaba/norma/855152"),
    # Neuquén
    ("58-ley-3541", "Ley 3541", "2025-12-23", "Legislatura de Neuquén", "58", TODOS,
     "Ley Impositiva 2026: alícuota general de Ingresos Brutos de 3% y baja promedio de 30% para unas 43.700 pymes.",
     "https://siap.blogdelcontador.com.ar/organismo/legislatura-neuquen/"),
    ("58-ley-gnl-ypf", "Ley del acuerdo GNL con YPF (sin número publicado)", "2026-06-24", "Legislatura de Neuquén", "58", ["ene"],
     "Ratifica el acta acuerdo con YPF para el GNL: regalías atadas al precio JKM, exención de Ingresos Brutos entre vehículos del RIGI y estabilidad por 30 años.",
     "https://www.iprofesional.com/energia/458334-ley-de-gnl-en-vaca-muerta-crea-un-nuevo-esquema-de-regalias-en-acuerdo-con-ypf"),
    ("58-impositiva-2027", "Ley Impositiva 2027 (sin número publicado)", "2026-11-18", "Legislatura de Neuquén", "58", TODOS,
     "Ley Impositiva y Código Fiscal para 2027.",
     "https://www.noticiasnqn.com.ar/noticias/2026/11/18/361395-neuquen-aprobo-la-ley-impositiva-y-el-codigo-fiscal-para-2027"),
    # Río Negro
    ("62-ley-5805", "Ley 5805", "2025-09-01", "Legislatura de Río Negro", "62", ["ene", "min", "ind", "cons", "com"],
     "Régimen de promoción y desarrollo de proveedores rionegrinos (compre local), aplicable también a proyectos del RIGI.",
     "https://web.legisrn.gov.ar/legislativa/legislacion/documento?id=11059"),
    # Mendoza
    ("50-rg-atm-27", "RG ATM 27/2026", "2026-06-11", "Administración Tributaria Mendoza", "50", ["com"],
     "Obliga a discriminar Ingresos Brutos en los comprobantes desde octubre (Ley 9655).",
     "https://boe.mendoza.gov.ar/publico/pdf_pedido/6ec5352b5caa9f8e95a3280325844549dce65fb702"),
    ("50-ley-hidrocarburos", "Ley de Hidrocarburos (sin número publicado)", "2026-11-10", "Legislatura de Mendoza", "50", ["ene"],
     "Nueva ley de hidrocarburos: regalía de referencia de 15% con oferta de los interesados, incentivos para campos maduros y no convencionales, y más multas ambientales.",
     "https://www.iprofesional.com/energia/468774-mendoza-sanciona-nueva-ley-de-hidrocarburos-para-impulsar-inversiones"),
    # San Juan
    ("70-ley-desarrollo-local-minero", "Ley de Desarrollo Local Minero (sin número publicado)", "2026-07-02", "Legislatura de San Juan", "70", ["min", "ind", "com"],
     "Ley de Desarrollo Local Minero: metas de 80% de empleo local y 60% de proveedores sanjuaninos en los proyectos mineros.",
     "https://www.ambito.com/energia/san-juan-endurece-el-compre-local-minero-nueva-ley-y-vicuna-acelera-la-incorporacion-proveedores-n6297090"),
    # Catamarca
    ("10-ley-5940", "Ley 5940", "2026-05-22", "Legislatura de Catamarca", "10", ["min"],
     "Ratifica el acuerdo de facilitación del proyecto minero Diablillos (AbraSilver), compartido con Salta.",
     "https://www.marval.com/Publicacion/mining-news-mayo-2026-17634"),
    ("10-ley-5956", "Ley 5956", "2026-10", "Legislatura de Catamarca", "10", ["min"],
     "Transforma a la minera estatal CAMYEN en sociedad anónima unipersonal.",
     "https://www.elancasti.com.ar/edicion-impresa/camyen-sera-una-sociedad-anonima-unipersonal-n619815"),
    # Salta
    ("66-ley-8524", "Ley 8524", "2025-12", "Legislatura de Salta", "66", ["min"],
     "Ratifica el acuerdo de facilitación del proyecto minero Diablillos (AbraSilver), compartido con Catamarca.",
     "https://www.elancasti.com.ar/abrasilver-celebro-la-sancion-definitiva-del-acuerdo-diablillos-catamarca-n612711"),
    ("66-dec-266-2026", "Decreto 266/2026", "2026-05-06", "Gobierno de Salta", "66", ["min"],
     "Aprueba el acta de asistencia técnica de la Región Minera del Litio con Jujuy, Catamarca y el CFI.",
     "https://www.marval.com/Publicacion/mining-news-mayo-2026-17634"),
    # Jujuy
    ("38-ley-6491", "Ley 6491", "2025-12-17", "Legislatura de Jujuy", "38", ["ind"],
     "Estímulos fiscales a la industria hasta 2030 y régimen de regularización de deudas tributarias.",
     "https://siap.blogdelcontador.com.ar/novedades/jujuy-implementa-una-nueva-ley-de-estimulos-fiscales-para-impulsar-la-industria-y-regularizar-deudas-tributarias/"),
    ("38-ley-6492", "Ley 6492", "2025-12-18", "Legislatura de Jujuy", "38", TODOS,
     "Ley Impositiva 2026 de la provincia.",
     "https://siap.blogdelcontador.com.ar/?p=78056"),
    ("38-dec-4900", "Decreto Acuerdo 4900-JG/2025", "2026-01-21", "Gobierno de Jujuy", "38", ["min"],
     "Crea el Ministerio de Minería, que absorbe la Secretaría de Minería e Hidrocarburos y el Juzgado Administrativo de Minas.",
     "https://abogados.com.ar/mineria/38440"),
    ("38-ley-6512", "Ley 6512", "2026-06-24", "Legislatura de Jujuy", "38", ["com"],
     "Régimen transitorio de asistencia fiscal al comercio.",
     "https://indicadores.ar/legislacion/jujuy"),
    # Santa Cruz
    ("78-dec-incentivos-petroleo", "Decreto de incentivos petroleros (sin número publicado)", "2026-04-08", "Gobierno de Santa Cruz", "78", ["ene"],
     "Esquema de incentivos para operadoras petroleras en áreas maduras.",
     "https://www.iprofesional.com/energia/452016-como-es-nuevo-esquema-incentivos-que-lanzo-esta-provincia-para-sector-petrolero"),
    # Chubut
    ("26-ley-convenio-ypf", "Ley del convenio con YPF (sin número publicado)", "2026-07-02", "Legislatura de Chubut", "26", ["ene"],
     "Ratifica el convenio de salida de YPF de áreas convencionales del Golfo San Jorge: compensación de unos USD 25 millones y traspaso de bienes a la provincia.",
     "https://diariojornada.com.ar/419555/politica/la_legislatura_aprobo_el_acuerdo_entre_chubut_e_ypf"),

    # ── Localidades de más de 10.000 habitantes ──
    ("c-rosario-ord-10876", "Ordenanza 10.876", "2026-02", "Concejo Municipal de Rosario", "c:rosario", ["ind", "com"],
     "Crea el registro voluntario de huella de carbono para empresas e instituciones.",
     "https://www.ellitoral.com/informacion-general/funciona-registro-empresas-instituciones_0_4g6zqkXDbV.html"),
    ("c-santa-fe-ord-13095", "Ordenanza 13.095", "2025-12", "Concejo Municipal de Santa Fe", "c:santa-fe", TODOS,
     "Ordenanza Tributaria Anual: Derecho de Registro e Inspección (DReI) atado al Módulo Tributario.",
     "https://www.ellitoral.com/area-metropolitana/ciudad-capitalaumentan-tasas-derechos-santafe-modulo-tributario-derecho-registro-inspeccion-comercios-industrias-cementerio-espectaculos-publicos_0_lIU0uSHgMv.html"),
    ("c-santa-fe-res-25592", "Resolución HCM 25.592", "2025-11-27", "Concejo Municipal de Santa Fe", "c:santa-fe", ["com"],
     "Pide eximir de TGI y DReI por seis meses a los comercios de la avenida J. J. Paso afectados por obras.",
     "https://transparencia.santafeciudad.gov.ar/wp-content/uploads/2025/12/resolucion-hcm-25.592.pdf"),
    ("c-cordoba-ord-13562", "Ordenanza 13.562", "2025-12", "Concejo Deliberante de Córdoba", "c:cordoba", ["ind", "com"],
     "Régimen de Promoción de Actividades Productivas, vigente desde diciembre de 2025.",
     "https://hoydia.com.ar/?p=335460"),
    ("c-la-plata-ord-12682", "Ordenanza 12.682", "2025-12", "Concejo Deliberante de La Plata", "c:la-plata", TODOS,
     "Ordenanza Impositiva: alícuotas máximas y mínimos de la Tasa por Inspección de Seguridad e Higiene por actividad.",
     "https://sibom.slyt.gba.gob.ar/bulletins/14010/contents/2319885"),
    ("c-bahia-blanca-ord-22252", "Ordenanza 22.252", "2025-11-27", "Concejo Deliberante de Bahía Blanca", "c:bahia-blanca", TODOS,
     "Ordenanza Fiscal 2026: tasas municipales, entre ellas la de Inspección de Seguridad e Higiene.",
     "https://www.bahia.gob.ar/wp-content/uploads/2026/01/Ordenanza-Fiscal-2026.pdf"),
    ("d-06560-ord-7437", "Ordenanza 7437/25", "2025-12-11", "Concejo Deliberante de Moreno", "d:06560", TODOS,
     "Ordenanza Fiscal 2026: habilitación de comercios e industrias y Tasa por Inspección de Seguridad e Higiene.",
     "https://sibom.slyt.gba.gob.ar/bulletins/14607/contents/2361352"),
    ("d-06638-ord-112", "Ordenanza 112/2025", "2025-12", "Concejo Deliberante de Pilar", "d:06638", TODOS,
     "Ordenanza Impositiva 2026 (Decreto 1661/2025): valores de las tasas municipales, incluidas las de comercios e industrias.",
     "https://pilar.gov.ar/wp-content/uploads/2025/12/ORDENANZA-IMPOSITIVA-2026.pdf"),
    ("c-neuquen-tarifaria-2026", "Ordenanza Tarifaria 2026", "2025-12-04", "Concejo Deliberante de Neuquén", "c:neuquen", ["com", "ind", "ene"],
     "Elimina las tasas de Residuos Urbanos y Forestal-Habitacional, que pagaban comercios, industrias y empresas petroleras.",
     "https://www.noticiasnqn.com.ar/noticias/2025/12/04/324414-el-deliberante-aprobo-el-presupuesto-y-tarifaria-2026-con-fuerte-foco-en-obras-y-alivio-fiscal"),
]

# Funcionarios que regulan cada rubro en cada provincia: (área, cargo, nombre o None si solo se conoce el organismo, fuente).
# Áreas: Producción, Energía, Minería, Recaudación. Faltantes: se completan en la carga semanal.
FUNCIONARIOS = {
    "82": [("Producción", "Ministro de Desarrollo Productivo", "Gustavo Puccini", "https://www.santafe.gov.ar/noticias/noticia/287290/"),
           ("Recaudación", "Ministro de Economía (del que depende la API)", "Pablo Olivares", "https://www.santafe.gov.ar/noticias/noticia/285603/")],
    "14": [("Producción", "Ministro de Producción", "Fernando Sibilla", "https://www.santafe.gov.ar/noticias/noticia/287290/")],
    "06": [("Recaudación", "Director ejecutivo de ARBA", "Cristian Girard", "https://www.cronista.com/economia-politica/tres-de-cuatro-autos-tendran-un-alivio-en-patente-que-pasara-con-los-otros-impuestos-en-2026")],
    "58": [("Producción", "Ministro de Economía, Producción e Industria", "Guillermo Koenig", "https://www.noticiasnqn.com.ar/noticias/2026/11/07/359958-presupuesto-2027-en-neuquen-koenig-explicara-el-plan-de-gastos-en-la-legislatura")],
    "62": [("Producción", "Ministro de Desarrollo Económico y Productivo", "Carlos Banacloy", "https://rionegro.gov.ar/articulo/59066/rio-negro-fortalece-control-energetico-y-ambiental-con-nueva-sede-en-roca"),
           ("Energía", "Secretaria de Energía y Ambiente", "Andrea Confini", "https://rionegro.gov.ar/articulo/59066/rio-negro-fortalece-control-energetico-y-ambiental-con-nueva-sede-en-roca"),
           ("Recaudación", "Agencia de Recaudación Tributaria", None, "https://rionegro.gov.ar/articulo/61731/control-tributario-especializado-para-las-grandes-obras-energeticas-de-rio-negro")],
    "50": [("Energía", "Ministra de Energía y Ambiente", "Jimena Latorre", "https://www.losandes.com.ar/economia/petroleo-cornejo-anuncio-que-enviara-legislatura-un-proyecto-actualizacion-la-ley-hidrocarburos-n5989640"),
           ("Minería", "Director de Minería", "Jerónimo Shantal", "https://www.mendoza.gov.ar/prensa/con-la-sancion-del-senado-la-reforma-que-moderniza-el-codigo-de-procedimiento-minero-de-mendoza-ya-es-ley/"),
           ("Recaudación", "Administrador general de ATM", "Alejandro Luis Donati", "https://boe.mendoza.gov.ar/publico/pdf_pedido/6ec5352b5caa9f8e95a3280325844549dce65fb702")],
    "70": [("Producción", "Ministro de Producción", "Gustavo Fernández", "https://www.tiempodesanjuan.com/economia/la-ley-desarrollo-local-minero-san-juan-entra-su-fase-final-y-se-espera-que-sea-tratada-mayo-n429353/amp"),
           ("Minería", "Ministro de Minería", "Juan Pablo Perea", "https://www.tiempodesanjuan.com/politica/perea-la-media-sancion-la-ley-glaciares-es-una-satisfaccion-que-se-les-devuelva-las-provincias-las-facultades-evaluar-su-ambiente-periglaciar-n424125")],
    "10": [("Minería", "Ministra de Minería", "Teresita Regalado", "https://www.elancasti.com.ar/teresita-regalado-a30869"),
           ("Recaudación", "Agencia de Recaudación de Catamarca (ARCA)", None, "https://digesto.catamarca.gob.ar/digesto/crearpdf/decreto/2021")],
    "66": [("Producción", "Ministro de Producción y Minería", "José Ignacio Lupión", "https://www.letrap.com.ar/economia/salta-quien-es-el-ministro-que-le-da-otra-vuelta-rosca-al-perfil-minero-la-gestion-gustavo-saenz-n5420982"),
           ("Minería", "Secretario de Minería", "Gustavo Carrizo", "https://www.diariopanorama.com/noticia/538200/hay-oportunidades-no-podemos-desaprovechar-salta-busca-acelerar-mineria")],
    "38": [("Minería", "Ministro de Minería", "José Gabriel Gómez", "https://www.todojujuy.com/jujuy/jose-gabriel-gomez-asumio-como-ministro-mineria-jujuy-n284462")],
    "26": [("Energía", "Ministro de Hidrocarburos", "Federico Ponce", "https://cholilaonline.ar/2026/04/federico-ponce-detallo-el-plan-petrolero-en-chubut-es-una-epoca-de-transicion-compleja.html")],
}
AREAS = ["Producción", "Energía", "Minería", "Recaudación"]
