var c=(n,a={},s=[])=>{let t=document.createElement(n);for(let[e,r]of Object.entries(a))if(e==="className")t.className=r;else if(e==="onclick")t.addEventListener("click",r);else t.setAttribute(e,r);for(let e of s)t.append(typeof e==="string"?document.createTextNode(e):e);return t};
export{c as d};
