// El mapa del poder argentino · aplicación
{
const MOT={cap:["Capital","#F5F0E6"],pob:["Ciudad grande","#9A9A9A"],emp:["Empresa o cluster","#FF3B30"],pue:["Puerto","#2F6BFF"],ene:["Energía","#F2A93B"],min:["Minería","#C8743C"],fro:["Frontera","#3FB8C9"],def:["Defensa y estrategia","#9E8CFF"]};
const ORDEN=["emp","pue","ene","min","fro","def","cap","pob"];
const POT=["EE.UU.","China","Unión Europea","Reino Unido","Brasil","Rusia","Israel","Golfo","Canadá y Australia","Japón y Corea","FMI, BM y BID"];
const CK=["com","inv","deu","pre","pol"],CAN=["Comercio","Inversión","Deuda","Presencia","Política"];
const CAPAS=[["terr","Territorio",1],["ali","Alineamiento con Nación",1],["inf","Influencias mundiales",1],["eco","Economía y recursos",1],["act","Actores"],["zl","Zonas liberadas"],["fr","Fricción"]];
const PCOL={"EE.UU.":"#2F6BFF","China":"#D7263D","Unión Europea":"#F2C14E","Reino Unido":"#7FB3D5","Brasil":"#2EB872","Rusia":"#9E1B32","Israel":"#A0C4FF","Golfo":"#C8743C","Canadá y Australia":"#B07CFF","Japón y Corea":"#FF8FAB","FMI, BM y BID":"#BDBDBD"};
const ACOL={A:"#8E6CFF",D:"#9A8F8C",I:"#F2A93B",O:"#3FB8C9"},ALI={A:"Aliado",D:"Dialoguista",I:"Independiente",O:"Opositor"};
const ADESC={A:"acuerdos electorales con La Libertad Avanza",D:"negocia votos y fondos sin acuerdo electoral pleno",I:"espacio propio que compite con LLA (Provincias Unidas)",O:"opositor al Gobierno nacional"};
let capa="terr",potSel="dom",ecoSel="exp";
const nf=n=>Number(n).toLocaleString("es-AR");
const host=u=>{try{return new URL(u).hostname.replace(/^www\./,"")}catch(e){return "fuente"}};
const src=u=>`<a class="src" href="${esc(u)}" target="_blank" rel="noopener">${esc(host(u))}</a>`;
const aliTag=a=>`<span class="tag" style="color:${ACOL[a]}">${ALI[a]}</span>`;
const MES=["ene.","feb.","mar.","abr.","may.","jun.","jul.","ago.","sep.","oct.","nov.","dic."];
const app=document.getElementById("app"),tip=document.getElementById("tip");
const esc=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const fmes=s=>{const[y,m]=s.split("-");return MES[+m-1]+" "+y};
const color=c=>{for(const k of ORDEN)if(c.mot.includes(k))return MOT[k][1]};
const tags=c=>`<span class="tags">${c.mot.map(m=>`<span class="tag" style="color:${MOT[m][1]}">${MOT[m][0]}</span>`).join("")}</span>`;
let T,PF,PROJ,PATH,FULL,cur,svg,G={},ANT,filt=new Set(Object.keys(MOT)),showDeps=false;
const DEP={},depLoad={};
const byS={},byId={},cityS={},depInfo={};

function more(h){document.getElementById("more").innerHTML=h}
function pend(t,d){return `<div class="blk"><h2>${t}</h2><div class="pend">${d}</div></div>`}
function infGrid(list){
  const m={};for(const i of list){(m[i.p]=m[i.p]||{})[i.c]=Math.max(m[i.p][i.c]||0,i.n)}
  const rows=POT.filter(p=>m[p]).sort((a,b)=>CK.reduce((s,k)=>s+(m[b][k]||0),0)-CK.reduce((s,k)=>s+(m[a][k]||0),0));
  if(!rows.length)return `<p class="muted">Sin influencias relevantes cargadas con fuente.</p>`;
  return `<div class="grid5"><span class="h"></span>${CAN.map(c=>`<span class="h">${c}</span>`).join("")}${rows.map(p=>`<span class="r"><i style="background:${PCOL[p]}"></i>${esc(p)}</span>`+CK.map(k=>{const n=m[p][k]||0;return `<span class="v" style="${n?`background:${PCOL[p]}${["","40","80","d0"][n]};color:#fff`:""}">${n||"·"}</span>`}).join("")).join("")}</div>`}
function infList(list){return `<ul class="ilist">${list.map(i=>`<li><b style="color:${PCOL[i.p]}">${esc(i.p)}</b> <span class="muted">· ${esc(T.meta.canales[i.c])} · ${i.n}</span><br>${esc(i.x)} ${src(i.u)}</li>`).join("")}</ul>`}
function influ(list,title,nota){return `<div class="blk"><h2>${title||"Influencias mundiales"}</h2>${infGrid(list)}<p class="muted" style="font-size:13px;margin:8px 0 10px">${nota||"De 0 a 3 por canal. Comercio: participación en las exportaciones (INDEC); el resto, con la fuente de cada dato."}</p><details><summary>${list.length} datos con fuente</summary>${infList(list)}</details></div>`}

function setup(){
  const W=600;
  PROJ=d3.geoTransverseMercator().rotate([65,0]).fitWidth(W-24,PF);
  PATH=d3.geoPath(PROJ);
  const b=PATH.bounds(PF);
  FULL=[b[0][0]-12,b[0][1]-12,b[1][0]-b[0][0]+24,b[1][1]-b[0][1]+24];
  for(const f of PF.features){const p=byId[f.properties.id];p.f=f;p.b=PATH.bounds(f)}
  for(const c of T.ciudades){c.xy=PROJ([c.lon,c.lat])}
}

function mapShell(){
  app.innerHTML=`<div class="mapview"><div><div class="crumbs" id="crumbs"></div>
  <div class="bar" id="capas" role="group" aria-label="Capas"></div><div class="bar sub" id="sub"></div>
  <div class="mapbox" id="mapbox"><svg id="map" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Mapa de la Argentina por provincias"></svg>
  <div class="ant" id="ant"><svg id="antsvg" aria-hidden="true"></svg>Antártida Argentina<br>(otra escala)</div></div>
  <div class="bar" id="filt" role="group" aria-label="Ciudades por motivo" style="margin-top:10px"></div></div>
  <aside class="panel"><div class="pin" id="panel"></div></aside></div><section class="more" id="more"></section>`;
  svg=document.getElementById("map");
  svg.setAttribute("viewBox",FULL.join(" "));cur=FULL.slice();
  svg.innerHTML=`<g id="gp">${PF.features.map(f=>`<path class="prov" data-k="p:${f.properties.id}" d="${PATH(f)}"><title>${esc(byId[f.properties.id].n)}</title></path>`).join("")}</g><g id="gd"></g><g id="gc"></g><g id="gl"></g>`;
  G={p:svg.querySelector("#gp"),d:svg.querySelector("#gd"),c:svg.querySelector("#gc"),l:svg.querySelector("#gl")};
  for(const pid in DEP)depGroup(pid);
  if(ANT){const as=document.getElementById("antsvg"),pr=d3.geoAzimuthalEqualArea().rotate([50,90]).fitExtent([[4,4],[104,92]],ANT);as.setAttribute("viewBox","0 0 108 96");as.innerHTML=`<path d="${d3.geoPath(pr)(ANT)}" fill="#161414" stroke="#4A3A38"/>`}
  svg.addEventListener("click",e=>{const t=e.target.closest("[data-k]");if(!t)return;const[k,v]=t.dataset.k.split(":");
    if(k==="p"){location.hash="prov-"+byId[v].s}else if(k==="d"){location.hash="d-"+v}else if(k==="c"){location.hash="c-"+v}});
  svg.addEventListener("pointermove",e=>{const t=e.target.closest("[data-k]");if(!t||e.pointerType!=="mouse"){tip.style.display="none";return}
    const[k,v]=t.dataset.k.split(":");const txt=k==="p"?tipText(byId[v]):k==="d"?(depInfo[v]?.n||v):cityS[v]?.n;tip.textContent=txt;tip.style.display="block";tip.style.left=e.clientX+14+"px";tip.style.top=e.clientY+12+"px"});
  svg.addEventListener("pointerleave",()=>tip.style.display="none");
  new ResizeObserver(()=>scaleMarks()).observe(svg);
  document.getElementById("capas").onclick=e=>{const b=e.target.closest("button[data-c]");if(!b||b.disabled)return;capa=b.dataset.c;route()};
  document.getElementById("sub").onclick=e=>{const b=e.target.closest("button");if(!b)return;if(b.dataset.pot)potSel=b.dataset.pot;if(b.dataset.eco)ecoSel=b.dataset.eco;route()};
}
function tipText(p){
  if(capa==="ali")return `${p.n}: ${ALI[p.ali.ali]}`;
  if(capa==="inf")return potSel==="dom"?`${p.n}: ${p.dom||(p.emp.length?"empate entre "+p.emp.join(", "):"sin datos")}`:`${p.n}: ${potSel} ${p.tot[potSel]||0} puntos`;
  if(capa==="eco")return ecoSel==="exp"?`${p.n}: USD ${nf(p.eco.exp)} M exportados`:`${p.n}: ${p.eco.propios==null?"sin datos":p.eco.propios.toLocaleString("es-AR")+"% de recursos propios"}`;
  return p.n}
function paint(){
  document.getElementById("capas").innerHTML=CAPAS.map(([k,n,on])=>on?`<button class="chip ${capa===k?"on":""}" data-c="${k}" aria-pressed="${capa===k}">${n}</button>`:`<button class="chip" disabled title="Se carga en los próximos pasos">${n} <small>pronto</small></button>`).join("");
  const P=T.provincias,sub=document.getElementById("sub");let leg="";
  const maxPot=k=>Math.max(1,...P.map(p=>p.tot[k]||0)),maxExp=Math.max(...P.map(p=>p.eco.exp));
  const fill=p=>{
    if(capa==="ali")return[ACOL[p.ali.ali],.6];
    if(capa==="inf"){if(potSel==="dom")return p.dom?[PCOL[p.dom],.62]:p.emp.length?["#6E6462",.55]:null;const v=p.tot[potSel]||0;return v?[PCOL[potSel],.18+.7*v/maxPot(potSel)]:null}
    if(capa==="eco"){if(ecoSel==="exp")return["#FF3B30",.1+.8*Math.log10(p.eco.exp)/Math.log10(maxExp)];return p.eco.propios==null?null:["#FF3B30",.1+.8*p.eco.propios/90]}
    return null};
  for(const el of G.p.children){const p=byId[el.dataset.k.slice(2)],f=fill(p);el.style.fill=f?f[0]:"";el.style.fillOpacity=f?f[1]:"";el.querySelector("title").textContent=tipText(p)}
  if(capa==="ali"){const c={};P.forEach(p=>c[p.ali.ali]=(c[p.ali.ali]||0)+1);leg=Object.keys(ALI).map(a=>`<span class="lg"><i style="background:${ACOL[a]}"></i>${ALI[a]} ${c[a]||0}</span>`).join("")}
  else if(capa==="inf"){leg=`<button class="chip ${potSel==="dom"?"on":""}" data-pot="dom">Dominante</button>`+POT.map(k=>`<button class="chip ${potSel===k?"on":""}" data-pot="${esc(k)}"><i style="background:${PCOL[k]}"></i>${esc(k)}</button>`).join("")}
  else if(capa==="eco"){leg=`<button class="chip ${ecoSel==="exp"?"on":""}" data-eco="exp">Exportaciones</button><button class="chip ${ecoSel==="pro"?"on":""}" data-eco="pro">Recursos propios</button><span class="lg">${ecoSel==="exp"?"USD exportados, "+esc(T.meta.periodo_exp)+" (escala logarítmica)":"Ingresos propios sobre el total, 2025 (ASAP)"}</span>`}
  sub.innerHTML=leg;sub.style.display=leg?"":"none";
}

function filters(){
  const cnt={};for(const c of T.ciudades)for(const m of c.mot)cnt[m]=(cnt[m]||0)+1;
  const el=document.getElementById("filt");
  el.innerHTML=`<button class="chip ${showDeps?"on":""}" id="tdep" aria-pressed="${showDeps}">Departamentos</button>`+Object.keys(MOT).map(m=>`<button class="chip ${filt.has(m)?"":"off"}" data-m="${m}" aria-pressed="${filt.has(m)}"><i style="background:${MOT[m][1]}"></i>${MOT[m][0]} <small>${cnt[m]||0}</small></button>`).join("");
  el.onclick=async e=>{const b=e.target.closest("button");if(!b)return;
    if(b.id==="tdep"){showDeps=!showDeps;if(showDeps)await Promise.all(T.provincias.map(p=>loadDep(p.id)));route();return}
    const m=b.dataset.m;filt.has(m)?filt.delete(m):filt.add(m);if(!filt.size)Object.keys(MOT).forEach(x=>filt.add(x));route()};
}

async function loadDep(pid){
  if(DEP[pid])return DEP[pid];
  if(!depLoad[pid])depLoad[pid]=fetch(`data/dep/${pid}.json`).then(r=>r.json()).then(t=>{const fc=topojson.feature(t,t.objects.dep);DEP[pid]=fc;
    for(const f of fc.features){const p=f.properties;depInfo[p.id]={n:p.nombre,cat:p.cat,pid,f}}
    depGroup(pid);return fc});
  return depLoad[pid];
}

function depGroup(pid){if(!G.d||G.d.querySelector("#dg"+pid))return;G.d.insertAdjacentHTML("beforeend",`<g id="dg${pid}">${DEP[pid].features.map(f=>`<path class="dep" data-k="d:${f.properties.id}" d="${PATH(f)}"></path>`).join("")}</g>`)}
function zoomTo(box){
  const pad=.07,b=[box[0]-box[2]*pad,box[1]-box[3]*pad,box[2]*(1+2*pad),box[3]*(1+2*pad)];
  const from=cur.slice(),t0=performance.now(),dur=matchMedia("(prefers-reduced-motion: reduce)").matches?0:520;
  const step=now=>{let k=dur?Math.min(1,(now-t0)/dur):1;k=k<.5?2*k*k:1-(-2*k+2)**2/2;
    cur=from.map((v,i)=>v+(b[i]-v)*k);svg.setAttribute("viewBox",cur.join(" "));scaleMarks();if(k<1)requestAnimationFrame(step)};
  requestAnimationFrame(step);
}
function scaleMarks(){
  if(!svg)return;const r=svg.getBoundingClientRect();if(!r.width)return;
  const px=Math.max(cur[2]/r.width,cur[3]/r.height);
  for(const c of G.c.children)c.setAttribute("r",(c.classList.contains("cap")?5.2:4.2)*px);
  const placed=[];
  for(const l of G.l.children){const fs=12*px,x=+l.getAttribute("x")+7*px,y=+l.getAttribute("y")+4*px,w=l.textContent.length*fs*.56,bb=[x-2*px,y-fs,x+w,y+3*px];
    l.setAttribute("font-size",fs);l.setAttribute("stroke-width",3*px);l.setAttribute("dx",7*px);l.setAttribute("dy",4*px);
    const hit=!l.classList.contains("keep")&&placed.some(o=>bb[0]<o[2]&&bb[2]>o[0]&&bb[1]<o[3]&&bb[3]>o[1]);
    l.style.display=hit?"none":"";if(!hit)placed.push(bb)}
}
function drawCities(list,labels,sel){
  const vis=list.filter(c=>c.mot.some(m=>filt.has(m))||c.s===sel);
  vis.sort((a,b)=>(a.mot.includes("cap")-b.mot.includes("cap")));
  G.c.innerHTML=vis.map(c=>`<circle class="city ${c.mot.includes("cap")?"cap":""} ${c.s===sel?"sel":""}" cx="${c.xy[0]}" cy="${c.xy[1]}" r="3" fill="${color(c)}" data-k="c:${c.s}"></circle>`).join("");
  const pr=c=>c.s===sel?0:c.mot.includes("cap")?1:c.mot.includes("pob")?2:3;
  G.l.innerHTML=labels?vis.slice().sort((a,b)=>pr(a)-pr(b)).map(c=>`<text class="clbl ${c.mot.includes("cap")?"cap":""} ${c.s===sel?"keep":""}" x="${c.xy[0]}" y="${c.xy[1]}">${esc(c.n)}</text>`).join(""):"";
  scaleMarks();
}
function provState(pid,did){
  for(const el of G.p.children){const id=el.dataset.k.slice(2);el.classList.toggle("sel",id===pid);el.classList.toggle("dim",!!pid&&id!==pid)}
  for(const g of G.d.children){const id=g.id.slice(2);g.style.display=(showDeps&&!pid)||id===pid?"":"none";
    for(const d of g.children){d.classList.toggle("live",id===pid);d.classList.toggle("sel",d.dataset.k.slice(2)===did)}}
}
function crumbs(parts){document.getElementById("crumbs").innerHTML=parts.map((p,i)=>i<parts.length-1?`<a href="#${p[1]}">${esc(p[0])}</a> ›`:`<b>${esc(p[0])}</b>`).join(" ")}
function ensureMap(){if(!document.getElementById("map")){mapShell()}filters();paint()}

function vPais(){
  ensureMap();provState(null);drawCities(T.ciudades,false);zoomTo(FULL);crumbs([["Argentina"]]);
  document.getElementById("ant").style.display="";
  const cnt={};for(const c of T.ciudades)for(const m of c.mot)cnt[m]=(cnt[m]||0)+1;const mx=Math.max(...Object.values(cnt));
  const P=T.provincias;let side="";
  if(capa==="ali")side=`<h2>Alineamiento con Nación</h2><ul class="clist">${Object.keys(ALI).map(a=>`<li>${aliTag(a)}<span class="muted" style="font-size:13px">${ADESC[a]}</span><span class="nota">${P.filter(p=>p.ali.ali===a).map(p=>`<a href="#prov-${p.s}">${esc(p.c)}</a>`).join(", ")}</span></li>`).join("")}</ul><p class="muted" style="font-size:13px">Clasificación al ${esc(T.corte)}. ${src(T.meta.fuente_ali)}</p>`;
  else if(capa==="inf"){const d={};P.forEach(p=>{if(p.dom)(d[p.dom]=d[p.dom]||[]).push(p)});const emp=P.filter(p=>!p.dom&&p.emp.length);
    side=`<h2>Potencia dominante por provincia</h2><ul class="clist">${POT.filter(k=>d[k]).sort((a,b)=>d[b].length-d[a].length).map(k=>`<li><b style="color:${PCOL[k]}">${esc(k)}</b> <span class="mono muted">${d[k].length}</span><span class="nota">${d[k].map(p=>`<a href="#prov-${p.s}">${esc(p.c)}</a>`).join(", ")}</span></li>`).join("")}${emp.length?`<li><b>Empate</b> <span class="mono muted">${emp.length}</span><span class="nota">${emp.map(p=>`<a href="#prov-${p.s}">${esc(p.c)}</a> (${p.emp.join(", ")})`).join("; ")}</span></li>`:""}</ul>`}
  else if(capa==="eco"){const L=P.slice().sort((a,b)=>ecoSel==="exp"?b.eco.exp-a.eco.exp:(b.eco.propios??-1)-(a.eco.propios??-1)),mx=Math.max(...P.map(p=>ecoSel==="exp"?p.eco.exp:(p.eco.propios||0)));
    side=`<h2>${ecoSel==="exp"?"Exportaciones, "+esc(T.meta.periodo_exp):"Recursos propios, 2025"}</h2><div class="mbars">${L.map(p=>{const v=ecoSel==="exp"?p.eco.exp:p.eco.propios;return `<div><span><a href="#prov-${p.s}">${esc(p.c)}</a></span><em style="width:${(v||0)/mx*100}%;background:#FF3B30"></em><span>${v==null?"s/d":ecoSel==="exp"?nf(v):Math.round(v)+"%"}</span></div>`}).join("")}</div><p class="muted" style="font-size:13px">${ecoSel==="exp"?"Millones de USD. "+src(T.meta.fuente_exp):"Ingresos propios sobre el total. "+src(T.meta.fuente_propios)}</p>`}
  else side=`<h2>Por qué está cada ciudad</h2><div class="mbars">${Object.keys(MOT).map(m=>`<div><span>${MOT[m][0]}</span><em style="width:${cnt[m]/mx*100}%;background:${MOT[m][1]}"></em><span>${cnt[m]||0}</span></div>`).join("")}</div>
  <p class="muted" style="font-size:13px;margin:8px 0 0">Una ciudad puede tener varios motivos. Las de empresa o cluster entran aunque sean chicas.</p>`;
  document.getElementById("panel").innerHTML=`<h1>Argentina</h1><p class="sub">Tocá una provincia para bajar a sus departamentos y ciudades. Cambiá la capa para ver alineamiento, influencias o economía.</p>
  <div class="facts"><div><span>Población (Censo 2022)</span><b class="mono">${nf(T.pais.pob)}</b></div><div><span>Departamentos</span><b class="mono">${P.reduce((s,p)=>s+p.ndep,0)}</b></div><div><span>Ciudades en el mapa</span><b class="mono">${T.ciudades.length}</b></div></div>
  <div class="blk grow">${side}</div>`;
  more(influ(T.pais.inf,"Influencias sobre el Estado nacional","Vínculos de la Nación con cada potencia. Las de cada provincia, en su ficha.")+pend("Quién manda","<b>Paso 3.</b> Unos 40 actores núcleo nacionales con sus relaciones: Casa Rosada, Economía, BCRA, Corte, Comodoro Py, SIDE, partidos, sindicatos, grandes grupos y poder externo."));
}
async function vProv(p,did){
  ensureMap();document.getElementById("ant").style.display="none";
  await loadDep(p.id);provState(p.id,did);
  const cs=T.ciudades.filter(c=>c.prov===p.id);drawCities(cs,true);
  const df=did&&depInfo[did];zoomTo(df?bx(PATH.bounds(df.f),p.b):bx(p.b));
  const deps=DEP[p.id].features.map(f=>f.properties).sort((a,b)=>a.nombre.localeCompare(b.nombre,"es"));
  const cap=cityS[p.cap];
  if(df){crumbs([["Argentina","inicio"],[p.n,"prov-"+p.s],[df.n]]);vDep(p,did);return}
  crumbs([["Argentina","inicio"],[p.n]]);
  document.getElementById("panel").innerHTML=`<h1>${esc(p.n)}</h1><p class="sub">${esc(p.cat)}. Capital: ${cap?`<a href="#c-${cap.s}">${esc(cap.n)}</a>`:"—"}.</p>
  <div class="facts"><div><span>Gobierna</span><b>${esc(p.gob)}</b></div><div><span>Partido o frente</span><b style="font-size:14px">${esc(p.par)}</b></div><div><span>En el cargo desde</span><b class="mono">${fmes(p.desde)}</b></div><div><span>Frente a la Nación</span><b>${aliTag(p.ali.ali)}</b></div><div><span>Población</span><b class="mono">${nf(p.pob)}</b></div><div><span>Potencia dominante</span><b style="font-size:14px;color:${p.dom?PCOL[p.dom]:"inherit"}">${esc(p.dom||(p.emp.length?"Empate: "+p.emp.join(", "):"—"))}</b></div></div>
  <div class="blk grow"><h2>Ciudades en el mapa · ${cs.length}</h2><ul class="clist">${cs.map(c=>`<li><a href="#c-${c.s}">${esc(c.n)}</a>${tags(c)}<span class="nota">${esc(c.nota)}</span></li>`).join("")||`<li class="muted">Ninguna todavía.</li>`}</ul></div>`;
  const depBlk=`<div class="blk wide"><details ${deps.length<=40?"open":""}><summary><h2 style="display:inline">${deps.length} ${p.id==="06"?"partidos":p.id==="02"?"comunas":"departamentos"}</h2></summary><div class="deps">${deps.map(d=>`<a href="#d-${d.id}">${esc(d.nombre)} <span class="mono muted">${T.deppob[d.id]?nf(T.deppob[d.id]):""}</span></a>`).join("")}</div></details></div>`;
  const a=p.ali,e=p.eco;
  const manda=`<div class="blk"><h2>Quién manda de verdad</h2><p class="lead">${esc(a.manda)}</p><dl class="dl"><dt>Gobierna</dt><dd>${esc(a.grupo)}</dd><dt>Frente a la Nación</dt><dd>${aliTag(a.ali)} <span class="muted">${ADESC[a.ali]}</span></dd><dt>Fuentes</dt><dd>${a.fuentes.map(src).join(" · ")}</dd></dl></div>`;
  const eco=`<div class="blk"><h2>Economía y recursos</h2><dl class="dl"><dt>Exportaciones</dt><dd><b class="mono">USD ${nf(e.exp)} M</b> en el ${esc(T.meta.periodo_exp)}</dd><dt>Rubro principal</dt><dd>${esc(e.rubro)}</dd><dt>Destinos</dt><dd>${esc(e.destx)}</dd><dt>Recursos propios</dt><dd>${e.propios==null?"Sin datos actualizados":`<b class="mono">${e.propios.toLocaleString("es-AR")}%</b> de los ingresos; el resto llega de la Nación`}</dd><dt>Fuentes</dt><dd>${src(T.meta.fuente_exp)} · ${src(T.meta.fuente_propios)} · ${src(T.meta.fuente_censo)}</dd></dl></div>`;
  more(manda+influ(p.inf)+eco+pend("Actores con sede","<b>Pasos 3 y 5.</b> Con su puntaje de poder en los 21 ejes y su gráfico de relaciones.")+depBlk);
}
function bx(b,pb){let w=b[1][0]-b[0][0],h=b[1][1]-b[0][1];
  if(pb){const pw=pb[1][0]-pb[0][0],ph=pb[1][1]-pb[0][1],mw=Math.max(w,pw*.35),mh=Math.max(h,ph*.35),cx=(b[0][0]+b[1][0])/2,cy=(b[0][1]+b[1][1])/2;return[cx-mw/2,cy-mh/2,mw,mh]}
  return[b[0][0],b[0][1],w,h]}
function vDep(p,did){
  const d=depInfo[did],cs=T.ciudades.filter(c=>c.dep===did);
  document.getElementById("panel").innerHTML=`<h1>${esc(d.n)}</h1><p class="sub">${esc(d.cat)} de <a href="#prov-${p.s}">${esc(p.n)}</a>.</p>
  <div class="facts"><div><span>Población (Censo 2022)</span><b class="mono">${T.deppob[did]?nf(T.deppob[did]):"—"}</b></div><div><span>Peso en la provincia</span><b class="mono">${T.deppob[did]?(T.deppob[did]/p.pob*100).toLocaleString("es-AR",{maximumFractionDigits:1})+"%":"—"}</b></div></div>
  <div class="blk grow"><h2>Ciudades en el mapa</h2><ul class="clist">${cs.map(c=>`<li><a href="#c-${c.s}">${esc(c.n)}</a>${tags(c)}<span class="nota">${esc(c.nota)}</span></li>`).join("")||`<li class="muted">Ninguna de las ciudades seleccionadas está en este ${d.cat.toLowerCase()}.</li>`}</ul></div>`;
  more(pend("Datos del "+d.cat.toLowerCase(),"<b>Próximos pasos.</b> Cabecera, actividad principal, intendente o comisionado y actores con sede.")+`<div class="blk"><h2>Influencias mundiales</h2><p>Se miden por provincia: <a href="#prov-${p.s}">ver ${esc(p.n)}</a>${p.dom?`, donde domina <b style="color:${PCOL[p.dom]}">${esc(p.dom)}</b>`:""}.</p></div>`);
}
async function vCity(c){
  const p=byId[c.prov];ensureMap();document.getElementById("ant").style.display="none";
  await loadDep(p.id);provState(p.id,c.dep);drawCities(T.ciudades.filter(x=>x.prov===p.id),true,c.s);
  const s=Math.max(p.b[1][0]-p.b[0][0],p.b[1][1]-p.b[0][1])*(p.id==="02"?.8:.32);
  zoomTo([c.xy[0]-s/2,c.xy[1]-s/2,s,s]);
  const d=depInfo[c.dep];
  crumbs([["Argentina","inicio"],[p.n,"prov-"+p.s],...(d&&p.id!=="02"&&d.n!==c.n?[[d.n,"d-"+c.dep]]:[]),[c.n]]);
  document.getElementById("panel").innerHTML=`<h1>${esc(c.n)}</h1><p class="sub">${esc(c.nota)}</p>
  <div class="facts"><div><span>Provincia</span><b><a href="#prov-${p.s}">${esc(p.n)}</a></b></div>${d&&p.id!=="02"?`<div><span>${esc(d.cat)}</span><b><a href="#d-${c.dep}">${esc(d.n)}</a></b></div>`:""}<div><span>Población del ${d?esc(d.cat.toLowerCase()):"distrito"}</span><b class="mono">${c.dep&&T.deppob[c.dep]?nf(T.deppob[c.dep]):p.id==="02"?nf(p.pob):"—"}</b></div><div><span>Coordenadas</span><b class="mono" style="font-size:13px">${c.lat.toFixed(3)}, ${c.lon.toFixed(3)}</b></div></div>
  <div class="blk grow"><h2>Por qué está en el mapa</h2>${tags(c)}</div>`;
  more(pend("Quién gobierna y quién manda","<b>Paso 4.</b> Intendente, concejo y alineamiento; en las ciudades de una empresa, el peso de la empresa frente al municipio.")+`<div class="blk"><h2>Influencias mundiales</h2><p>Hoy se miden por provincia: <a href="#prov-${p.s}">ver ${esc(p.n)}</a>${p.dom?`, donde domina <b style="color:${PCOL[p.dom]}">${esc(p.dom)}</b>`:""}. Las de cada ciudad, con los mercados y socios de sus empresas, llegan en el paso 4.</p></div>`+pend("Actores y fricciones","<b>Paso 4.</b> Empresas, sindicatos, organizaciones y conflictos con sede en la ciudad."));
}
function vProvincias(){
  app.innerHTML=`<div class="page"><h1>Provincias</h1><p class="sub">Las 24 jurisdicciones: quién las gobierna, cómo se paran frente a la Nación y qué potencia pesa más en cada una.</p>
  <table class="stack"><thead><tr><th>Provincia</th><th>Gobierna</th><th>Partido o frente</th><th>Desde</th><th>Frente a la Nación</th><th>Potencia dominante</th><th class="n">Población</th><th class="n">Export. USD M</th><th class="n">Rec. propios</th></tr></thead><tbody>
  ${T.provincias.map(p=>`<tr><td><a href="#prov-${p.s}">${esc(p.n)}</a></td><td>${esc(p.gob)}</td><td>${esc(p.par)}</td><td class="mono">${fmes(p.desde)}</td><td>${aliTag(p.ali.ali)}</td><td style="color:${p.dom?PCOL[p.dom]:"inherit"}">${esc(p.dom||(p.emp.length?"Empate: "+p.emp.join(", "):"—"))}</td><td class="n">${nf(p.pob)}</td><td class="n">${nf(p.eco.exp)}</td><td class="n">${p.eco.propios==null?"s/d":Math.round(p.eco.propios)+"%"}</td></tr>`).join("")}</tbody></table>
  <p class="muted" style="font-size:13px;margin-top:12px">Exportaciones del ${esc(T.meta.periodo_exp)} (${src(T.meta.fuente_exp)}); recursos propios 2025 (${src(T.meta.fuente_propios)}); población del Censo 2022 (${src(T.meta.fuente_censo)}).</p></div>`;
}
let cq="",cm=null;
function vCiudades(){
  app.innerHTML=`<div class="page"><h1>Ciudades</h1><p class="sub">Entran las capitales, las ciudades grandes y las que concentran poder aunque sean chicas: sede de una empresa, cluster, puerto, energía, minería, frontera o defensa. Cada una con su motivo.</p>
  <input class="search" id="q" type="search" placeholder="Buscar ciudad o provincia" value="${esc(cq)}" aria-label="Buscar ciudad o provincia">
  <div class="bar" id="cf"><button class="chip ${cm?"":"on"}" data-m="">Todas</button>${Object.keys(MOT).map(m=>`<button class="chip ${cm===m?"on":""}" data-m="${m}"><i style="background:${MOT[m][1]}"></i>${MOT[m][0]}</button>`).join("")}</div>
  <table class="stack"><thead><tr><th>Ciudad</th><th>Provincia</th><th>Motivos</th><th>Por qué</th></tr></thead><tbody id="ct"></tbody></table></div>`;
  const draw=()=>{const q=cq.normalize("NFD").replace(/[̀-ͯ]/g,"").toLowerCase();
    document.getElementById("ct").innerHTML=T.ciudades.filter(c=>(!cm||c.mot.includes(cm))&&(c.n+" "+byId[c.prov].n).normalize("NFD").replace(/[̀-ͯ]/g,"").toLowerCase().includes(q))
    .map(c=>`<tr><td><a href="#c-${c.s}">${esc(c.n)}</a></td><td>${esc(byId[c.prov].c)}</td><td>${tags(c)}</td><td>${esc(c.nota)}</td></tr>`).join("")||`<tr><td colspan="4" class="muted">Sin resultados.</td></tr>`};
  document.getElementById("q").oninput=e=>{cq=e.target.value;draw()};
  document.getElementById("cf").onclick=e=>{const b=e.target.closest("button");if(!b)return;cm=b.dataset.m||null;vCiudades()};draw();
}
function vPlan(){
  app.innerHTML=`<div class="page plan"><h1>Plan</h1>
  <h2>Hecho</h2><ol><li><b>Esqueleto.</b> Mapa oficial del IGN con zoom de país a provincia, departamento y ciudad; ${T.ciudades.length} ciudades con su motivo; gobernadores al día.</li><li><b>Las 24 provincias.</b> Población del Censo 2022 por provincia y departamento; exportaciones, destinos y rubro principal (INDEC); recursos propios frente a los fondos nacionales (ASAP); quién manda de verdad y alineamiento con la Nación; influencias de 11 potencias en cinco canales, con fuente. Capas de alineamiento, influencias y economía en el mapa.</li></ol>
  <h2>Próximos pasos</h2><ol start="3"><li>Unos 40 actores núcleo nacionales con sus relaciones, medidos en los 21 ejes.</li><li>Fichas de ciudades: intendente, actores, fricciones e influencias propias.</li><li>Actores provinciales y municipales; puntos de fricción; zonas liberadas.</li></ol>
  <h2>Método de las influencias</h2><p>Cada potencia recibe de 0 a 3 en cinco canales. El comercio se calcula con la participación de cada destino en las exportaciones de la provincia (40% o más vale 3; de 20% a 40%, 2; de 8% a 20%, 1); cuando el INDEC informa un bloque se toma como aproximación (USMCA como EE.UU. y Mercosur como Brasil). Inversión, deuda, presencia e influencia política se cargan dato por dato con su fuente. La potencia dominante es la de mayor suma; si dos empatan, se marca el empate.</p>
  <h2>Pendientes</h2><ul><li>Población de cada ciudad (hoy se muestra la de su departamento) y fuente de cada ciudad.</li><li>Ubicación exacta de la estación espacial china (cargada en Bajada del Agrio, a confirmar con el paraje Quintuco).</li></ul></div>`;
}
function route(){
  const h=decodeURIComponent(location.hash.slice(1));tip.style.display="none";let nk="inicio";
  if(h.startsWith("prov-")&&byS[h.slice(5)])vProv(byS[h.slice(5)]);
  else if(h.startsWith("d-")){const id=h.slice(2),p=byId[id.slice(0,2)];if(p)loadDep(p.id).then(()=>depInfo[id]?vProv(p,id):vProv(p))}
  else if(h.startsWith("c-")&&cityS[h.slice(2)])vCity(cityS[h.slice(2)]);
  else if(h==="provincias"){vProvincias();nk=h;svg=null}
  else if(h==="ciudades"){vCiudades();nk=h;svg=null}
  else if(h==="plan"){vPlan();nk=h;svg=null}
  else vPais();
  document.querySelectorAll("nav a").forEach(a=>a.classList.toggle("on",a.dataset.k===nk));
  if(["provincias","ciudades","plan"].includes(nk))window.scrollTo(0,0);
}
Promise.all(["data/territorio.json","data/provincias.json","data/antartida.json"].map(u=>fetch(u).then(r=>r.json()))).then(([t,pt,an])=>{
  T=t;ANT=an.features?an.features[0]:an;{const g=ANT.geometry||ANT;if(d3.geoArea(ANT)>2*Math.PI)(g.type==="Polygon"?[g.coordinates]:g.coordinates).forEach(pl=>pl.forEach(r=>r.reverse()))}
  PF=topojson.feature(pt,pt.objects.provincias);
  for(const p of T.provincias){byS[p.s]=p;byId[p.id]=p}
  for(const c of T.ciudades)cityS[c.s]=c;
  const fd=d=>{const[y,m,x]=d.split("-");return +x+" "+MES[+m-1]+" "+y};
  document.getElementById("stamp").innerHTML=`Paso 2 de 5<br>Corte ${fd(T.corte)} · próxima ${fd(T.proxima)}`;
  document.getElementById("foot-date").textContent=`Corte del ${fd(T.corte)}; próxima revisión el ${fd(T.proxima)}.`;
  setup();addEventListener("hashchange",route);route();
}).catch(e=>{app.innerHTML=`<p style="padding:40px 0">No se pudo cargar el mapa: ${esc(e.message)}</p>`});
}
