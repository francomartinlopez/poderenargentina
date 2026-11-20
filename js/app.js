// El mapa del poder argentino · aplicación
{
const MOT={cap:["Capital","#F5F0E6"],pob:["Ciudad grande","#9A9A9A"],emp:["Empresa o cluster","#FF3B30"],pue:["Puerto","#2F6BFF"],ene:["Energía","#F2A93B"],min:["Minería","#C8743C"],fro:["Frontera","#3FB8C9"],def:["Defensa y estrategia","#9E8CFF"]};
const ORDEN=["emp","pue","ene","min","fro","def","cap","pob"];
const POT=["EE.UU.","China","Unión Europea","Reino Unido","Brasil","Rusia","Israel","Golfo","Canadá y Australia","Japón y Corea","India","FMI, BM y BID"];
const CK=["com","inv","deu","pre","pol"],CAN=["Comercio","Inversión","Deuda","Presencia","Política"];
const CAPAS=[["terr","Territorio",1],["ali","Alineamiento con Nación",1],["inf","Influencias mundiales",1],["eco","Economía y recursos",1],["act","Actores",1],["fr","Fricción",1],["zl","Zonas liberadas",1]];
const PCOL={"EE.UU.":"#2F6BFF","China":"#D7263D","Unión Europea":"#F2C14E","Reino Unido":"#7FB3D5","Brasil":"#2EB872","Rusia":"#9E1B32","Israel":"#A0C4FF","Golfo":"#C8743C","Canadá y Australia":"#B07CFF","Japón y Corea":"#FF8FAB","India":"#FF9933","FMI, BM y BID":"#BDBDBD"};
const ACOL={A:"#8E6CFF",D:"#9A8F8C",I:"#F2A93B",O:"#3FB8C9"},ALI={A:"Aliado",D:"Dialoguista",I:"Independiente",O:"Opositor"};
const ADESC={A:"acuerdos electorales con La Libertad Avanza",D:"negocia votos y fondos sin acuerdo electoral pleno",I:"espacio propio que compite con LLA (Provincias Unidas)",O:"opositor al Gobierno nacional"};
let capa="terr",potSel="dom",ecoSel="exp";
const TCOL={Estado:"#FF3B30",Persona:"#F5F0E6",Capital:"#F2A93B",Influencia:"#3FB8C9",Información:"#9E8CFF",Sombra:"#8B8B8B"};
const RCOL={Gobierna:"#FF3B30",Propiedad:"#F2A93B",Financiamiento:"#2EB872",Alianza:"#2F6BFF",Enfrentamiento:"#D7263D",Ambigua:"#9A8F8C",Contrato:"#C8743C",Abastecimiento:"#7FB3D5","Puerta giratoria":"#B07CFF"};
let ANTP=null;
const ACT={},actCity={},actProv={},actPres={},FR={},frProv={},frCity={},zlCity={};
const NVC={3:"#FF3B30",2:"#F2A93B",1:"#9A8F8C"},NVT={3:"Violencia o fuerza extranjera",2:"Disputa abierta",1:"Latente o local"};
const nvTag=n=>`<span class="tag" style="color:${NVC[n]}">${NVT[n]}</span>`;
function frList(list){return list.length?`<ul class="flist2">${list.map(f=>`<li><i style="background:${NVC[f.nv]}"></i><a href="#f-${f.id}">${esc(f.n)}</a><span class="muted">${esc(f.tipo)} · ${esc(f.est)}</span></li>`).join("")}</ul>`:`<p class="muted">Ningún punto de fricción cargado aquí.</p>`}
function zlBlk(list,full){return `<ul class="rlist">${list.map(z=>`<li><b>${esc(z.n)}.</b> <span class="tag" style="color:#FF3B30">${esc(z.est)}</span><br>${esc(z.x)} ${z.fu.map(f=>src(f.u)).join(" · ")}${full&&z.cs?` <a href="#c-${z.cs}">Ver ${esc(cityS[z.cs].n)}</a>`:""}</li>`).join("")}</ul>`}
const ZLNOTA="Solo entran las zonas donde un organismo oficial describió la pérdida de control del Estado o documentó pasos o circuitos ilegales operando a la vista, con fuente. Se indica si el Estado recuperó el control.";
const aName=id=>ACT[id]?ACT[id].n:(T.meta.act.externos[id]||id);
const aLink=id=>ACT[id]?`<a href="#a-${id}">${esc(ACT[id].n)}</a>`:(T.meta.act.sin_ficha||[]).includes(id)?esc(aName(id)):`<a href="${esc(T.meta.act.global_url)}#o-${id}" target="_blank" rel="noopener">${esc(aName(id))}</a> <span class="muted" style="font-size:12px">(mapa global)</span>`;
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
const NVI=["","Acotada","De primer orden","Dominante"];
function infGrid(list,abierto){
  const m={},d={};for(const i of list){(m[i.p]=m[i.p]||{})[i.c]=Math.max(m[i.p][i.c]||0,i.n);(d[i.p]=d[i.p]||[]).push(i)}
  const tot=p=>CK.reduce((s,k)=>s+(m[p][k]||0),0);
  const rows=POT.filter(p=>m[p]).sort((a,b)=>tot(b)-tot(a));
  if(!rows.length)return `<p class="muted">Sin influencias relevantes cargadas con fuente.</p>`;
  const mx=tot(rows[0]),top=rows.filter(p=>tot(p)===mx);
  const cel=(p,k)=>{const n=m[p][k]||0;return `<span class="v${n?"":" z"}" title="${CAN[CK.indexOf(k)]}: ${n?NVI[n]+" ("+n+")":"sin dato"}" style="${n?`background:${PCOL[p]}${["","45","8a","dd"][n]}`:""}">${n||"–"}</span>`};
  return `<div class="itab"><div class="ih"><span>Potencia</span><span>Total</span>${CAN.map((c,i)=>`<span title="${T.meta.canales[CK[i]]}">${["Com.","Inv.","Deuda","Pres.","Pol."][i]}</span>`).join("")}</div><div class="ileg">Com. comercio · Inv. inversión · Deuda y finanzas · Pres. presencia física o de seguridad · Pol. influencia política y cultural</div>
  ${rows.map((p,i)=>`<details class="irow"${abierto&&i===0?" open":""}><summary><span class="r"><i style="background:${PCOL[p]}"></i><span class="pn">${esc(p)}</span>${top.length===1&&top[0]===p?`<em title="Potencia dominante">dom.</em>`:top.length>1&&top.includes(p)?`<em>empate</em>`:""}</span><span class="t"><b>${tot(p)}</b><s style="width:${tot(p)/15*100}%;background:${PCOL[p]}"></s></span>${CK.map(k=>cel(p,k)).join("")}</summary>${infList(d[p])}</details>`).join("")}</div>`}
function infList(list){return `<ul class="ilist">${list.sort((a,b)=>CK.indexOf(a.c)-CK.indexOf(b.c)).map(i=>`<li><span class="muted mono" style="font-size:12px">${esc(T.meta.canales[i.c])} · ${NVI[i.n]} (${i.n})</span><br>${esc(i.x)} ${src(i.u)}</li>`).join("")}</ul>`}
function influ(list,title,nota){return `<div class="blk"><h2>${title||"Influencias mundiales"}</h2><p class="muted" style="font-size:13px;margin:0 0 10px">Cada potencia puntúa de 0 a 3 en cinco canales (1 acotada, 2 de primer orden, 3 dominante); el total va de 0 a 15 y manda la de mayor total. Tocá una fila para ver los datos y sus fuentes.</p>${infGrid(list)}<p class="muted" style="font-size:13px;margin:10px 0 0">${nota||"Comercio: participación de cada socio en las exportaciones de la provincia (INDEC). El INDEC solo informa los destinos principales de cada provincia: un socio que no figura entre ellos queda sin puntaje de comercio aunque compre algo. El resto de los canales, dato por dato con su fuente."}</p></div>`}

function setup(){
  const W=600;
  PROJ=d3.geoTransverseMercator().rotate([65,0]).fitWidth(W-24,PF);
  PATH=d3.geoPath(PROJ);
  const b=PATH.bounds(PF);
  FULL=[b[0][0]-12,b[0][1]-12,b[1][0]-b[0][0]+24,b[1][1]-b[0][1]+24];
  for(const f of PF.features){const p=byId[f.properties.id];p.f=f;p.b=PATH.bounds(f)}
  for(const c of T.ciudades){c.xy=PROJ([c.lon,c.lat])}
  for(const f of [...T.friccion,...T.zonas])f.xy=PROJ([f.lon,f.lat]);
}

function mapShell(){
  app.innerHTML=`<div class="mapview"><div><div class="crumbs" id="crumbs"></div>
  <div class="selrow"><label for="capasel">Ver en el mapa</label><select id="capasel" class="sel"></select><span id="subsel"></span></div><div class="bar sub" id="sub"></div>
  <div class="mapbox" id="mapbox"><svg id="map" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Mapa de la Argentina por provincias"></svg>
  <div class="ant" id="ant"><svg id="antsvg" aria-label="Antártida"></svg><span id="antlb">Antártida Argentina<br>(otra escala)</span></div></div>
  <div class="bar" id="filt" role="group" aria-label="Ciudades por motivo" style="margin-top:10px"></div></div>
  <aside class="panel"><div class="pin" id="panel"></div></aside></div><section class="more" id="more"></section>`;
  svg=document.getElementById("map");
  svg.setAttribute("viewBox",FULL.join(" "));cur=FULL.slice();
  svg.innerHTML=`<g id="gp">${PF.features.map(f=>`<path class="prov" data-k="p:${f.properties.id}" d="${PATH(f)}"><title>${esc(byId[f.properties.id].n)}</title></path>`).join("")}</g><g id="gd"></g><g id="gc"></g><g id="gl"></g><g id="gf"></g>`;
  G={p:svg.querySelector("#gp"),d:svg.querySelector("#gd"),c:svg.querySelector("#gc"),l:svg.querySelector("#gl"),f:svg.querySelector("#gf")};
  for(const pid in DEP)depGroup(pid);
  if(ANT){const as=document.getElementById("antsvg");ANTP=d3.geoAzimuthalEqualArea().rotate([50,90]).fitExtent([[4,4],[104,92]],ANT);as.setAttribute("viewBox","0 0 108 96");
    as.addEventListener("click",e=>{const t=e.target.closest("[data-k]");if(t)location.hash="f-"+t.dataset.k.split(":")[1]})}
  svg.addEventListener("click",e=>{const t=e.target.closest("[data-k]");if(!t)return;const[k,v]=t.dataset.k.split(":");
    if(k==="p"){location.hash="prov-"+byId[v].s}else if(k==="d"){location.hash="d-"+v}else if(k==="c"){location.hash="c-"+v}else if(k==="f"){location.hash="f-"+v}else if(k==="z"){location.hash="c-"+v}});
  svg.addEventListener("pointermove",e=>{const t=e.target.closest("[data-k]");if(!t||e.pointerType!=="mouse"){tip.style.display="none";return}
    const[k,v]=t.dataset.k.split(":");const txt=k==="p"?tipText(byId[v]):k==="d"?(depInfo[v]?.n||v):k==="f"?FR[v].n:k==="z"?T.zonas.find(z=>z.cs===v).n:capa==="act"&&actCity[v]?`${cityS[v].n}: ${actCity[v].length} actores`:cityS[v]?.n;tip.textContent=txt;tip.style.display="block";tip.style.left=e.clientX+14+"px";tip.style.top=e.clientY+12+"px"});
  svg.addEventListener("pointerleave",()=>tip.style.display="none");
  new ResizeObserver(()=>scaleMarks()).observe(svg);
  document.getElementById("capasel").onchange=e=>{capa=e.target.value;route()};
  document.getElementById("subsel").onchange=e=>{const t=e.target;if(t.dataset.k==="pot")potSel=t.value;if(t.dataset.k==="eco")ecoSel=t.value;route()};
}
function tipText(p){
  if(capa==="ali")return `${p.n}: ${ALI[p.ali.ali]}`;
  if(capa==="inf")return potSel==="dom"?`${p.n}: ${p.dom||(p.emp.length?"empate entre "+p.emp.join(", "):"sin datos")}`:`${p.n}: ${potSel} ${p.tot[potSel]||0} puntos`;
  if(capa==="act")return `${p.n}: ${(actProv[p.id]||[]).length} actores núcleo con sede`;
  if(capa==="fr")return `${p.n}: ${(frProv[p.id]||[]).length} puntos de fricción`;
  if(capa==="zl")return `${p.n}: ${T.zonas.filter(z=>z.prov===p.id).length} zonas liberadas documentadas`;
  if(capa==="eco")return ecoSel==="exp"?`${p.n}: USD ${nf(p.eco.exp)} M exportados`:`${p.n}: ${p.eco.propios==null?"sin datos":p.eco.propios.toLocaleString("es-AR")+"% de recursos propios"}`;
  return p.n}
function paint(){
  document.getElementById("capasel").innerHTML=CAPAS.filter(c=>c[2]).map(([k,n])=>`<option value="${k}"${capa===k?" selected":""}>${n}</option>`).join("");
  const ss=document.getElementById("subsel");
  ss.innerHTML=capa==="inf"?`<select class="sel" data-k="pot" aria-label="Potencia"><option value="dom"${potSel==="dom"?" selected":""}>Potencia dominante</option>${POT.map(k=>`<option value="${esc(k)}"${potSel===k?" selected":""}>${esc(k)}</option>`).join("")}</select>`
    :capa==="eco"?`<select class="sel" data-k="eco" aria-label="Indicador"><option value="exp"${ecoSel==="exp"?" selected":""}>Exportaciones</option><option value="pro"${ecoSel==="pro"?" selected":""}>Recursos propios</option></select>`:"";
  const P=T.provincias,sub=document.getElementById("sub");let leg="";
  const maxPot=k=>Math.max(1,...P.map(p=>p.tot[k]||0)),maxExp=Math.max(...P.map(p=>p.eco.exp));
  const fill=p=>{
    if(capa==="ali")return[ACOL[p.ali.ali],.6];
    if(capa==="inf"){if(potSel==="dom")return p.dom?[PCOL[p.dom],.62]:p.emp.length?["#6E6462",.55]:null;const v=p.tot[potSel]||0;return v?[PCOL[potSel],.18+.7*v/maxPot(potSel)]:null}
    if(capa==="fr"){const l=frProv[p.id];return l?[NVC[Math.max(...l.map(f=>f.nv))],.32]:null}
    if(capa==="zl")return T.zonas.some(z=>z.prov===p.id)?["#FF3B30",.3]:null;
    if(capa==="act"){const n=(actProv[p.id]||[]).length;return n?["#FF3B30",.12+.5*Math.min(1,n/6)]:null}
    if(capa==="eco"){if(ecoSel==="exp")return["#FF3B30",.1+.8*Math.log10(p.eco.exp)/Math.log10(maxExp)];return p.eco.propios==null?null:["#FF3B30",.1+.8*p.eco.propios/90]}
    return null};
  for(const el of G.p.children){const p=byId[el.dataset.k.slice(2)],f=fill(p);el.style.fill=f?f[0]:"";el.style.fillOpacity=f?f[1]:"";el.querySelector("title").textContent=tipText(p)}
  if(capa==="ali"){const c={};P.forEach(p=>c[p.ali.ali]=(c[p.ali.ali]||0)+1);leg=Object.keys(ALI).map(a=>`<span class="lg"><i style="background:${ACOL[a]}"></i>${ALI[a]} ${c[a]||0}</span>`).join("")}
  else if(capa==="inf"){leg=potSel==="dom"?POT.filter(k=>P.some(p=>p.dom===k)).map(k=>`<span class="lg"><i style="background:${PCOL[k]}"></i>${esc(k)} ${P.filter(p=>p.dom===k).length}</span>`).join("")+(P.some(p=>!p.dom&&p.emp.length)?`<span class="lg"><i style="background:#6E6462"></i>Empate ${P.filter(p=>!p.dom&&p.emp.length).length}</span>`:""):`<span class="lg"><i style="background:${PCOL[potSel]}"></i>Más intenso, más influencia de ${esc(potSel)} (total de 0 a 15)</span>`}
  else if(capa==="act"){leg=`<span class="lg">Círculos: ciudades sede de actores núcleo, según la suma de sus puntajes. La mayoría tiene sede en la Capital.</span>`}
  else if(capa==="fr"){leg=[3,2,1].map(n=>`<span class="lg"><i style="background:${NVC[n]}"></i>${NVT[n]}</span>`).join("")}
  else if(capa==="zl"){leg=`<span class="lg">Zonas documentadas con fuente oficial o periodística. Ver criterio en el panel.</span>`}
  else if(capa==="eco"){leg=`<span class="lg">${ecoSel==="exp"?"USD exportados, "+esc(T.meta.periodo_exp)+" (escala logarítmica)":"Ingresos propios sobre el total, 2025 (ASAP)"}</span>`}
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
  if(G.f)for(const c of G.f.children){if(c.tagName==="circle")c.setAttribute("r",(+c.dataset.m)*px);else{const q=(+c.dataset.m)*px,x=+c.dataset.x,y=+c.dataset.y;c.setAttribute("points",`${x},${y-q} ${x+q},${y} ${x},${y+q} ${x-q},${y}`)}}
  const placed=[];
  for(const l of G.l.children){const fs=12*px,x=+l.getAttribute("x")+7*px,y=+l.getAttribute("y")+4*px,w=l.textContent.length*fs*.56,bb=[x-2*px,y-fs,x+w,y+3*px];
    l.setAttribute("font-size",fs);l.setAttribute("stroke-width",3*px);l.setAttribute("dx",7*px);l.setAttribute("dy",4*px);
    const hit=!l.classList.contains("keep")&&placed.some(o=>bb[0]<o[2]&&bb[2]>o[0]&&bb[1]<o[3]&&bb[3]>o[1]);
    l.style.display=hit?"none":"";if(!hit)placed.push(bb)}
}
// Reclamos antárticos superpuestos (meridianos oeste): Argentina 25°-74°, Reino Unido 20°-80°, Chile 53°-90°.
const CLAIMS=[["Reino Unido",20,80,"#7FB3D5"],["Chile",53,90,"#E0B341"],["Argentina",25,74,"#FF3B30"]];
function wedge(pr,a,b,lat){const c=pr([0,-90]),pts=[];for(let l=a;l<=b;l+=1)pts.push(pr([-l,lat]));return `M${c[0].toFixed(1)},${c[1].toFixed(1)}`+pts.map(q=>`L${q[0].toFixed(1)},${q[1].toFixed(1)}`).join("")+"Z"}
function antDraw(){const as=document.getElementById("antsvg");if(!as||!ANTP)return;
  const base=`<path d="${d3.geoPath(ANTP)(ANT)}" fill="#161414" stroke="#4A3A38"/>`,fa=T.friccion.filter(f=>f.lat<-58);
  as.innerHTML=base+(capa==="fr"?CLAIMS.map(([n,a,b,c])=>`<path d="${wedge(ANTP,a,b,-62)}" fill="${c}" fill-opacity=".14" stroke="${c}" stroke-width=".8" stroke-dasharray="2 1.5"><title>${n}: ${a}° a ${b}° O</title></path>`).join("")+fa.map(f=>{const[x,y]=ANTP([f.lon,f.lat]);return `<polygon class="frm" data-k="f:${f.id}" points="${x},${y-6} ${x+6},${y} ${x},${y+6} ${x-6},${y}" fill="${NVC[f.nv]}" style="cursor:pointer"><title>${esc(f.n)}</title></polygon>`}).join(""):"");
  const lb=document.getElementById("antlb");if(lb)lb.innerHTML=capa==="fr"?`Antártida: reclamos de <b style="color:#FF3B30">Argentina</b>, <b style="color:#E0B341">Chile</b> y <b style="color:#7FB3D5">Reino Unido</b>`:"Antártida Argentina<br>(otra escala)"}
function claimSvg(){if(!ANT)return "";const w=420,h=380,pr=d3.geoAzimuthalEqualArea().rotate([50,90]).fitExtent([[10,10],[w-10,h-10]],ANT);
  return `<figure class="claims"><svg viewBox="0 0 ${w} ${h}" role="img" aria-label="Sectores antárticos reclamados por la Argentina, Chile y el Reino Unido"><path d="${d3.geoPath(pr)(ANT)}" fill="#161414" stroke="#4A3A38"/>${CLAIMS.map(([n,a,b,c])=>`<path d="${wedge(pr,a,b,-62)}" fill="${c}" fill-opacity=".16" stroke="${c}" stroke-width="1.4" stroke-dasharray="6 4"></path>`).join("")}</svg>
  <figcaption>${CLAIMS.slice().reverse().map(([n,a,b,c])=>`<span class="lg"><i style="background:${c}"></i>${n}: ${a}° a ${b}° O</span>`).join("")}<br><span class="muted">Sectores aproximados, del polo al paralelo 62° S. Los tres reclamos se superponen en la península antártica; el Tratado Antártico los congela.</span></figcaption></figure>`}
function drawCities(list,labels,sel){
  const vis=capa==="act"?list.filter(c=>actCity[c.s]||c.s===sel):list.filter(c=>c.mot.some(m=>filt.has(m))||c.s===sel);
  vis.sort((a,b)=>(a.mot.includes("cap")-b.mot.includes("cap")));
  G.c.innerHTML=vis.map(c=>`<circle class="city ${c.mot.includes("cap")?"cap":""} ${c.s===sel?"sel":""}" cx="${c.xy[0]}" cy="${c.xy[1]}" r="3" fill="${color(c)}" data-k="c:${c.s}" ${capa==="act"&&actCity[c.s]?`data-m="${(1+Math.log1p(actCity[c.s].reduce((t,a)=>t+a.pt,0))/2.6).toFixed(2)}" style="fill:#FF3B30;fill-opacity:.75"`:""}></circle>`).join("");
  const pr=c=>c.s===sel?0:c.mot.includes("cap")?1:c.mot.includes("pob")?2:3;
  G.l.innerHTML=labels?vis.slice().sort((a,b)=>pr(a)-pr(b)).map(c=>`<text class="clbl ${c.mot.includes("cap")?"cap":""} ${c.s===sel?"keep":""}" x="${c.xy[0]}" y="${c.xy[1]}">${esc(c.n)}</text>`).join(""):"";
  G.f.innerHTML=capa==="fr"?T.friccion.filter(f=>f.lat>-58).sort((a,b)=>a.nv-b.nv).map(f=>`<polygon class="frm" data-k="f:${f.id}" data-x="${f.xy[0]}" data-y="${f.xy[1]}" data-m="${5+2.2*f.nv}" fill="${NVC[f.nv]}"></polygon>`).join(""):capa==="zl"?T.zonas.map(z=>`<circle class="zlm" data-k="z:${z.cs}" cx="${z.xy[0]}" cy="${z.xy[1]}" data-m="16"></circle>`).join(""):"";
  scaleMarks();antDraw();
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
  else if(capa==="fr")side=`<h2>Puntos de fricción · ${T.friccion.length}</h2>${frList(T.friccion.slice().sort((a,b)=>b.nv-a.nv))}<p class="muted" style="font-size:13px;margin:8px 0 0">Lugares donde actores del mapa, o una potencia y el Estado, disputan un recurso, un territorio o una regla. <a href="#friccion">Ver todos con su cronología</a>.</p>`;
  else if(capa==="zl")side=`<h2>Zonas liberadas · ${T.zonas.length}</h2>${zlBlk(T.zonas,1)}<p class="muted" style="font-size:13px;margin:8px 0 0">${ZLNOTA}</p>`;
  else if(capa==="act")side=`<h2>Los más poderosos</h2>${actList(T.actores,12)}<p class="muted" style="font-size:13px;margin:8px 0 0">Puntaje de 0 a 100, con el mismo método que el mapa global. <a href="#actores">Ver los ${T.actores.length} actores y sus relaciones</a>.</p>`;
  else side=`<h2>Por qué está cada ciudad</h2><div class="mbars">${Object.keys(MOT).map(m=>`<div><span>${MOT[m][0]}</span><em style="width:${cnt[m]/mx*100}%;background:${MOT[m][1]}"></em><span>${cnt[m]||0}</span></div>`).join("")}</div>
  <p class="muted" style="font-size:13px;margin:8px 0 0">Una ciudad puede tener varios motivos. Las de empresa o cluster entran aunque sean chicas.</p>`;
  document.getElementById("panel").innerHTML=`<h1>Argentina</h1><p class="sub">Tocá una provincia para bajar a sus departamentos y ciudades. Cambiá la capa para ver alineamiento, influencias o economía.</p>
  <div class="facts"><div><span>Población (Censo 2022)</span><b class="mono">${nf(T.pais.pob)}</b></div><div><span>Departamentos</span><b class="mono">${P.reduce((s,p)=>s+p.ndep,0)}</b></div><div><span>Ciudades en el mapa</span><b class="mono">${T.ciudades.length}</b></div></div>
  ${T.pais.rigi?`<p class="muted" style="font-size:13px;margin:6px 0 0">RIGI: ${T.pais.rigi.proyectos} proyectos aprobados por USD ${nf(T.pais.rigi.monto)} millones en compromisos (petróleo y gas ${nf(T.pais.rigi.petroleo_gas)}, minería ${nf(T.pais.rigi.mineria)}), ${esc(T.pais.rigi.fecha)}. <a href="${esc(T.pais.rigi.fuente)}" target="_blank" rel="noopener">Fuente</a></p>`:""}
  <div class="blk grow">${side}</div>`;
  more(influ(T.pais.inf,"Influencias sobre el Estado nacional","Vínculos de la Nación con cada potencia. Comercio: participación de cada socio en las exportaciones y en las importaciones de bienes del país (INDEC, vía Cancillería); vale el mayor de los dos, por eso China, primer origen de las importaciones, puntúa 2. Las influencias de cada provincia, en su ficha.")+`<div class="blk"><h2>Quién manda</h2>${actList(T.actores,8)}<p style="margin-top:10px"><a href="#actores">Los ${T.actores.length} actores núcleo, su puntaje y sus relaciones</a></p></div>`);
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
  const eco=`<div class="blk"><h2>Economía y recursos</h2><dl class="dl"><dt>Exportaciones</dt><dd><b class="mono">USD ${nf(e.exp)} M</b> en el ${esc(T.meta.periodo_exp)}</dd><dt>Rubro principal</dt><dd>${esc(e.rubro)}</dd><dt>Destinos</dt><dd>${esc(e.destx)}</dd>${p.rigi?`<dt>RIGI</dt><dd><b class="mono">USD ${nf(p.rigi)} M</b> en compromisos de proyectos aprobados (${esc(T.pais.rigi.prov_fecha)}) ${src(T.pais.rigi.prov_u)}</dd>`:""}<dt>Recursos propios</dt><dd>${e.propios==null?"Sin datos actualizados":`<b class="mono">${e.propios.toLocaleString("es-AR")}%</b> de los ingresos; el resto llega de la Nación`}</dd><dt>Fuentes</dt><dd>${src(T.meta.fuente_exp)} · ${src(T.meta.fuente_propios)} · ${src(T.meta.fuente_censo)}</dd></dl></div>`;
  more(manda+influ(p.inf)+eco+`<div class="blk"><h2>Actores núcleo con sede</h2>${actList(actProv[p.id]||[])}${(actPres[p.id]||[]).length?`<h2 style="margin-top:14px">Con presencia en la provincia</h2><ul class="alist">${actPres[p.id].slice().sort((x,y)=>y[0].pt-x[0].pt).map(([a,q])=>`<li><a href="#a-${a.id}">${esc(a.n)}</a><span class="muted">${q.f?`<a href="#f-${q.f}">${esc(q.x)}</a>`:esc(q.x)}${q.u?" "+src(q.u):""}</span>${ptBar(a.pt,TCOL[a.tipo],.56)}</li>`).join("")}</ul>`:""}</div>`+`<div class="blk"><h2>Puntos de fricción</h2>${frList(frProv[p.id]||[])}${T.zonas.some(z=>z.prov===p.id)?`<h2 style="margin-top:14px">Zonas liberadas</h2>${zlBlk(T.zonas.filter(z=>z.prov===p.id),1)}`:""}</div>`+depBlk);
}
function bx(b,pb){let w=b[1][0]-b[0][0],h=b[1][1]-b[0][1];
  if(pb){const pw=pb[1][0]-pb[0][0],ph=pb[1][1]-pb[0][1],mw=Math.max(w,pw*.35),mh=Math.max(h,ph*.35),cx=(b[0][0]+b[1][0])/2,cy=(b[0][1]+b[1][1])/2;return[cx-mw/2,cy-mh/2,mw,mh]}
  return[b[0][0],b[0][1],w,h]}
function vDep(p,did){
  const d=depInfo[did],cs=T.ciudades.filter(c=>c.dep===did);
  document.getElementById("panel").innerHTML=`<h1>${esc(d.n)}</h1><p class="sub">${esc(d.cat)} de <a href="#prov-${p.s}">${esc(p.n)}</a>.</p>
  <div class="facts"><div><span>Población (Censo 2022)</span><b class="mono">${T.deppob[did]?nf(T.deppob[did]):"—"}</b></div><div><span>Peso en la provincia</span><b class="mono">${T.deppob[did]?(T.deppob[did]/p.pob*100).toLocaleString("es-AR",{maximumFractionDigits:1})+"%":"—"}</b></div></div>
  <div class="blk grow"><h2>Ciudades en el mapa</h2><ul class="clist">${cs.map(c=>`<li><a href="#c-${c.s}">${esc(c.n)}</a>${tags(c)}<span class="nota">${esc(c.nota)}</span></li>`).join("")||`<li class="muted">Ninguna de las ciudades seleccionadas está en este ${d.cat.toLowerCase()}.</li>`}</ul></div>`;
  const F=(T.deps||{})[did],dc=d.cat.toLowerCase();
  const ficha=F?`${F.cab?`<div class="blk"><h2>Quién gobierna y qué pesa</h2><dl class="dl"><dt>Cabecera</dt><dd>${esc(F.cab)}</dd>${F.gob?`<dt>${p.id==="06"?"Intendente":"Gobierno local"}</dt><dd><b>${esc(F.gob.n)}</b> <span class="muted">· ${esc(F.gob.par)}</span>${F.gob.nota?`<br><span class="muted" style="font-size:13px">${esc(F.gob.nota)}</span>`:""} ${src(F.gob.u)}</dd>`:`<dt>Gobierno local</dt><dd class="muted">Varios municipios y comunas, sin un gobierno único del ${esc(dc)}.</dd>`}</dl><p class="lead" style="margin-top:12px">${esc(F.act)}</p>${F.fu.length?`<p class="src">Fuentes: ${F.fu.map(f=>`<a href="${esc(f.u)}" target="_blank" rel="noopener">${esc(f.t)}</a>`).join(" · ")}</p>`:""}</div>`:""}
  <div class="blk"><h2>Actores con sede o peso aquí</h2>${actList(F.ai.map(i=>ACT[i]).filter(Boolean))}</div>${F.fr.length?`<div class="blk"><h2>Fricción</h2>${frList(F.fr.map(i=>FR[i]).filter(Boolean))}</div>`:""}`
   :pend("Datos del "+dc,"Panel corto. Ficha propia solo para los "+(p.id==="06"?"partidos":"departamentos")+" relevantes (conurbano, Rosario, San Lorenzo, Vaca Muerta).");
  more(ficha+`<div class="blk"><h2>Influencias mundiales</h2><p>Se miden por provincia: <a href="#prov-${p.s}">ver ${esc(p.n)}</a>${p.dom?`, donde domina <b style="color:${PCOL[p.dom]}">${esc(p.dom)}</b>`:""}.</p></div>`);
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
  const fz=(frCity[c.s]||[]),zz=T.zonas.filter(z=>z.cs===c.s);
  const frc=fz.length||zz.length?`<div class="blk"><h2>Fricción y zonas liberadas</h2>${fz.length?frList(fz):""}${zz.length?zlBlk(zz):""}</div>`:"";
  const conf=c.conf?`<div class="blk"><h2>Conflictos</h2><ul class="rlist">${c.conf.map(f=>`<li><b>${esc(f.t)}.</b> ${esc(f.x)} ${src(f.u)}</li>`).join("")}</ul></div>`:"";
  more(gob+(c.inf?influ(c.inf,"Influencias mundiales","Por las empresas y proyectos con sede en la ciudad, de 0 a 3 por canal. Las de la provincia, en su ficha."):`<div class="blk"><h2>Influencias mundiales</h2><p>Sin influencias propias cargadas: rigen las de la provincia, <a href="#prov-${p.s}">${esc(p.n)}</a>${p.dom?`, donde domina <b style="color:${PCOL[p.dom]}">${esc(p.dom)}</b>`:""}.</p></div>`)+conf+frc+`<div class="blk"><h2>Actores núcleo con sede</h2>${actList(actCity[c.s]||[])}</div>`);
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
  <h2>Hecho</h2><ol><li><b>Esqueleto.</b> Mapa oficial del IGN con zoom de país a provincia, departamento y ciudad; ${T.ciudades.length} ciudades con su motivo; gobernadores al día.</li><li><b>Las 24 provincias.</b> Población del Censo 2022 por provincia y departamento; exportaciones, destinos y rubro principal (INDEC); recursos propios frente a los fondos nacionales (ASAP); quién manda de verdad y alineamiento con la Nación; influencias de 12 potencias en cinco canales, con fuente. Capas de alineamiento, influencias y economía en el mapa.</li><li><b>Actores núcleo.</b> ${T.actores.length} actores nacionales medidos en los 21 ejes con la fórmula del mapa global, con ficha, fuentes y ${T.relaciones.length} relaciones; capa de actores en el mapa.</li><li><b>Fichas de ciudades.</b> Intendente de ${T.ciudades.filter(c=>c.int).length} ciudades, quién manda en las ciudades de empresa, influencias propias de ${T.ciudades.filter(c=>c.inf).length} ciudades y conflictos documentados.</li><li><b>Fricción y actores locales.</b> Los gobiernos de las 24 jurisdicciones como actores, con su alineamiento; Zamora en Santiago del Estero, los intendentes de Rosario y Córdoba, sindicatos regionales, empresas provinciales y, por categoría, dirigentes políticos, empresas y grupos económicos, bandas criminales con condena, Justicia, religiosos, organizaciones sociales y ONG, medios y periodistas; ${T.actores.length} actores en total. ${T.friccion.length} puntos de fricción con cronología y fuentes, y las zonas liberadas documentadas, con capas propias en el mapa.</li><li><b>Departamentos relevantes.</b> Ficha propia de ${Object.keys(T.deps||{}).length} partidos y departamentos (conurbano, Rosario, San Lorenzo y Vaca Muerta): cabecera, quién gobierna, actividad, actores y fricción.</li></ol>
  
  <h2>Método de las influencias</h2><p>Cada potencia recibe de 0 a 3 en cinco canales. El comercio se calcula con la participación de cada destino en las exportaciones de la provincia (40% o más vale 3; de 20% a 40%, 2; de 8% a 20%, 1); cuando el INDEC informa un bloque se toma como aproximación (USMCA como EE.UU. y Mercosur como Brasil). Inversión, deuda, presencia e influencia política se cargan dato por dato con su fuente. La potencia dominante es la de mayor suma; si dos empatan, se marca el empate.</p>
  <h2>Pendientes</h2><ul><li>Confirmar con fuente del año los ${T.ciudades.filter(c=>c.int&&c.int.ver==="W").length} intendentes marcados «a confirmar» y cargar los de Timbúes y San Antonio de los Cobres.</li><li>Censo 2022 de las localidades que todavía muestran una proyección propia a 2026 (San Antonio de los Cobres, Antofagasta de la Sierra, San José de Jáchal y Salvador Mazza).</li><li>Más intendentes del conurbano como actores puntuados (hoy, siete) y la nueva conducción de Independiente tras las elecciones del 13 de diciembre de 2026.</li><li>Próximo corte: 23 de febrero de 2027.</li></ul></div>`;
}
function vElecciones(){
  const E=T.elecciones,fd=d=>{const[y,m,x]=d.split("-");return +x+" de "+MES[+m-1]+" de "+y};
  const L=T.provincias.slice().map(p=>({p,e:E.prov[p.id]})).sort((a,b)=>((a.e&&a.e.f)||"9")<((b.e&&b.e.f)||"9")?-1:((a.e&&a.e.f)||"9")>((b.e&&b.e.f)||"9")?1:a.p.n.localeCompare(b.p.n));
  const D={S:"Desdobla",N:"Con la Nación"};
  app.innerHTML=`<div class="page"><h1>Elecciones 2027</h1><p class="sub">La elección presidencial es el ${fd(E.pres.f)} (<a href="${esc(E.pres.u)}" target="_blank" rel="noopener">fuente</a>). Las provincias que separan su elección de la nacional evitan el arrastre de la boleta presidencial. ${Object.values(E.prov).filter(e=>e.d==="S").length} anunciaron que desdoblan y ${Object.values(E.prov).filter(e=>e.f).length} ya tienen fecha.</p>
  <table class="stack"><thead><tr><th>Provincia</th><th>Fecha provincial</th><th>Calendario</th><th>Gobierna</th><th>Alineamiento</th><th>Nota</th></tr></thead><tbody>
  ${L.map(({p,e})=>`<tr><td><a href="#prov-${p.s}">${esc(p.n)}</a></td><td class="mono">${e&&e.f?fd(e.f):"<span class=muted>sin fijar</span>"}</td><td>${e&&e.d?D[e.d]:"<span class=muted>sin definir</span>"}</td><td>${esc(p.gob)} <span class="muted">(${esc(p.par)})</span></td><td>${esc(T.meta.alineamiento[p.ali.ali]||"")}</td><td>${e?esc(e.x)+` <a href="${esc(e.u)}" target="_blank" rel="noopener">Fuente</a>`:""}</td></tr>`).join("")}
  </tbody></table>
  <p class="muted" style="font-size:13px">Se actualiza en cada corte y después de cada convocatoria. Solo fechas confirmadas por la provincia o publicadas con fuente.</p></div>`;
}
function vFriccion(){
  const L=T.friccion.slice().sort((a,b)=>b.nv-a.nv);
  app.innerHTML=`<div class="page"><h1>Fricción</h1><p class="sub">Dónde se disputa el poder en el territorio: ${L.length} puntos donde actores del mapa, o una potencia y el Estado argentino, chocan por un recurso, un territorio o una regla. Cada uno con su cronología y sus fuentes.</p>
  <div class="bar">${[3,2,1].map(n=>`<span class="lg"><i style="background:${NVC[n]}"></i>${NVT[n]} <span class="mono muted">${L.filter(f=>f.nv===n).length}</span></span>`).join("")}</div>
  <table class="stack"><thead><tr><th>Punto</th><th>Tipo</th><th>Provincia</th><th>Intensidad</th><th>Estado</th><th>Potencias</th></tr></thead><tbody>
  ${L.map(f=>`<tr><td><a href="#f-${f.id}">${esc(f.n)}</a></td><td>${esc(f.tipo)}</td><td><a href="#prov-${byId[f.prov].s}">${esc(byId[f.prov].c)}</a></td><td>${nvTag(f.nv)}</td><td>${esc(f.est)}</td><td>${f.pot.map(q=>`<b style="color:${PCOL[q]};font-weight:500">${esc(q)}</b>`).join(", ")||`<span class="muted">—</span>`}</td></tr>`).join("")}</tbody></table>
  <h2 class="sec">Zonas liberadas</h2>${zlBlk(T.zonas,1)}<p class="muted" style="font-size:13px">${ZLNOTA}</p>
  <h2 class="sec">Criterio</h2><p>Intensidad 3: hay violencia, enfrentamientos con fuerzas de seguridad o presencia militar extranjera. 2: disputa abierta, judicial, diplomática, licitatoria o política. 1: disputa latente o localizada. Para vincular a alguien con delitos se exige fuente; en personas vivas, solo lo establecido por un tribunal u organismo oficial.</p></div>`;
}
function vFr(f){
  const p=byId[f.prov];
  app.innerHTML=`<div class="page actor"><p class="crumbs"><a href="#friccion">Fricción</a> › <b>${esc(f.n)}</b></p><h1>${esc(f.n)}</h1><p class="sub">${esc(f.x)}</p>
  <div class="facts"><div><span>Tipo</span><b>${esc(f.tipo)}</b></div><div><span>Intensidad</span><b>${nvTag(f.nv)}</b></div><div><span>Estado</span><b style="font-size:14px">${esc(f.est)}</b></div><div><span>Dónde</span><b style="font-size:14px">${f.cs?`<a href="#c-${f.cs}">${esc(cityS[f.cs].n)}</a>, `:""}<a href="#prov-${p.s}">${esc(p.n)}</a></b></div></div>
  ${f.id==="antartida"?claimSvg():""}
  <div class="cols"><div><h2 class="sec">Actores</h2><ul class="rlist">${f.act.map(a=>`<li>${aLink(a)}</li>`).join("")}${f.pot.map(q=>`<li><b style="color:${PCOL[q]}">${esc(q)}</b> <span class="muted">(potencia)</span></li>`).join("")}</ul></div>
  <div><h2 class="sec">Cronología</h2><ul class="rlist">${f.hit.map(h=>`<li><span class="mono muted">${esc(h.f.length>4?fmes(h.f):h.f)}</span> ${esc(h.x)} ${src(h.u)}</li>`).join("")}</ul>
  <h2 class="sec">Fuentes</h2><ul class="rlist">${f.fu.map(x=>`<li><a href="${esc(x.u)}" target="_blank" rel="noopener">${esc(x.t)}</a></li>`).join("")}</ul></div></div></div>`;
}
let atSel=null,acSel="",aq="";
function aRows(){const A=T.actores,q=aq.normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase();return A.map((a,i)=>[a,i]).filter(([a])=>(!atSel||a.tipo===atSel)&&(!acSel||a.cat===acSel)&&(!q||(a.n+" "+a.cat+" "+a.sede).normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase().includes(q))).map(([a,i])=>`<tr><td class="n mono">${i+1}</td><td><a href="#a-${a.id}">${esc(a.n)}</a></td><td style="color:${TCOL[a.tipo]}">${esc(a.cat)}</td><td><a href="#${a.sd?"d-"+a.sd:"c-"+a.cs}">${esc(a.sede==="Ciudad Autónoma de Buenos Aires"?"CABA":a.sede)}</a></td><td>${esc(T.meta.act.alcance[a.alc])}</td><td>${ptBar(a.pt,TCOL[a.tipo])}</td><td class="n mono">${a.oculto.toLocaleString("es-AR")}</td></tr>`).join("")||`<tr><td colspan="7" class="muted">Sin resultados.</td></tr>`}
function vActores(){
  const A=T.actores,tipos=[...new Set(A.map(a=>a.tipo))];
  app.innerHTML=`<div class="page"><h1>Actores</h1><p class="sub">Quién tiene el poder real en la Argentina: ${A.length} actores núcleo, nacionales, provinciales y municipales, medidos en 21 ejes, con el mismo método y la misma fórmula que El mapa del poder global. En este mapa, el 3 de cada eje es dominio a escala nacional.</p>
  <div class="bar" id="tf"><button class="chip ${atSel?"":"on"}" data-t="">Todos</button>${tipos.map(t=>`<button class="chip ${atSel===t?"on":""}" data-t="${t}"><i style="background:${TCOL[t]}"></i>${t} <small>${A.filter(a=>a.tipo===t).length}</small></button>`).join("")}</div>
  <div class="selrow"><label for="acsel">Categoría</label><select id="acsel" class="sel"><option value="">Todas</option>${[...new Set(A.map(a=>a.cat))].sort().map(c=>`<option${acSel===c?" selected":""}>${esc(c)}</option>`).join("")}</select><input class="search" id="aq" type="search" placeholder="Buscar actor" value="${esc(aq)}" aria-label="Buscar actor" style="flex:1;min-width:180px;margin:0"></div>
  <table class="stack"><thead><tr><th class="n">#</th><th>Actor</th><th>Categoría</th><th>Sede</th><th>Alcance</th><th>Puntaje de poder</th><th class="n" title="Poder real que no surge del cargo formal">Oculto</th></tr></thead><tbody id="atb">${aRows()}</tbody></table>
  <h2 class="sec">Red de relaciones</h2><p class="muted" style="font-size:14px;max-width:760px">${T.relaciones.length} relaciones con fuente. Pasá el cursor por un actor para ver sus vínculos; tocalo para abrir su ficha. Los nodos grises son actores del mapa global.</p>
  <div class="bar">${Object.keys(RCOL).filter(t=>T.relaciones.some(r=>r.t===t)).map(t=>`<span class="lg"><i style="background:${RCOL[t]}"></i>${t}</span>`).join("")}</div>
  ${netSvg()}
  <h2 class="sec">Método</h2><p style="max-width:760px">Cada actor recibe de 0 a 3 en 21 ejes (materia, dinero, fuerza, información, personas y norma). Coerción, adquisición de información y acción fuera de la ley valen el doble; contactos y privilegio legal, una vez y media. El puntaje final es una media geométrica ponderada de la categoría teórica del actor (40 %), su capacidad (30 %), su alcance (20 %), su autonomía real (5 %) y el poder que hereda de quienes dependen de él (5 %); el resultado se eleva al cubo y el mayor vale 100. El poder oculto mide cuánto de ese poder no surge del cargo formal. La acción fuera de la ley solo se puntúa con un hecho establecido por un tribunal u organismo oficial.</p></div>`;
  document.getElementById("tf").onclick=e=>{const b=e.target.closest("button");if(!b)return;atSel=b.dataset.t||null;vActores()};
  document.getElementById("acsel").onchange=e=>{acSel=e.target.value;document.getElementById("atb").innerHTML=aRows()};
  document.getElementById("aq").oninput=e=>{aq=e.target.value;document.getElementById("atb").innerHTML=aRows()};
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
  s.addEventListener("click",e=>{const g=e.target.closest(".nn");if(!g)return;if(g.dataset.ext&&(T.meta.act.sin_ficha||[]).includes(g.dataset.id))return;if(g.dataset.ext)window.open(T.meta.act.global_url+"#o-"+g.dataset.id,"_blank","noopener");else location.hash="a-"+g.dataset.id});
}
function vActor(a){
  const M=T.meta.act,i=T.actores.indexOf(a),c=cityS[a.cs];
  const rel=T.relaciones.filter(r=>r.o===a.id||r.d===a.id).sort((x,y)=>y.n-x.n||x.t.localeCompare(y.t)),deps=T.actores.filter(x=>x.dep.includes(a.id));
  const afr=T.friccion.filter(f=>f.act.includes(a.id)),adp=Object.entries(T.deps).filter(([,d])=>d.ai.includes(a.id)),vec=a.cs!=="ciudad-autonoma-de-buenos-aires"?T.actores.filter(x=>x.id!==a.id&&(a.sd?x.sd===a.sd:a.cs&&x.cs===a.cs)):[];
  const grupos=[...new Set(M.ejes.map(e=>e.g))];
  const ejes=grupos.map(g=>`<div class="axg"><h3>${g}</h3>${M.ejes.map((e,k)=>[e,k]).filter(([e])=>e.g===g).map(([e,k])=>{const v=a.sc[k];return `<div class="axr" title="${esc(e.d)}${v?" · "+v+": "+esc(e.a[3-v]):""}"><span>${esc(e.n)}${M.pesos[e.k]?` <small class="muted">×${String(M.pesos[e.k]).replace(".",",")}</small>`:""}</span><span class="dots">${[1,2,3].map(n=>`<i class="${n<=v?"on":""}"></i>`).join("")}</span><b class="mono">${v}</b></div>`}).join("")}</div>`).join("");
  const compN={ct:"Categoría teórica",cap:"Capacidad",alc:"Alcance",aut:"Autonomía real",red:"Red heredada"};
  app.innerHTML=`<div class="page actor"><p class="crumbs"><a href="#actores">Actores</a> › <b>${esc(a.n)}</b></p>
  <h1>${esc(a.n)}</h1><p class="sub">${esc(a.res)}</p>${a.txt?`<p class="atxt">${esc(a.txt)}</p>`:""}
  <div class="facts"><div><span>Puntaje de poder</span><b class="mono">${a.pt.toLocaleString("es-AR")} <small class="muted">· n.º ${i+1}</small></b></div><div><span>Poder oculto</span><b class="mono">${a.oculto.toLocaleString("es-AR")}</b></div><div><span>Categoría</span><b style="color:${TCOL[a.tipo]};font-size:15px">${esc(a.cat)}</b></div><div><span>Sede</span><b style="font-size:15px">${c?`<a href="#c-${c.s}">${esc(c.n)}</a>`:a.sd?`<a href="#d-${a.sd}">${esc(a.sede)}</a>`:esc(a.sede)}</b></div><div><span>Alcance</span><b style="font-size:15px">${esc(M.alcance[a.alc])}</b></div><div><span>Autonomía</span><b style="font-size:15px">${esc(M.autonomia[a.aut])}</b></div><div><span>Depende de</span><b style="font-size:15px">${a.dep.length?a.dep.map(aLink).join(", "):"Nadie en el mapa"}</b></div><div><span>Bloque</span><b style="font-size:15px">${esc(M.bloques[a.bloque])}</b></div>${(a.pres||[]).length?`<div><span>Presencia</span><b style="font-size:15px">${a.pres.map(q=>{const pv=T.provincias.find(x=>x.id===q.p);return pv?`<a href="#prov-${pv.s}" title="${esc(q.x)}">${esc(pv.c)}</a>`:""}).join(", ")}</b></div>`:""}</div>
  <div class="cols"><div><h2 class="sec">Quién manda</h2><p class="lead">${esc(a.manda)}</p>
  <h2 class="sec">Relaciones · ${rel.length}</h2>${rel.length?`<ul class="rlist">${rel.map(r=>{const o=r.o===a.id?r.d:r.o,dir=r.o===a.id?"→":"←";return `<li><span class="tag" style="color:${RCOL[r.t]}">${r.t} ${dir}</span> ${aLink(o)} <span class="mono muted">${"●".repeat(r.n)}</span><br><span class="muted">${esc(r.x)}</span> ${src(r.u)}</li>`}).join("")}</ul>`:`<p class="muted">Sin relaciones cargadas todavía.</p>`}
  ${deps.length?`<h2 class="sec">Dependen de este actor</h2><p>${deps.map(d=>aLink(d.id)).join(" · ")}</p>`:""}
  ${a.dep.length?`<h2 class="sec">Depende de</h2><p>${a.dep.map(aLink).join(" · ")}</p>`:""}
  ${afr.length?`<h2 class="sec">Puntos de fricción · ${afr.length}</h2>${frList(afr)}`:""}
  ${adp.length?`<h2 class="sec">Departamentos donde pesa</h2><ul class="rlist">${adp.map(([id,d])=>`<li><a href="#d-${id}">${esc(d.n)}</a> <span class="muted">(${esc(byId[id.slice(0,2)].c)})</span></li>`).join("")}</ul>`:""}
  ${vec.length?`<h2 class="sec">Con sede en la misma ciudad</h2><p>${vec.map(x=>aLink(x.id)).join(" · ")}</p>`:""}
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
  else if(h==="friccion"){vFriccion();nk=h;svg=null}
  else if(h==="elecciones"){vElecciones();nk=h;svg=null}
  else if(h.startsWith("f-")&&FR[h.slice(2)]){vFr(FR[h.slice(2)]);nk="friccion";svg=null}
  else if(h.startsWith("a-")&&ACT[h.slice(2)]){vActor(ACT[h.slice(2)]);nk="actores";svg=null}
  else vPais();
  document.querySelectorAll("nav a").forEach(a=>a.classList.toggle("on",a.dataset.k===nk));
  if(["provincias","ciudades","plan","actores","friccion","elecciones"].includes(nk))window.scrollTo(0,0);
}
Promise.all(["data/territorio.json","data/provincias.json","data/antartida.json"].map(u=>fetch(u).then(r=>r.json()))).then(([t,pt,an])=>{
  T=t;ANT=an.features?an.features[0]:an;{const g=ANT.geometry||ANT;if(d3.geoArea(ANT)>2*Math.PI)(g.type==="Polygon"?[g.coordinates]:g.coordinates).forEach(pl=>pl.forEach(r=>r.reverse()))}
  PF=topojson.feature(pt,pt.objects.provincias);
  for(const p of T.provincias){byS[p.s]=p;byId[p.id]=p}
  for(const c of T.ciudades)cityS[c.s]=c;
  for(const a of T.actores){ACT[a.id]=a;(actCity[a.cs]=actCity[a.cs]||[]).push(a);(actProv[a.prov]=actProv[a.prov]||[]).push(a);for(const q of a.pres||[])(actPres[q.p]=actPres[q.p]||[]).push([a,q])}
  for(const f of T.friccion){FR[f.id]=f;(frProv[f.prov]=frProv[f.prov]||[]).push(f);if(f.cs)(frCity[f.cs]=frCity[f.cs]||[]).push(f)}
  const fd=d=>{const[y,m,x]=d.split("-");return +x+" "+MES[+m-1]+" "+y};
  document.getElementById("stamp").innerHTML=`Paso 5 de 5<br>Corte ${fd(T.corte)} · próxima ${fd(T.proxima)}`;
  document.getElementById("foot-date").textContent=`Corte del ${fd(T.corte)}; próxima revisión el ${fd(T.proxima)}.`;
  setup();addEventListener("hashchange",route);route();
}).catch(e=>{app.innerHTML=`<p style="padding:40px 0">No se pudo cargar el mapa: ${esc(e.message)}</p>`});
}
