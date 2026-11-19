#!/usr/bin/env node
// Controla data/territorio.json y la cartografía. Uso: node scripts/validate.js
const fs = require("fs"), path = require("path");
const R = path.join(__dirname, "..");
const T = JSON.parse(fs.readFileSync(path.join(R, "data/territorio.json"), "utf8"));
const err = [], av = [];
const MOT = ["cap", "pob", "emp", "pue", "ene", "min", "fro", "def"];

if (T.provincias.length !== 24) err.push(`Hay ${T.provincias.length} jurisdicciones (deben ser 24).`);
const deps = {};
for (const p of T.provincias) {
  const f = path.join(R, "data/dep", p.id + ".json");
  if (!fs.existsSync(f)) { err.push(`Falta data/dep/${p.id}.json`); continue; }
  for (const g of JSON.parse(fs.readFileSync(f, "utf8")).objects.dep.geometries) deps[g.properties.id] = p.id;
  for (const k of ["s", "gob", "par", "desde"]) if (!p[k]) err.push(`${p.n}: falta ${k}`);
  if (!/^\d{4}-\d{2}$/.test(p.desde || "")) err.push(`${p.n}: fecha «desde» inválida`);
  if (!p.cap) err.push(`${p.n}: no tiene capital entre las ciudades`);
}
for (const p of T.provincias) {
  if (!p.pob) err.push(`${p.n}: falta la población`);
  if (!p.ali || !"ADIO".includes(p.ali.ali) || !p.ali.manda || !p.ali.fuentes.length) err.push(`${p.n}: falta el alineamiento o sus fuentes`);
  if (!p.eco || !(p.eco.exp > 0)) err.push(`${p.n}: faltan las exportaciones`);
  for (const i of p.inf) if (!/^https?:\/\//.test(i.u) || !(i.n >= 1 && i.n <= 3)) err.push(`${p.n}: influencia sin fuente o fuera de escala (${i.p})`);
}
const slugs = new Set();
for (const c of T.ciudades) {
  if (slugs.has(c.s)) err.push(`Ciudad repetida: ${c.n}`); slugs.add(c.s);
  if (!T.provincias.some(p => p.id === c.prov)) err.push(`${c.n}: provincia ${c.prov} inexistente`);
  if (c.dep && deps[c.dep] !== c.prov) err.push(`${c.n}: el departamento ${c.dep} no es de la provincia ${c.prov}`);
  if (!c.dep && c.prov !== "02") err.push(`${c.n}: falta departamento`);
  if (!(c.lon > -74 && c.lon < -53 && c.lat > -56 && c.lat < -21)) err.push(`${c.n}: coordenadas fuera de la Argentina`);
  if (!c.mot.length || c.mot.some(m => !MOT.includes(m))) err.push(`${c.n}: motivos inválidos (${c.mot})`);
  if (!c.nota) err.push(`${c.n}: falta el motivo escrito`);
  if (!c.fuente && !c.mot.every(m => m === "cap" || m === "pob")) av.push(`${c.n}: sin fuente`);
  if (c.mot.includes("pob") && !(c.agpob || c.pob)) av.push(`${c.n}: falta la población del Censo 2022`);
  if (c.mot.includes("pob") && !c.exc && Math.max(c.agpob || 0, c.pob || 0) < 100000) err.push(`${c.n}: motivo pob pero menos de 100.000 habitantes (ni la localidad ni su aglomerado)`);
  if ((c.pob && !c.anio) || (c.agpob && !c.fag)) err.push(`${c.n}: población sin año o sin fuente`);
}
// Actores (paso 3)
const A = T.actores || [], AID = new Set(A.map(a => a.id)), EXT = T.meta.act ? T.meta.act.externos : {};
if (A.length < 30) err.push(`Hay ${A.length} actores; el paso 3 pide unos 40.`);
for (const a of A) {
  if (a.sc.length !== 21 || a.sc.some(v => v < 0 || v > 3)) err.push(`${a.n}: puntajes inválidos`);
  if (!a.fu.length || a.fu.some(([t, u]) => !t || !/^https?:/.test(u))) err.push(`${a.n}: faltan fuentes`);
  if (!a.res || !a.manda) err.push(`${a.n}: falta la ficha`);
  if (a.sc[8] > 0 && a.cert !== "D") err.push(`${a.n}: acción fuera de la ley sin documentar`);
  if (!T.ciudades.some(c => c.s === a.cs)) err.push(`${a.n}: la sede no está en el mapa`);
  if (a.pt < 0 || a.pt > 100) err.push(`${a.n}: puntaje fuera de rango`);
}
if (A.length && Math.max(...A.map(a => a.pt)) !== 100) err.push("El mayor puntaje tiene que valer 100.");
for (const r of T.relaciones || []) {
  for (const z of [r.o, r.d]) if (!AID.has(z) && !(z in EXT)) err.push(`Relación con actor desconocido: ${z}`);
  if (!/^https?:/.test(r.u)) err.push(`Relación ${r.o}-${r.d} sin fuente`);
}
const hoy = new Date().toISOString().slice(0, 10);
if (T.proxima < hoy) err.push(`El corte venció: la próxima revisión era el ${T.proxima}.`);

const noFuente = av.filter(a => a.endsWith("sin fuente")).length, noPob = av.length - noFuente;
if (av.length) console.log(`Avisos: ${noFuente} ciudades sin fuente y ${noPob} ciudades grandes sin población (pendientes del paso 2 y 4).`);
if (err.length) { console.error("ERRORES:\n- " + err.join("\n- ")); process.exit(1); }
console.log(`OK: ${T.provincias.length} jurisdicciones, ${Object.keys(deps).length} departamentos, ${T.ciudades.length} ciudades, ${A.length} actores, ${(T.relaciones || []).length} relaciones. Corte ${T.corte}, próxima revisión ${T.proxima}.`);
