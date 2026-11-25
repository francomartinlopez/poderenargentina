# Novena tanda de actores (25/11/2026, pedido de Franco: completar los actores pendientes).
# Instituto Patria, La Voz del Interior, Roemmers, FARN y la Federación de Luz y Fuerza. Mismo formato que fuente/actores_mas.py.
# Resguardos: de las personas vivas, solo cargos, hechos públicos y lo que estableció un tribunal u organismo oficial.

from actores_mas import S, CABA

ACTORES = [
    ("instituto_patria", "Instituto Patria (Cristina Kirchner, Oscar Parrilli)", "ONG, fundación o think tank", CABA, "N", "P", 1,
     S(cul=1, red=2, apo=1), "D", "", 0),
    ("la_voz", "La Voz del Interior (Grupo Clarín)", "Medio de comunicación", "Córdoba", "P", "T", 1,
     S(mod=2, cul=1, red=1), "D", "", 0),
    ("roemmers", "Laboratorios Roemmers (familia Roemmers)", "Empresa industrial", CABA, "N", "I", 2,
     S(cap=2, prd=2, red=1), "D", "", 0),
    ("farn", "FARN (Fundación Ambiente y Recursos Naturales)", "ONG, fundación o think tank", CABA, "N", "I", 1,
     S(cul=1, red=1, apo=1), "D", "", 0),
    ("fatlyf", "FATLyF (Federación de Luz y Fuerza)", "Sindicato", CABA, "N", "P", 1,
     S(red=1, apo=1, prd=1), "D", "", 0),
]

PATRIA = "https://www.letrap.com.ar/politica/el-instituto-patria-convertira-el-documento-cfk-un-plan-gobierno-n5407338"
LA_VOZ = "https://argentina.mom-rsf.org/en/media/detail/outlet/la-voz-del-interior/"
SIDUS = "https://www.iprofesional.com/salud/439455-roemmers-compro-empresa-medicamentos-sidus-alerta-por-monopolio"
GLACIARES = "https://www.greenpeace.org/argentina/story/problemas/climayenergia/justicia-por-los-glaciares-presentan-demanda-colectiva-con-mas-de-850-mil-adherentes/"
FATLYF_DNU = "https://www.tiempoar.com.ar/ta_article/sindical-dnu-milei-institucionalidad/"

FICHAS = {
    "instituto_patria": dict(res="Centro de formación y debate del kirchnerismo, fundado en 2016 por Cristina Kirchner, que es su presidenta honoraria; lo preside Oscar Parrilli y funciona en la calle Rodríguez Peña 80, en la Ciudad de Buenos Aires. Es punto de reunión de la militancia y elabora documentos programáticos del espacio.",
                             manda="Cristina Kirchner (presidenta honoraria) y Oscar Parrilli (presidente).",
                             fuentes=[("Letra P: el Instituto Patria y el documento de CFK", PATRIA),
                                      ("La Nación: la militancia en el Instituto Patria", "https://www.lanacion.com.ar/politica/vialidad-la-militancia-kirchneristas-se-congrega-en-el-instituto-patria-para-respaldar-a-cristina-nid13112024/")]),
    "la_voz": dict(res="Principal diario de Córdoba, fundado en 1904. Lo edita La Voz del Interior S.A., de la Compañía Inversora de Medios de Comunicación (CIMECO), controlada por el Grupo Clarín; desde 2025 se imprime en la planta de El Litoral, en Santa Fe.",
                   manda="El Grupo Clarín.",
                   fuentes=[("Media Ownership Monitor (RSF): La Voz del Interior", LA_VOZ),
                            ("InfoNegocios: deja de imprimir en Córdoba", "https://infonegocios.info/que-esta-pasando/la-voz-del-interior-deja-de-imprimir-su-diario-en-cordoba-cierra-la-rotativa-local-y-los-ejemplares-vendran-desde-santa-fe")]),
    "roemmers": dict(res="Laboratorio farmacéutico fundado en 1921, de la familia Roemmers; encabezó el mercado nacional en 2024 con 8,44% de las ventas en dólares. En 2025 compró el laboratorio Sidus, operación que analizó Defensa de la Competencia, y en 2026 negoció un préstamo de la Corporación Financiera Internacional para expandirse en la región.",
                     manda="Alberto y Pablo Roemmers.",
                     fuentes=[("iProfesional: los 10 laboratorios más poderosos", "https://www.iprofesional.com/salud/422212-cuales-son-los-10-laboratorios-mas-poderosos-de-argentina-y-que-manejan-el-negocio"),
                              ("iProfesional: la compra de Sidus", SIDUS),
                              ("iProfesional: el préstamo de la CFI", "https://www.iprofesional.com/negocios/407972-un-laboratorio-local-negocia-millonario-prestamo-para-expandirse-cuanto-recibiria")]),
    "farn": dict(res="Organización ambientalista dedicada al derecho ambiental, dirigida por Andrés Nápoli. En mayo de 2026 presentó con Greenpeace y la Asociación Argentina de Abogados/as Ambientalistas, ante la Justicia federal de La Pampa, el amparo colectivo contra la reforma de la Ley de Glaciares, con unas 850.000 adhesiones.",
                 manda="Andrés Nápoli (director ejecutivo).",
                 fuentes=[("Greenpeace: la demanda por los glaciares", GLACIARES),
                          ("La Nación: el amparo con 850.000 adhesiones", "https://www.lanacion.com.ar/sociedad/presentan-un-amparo-con-850000-adhesiones-para-suspender-la-reforma-de-la-ley-de-glaciares-nid05052026/")]),
    "fatlyf": dict(res="Federación de los trabajadores de la energía eléctrica, creada en 1948, que reúne a 41 sindicatos de Luz y Fuerza. Rechazó el DNU 70/2023 y la privatización de empresas públicas; en 2026 respaldó al gobierno de Misiones por mantener estatal a Energía de Misiones.",
                   manda="Su Secretariado Nacional.",
                   fuentes=[("Tiempo Argentino: el rechazo al DNU", FATLYF_DNU),
                            ("Misiones Online: respaldo a Passalacqua", "https://misionesonline.net/2026/07/22/luz-y-fuerza-respaldo-a-hugo-passalacqua/")]),
}

RELACIONES = [
    ("cfk", "instituto_patria", "Gobierna", "Fundadora y presidenta honoraria del instituto.", 3, PATRIA),
    ("clarin", "la_voz", "Propiedad", "Controla el diario a través de CIMECO.", 3, LA_VOZ),
    ("economia", "roemmers", "Gobierna", "Defensa de la Competencia analizó su compra del laboratorio Sidus.", 1, SIDUS),
    ("farn", "greenpeace", "Alianza", "Presentaron juntos el amparo colectivo contra la reforma de la Ley de Glaciares.", 2, GLACIARES),
    ("farn", "milei", "Enfrentamiento", "Pide la inconstitucionalidad de la reforma de la Ley de Glaciares, promulgada por el Decreto 271/2026.", 1,
     "https://www.greenpeace.org/argentina/?p=35737"),
    ("fatlyf", "milei", "Enfrentamiento", "Rechazó el DNU 70/2023 y la privatización de empresas públicas.", 1, FATLYF_DNU),
    ("fatlyf", "gob_misiones", "Alianza", "Respaldó que Energía de Misiones siga siendo estatal.", 1,
     "https://misionesonline.net/2026/07/22/luz-y-fuerza-respaldo-a-hugo-passalacqua/"),
]
