import streamlit as st

st.set_page_config(page_title="மண் வாசம் — திறந்த உலகம்", page_icon="🏍️", layout="wide")

st.title("மண் வாசம்")
st.caption("தமிழ்நாட்டைத் தழுவிய 3D திறந்த உலகச் சாகசம் · ஓர் அசல் சிறு விளையாட்டு")

GAME_HTML = """
<main class="game-shell" aria-label="மண் வாசம் 3D திறந்த உலக விளையாட்டு">
  <header class="game-top">
    <div><span class="eyebrow">தமிழ்நாடு · 1998</span><h1>மண் வாசம் <span>ஒரு திறந்த உலகப் பயணம்</span></h1></div>
    <div class="top-right"><span class="live-dot"></span><span id="world-status">கதை தொடங்குகிறது</span></div>
  </header>
  <section class="play-area">
    <canvas id="world" aria-label="தமிழ்நாட்டு நகரங்களுடன் கூடிய 3D உலகம் · நடக்கும்போது கேமராவை மவுஸால் திருப்பு"></canvas>
    <div class="hud">
      <div class="mission-card"><div class="mission-kicker">✦ முதன்மைப் பணி</div><div id="mission-title" class="mission-title">மதுரையிலிருந்து ஒரு கடிதம்</div><div id="mission-copy" class="mission-copy">மீனாவிடம் பேசு; பிறகு ஒளிரும் கடிதத்தைத் தேடு.</div></div>
      <div class="location-card"><span class="location-pin">◆</span><span id="location-label">மதுரை</span></div>
      <div class="speed-card"><span id="speed-readout">0</span><small>கி.மீ/மணி</small></div>
      <div class="minimap-frame"><canvas id="minimap" aria-label="தமிழ்நாடு வழிச் சிறு வரைபடம்"></canvas><span>தமிழ்நாடு</span></div>
      <div class="hint-card" id="hint">WASD / அம்புகள் — நகர்வு · E — ஏறு / இறங்கு · F — பேசு</div>
    </div>
    <div id="dialogue" class="dialogue hidden" role="status"><div class="speaker" id="speaker"></div><div id="dialogue-text"></div><button id="dialogue-next" type="button">தொடர்க</button></div>
    <div id="cutscene" class="cutscene hidden" role="status"><div class="cutscene-kicker">கதைத் தொடர்</div><h2 id="cutscene-title"></h2><p id="cutscene-copy"></p><button id="cutscene-skip" type="button">தொடர்க →</button></div>
    <div id="intro" class="intro">
      <div class="intro-content"><div class="intro-overline">ஒரு தமிழ்நாட்டுப் பயணம்</div><h2 id="intro-title">ஊர் திரும்பும் பாதை</h2><p id="intro-copy">மழை ஓய்ந்த மதுரையின் ஒரு விடியற்காலை.</p><div class="intro-progress"><span id="intro-progress"></span></div><div class="intro-actions"><span>ஒரு சிறிய கதை · ஒரு முழுமையான 3D உலகம்</span><button id="start-game" type="button">பயணத்தைத் தொடங்கு <b>→</b></button></div></div>
      <div class="cinema-bar top"></div><div class="cinema-bar bottom"></div><div class="skip-label">தொடர அழுத்தவும்</div>
    </div>
    <div class="touch-controls" aria-label="தொடு கட்டுப்பாடுகள்"><div class="touch-pad"><button data-key="ArrowUp" aria-label="முன்னே">↑</button><button data-key="ArrowLeft" aria-label="இடது">←</button><button data-key="ArrowDown" aria-label="பின்னே">↓</button><button data-key="ArrowRight" aria-label="வலது">→</button></div><div class="touch-actions"><button class="touch-action" data-key="e" aria-label="வாகனத்தில் ஏறு அல்லது இறங்கு">E</button><button class="touch-action" data-key="f" aria-label="அருகிலுள்ளவரிடம் பேசு">F</button></div></div>
  </section>
  <footer class="game-footer"><span><b>W / ↑</b> முன்னேற்று · <b>S / ↓</b> பின்னோக்கு</span><span><b>A / ←</b> இடப்புறம் · <b>D / →</b> வலப்புறம்</span><span><b>E</b> வாகனத்தில் ஏறு / இறங்கு</span><span><b>F</b> அருகிலுள்ளவரிடம் பேசு</span><span><b>Space</b> பிரேக்</span><span class="footer-note">நடக்கும்போது மவுஸால் பார்வையைத் திருப்பு · மதுரை முதல் ராமேஸ்வரம் வரை</span></footer>
</main>
"""

GAME_CSS = """
:host { display:block; color:#f4eee2; font-family:Inter,"Noto Sans Tamil","Latha",system-ui,sans-serif; }
* { box-sizing:border-box; }
.game-shell { width:100%; overflow:hidden; border:1px solid #32443a; border-radius:18px; background:#111915; box-shadow:0 24px 80px #0007; }
.game-top { min-height:78px; display:flex; align-items:center; justify-content:space-between; gap:16px; padding:13px 22px; background:linear-gradient(100deg,#111a17,#1a2620); border-bottom:1px solid #35453b; }
.eyebrow { color:#d5a65e; font-size:10px; letter-spacing:2px; }
.game-top h1 { margin:3px 0 0; font-size:24px; line-height:1.2; }.game-top h1 span { margin-left:8px; color:#a9b3a9; font-size:12px; font-weight:400; }
.top-right { display:flex; align-items:center; gap:9px; color:#c7d0c4; font-size:12px; white-space:nowrap; }.live-dot { width:7px; height:7px; border-radius:50%; background:#83ca83; box-shadow:0 0 11px #83ca83; }
.play-area { height:min(70vw,660px); min-height:420px; position:relative; overflow:hidden; background:linear-gradient(#91b4c3 0%,#bbd0ce 54%,#73875f 100%); }#world { display:block; width:100%; height:100%; }
.play-area.walking #world { cursor:crosshair; }
.hud { pointer-events:none; position:absolute; inset:0; }.mission-card { position:absolute; top:17px; left:17px; width:min(300px,48%); padding:12px 15px; border:1px solid #b58a51a8; border-radius:10px; background:#111a17e8; box-shadow:0 6px 20px #0003; }
.mission-kicker { color:#e9b96e; font-size:11px; }.mission-title { margin-top:5px; font-size:15px; font-weight:700; }.mission-copy { margin-top:4px; color:#c2cabc; font-size:11px; line-height:1.5; }
.location-card { position:absolute; top:17px; right:17px; padding:9px 13px; border:1px solid #ffffff45; border-radius:8px; background:#111a17d9; color:#fff1d6; font-size:13px; }.location-pin { margin-right:8px; color:#f1bd6c; font-size:10px; }
.speed-card { position:absolute; right:18px; bottom:18px; width:78px; height:78px; display:flex; flex-direction:column; align-items:center; justify-content:center; border:2px solid #d6ad66a8; border-radius:50%; background:#121a17e8; }.speed-card span { font-size:25px; font-weight:750; line-height:1; }.speed-card small { margin-top:5px; color:#bdc7b7; font-size:9px; }
.minimap-frame { position:absolute; top:69px; right:17px; width:145px; height:112px; overflow:hidden; border:1px solid #d4c39799; border-radius:8px; background:#111a17ec; }.minimap-frame canvas { display:block; width:100%; height:86px; }.minimap-frame span { display:block; padding:2px 8px 4px; color:#e3d2ad; font-size:9px; text-align:right; }
.hint-card { position:absolute; bottom:17px; left:17px; max-width:calc(100% - 125px); padding:9px 12px; border:1px solid #ffffff45; border-radius:7px; background:#111a17d9; color:#e5e9dd; font-size:11px; }
.dialogue { position:absolute; z-index:2; bottom:20px; left:50%; width:min(570px,calc(100% - 36px)); padding:14px 17px; transform:translateX(-50%); border:1px solid #d5ad6d; border-radius:10px; background:#121916f2; box-shadow:0 8px 30px #0008; font-size:13px; line-height:1.7; }.dialogue.hidden { display:none; }.speaker { color:#f1ba62; font-size:12px; font-weight:700; }.dialogue button { float:right; margin-top:7px; padding:5px 12px; border:0; border-radius:5px; background:#d9a958; color:#191b15; font-weight:700; cursor:pointer; }
.cutscene { position:absolute; z-index:2; right:0; bottom:0; left:0; padding:25px max(24px,7%) 23px; border-top:1px solid #e5b969; background:linear-gradient(90deg,#101714f5,#101714dc 75%,#101714a8); }.cutscene.hidden { display:none; }.cutscene-kicker { color:#e8bc72; font-size:10px; letter-spacing:2px; }.cutscene h2 { margin:5px 0; color:#fff1d6; font-size:clamp(20px,3vw,30px); }.cutscene p { max-width:640px; margin:0; color:#d6d8cd; font-size:13px; line-height:1.7; }.cutscene button { position:absolute; right:max(24px,7%); bottom:22px; padding:9px 14px; border:1px solid #d8b578; border-radius:5px; background:#d9a958; color:#191b15; font-weight:700; cursor:pointer; }
.intro { position:absolute; z-index:3; inset:0; overflow:hidden; background:linear-gradient(180deg,#10161322 0%,#10161366 42%,#101613ed 100%); transition:opacity .65s ease; }.intro::before { content:""; position:absolute; inset:0; opacity:.42; background:radial-gradient(ellipse at 50% 32%,#edbe7622 0,transparent 44%),linear-gradient(180deg,transparent 30%,#10161377 100%); }.intro.hidden { opacity:0; pointer-events:none; }
.intro-content { position:absolute; z-index:1; right:8%; bottom:13%; left:8%; }.intro-overline { color:#edc47f; font-size:11px; letter-spacing:2px; }.intro-content h2 { max-width:650px; margin:8px 0; font-size:clamp(30px,5vw,58px); line-height:1.15; }.intro-content p { color:#e3dfd1; font-size:15px; }.intro-progress { width:min(340px,70%); height:2px; margin-top:23px; background:#ffffff42; }.intro-progress span { display:block; width:0; height:100%; background:#f0bd6d; transition:width .5s; }
.intro-actions { display:flex; align-items:center; justify-content:space-between; gap:14px; margin-top:14px; color:#d4d6ca; font-size:11px; }.intro-actions button { padding:11px 16px; border:0; border-radius:5px; background:#e8b96d; color:#192019; font:inherit; font-weight:700; cursor:pointer; }.intro-actions button b { margin-left:12px; }.cinema-bar { position:absolute; z-index:2; left:0; right:0; height:0; background:#090c0b; transition:height .7s ease; }.cinema-bar.top { top:0; }.cinema-bar.bottom { bottom:0; }.intro.cinematic .cinema-bar { height:8%; }.skip-label { position:absolute; z-index:3; top:14px; right:18px; color:#ffffffaa; font-size:10px; }
.game-footer { display:flex; flex-wrap:wrap; gap:10px 19px; align-items:center; padding:12px 18px; background:#121a16; color:#bcc6b8; font-size:10px; }.game-footer b { color:#e8c27c; }.footer-note { margin-left:auto; color:#d7d1bd; }
.touch-controls { display:none; }.touch-actions { display:flex; gap:8px; pointer-events:auto; }
@media(max-width:700px) { .game-top { padding:12px 14px; }.game-top h1 { font-size:20px; }.game-top h1 span { display:block; margin:3px 0 0; font-size:10px; }.play-area { height:75vw; min-height:430px; max-height:580px; }.mission-card { top:10px; left:10px; width:min(260px,64%); padding:9px 11px; }.mission-title { font-size:13px; }.mission-copy { font-size:10px; }.minimap-frame { top:auto; right:10px; bottom:170px; width:112px; height:88px; }.minimap-frame canvas { height:65px; }.location-card { top:10px; right:10px; padding:7px 9px; font-size:11px; }.speed-card { right:10px; bottom:12px; width:65px; height:65px; }.speed-card span { font-size:20px; }.hint-card { display:none; }.game-footer { gap:8px 13px; padding:10px 12px; }.footer-note { width:100%; margin-left:0; }.touch-controls { position:absolute; z-index:2; inset:auto 10px 72px; display:flex; justify-content:space-between; align-items:end; pointer-events:none; }.touch-pad { display:grid; grid-template-columns:38px 38px 38px; grid-template-rows:38px 38px; gap:3px; pointer-events:auto; }.touch-pad button,.touch-action { border:1px solid #ffffff66; border-radius:8px; background:#18221dc7; color:#fff; font-size:18px; touch-action:none; }.touch-pad button:nth-child(1) { grid-column:2; }.touch-pad button:nth-child(2) { grid-column:1; grid-row:2; }.touch-pad button:nth-child(3) { grid-column:2; grid-row:2; }.touch-pad button:nth-child(4) { grid-column:3; grid-row:2; }.touch-action { width:45px; height:45px; border-radius:50%; pointer-events:auto; }.intro-content { right:7%; bottom:11%; left:7%; }.intro-actions { align-items:flex-start; flex-direction:column; }.intro-actions button { align-self:flex-end; } }
"""

GAME_JS = r"""
export default function (component) {
  const root=component.parentElement, canvas=root.querySelector("#world"), gl=canvas.getContext("webgl",{antialias:true});
  const mini=root.querySelector("#minimap"), mctx=mini.getContext("2d"), $=id=>root.querySelector("#"+id);
  if(!gl){$("world-status").textContent="இந்த உலாவியில் WebGL இயங்கவில்லை";return;}
  const keys=new Set(), clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
  const mapPoint=p=>[(p[0]-1100)/18,(p[1]-950)/18];
  const roadData=[
    [[-100,930],[350,930],[700,920],[1030,960],[1350,970],[1690,1000],[2030,1040],[2280,1070]],
    [[560,200],[580,540],[640,800],[700,920],[740,1240],[760,1600]],
    [[1200,200],[1190,540],[1200,820],[1190,980],[1230,1280],[1250,1660]],
    [[1920,220],[1900,520],[1860,800],[1900,1050],[1910,1340],[1880,1700]],
    [[350,930],[300,1180],[320,1430],[420,1670]],[[1030,960],[1020,1180],[1050,1430],[1120,1680]],
    [[1690,1000],[1600,1220],[1560,1470],[1600,1720]],[[2030,1040],[2200,920],[2350,850]],
    [[560,540],[850,520],[1190,540],[1510,550],[1900,520]],
    [[700,1240],[900,1240],[1230,1280],[1460,1280],[1860,1300]],
    [[300,1180],[550,1160],[800,1180],[1020,1180]],[[1600,1470],[1810,1460],[2050,1490],[2230,1560]]
  ].map(route=>route.map(mapPoint));
  roadData.push(
    [[-66,-1],[-79,-3],[-91,-10],[-103,-12]],
    [[-41,-1],[-50,-10],[-56,-21],[-62,-30]],
    [[-30,36],[-30,48],[-25,60],[-16,69]],
    [[5,39],[7,52],[16,64],[28,69]],
    [[68,6],[80,8],[91,15],[103,18]],
    [[69,33],[81,38],[91,46],[99,54]],
    [[25,45],[37,54],[49,60],[62,65]],
    [[-56,-21],[-43,-25],[-31,-28],[-20,-31]]
  );
  const towns=[
    {name:"சென்னை",p:[1900,430],kind:"city"},{name:"கோயம்புத்தூர்",p:[350,930],kind:"city"},
    {name:"திருச்சி",p:[1190,980],kind:"city"},{name:"மதுரை",p:[740,1240],kind:"city"},
    {name:"தஞ்சாவூர்",p:[1460,1280],kind:"town"},{name:"ராமநாதபுரம்",p:[1910,1340],kind:"town"},
    {name:"ராமேஸ்வரம்",p:[2230,1560],kind:"coast"},{name:"கன்னியாகுமரி",p:[1560,1720],kind:"coast"},
    {name:"ஊட்டி",p:[390,360],kind:"hill"},{name:"சேலம்",p:[1020,690],kind:"town"},
    {name:"காரைக்குடி",p:[1540,1120],kind:"town"}
  ].map(t=>({...t,pos:mapPoint(t.p)}));
  towns.push(
    {name:"திண்டுக்கல்",pos:[-18,9],kind:"town"},
    {name:"தேனி",pos:[-26,26],kind:"town"},
    {name:"ஈரோடு",pos:[-47,-10],kind:"town"},
    {name:"கும்பகோணம்",pos:[27,13],kind:"town"},
    {name:"நாகப்பட்டினம்",pos:[43,24],kind:"coast"}
  );
  const start=mapPoint([720,1270]), letter=mapPoint([810,1280]), goal=mapPoint([2220,1610]);
  const teaParcel=[-24,14], selviSpot=[-12.5,19], lostNet=[66,39], arunSpot=[66,34];
  const player={x:start[0],z:start[1],yaw:0,speed:0,vx:0,vz:0,steer:0,inCar:true}, car={x:start[0],z:start[1],yaw:0};
  const obstacles=[], staticDraws=[];
  const npcs=[
    {name:"மீனா",role:"பாட்டியின் பேத்தி",x:-19,z:15.5,color:[.82,.33,.22],line:"அக்கா, பாட்டி உனக்காக ஒரு கடிதம் வைத்திருக்கிறார். மதுரை கோவிலருகே தேடு."},
    {name:"முருகன்",role:"தேநீர்க் கடைக்காரர்",x:-24,z:14,color:[.19,.43,.35],line:"மதுரைலிருந்து ராமேஸ்வரமா? கிழக்குச் சாலையைப் பிடிச்சுப் போங்க. நல்ல பயணம்!"},
    {name:"செல்வி",role:"பள்ளி மாணவி",x:-16,z:19,color:[.84,.68,.3],line:"அக்கா, உங்க சிவப்புக் கார் ரொம்ப அழகு! எனக்கும் ஒருநாள் ஓட்டக் கற்றுக்கொடுக்கணும்."},
    {name:"ராஜா",role:"ஆட்டோ ஓட்டுநர்",x:-26,z:20,color:[.3,.45,.78],line:"மதுரையைச் சுற்றிப் பார்க்க நிறைய இடங்கள் இருக்கு. வரைபடத்திலுள்ள ஊர்களுக்குப் போய்ப் பாருங்க."},
    {name:"சுந்தரம்",role:"கோவில் பூசாரி",x:-20,z:22,color:[.75,.72,.57],line:"கடிதத்தை ராமேஸ்வரம் கோவிலில் சேர்த்தால், உன் பாட்டியின் ஆசை நிறைவேறும்."},
    {name:"கவி",role:"பயணி",x:-31,z:16,color:[.65,.35,.61],line:"இந்தச் சாலைகள் ஊருக்கு ஊர் கதைகளைச் சொல்லும். நிதானமாகச் சுற்றிப் பாருங்கள்!"},
    {name:"அருண்",role:"மீனவர்",x:64,z:34,color:[.78,.48,.25],line:"கடல் பாலத்தின் மேலே போனால் ராமேஸ்வரம் வந்துவிடும். கடற்காற்றை ரசித்துக்கொண்டே போங்க!"},
    {name:"திலகம்",role:"மலர் விற்பவர்",x:62,z:31,color:[.72,.31,.43],line:"கோவிலுக்குப் பூ வாங்கிக்கோங்க! ராமேஸ்வரத்தில் பார்க்க நிறைய இடங்கள் இருக்கு."},
    {name:"செந்தில்",role:"சென்னையிலிருந்து வந்த பயணி",x:44,z:-28,color:[.30,.48,.69],line:"சென்னையிலிருந்து நீண்ட பயணம் செய்து வந்தேன். தமிழ்நாட்டின் ஒவ்வொரு ஊருக்கும் ஒரு தனி அழகு!"}
  ];
  const introLines=[["ஊர் திரும்பும் பாதை","மழை ஓய்ந்த மதுரையின் ஒரு விடியற்காலை."],["ஒரு பழைய கடிதம்","பாட்டியின் கடைசி ஆசை — ராமேஸ்வரம் கோவிலில் இந்தக் கடிதத்தைச் சேர்க்க வேண்டும்."],["பயணம் உன்னுடையது","மீனாவைச் சந்தி, கடிதத்தைப் பெறு, தமிழ்நாட்டின் சாலைகளில் உன் வழியைத் தேடு."]];
  let started=false,dialogOpen=false,last=0,introFrame=0,elapsed=0;
  let cameraYaw=0,cameraPitch=.38,mouseLookDrag=false;
  let mission=0,missionStage=0,cutsceneUntil=0,cutsceneTarget=null,worldBuilt=false,buildingWorld=false;

  const vertex=`attribute vec3 aPosition;attribute vec3 aNormal;uniform mat4 uMvp;uniform mat4 uModel;varying vec3 vNormal;varying vec3 vWorld;void main(){vec4 world=uModel*vec4(aPosition,1.0);vWorld=world.xyz;vNormal=normalize(mat3(uModel)*aNormal);gl_Position=uMvp*vec4(aPosition,1.0);}`;
  const fragment=`precision mediump float;uniform vec3 uColor;uniform vec3 uEye;varying vec3 vNormal;varying vec3 vWorld;void main(){vec3 n=normalize(vNormal);vec3 light=normalize(vec3(-0.45,0.85,0.35));vec3 viewDir=normalize(uEye-vWorld);vec3 halfDir=normalize(light+viewDir);float diffuse=max(dot(n,light),0.0);float paint=step(0.35,uColor.r)*(1.0-step(0.15,uColor.g));float specular=pow(max(dot(n,halfDir),0.0),mix(24.0,48.0,paint))*mix(0.16,0.4,paint);float shade=0.46+diffuse*0.58;float grain=sin(vWorld.x*19.0+sin(vWorld.z*17.0))*0.018;vec3 lit=uColor*(shade+grain)+vec3(specular);float fog=smoothstep(48.0,105.0,distance(vWorld,uEye));vec3 sky=vec3(0.59,0.72,0.77);vec3 color=mix(lit,sky,fog);gl_FragColor=vec4(color,1.0);}`;
  function shader(type,source){const s=gl.createShader(type);gl.shaderSource(s,source);gl.compileShader(s);if(!gl.getShaderParameter(s,gl.COMPILE_STATUS))throw new Error(gl.getShaderInfoLog(s));return s;}
  const program=gl.createProgram();gl.attachShader(program,shader(gl.VERTEX_SHADER,vertex));gl.attachShader(program,shader(gl.FRAGMENT_SHADER,fragment));gl.linkProgram(program);
  if(!gl.getProgramParameter(program,gl.LINK_STATUS))throw new Error(gl.getProgramInfoLog(program));
  gl.useProgram(program);
  const loc={pos:gl.getAttribLocation(program,"aPosition"),normal:gl.getAttribLocation(program,"aNormal"),mvp:gl.getUniformLocation(program,"uMvp"),model:gl.getUniformLocation(program,"uModel"),color:gl.getUniformLocation(program,"uColor"),eye:gl.getUniformLocation(program,"uEye")};
  gl.enableVertexAttribArray(loc.pos);gl.enableVertexAttribArray(loc.normal);
  function mesh(data){const b=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,b);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array(data),gl.STATIC_DRAW);return{buffer:b,count:data.length/6};}
  function face(out,a,b,c,d,n){for(const v of [a,b,c,a,c,d])out.push(...v,...n);}
  function carBodyMesh(sections,bottom=-.5,cornerRadius=.11){
    const steps=4,profiles=sections.map(([,width,top])=>{
      const corners=[[width-cornerRadius,bottom+cornerRadius,-Math.PI/2,0],[width-cornerRadius,top-cornerRadius,0,Math.PI/2],[-width+cornerRadius,top-cornerRadius,Math.PI/2,Math.PI],[-width+cornerRadius,bottom+cornerRadius,Math.PI,Math.PI*1.5]];
      return corners.flatMap(([cx,cy,start,end])=>Array.from({length:steps},(_,i)=>{const a=start+(end-start)*i/steps;return[cx+Math.cos(a)*cornerRadius,cy+Math.sin(a)*cornerRadius];}));
    });
    const out=[],unit=v=>{const d=Math.hypot(...v)||1;return v.map(n=>n/d);},cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
    for(let section=0;section<sections.length-1;section++)for(let i=0;i<profiles[section].length;i++){
      const next=(i+1)%profiles[section].length,vertices=[[section,i],[section,next],[section+1,next],[section+1,i]].map(([s,j])=>[profiles[s][j][0],profiles[s][j][1],sections[s][0]]);
      const normalAt=(s,j)=>{
        const before=profiles[s][(j+profiles[s].length-1)%profiles[s].length],after=profiles[s][(j+1)%profiles[s].length],tangent=after.map((n,k)=>n-before[k]);
        const prev=profiles[Math.max(0,s-1)][j],following=profiles[Math.min(sections.length-1,s+1)][j],depth=following.map((n,k)=>n-prev[k]);
        return unit(cross([tangent[0],tangent[1],0],[depth[0],depth[1],sections[Math.min(sections.length-1,s)][0]-sections[Math.max(0,s-1)][0]]));
      };
      const normals=[[section,i],[section,next],[section+1,next],[section+1,i]].map(([s,j])=>normalAt(s,j));
      for(const k of [0,1,2,0,2,3])out.push(...vertices[k],...normals[k]);
    }
    for(const s of [0,sections.length-1]){
      const profile=profiles[s],centerY=(profile[4][1]+profile[12][1])/2,normal=[0,0,s===0?-1:1];
      for(let i=0;i<profile.length;i++){
        const a=profile[i],b=profile[(i+1)%profile.length],center=[0,centerY,sections[s][0]];
        for(const point of [center,[a[0],a[1],sections[s][0]],[b[0],b[1],sections[s][0]]])out.push(...point,...normal);
      }
    }
    return mesh(out);
  }
  const carBody=carBodyMesh([[-.5,.34,-.12],[-.46,.42,.22],[-.34,.47,.36],[-.18,.5,.42],[.12,.5,.38],[.28,.48,.27],[.42,.43,.12],[.48,.35,-.02],[.5,.28,-.1]]);
  const carCabin=carBodyMesh([[-.5,.36,.20],[-.42,.47,.42],[-.3,.5,.5],[.18,.5,.5],[.34,.47,.4],[.5,.35,.12]],-.5,.09);
  const cubeData=[];face(cubeData,[-.5,-.5,.5],[.5,-.5,.5],[.5,.5,.5],[-.5,.5,.5],[0,0,1]);face(cubeData,[.5,-.5,-.5],[-.5,-.5,-.5],[-.5,.5,-.5],[.5,.5,-.5],[0,0,-1]);face(cubeData,[-.5,-.5,-.5],[-.5,-.5,.5],[-.5,.5,.5],[-.5,.5,-.5],[-1,0,0]);face(cubeData,[.5,-.5,.5],[.5,-.5,-.5],[.5,.5,-.5],[.5,.5,.5],[1,0,0]);face(cubeData,[-.5,.5,.5],[.5,.5,.5],[.5,.5,-.5],[-.5,.5,-.5],[0,1,0]);face(cubeData,[-.5,-.5,-.5],[.5,-.5,-.5],[.5,-.5,.5],[-.5,-.5,.5],[0,-1,0]);
  const cube=mesh(cubeData);
  function roundedBoxMesh(segments=6,radius=.12){
    const out=[],axes=[[0,1,2],[0,2,1],[1,2,0],[1,0,2],[2,0,1],[2,1,0]];
    for(let side=0;side<6;side++){
      const [u,v,fixed]=axes[side],sign=side%2?1:-1;
      const point=(a,b)=>{
        const q=[0,0,0];q[u]=a;q[v]=b;q[fixed]=sign*.5;
        const inner=q.map(n=>clamp(n,-.5+radius,.5-radius)),delta=q.map((n,i)=>n-inner[i]),length=Math.hypot(...delta);
        const normal=delta.map(n=>n/length),p=inner.map((n,i)=>n+normal[i]*radius);
        return[p,normal];
      };
      for(let row=0;row<segments;row++)for(let col=0;col<segments;col++){
        const a0=col/segments-.5,a1=(col+1)/segments-.5,b0=row/segments-.5,b1=(row+1)/segments-.5;
        const corners=[point(a0,b0),point(a1,b0),point(a1,b1),point(a0,b1)];
        for(const i of [0,1,2,0,2,3])out.push(...corners[i][0],...corners[i][1]);
      }
    }
    return mesh(out);
  }
  const roundedCube=roundedBoxMesh();
  function roundMesh(sides=12,rings=8){const out=[];for(let y=0;y<rings;y++){const v0=y/rings,v1=(y+1)/rings,lat0=(v0-.5)*Math.PI,lat1=(v1-.5)*Math.PI;for(let x=0;x<sides;x++){const a=x/sides*Math.PI*2,b=(x+1)/sides*Math.PI*2;const pt=(lat,lon)=>[Math.cos(lat)*Math.cos(lon),Math.sin(lat),Math.cos(lat)*Math.sin(lon)];const p00=pt(lat0,a),p10=pt(lat0,b),p11=pt(lat1,b),p01=pt(lat1,a);face(out,p00,p10,p11,p01,p00.map((n,i)=>n));}}return mesh(out);}
  const sphere=roundMesh(16,11);
  function cylinderMesh(sides=10){const out=[];for(let i=0;i<sides;i++){const a=i/sides*Math.PI*2,b=(i+1)/sides*Math.PI*2,p0=[Math.cos(a),-.5,Math.sin(a)],p1=[Math.cos(b),-.5,Math.sin(b)],p2=[Math.cos(b),.5,Math.sin(b)],p3=[Math.cos(a),.5,Math.sin(a)];face(out,p0,p1,p2,p3,[Math.cos((a+b)/2),0,Math.sin((a+b)/2)]);face(out,[0,.5,0],p3,p2,[0,.5,0],[0,1,0]);face(out,[0,-.5,0],p1,p0,[0,-.5,0],[0,-1,0]);}return mesh(out);}
  const cylinder=cylinderMesh();
  function gableRoofMesh(){
    const out=[],triangle=(a,b,c,n)=>{for(const p of [a,b,c])out.push(...p,...n);};
    for(const z of [-.5,.5]){
      const sign=z<0?-1:1;
      triangle([-.5,-.5,z],[.5,-.5,z],[0,.5,z],[0,0,sign]);
    }
    face(out,[0,.5,-.5],[.5,-.5,-.5],[.5,-.5,.5],[0,.5,.5],[.71,.71,0]);
    face(out,[0,.5,.5],[-.5,-.5,.5],[-.5,-.5,-.5],[0,.5,-.5],[-.71,.71,0]);
    return mesh(out);
  }
  const gableRoof=gableRoofMesh();
  function wheelMeshCreate(sides=24){
    const out=[];
    const rings=[[-.5,.82],[-.40,.98],[.40,.98],[.5,.82]];
    for(let i=0;i<sides;i++){
      const a=i/sides*Math.PI*2,b=(i+1)/sides*Math.PI*2;
      const p=(ring,t)=>[ring[0],Math.cos(t)*ring[1],Math.sin(t)*ring[1]],n=[0,Math.cos((a+b)/2),Math.sin((a+b)/2)];
      for(let ring=0;ring<rings.length-1;ring++)face(out,p(rings[ring],a),p(rings[ring],b),p(rings[ring+1],b),p(rings[ring+1],a),n);
      face(out,[-.5,0,0],p(rings[0],b),p(rings[0],a),[-.5,0,0],[-1,0,0]);
      face(out,[.5,0,0],p(rings[3],a),p(rings[3],b),[.5,0,0],[1,0,0]);
    }
    return mesh(out);
  }
  const wheelMesh=wheelMeshCreate();
  function ident(){return[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1];}
  function mul(a,b){const o=new Array(16);for(let c=0;c<4;c++)for(let r=0;r<4;r++)o[c*4+r]=a[r]*b[c*4]+a[4+r]*b[c*4+1]+a[8+r]*b[c*4+2]+a[12+r]*b[c*4+3];return o;}
  function persp(fov,aspect,near,far){const f=1/Math.tan(fov/2),nf=1/(near-far);return[f/aspect,0,0,0,0,f,0,0,0,0,(far+near)*nf,-1,0,0,2*far*near*nf,0];}
  function look(eye,target){const norm=v=>{const l=Math.hypot(...v)||1;return v.map(x=>x/l);},cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sub=(a,b)=>a.map((v,i)=>v-b[i]);const z=norm(sub(eye,target)),x=norm(cross([0,1,0],z)),y=cross(z,x);return[x[0],y[0],z[0],0,x[1],y[1],z[1],0,x[2],y[2],z[2],0,-x[0]*eye[0]-x[1]*eye[1]-x[2]*eye[2],-y[0]*eye[0]-y[1]*eye[1]-y[2]*eye[2],-z[0]*eye[0]-z[1]*eye[1]-z[2]*eye[2],1];}
  function modelMatrix(x,y,z,sx,sy,sz,rot=0,pitch=0){const c=Math.cos(rot),s=Math.sin(rot),cp=Math.cos(pitch),sp=Math.sin(pitch);return[c*sx,0,-s*sx,0,s*sp*sy,cp*sy,c*sp*sy,0,s*cp*sz,-sp*sz,c*cp*sz,0,x,y,z,1];}
  const colors={grass:[.42,.55,.34],yard:[.38,.50,.31],shoulder:[.47,.41,.31],road:[.29,.31,.30],line:[.82,.76,.59],roof:[.50,.23,.16],wall:[.73,.62,.43],leaf:[.19,.38,.24],trunk:[.34,.24,.14],water:[.22,.49,.56],field:[.48,.40,.23],crop:[.29,.40,.19],car:[.58,.055,.035],carLight:[.72,.10,.06],glass:[.12,.25,.29],rubber:[.055,.06,.058],skin:[.70,.47,.32],white:[.9,.82,.62],gold:[.87,.65,.27],chrome:[.56,.59,.55],dark:[.10,.12,.12],seat:[.17,.13,.10]};
  function drawMesh(m,mod,color){const mvp=mul(viewProj,mod);gl.uniformMatrix4fv(loc.model,false,new Float32Array(mod));gl.uniformMatrix4fv(loc.mvp,false,new Float32Array(mvp));gl.uniform3fv(loc.color,color);gl.bindBuffer(gl.ARRAY_BUFFER,m.buffer);gl.vertexAttribPointer(loc.pos,3,gl.FLOAT,false,24,0);gl.vertexAttribPointer(loc.normal,3,gl.FLOAT,false,24,12);gl.drawArrays(gl.TRIANGLES,0,m.count);}
  function draw(m,x,y,z,sx,sy,sz,color,rot=0,pitch=0){const mod=modelMatrix(x,y,z,sx,sy,sz,rot,pitch);if(buildingWorld){staticDraws.push({m,mod,color});return;}drawMesh(m,mod,color);}
  function box(x,y,z,sx,sy,sz,color,rot=0,pitch=0){draw(cube,x,y,z,sx,sy,sz,color,rot,pitch);}
  function softBox(x,y,z,sx,sy,sz,color,rot=0,pitch=0){draw(roundedCube,x,y,z,sx,sy,sz,color,rot,pitch);}
  function ball(x,y,z,sx,sy,sz,color){draw(sphere,x,y,z,sx,sy,sz,color);}
  let viewProj,eye=[0,10,20];
  function buildWorld(){
    box(0,-.52,0,220,.5,150,colors.grass);
    box(92,-.16,0,88,.12,150,colors.water);
    box(48,-.14,34,10,.08,34,[.74,.65,.45]);
    for(const [x,z,sx,sz] of [[-89,-64,12,7],[-60,-67,15,8],[-28,-65,13,7],[6,-68,16,8],[43,-64,13,7]]){
      ball(x,1.2,z,sx,3.2,sz,[.34,.46,.33]);
      ball(x+sx*.48,.25,z+sz*.55,sx*.56,1.15,sz*.48,[.37,.49,.34]);
    }
    for(let routeIndex=0;routeIndex<roadData.length;routeIndex++)for(let i=0;i<roadData[routeIndex].length-1;i++){
      const route=roadData[routeIndex],a=route[i],b=route[i+1],dx=b[0]-a[0],dz=b[1]-a[1],length=Math.hypot(dx,dz),yaw=Math.atan2(dx,dz),mx=(a[0]+b[0])/2,mz=(a[1]+b[1])/2;
      const roadWidth=routeIndex<12?5.4:4.2,shoulderWidth=roadWidth+1.3;
      box(mx,-.205,mz,shoulderWidth,.08,length,colors.shoulder,yaw);
      box(mx,-.15,mz,roadWidth,.10,length,colors.road,yaw);
      if(routeIndex<12)for(let distance=5;distance<length-2;distance+=9){
        box(a[0]+dx*distance/length,-.086,a[1]+dz*distance/length,.12,.018,2.4,colors.line,yaw);
      }
    }
    const junctions=[];
    const addJunction=(x,z,width)=>{
      const existing=junctions.find(point=>Math.hypot(point.x-x,point.z-z)<1);
      if(existing)existing.width=Math.max(existing.width,width);
      else junctions.push({x,z,width});
    };
    for(let first=0;first<roadData.length;first++)for(let second=first+1;second<roadData.length;second++){
      const firstWidth=first<12?5.4:4.2,secondWidth=second<12?5.4:4.2;
      for(let i=1;i<roadData[first].length;i++)for(let j=1;j<roadData[second].length;j++){
        const a=roadData[first][i-1],b=roadData[first][i],c=roadData[second][j-1],d=roadData[second][j];
        const rx=b[0]-a[0],rz=b[1]-a[1],sx=d[0]-c[0],sz=d[1]-c[1],denominator=rx*sz-rz*sx;
        if(Math.abs(denominator)<.001)continue;
        const qx=c[0]-a[0],qz=c[1]-a[1],t=(qx*sz-qz*sx)/denominator,u=(qx*rz-qz*rx)/denominator;
        if(t>=0&&t<=1&&u>=0&&u<=1)addJunction(a[0]+rx*t,a[1]+rz*t,Math.max(firstWidth,secondWidth));
      }
    }
    for(const junction of junctions)draw(cylinder,junction.x,-.14,junction.z,junction.width+1,.08,junction.width+1,colors.road);
    const placedHouses=[];
    towns.forEach(town=>{
      const [x,z]=town.pos;
      if(town.kind==="hill"){
        for(let i=0;i<7;i++)ball(x-10+i*4,2+i*.55,z-7,10-i*.6,5+i*.25,11-i*.5,[.27,.39,.28]);
      }else{
        let nearest=null;
        for(let routeIndex=0;routeIndex<roadData.length;routeIndex++)for(let i=1;i<roadData[routeIndex].length;i++){
          const route=roadData[routeIndex];
          const a=route[i-1],b=route[i],dx=b[0]-a[0],dz=b[1]-a[1],lengthSq=dx*dx+dz*dz;
          const t=clamp(((x-a[0])*dx+(z-a[1])*dz)/lengthSq,0,1),px=a[0]+dx*t,pz=a[1]+dz*t,distance=Math.hypot(x-px,z-pz);
          if(!nearest||distance<nearest.distance)nearest={a,b,dx,dz,length:Math.sqrt(lengthSq),px,pz,distance,roadWidth:routeIndex<12?5.4:4.2};
        }
        if(nearest&&nearest.distance<13&&!(x>45&&z>25)){
          const {dx,dz,length,px,pz}=nearest,yaw=Math.atan2(dx,dz),nx=dz/length,nz=-dx/length;
          const count=town.kind==="city"?5:4,spacing=town.kind==="city"?7.5:8.2;
          for(const side of [-1,1])for(let i=0;i<count;i++){
            const along=(i-(count-1)/2)*spacing,bx=px+dx/length*along+nx*side*(nearest.roadWidth/2+7.2),bz=pz+dz/length*along+nz*side*(nearest.roadWidth/2+7.2);
            const turn=yaw-side*Math.PI/2;
            const roadClearance=roadData.some(route=>route.some((p,j)=>j>0&&distSeg([bx,bz],route[j-1],p)<nearest.roadWidth/2+3));
            if(roadClearance||Math.hypot(bx-start[0],bz-start[1])<8||placedHouses.some(p=>Math.hypot(p.x-bx,p.z-bz)<6.6))continue;
            placedHouses.push({x:bx,z:bz});
            obstacles.push({x:bx,z:bz,rx:1.7,rz:1.7});
            const width=2.8+(i%2)*.22,depth=2.8+(i%3)*.16,height=1.9+(i%3)*.17,ground=-.27;
            const localPoint=(lx,lz)=>[bx+Math.cos(turn)*lx+Math.sin(turn)*lz,bz-Math.sin(turn)*lx+Math.cos(turn)*lz];
            box(bx,ground+.018,bz,spacing*.88,.035,8.2,colors.yard,turn);
            softBox(bx,ground+height*.5,bz,width,height,depth,colors.wall,turn);
            draw(gableRoof,bx,ground+height+.22,bz,width+.45,.78,depth+.42,colors.roof,turn);
            const [frontX,frontZ]=localPoint(0,depth*.51);
            softBox(frontX,ground+.55,frontZ,.48,1.05,.09,[.26,.17,.12],turn);
            const [porchX,porchZ]=localPoint(0,depth*.51+.42);
            softBox(porchX,ground+.17,porchZ,1.15,.14,.76,colors.shoulder,turn);
            for(const windowSide of [-1,1]){
              const [windowX,windowZ]=localPoint(windowSide*.76,depth*.51);
              softBox(windowX,ground+1.02,windowZ,.48,.5,.09,[.23,.38,.39],turn);
              softBox(windowX,ground+1.02,windowZ-.012,.12,.52,.10,[.77,.67,.48],turn);
            }
            const pathLength=Math.max(1.5,nearest.roadWidth/2+7.2-depth/2-nearest.roadWidth/2-.25);
            const [pathX,pathZ]=localPoint(0,depth/2+pathLength/2);
            box(pathX,ground+.045,pathZ,.78,.07,pathLength,colors.shoulder,turn);
          }
        }
      }
    });
    for(let i=0;i<155;i++){
      const x=(hash(i)*202)-101,z=(hash(i+440)*132)-66;
      const nearRoad=roadData.some(r=>r.some((p,j)=>j&&distSeg([x,z],r[j-1],p)<4.3));
      const nearTown=towns.some(t=>Math.hypot(t.pos[0]-x,t.pos[1]-z)<7);
      if(nearRoad||nearTown||x>45)continue;
      tree(x,z,.58+hash(i+800)*.68);
    }
    for(let i=0;i<38;i++){
      const x=hash(i+1700)*194-97,z=hash(i+2300)*126-63;
      const nearRoad=roadData.some(route=>route.some((p,j)=>j&&distSeg([x,z],route[j-1],p)<7));
      const nearTown=towns.some(t=>Math.hypot(t.pos[0]-x,t.pos[1]-z)<11);
      if(nearRoad||nearTown||x>43)continue;
      palm(x,z,.75+hash(i+2900)*.55,i*.73);
    }
    const roadsideTrees=[],streetLamps=[];
    for(let routeIndex=0;routeIndex<roadData.length;routeIndex++)for(let segment=1;segment<roadData[routeIndex].length;segment++){
      const route=roadData[routeIndex],a=route[segment-1],b=route[segment],dx=b[0]-a[0],dz=b[1]-a[1],length=Math.hypot(dx,dz);
      if(length<12)continue;
      const yaw=Math.atan2(dx,dz),nx=dz/length,nz=-dx/length,roadWidth=routeIndex<12?5.4:4.2;
      for(const side of [-1,1])for(let distance=12+(side>0?15:0);distance<length-5;distance+=30){
        const t=distance/length,x=a[0]+dx*t,z=a[1]+dz*t,px=x+nx*side*(roadWidth/2+2.8),pz=z+nz*side*(roadWidth/2+2.8);
        const nearHouse=placedHouses.some(house=>Math.hypot(house.x-px,house.z-pz)<4);
        const repeated=roadsideTrees.some(treePos=>Math.hypot(treePos.x-px,treePos.z-pz)<8);
        const nearRoad=roadData.some((otherRoute,index)=>index!==routeIndex&&otherRoute.some((point,j)=>j>0&&distSeg([px,pz],otherRoute[j-1],point)<4));
        const nearJunction=roadData.some((otherRoute,index)=>index!==routeIndex&&otherRoute.some((point,j)=>j>0&&distSeg([x,z],otherRoute[j-1],point)<8));
        if(!nearHouse&&!repeated&&!nearRoad&&!nearJunction&&!(px>45&&pz>25)&&px<102&&px>-102&&pz<67&&pz>-67){
          roadsideTrees.push({x:px,z:pz});
          tree(px,pz,.95+hash(routeIndex*137+segment*31+distance)*.32);
        }
      }
      for(let distance=10;distance<length-5;distance+=30){
        const t=distance/length,x=a[0]+dx*t,z=a[1]+dz*t,side=((Math.floor(distance/30)+segment)%2)?1:-1;
        const px=x+nx*side*(roadWidth/2+1.1),pz=z+nz*side*(roadWidth/2+1.1);
        const nearCrossing=roadData.some(otherRoute=>otherRoute.some((point,j)=>j>0&&distSeg([px,pz],otherRoute[j-1],point)<2.8));
        const repeated=streetLamps.some(lamp=>Math.hypot(lamp.x-px,lamp.z-pz)<12);
        const nearTree=roadsideTrees.some(treePos=>Math.hypot(treePos.x-px,treePos.z-pz)<4.5);
        if(nearCrossing||repeated||nearTree||px>102||px< -102||pz>67||pz< -67)continue;
        streetLamps.push({x:px,z:pz});
        obstacles.push({x:px,z:pz,r:.24});
        draw(cylinder,px,1.65,pz,.075,3.3,.075,[.34,.32,.27]);
        draw(cylinder,px,.18,pz,.2,.34,.2,[.42,.37,.27]);
        const lampYaw=yaw-side*Math.PI/2,lampX=px+Math.sin(lampYaw)*.52,lampZ=pz+Math.cos(lampYaw)*.52;
        box(lampX,3.08,lampZ,.09,.09,.95,[.34,.32,.27],lampYaw);
        ball(px+Math.sin(lampYaw)*.92,2.98,pz+Math.cos(lampYaw)*.92,.16,.12,.16,[.96,.79,.43]);
      }
    }
    for(const [x,z] of [[-83,27],[-78,-18],[-34,-55],[-8,48],[23,-44],[31,29],[-59,47]]){
      const nearRoad=roadData.some(route=>route.some((p,i)=>i&&distSeg([x,z],route[i-1],p)<7));
      const nearTown=towns.some(t=>Math.hypot(t.pos[0]-x,t.pos[1]-z)<10);
      if(nearRoad||nearTown||x>43)continue;
      box(x,-.245,z,12,.04,8,colors.field);
      for(let row=0;row<8;row++)box(x-5+row*1.4,-.19,z,.07,.08,7.5,colors.crop);
      for(const edge of [-1,1])box(x,-.19,z+edge*4,12,.12,.18,[.43,.38,.24]);
    }
    temple(-16.5,13.5);temple(goal[0],goal[1]);
    bridge();
  }
  function hash(n){const v=Math.sin(n*127.1+311.7)*43758.5453;return v-Math.floor(v);}
  function distSeg(p,a,b){const dx=b[0]-a[0],dz=b[1]-a[1],t=clamp(((p[0]-a[0])*dx+(p[1]-a[1])*dz)/(dx*dx+dz*dz),0,1);return Math.hypot(p[0]-a[0]-t*dx,p[1]-a[1]-t*dz);}
  function isOnRoad(x,z){return roadData.some(route=>route.some((p,i)=>i>0&&distSeg([x,z],route[i-1],p)<2.7));}
  function moveWithCollisions(x,z,dx,dz,radius,withNpcs){
    const distance=Math.hypot(dx,dz),steps=Math.max(1,Math.ceil(distance/.3));
    let hit=false;
    for(let i=0;i<steps;i++){
      const next=resolvePosition(x+dx/steps,z+dz/steps,radius,withNpcs);
      x=next.x;z=next.z;
      if(next.hit){hit=true;break;}
    }
    return{x,z,hit};
  }
  function resolvePosition(x,z,radius,withNpcs){
    let hit=false;
    for(let pass=0;pass<2;pass++)for(const o of obstacles){
      if(o.r!==undefined){let dx=x-o.x,dz=z-o.z,d=Math.hypot(dx,dz);if(d<radius+o.r){if(d<.001){dx=1;dz=0;d=1;}const push=radius+o.r-d;x+=dx/d*push;z+=dz/d*push;hit=true;}}
      else{const qx=clamp(x,o.x-o.rx,o.x+o.rx),qz=clamp(z,o.z-o.rz,o.z+o.rz);let dx=x-qx,dz=z-qz,d=Math.hypot(dx,dz);if(d<radius){if(d<.001){const edges=[{d:x-(o.x-o.rx),x:o.x-o.rx-radius,z},{d:o.x+o.rx-x,x:o.x+o.rx+radius,z},{d:z-(o.z-o.rz),x,z:o.z-o.rz-radius},{d:o.z+o.rz-z,x,z:o.z+o.rz+radius}].sort((a,b)=>a.d-b.d);x=edges[0].x;z=edges[0].z;}else{x+=dx/d*(radius-d);z+=dz/d*(radius-d);}hit=true;}}
    }
    if(withNpcs){
      for(const n of npcs){const nx=n.worldX??n.x,nz=n.worldZ??n.z,dx=x-nx,dz=z-nz,d=Math.hypot(dx,dz),minimum=radius+.48;if(d<minimum){const safe=d||1;x+=(dx||1)/safe*(minimum-d);z+=(dz||0)/safe*(minimum-d);hit=true;}}
      if(!player.inCar){const dx=x-car.x,dz=z-car.z,d=Math.hypot(dx,dz),minimum=radius+1.45;if(d<minimum){const safe=d||1;x+=(dx||1)/safe*(minimum-d);z+=(dz||0)/safe*(minimum-d);hit=true;}}
    }
    if(x< -104||x>104||z< -69||z>69)hit=true;
    return{x:clamp(x,-104,104),z:clamp(z,-69,69),hit};
  }
  function tree(x,z,s){
    obstacles.push({x,z,r:.34*s});
    draw(cylinder,x,.88*s-.27,z,.16*s,1.76*s,.16*s,colors.trunk);
    const foliage=[[-.38,1.66,.02,.67,.72,.65],[.38,1.72,.08,.68,.76,.68],[0,2.12,0,.76,.78,.74],[.05,1.72,-.42,.63,.68,.62],[.12,1.75,.43,.66,.7,.64]];
    for(let i=0;i<foliage.length;i++){
      const [ox,oy,oz,sx,sy,sz]=foliage[i];
      ball(x+ox*s,-.27+oy*s,z+oz*s,sx*s,sy*s,sz*s,[.19+i*.012,.34+i*.012,.20+i*.008]);
    }
  }
  function palm(x,z,s,phase=0){
    obstacles.push({x,z,r:.3*s});
    const ground=isOnRoad(x,z)?-.11:-.27,top=ground+4.5*s;
    for(let i=0;i<3;i++){
      const t=(i+.5)/3;
      draw(cylinder,x+Math.sin(phase)*t*.18*s,ground+(i+.5)*1.5*s,z+Math.cos(phase)*t*.18*s,.12*s*(1-t*.35),1.55*s,.12*s*(1-t*.35),[.37,.29,.18],phase);
    }
    const crownX=x+Math.sin(phase)*.18*s,crownZ=z+Math.cos(phase)*.18*s;
    for(let i=0;i<8;i++){
      const angle=phase+i*Math.PI/4,cx=crownX+Math.sin(angle)*.52*s,cz=crownZ+Math.cos(angle)*.52*s;
      draw(sphere,cx,top-.42*s,cz,.16*s,.10*s,1.12*s,[.17,.34,.16],angle,.36);
    }
    for(let i=0;i<3;i++)ball(crownX+(i-1)*.13*s,top-.1*s,crownZ,.09*s,.1*s,.09*s,[.31,.43,.18]);
  }
  function temple(x,z){obstacles.push({x,z,rx:2.25,rz:2.1});box(x,.38,z,3.2,1.3,2.8,colors.wall);for(let i=0;i<4;i++)box(x,.63+i*.55,z,2.8-i*.5,.45,2.5-i*.45,i%2?colors.roof:colors.gold);draw(cylinder,x,2.08,z,.16,.6,.16,colors.gold);}
  function bridge(){for(let i=0;i<9;i++){const t=i/8,x=44+t*15,z=31+t*3.75;box(x,-.025,z,2.05,.18,5.2,colors.wall);box(x,.25,z-2.45,.13,.75,.13,colors.line);box(x,.25,z+2.45,.13,.75,.13,colors.line);}}
  function person(x,z,color,phase=0,scale=1,yaw=0){const bob=Math.sin(elapsed*3+phase)*.055,leg=Math.sin(elapsed*4+phase)*.15,floor=isOnRoad(x,z)?-.11:-.27;
    const point=(lx,lz)=>[x+Math.cos(yaw)*lx+Math.sin(yaw)*lz,z-Math.sin(yaw)*lx+Math.cos(yaw)*lz];
    const torso=point(0,0),head=point(0,0),leftArm=point(-.34*scale,0),rightArm=point(.34*scale,0),leftLeg=point(Math.sin(leg)*.2*scale,0),rightLeg=point(-Math.sin(leg)*.2*scale,0);
    box(torso[0],floor+.80*scale+bob,torso[1],.55*scale,.95*scale,.36*scale,color,yaw+leg*.25);
    ball(head[0],floor+1.48*scale+bob,head[1],.24*scale,.27*scale,.24*scale,colors.skin);
    box(leftArm[0],floor+.78*scale,leftArm[1],.16*scale,.73*scale,.16*scale,color,yaw+leg);
    box(rightArm[0],floor+.78*scale,rightArm[1],.16*scale,.73*scale,.16*scale,color,yaw-leg);
    box(leftLeg[0],floor+.16*scale,leftLeg[1],.18*scale,.32*scale,.2*scale,[.20,.22,.20],yaw+leg);
    box(rightLeg[0],floor+.16*scale,rightLeg[1],.18*scale,.32*scale,.2*scale,[.20,.22,.20],yaw-leg);
  }
  function vehicle(x,z,yaw,steerAngle=0){
    const floor=isOnRoad(x,z)?-.11:-.27;
    const point=(lx,lz)=>[x+Math.cos(yaw)*lx+Math.sin(yaw)*lz,z-Math.sin(yaw)*lx+Math.cos(yaw)*lz];
    const part=(lx,y,lz,sx,sy,sz,color,pitch=0)=>{const p=point(lx,lz);softBox(p[0],y,p[1],sx,sy,sz,color,yaw,pitch);};
    const shape=(mesh,lx,y,lz,sx,sy,sz,color,steer=0)=>{const p=point(lx,lz);draw(mesh,p[0],y,p[1],sx,sy,sz,color,yaw+steer);};
    const detailBall=(lx,y,lz,sx,sy,sz,color)=>{const p=point(lx,lz);ball(p[0],y,p[1],sx,sy,sz,color);};
    detailBall(0,floor+.12,0,.97,.07,1.86,[.12,.14,.13]);
    part(0,floor+.45,0,1.58,.3,3.12,colors.dark);
    shape(carBody,0,floor+.68,0,1.92,.66,3.72,colors.car);
    shape(carCabin,0,floor+1.22,-.10,1.48,.62,1.72,colors.car);
    part(0,floor+1.37,.56,1.32,.42,.075,colors.glass,.55);
    part(0,floor+1.40,-.78,1.29,.34,.075,colors.glass,-.45);
    for(const side of [-1,1]){
      part(side*.77,floor+1.24,-.52,.075,.39,.50,colors.glass);
      part(side*.77,floor+1.24,.26,.075,.39,.45,colors.glass);
      part(side*.77,floor+1.25,-.11,.09,.43,.075,colors.car);
      part(side*.80,floor+1.08,.86,.16,.13,.22,colors.carLight);
      part(side*.82,floor+1.04,-.82,.12,.11,.17,colors.dark);
      part(side*.87,floor+.78,-.05,.055,.055,.19,colors.chrome);
      part(side*.96,floor+1.14,.73,.25,.12,.19,colors.car);
      part(side*.95,floor+1.20,.75,.18,.08,.13,colors.dark);
    }
    part(0,floor+.71,1.91,1.54,.22,.17,colors.dark);
    part(0,floor+.72,-1.91,1.62,.2,.18,colors.dark);
    part(0,floor+.74,1.91,.76,.25,.065,colors.chrome);
    part(0,floor+.79,-1.92,.48,.14,.05,colors.white);
    for(const side of [-1,1]){
      part(side*.63,floor+.80,1.83,.38,.22,.07,colors.white);
      part(side*.63,floor+.79,-1.81,.39,.22,.075,[.70,.035,.018]);
    }
    part(0,floor+.79,1.92,.68,.23,.045,colors.dark);
    for(let i=0;i<5;i++)part(-.25+i*.125,floor+.79,1.95,.035,.17,.025,colors.chrome);
    for(const side of [-1,1])for(const end of [-1,1]){
      const wy=floor+.38,steer=end>0?steerAngle:0;
      shape(wheelMesh,side*.96,wy,end*1.14,.38,.43,.43,colors.rubber,steer);
      shape(wheelMesh,side*.985,wy,end*1.14,.385,.22,.22,colors.chrome,steer);
      detailBall(side*1.11,wy,end*1.14,.06,.075,.075,colors.dark);
    }
    part(0,floor+.50,-.18,.12,.11,.32,colors.seat);
    detailBall(0,floor+1.02,-.20,.14,.16,.14,colors.skin);
    part(0,floor+.88,-.21,.31,.29,.25,[.18,.36,.66]);
  }
  let cameraX=start[0],cameraZ=start[1]-12,cameraY=5.2;
  function resize(){
    const rect=canvas.getBoundingClientRect(),dpr=Math.min(devicePixelRatio||1,2);
    const width=Math.max(1,Math.floor(rect.width*dpr)),height=Math.max(1,Math.floor(rect.height*dpr));
    if(canvas.width!==width||canvas.height!==height){canvas.width=width;canvas.height=height;}
  }
  new ResizeObserver(resize).observe(canvas);resize();
  function render(){
    const w=canvas.width,h=canvas.height;gl.viewport(0,0,w,h);gl.enable(gl.DEPTH_TEST);gl.clearColor(.59,.72,.77,1);gl.clear(gl.COLOR_BUFFER_BIT|gl.DEPTH_BUFFER_BIT);
    if(!worldBuilt){buildingWorld=true;buildWorld();buildingWorld=false;worldBuilt=true;}
    const cinematicNow=!started||cutsceneUntil>performance.now();
    const viewYaw=player.inCar?player.yaw:cameraYaw;
    const fwdX=Math.sin(viewYaw),fwdZ=Math.cos(viewYaw);
    const targetX=player.x+fwdX*2,targetZ=player.z+fwdZ*2;
    const orbit=elapsed*.14;
    const cameraDistance=player.inCar?10:8.5;
    const desiredX=cinematicNow?player.x+Math.sin(orbit)*11:player.x-fwdX*cameraDistance*Math.cos(cameraPitch);
    const desiredZ=cinematicNow?player.z-Math.cos(orbit)*11:player.z-fwdZ*cameraDistance*Math.cos(cameraPitch);
    const focusX=cutsceneTarget?cutsceneTarget[0]:targetX,focusZ=cutsceneTarget?cutsceneTarget[1]:targetZ;
    cameraX+=(desiredX-cameraX)*.08;cameraZ+=(desiredZ-cameraZ)*.08;
    const desiredY=cinematicNow?9:1.1+cameraDistance*Math.sin(cameraPitch);
    cameraY+=(desiredY-cameraY)*.08;
    eye=[cameraX,cameraY,cameraZ];viewProj=mul(persp(Math.PI/3,w/h,.1,260),look(eye,[focusX,1.1,focusZ]));
    gl.uniform3fv(loc.eye,eye);
    staticDraws.forEach(item=>drawMesh(item.m,item.mod,item.color));
    npcs.forEach((n,i)=>{const wander=resolvePosition(n.x+Math.sin(elapsed*.22+i*2)*.75,n.z+Math.cos(elapsed*.18+i*1.7)*.65,.3,false);n.worldX=wander.x;n.worldZ=wander.z;person(n.worldX,n.worldZ,n.color,i);});
    if(player.inCar)vehicle(player.x,player.z,player.yaw,player.steer);else{vehicle(car.x,car.z,car.yaw);person(player.x,player.z,[.18,.33,.70],0,1.06,player.yaw);}
    const beacon=missionMarker();
    if(beacon){draw(cylinder,beacon[0],.1+Math.sin(elapsed*3)*.1,beacon[1],.16,.2,.16,colors.gold);draw(sphere,beacon[0],1.8+Math.sin(elapsed*2)*.25,beacon[1],.48,.48,.48,colors.gold);}
    drawMini();updateHud();
  }
  function drawMini(){
    const w=mini.clientWidth,h=mini.clientHeight,dpr=Math.min(devicePixelRatio||1,2);if(mini.width!==Math.floor(w*dpr)||mini.height!==Math.floor(h*dpr)){mini.width=Math.floor(w*dpr);mini.height=Math.floor(h*dpr);}
    mctx.setTransform(dpr,0,0,dpr,0,0);mctx.clearRect(0,0,w,h);mctx.fillStyle="#647a5c";mctx.fillRect(0,0,w,h);
    mctx.fillStyle="#477b88";mctx.fillRect(w*.73,0,w*.27,h);
    const xy=p=>[(100-p[0])/200*w,(p[1]+70)/140*h];
    roadData.forEach(r=>{mctx.beginPath();r.forEach((p,i)=>{const q=xy(p);i?mctx.lineTo(q[0],q[1]):mctx.moveTo(q[0],q[1]);});mctx.strokeStyle="#ddcda5";mctx.lineWidth=1.4;mctx.stroke();});
    towns.forEach(t=>{const p=xy(t.pos);mctx.fillStyle=t.kind==="city"?"#f4d38b":"#ded9c8";mctx.beginPath();mctx.arc(p[0],p[1],t.kind==="city"?2.5:1.6,0,Math.PI*2);mctx.fill();});
    const p=xy([player.x,player.z]),yaw=player.inCar?player.yaw:player.yaw;
    mctx.save();mctx.translate(p[0],p[1]);mctx.rotate(-yaw);mctx.fillStyle="#fff";mctx.beginPath();mctx.moveTo(0,-5);mctx.lineTo(3.5,4);mctx.lineTo(0,2);mctx.lineTo(-3.5,4);mctx.closePath();mctx.fill();mctx.restore();
    const marker=missionMarker();if(marker){const q=xy(marker);mctx.fillStyle="#f5dc58";mctx.beginPath();mctx.arc(q[0],q[1],2.5,0,Math.PI*2);mctx.fill();}
  }
  function missionMarker(){
    if(mission===0&&missionStage===1)return letter;
    if(mission===0&&missionStage===2)return goal;
    if(mission===1&&missionStage===1)return teaParcel;
    if(mission===1&&missionStage===2)return selviSpot;
    if(mission===2&&missionStage===1)return lostNet;
    if(mission===2&&missionStage===2)return arunSpot;
    return null;
  }
  function updateHud(){
    root.querySelector(".play-area").classList.toggle("walking",!player.inCar);
    const nearest=towns.reduce((best,t)=>Math.hypot(t.pos[0]-player.x,t.pos[1]-player.z)<Math.hypot(best.pos[0]-player.x,best.pos[1]-player.z)?t:best,towns[0]);
    $("location-label").textContent=nearest.name;$("speed-readout").textContent=String(Math.round(Math.abs(player.speed)*3.6));$("world-status").textContent=mission>=3?"பணிகள் நிறைவு · திறந்த உலகம்":"3D உலகம் · 9 கதாபாத்திரங்கள்";
    const titles=["பாட்டியின் கடிதம்","தேநீர்க் கடையின் பொட்டலம்","மீனவரின் வலை"];
    const objectives=[
      ["மீனாவிடம் F அழுத்திப் பேசு; கடிதத்தைக் கண்டுபிடி.","மஞ்சள் குறியை அடைந்து கடிதத்தை எடு.","கிழக்குக் கடற்கரை வழியாக ராமேஸ்வரம் சென்று கடிதத்தை ஒப்படை."],
      ["முருகனிடம் பேசு; அவர் ஒரு உதவி கேட்கிறார்.","தேநீர்க் கடை அருகிலுள்ள பொட்டலத்தை எடு.","பொட்டலத்தைச் செல்வியிடம் கொண்டு சேர்."],
      ["ராமேஸ்வரத்தில் மீனவர் அருணிடம் பேசு.","கடற்கரையில் காணாமல் போன வலையைத் தேடு.","வலையை அருணிடம் திருப்பிக் கொடு."]
    ];
    $("mission-title").textContent=mission>=3?"பணிகள் நிறைவு!":titles[mission];
    $("mission-copy").textContent=mission>=3?"மூன்று பணிகளையும் முடித்துவிட்டாய். தமிழ்நாட்டைத் தொடர்ந்து சுற்றிப் பார்.":objectives[mission][missionStage];
    $("hint").textContent=!player.inCar?"WASD — நகர்வு · மவுஸ் கிளிக் செய்து பார்வையைத் திருப்பு · E — காரில் ஏறு":"W / ↑ — முன் · S / ↓ — பின் · A / ← — இடம் · D / → — வலம் · Space — பிரேக்";
  }
  function showCutscene(title,text,target){
    $("cutscene-title").textContent=title;$("cutscene-copy").textContent=text;
    $("cutscene").classList.remove("hidden");cutsceneUntil=performance.now()+5500;cutsceneTarget=target||null;
  }
  function finishCutscene(){$("cutscene").classList.add("hidden");cutsceneUntil=0;cutsceneTarget=null;}
  function completeMission(title,text){
    mission++;missionStage=0;
    showCutscene(title,text,[player.x,player.z]);
  }
  function talk(){
    if(cutsceneUntil>performance.now())return;
    if(dialogOpen){closeDialogue();return;}
    const nearest=npcs.map(n=>({...n,d:Math.hypot((n.worldX??n.x)-player.x,(n.worldZ??n.z)-player.z)})).sort((a,b)=>a.d-b.d)[0];
    if(nearest&&nearest.d<4.8){
      if(mission===0&&missionStage===0&&nearest.name==="மீனா"){missionStage=1;showCutscene("பாட்டியின் கடைசி ஆசை","மீனா: பாட்டியின் கடிதத்தை ராமேஸ்வரத்தில் சேர்த்துவிடு. மதுரை கோவிலருகே தேடு.",[nearest.x,nearest.z]);return;}
      if(mission===1&&missionStage===0&&nearest.name==="முருகன்"){missionStage=1;showCutscene("தேநீர்க் கடையின் உதவி","முருகன்: இந்தத் தேநீர்ப் பொட்டலத்தைப் பள்ளி வாசலில் காத்திருக்கும் செல்வியிடம் கொடுத்துவிடு.",[nearest.x,nearest.z]);return;}
      if(mission===1&&missionStage===2&&nearest.name==="செல்வி"){completeMission("ஒரு சிறிய நன்றி","செல்வி: ரொம்ப நன்றி! இப்போது ராமேஸ்வரத்தில் அருணுக்கு ஒரு உதவி தேவைப்படுகிறது.",[nearest.x,nearest.z]);return;}
      if(mission===2&&missionStage===0&&nearest.name==="அருண்"){missionStage=1;showCutscene("காணாமல் போன வலை","அருண்: என் மீன்பிடி வலை கடற்கரையில் தொலைந்துவிட்டது. பார்த்தால் திருப்பிக் கொடு.",[nearest.x,nearest.z]);return;}
      if(mission===2&&missionStage===2&&nearest.name==="அருண்"){completeMission("கடற்கரையின் நண்பன்","அருண்: வலையைக் கண்டுபிடித்ததற்கு நன்றி! உன் பயணம் இனிதாக அமையட்டும்.",[nearest.x,nearest.z]);return;}
      showDialogue(nearest.role+" · "+nearest.name,nearest.line);
    }
    else showDialogue("பயணக் குறிப்பு","அருகிலுள்ள மனிதரிடம் சென்று F அழுத்திப் பேசு. ஊருக்குள் பல கதாபாத்திரங்கள் இருக்கிறார்கள்.");
  }
  function showDialogue(who,text){$("speaker").textContent=who;$("dialogue-text").textContent=text;$("dialogue").classList.remove("hidden");dialogOpen=true;}
  function closeDialogue(){$("dialogue").classList.add("hidden");dialogOpen=false;}
  function action(){
    if(!started||cutsceneUntil>performance.now())return;if(dialogOpen){closeDialogue();return;}
    if(!player.inCar){if(Math.hypot(player.x-car.x,player.z-car.z)<4){player.inCar=true;player.x=car.x;player.z=car.z;player.yaw=car.yaw;cameraYaw=car.yaw;player.speed=0;player.steer=0;}else showDialogue("பயணக் குறிப்பு","உன் சிவப்புக் கார் அருகில் சென்றால் E அழுத்தி ஏறு.");}
    else{const exit=resolvePosition(player.x-Math.cos(player.yaw)*2,player.z+Math.sin(player.yaw)*2,.38,true);if(Math.hypot(exit.x-player.x,exit.z-player.z)<1){showDialogue("பயணக் குறிப்பு","இங்கே இறங்க இடமில்லை; சற்று முன்னால் நகர்ந்து முயற்சி செய்.");return;}player.inCar=false;player.speed=0;player.vx=player.vz=0;player.x=exit.x;player.z=exit.z;cameraYaw=player.yaw;}
  }
  function startGame(){started=true;player.speed=0;keys.clear();$("intro").classList.add("hidden");}
  function update(dt){
    elapsed+=dt;
    if(cutsceneUntil&&performance.now()>=cutsceneUntil)finishCutscene();
    if(!started||cutsceneUntil>performance.now()||dialogOpen)return;
    const f=keys.has("w")||keys.has("arrowup"),b=keys.has("s")||keys.has("arrowdown"),l=keys.has("a")||keys.has("arrowleft"),r=keys.has("d")||keys.has("arrowright");
    if(player.inCar){
      const roadGrip=isOnRoad(player.x,player.z),engineForce=roadGrip?13:7.5;
      if(f)player.speed+=engineForce*dt;
      if(b){if(player.speed>1)player.speed-=23*dt;else player.speed-=8*dt;}
      player.speed*=Math.pow(keys.has(" ")?0.84:(roadGrip ? 0.992 : 0.976),dt*60);player.speed=clamp(player.speed,-7,roadGrip?26:13);
      const steering=((r?1:0)-(l?1:0)),speedFactor=.28+Math.min(Math.abs(player.speed)/9,1.7);
      player.steer+=( -steering*.42-player.steer)*(1-Math.exp(-10*dt));
      player.yaw-=steering*dt*(roadGrip?1.25:.8)*speedFactor*(player.speed<0?-1:1);
      const next=moveWithCollisions(player.x,player.z,Math.sin(player.yaw)*player.speed*dt,Math.cos(player.yaw)*player.speed*dt,1.18,true);
      player.x=next.x;player.z=next.z;
      if(next.hit){player.speed=Math.abs(player.speed)>7?-player.speed*.22:0;player.vx=player.vz=0;}
      car.x=player.x;car.z=player.z;car.yaw=player.yaw;
    }else{
      const forward=(f?1:0)-(b?1:0),strafe=(r?1:0)-(l?1:0),length=Math.hypot(forward,strafe);
      const normalizedForward=length?forward/length:0,normalizedStrafe=length?strafe/length:0;
      const targetX=(Math.sin(cameraYaw)*normalizedForward+Math.cos(cameraYaw)*normalizedStrafe)*4.8;
      const targetZ=(Math.cos(cameraYaw)*normalizedForward-Math.sin(cameraYaw)*normalizedStrafe)*4.8;
      const traction=1-Math.exp(-(length?10:13)*dt);
      player.vx+=(targetX-player.vx)*traction;player.vz+=(targetZ-player.vz)*traction;
      if(length)player.yaw=Math.atan2(player.vx,player.vz);
      const next=moveWithCollisions(player.x,player.z,player.vx*dt,player.vz*dt,.38,true);
      player.x=next.x;player.z=next.z;if(next.hit){player.vx*=.12;player.vz*=.12;}
      player.speed=Math.hypot(player.vx,player.vz);
    }
    if(mission===0&&missionStage===1&&Math.hypot(player.x-letter[0],player.z-letter[1])<1.7){
      missionStage=2;showDialogue("பணி புதுப்பிப்பு","கடிதம் கிடைத்தது! இப்போது அதை ராமேஸ்வரத்திற்குக் கொண்டு செல்.");
    }
    if(mission===0&&missionStage===2&&Math.hypot(player.x-goal[0],player.z-goal[1])<2.2){
      completeMission("கடிதம் சேர்ந்துவிட்டது","பாட்டியின் கடைசி ஆசையை நிறைவேற்றிவிட்டாய். மதுரையில் முருகனுக்கு ஒரு பொட்டலத்தைச் சேர்க்க உதவி செய்.",[player.x,player.z]);
    }
    if(mission===1&&missionStage===1&&Math.hypot(player.x-teaParcel[0],player.z-teaParcel[1])<1.7){
      missionStage=2;showDialogue("பணி புதுப்பிப்பு","தேநீர்ப் பொட்டலம் கிடைத்தது. இப்போது அதைச் செல்வியிடம் கொண்டு சேர்.");
    }
    if(mission===2&&missionStage===1&&Math.hypot(player.x-lostNet[0],player.z-lostNet[1])<1.7){
      missionStage=2;showDialogue("பணி புதுப்பிப்பு","வலை கிடைத்துவிட்டது! அதை அருணிடம் திருப்பிக் கொடு.");
    }
  }
  function frame(now){const dt=Math.min((now-last)/1000||0,.04);last=now;update(dt);render();requestAnimationFrame(frame);}
  requestAnimationFrame(frame);
  canvas.addEventListener("click",()=>{
    if(!started||player.inCar||dialogOpen||cutsceneUntil>performance.now()||!canvas.requestPointerLock)return;
    const request=canvas.requestPointerLock();
    if(request&&request.catch)request.catch(()=>{});
  });
  canvas.addEventListener("pointerdown",e=>{
    if(e.button!==2||!started||player.inCar)return;
    e.preventDefault();mouseLookDrag=true;canvas.setPointerCapture(e.pointerId);
  });
  const stopMouseLook=()=>{mouseLookDrag=false;};
  canvas.addEventListener("pointerup",stopMouseLook);canvas.addEventListener("pointercancel",stopMouseLook);canvas.addEventListener("lostpointercapture",stopMouseLook);
  canvas.addEventListener("contextmenu",e=>e.preventDefault());
  document.addEventListener("mousemove",e=>{
    if(!started||player.inCar||dialogOpen||cutsceneUntil>performance.now())return;
    if(document.pointerLockElement!==canvas&&!mouseLookDrag)return;
    cameraYaw-=e.movementX*.0025;
    cameraPitch=clamp(cameraPitch+e.movementY*.002,.18,.86);
  });
  document.addEventListener("keydown",e=>{const k=e.key.toLowerCase();if(["arrowup","arrowdown","arrowleft","arrowright"," "].includes(k))e.preventDefault();keys.add(k);if(k==="e"&&!e.repeat)action();if(k==="f"&&!e.repeat)talk();if(k==="enter"&&!started)startGame();if(k==="escape"&&dialogOpen)closeDialogue();});
  document.addEventListener("keyup",e=>keys.delete(e.key.toLowerCase()));window.addEventListener("blur",()=>{keys.clear();mouseLookDrag=false;});
  root.querySelector("#start-game").addEventListener("click",startGame);root.querySelector("#dialogue-next").addEventListener("click",closeDialogue);
  root.querySelector("#cutscene-skip").addEventListener("click",finishCutscene);
  root.querySelectorAll("[data-key]").forEach(button=>{const k=button.dataset.key.toLowerCase();button.addEventListener("pointerdown",e=>{e.preventDefault();button.setPointerCapture(e.pointerId);if(k==="e")action();else if(k==="f")talk();else keys.add(k);});const clear=()=>keys.delete(k);button.addEventListener("pointerup",clear);button.addEventListener("pointercancel",clear);button.addEventListener("lostpointercapture",clear);});
  $("intro").addEventListener("click",e=>{if(e.target.id!=="start-game")startGame();});
  function cinematic(){if(started)return;const line=introLines[introFrame%introLines.length];$("intro-title").textContent=line[0];$("intro-copy").textContent=line[1];$("intro-progress").style.width=((introFrame+1)/introLines.length*100)+"%";$("intro").classList.add("cinematic");introFrame++;if(introFrame<introLines.length)setTimeout(cinematic,2500);}
  setTimeout(cinematic,500);
}
"""

game = st.components.v2.component(
    "tamil_nadu_open_world_3d",
    html=GAME_HTML,
    css=GAME_CSS,
    js=GAME_JS,
)

game(key="tamil-nadu-game", width="stretch", height=760)
