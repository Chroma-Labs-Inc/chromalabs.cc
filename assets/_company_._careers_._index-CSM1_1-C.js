import{r as e}from"./rolldown-runtime-QTnfLwEv.js";import{A as t,j as n,n as r}from"./chunk-62JRHF6Z-Dq1aAwXd.js";import{N as i,_ as a,a as o,b as s,c,d as l,f as u,g as d,h as f,l as p,o as m,p as h,s as g,t as _,u as v}from"./createLucideIcon-CjcLMg3u.js";import{n as y}from"./emotion-react.browser.esm-D66BJTCW.js";import{n as b,t as x}from"./menu-CrGbFF4G.js";var S=e(n(),1),C=_(`briefcase`,[[`path`,{d:`M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16`,key:`jecpp`}],[`rect`,{width:`20`,height:`14`,x:`2`,y:`6`,rx:`2`,key:`i6l2r4`}]]),w=t(function(){let e=(0,S.useRef)(null);i.ref_lambdaBackground=e;let t=(0,S.useRef)(null);return i.ref_chromaNavCrystal=t,y(S.Fragment,{},y(a,{css:{background:`transparent`,color:`white`,fontFamily:`Inter, sans-serif`,"--default-font-family":`Inter, sans-serif`,position:`relative`}},y(a,{css:{position:`fixed`,top:`0`,left:`0`,width:`100vw`,height:`100vh`,zIndex:`-1`,background:`#07070A`}}),y(a,{css:{position:`fixed`,top:`12%`,left:`50%`,transform:`translateX(-50%)`,width:`65vw`,height:`65vw`,background:`radial-gradient(circle, rgba(223, 188, 97, 0.07) 0%, transparent 65%)`,zIndex:`1`,filter:`blur(90px)`,borderRadius:`50%`,pointerEvents:`none`}}),y(a,{css:{position:`fixed`,top:`35%`,left:`-10%`,width:`55vw`,height:`55vw`,background:`radial-gradient(circle, rgba(168, 85, 247, 0.05) 0%, transparent 70%)`,zIndex:`1`,filter:`blur(110px)`,borderRadius:`50%`,pointerEvents:`none`}}),y(a,{css:{position:`fixed`,bottom:`-10%`,right:`-10%`,width:`60vw`,height:`60vw`,background:`radial-gradient(circle, rgba(6, 182, 212, 0.04) 0%, transparent 70%)`,zIndex:`1`,filter:`blur(110px)`,borderRadius:`50%`,pointerEvents:`none`}}),y(`canvas`,{css:{position:`fixed`,top:`0`,left:`0`,width:`100vw`,height:`100vh`,zIndex:`2`,pointerEvents:`none`},id:`lambdaBackground`,ref:e}),y(b,{},y(`script`,{},`
if (!window.__chromaCanvasInitialized) {
    window.__chromaCanvasInitialized = true;
    
    function initCanvas() {
        let canvas = document.getElementById("lambdaBackground");
        if (!canvas) {
            requestAnimationFrame(initCanvas);
            return;
        }
        let ctx = canvas.getContext("2d");

        function resize() {
            if (!canvas) return;
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener("resize", resize);
        resize();
        
        const GRID_SIZE = 60;
        const SPEED = 2.5;
        let threads = [];
        
        const PALETTE = [
            { stroke: "212, 175, 55", glow: "#DFBC61" }, // Gold
            { stroke: "56, 189, 248", glow: "#38BDF8" }, // Electric Cyan
            { stroke: "245, 158, 11", glow: "#F59E0B" }, // Amber
            { stroke: "192, 132, 252", glow: "#C084FC" }, // Lilac
        ];

        // Layer 1: Distant micro-dust specks
        const DUST_COUNT = 35;
        let dust = [];
        function initDust() {
            dust = [];
            for (let i = 0; i < DUST_COUNT; i++) {
                dust.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    vx: (Math.random() - 0.5) * 0.12,
                    vy: -0.06 - Math.random() * 0.15,
                    r: 0.5 + Math.random() * 0.7,
                    alpha: 0.15 + Math.random() * 0.35,
                    glow: Math.random() > 0.45 ? "#DFBC61" : (Math.random() > 0.5 ? "#38BDF8" : "#C084FC")
                });
            }
        }

        // Layer 3: Foreground Camera Focal Bokeh Orbs (soft out-of-focus optics)
        const BOKEH_COUNT = 8;
        let bokehOrbs = [];
        const BOKEH_COLORS = [
            "rgba(56, 189, 248, 0.08)",   // Cyan
            "rgba(223, 188, 97, 0.08)",   // Gold
            "rgba(192, 132, 252, 0.07)",  // Lilac
            "rgba(245, 158, 11, 0.07)"    // Amber
        ];

        function initBokeh() {
            bokehOrbs = [];
            for (let i = 0; i < BOKEH_COUNT; i++) {
                bokehOrbs.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    vx: (Math.random() - 0.5) * 0.20,
                    vy: -0.08 - Math.random() * 0.18,
                    r: 22 + Math.random() * 28,
                    color: BOKEH_COLORS[i % BOKEH_COLORS.length]
                });
            }
        }

        initDust();
        initBokeh();
        
        function drawGrid() {
            const centerX = canvas.width / 2;
            const centerY = canvas.height * 0.42;
            const maxDist = Math.hypot(canvas.width, canvas.height) * 0.65;

            // Radial Occlusion: grid is crisper near hero, softly falls off toward edges
            const offsetX = (canvas.width / 2) % GRID_SIZE;
            const offsetY = (canvas.height / 2) % GRID_SIZE;
            
            for (let x = offsetX; x <= canvas.width; x += GRID_SIZE) {
                const distRatio = Math.min(1.0, Math.abs(x - centerX) / (canvas.width * 0.6));
                const lineOpacity = 0.095 - distRatio * 0.045;
                ctx.strokeStyle = \`rgba(212, 175, 55, \${lineOpacity.toFixed(3)})\`;
                ctx.lineWidth = 1;
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
            }
            for (let y = offsetY; y <= canvas.height; y += GRID_SIZE) {
                const distRatio = Math.min(1.0, Math.abs(y - centerY) / (canvas.height * 0.6));
                const lineOpacity = 0.095 - distRatio * 0.045;
                ctx.strokeStyle = \`rgba(212, 175, 55, \${lineOpacity.toFixed(3)})\`;
                ctx.lineWidth = 1;
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
            }
            
            // Intersection tick crosses with radial falloff
            for (let x = offsetX; x <= canvas.width; x += GRID_SIZE) {
                for (let y = offsetY; y <= canvas.height; y += GRID_SIZE) {
                    const d = Math.hypot(x - centerX, y - centerY);
                    const crossOpacity = Math.max(0.06, 0.25 * (1.0 - d / maxDist));
                    ctx.strokeStyle = \`rgba(212, 175, 55, \${crossOpacity.toFixed(3)})\`;
                    ctx.beginPath();
                    ctx.moveTo(x - 4, y); ctx.lineTo(x + 4, y);
                    ctx.moveTo(x, y - 4); ctx.lineTo(x, y + 4);
                    ctx.stroke();
                }
            }
        }
        
        function spawnThread(x, y, isBranch = false, inheritedColor = null) {
            if (threads.length > 50) return;
            
            let startX = x !== undefined ? x : Math.floor(Math.random() * (canvas.width / GRID_SIZE)) * GRID_SIZE + ((canvas.width / 2) % GRID_SIZE);
            let startY = y !== undefined ? y : Math.floor(Math.random() * (canvas.height / GRID_SIZE)) * GRID_SIZE + ((canvas.height / 2) % GRID_SIZE);
            let colorScheme = inheritedColor || PALETTE[Math.floor(Math.random() * PALETTE.length)];

            threads.push({
                x: startX, y: startY,
                path: [{x: startX, y: startY}],
                maxLength: 3 + Math.random() * 6,
                life: 0,
                maxLife: 200 + Math.random() * 200,
                moving: false,
                colorScheme: colorScheme
            });
        }

        function animate() {
            // Re-fetch canvas in case React unmounted and remounted it during SPA navigation
            const currentCanvas = document.getElementById("lambdaBackground");
            if (!currentCanvas) {
                requestAnimationFrame(animate);
                return;
            }
            
            // Re-bind ctx if canvas DOM element was replaced by router
            if (currentCanvas !== canvas) {
                canvas = currentCanvas;
                ctx = canvas.getContext("2d");
                resize();
                initDust();
                initBokeh();
            }

            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            drawGrid();

            // Layer 1: Distant Ambient Spatial Dust
            for (let i = 0; i < dust.length; i++) {
                let d = dust[i];
                d.x += d.vx;
                d.y += d.vy;
                if (d.y < 0) { d.y = canvas.height; d.x = Math.random() * canvas.width; }
                if (d.x < 0) d.x = canvas.width;
                if (d.x > canvas.width) d.x = 0;

                ctx.beginPath();
                ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
                ctx.fillStyle = d.glow;
                ctx.globalAlpha = d.alpha;
                ctx.fill();
            }
            ctx.globalAlpha = 1.0;
            
            if (threads.length < 15) {
                spawnThread();
            }
            
            for (let i = threads.length - 1; i >= 0; i--) {
                let t = threads[i];
                
                if (t.moving) {
                    t.x += t.vx;
                    t.y += t.vy;
                    t.progress += SPEED;
                    
                    if (t.progress >= GRID_SIZE) {
                        t.x = t.targetX;
                        t.y = t.targetY;
                        t.path.push({x: t.x, y: t.y});
                        if (t.path.length > t.maxLength) t.path.shift();
                        t.moving = false;
                    }
                } else {
                    let dirs = [
                        {vx: 0, vy: -SPEED}, {vx: SPEED, vy: 0},
                        {vx: 0, vy: SPEED}, {vx: -SPEED, vy: 0}
                    ];
                    
                    let possibleDirs = dirs;
                    if (t.lastDir !== undefined) {
                        possibleDirs = dirs.filter((d, idx) => idx !== (t.lastDir + 2) % 4);
                    }
                    
                    let choiceIdx = Math.floor(Math.random() * possibleDirs.length);
                    let selected = possibleDirs[choiceIdx];
                    
                    t.vx = selected.vx;
                    t.vy = selected.vy;
                    t.targetX = t.x + (t.vx > 0 ? GRID_SIZE : t.vx < 0 ? -GRID_SIZE : 0);
                    t.targetY = t.y + (t.vy > 0 ? GRID_SIZE : t.vy < 0 ? -GRID_SIZE : 0);
                    t.progress = 0;
                    t.moving = true;
                    t.lastDir = dirs.indexOf(selected);
                    
                    if (Math.random() < 0.03) {
                        spawnThread(t.x, t.y, true, t.colorScheme);
                    }
                }
                
                t.life++;
                if (t.life > t.maxLife) {
                    t.path.shift();
                    if (t.path.length === 0) {
                        threads.splice(i, 1);
                        continue;
                    }
                }
                
                if (t.path.length > 0) {
                    let points = [...t.path, {x: t.x, y: t.y}];
                    const lifeOpacity = t.life > t.maxLife ? Math.max(0, t.path.length / t.maxLength) : 1.0;
                    
                    ctx.lineCap = "round";
                    ctx.lineJoin = "round";
                    
                    const col = t.colorScheme || PALETTE[0];

                    for (let j = 1; j < points.length; j++) {
                        const p1 = points[j - 1];
                        const p2 = points[j];
                        
                        const segmentOpacity = Math.pow(j / points.length, 2) * lifeOpacity * 0.40; 
                        
                        ctx.beginPath();
                        ctx.moveTo(p1.x, p1.y);
                        ctx.lineTo(p2.x, p2.y);
                        
                        ctx.strokeStyle = \`rgba(\${col.stroke}, \${segmentOpacity})\`;
                        ctx.lineWidth = 2.0;
                        ctx.stroke();
                    }
                    
                    const headOpacity = lifeOpacity * 0.75;
                    ctx.beginPath();
                    ctx.arc(t.x, t.y, 2.5, 0, Math.PI * 2);
                    ctx.fillStyle = \`rgba(255, 255, 255, \${headOpacity})\`;
                    ctx.shadowBlur = 8;
                    ctx.shadowColor = col.glow;
                    ctx.fill();
                    ctx.shadowBlur = 0;
                }
            }

            // Layer 3: Foreground Camera Focal Bokeh Orbs
            for (let i = 0; i < bokehOrbs.length; i++) {
                let b = bokehOrbs[i];
                b.x += b.vx;
                b.y += b.vy;
                if (b.y < -b.r * 2) { b.y = canvas.height + b.r; b.x = Math.random() * canvas.width; }
                if (b.x < -b.r * 2) b.x = canvas.width + b.r;
                if (b.x > canvas.width + b.r * 2) b.x = -b.r;

                const grad = ctx.createRadialGradient(b.x, b.y, 0, b.x, b.y, b.r);
                grad.addColorStop(0, b.color);
                grad.addColorStop(0.5, b.color.replace(/[\\d\\.]+\\)$/, "0.03)"));
                grad.addColorStop(1, "rgba(0, 0, 0, 0)");

                ctx.fillStyle = grad;
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
                ctx.fill();
            }
            
            requestAnimationFrame(animate);
        }
        
        animate();
    }
    initCanvas();
}
`)),y(a,{css:{width:`100%`,height:`100vh`,maxHeight:`100vh`,display:`flex`,flexDirection:`column`,overflow:`hidden`,position:`relative`}},y(a,{css:{width:`100%`,height:`56px`,position:`fixed`,top:`0`,left:`0`,background:`rgba(0, 0, 0, 0.6)`,backdropFilter:`blur(24px)`,zIndex:`50`}},y(d,{align:`start`,className:`rx-Stack`,css:{width:`100%`,"@media screen and (min-width: 0)":{paddingInlineStart:`16px`,paddingInlineEnd:`16px`},"@media screen and (min-width: 30em)":{paddingInlineStart:`24px`,paddingInlineEnd:`24px`},"@media screen and (min-width: 48em)":{paddingInlineStart:`36px`,paddingInlineEnd:`36px`},"@media screen and (min-width: 62em)":{paddingInlineStart:`48px`,paddingInlineEnd:`48px`},height:`56px`,alignItems:`center`},direction:`row`,gap:`3`},y(o,{asChild:!0,css:{"&:hover":{textDecoration:`none`}}},y(r,{to:`/`},y(d,{align:`start`,className:`rx-Stack`,css:{alignItems:`center`},direction:`row`,gap:`3`},y(a,{css:{display:`inline-flex`,alignItems:`center`,justifyContent:`center`,width:`48px`,height:`34px`}},y(`canvas`,{css:{width:`48px`,height:`34px`,display:`block`,pointerEvents:`none`},id:`chromaNavCrystal`,ref:t})),y(d,{align:`start`,className:`rx-Stack`,css:{alignItems:`center`},direction:`row`,gap:`2`},y(s,{as:`p`,css:{fontWeight:`800`,"@media screen and (min-width: 0)":{fontSize:`1.05rem`},"@media screen and (min-width: 30em)":{fontSize:`1.15rem`},color:`white`,letterSpacing:`0.12em`}},`CHROMA`),y(s,{as:`p`,css:{fontWeight:`400`,"@media screen and (min-width: 0)":{fontSize:`1.05rem`},"@media screen and (min-width: 30em)":{fontSize:`1.15rem`},color:`#DFBC61`,letterSpacing:`0.12em`}},`LABS`))))),y(d,{css:{flex:1,justifySelf:`stretch`,alignSelf:`stretch`}}),y(d,{align:`start`,className:`rx-Stack`,css:{"@media screen and (min-width: 0)":{display:`none`},"@media screen and (min-width: 30em)":{display:`none`},"@media screen and (min-width: 48em)":{display:`flex`},"@media screen and (min-width: 62em)":{display:`flex`},alignItems:`center`},direction:`row`,gap:`4`},y(g,{},y(c,{},y(f,{css:{background:`transparent`,border:`1px solid transparent`,padding:`8px 16px`,borderRadius:`6px`,cursor:`pointer`,transition:`all 0.2s ease`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`,border:`1px solid rgba(255, 255, 255, 0.1)`,boxShadow:`0 0 15px rgba(255, 255, 255, 0.05)`,color:`white`},height:`auto`}},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`0.9rem`,fontWeight:`500`,letterSpacing:`0.05em`,transition:`color 0.2s ease`}},`CAPABILITIES`))),y(m,{css:{background:`rgba(5, 5, 5, 0.95)`,border:`1px solid rgba(255, 255, 255, 0.08)`,backdropFilter:`blur(24px)`,padding:`6px`,borderRadius:`8px`,boxShadow:`0 10px 40px rgba(0,0,0,0.5)`,minWidth:`220px`}},y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/capabilities`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Capabilities Overview`)))),y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/capabilities/thermodynamics`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Thermodynamic Scaling`)))),y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/capabilities/ai`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Artificial Intelligence`)))),y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/capabilities/defense`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Defense & Security`)))),y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/capabilities/robotics`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Autonomous Robotics`)))))),y(g,{},y(c,{},y(f,{css:{background:`transparent`,border:`1px solid transparent`,padding:`8px 16px`,borderRadius:`6px`,cursor:`pointer`,transition:`all 0.2s ease`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`,border:`1px solid rgba(255, 255, 255, 0.1)`,boxShadow:`0 0 15px rgba(255, 255, 255, 0.05)`,color:`white`},height:`auto`}},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`0.9rem`,fontWeight:`500`,letterSpacing:`0.05em`,transition:`color 0.2s ease`}},`RESEARCH`))),y(m,{css:{background:`rgba(5, 5, 5, 0.95)`,border:`1px solid rgba(255, 255, 255, 0.08)`,backdropFilter:`blur(24px)`,padding:`6px`,borderRadius:`8px`,boxShadow:`0 10px 40px rgba(0,0,0,0.5)`,minWidth:`220px`}},y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/research/log`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Research Log`)))),y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/research/papers`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Published Papers`)))))),y(g,{},y(c,{},y(f,{css:{background:`transparent`,border:`1px solid transparent`,padding:`8px 16px`,borderRadius:`6px`,cursor:`pointer`,transition:`all 0.2s ease`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`,border:`1px solid rgba(255, 255, 255, 0.1)`,boxShadow:`0 0 15px rgba(255, 255, 255, 0.05)`,color:`white`},height:`auto`}},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`0.9rem`,fontWeight:`500`,letterSpacing:`0.05em`,transition:`color 0.2s ease`}},`COMPANY`))),y(m,{css:{background:`rgba(5, 5, 5, 0.95)`,border:`1px solid rgba(255, 255, 255, 0.08)`,backdropFilter:`blur(24px)`,padding:`6px`,borderRadius:`8px`,boxShadow:`0 10px 40px rgba(0,0,0,0.5)`,minWidth:`220px`}},y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/company/mission`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Mission`)))),y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/company/careers`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Careers`)))),y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/company/directory`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Staff Directory`)))),y(a,{css:{background:`transparent`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`},paddingTop:`16px`,paddingBottom:`16px`,paddingInlineStart:`20px`,paddingInlineEnd:`20px`,cursor:`pointer`,transition:`background 0.2s ease`,borderRadius:`4px`}},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/contact`},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`1.1rem`,transition:`color 0.2s ease`,"&:hover":{color:`white`}}},`Contact Us`)))))),y(o,{asChild:!0,css:{"&:hover":{textDecoration:`none`},"@media screen and (min-width: 0)":{marginRight:`0px`},"@media screen and (min-width: 30em)":{marginRight:`4px`},"@media screen and (min-width: 48em)":{marginRight:`12px`},"@media screen and (min-width: 62em)":{marginRight:`16px`}}},y(r,{to:`/developer`},y(f,{css:{background:`transparent`,border:`1px solid transparent`,padding:`8px 16px`,borderRadius:`6px`,cursor:`pointer`,transition:`all 0.2s ease`,"&:hover":{background:`rgba(255, 255, 255, 0.05)`,border:`1px solid rgba(255, 255, 255, 0.1)`,boxShadow:`0 0 15px rgba(255, 255, 255, 0.05)`,color:`white`},height:`auto`}},y(s,{as:`p`,css:{color:`slate.11`,fontSize:`0.9rem`,fontWeight:`500`,letterSpacing:`0.05em`,transition:`color 0.2s ease`}},`DEVELOPER PORTAL`))))),y(a,{css:{"@media screen and (min-width: 0)":{display:`block`},"@media screen and (min-width: 30em)":{display:`block`},"@media screen and (min-width: 48em)":{display:`none`},"@media screen and (min-width: 62em)":{display:`none`}}},y(v,{},y(u,{},y(x,{css:{color:`white`,cursor:`pointer`},size:32})),y(l,{css:{background:`rgba(10, 10, 10, 0.95)`,color:`slate.11`,border:`1px solid rgba(255, 255, 255, 0.08)`}},y(s,{as:`p`,css:{padding:`8px 12px`,color:`#DFBC61`,fontSize:`0.75rem`,fontWeight:`bold`,letterSpacing:`0.1em`}},`CAPABILITIES`),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/capabilities`},`Capabilities Overview`))),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/capabilities/thermodynamics`},`Thermodynamic Scaling`))),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/capabilities/ai`},`Artificial Intelligence`))),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/capabilities/defense`},`Defense & Security`))),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/capabilities/robotics`},`Autonomous Robotics`))),y(p,{}),y(s,{as:`p`,css:{padding:`8px 12px`,color:`#DFBC61`,fontSize:`0.75rem`,fontWeight:`bold`,letterSpacing:`0.1em`}},`RESEARCH`),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/research/log`},`Research Log`))),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/research/papers`},`Published Papers`))),y(p,{}),y(s,{as:`p`,css:{padding:`8px 12px`,color:`#DFBC61`,fontSize:`0.75rem`,fontWeight:`bold`,letterSpacing:`0.1em`}},`COMPANY`),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/company/mission`},`Mission`))),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/company/careers`},`Careers`))),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/company/directory`},`Staff Directory`))),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/contact`},`Contact Us`))),y(p,{}),y(h,{},y(o,{asChild:!0,css:{width:`100%`,display:`block`,color:`inherit`,fontWeight:`bold`,"&:hover":{textDecoration:`none`}}},y(r,{to:`/developer`},`DEVELOPER PORTAL`))))))),y(a,{css:{position:`absolute`,bottom:`0`,left:`0`,width:`100%`,height:`1px`,background:`linear-gradient(90deg, rgba(223, 188, 97, 0) 0%, rgba(223, 188, 97, 0.15) 20%, rgba(223, 188, 97, 0.75) 50%, rgba(223, 188, 97, 0.15) 80%, rgba(223, 188, 97, 0) 100%)`,boxShadow:`0 0 16px rgba(223, 188, 97, 0.45), 0 0 4px rgba(223, 188, 97, 0.7)`,pointerEvents:`none`}})),y(a,{css:{width:`100%`,height:`calc(100vh - 112px)`,maxHeight:`calc(100vh - 112px)`,marginTop:`56px`,position:`relative`,zIndex:`10`,display:`flex`,flexDirection:`column`,alignItems:`center`,justifyContent:`center`,"@media screen and (min-width: 0)":{overflowY:`auto`},"@media screen and (min-width: 30em)":{overflowY:`auto`},"@media screen and (min-width: 48em)":{overflowY:`hidden`},"@media screen and (min-width: 62em)":{overflowY:`hidden`},overflowX:`hidden`}},y(a,{css:{width:`100%`,height:`100%`,display:`flex`,alignItems:`center`,justifyContent:`center`}},y(d,{align:`start`,className:`rx-Stack`,css:{width:`100%`,maxWidth:`1000px`,alignItems:`center`,justifyContent:`center`,"@media screen and (min-width: 0)":{paddingInlineStart:`4`,paddingInlineEnd:`4`},"@media screen and (min-width: 30em)":{paddingInlineStart:`6`,paddingInlineEnd:`6`},"@media screen and (min-width: 48em)":{paddingInlineStart:`8`,paddingInlineEnd:`8`}},direction:`column`,gap:`3`},y(s,{as:`p`,className:`animate-fade-up`,css:{fontSize:`0.75rem`,color:`#DFBC61`,letterSpacing:`0.15em`,textAlign:`center`,fontFamily:`JetBrains Mono, monospace`,"--default-font-family":`JetBrains Mono, monospace`},weight:`bold`},`JOIN THE LAB`),y(s,{as:`p`,className:`animate-fade-up delay-100`,css:{"@media screen and (min-width: 0)":{fontSize:`2.0rem`},"@media screen and (min-width: 30em)":{fontSize:`2.6rem`},"@media screen and (min-width: 48em)":{fontSize:`3.2rem`},letterSpacing:`-0.03em`,lineHeight:`1.1`,color:`white`,fontFamily:`'EB Garamond', 'Playfair Display', serif`,"--default-font-family":`'EB Garamond', 'Playfair Display', serif`,marginBottom:`2`,textAlign:`center`},weight:`bold`},`Engineering & Research.`),y(s,{as:`p`,className:`animate-fade-up delay-200`,css:{fontSize:`0.95rem`,color:`slate.11`,maxWidth:`740px`,textAlign:`center`,marginBottom:`4`,lineHeight:`1.55`}},`We are building a highly concentrated, elite technical cadre across mathematical formalization, deep-silicon engineering, and sovereign defense infrastructure.`),y(d,{className:`animate-fade-up delay-300`,css:{display:`flex`,alignItems:`center`,justifyContent:`center`,background:`rgba(10, 10, 14, 0.6)`,border:`1px solid rgba(255, 255, 255, 0.06)`,borderRadius:`8px`,padding:`32px 28px`,width:`100%`,maxWidth:`720px`}},y(d,{align:`start`,className:`rx-Stack`,css:{alignItems:`center`},direction:`column`,gap:`3`},y(C,{css:{color:`#DFBC61`,marginBottom:`2`},size:32}),y(s,{as:`p`,css:{color:`white`,fontSize:`1.2rem`,fontWeight:`700`}},`Targeted Institutional Recruiting`),y(s,{as:`p`,css:{color:`slate.11`,textAlign:`center`,maxWidth:`560px`,marginTop:`1`,fontSize:`0.85rem`,lineHeight:`1.55`}},`Positions are opened on a mission-specific basis aligned with deployment schedules and defense partnerships. We welcome inquiries from elite contributors with backgrounds in Lean 4 formal verification, compiler architecture, and low-SWaP systems engineering.`),y(o,{asChild:!0,css:{"&:hover":{textDecoration:`none`}}},y(r,{to:`/contact?topic=Research%20and%20Engineering%20Candidacy`},y(f,{css:{background:`#DFBC61`,border:`none`,color:`black`,borderRadius:`4px`,fontWeight:`600`,cursor:`pointer`,transition:`all 0.3s ease`,"&:hover":{background:`#e6c455`,transform:`translateY(-2px)`,boxShadow:`0 0 35px rgba(223, 188, 97, 0.5), 0 0 20px rgba(168, 85, 247, 0.4)`},fontSize:`0.82rem`,letterSpacing:`0.08em`,padding:`12px 24px`,marginTop:`4`}},`SUBMIT RESEARCHER CV`)))))))),y(a,{css:{width:`100%`,height:`56px`,position:`fixed`,bottom:`0`,left:`0`,background:`rgba(0, 0, 0, 0.6)`,backdropFilter:`blur(24px)`,zIndex:`50`}},y(a,{css:{position:`absolute`,top:`0`,left:`0`,width:`100%`,height:`1px`,background:`linear-gradient(90deg, rgba(223, 188, 97, 0) 0%, rgba(223, 188, 97, 0.15) 20%, rgba(223, 188, 97, 0.75) 50%, rgba(223, 188, 97, 0.15) 80%, rgba(223, 188, 97, 0) 100%)`,boxShadow:`0 0 16px rgba(223, 188, 97, 0.45), 0 0 4px rgba(223, 188, 97, 0.7)`,pointerEvents:`none`}}),y(d,{css:{width:`100%`,maxWidth:`1200px`,margin:`0 auto`,"@media screen and (min-width: 0)":{paddingInlineStart:`4`,paddingInlineEnd:`4`,flexDirection:`column`},"@media screen and (min-width: 30em)":{paddingInlineStart:`8`,paddingInlineEnd:`8`,flexDirection:`column`},"@media screen and (min-width: 48em)":{paddingInlineStart:`16`,paddingInlineEnd:`16`,flexDirection:`row`},height:`56px`,alignItems:`center`,justifyContent:`center`},gap:`2`},y(s,{as:`p`,css:{color:`slate.8`,fontFamily:`JetBrains Mono, monospace`,"--default-font-family":`JetBrains Mono, monospace`,fontSize:`0.75rem`,letterSpacing:`0.08em`,"@media screen and (min-width: 0)":{textAlign:`center`},"@media screen and (min-width: 30em)":{textAlign:`center`},"@media screen and (min-width: 48em)":{textAlign:`left`}}},`© 2026 Chroma Labs, Inc.™`),y(d,{css:{flex:1,justifySelf:`stretch`,alignSelf:`stretch`,"@media screen and (min-width: 0)":{display:`none`},"@media screen and (min-width: 30em)":{display:`none`},"@media screen and (min-width: 48em)":{display:`block`}}}),y(s,{as:`p`,css:{color:`slate.8`,fontSize:`0.75rem`,fontFamily:`JetBrains Mono, monospace`,"--default-font-family":`JetBrains Mono, monospace`,"@media screen and (min-width: 0)":{textAlign:`center`},"@media screen and (min-width: 30em)":{textAlign:`center`},"@media screen and (min-width: 48em)":{textAlign:`right`}}},`17350 STATE HWY 249, STE 220 #37670 · HOUSTON, TX 77064`))))),y(`title`,{},`Careers | Chroma Labs`),y(`meta`,{content:`/logo_glyph.png`,property:`og:image`}))});export{w as default};