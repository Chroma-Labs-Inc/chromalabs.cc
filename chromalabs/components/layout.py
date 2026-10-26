
import reflex as rx
from .navbar import navbar
from .footer import footer

GRID_ANIMATION_JS = r"""
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
                ctx.strokeStyle = `rgba(212, 175, 55, ${lineOpacity.toFixed(3)})`;
                ctx.lineWidth = 1;
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
            }
            for (let y = offsetY; y <= canvas.height; y += GRID_SIZE) {
                const distRatio = Math.min(1.0, Math.abs(y - centerY) / (canvas.height * 0.6));
                const lineOpacity = 0.095 - distRatio * 0.045;
                ctx.strokeStyle = `rgba(212, 175, 55, ${lineOpacity.toFixed(3)})`;
                ctx.lineWidth = 1;
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
            }
            
            // Intersection tick crosses with radial falloff
            for (let x = offsetX; x <= canvas.width; x += GRID_SIZE) {
                for (let y = offsetY; y <= canvas.height; y += GRID_SIZE) {
                    const d = Math.hypot(x - centerX, y - centerY);
                    const crossOpacity = Math.max(0.06, 0.25 * (1.0 - d / maxDist));
                    ctx.strokeStyle = `rgba(212, 175, 55, ${crossOpacity.toFixed(3)})`;
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
                        
                        ctx.strokeStyle = `rgba(${col.stroke}, ${segmentOpacity})`;
                        ctx.lineWidth = 2.0;
                        ctx.stroke();
                    }
                    
                    const headOpacity = lifeOpacity * 0.75;
                    ctx.beginPath();
                    ctx.arc(t.x, t.y, 2.5, 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(255, 255, 255, ${headOpacity})`;
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
                grad.addColorStop(0.5, b.color.replace(/[\d\.]+\)$/, "0.03)"));
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
"""

def base_layout(content: rx.Component) -> rx.Component:
    return rx.box(
        rx.box(
            position="fixed", top="0", left="0", width="100vw", height="100vh", z_index="-1",
            bg="#07070A",
        ),
        rx.box(
            position="fixed", top="12%", left="50%", transform="translateX(-50%)", width="65vw", height="65vw",
            background="radial-gradient(circle, rgba(223, 188, 97, 0.07) 0%, transparent 65%)",
            z_index="1", filter="blur(90px)", border_radius="50%", pointer_events="none",
        ),
        rx.box(
            position="fixed", top="35%", left="-10%", width="55vw", height="55vw",
            background="radial-gradient(circle, rgba(168, 85, 247, 0.05) 0%, transparent 70%)",
            z_index="1", filter="blur(110px)", border_radius="50%", pointer_events="none",
        ),
        rx.box(
            position="fixed", bottom="-10%", right="-10%", width="60vw", height="60vw",
            background="radial-gradient(circle, rgba(6, 182, 212, 0.04) 0%, transparent 70%)",
            z_index="1", filter="blur(110px)", border_radius="50%", pointer_events="none",
        ),
        rx.el.canvas(
            id="lambdaBackground", 
            style={"position": "fixed", "top": "0", "left": "0", "width": "100vw", "height": "100vh", "z_index": "2", "pointer_events": "none"}
        ),
        rx.script(GRID_ANIMATION_JS),

        rx.box(
            navbar(),
            rx.box(
                content,
                width="100%",
                height="calc(100vh - 112px)",
                max_height="calc(100vh - 112px)",
                margin_top="56px",
                position="relative",
                z_index="10",
                display="flex",
                flex_direction="column",
                align_items="center",
                justify_content=["flex-start", "flex-start", "center", "center"],
                overflow_y=["auto", "auto", "hidden", "hidden"],
                overflow_x="hidden",
            ),
            footer(),
            width="100%",
            height="100vh",
            max_height="100vh",
            display="flex",
            flex_direction="column",
            overflow="hidden",
            position="relative",
        ),
        background="transparent", color="white", font_family="Inter, sans-serif",
        position="relative"
    )

