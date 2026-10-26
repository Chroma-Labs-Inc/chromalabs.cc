import reflex as rx

CRYSTAL_JS = """
(function() {
    if (window.__chromaCrystalRenderAll) {
        window.__chromaCrystalRenderAll();
        return;
    }

    // Authentic Secure Client 3D Polyhedron Geometry (Tall Spire with Exact Unclipped Bounds)
    const N = 8;
    const y_top = 2.80;
    const R_girdle = 0.88;
    const y_girdle = -0.20;
    const r_mid = 0.46;
    const y_mid = -0.50;
    const y_bottom = -0.80;

    const top_tip = [0.0, y_top, 0.0];
    const bottom_tip = [0.0, y_bottom, 0.0];

    const girdle_v = [];
    for (let i = 0; i < N; i++) {
        const theta = (2 * Math.PI * i) / N;
        girdle_v.push([R_girdle * Math.cos(theta), y_girdle, R_girdle * Math.sin(theta)]);
    }

    const mid_v = [];
    for (let i = 0; i < N; i++) {
        const theta = ((i + 0.5) * 2 * Math.PI) / N;
        mid_v.push([r_mid * Math.cos(theta), y_mid, r_mid * Math.sin(theta)]);
    }

    // Inward shadow groove down the top very front
    const delta_x = 0.08, dip_z = 0.20, delta_top = 0.035, dip_top_y = 0.12;
    const top_L = [-delta_top, y_top, 0.0];
    const top_R = [+delta_top, y_top, 0.0];
    const top_dip = [0.0, y_top - dip_top_y, delta_top * 0.5];
    const ridge_L = [-delta_x, y_girdle, -R_girdle];
    const ridge_R = [+delta_x, y_girdle, -R_girdle];
    const groove_bot = [0.0, y_girdle, -R_girdle + dip_z];

    const triangles = [];
    for (let i = 0; i < N; i++) {
        if (i === 5 || i === 6) continue;
        const nxt = (i + 1) % N;
        triangles.push([girdle_v[i], top_tip, girdle_v[nxt], i]);
    }
    triangles.push([girdle_v[5], top_L, ridge_L, 5]);
    triangles.push([ridge_R, top_R, girdle_v[7], 6]);
    triangles.push([ridge_L, top_L, top_dip, 20]);
    triangles.push([ridge_L, top_dip, groove_bot, 21]);
    triangles.push([top_R, ridge_R, groove_bot, 22]);
    triangles.push([top_R, groove_bot, top_dip, 23]);

    for (let i = 0; i < N; i++) {
        if (i === 5 || i === 6) continue;
        const nxt = (i + 1) % N;
        triangles.push([girdle_v[nxt], bottom_tip, girdle_v[i], 10 + i]);
    }
    triangles.push([ridge_L, bottom_tip, girdle_v[5], 15]);
    triangles.push([ridge_R, bottom_tip, ridge_L, 16]);
    triangles.push([girdle_v[7], bottom_tip, ridge_R, 17]);

    let angle = 0.8;
    let pulsePhase = 1.0;

    function renderEngine(canvas, isNav) {
        if (!canvas || !canvas.getContext) return;
        let ctx;
        try {
            ctx = canvas.getContext("2d");
        } catch (e) {
            return;
        }
        if (!ctx) return;

        const dpr = window.devicePixelRatio || 2;
        const cssW = isNav ? 48 : 300;
        const cssH = isNav ? 34 : 200;

        if (canvas.width !== Math.round(cssW * dpr) || canvas.height !== Math.round(cssH * dpr)) {
            canvas.width = Math.round(cssW * dpr);
            canvas.height = Math.round(cssH * dpr);
        }

        ctx.save();
        ctx.scale(dpr, dpr);
        ctx.clearRect(0, 0, cssW, cssH);

        const COLS = isNav ? 15 : 32;
        const ROWS = isNav ? 11 : 21;
        const cellW = cssW / COLS;
        const cellH = cssH / ROWS;

        const pitch = 0.36; // Perspective pitch
        const cosY = Math.cos(angle), sinY = Math.sin(angle);
        const cosP = Math.cos(pitch), sinP = Math.sin(pitch);

        // Exact unclipped mathematical projection
        function tr(p) {
            const x = p[0], y = p[1], z = p[2];
            const rx = x * cosY + z * sinY;
            const ry = y;
            const rz = -x * sinY + z * cosY;
            const ry2 = ry * cosP - rz * sinP;
            const rz2 = ry * sinP + rz * cosP;
            const dist = 3.5;
            const fov = dist / (dist + rz2);
            // Perfectly centered and scaled within bounds
            const sx = (rx * fov * (COLS * 0.468)) + (COLS / 2.0);
            const sy = (-(ry2 * fov - 0.615) * (ROWS * 0.295)) + (ROWS / 2.0);
            return { rx, ry: ry2, rz: rz2, sx, sy };
        }

        const grid = Array.from({ length: ROWS }, () => new Array(COLS).fill(' '));
        const charColors = Array.from({ length: ROWS }, () => new Array(COLS).fill(''));
        const zbuf = Array.from({ length: ROWS }, () => new Array(COLS).fill(-999.0));
        const facetMap = Array.from({ length: ROWS }, () => new Array(COLS).fill(-1));
        const intensityMap = Array.from({ length: ROWS }, () => new Array(COLS).fill(0.0));
        const normalMap = Array.from({ length: ROWS }, () => new Array(COLS).fill(null));

        const light = [0.4, 0.7, -0.6];
        const lLen = Math.hypot(...light);
        const lx = light[0] / lLen, ly = light[1] / lLen, lz = light[2] / lLen;

        for (let i = 0; i < triangles.length; i++) {
            const [v0, v1, v2, fid] = triangles[i];
            const p0 = tr(v0), p1 = tr(v1), p2 = tr(v2);

            const ux = p1.rx - p0.rx, uy = p1.ry - p0.ry, uz = p1.rz - p0.rz;
            const vx = p2.rx - p0.rx, vy = p2.ry - p0.ry, vz = p2.rz - p0.rz;
            const nx = uy * vz - uz * vy, ny = uz * vx - ux * vz, nz = ux * vy - uy * vx;
            const nlen = Math.hypot(nx, ny, nz);
            if (nlen > 1e-6) {
                const nnx = nx / nlen, nny = ny / nlen, nnz = nz / nlen;
                if (nnz < -0.01) {
                    const dot = Math.max(0.15, nnx * lx + nny * ly + nnz * lz);
                    const minX = Math.max(0, Math.floor(Math.min(p0.sx, p1.sx, p2.sx)));
                    const maxX = Math.min(COLS - 1, Math.ceil(Math.max(p0.sx, p1.sx, p2.sx)));
                    const minY = Math.max(0, Math.floor(Math.min(p0.sy, p1.sy, p2.sy)));
                    const maxY = Math.min(ROWS - 1, Math.ceil(Math.max(p0.sy, p1.sy, p2.sy)));

                    const denom = (p1.sy - p2.sy) * (p0.sx - p2.sx) + (p2.sx - p1.sx) * (p0.sy - p2.sy);
                    if (Math.abs(denom) > 1e-6) {
                        for (let py = minY; py <= maxY; py++) {
                            for (let px = minX; px <= maxX; px++) {
                                const w0 = ((p1.sy - p2.sy) * (px - p2.sx) + (p2.sx - p1.sx) * (py - p2.sy)) / denom;
                                const w1 = ((p2.sy - p0.sy) * (px - p2.sx) + (p0.sx - p2.sx) * (py - p2.sy)) / denom;
                                const w2 = 1.0 - w0 - w1;
                                if (w0 >= 0 && w1 >= 0 && w2 >= 0) {
                                    const pz = w0 * p0.rz + w1 * p1.rz + w2 * p2.rz;
                                    if (pz > zbuf[py][px]) {
                                        zbuf[py][px] = pz;
                                        facetMap[py][px] = fid;
                                        intensityMap[py][px] = dot;
                                        normalMap[py][px] = { nx: nnx, ny: nny, nz: nnz };
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        const rowSpans = {};
        for (let py = 0; py < ROWS; py++) {
            const pixels = [];
            for (let px = 0; px < COLS; px++) {
                if (zbuf[py][px] > -900) pixels.push(px);
            }
            if (pixels.length > 0) rowSpans[py] = [pixels[0], pixels[pixels.length - 1]];
        }

        const activeRows = Object.keys(rowSpans).map(Number);
        if (activeRows.length === 0) { ctx.restore(); return; }

        const minY = Math.min(...activeRows);
        const maxY = Math.max(...activeRows);

        let leftMinX = 999, leftWidestRow = minY;
        let rightMaxX = -1, rightWidestRow = minY;
        for (const py of activeRows) {
            const [x0, x1] = rowSpans[py];
            if (x0 < leftMinX) { leftMinX = x0; leftWidestRow = py; }
            if (x1 > rightMaxX) { rightMaxX = x1; rightWidestRow = py; }
        }

        function sampleSpectrum(t) {
            const stops = [
                { p: 0.00, r: 245, g: 215, b: 120 }, // Gold (#DFBC61)
                { p: 0.22, r: 245, g: 158, b: 80  }, // Amber
                { p: 0.48, r: 192, g: 132, b: 252 }, // Lilac / Violet
                { p: 0.74, r: 56,  g: 189, b: 248 }, // Electric Cyan
                { p: 1.00, r: 245, g: 215, b: 120 }
            ];
            let r = 245, g = 215, b = 120;
            for (let i = 0; i < stops.length - 1; i++) {
                if (t >= stops[i].p && t <= stops[i + 1].p) {
                    let lt = (t - stops[i].p) / (stops[i + 1].p - stops[i].p);
                    lt = (1 - Math.cos(lt * Math.PI)) / 2;
                    r = Math.floor(stops[i].r + (stops[i + 1].r - stops[i].r) * lt);
                    g = Math.floor(stops[i].g + (stops[i + 1].g - stops[i].g) * lt);
                    b = Math.floor(stops[i].b + (stops[i + 1].b - stops[i].b) * lt);
                    break;
                }
            }
            return { r, g, b };
        }

        function getFresnelColor(px, py, role) {
            if (role === "groove") return "#6E5F3C";
            if (role === "glint") return "#FFFFFF";

            const norm = normalMap[py][px];
            let t = 0;
            if (norm) {
                const fresnel = 1.0 - Math.abs(norm.nz);
                const reflect = Math.abs(norm.nx * 0.7 + norm.ny * 0.4);
                t = ((fresnel * 0.8 + reflect * 0.4 + angle * 0.15) % 1.0);
            } else {
                const relX = (px - COLS / 2) / (COLS / 2);
                t = (((Math.atan2(0, relX) + angle * 0.3) % (2 * Math.PI)) + 2 * Math.PI) % (2 * Math.PI) / (2 * Math.PI);
            }
            const c = sampleSpectrum(t);
            if (role === "bright") return `rgb(${Math.min(255, c.r + 20)}, ${Math.min(255, c.g + 20)}, ${Math.min(255, c.b + 20)})`;
            if (role === "dim") return `rgba(${Math.floor(c.r * 0.7)}, ${Math.floor(c.g * 0.7)}, ${Math.floor(c.b * 0.7)}, 0.85)`;
            return `rgb(${c.r}, ${c.g}, ${c.b})`;
        }

        for (const py of activeRows) {
            const [minPx, maxPx] = rowSpans[py];
            for (let px = minPx; px <= maxPx; px++) {
                const isTop = (py === minY);
                const isBottom = (py === maxY);
                const isLeftEdge = (px === minPx);
                const isRightEdge = (px === maxPx);

                if (isTop) {
                    const midX = Math.floor((minPx + maxPx) / 2);
                    grid[py][px] = (px === midX) ? '▲' : ((px < midX) ? '╱' : '╲');
                    charColors[py][px] = getFresnelColor(px, py, "bright");
                } else if (isBottom) {
                    const midX = Math.floor((minPx + maxPx) / 2);
                    grid[py][px] = (px === midX) ? '▼' : ((px < midX) ? '╲' : '╱');
                    charColors[py][px] = getFresnelColor(px, py, "bright");
                } else if (isLeftEdge) {
                    grid[py][px] = (py < leftWidestRow) ? '╱' : ((py === leftWidestRow) ? '◀' : '╲');
                    charColors[py][px] = getFresnelColor(px, py, "bright");
                } else if (isRightEdge) {
                    grid[py][px] = (py < rightWidestRow) ? '╲' : ((py === rightWidestRow) ? '▶' : '╱');
                    charColors[py][px] = getFresnelColor(px, py, "bright");
                } else {
                    const fid = facetMap[py][px];
                    if (fid >= 20 && fid <= 23) {
                        grid[py][px] = ':';
                        charColors[py][px] = getFresnelColor(px, py, "groove");
                    } else {
                        const isRidgeH = (px > minPx && facetMap[py][px] !== facetMap[py][px - 1] && facetMap[py][px - 1] !== -1);
                        const isRidgeV = (py > minY && facetMap[py][px] !== facetMap[py - 1][px] && facetMap[py - 1][px] !== -1);
                        if (isRidgeH) {
                            grid[py][px] = '│';
                            charColors[py][px] = "#FFE680"; // Bright caustic gold spine
                        } else if (isRidgeV) {
                            grid[py][px] = '─';
                            charColors[py][px] = "#38BDF8"; // Electric cyan dispersion crease
                        } else {
                            const val = intensityMap[py][px];
                            if (val > 0.72) {
                                grid[py][px] = '▒';
                                charColors[py][px] = getFresnelColor(px, py, "bright");
                            } else if (val > 0.48) {
                                grid[py][px] = '░';
                                charColors[py][px] = getFresnelColor(px, py, "normal");
                            } else if (val > 0.28) {
                                grid[py][px] = '·';
                                charColors[py][px] = getFresnelColor(px, py, "dim");
                            } else {
                                grid[py][px] = ':';
                                charColors[py][px] = getFresnelColor(px, py, "groove");
                            }
                        }
                    }
                }
            }
        }

        // Specular Primary Glint (✦)
        const cx = Math.floor(COLS / 2) + 2;
        const cy = Math.max(0, Math.min(ROWS - 1, leftWidestRow - 4));
        if (cx >= 0 && cx < COLS && cy >= 0 && cy < ROWS && zbuf[cy][cx] > -900) {
            if (!['▲','▼','╱','╲','◀','▶'].includes(grid[cy][cx])) {
                grid[cy][cx] = (Math.floor(pulsePhase * 2) % 2 === 0) ? '✦' : '✧';
                charColors[cy][cx] = "#FFFFFF";
            }
        }

        // Secondary Cyan Caustic Glint (✧) on Opposing Facet
        const cx2 = Math.floor(COLS / 2) - 3;
        const cy2 = Math.max(0, Math.min(ROWS - 1, leftWidestRow - 2));
        if (cx2 >= 0 && cx2 < COLS && cy2 >= 0 && cy2 < ROWS && zbuf[cy2][cx2] > -900) {
            if (!['▲','▼','╱','╲','◀','▶'].includes(grid[cy2][cx2])) {
                grid[cy2][cx2] = (Math.floor(pulsePhase * 2 + 1) % 2 === 0) ? '✧' : '·';
                charColors[cy2][cx2] = "#38BDF8";
            }
        }

        // Render Characters with Sub-pixel Crispness
        const fontSize = isNav ? Math.min(cellH * 0.95, cellW * 1.45) : 10.5;
        ctx.font = `bold ${fontSize}px 'JetBrains Mono', monospace`;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";

        for (let py = 0; py < ROWS; py++) {
            for (let px = 0; px < COLS; px++) {
                const ch = grid[py][px];
                if (ch !== ' ') {
                    const col = charColors[py][px];
                    ctx.fillStyle = col;
                    if (ch === '✦') {
                        ctx.shadowColor = "#FFFFFF";
                        ctx.shadowBlur = isNav ? 2 : 6;
                    } else if (ch === '✧') {
                        ctx.shadowColor = "#38BDF8";
                        ctx.shadowBlur = isNav ? 2 : 5;
                    } else if (['▲','▼','◀','▶'].includes(ch)) {
                        ctx.shadowColor = col;
                        ctx.shadowBlur = isNav ? 1 : 4;
                    } else {
                        ctx.shadowBlur = 0;
                    }
                    const posX = px * cellW + cellW / 2;
                    const posY = py * cellH + cellH / 2;
                    ctx.fillText(ch, posX, posY);
                }
            }
        }
        ctx.shadowBlur = 0;
        ctx.restore();
    }

    window.__chromaCrystalRenderAll = function() {
        try {
            const heroes = document.querySelectorAll(".chroma-hero-crystal-canvas, #chromaHeroCrystal");
            heroes.forEach(h => renderEngine(h, false));

            const navs = document.querySelectorAll(".chroma-nav-crystal-canvas, #chromaNavCrystal");
            navs.forEach(n => renderEngine(n, true));
        } catch (e) {}
    };

    function animate() {
        angle += 0.0055;
        pulsePhase += 0.015;

        if (window.__chromaCrystalRenderAll) {
            window.__chromaCrystalRenderAll();
        }

        requestAnimationFrame(animate);
    }

    if (!window.__chromaCrystalLoopStarted) {
        window.__chromaCrystalLoopStarted = true;
        requestAnimationFrame(animate);
    }

    if (window.__chromaCrystalRenderAll) {
        window.__chromaCrystalRenderAll();
    }
})();
"""

def chroma_crystal() -> rx.Component:
    return rx.box(
        rx.el.canvas(
            id="chromaHeroCrystal",
            class_name="chroma-hero-crystal-canvas",
        ),
        rx.script(CRYSTAL_JS),
        display="flex",
        justify_content="center",
        align_items="center",
        width="100%",
        height=["170px", "180px", "190px"],
        margin_bottom=["16px", "10px", "0px"],
        position="relative",
        z_index="10",
    )

def chroma_nav_crystal() -> rx.Component:
    return rx.box(
        rx.el.canvas(
            id="chromaNavCrystal",
            class_name="chroma-nav-crystal-canvas",
            style={
                "width": "48px",
                "height": "34px",
                "display": "block",
                "pointer_events": "none",
            }
        ),
        rx.script(CRYSTAL_JS),
        display="inline-flex",
        align_items="center",
        justify_content="center",
        width="48px",
        height="34px",
    )
