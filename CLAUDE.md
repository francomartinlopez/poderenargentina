# El mapa del poder argentino (poderenargentina)

Sitio estático publicado con GitHub Pages desde `main` (raíz): https://francomartinlopez.github.io/poderenargentina/. Todo en español rioplatense neutro, con fechas ISO en los datos.
Responsable editorial: Franco Martín López. Proyecto hermano de El mapa del poder global (`podermundial`): mismo método, misma escala y misma estética. Ante una duda de método, vale lo que diga el CLAUDE.md de `podermundial`.

## Reglas
- La fuente de los datos es `fuente/*.py`. Nunca editar `data/territorio.json` a mano: correr `python3 scripts/generar_datos.py` y luego `node scripts/validate.js` (tiene que dar OK; los avisos de fuentes y población faltantes son pendientes conocidos).
- La cartografía (`data/provincias.json`, `data/antartida.json`, `data/dep/*.json`) sale del IGN vía Georef con `scripts/cartografia.sh`; no se edita a mano. Malvinas va en el mapa principal; la Antártida en el recuadro; las Georgias y las Sandwich del Sur no se dibujan (decisión pendiente de Franco).
- Se mide el poder real, no la jerarquía oficial. Escala, ejes, categorías y fórmula de puntaje: las del mapa global (21 ejes de 0 a 3; el 3 en este mapa es dominio a escala nacional).
- Resguardos: fuente obligatoria para vincular a alguien con delitos, grupos armados, narcotráfico o corrupción, o para calificar a un actor de fachada; en personas vivas, solo lo establecido por un tribunal u organismo oficial; nada especulativo sobre personas vivas. Las zonas liberadas solo con fuente.
- Neutralidad: mismo trato para oficialismo y oposición, sin adjetivos ni opinión en los datos.

## Ciudades
Entra una ciudad si cumple al menos un criterio, con el motivo escrito y una fuente:
1. Capital de provincia (y CABA).
2. Más de 100.000 habitantes (Censo 2022).
3. Sede de poder económico aunque sea chica (criterio de Franco: Armstrong, General Deheza): sede o planta principal de un actor del mapa, cluster productivo de peso nacional, o «ciudad de una empresa» donde una firma domina el empleo y la vida local.
4. Relevancia estratégica: puerto, energía, minería, frontera, defensa.
Motivos en `fuente/ciudades.py`: cap, pob, emp, pue, ene, min, fro, def. Coordenadas y departamento: `python3 scripts/ubicar_ciudad.py "<nombre>" "<provincia>"`.

## Influencias mundiales (paso 2)
Potencias de `fuente/influencias.py` puntuadas de 0 a 3 en cinco canales (comercio, inversión, deuda, presencia física o de seguridad, influencia política y cultural), con fuente, por país, provincia, departamento y ciudad. En las ciudades de empresa, la influencia sale sobre todo de los mercados y socios de esa empresa. El nivel país suma los vínculos del Estado nacional (FMI, Tesoro de EE.UU., swap chino).

## Estética
Fondo negro, rojo de marca #E10600 para rellenos y #FF3B30 para texto. Tipografías: Big Shoulders Display, Archivo, Newsreader, JetBrains Mono. Símbolo: el del mapa global con la silueta de la Argentina dentro del círculo y el nodo rojo en Buenos Aires (img/logo.svg; reducido en img/favicon.svg). Vista previa para redes: img/og-mapa-argentino.png (1200×630); si cambian las cifras de la portada, se regenera.
En escritorio, el panel lateral mide lo mismo que el mapa y lleva lo principal; los bloques que aparecen al elegir van debajo, a lo ancho.

## Actualización trimestral
23 de febrero, mayo, agosto y noviembre (una semana después del mapa global). Subir `CORTE` y `PROXIMA` en `scripts/generar_datos.py`, subir el sufijo `?v=` de index.html, registrar en CHANGELOG.md y etiquetar el commit (`corte-AAAA-MM`). En 2027 conviene una revisión extra después de las elecciones de octubre y otra después de las asunciones del 10 de diciembre.
