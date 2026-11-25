# El mapa del poder argentino (poderenargentina)

Sitio estático publicado con GitHub Pages desde `main` (raíz): https://francomartinlopez.github.io/poderenargentina/. Todo en español rioplatense neutro, con fechas ISO en los datos.
Responsable editorial: Franco Martín López. Proyecto hermano de El mapa del poder global (`podermundial`): mismo método, misma escala y misma estética. Ante una duda de método, vale lo que diga el CLAUDE.md de `podermundial`.

## Reglas
- La fuente de los datos es `fuente/*.py`. Nunca editar `data/territorio.json` a mano: correr `python3 scripts/generar_datos.py` y luego `node scripts/validate.js` (tiene que dar OK; los avisos de fuentes y población faltantes son pendientes conocidos).
- La cartografía (`data/provincias.json`, `data/antartida.json`, `data/dep/*.json`) sale del IGN vía Georef con `scripts/cartografia.sh`; no se edita a mano. Malvinas va en el mapa principal; la Antártida en el recuadro; las Georgias y las Sandwich del Sur no se dibujan (decisión de Franco, 19/11/2026).
- Se mide el poder real, no la jerarquía oficial. Escala, ejes, categorías y fórmula de puntaje: las del mapa global (21 ejes de 0 a 3; el 3 en este mapa es dominio a escala nacional), con una diferencia aprobada por Franco el 20/11/2026: el componente de categoría promedia 50/50 el teórico del mapa global y el relevado con las relaciones del mapa argentino (`scripts/puntaje.py`, publicado en `meta.act.cat_relevada`).
- Paraguas y componentes (20/11/2026): el ministerio (Defensa, Seguridad) lleva los ejes políticos y la capacidad material queda en cada fuerza; no se duplica capacidad entre un actor y los que dependen de él.
- Intendentes: ejes por la regla única de población de `scripts/puntaje.py` (`sc_intendente`), sea cual sea la tanda en que se cargaron. Gobiernos provinciales: plantilla con datos duros (población, recursos propios) en `fuente/actores_provinciales.py`.
- Resguardos: fuente obligatoria para vincular a alguien con delitos, grupos armados, narcotráfico o corrupción, o para calificar a un actor de fachada; en personas vivas, solo lo establecido por un tribunal u organismo oficial; nada especulativo sobre personas vivas. Las zonas liberadas solo con fuente.
- Neutralidad: mismo trato para oficialismo y oposición, sin adjetivos ni opinión en los datos.

## Ciudades
Entra una ciudad si cumple al menos un criterio, con el motivo escrito y una fuente:
1. Capital de provincia (y CABA).
2. Más de 100.000 habitantes (Censo 2022), medido sobre el aglomerado urbano del INDEC cuando la ciudad forma parte de uno.
3. Sede de poder económico aunque sea chica (criterio de Franco: Armstrong, General Deheza): sede o planta principal de un actor del mapa, cluster productivo de peso nacional, o «ciudad de una empresa» donde una firma domina el empleo y la vida local.
4. Relevancia estratégica: puerto, energía, minería, frontera, defensa.
Motivos en `fuente/ciudades.py`: cap, pob, emp, pue, ene, min, fro, def. Población en `fuente/poblacion_ciudades.py`: aglomerado (Censo 2022 y 2010) y localidad con su año; si el aglomerado une varias localidades, la cifra es la del conjunto y se dice. Coordenadas y departamento: `python3 scripts/ubicar_ciudad.py "<nombre>" "<provincia>"`.

## Departamentos
Panel corto (población, cabecera, actividad, intendente o comisionado, actores con sede); ficha propia solo para los relevantes, como los partidos del conurbano, Rosario o Vaca Muerta (decisión de Franco, 19/11/2026). Las fichas van en `fuente/departamentos.py` (cabecera, actividad, gobierno con fuente o None si el departamento reúne varios municipios, actores y fricción); en cada corte se revisan los intendentes y los interinatos.

## Influencias mundiales (paso 2)
Potencias de `fuente/influencias.py` (lista aprobada por Franco el 19/11/2026: EE.UU., China, Unión Europea, Reino Unido, Brasil, Rusia, Israel, Golfo, Canadá y Australia, Japón y Corea, y FMI, BM y BID; India sumada el 20/11/2026) puntuadas de 0 a 3 en cinco canales (comercio, inversión, deuda, presencia física o de seguridad, influencia política y cultural), con fuente, por país, provincia, departamento y ciudad. En las ciudades de empresa, la influencia sale sobre todo de los mercados y socios de esa empresa. El nivel país suma los vínculos del Estado nacional (FMI, Tesoro de EE.UU., swap chino).
- Comercio no se carga a mano: lo calcula el generador con los destinos de `fuente/economia.py` (40% o más de las exportaciones = 3; 20% a 40% = 2; 8% a 20% = 1). En el nivel país se miden también las importaciones (`COMERCIO_NACIONAL`, INDEC vía Cancillería) y vale el mayor de los dos puntajes (decisión del 19/11/2026, por China). Si el INDEC da un bloque, se aproxima: USMCA → EE.UU., Mercosur → Brasil; si da el país, vale el país.
- Inversión, deuda, presencia e influencia política: una entrada por dato, con fuente; 3 = controla el recurso, la deuda o la presencia principal; 2 = actor de primer orden entre varios; 1 = presencia relevante pero acotada.
- Potencia dominante = mayor suma, siempre que sume 3 o más o esté en dos canales (si no, «sin potencia dominante»); los empates se muestran como empate, nunca se desempatan por el orden de la lista. En las provincias que exportan menos de USD 400 M en el semestre, el comercio vale como máximo 1. Inversión en el nivel país: stock de inversión extranjera directa por país del BCRA.

## Alineamiento y quién manda (paso 2)
`fuente/alineamiento.py`: A aliado (acuerdos electorales con LLA), D dialoguista, I independiente (Provincias Unidas u otro espacio propio), O opositor; grupo que gobierna y desde cuándo; «manda» en una o dos frases; fuentes. Se revisa en cada corte y, en 2027, después de cada elección provincial.

## Elecciones 2027
`fuente/elecciones.py`: fecha de la elección provincial, si desdobla (S/N/None), nota y fuente; página «Elecciones». Solo fechas confirmadas o publicadas con fuente; se revisa en cada corte.

## Datos duros (paso 2)
Población: `python3 scripts/importar_censo.py` (INDEC, Censo 2022, cuadro 2 de cada provincia). Exportaciones: informe del INDEC «Origen provincial de las exportaciones» más reciente (semestral o anual; actualizar `PERIODO_EXPORTACIONES`). Recursos propios: ASAP (o la Oficina de Presupuesto del Congreso si ASAP no publica).

## Estética
Fondo negro, rojo de marca #E10600 para rellenos y #FF3B30 para texto. Tipografías: Big Shoulders Display, Archivo, Newsreader, JetBrains Mono. Símbolo: el del mapa global con la silueta de la Argentina dentro del círculo y el nodo rojo en Buenos Aires (img/logo.svg; reducido en img/favicon.svg). Vista previa para redes: img/og-mapa-argentino.png (1200×630); si cambian las cifras de la portada, se regenera.
En escritorio, el panel lateral mide lo mismo que el mapa y lleva lo principal; los bloques que aparecen al elegir van debajo, a lo ancho.

## Actores (paso 3)
`fuente/actores.py` (actores, fichas y relaciones) y `fuente/ejes.py` (ejes con anclas a escala nacional, pesos, categorías, alcance); el puntaje lo calcula `scripts/puntaje.py` con la fórmula del mapa global. Un actor que ya está en el mapa global usa el mismo id. El Estado no figura como bloque formal: figuran quienes ejercen el poder. Cada actor lleva ficha y fuentes; cada relación, una fuente. Las relaciones con actores del mapa global usan sus ids (`EXTERNOS`); los externos que no están en el mapa global van en `EXTERNOS_SIN_FICHA` y se muestran sin enlace. Excepciones al criterio de ciudades: `EXCEPCIONES` en `fuente/ciudades.py` (Junín y Goya, decisión de Franco del 19/11/2026).

## Ciudades: fichas (paso 4)
`fuente/ciudades_fichas.py`: INTENDENTES (a cargo, partido, familia, V = confirmado con fuente del año / W = Wikipedia, a confirmar), MANDA (empresa o enclave dominante) y CONFLICTOS (con fuente). Las influencias de una ciudad van en `fuente/influencias.py` con la clave `c:<slug>`. Poblaciones con último dato de 2001 o 2010: proyección propia a la fecha del corte con el crecimiento del departamento, siempre marcada como proyección. En cada corte se confirman los intendentes «W».

## Fricción y zonas liberadas (paso 5)
`fuente/friccion.py`: FRICCION (lugar, tipo, intensidad 3/2/1, estado, actores con ids del mapa o EXTERNOS, potencias, cronología con fuente por hito) y ZONAS (solo con fuente oficial o documentada; se dice si el Estado recuperó el control). Actores provinciales y municipales en `fuente/actores_provinciales.py`; actores por categoría (políticos, empresas, bandas con condena, Justicia, religiosos, ONG, medios) en `fuente/actores_mas.py`, `fuente/actores_mas2.py`, `fuente/actores_mas3.py`, `fuente/actores_mas4.py`, `fuente/actores_mas5.py`, `fuente/actores_mas6.py` y `fuente/actores_mas7.py` (el séptimo: energía, salud, Claro, UATRE, CONADU, SOMU, IDEA, ADEFA, Faro, ODSA, Cámara Federal, Corte de Santa Fe y Procuración del Tesoro; el sexto: organismos del Estado, Justicia electoral y bonaerense, PIA, UTA, SMATA, SUTEBA, UTHGRA, CAME, CAEM y Greenpeace; el quinto: intendentes de capitales con datos de `ciudades_fichas.py`, empresas de las ciudades de empresa, Bornoroni, Rosenkrantz, Ishii, Scaglione y Telefe; el cuarto: Fuerzas Armadas, UIF, policías, logística, tecnología, bancos, partidos y referentes; el tercero: fútbol, barras con condena, diplomacia, cámaras, intendentes; sede «dep:<código>» para actores de un partido sin ciudad propia; `NOMBRES` agrega a quien conduce un actor de `actores.py`) (el segundo con `TEXTOS`, el párrafo ampliado de los actores núcleo, y las relaciones de los gobernadores derivadas de `alineamiento.py`), con el ayudante `S(eje=valor)` (plantilla en el encabezado; los cuatro gobiernos de `actores.py` no se duplican). En cada corte se revisa el estado de cada punto y de cada zona.

## Presencia
`fuente/presencia.py`: provincias donde opera un actor fuera de la de su sede. El generador la deriva de los puntos de fricción y de las relaciones con actores de alcance provincial o municipal; lo demás va a mano, una entrada por dato con fuente. Las categorías de `EXCLUIDAS` (líderes, gobiernos, organismos, Justicia, fuerzas) solo tienen presencia cargada a mano.

## Normas para empresas
`fuente/normas.py`: NORMAS en tres niveles (Nación: Congreso, DNU y decretos, ARCA, BCRA, Comercio, Energía y Minería; provincias: Ingresos Brutos, Sellos, promoción industrial, compre local, ambiente y minería; localidades de más de 10.000 habitantes: tasas de comercio e industria, habilitaciones, zonificación y parques industriales). Cada norma: id, número, fecha ISO (o AAAA-MM), emisor, lugar ('AR', código de provincia, 'c:<slug>' o 'd:<código>'), rubros (ind, agro, min, ene, cons, com), resumen de una línea sin opinión y fuente (Boletín Oficial o, si no, una fuente que la cite). Si no tiene número publicado, se nombra y se agrega «(sin número publicado)»; se completa en la carga siguiente. FUNCIONARIOS: por provincia, quién regula Producción, Energía, Minería y Recaudación, con fuente. Página «Normas» con filtros por lugar y rubro; cada ficha de provincia, ciudad o partido muestra sus normas junto a sus autoridades. Primera etapa (25/11/2026): Santa Fe (Rosario, Gran Rosario y cordón), Córdoba y Gran Córdoba, AMBA y las provincias de energía y minería. Carga semanal para Nación y provincias, mensual para municipios (tareas programadas).

## Actualización trimestral
23 de febrero, mayo, agosto y noviembre (una semana después del mapa global). Subir `CORTE` y `PROXIMA` en `scripts/generar_datos.py`, subir el sufijo `?v=` de index.html, registrar en CHANGELOG.md y etiquetar el commit (`corte-AAAA-MM`). En 2027 conviene una revisión extra después de las elecciones de octubre y otra después de las asunciones del 10 de diciembre.
