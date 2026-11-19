# El mapa del poder argentino (poderenargentina)

Sitio estático publicado con GitHub Pages desde `main` (raíz): https://francomartinlopez.github.io/poderenargentina/. Todo en español rioplatense neutro, con fechas ISO en los datos.
Responsable editorial: Franco Martín López. Proyecto hermano de El mapa del poder global (`podermundial`): mismo método, misma escala y misma estética. Ante una duda de método, vale lo que diga el CLAUDE.md de `podermundial`.

## Reglas
- La fuente de los datos es `fuente/*.py`. Nunca editar `data/territorio.json` a mano: correr `python3 scripts/generar_datos.py` y luego `node scripts/validate.js` (tiene que dar OK; los avisos de fuentes y población faltantes son pendientes conocidos).
- La cartografía (`data/provincias.json`, `data/antartida.json`, `data/dep/*.json`) sale del IGN vía Georef con `scripts/cartografia.sh`; no se edita a mano. Malvinas va en el mapa principal; la Antártida en el recuadro; las Georgias y las Sandwich del Sur no se dibujan (decisión de Franco, 19/11/2026).
- Se mide el poder real, no la jerarquía oficial. Escala, ejes, categorías y fórmula de puntaje: las del mapa global (21 ejes de 0 a 3; el 3 en este mapa es dominio a escala nacional).
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
Potencias de `fuente/influencias.py` (lista aprobada por Franco el 19/11/2026: EE.UU., China, Unión Europea, Reino Unido, Brasil, Rusia, Israel, Golfo, Canadá y Australia, Japón y Corea, y FMI, BM y BID) puntuadas de 0 a 3 en cinco canales (comercio, inversión, deuda, presencia física o de seguridad, influencia política y cultural), con fuente, por país, provincia, departamento y ciudad. En las ciudades de empresa, la influencia sale sobre todo de los mercados y socios de esa empresa. El nivel país suma los vínculos del Estado nacional (FMI, Tesoro de EE.UU., swap chino).
- Comercio no se carga a mano: lo calcula el generador con los destinos de `fuente/economia.py` (40% o más de las exportaciones = 3; 20% a 40% = 2; 8% a 20% = 1). Si el INDEC da un bloque, se aproxima: USMCA → EE.UU., Mercosur → Brasil; si da el país, vale el país.
- Inversión, deuda, presencia e influencia política: una entrada por dato, con fuente; 3 = controla el recurso, la deuda o la presencia principal; 2 = actor de primer orden entre varios; 1 = presencia relevante pero acotada.
- Potencia dominante = mayor suma; los empates se muestran como empate, nunca se desempatan por el orden de la lista.

## Alineamiento y quién manda (paso 2)
`fuente/alineamiento.py`: A aliado (acuerdos electorales con LLA), D dialoguista, I independiente (Provincias Unidas u otro espacio propio), O opositor; grupo que gobierna y desde cuándo; «manda» en una o dos frases; fuentes. Se revisa en cada corte y, en 2027, después de cada elección provincial.

## Datos duros (paso 2)
Población: `python3 scripts/importar_censo.py` (INDEC, Censo 2022, cuadro 2 de cada provincia). Exportaciones: informe del INDEC «Origen provincial de las exportaciones» más reciente (semestral o anual; actualizar `PERIODO_EXPORTACIONES`). Recursos propios: ASAP (o la Oficina de Presupuesto del Congreso si ASAP no publica).

## Estética
Fondo negro, rojo de marca #E10600 para rellenos y #FF3B30 para texto. Tipografías: Big Shoulders Display, Archivo, Newsreader, JetBrains Mono. Símbolo: el del mapa global con la silueta de la Argentina dentro del círculo y el nodo rojo en Buenos Aires (img/logo.svg; reducido en img/favicon.svg). Vista previa para redes: img/og-mapa-argentino.png (1200×630); si cambian las cifras de la portada, se regenera.
En escritorio, el panel lateral mide lo mismo que el mapa y lleva lo principal; los bloques que aparecen al elegir van debajo, a lo ancho.

## Actores (paso 3)
`fuente/actores.py` (actores, fichas y relaciones) y `fuente/ejes.py` (ejes con anclas a escala nacional, pesos, categorías, alcance); el puntaje lo calcula `scripts/puntaje.py` con la fórmula del mapa global. Un actor que ya está en el mapa global usa el mismo id. El Estado no figura como bloque formal: figuran quienes ejercen el poder. Cada actor lleva ficha y fuentes; cada relación, una fuente. Las relaciones con actores del mapa global usan sus ids (`EXTERNOS`). Excepciones al criterio de ciudades: `EXCEPCIONES` en `fuente/ciudades.py` (Junín y Goya, decisión de Franco del 19/11/2026).

## Ciudades: fichas (paso 4)
`fuente/ciudades_fichas.py`: INTENDENTES (a cargo, partido, familia, V = confirmado con fuente del año / W = Wikipedia, a confirmar), MANDA (empresa o enclave dominante) y CONFLICTOS (con fuente). Las influencias de una ciudad van en `fuente/influencias.py` con la clave `c:<slug>`. Poblaciones con último dato de 2001 o 2010: proyección propia a la fecha del corte con el crecimiento del departamento, siempre marcada como proyección. En cada corte se confirman los intendentes «W».

## Fricción y zonas liberadas (paso 5)
`fuente/friccion.py`: FRICCION (lugar, tipo, intensidad 3/2/1, estado, actores con ids del mapa o EXTERNOS, potencias, cronología con fuente por hito) y ZONAS (solo con fuente oficial o documentada; se dice si el Estado recuperó el control). Actores provinciales y municipales en `fuente/actores_provinciales.py` (plantilla en el encabezado; los cuatro gobiernos de `actores.py` no se duplican). En cada corte se revisa el estado de cada punto y de cada zona.

## Actualización trimestral
23 de febrero, mayo, agosto y noviembre (una semana después del mapa global). Subir `CORTE` y `PROXIMA` en `scripts/generar_datos.py`, subir el sufijo `?v=` de index.html, registrar en CHANGELOG.md y etiquetar el commit (`corte-AAAA-MM`). En 2027 conviene una revisión extra después de las elecciones de octubre y otra después de las asunciones del 10 de diciembre.
