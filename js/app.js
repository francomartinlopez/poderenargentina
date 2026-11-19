// El mapa del poder argentino · aplicación
{
const MOT={cap:["Capital","#F5F0E6"],pob:["Ciudad grande","#9A9A9A"],emp:["Empresa o cluster","#FF3B30"],pue:["Puerto","#2F6BFF"],ene:["Energía","#F2A93B"],min:["Minería","#C8743C"],fro:["Frontera","#3FB8C9"],def:["Defensa y estrategia","#9E8CFF"]};
const ORDEN=["emp","pue","ene","min","fro","def","cap","pob"];
const POT=["EE.UU.","China","Unión Europea","Reino Unido","Brasil","Rusia","Israel","Golfo","Canadá y Australia","Japón y Corea","FMI, BM y BID"];
const CK=["com","inv","deu","pre","pol"],CAN=["Comercio","Inversión","Deuda","Presencia","Política"];
const CAPAS=[["terr","Territorio",1],["ali","Alineamiento con Nación",1],["inf","Influencias mundiales",1],["eco","Economía y recursos",1],["act","Actores",1],["zl","Zonas liberadas"],["fr","Fricción"]];
const PCOL={"EE.UU.":"#2F6BFF","China":"#D7263D","Unión Europea":"#F2C14E","Reino Unido":"#7FB3D5","Brasil":"#2EB872","Rusia":"#9E1B32","Israel":"#A0C4FF","Golfo":"#C8743C","Canadá y Australia":"#B07CFF","Japón y Corea":"#FF8FAB","FMI, BM y BID":"#BDBDBD"};
const ACOL={A:"#8E6CFF",D:"#9A8F8C",I:"#F2A93B",O:"#3FB8C9"},ALI={A:"Aliado",D:"Dialoguista",I:"Independiente",O:"Opositor"};
const ADESC={A:"acuerdos electorales con La Libertad Avanza",D:"negocia votos y fondos sin acuerdo electoral pleno",I:"espacio propio que compite con LLA (Provincias Unidas)",O:"opositor al Gobierno nacional"};
let capa="terr",potSel="dom",ecoSel="exp";
const TCOL={Estado:"#FF3B30",Persona:"#F5F0E6",Capital:"#F2A93B",Influencia:"#3FB8C9",Información:"#9E8CFF",Sombra:"#8B8B8B"};
const RCOL={Gobierna:"#FF3B30",Propiedad:"#F2A93B",Financiamiento:"#2EB872",Alianza:"#2F6BFF",Enfrentamiento:"#D7263D",Ambigua:"#9A8F8C",Contrato:"#C8743C",Abastecimiento:"#7FB3D5","Puerta giratoria":"#B07CFF"};
const ACT={},actCity={},actProv={};
const aName=id=>ACT[id]?ACT[id].n:(T.meta.act.externos[id]||id);
const aLink=id=>ACT[id]?`<a href="#a-${id}">${esc(ACT[id].n)}</a>`:`<a href="${esc(T.meta.act.global_url)}#o-${id}" target="_blank" rel="noopener">${esc(aName(id))}</a> <span class="muted" style="font-size:12px">(mapa global)</span>`;
const ptBar=(v,c,k)=>`<span class="ptb"><em style="width:${(v*(k||1.1)).toFixed(1)}px;background:${c||"#FF3B30"}"></em><b class="mono">${v.toLocaleString("es-AR",{maximumFractionDigits:1})}</b></span>`;
function actList(list,lim){return list.length?`<ul class="alist">${list.slice(0,lim||99).map(a=>`<li><a href="#a-${a.id}">${esc(a.n)}</a><span class="muted">${esc(a.cat)}</span>${ptBar(a.pt,TCOL[a.tipo],.56)}</li>`).join("")}</ul>`:`<p class="muted">Ningún actor núcleo con sede aquí todavía.</p>`}
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
function influ(list,title,nota){return `<div class="blk"><h2>${title||"Influencias mundiales"}</h2>${infGrid(list)}<p class="muted" style="font-size:13px;margin:8px 0 10px">${nota||"De 0 a 3 por canal. Comercio: participación en las exportaciones (INDEC); el resto, con la fuente de cada dato."}</p><details><summary>${list.length} ${list.length===1?"dato":"datos"} con fuente</summary>${infList(list)}</details></div>`}

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
    const[k,v]=t.dataset.k.split(":");const txt=k==="p"?tipText(byId[v]):k==="d"?(depInfo[v]?.n||v):capa==="act"&&actCity[v]?`${cityS[v].n}: ${actCity[v].length} actores`:cityS[v]?.n;tip.textContent=txt;tip.style.display="block";tip.style.left=e.clientX+14+"px";tip.style.top=e.clientY+12+"px"});
  svg.addEventListener("pointerleave",()=>tip.style.display="none");
  new ResizeObserver(()=>scaleMarks()).observe(svg);
  document.getElementById("capas").onclick=e=>{const b=e.target.closest("button[data-c]");if(!b||b.disabled)return;capa=b.dataset.c;route()};
  document.getElementById("sub").onclick=e=>{const b=e.target.closest("button");if(!b)return;if(b.dataset.pot)potSel=b.dataset.pot;if(b.dataset.eco)ecoSel=b.dataset.eco;route()};
}
function tipText(p){
  if(capa==="ali")return `${p.n}: ${ALI[p.ali.ali]}`;
  if(capa==="inf")return potSel==="dom"?`${p.n}: ${p.dom||(p.emp.length?"empate entre "+p.emp.join(", "):"sin datos")}`:`${p.n}: ${potSel} ${p.tot[potSel]||0} puntos`;
  if(capa==="act")return `${p.n}: ${(actProv[p.id]||[]).length} actores núcleo con sede`;
  if(capa==="eco")return ecoSel==="exp"?`${p.n}: USD ${nf(p.eco.exp)} M exportados`:`${p.n}: ${p.eco.propios==null?"sin datos":p.eco.propios.toLocaleString("es-AR")+"% de recursos propios"}`;
  return p.n}
function paint(){
  document.getElementById("capas").innerHTML=CAPAS.map(([k,n,on])=>on?`<button class="chip ${capa===k?"on":""}" data-c="${k}" aria-pressed="${capa===k}">${n}</button>`:`<button class="chip" disabled title="Se carga en los próximos pasos">${n} <small>pronto</small></button>`).join("");
  const P=T.provincias,sub=document.getElementById("sub");let leg="";
  const maxPot=k=>Math.max(1,...P.map(p=>p.tot[k]||0)),maxExp=Math.max(...P.map(p=>p.eco.exp));
  const fill=p=>{
    if(capa==="ali")return[ACOL[p.ali.ali],.6];
    if(capa==="inf"){if(potSel==="dom")return p.dom?[PCOL[p.dom],.62]:p.emp.length?["#6E6462",.55]:null;const v=p.tot[potSel]||0;return v?[PCOL[potSel],.18+.7*v/maxPot(potSel)]:null}
    if(capa==="act"){const n=(actProv[p.id]||[]).length;return n?["#FF3B30",.12+.5*Math.min(1,n/6)]:null}
    if(capa==="eco"){if(ecoSel==="exp")return["#FF3B30",.1+.8*Math.log10(p.eco.exp)/Math.log10(maxExp)];return p.eco.propios==null?null:["#FF3B30",.1+.8*p.eco.propios/90]}
    return null};
  for(const el of G.p.children){const p=byId[el.dataset.k.slice(2)],f=fill(p);el.style.fill=f?f[0]:"";el.style.fillOpacity=f?f[1]:"";el.querySelector("title").textContent=tipText(p)}
  if(capa==="ali"){const c={};P.forEach(p=>c[p.ali.ali]=(c[p.ali.ali]||0)+1);leg=Object.keys(ALI).map(a=>`<span class="lg"><i style="background:${ACOL[a]}"></i>${ALI[a]} ${c[a]||0}</span>`).join("")}
  else if(capa==="inf"){leg=`<button class="chip ${potSel==="dom"?"on":""}" data-pot="dom">Dominante</button>`+POT.map(k=>`<button class="chip ${potSel===k?"on":""}" data-pot="${esc(k)}"><i style="background:${PCOL[k]}"></i>${esc(k)}</button>`).join("")}
  else if(capa==="act"){leg=`<span class="lg">Círculos: ciudades sede de actores núcleo, según la suma de sus puntajes. La mayoría tiene sede en la Capital.</span>`}
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
  const step=now=>{if(!svg||!svg.isConnected)return;let k=dur?Math.min(1,(now-t0)/dur):1;k=k<.5?2*k*k:1-(-2*k+2)**2/2;
    cur=from.map((v,i)=>v+(b[i]-v)*k);svg.setAttribute("viewBox",cur.join(" "));scaleMarks();if(k<1)requestAnimationFrame(step)};
  requestAnimationFrame(step);
}
function scaleMarks(){
  if(!svg)return;const r=svg.getBoundingClientRect();if(!r.width)return;
  const px=Math.max(cur[2]/r.width,cur[3]/r.height);
  for(const c of G.c.children)c.setAttribute("r",(c.classList.contains("cap")?5.2:4.2)*px*(+c.dataset.m||1));
  const placed=[];
  for(const l of G.l.children){const fs=12*px,x=+l.getAttribute("x")+7*px,y=+l.getAttribute("y")+4*px,w=l.textContent.length*fs*.56,bb=[x-2*px,y-fs,x+w,y+3*px];
    l.setAttribute("font-size",fs);l.setAttribute("stroke-width",3*px);l.setAttribute("dx",7*px);l.setAttribute("dy",4*px);
    const hit=!l.classList.contains("keep")&&placed.some(o=>bb[0]<o[2]&&bb[2]>o[0]&&bb[1]<o[3]&&bb[3]>o[1]);
    l.style.display=hit?"none":"";if(!hit)placed.push(bb)}
}
function drawCities(list,labels,sel){
  const vis=capa==="act"?list.filter(c=>actCity[c.s]||c.s===sel):list.filter(c=>c.mot.some(m=>filt.has(m))||c.s===sel);
  vis.sort((a,b)=>(a.mot.includes("cap")-b.mot.includes("cap")));
  G.c.innerHTML=vis.map(c=>`<circle class="city ${c.mot.includes("cap")?"cap":""} ${c.s===sel?"sel":""}" cx="${c.xy[0]}" cy="${c.xy[1]}" r="3" fill="${color(c)}" data-k="c:${c.s}" ${capa==="act"&&actCity[c.s]?`data-m="${(1+Math.log1p(actCity[c.s].reduce((t,a)=>t+a.pt,0))/2.6).toFixed(2)}" style="fill:#FF3B30;fill-opacity:.75"`:""}></circle>`).join("");
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
  else if(capa==="act")side=`<h2>Los más poderosos</h2>${actList(T.actores,12)}<p class="muted" style="font-size:13px;margin:8px 0 0">Puntaje de 0 a 100, con el mismo método que el mapa global. <a href="#actores">Ver los ${T.actores.length} actores y sus relaciones</a>.</p>`;
  else side=`<h2>Por qué está cada ciudad</h2><div class="mbars">${Object.keys(MOT).map(m=>`<div><span>${MOT[m][0]}</span><em style="width:${cnt[m]/mx*100}%;background:${MOT[m][1]}"></em><span>${cnt[m]||0}</span></div>`).join("")}</div>
  <p class="muted" style="font-size:13px;margin:8px 0 0">Una ciudad puede tener varios motivos. Las de empresa o cluster entran aunque sean chicas.</p>`;
  document.getElementById("panel").innerHTML=`<h1>Argentina</h1><p class="sub">Tocá una provincia para bajar a sus departamentos y ciudades. Cambiá la capa para ver alineamiento, influencias o economía.</p>
  <div class="facts"><div><span>Población (Censo 2022)</span><b class="mono">${nf(T.pais.pob)}</b></div><div><span>Departamentos</span><b class="mono">${P.reduce((s,p)=>s+p.ndep,0)}</b></div><div><span>Ciudades en el mapa</span><b class="mono">${T.ciudades.length}</b></div></div>
  <div class="blk grow">${side}</div>`;
  more(influ(T.pais.inf,"Influencias sobre el Estado nacional","Vínculos de la Nación con cada potencia. Las de cada provincia, en su ficha.")+`<div class="blk"><h2>Quién manda</h2>${actList(T.actores,8)}<p style="margin-top:10px"><a href="#actores">Los ${T.actores.length} actores núcleo, su puntaje y sus relaciones</a></p></div>`);
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
  more(manda+influ(p.inf)+eco+`<div class="blk"><h2>Actores núcleo con sede</h2>${actList(actProv[p.id]||[])}<p class="muted" style="font-size:13px;margin-top:8px">Los actores provinciales y municipales llegan en el paso 5.</p></div>`+depBlk);
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
  <div class="facts"><div><span>Provincia</span><b><a href="#prov-${p.s}">${esc(p.n)}</a></b></div>${d&&p.id!=="02"?`<div><span>${esc(d.cat)}</span><b><a href="#d-${c.dep}">${esc(d.n)}</a></b></div>`:""}${c.proy?`<div><span>Población (proyección ${c.proya})</span><b class="mono">${nf(c.proy)}</b></div>`:""}${c.pob?`<div><span>${c.proy?"Último censo de la localidad":"Población"} (${c.est?"estimación ":"Censo "}${c.anio})</span><b class="mono">${nf(c.pob)}</b></div>`:c.ag||!c.mot.some(m=>m==="def"||m==="ene"||m==="min")?(c.ag?"":`<div><span>Población</span><b class="mono">s/d</b></div>`):""}${c.ag&&(c.ag!==c.n||!c.pob)?`<div><span>Aglomerado ${esc(c.ag)}</span><b class="mono">${nf(c.agpob)}</b></div>`:""}${d&&p.id!=="02"?`<div><span>Población del ${esc(d.cat.toLowerCase())}</span><b class="mono">${T.deppob[c.dep]?nf(T.deppob[c.dep]):"—"}</b></div>`:""}<div><span>Coordenadas</span><b class="mono" style="font-size:13px">${c.lat.toFixed(3)}, ${c.lon.toFixed(3)}</b></div></div>
  <div class="blk grow"><h2>Por qué está en el mapa</h2>${tags(c)}${c.proy?`<p class="muted" style="font-size:13px">${esc(c.proyn)} ${src(c.fproy)}</p>`:""}${c.exc?`<p class="muted" style="font-size:13px">${esc(c.exc)}</p>`:""}${c.fuente?`<p class="src">Fuente: ${src(c.fuente)}</p>`:""}<p class="src">${c.ag?`Aglomerado: Censo 2022 (2010: ${nf(c.agpob10)}), ${src(c.fag)}. `:""}${c.fpob?`Localidad: ${src(c.fpob)}.`:""}${c.ag&&c.ag!==c.n?" El aglomerado une varias localidades; la cifra es la del conjunto.":""}</p></div>`;
  const it=c.int;
  const gob=`<div class="blk"><h2>Quién gobierna y quién manda</h2>${it?`<dl class="dl"><dt>${p.id==="02"?"Jefe de Gobierno":c.int.nota&&/partido/.test(c.int.nota)?"Intendente del partido":"Intendente"}</dt><dd><b>${esc(it.n)}</b>${it.par?` <span class="muted">· ${esc(it.par)}</span>`:""}${it.ver==="W"?` <span class="tag" title="Según la ficha de la ciudad en Wikipedia; se confirma en el próximo corte" style="color:#9A8F8C">a confirmar</span>`:""}</dd>${it.nota?`<dt>Nota</dt><dd>${esc(it.nota)}</dd>`:""}<dt>Fuente</dt><dd>${src(it.u)}</dd></dl>`:`<p class="muted">Intendente sin dato verificado todavía.</p>`}${c.manda?`<p class="lead" style="margin-top:12px">${esc(c.manda)}</p>`:""}</div>`;
  const conf=c.conf?`<div class="blk"><h2>Conflictos</h2><ul class="rlist">${c.conf.map(f=>`<li><b>${esc(f.t)}.</b> ${esc(f.x)} ${src(f.u)}</li>`).join("")}</ul></div>`:"";
  more(gob+(c.inf?influ(c.inf,"Influencias mundiales","Por las empresas y proyectos con sede en la ciudad, de 0 a 3 por canal. Las de la provincia, en su ficha."):`<div class="blk"><h2>Influencias mundiales</h2><p>Sin influencias propias cargadas: rigen las de la provincia, <a href="#prov-${p.s}">${esc(p.n)}</a>${p.dom?`, donde domina <b style="color:${PCOL[p.dom]}">${esc(p.dom)}</b>`:""}.</p></div>`)+conf+`<div class="blk"><h2>Actores núcleo con sede</h2>${actList(actCity[c.s]||[])}<p class="muted" style="font-size:13px;margin-top:8px">Empresas, sindicatos y actores locales, en el paso 5.</p></div>`);
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
  <p class="muted" style="font-size:13px">Población del aglomerado urbano cuando la ciudad forma parte de uno (Censo 2022); con asterisco, cuando el aglomerado une varias localidades. Las ciudades chicas, con la población de la localidad del Censo 2022; donde el último dato es de 2001 o 2010, una proyección propia a 2026 con el crecimiento del departamento, marcada como «proy.».</p><table class="stack"><thead><tr><th>Ciudad</th><th>Provincia</th><th class="n">Población</th><th>Intendente</th><th>Motivos</th><th>Por qué</th></tr></thead><tbody id="ct"></tbody></table></div>`;
  const draw=()=>{const q=cq.normalize("NFD").replace(/[̀-ͯ]/g,"").toLowerCase();
    document.getElementById("ct").innerHTML=T.ciudades.filter(c=>(!cm||c.mot.includes(cm))&&(c.n+" "+byId[c.prov].n).normalize("NFD").replace(/[̀-ͯ]/g,"").toLowerCase().includes(q))
    .map(c=>`<tr><td><a href="#c-${c.s}">${esc(c.n)}</a></td><td>${esc(byId[c.prov].c)}</td><td class="n" title="${c.ag&&c.ag!==c.n?"Aglomerado "+esc(c.ag):""}">${c.agpob?nf(c.agpob)+(c.ag!==c.n?"*":""):c.proy?nf(c.proy)+" (proy. "+c.proya+")":c.pob?nf(c.pob)+(c.anio!==2022?` (${c.anio})`:""):"s/d"}</td><td>${c.int?esc(c.int.n)+(c.int.fam?` <span class="muted" style="font-size:12px">${esc(c.int.fam)}</span>`:""):`<span class="muted">s/d</span>`}</td><td>${tags(c)}</td><td>${esc(c.nota)}</td></tr>`).join("")||`<tr><td colspan="6" class="muted">Sin resultados.</td></tr>`};
  document.getElementById("q").oninput=e=>{cq=e.target.value;draw()};
  document.getElementById("cf").onclick=e=>{const b=e.target.closest("button");if(!b)return;cm=b.dataset.m||null;vCiudades()};draw();
}
function vPlan(){
  app.innerHTML=`<div class="page plan"><h1>Plan</h1>
  <h2>Hecho</h2><ol><li><b>Esqueleto.</b> Mapa oficial del IGN con zoom de país a provincia, departamento y ciudad; ${T.ciudades.length} ciudades con su motivo; gobernadores al día.</li><li><b>Las 24 provincias.</b> Población del Censo 2022 por provincia y departamento; exportaciones, destinos y rubro principal (INDEC); recursos propios frente a los fondos nacionales (ASAP); quién manda de verdad y alineamiento con la Nación; influencias de 11 potencias en cinco canales, con fuente. Capas de alineamiento, influencias y economía en el mapa.</li><li><b>Actores núcleo.</b> ${T.actores.length} actores nacionales medidos en los 21 ejes con la fórmula del mapa global, con ficha, fuentes y ${T.relaciones.length} relaciones; capa de actores en el mapa.</li><li><b>Fichas de ciudades.</b> Intendente de ${T.ciudades.filter(c=>c.int).length} ciudades, quién manda en las ciudades de empresa, influencias propias de ${T.ciudades.filter(c=>c.inf).length} ciudades y conflictos documentados.</li></ol>
  <h2>Próximos pasos</h2><ol start="5"><li>Actores provinciales y municipales; puntos de fricción; zonas liberadas.</li></ol>
  <h2>Método de las influencias</h2><p>Cada potencia recibe de 0 a 3 en cinco canales. El comercio se calcula con la participación de cada destino en las exportaciones de la provincia (40% o más vale 3; de 20% a 40%, 2; de 8% a 20%, 1); cuando el INDEC informa un bloque se toma como aproximación (USMCA como EE.UU. y Mercosur como Brasil). Inversión, deuda, presencia e influencia política se cargan dato por dato con su fuente. La potencia dominante es la de mayor suma; si dos empatan, se marca el empate.</p>
  <h2>Pendientes</h2><ul><li>Intendentes marcados «a confirmar» (tomados de Wikipedia) y los nueve sin dato: La Banda, Libertador General San Martín, Timbúes, Susques, San Antonio de los Cobres, Calingasta, Salvador Mazza, Aguas Blancas y La Quiaca.</li><li>Censo 2022 de seis localidades (Susques, San Antonio de los Cobres, Antofagasta de la Sierra, Calingasta, Jáchal y Salvador Mazza): hoy se muestra una proyección propia a 2026.</li></ul></div>`;
}
let atSel=null;
function vActores(){
  const A=T.actores,tipos=[...new Set(A.map(a=>a.tipo))];
  app.innerHTML=`<div class="page"><h1>Actores</h1><p class="sub">Quién tiene el poder real en la Argentina: ${A.length} actores núcleo nacionales medidos en 21 ejes, con el mismo método y la misma fórmula que El mapa del poder global. En este mapa, el 3 de cada eje es dominio a escala nacional.</p>
  <div class="bar" id="tf"><button class="chip ${atSel?"":"on"}" data-t="">Todos</button>${tipos.map(t=>`<button class="chip ${atSel===t?"on":""}" data-t="${t}"><i style="background:${TCOL[t]}"></i>${t} <small>${A.filter(a=>a.tipo===t).length}</small></button>`).join("")}</div>
  <table class="stack"><thead><tr><th class="n">#</th><th>Actor</th><th>Categoría</th><th>Sede</th><th>Alcance</th><th>Puntaje de poder</th><th class="n" title="Poder real que no surge del cargo formal">Oculto</th></tr></thead><tbody>
  ${A.map((a,i)=>[a,i]).filter(([a])=>!atSel||a.tipo===atSel).map(([a,i])=>`<tr><td class="n mono">${i+1}</td><td><a href="#a-${a.id}">${esc(a.n)}</a></td><td style="color:${TCOL[a.tipo]}">${esc(a.cat)}</td><td><a href="#c-${a.cs}">${esc(a.sede==="Ciudad Autónoma de Buenos Aires"?"CABA":a.sede)}</a></td><td>${esc(T.meta.act.alcance[a.alc])}</td><td>${ptBar(a.pt,TCOL[a.tipo])}</td><td class="n mono">${a.oculto.toLocaleString("es-AR")}</td></tr>`).join("")}</tbody></table>
  <h2 class="sec">Red de relaciones</h2><p class="muted" style="font-size:14px;max-width:760px">${T.relaciones.length} relaciones con fuente. Pasá el cursor por un actor para ver sus vínculos; tocalo para abrir su ficha. Los nodos grises son actores del mapa global.</p>
  <div class="bar">${Object.keys(RCOL).filter(t=>T.relaciones.some(r=>r.t===t)).map(t=>`<span class="lg"><i style="background:${RCOL[t]}"></i>${t}</span>`).join("")}</div>
  ${netSvg()}
  <h2 class="sec">Método</h2><p style="max-width:760px">Cada actor recibe de 0 a 3 en 21 ejes (materia, dinero, fuerza, información, personas y norma). Coerción, adquisición de información y acción fuera de la ley valen el doble; contactos y privilegio legal, una vez y media. El puntaje final es una media geométrica ponderada de la categoría teórica del actor (40 %), su capacidad (30 %), su alcance (20 %), su autonomía real (5 %) y el poder que hereda de quienes dependen de él (5 %); el resultado se eleva al cubo y el mayor vale 100. El poder oculto mide cuánto de ese poder no surge del cargo formal. La acción fuera de la ley solo se puntúa con un hecho establecido por un tribunal u organismo oficial.</p></div>`;
  document.getElementById("tf").onclick=e=>{const b=e.target.closest("button");if(!b)return;atSel=b.dataset.t||null;vActores()};
  netWire();
}
function netSvg(){
  const A=T.actores,ext=[...new Set(T.relaciones.flatMap(r=>[r.o,r.d]).filter(id=>!ACT[id]))];
  const ord=["Persona","Estado","Capital","Información","Influencia","Sombra"];
  const nodes=[...A.slice().sort((a,b)=>ord.indexOf(a.tipo)-ord.indexOf(b.tipo)||b.pt-a.pt),...ext.map(id=>({id,n:aName(id),ext:1,pt:20}))];
  const R=290,C=480,pos={};nodes.forEach((n,i)=>{const t=i/nodes.length*2*Math.PI-Math.PI/2;pos[n.id]=[C+R*Math.cos(t),C+R*Math.sin(t),t]});
  const edges=T.relaciones.map(r=>{const[a,b]=[pos[r.o],pos[r.d]];return `<path class="ne" data-a="${r.o}" data-b="${r.d}" d="M${a[0].toFixed(1)},${a[1].toFixed(1)} Q${C},${C} ${b[0].toFixed(1)},${b[1].toFixed(1)}" stroke="${RCOL[r.t]}" stroke-width="${r.n*.9}"><title>${esc(aName(r.o))} → ${esc(aName(r.d))} · ${r.t}: ${esc(r.x)}</title></path>`}).join("");
  const nd=nodes.map(n=>{const[x,y,t]=pos[n.id],deg=t*180/Math.PI,left=Math.cos(t)<0,lx=C+(R+14)*Math.cos(t),ly=C+(R+14)*Math.sin(t);
    const short=n.n.replace(/ \(.*\)$/,"").replace(/^Gobierno de la Provincia de |^Gobierno del? /,"Gob. ").replace("Corte Suprema de Justicia de la Nación","Corte Suprema").replace("Ministerio de Seguridad y fuerzas federales","Seguridad federal").replace("Banco Central de la República Argentina","BCRA").replace("Fondo Monetario Internacional","FMI").replace("Banco de la Nación Argentina","Banco Nación");
    return `<g class="nn" data-id="${n.id}" ${n.ext?`data-ext="1"`:""}><circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${(3+Math.sqrt(n.pt)*.9).toFixed(1)}" fill="${n.ext?"#5A5150":TCOL[n.tipo]}"></circle><text x="${lx.toFixed(1)}" y="${ly.toFixed(1)}" transform="rotate(${left?deg+180:deg} ${lx.toFixed(1)} ${ly.toFixed(1)})" text-anchor="${left?"end":"start"}" dy="4">${esc(short)}</text></g>`}).join("");
  return `<div class="net"><svg id="net" viewBox="0 0 960 960" role="img" aria-label="Red de relaciones entre actores">${edges}${nd}</svg></div>`;
}
function netWire(){
  const s=document.getElementById("net");if(!s)return;
  s.addEventListener("pointerover",e=>{const g=e.target.closest(".nn");if(!g)return;const id=g.dataset.id;s.classList.add("hl");
    s.querySelectorAll(".ne").forEach(p=>p.classList.toggle("on",p.dataset.a===id||p.dataset.b===id));
    const nb=new Set([id]);s.querySelectorAll(".ne.on").forEach(p=>{nb.add(p.dataset.a);nb.add(p.dataset.b)});s.querySelectorAll(".nn").forEach(n=>n.classList.toggle("on",nb.has(n.dataset.id)))});
  s.addEventListener("pointerout",e=>{if(e.target.closest(".nn")){s.classList.remove("hl")}});
  s.addEventListener("click",e=>{const g=e.target.closest(".nn");if(!g)return;if(g.dataset.ext)window.open(T.meta.act.global_url+"#o-"+g.dataset.id,"_blank","noopener");else location.hash="a-"+g.dataset.id});
}
function vActor(a){
  const M=T.meta.act,i=T.actores.indexOf(a),c=cityS[a.cs];
  const rel=T.relaciones.filter(r=>r.o===a.id||r.d===a.id),deps=T.actores.filter(x=>x.dep.includes(a.id));
  const grupos=[...new Set(M.ejes.map(e=>e.g))];
  const ejes=grupos.map(g=>`<div class="axg"><h3>${g}</h3>${M.ejes.map((e,k)=>[e,k]).filter(([e])=>e.g===g).map(([e,k])=>{const v=a.sc[k];return `<div class="axr" title="${esc(e.d)}${v?" · "+v+": "+esc(e.a[3-v]):""}"><span>${esc(e.n)}${M.pesos[e.k]?` <small class="muted">×${String(M.pesos[e.k]).replace(".",",")}</small>`:""}</span><span class="dots">${[1,2,3].map(n=>`<i class="${n<=v?"on":""}"></i>`).join("")}</span><b class="mono">${v}</b></div>`}).join("")}</div>`).join("");
  const compN={ct:"Categoría teórica",cap:"Capacidad",alc:"Alcance",aut:"Autonomía real",red:"Red heredada"};
  app.innerHTML=`<div class="page actor"><p class="crumbs"><a href="#actores">Actores</a> › <b>${esc(a.n)}</b></p>
  <h1>${esc(a.n)}</h1><p class="sub">${esc(a.res)}</p>
  <div class="facts"><div><span>Puntaje de poder</span><b class="mono">${a.pt.toLocaleString("es-AR")} <small class="muted">· n.º ${i+1}</small></b></div><div><span>Poder oculto</span><b class="mono">${a.oculto.toLocaleString("es-AR")}</b></div><div><span>Categoría</span><b style="color:${TCOL[a.tipo]};font-size:15px">${esc(a.cat)}</b></div><div><span>Sede</span><b style="font-size:15px">${c?`<a href="#c-${c.s}">${esc(c.n)}</a>`:esc(a.sede)}</b></div><div><span>Alcance</span><b style="font-size:15px">${esc(M.alcance[a.alc])}</b></div><div><span>Autonomía</span><b style="font-size:15px">${esc(M.autonomia[a.aut])}</b></div><div><span>Depende de</span><b style="font-size:15px">${a.dep.length?a.dep.map(aLink).join(", "):"Nadie en el mapa"}</b></div><div><span>Bloque</span><b style="font-size:15px">${esc(M.bloques[a.bloque])}</b></div></div>
  <div class="cols"><div><h2 class="sec">Quién manda</h2><p class="lead">${esc(a.manda)}</p>
  <h2 class="sec">Relaciones · ${rel.length}</h2>${rel.length?`<ul class="rlist">${rel.map(r=>{const o=r.o===a.id?r.d:r.o,dir=r.o===a.id?"→":"←";return `<li><span class="tag" style="color:${RCOL[r.t]}">${r.t} ${dir}</span> ${aLink(o)} <span class="mono muted">${"●".repeat(r.n)}</span><br><span class="muted">${esc(r.x)}</span> ${src(r.u)}</li>`}).join("")}</ul>`:`<p class="muted">Sin relaciones cargadas todavía.</p>`}
  ${deps.length?`<h2 class="sec">Dependen de este actor</h2><p>${deps.map(d=>aLink(d.id)).join(" · ")}</p>`:""}
  <h2 class="sec">Fuentes</h2><ul class="flist">${a.fu.map(([t,u])=>`<li><a href="${esc(u)}" target="_blank" rel="noopener">${esc(t)}</a></li>`).join("")}</ul>
  <p class="muted" style="font-size:13px">Certeza: ${esc(M.certeza[a.cert])}. Corte del ${esc(T.corte)}.</p></div>
  <div><h2 class="sec">21 ejes</h2><div class="axes">${ejes}</div>
  <h2 class="sec">Cómo se forma el puntaje</h2><div class="mbars">${Object.keys(M.peso_final).map((k,j)=>`<div><span>${compN[k]} <small class="muted">${Math.round(M.peso_final[k]*100)} %</small></span><em style="width:${a.cp[j]*100}%;background:#FF3B30"></em><span>${a.cp[j].toLocaleString("es-AR")}</span></div>`).join("")}</div>
  <p class="muted" style="font-size:13px">Cada componente va de 0 a 1. Capacidad ${a.cap.toLocaleString("es-AR")} de 63 posibles. <a href="#actores">Método</a>.</p></div></div></div>`;
}
function route(){
  const h=decodeURIComponent(location.hash.slice(1));tip.style.display="none";let nk="inicio";
  if(h.startsWith("prov-")&&byS[h.slice(5)])vProv(byS[h.slice(5)]);
  else if(h.startsWith("d-")){const id=h.slice(2),p=byId[id.slice(0,2)];if(p)loadDep(p.id).then(()=>depInfo[id]?vProv(p,id):vProv(p))}
  else if(h.startsWith("c-")&&cityS[h.slice(2)])vCity(cityS[h.slice(2)]);
  else if(h==="provincias"){vProvincias();nk=h;svg=null}
  else if(h==="ciudades"){vCiudades();nk=h;svg=null}
  else if(h==="plan"){vPlan();nk=h;svg=null}
  else if(h==="actores"){vActores();nk=h;svg=null}
  else if(h.startsWith("a-")&&ACT[h.slice(2)]){vActor(ACT[h.slice(2)]);nk="actores";svg=null}
  else vPais();
  document.querySelectorAll("nav a").forEach(a=>a.classList.toggle("on",a.dataset.k===nk));
  if(["provincias","ciudades","plan","actores"].includes(nk))window.scrollTo(0,0);
}
Promise.all(["data/territorio.json","data/provincias.json","data/antartida.json"].map(u=>fetch(u).then(r=>r.json()))).then(([t,pt,an])=>{
  T=t;ANT=an.features?an.features[0]:an;{const g=ANT.geometry||ANT;if(d3.geoArea(ANT)>2*Math.PI)(g.type==="Polygon"?[g.coordinates]:g.coordinates).forEach(pl=>pl.forEach(r=>r.reverse()))}
  PF=topojson.feature(pt,pt.objects.provincias);
  for(const p of T.provincias){byS[p.s]=p;byId[p.id]=p}
  for(const c of T.ciudades)cityS[c.s]=c;
  for(const a of T.actores){ACT[a.id]=a;(actCity[a.cs]=actCity[a.cs]||[]).push(a);(actProv[a.prov]=actProv[a.prov]||[]).push(a)}
  const fd=d=>{const[y,m,x]=d.split("-");return +x+" "+MES[+m-1]+" "+y};
  document.getElementById("stamp").innerHTML=`Paso 4 de 5<br>Corte ${fd(T.corte)} · próxima ${fd(T.proxima)}`;
  document.getElementById("foot-date").textContent=`Corte del ${fd(T.corte)}; próxima revisión el ${fd(T.proxima)}.`;
  setup();addEventListener("hashchange",route);route();
}).catch(e=>{app.innerHTML=`<p style="padding:40px 0">No se pudo cargar el mapa: ${esc(e.message)}</p>`});
}
