var _=new Map,Q=null,$=(q)=>q.replace(/\[([^\]\n]+)\]\(https?:\/\/\1\)/g,"$1"),E=(q)=>{let j=$(q.trim());if(/^\s*<!doctype\s+html|^\s*<html[\s>]/i.test(j))return j;if(/^\s*<svg[\s>]/i.test(j))return Y(j,!0);return Y(j,!1)},Y=(q,j)=>`<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  html, body { margin: 0; padding: 0; height: 100%; background: #fff; color: #111; font-family: system-ui, -apple-system, sans-serif; }
  ${j?"body { display: flex; align-items: center; justify-content: center; padding: 24px; box-sizing: border-box; } svg { max-width: 100%; max-height: 100%; }":"body { padding: 16px; box-sizing: border-box; }"}
  #__genos_err { position: fixed; inset: 0; background: #1a0000; color: #ff6464; padding: 24px; font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 13px; line-height: 1.6; white-space: pre-wrap; word-break: break-word; overflow: auto; display: none; z-index: 999999; }
  #__genos_err.show { display: block; }
  #__genos_err h2 { margin: 0 0 12px; font-size: 14px; color: #ff8c8c; font-weight: 600; }
</style>
<script>
  // Surface any uncaught error / module error / promise rejection visibly,
  // instead of letting the iframe stay silently black. This makes broken
  // generated code self-diagnose.
  (function() {
    let div;
    const show = (msg) => {
      div = div || (() => { const d = document.createElement('div'); d.id = '__genos_err'; d.innerHTML = '<h2>Preview error</h2><pre></pre>'; document.body && document.body.appendChild(d); return d })()
      if (!div.parentNode) document.body && document.body.appendChild(div);
      div.classList.add('show');
      div.querySelector('pre').textContent = (div.querySelector('pre').textContent || '') + msg + '\\n\\n';
    };
    window.addEventListener('error', e => show((e.error && e.error.stack) || e.message || 'Unknown error'));
    window.addEventListener('unhandledrejection', e => show('Unhandled rejection: ' + (e.reason && e.reason.stack || e.reason || '')));
  })();
</script>
</head>
<body>
${q}
</body>
</html>`,P=(q)=>{if(Q)L();let j=document.createElement("div");j.className="preview-modal__overlay";let D=document.createElement("div");D.className="preview-modal";let z=document.createElement("div");z.className="preview-modal__header";let T=document.createElement("div");T.className="preview-modal__title",T.textContent="Preview";let F=document.createElement("button");F.className="preview-modal__btn",F.title="View source",F.innerHTML='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>';let I=document.createElement("button");I.className="preview-modal__btn preview-modal__close",I.title="Close (Esc)",I.innerHTML='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',z.append(T,F,I);let O=document.createElement("div");O.className="preview-modal__body";let G=document.createElement("iframe");G.className="preview-modal__iframe",G.setAttribute("sandbox","allow-scripts"),G.setAttribute("allow","fullscreen; autoplay; gamepad"),G.setAttribute("srcdoc",E(q)),O.append(G);let J=document.createElement("pre");J.className="preview-modal__source",J.textContent=q,J.style.display="none",O.append(J),D.append(z,O),j.append(D),document.body.append(j),requestAnimationFrame(()=>j.classList.add("preview-modal__overlay--open"));let L=()=>{if(!Q)return;j.classList.remove("preview-modal__overlay--open"),setTimeout(()=>j.remove(),180),document.removeEventListener("keydown",X),Q=null},X=(U)=>{if(U.key==="Escape")L()};document.addEventListener("keydown",X),j.addEventListener("click",(U)=>{if(U.target===j)L()}),I.addEventListener("click",L);let N=!1;F.addEventListener("click",()=>{N=!N,G.style.display=N?"none":"block",J.style.display=N?"block":"none",F.classList.toggle("preview-modal__btn--active",N)}),Q={overlay:j,close:L}},R=(q,j)=>{_.set(q,j)},Z=!1,W=()=>{if(Z)return;Z=!0,document.addEventListener("click",(q)=>{let j=q.target.closest(".preview-pill");if(!j)return;let D=j.dataset.previewId,z=_.get(D);if(z)P(z)})},A=(q)=>{if(!q)return[];let j=/```genos-preview\s*\n([\s\S]*?)```/g,D=[],z;while((z=j.exec(q))!==null)D.push(z[1]);return D};
export{P as e,R as f,W as g,A as h};
