# Cambios

## 2026-11-19 (j) · Periodistas y streaming

- Once actores de medios, con programa verificado en 2026: Carlos Pagni, Joaquín Morales Solá, Hugo Alconada Mon, Eduardo Feinmann, Luis Majul, Jonatan Viale, Marcelo Longobardi (último programa confirmado, 2024), Gustavo Sylvestre, Olga, Luzu TV y Blender. Relaciones solo con hechos documentados (medio donde trabajan, cruces públicos con el Gobierno, la AFA o colegas, propiedad de Blender y Carajo). 211 actores y 328 relaciones.

## 2026-11-19 (i) · 200 actores, relaciones con fuente, fichas ampliadas y la Antártida

- Actores (`fuente/actores_mas2.py`): 88 nuevos, hasta llegar a 200. Estado nacional (Cancillería, Justicia, Salud, ANSES, INDEC, CNV, ENACOM, AGN, ARSAT, FAdeA, Nucleoeléctrica, Yacyretá, Aerolíneas, INVAP, Banco Provincia), Gendarmería, Prefectura y Policía Federal, Fiscalía de Santa Fe, Rosatti, Lorenzetti y Lijo, UBA y CIN, embajadas de EE.UU. y China, dirigentes (Mayans, Germán Martínez, Ritondo, Pareja, «Lule» Menem, Grabois, Pichetto, La Cámpora, Frente de Izquierda, Fundación Pensar), sindicatos (UOM, ATE, Aceiteros, La Bancaria, UOCRA, UPCN, Sanidad, CTA, CTERA, FreSU, APLA, Comercio, La Fraternidad), agro (Federación Agraria, CRA, Coninagro, Bolsa de Comercio de Rosario), empresas (Telecom, Pluspetrol, Rio Tinto, Vicuña, Southern Energy, Acindar, Molinos, IRSA, BYMA), familias y empresarios (Pérez Companc, Bulgheroni, Galperin, Mindlin, Rocca, Magnetto, Elsztain, Vila-Manzano, Brito, Galicia, Pagani, Urquía, Blaquier), bandas con condena (Fran Riquelme, Delfín Zacarías, Pupito Avalle, Los Picudos), Boca y River, Madres, Chequeado, CIPPEC, Poder Ciudadano, Página/12, Cadena 3 y La Capital.
- Relaciones: de 125 a 305, todas con fuente. La relación de cada gobernador con la Nación, con Provincias Unidas y con su partido sale de `fuente/alineamiento.py`. Ahora puede haber más de una relación por par si son de distinto tipo.
- Fichas: párrafo ampliado («txt», en `TEXTOS`) para 40 actores núcleo; la ficha suma de quién depende el actor, sus puntos de fricción, los departamentos donde pesa y los actores con sede en la misma ciudad; las relaciones se ordenan por intensidad.
- Fricción: «Antártida: tres reclamos superpuestos» (Argentina 25°–74° O, Reino Unido 20°–80° O, Chile 53°–90° O), con diagrama de los sectores en su ficha y marca en el recuadro antártico del mapa. Los actores nuevos se sumaron a Malvinas, la Milla 201, la hidrovía, Rosario, la reforma laboral, Acindar, el litio y Aguas Blancas (19 puntos).

## 2026-11-19 (h) · Más actores, más fricción, selector de capas e influencias más claras

- Actores (`fuente/actores_mas.py`): 41 nuevos por categoría: dirigentes políticos (Villarruel, Bullrich, Martín Menem, Macri, Massa, Máximo Kirchner, Provincias Unidas, Las Fuerzas del Cielo), ministerios de Desregulación y Capital Humano, empresas y grupos (Vista, Aluar, Werthein, Galicia, Macro, COFCO, Cargill, Ledesma), bandas criminales con condena (Alvarado, Funes), Justicia (Procuración, Consejo de la Magistratura, Casación, juzgado electoral), religiosos (Arzobispado de Buenos Aires, DAIA, AMIA, ACIERA), organizaciones sociales y ONG (CELS, Abuelas, Fundación Libertad, Fundación Mediterránea, Movimiento Evita, Polo Obrero) y medios y periodistas (Grupo América, La Nación, Infobae, C5N, Perfil, Neura, El Destape). 112 actores y 125 relaciones. Página Actores con filtro por categoría y buscador.
- Fricción: pesca ilegal en la Milla 201, Estrecho de Magallanes y la frontera austral con Chile, conflicto territorial mapuche en Villa Mascardi y Lago Escondido (18 puntos).
- Influencias: el país ahora mide el comercio por exportaciones e importaciones (vale el mayor puntaje), así China, primer origen de las importaciones, puntúa 2. Cuadro rediseñado: una fila por potencia con total, cinco canales con nombre y los datos y fuentes de cada potencia al tocar la fila. Se aclara que en las provincias el INDEC solo publica los destinos principales.
- Mapa: selector «Ver en el mapa» en lugar de botones con desplazamiento lateral; selector de potencia y de indicador económico.

## 2026-11-19 (g) · Pendientes y mejoras: intendentes, censo, departamentos, actores locales y más fricción

- Intendentes: 39 confirmados con fuente de 2026 o reciente (92 en total con «V»); nuevos Paso de los Libres (Miguel Arias) y Perito Moreno (Matías Trepo); se suman Calingasta, Susques (comisión municipal; municipio desde junio de 2026) y Aguas Blancas (intervenida, a confirmar). Quedan cuatro «a confirmar» (Villa Mercedes, Orán, Salvador Mazza, Aguas Blancas) y dos sin dato (Timbúes, San Antonio de los Cobres).
- Censo 2022 de localidades: Susques (1.374) y Calingasta (2.722) dejan la proyección. San Antonio de los Cobres, Antofagasta de la Sierra, San José de Jáchal y Salvador Mazza siguen proyectadas: el INDEC no publica la localidad o no se encontró el dato.
- Fichas de departamento (`fuente/departamentos.py`): 18 partidos y departamentos relevantes (La Matanza, Lomas de Zamora, Quilmes, Lanús, Avellaneda, Almirante Brown, Florencio Varela, Ezeiza, Merlo, Moreno, San Martín, Tres de Febrero, Tigre, Pilar, Rosario, San Lorenzo, Confluencia y Añelo), con cabecera, quién gobierna (incluidos los interinatos de Quilmes, Almirante Brown y Avellaneda), actividad, actores y fricción, con fuentes.
- Actores locales: Sindicato de Petroleros Privados (Neuquén), aceiteros de San Lorenzo (SOEA), UOM Villa Constitución, SMATA Córdoba, Gas y Petróleo del Neuquén y JEMSE (Jujuy). 71 actores y 82 relaciones.
- Fricción: cinco puntos nuevos con cronología y fuentes: puerto de Dock Sud, Andalgalá y el proyecto MARA, paros aceiteros en el Gran Rosario, salarios y tarifas en Vaca Muerta y Acindar en Villa Constitución (14 en total). No se sumaron zonas liberadas: ninguna nueva tiene fuente oficial.
- Validador: ahora frena de verdad ante fricción sin fuente (antes avisaba después de cerrar) y revisa las fichas de departamento.

## 2026-11-19 (f) · Paso 5: actores locales, fricción y zonas liberadas

- Cierre del paso 4: 93 ciudades con intendente (51 confirmados con fuente de 2026, 42 «a confirmar»). Nuevos confirmados: Córdoba, Santiago del Estero (Benavente), Puerto Madryn, Bariloche, Villa María, Antofagasta de la Sierra, La Banda, Libertador General San Martín, La Quiaca y Puerto Piray; Salvador Mazza, a confirmar. Siguen sin dato Timbúes, Susques, San Antonio de los Cobres, Calingasta y Aguas Blancas (intervenido).
- Actores provinciales y municipales (`fuente/actores_provinciales.py`): los gobiernos de las otras 20 jurisdicciones, con plantilla documentada y relación con la Nación según su alineamiento; Gerardo Zamora; los intendentes de Rosario y Córdoba. 65 actores y 74 relaciones.
- Puntos de fricción (`fuente/friccion.py`): Malvinas, estación china de Neuquén, hidrovía, Base Naval Integrada de Ushuaia, violencia narco en Rosario, Triple Frontera, litio en la Puna, CGT frente a la reforma laboral y frontera Aguas Blancas–Bermejo, con intensidad, actores, potencias, cronología y fuentes.
- Zonas liberadas: solo las documentadas por un organismo oficial; por ahora, la ribera del Bermejo en Aguas Blancas, con su estado actual.
- Sitio: capas Fricción y Zonas liberadas; página Fricción (`#friccion`) y ficha de cada punto (`#f-<id>`); fricción en las fichas de provincia y ciudad. Validador ampliado.

## 2026-11-19 (e) · Paso 4: fichas de ciudades

- Quién gobierna (`fuente/ciudades_fichas.py`): intendente de 89 ciudades. Las capitales y los partidos bonaerenses, confirmados con fuentes de 2026 (incluidos los interinatos de Mar del Plata, San Nicolás y Junín); el resto, tomado de Wikipedia y marcado «a confirmar». Nueve localidades siguen sin dato.
- Quién manda en las ciudades de empresa (General Deheza, Arroyito, Villa Constitución, Zárate, Fiambalá, Antofagasta de la Sierra y otras).
- Influencias mundiales propias de 13 ciudades, por las empresas y proyectos con sede en ellas (Toyota en Zárate, Ford en Pacheco, COFCO y Dreyfus en Timbúes, Zijin en Fiambalá, Rio Tinto en el Hombre Muerto, la ESA en Malargüe, la estación china, entre otras), con fuente.
- Conflictos documentados: Rosario, Fiambalá, Jáchal y Gualeguaychú.
- Población: las seis localidades con último dato de 2001 o 2010 muestran una proyección propia a 2026 con el crecimiento del departamento (INDEC), marcada como proyección. Puerto Piray y Fiambalá pasan al Censo 2022.
- Sitio: ficha de ciudad con quién gobierna, influencias y conflictos; columna de intendente en la tabla de Ciudades.

## 2026-11-19 (d) · Paso 3: actores núcleo nacionales

- 42 actores nacionales (`fuente/actores.py`) medidos en los 21 ejes con la fórmula del mapa global (`fuente/ejes.py`, `scripts/puntaje.py`): conducción del Ejecutivo, Economía, BCRA, ARCA, Banco Nación, SIDE, Fuerzas Armadas, fuerzas federales, Corte, Comodoro Py, Congreso, los cuatro gobiernos provinciales de mayor peso nacional, partidos, Cristina Fernández de Kirchner, grandes grupos, cámaras empresarias, CGT, Camioneros, UTEP, Iglesia, AFA y Los Monos. Como en el mapa global, el Estado no figura como bloque formal sino a través de quienes ejercen el poder.
- Cada actor con ficha (qué es, quién manda), fuentes, puntaje de poder, poder oculto, autonomía, alcance y dependencias; acción fuera de la ley solo con condena judicial (causa Vialidad, Los Monos).
- 48 relaciones con fuente, incluidas las que cruzan con actores del mapa global (FMI, Tesoro de EE.UU., Banco Popular de China, Casa Blanca, CIA, Santa Sede, FIFA).
- Sitio: página Actores con ranking, filtro por tipo, red de relaciones y método; ficha de cada actor (`#a-<id>`); capa Actores en el mapa; actores con sede en las fichas de provincia y ciudad. Validador ampliado. Vista previa para redes regenerada.
- Cabos sueltos: fuente para las 67 ciudades que no la tenían; Junín y Goya vuelven por decisión de Franco (excepción al umbral de 100.000 habitantes, registrada en `fuente/ciudades.py`); población de Timbúes (5.406), La Quiaca (22.078), Salvador Mazza (2010) y Jáchal (2010).

## 2026-11-19 (c) · Población de ciudades y estación china

- Población de cada ciudad (`fuente/poblacion_ciudades.py`): la del aglomerado urbano del INDEC cuando la ciudad forma parte de uno (Censo 2022, con el dato de 2010), y la de la localidad sola para las ciudades chicas, con el año del dato (2022, 2010, 2001 o estimación). Cuando un aglomerado une varias localidades (Neuquén-Plottier-Cipolletti, Gran Rosario, Santiago del Estero-La Banda y otros), la cifra es la del conjunto. Faltan Timbúes y Salvador Mazza.
- El criterio «más de 100.000 habitantes» se mide sobre el aglomerado y el validador lo controla. Siete ciudades no llegaban: Puerto Madryn, Gualeguaychú, Venado Tuerto, Orán, Río Grande, Oberá y Sáenz Peña siguen por otro motivo (empresa o cluster, puerto o frontera); Junín y Goya, que solo entraban por población, salen del mapa. Quedan 97 ciudades.
- Estación de Espacio Lejano de China: ubicada en la Pampa de Pilmatué, paraje Quintuco, al norte de Bajada del Agrio (departamento Loncopué, −38,1914; −70,1495). Reemplaza el punto provisorio en Bajada del Agrio.

## 2026-11-19 (b) · Paso 2: las 24 provincias

- Población del Censo 2022 (INDEC, resultados definitivos) por provincia y por departamento: 45.892.285 habitantes. `fuente/poblacion.py` se genera con `scripts/importar_censo.py`.
- Economía y recursos (`fuente/economia.py`): exportaciones, destinos y rubro principal de cada provincia (INDEC, origen provincial de las exportaciones, primer semestre de 2026) y recursos propios sobre el total de ingresos (ASAP, 2025; La Pampa sin datos).
- Quién manda de verdad y alineamiento con la Nación (`fuente/alineamiento.py`): 5 aliados, 10 dialoguistas, 3 independientes y 6 opositores al 19/11/2026, con el grupo que gobierna, desde cuándo y fuentes. Misiones: ruptura de Passalacqua con Carlos Rovira en 2026.
- Influencias mundiales (`fuente/influencias.py`): 11 potencias en cinco canales, con fuente. El comercio se calcula con los destinos de exportación; inversión, deuda, presencia e influencia política se cargan dato por dato. Potencia dominante por provincia, con empates marcados.
- Mapa: capas de alineamiento, influencias (dominante o una potencia) y economía (exportaciones o recursos propios). Fichas de provincia, departamento y ciudad con población; tabla de Provincias ampliada.
- Validador: controla población, alineamiento, exportaciones y fuentes de cada influencia.

## 2026-11-19 · Paso 1: esqueleto

- Mapa de las 24 jurisdicciones con la cartografía del IGN (vía Georef): zoom de país a provincia, departamento (528 departamentos, partidos y comunas) y ciudad, con rutas propias (`#prov-`, `#d-`, `#c-`). Malvinas en el mapa principal y la Antártida Argentina en un recuadro.
- 99 ciudades ubicadas con Georef, cada una con su motivo: capitales, ciudades grandes, sedes de empresas y clusters aunque sean chicas (General Deheza, Armstrong, Las Parejas, Arroyito, Sunchales y otras), puertos, energía, minería, frontera y defensa. Filtrables por motivo en el mapa.
- Gobernadores al 19 de noviembre de 2026 (Corrientes: Juan Pablo Valdés y Santiago del Estero: Elías Suárez, desde diciembre de 2025).
- Escritorio: panel lateral de la misma altura que el mapa con lo principal y los bloques de detalle debajo, a lo ancho.
- Símbolo propio (silueta de la Argentina dentro del círculo del mapa global) e imagen de vista previa para WhatsApp y X.
- Pendientes: población del Censo 2022 de las ciudades grandes, fuentes de cada ciudad y ubicación exacta de la estación espacial china de Neuquén.
