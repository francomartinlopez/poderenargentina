// El mapa del poder argentino · aplicación
{
const MOT={cap:["Capital","#F5F0E6"],pob:["Ciudad grande","#9A9A9A"],emp:["Empresa o cluster","#FF3B30"],pue:["Puerto","#2F6BFF"],ene:["Energía","#F2A93B"],min:["Minería","#C8743C"],fro:["Frontera","#3FB8C9"],def:["Defensa y estrategia","#9E8CFF"]};
const ORDEN=["emp","pue","ene","min","fro","def","cap","pob"];
const POT=["EE.UU.","China","Unión Europea","Reino Unido","Brasil","Rusia","Israel","Golfo","Canadá y Australia","Japón y Corea","FMI, BM y BID"];
const CAN=["Comercio","Inversión","Deuda","Presencia","Política y cultura"];
const CAPAS=[["terr","Territorio",1],["act","Actores"],["ali","Alineamiento con Nación"],["inf","Influencias mundiales"],["eco","Economía y recursos"],["zl","Zonas liberadas"],["fr","Fricción"]];
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
function influ(){return `<div class="blk"><h2>Influencias mundiales</h2><div class="pend"><b>Paso 2.</b> Cada potencia se puntúa de 0 a 3 en cinco canales, con fuente. El color del territorio en el mapa será el de la potencia dominante.</div>
<div class="grid5" aria-hidden="true"><span class="h"></span>${CAN.map(c=>`<span class="h" title="${c}">${c.split(" ")[0]}</span>`).join("")}${POT.slice(0,6).map(p=>`<span class="r">${p}</span>`+CAN.map(()=>`<span>·</span>`).join("")).join("")}</div>
<p class="muted" style="font-size:13px;margin:8px 0 0">También se miden: ${POT.slice(6).join(", ")}.</p></div>`}

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
  <div class="bar" role="group" aria-label="Capas">${CAPAS.map(([k,n,on])=>on?`<button class="chip on" aria-pressed="true">${n}</button>`:`<button class="chip" disabled title="Se carga en los próximos pasos">${n} <small>pronto</small></button>`).join("")}</div>
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
    const[k,v]=t.dataset.k.split(":");const txt=k==="p"?byId[v].n:k==="d"?(depInfo[v]?.n||v):cityS[v]?.n;tip.textContent=txt;tip.style.display="block";tip.style.left=e.clientX+14+"px";tip.style.top=e.clientY+12+"px"});
  svg.addEventListener("pointerleave",()=>tip.style.display="none");
  new ResizeObserver(()=>scaleMarks()).observe(svg);
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
function ensureMap(){if(!document.getElementById("map")){mapShell()}filters()}

function vPais(){
  ensureMap();provState(null);drawCities(T.ciudades,false);zoomTo(FULL);crumbs([["Argentina"]]);
  document.getElementById("ant").style.display="";
  const cnt={};for(const c of T.ciudades)for(const m of c.mot)cnt[m]=(cnt[m]||0)+1;const mx=Math.max(...Object.values(cnt));
  document.getElementById("panel").innerHTML=`<h1>Argentina</h1><p class="sub">Tocá una provincia para bajar a sus departamentos y ciudades. Tocá una ciudad para abrir su ficha.</p>
  <div class="facts"><div><span>Jurisdicciones</span><b>24</b></div><div><span>Departamentos</span><b class="mono">${T.provincias.reduce((s,p)=>s+p.ndep,0)}</b></div><div><span>Ciudades en el mapa</span><b class="mono">${T.ciudades.length}</b></div></div>
  <div class="blk grow"><h2>Por qué está cada ciudad</h2><div class="mbars">${Object.keys(MOT).map(m=>`<div><span>${MOT[m][0]}</span><em style="width:${cnt[m]/mx*100}%;background:${MOT[m][1]}"></em><span>${cnt[m]||0}</span></div>`).join("")}</div>
  <p class="muted" style="font-size:13px;margin:8px 0 0">Una ciudad puede tener varios motivos. Las de empresa o cluster entran aunque sean chicas.</p></div>`;
  more(influ()+pend("Quién manda","<b>Paso 3.</b> Unos 40 actores núcleo nacionales con sus relaciones: Casa Rosada, Economía, BCRA, Corte, Comodoro Py, SIDE, partidos, sindicatos, grandes grupos y poder externo."));
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
  <div class="facts"><div><span>Gobierna</span><b>${esc(p.gob)}</b></div><div><span>Partido o frente</span><b style="font-size:14px">${esc(p.par)}</b></div><div><span>En el cargo desde</span><b class="mono">${fmes(p.desde)}</b></div><div><span>${p.id==="06"?"Partidos":p.id==="02"?"Comunas":"Departamentos"}</span><b class="mono">${p.ndep}</b></div></div>
  <div class="blk grow"><h2>Ciudades en el mapa · ${cs.length}</h2><ul class="clist">${cs.map(c=>`<li><a href="#c-${c.s}">${esc(c.n)}</a>${tags(c)}<span class="nota">${esc(c.nota)}</span></li>`).join("")||`<li class="muted">Ninguna todavía.</li>`}</ul></div>`;
  const depBlk=`<div class="blk wide"><details ${deps.length<=40?"open":""}><summary><h2 style="display:inline">${deps.length} ${p.id==="06"?"partidos":p.id==="02"?"comunas":"departamentos"}</h2></summary><div class="deps">${deps.map(d=>`<a href="#d-${d.id}">${esc(d.nombre)}</a>`).join("")}</div></details></div>`;
  more(pend("Quién manda de verdad","<b>Paso 2.</b> Poder formal frente a poder real: gobernador, familias, caudillos, intendentes fuertes, empresas y sindicatos que deciden. Alineamiento con Nación y años de permanencia.")+influ()+pend("Actores con sede","<b>Pasos 3 y 5.</b> Con su puntaje de poder en los 21 ejes y su gráfico de relaciones.")+pend("Recursos y coparticipación","<b>Paso 2.</b> Producto bruto, exportaciones y destino (INDEC), recurso dominante y dependencia de los fondos nacionales.")+depBlk);
}
function bx(b,pb){let w=b[1][0]-b[0][0],h=b[1][1]-b[0][1];
  if(pb){const pw=pb[1][0]-pb[0][0],ph=pb[1][1]-pb[0][1],mw=Math.max(w,pw*.35),mh=Math.max(h,ph*.35),cx=(b[0][0]+b[1][0])/2,cy=(b[0][1]+b[1][1])/2;return[cx-mw/2,cy-mh/2,mw,mh]}
  return[b[0][0],b[0][1],w,h]}
function vDep(p,did){
  const d=depInfo[did],cs=T.ciudades.filter(c=>c.dep===did);
  document.getElementById("panel").innerHTML=`<h1>${esc(d.n)}</h1><p class="sub">${esc(d.cat)} de <a href="#prov-${p.s}">${esc(p.n)}</a>.</p>
  <div class="blk grow"><h2>Ciudades en el mapa</h2><ul class="clist">${cs.map(c=>`<li><a href="#c-${c.s}">${esc(c.n)}</a>${tags(c)}<span class="nota">${esc(c.nota)}</span></li>`).join("")||`<li class="muted">Ninguna de las ciudades seleccionadas está en este ${d.cat.toLowerCase()}.</li>`}</ul></div>`;
  more(pend("Datos del "+d.cat.toLowerCase(),"<b>Paso 2.</b> Población (Censo 2022), cabecera, actividad principal, intendente o comisionado y actores con sede.")+influ());
}
async function vCity(c){
  const p=byId[c.prov];ensureMap();document.getElementById("ant").style.display="none";
  await loadDep(p.id);provState(p.id,c.dep);drawCities(T.ciudades.filter(x=>x.prov===p.id),true,c.s);
  const s=Math.max(p.b[1][0]-p.b[0][0],p.b[1][1]-p.b[0][1])*(p.id==="02"?.8:.32);
  zoomTo([c.xy[0]-s/2,c.xy[1]-s/2,s,s]);
  const d=depInfo[c.dep];
  crumbs([["Argentina","inicio"],[p.n,"prov-"+p.s],...(d&&p.id!=="02"&&d.n!==c.n?[[d.n,"d-"+c.dep]]:[]),[c.n]]);
  document.getElementById("panel").innerHTML=`<h1>${esc(c.n)}</h1><p class="sub">${esc(c.nota)}</p>
  <div class="facts"><div><span>Provincia</span><b><a href="#prov-${p.s}">${esc(p.n)}</a></b></div>${d&&p.id!=="02"?`<div><span>${esc(d.cat)}</span><b><a href="#d-${c.dep}">${esc(d.n)}</a></b></div>`:""}<div><span>Coordenadas</span><b class="mono" style="font-size:13px">${c.lat.toFixed(3)}, ${c.lon.toFixed(3)}</b></div></div>
  <div class="blk grow"><h2>Por qué está en el mapa</h2>${tags(c)}</div>`;
  more(pend("Quién gobierna y quién manda","<b>Paso 4.</b> Intendente, concejo y alineamiento; en las ciudades de una empresa, el peso de la empresa frente al municipio.")+influ()+pend("Actores y fricciones","<b>Paso 4.</b> Empresas, sindicatos, organizaciones y conflictos con sede en la ciudad."));
}
function vProvincias(){
  app.innerHTML=`<div class="page"><h1>Provincias</h1><p class="sub">Las 24 jurisdicciones, con quién las gobierna. El alineamiento con Nación y el poder real de cada una se cargan en el paso 2.</p>
  <table class="stack"><thead><tr><th>Provincia</th><th>Capital</th><th>Gobierna</th><th>Partido o frente</th><th>Desde</th><th class="n">Deptos.</th><th class="n">Ciudades</th></tr></thead><tbody>
  ${T.provincias.map(p=>`<tr><td><a href="#prov-${p.s}">${esc(p.n)}</a></td><td>${esc(cityS[p.cap]?.n||"")}</td><td>${esc(p.gob)}</td><td>${esc(p.par)}</td><td class="mono">${fmes(p.desde)}</td><td class="n">${p.ndep}</td><td class="n">${T.ciudades.filter(c=>c.prov===p.id).length}</td></tr>`).join("")}</tbody></table></div>`;
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
  <h2>Hecho en este paso</h2><ul><li>Mapa oficial del IGN: provincias, departamentos (partidos y comunas) y la Antártida en recuadro.</li><li>Zoom de país a provincia, departamento y ciudad, con rutas propias para cada uno.</li><li>${T.ciudades.length} ciudades ubicadas con Georef, cada una con su motivo, filtrables en el mapa.</li><li>Gobernadores al día (Corrientes y Santiago del Estero renovaron en diciembre de 2025).</li></ul>
  <h2>Próximos pasos</h2><ol start="2"><li>Las 24 provincias: población, recursos, coparticipación, alineamiento con Nación, poder real e influencias mundiales.</li><li>Unos 40 actores núcleo nacionales con sus relaciones, medidos en los 21 ejes.</li><li>Fichas de ciudades: intendente, actores, fricciones e influencias.</li><li>Actores provinciales y municipales; puntos de fricción.</li></ol>
  <h2>Para decidir</h2><ul><li>Lista final de potencias para las influencias mundiales.</li><li>Si los departamentos tienen ficha propia o solo el panel.</li><li>Cómo tratar Malvinas, la Antártida y el Atlántico Sur (hoy: Malvinas en el mapa, Antártida en recuadro, Georgias y Sandwich del Sur sin dibujar).</li><li>Ciudades a verificar: ubicación de la estación espacial china (Bajada del Agrio) y umbral de 100.000 habitantes con el Censo 2022.</li></ul></div>`;
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
  document.getElementById("stamp").innerHTML=`Esqueleto · paso 1 de 5<br>Corte ${fd(T.corte)} · próxima ${fd(T.proxima)}`;
  document.getElementById("foot-date").textContent=`Corte del ${fd(T.corte)}; próxima revisión el ${fd(T.proxima)}.`;
  setup();addEventListener("hashchange",route);route();
}).catch(e=>{app.innerHTML=`<p style="padding:40px 0">No se pudo cargar el mapa: ${esc(e.message)}</p>`});
}
