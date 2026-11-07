import reflex as rx
from chromalabs.components.layout import base_layout

DOSSIER_JS = """
(function() {
    function selectDossier(idx) {
        const tabs = document.querySelectorAll("[data-dossier-tab]");
        const panels = document.querySelectorAll("[data-dossier-panel]");
        if (!tabs.length || !panels.length) return;

        tabs.forEach(function(tab) {
            if (tab.getAttribute("data-dossier-tab") === String(idx)) {
                tab.classList.add("active-dossier-tab");
            } else {
                tab.classList.remove("active-dossier-tab");
            }
        });

        panels.forEach(function(panel) {
            if (panel.getAttribute("data-dossier-panel") === String(idx)) {
                panel.style.display = "flex";
            } else {
                panel.style.display = "none";
            }
        });
    }

    function initDossierConsole() {
        const tabs = document.querySelectorAll("[data-dossier-tab]");
        if (!tabs.length) return;

        tabs.forEach(function(tab) {
            if (tab.__dossierBound) return;
            tab.__dossierBound = true;
            const idx = tab.getAttribute("data-dossier-tab");
            tab.addEventListener("click", function() {
                selectDossier(idx);
            });
            tab.addEventListener("keydown", function(e) {
                if (e.key === "Enter" || e.key === " ") {
                    e.preventDefault();
                    selectDossier(idx);
                }
            });
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initDossierConsole);
    } else {
        initDossierConsole();
    }
    setTimeout(initDossierConsole, 150);
    setTimeout(initDossierConsole, 500);
})();
"""

LEADERSHIP_DATA = [
    {
        "idx": "0",
        "code": "EXEC-01 // PRINCIPAL ARCHITECT",
        "tier": "EXECUTIVE CADRE",
        "name": "Michael Reser",
        "short_role": "CEO, CTO & Architect",
        "role": "Founder, CEO, CTO & Systems Architect",
        "spec": "US Army Veteran and principal architect of Chroma Labs' computing physics. With foundational roots in robotics programs, STEM, and applied algorithms, Reser engineered the underlying mathematical frameworks and Lean 4 formal verification proofs de-risking the architecture.",
        "tags": ["Computing Physics", "Lean 4 Formal Proofs", "Post-Digital Silicon", "US Army Veteran"],
        "github": "https://github.com/I-Am-Finite",
        "linkedin": "https://www.linkedin.com/in/michaelreser/",
    },
    {
        "idx": "1",
        "code": "EXEC-02 // QUANTITATIVE SYSTEMS",
        "tier": "EXECUTIVE CADRE",
        "name": "Bryan C. Coward",
        "short_role": "Co-Founder & VP",
        "role": "Co-Founder, VP & Quantitative Architecture",
        "spec": "Quantitative systems and infrastructure architect. Coward directs global operations and enterprise financial architecture scaling Chroma's infrastructure across hyperscale enterprise and sovereign hardware deployments.",
        "tags": ["Quantitative Architecture", "Enterprise Infrastructure", "Capital Strategy", "Co-Founder"],
        "github": "https://github.com/bmasterc",
        "linkedin": "https://www.linkedin.com/in/cowardbryan/",
    },
    {
        "idx": "2",
        "code": "EXEC-03 // ENTERPRISE OPERATIONS",
        "tier": "EXECUTIVE CADRE",
        "name": "Jacob Gardner",
        "short_role": "Chief Operating Officer",
        "role": "Chief Operating Officer (COO)",
        "spec": "Operations executive and emerging-technology incubator founder. Drawing on leadership across the Ethereum Foundation, SWARM, Tech Dreams, and the Church of Ascension Technologies, along with technical project management and systems infrastructure, Gardner directs day-to-day enterprise operations and organizational scaling across Chroma Labs.",
        "tags": ["Ethereum Foundation", "SWARM & Tech Dreams", "Church of Ascension Technologies", "Systems Operations"],
        "github": "",
        "linkedin": "https://www.linkedin.com/in/jacobgardner770/",
    },
    {
        "idx": "3",
        "code": "EXEC-04 // MARKET ARCHITECTURE",
        "tier": "EXECUTIVE CADRE",
        "name": "Connor Dudek",
        "short_role": "Chief Marketing Officer",
        "role": "Chief Marketing Officer (CMO)",
        "spec": "Directs corporate positioning, high-velocity brand architecture, strategic communications, and institutional market alignment across global technology and defense sectors.",
        "tags": ["Brand Architecture", "Strategic Communications", "Institutional Positioning", "Global Go-To-Market"],
        "github": "",
        "linkedin": "https://www.linkedin.com/in/connordudek/",
    },
    {
        "idx": "4",
        "code": "EXEC-05 // GOVERNANCE & IP",
        "tier": "EXECUTIVE CADRE",
        "name": "Megan F. Teague",
        "short_role": "Secretary of the Board",
        "role": "Secretary of the Board",
        "spec": "Directs corporate governance, intellectual property compliance, and strategic administration across Chroma Labs' operations and sovereign defense contracts.",
        "tags": ["Corporate Governance", "IP Compliance", "Sovereign Contracts", "Board Administration"],
        "github": "",
        "linkedin": "",
    },
    {
        "idx": "5",
        "code": "ADV-01 // SCIENTIFIC VALIDATION",
        "tier": "ADVISORY COUNCIL",
        "name": "Dr. David Lary",
        "short_role": "Scientific & Defense Liaison",
        "role": "Scientific Validation & Defense Liaison",
        "spec": "Professor of Physics at UT Dallas and Director of the MINTS Lab (NASA AutoChem, SOFWERX). Dr. Lary advises on physical and thermodynamic validation across defense programs.",
        "tags": ["UT Dallas Physics", "MINTS Lab Director", "NASA AutoChem & SOFWERX", "Thermodynamic Validation"],
        "github": "",
        "linkedin": "https://www.linkedin.com/in/davidlary/",
    },
    {
        "idx": "6",
        "code": "ADV-02 // FEDERAL & REGULATORY",
        "tier": "ADVISORY COUNCIL",
        "name": "Houston Keene",
        "short_role": "Legislative & Policy Strategy",
        "role": "Legislative, Policy & Regulatory Strategy",
        "spec": "Founder of Keene Communications LLC, former Congressional Staffer and Capitol Hill correspondent. Advises on federal engagement and ITAR/EAR regulatory compliance.",
        "tags": ["Keene Communications LLC", "Capitol Hill & Federal Policy", "ITAR / EAR Compliance", "Defense Engagement"],
        "github": "",
        "linkedin": "https://www.linkedin.com/in/houston-k-15317799/",
    },
]


def roster_tab(member: dict, is_default: bool = False) -> rx.Component:
    active_cls = "chroma-dossier-tab active-dossier-tab" if is_default else "chroma-dossier-tab"
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(
                    member["name"],
                    color="white",
                    font_size=["0.82rem", "0.88rem", "0.92rem"],
                    font_weight="700",
                    line_height="1.15",
                ),
                rx.text(
                    member["short_role"],
                    color="#DFBC61",
                    font_size=["0.64rem", "0.68rem", "0.7rem"],
                    font_family="JetBrains Mono, monospace",
                    line_height="1.15",
                ),
                align_items="flex-start",
                spacing="1",
            ),
            rx.spacer(),
            rx.icon(tag="chevron-right", size=14, color="rgba(223, 188, 97, 0.7)"),
            width="100%",
            align_items="center",
        ),
        class_name=active_cls,
        custom_attrs={
            "data-dossier-tab": member["idx"],
            "role": "button",
            "tabIndex": "0",
        },
        padding=["8px 10px", "9px 12px", "10px 14px"],
        border_radius="6px",
        width="100%",
    )


def dossier_panel(member: dict, is_default: bool = False) -> rx.Component:
    links = []
    if member["github"]:
        links.append(
            rx.link(
                rx.hstack(
                    rx.icon(tag="code", size=14, color="#DFBC61"),
                    rx.text("GITHUB PROFILE", font_size="0.72rem", font_family="JetBrains Mono, monospace", font_weight="bold", color="white"),
                    rx.icon(tag="arrow-up-right", size=13, color="#DFBC61"),
                    spacing="2",
                    align_items="center",
                    padding="7px 14px",
                    background="rgba(223, 188, 97, 0.08)",
                    border="1px solid rgba(223, 188, 97, 0.35)",
                    border_radius="4px",
                    _hover={"background": "rgba(223, 188, 97, 0.18)", "border_color": "#DFBC61"},
                    transition="all 0.2s ease",
                ),
                href=member["github"],
                is_external=True,
                _hover={"text_decoration": "none"},
            )
        )
    if member["linkedin"]:
        links.append(
            rx.link(
                rx.hstack(
                    rx.icon(tag="external-link", size=14, color="#DFBC61"),
                    rx.text("LINKEDIN DOSSIER", font_size="0.72rem", font_family="JetBrains Mono, monospace", font_weight="bold", color="white"),
                    rx.icon(tag="arrow-up-right", size=13, color="#DFBC61"),
                    spacing="2",
                    align_items="center",
                    padding="7px 14px",
                    background="rgba(223, 188, 97, 0.08)",
                    border="1px solid rgba(223, 188, 97, 0.35)",
                    border_radius="4px",
                    _hover={"background": "rgba(223, 188, 97, 0.18)", "border_color": "#DFBC61"},
                    transition="all 0.2s ease",
                ),
                href=member["linkedin"],
                is_external=True,
                _hover={"text_decoration": "none"},
            )
        )

    tag_badges = [
        rx.box(
            rx.hstack(
                rx.box(width="5px", height="5px", border_radius="50%", bg="#DFBC61"),
                rx.text(t, font_family="JetBrains Mono, monospace", font_size=["0.65rem", "0.7rem"], color="slate.12"),
                spacing="2",
                align_items="center",
            ),
            padding="4px 10px",
            background="rgba(255, 255, 255, 0.03)",
            border="1px solid rgba(255, 255, 255, 0.08)",
            border_radius="4px",
        )
        for t in member["tags"]
    ]

    return rx.box(
        rx.vstack(
            # Top telemetry header bar
            rx.hstack(
                rx.text(
                    member["code"],
                    font_family="JetBrains Mono, monospace",
                    font_size=["0.62rem", "0.7rem"],
                    font_weight="bold",
                    color="#DFBC61",
                    letter_spacing="0.12em",
                ),
                rx.spacer(),
                rx.badge(member["tier"], color_scheme="amber", variant="surface", size="1"),
                width="100%",
                align_items="center",
                padding_bottom="2",
                border_bottom="1px solid rgba(255, 255, 255, 0.07)",
            ),
            # Name & Full Role
            rx.box(
                rx.text(
                    member["name"],
                    color="white",
                    font_size=["1.45rem", "1.75rem", "2.1rem"],
                    font_weight="700",
                    font_family="'EB Garamond', 'Playfair Display', serif",
                    letter_spacing="-0.02em",
                    line_height="1.1",
                ),
                rx.text(
                    member["role"],
                    color="#DFBC61",
                    font_size=["0.75rem", "0.82rem", "0.86rem"],
                    font_family="JetBrains Mono, monospace",
                    font_weight="600",
                    margin_top="1",
                ),
                margin_top="2",
                width="100%",
            ),
            # Full Bio Description
            rx.text(
                member["spec"],
                color="slate.11",
                font_size=["0.84rem", "0.9rem", "0.95rem"],
                line_height="1.65",
                margin_top="2",
                flex_grow="1",
            ),
            # Domain Focus Tags
            rx.vstack(
                rx.text(
                    "OPERATIONAL DOMAINS & CREDENTIALS",
                    font_family="JetBrains Mono, monospace",
                    font_size="0.62rem",
                    color="slate.9",
                    letter_spacing="0.12em",
                ),
                rx.hstack(
                    *tag_badges,
                    spacing="2",
                    wrap="wrap",
                    width="100%",
                ),
                align_items="flex-start",
                spacing="2",
                width="100%",
                margin_top="2",
                padding_top="3",
                border_top="1px solid rgba(255, 255, 255, 0.06)",
            ),
            # External Verification Links
            rx.hstack(*links, spacing="3", margin_top="3", wrap="wrap") if links else rx.box(),
            align_items="flex-start",
            width="100%",
            height="100%",
            justify_content="space-between",
        ),
        class_name="chroma-dossier-panel",
        custom_attrs={"data-dossier-panel": member["idx"]},
        style={"display": "flex" if is_default else "none"},
        background="rgba(10, 10, 15, 0.78)",
        border="1px solid rgba(223, 188, 97, 0.25)",
        border_radius="8px",
        padding=["16px 16px", "20px 24px", "26px 30px"],
        width="100%",
        height="100%",
        box_shadow="0 12px 36px rgba(0, 0, 0, 0.55), inset 0 0 28px rgba(223, 188, 97, 0.03)",
    )


def directory() -> rx.Component:
    exec_members = [m for m in LEADERSHIP_DATA if m["tier"] == "EXECUTIVE CADRE"]
    adv_members = [m for m in LEADERSHIP_DATA if m["tier"] == "ADVISORY COUNCIL"]

    return base_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "EXECUTIVE CADRE & ADVISORY COUNCIL",
                    font_size=["0.62rem", "0.72rem"],
                    weight="bold",
                    color="#DFBC61",
                    letter_spacing="0.15em",
                    class_name="animate-fade-up",
                    text_align="center",
                    font_family="JetBrains Mono, monospace",
                ),
                rx.text(
                    "Leadership & Strategic Direction.",
                    font_size=["1.45rem", "1.9rem", "2.4rem"],
                    weight="bold",
                    letter_spacing="-0.03em",
                    line_height="1.1",
                    color="white",
                    font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100",
                    margin_bottom=["2", "3"],
                    text_align="center",
                ),
                # Split-Pane Interactive Dossier Console
                rx.grid(
                    # Left Pane: Interactive Personnel Roster
                    rx.vstack(
                        rx.text(
                            "EXECUTIVE CADRE // SELECT DOSSIER",
                            font_family="JetBrains Mono, monospace",
                            font_size="0.62rem",
                            font_weight="bold",
                            color="#DFBC61",
                            letter_spacing="0.12em",
                            margin_bottom="1",
                        ),
                        rx.grid(
                            *[roster_tab(m, is_default=(m["idx"] == "0")) for m in exec_members],
                            grid_template_columns=["repeat(2, 1fr)", "repeat(2, 1fr)", "1fr"],
                            spacing="2",
                            width="100%",
                        ),
                        rx.text(
                            "ADVISORY COUNCIL",
                            font_family="JetBrains Mono, monospace",
                            font_size="0.62rem",
                            font_weight="bold",
                            color="#DFBC61",
                            letter_spacing="0.12em",
                            margin_top="2",
                            margin_bottom="1",
                        ),
                        rx.grid(
                            *[roster_tab(m, is_default=False) for m in adv_members],
                            grid_template_columns=["repeat(2, 1fr)", "repeat(2, 1fr)", "1fr"],
                            spacing="2",
                            width="100%",
                        ),
                        align_items="flex-start",
                        spacing="1",
                        width="100%",
                    ),
                    # Right Pane: Active Dossier Telemetry View
                    rx.box(
                        *[dossier_panel(m, is_default=(m["idx"] == "0")) for m in LEADERSHIP_DATA],
                        width="100%",
                        height="100%",
                    ),
                    grid_template_columns=["1fr", "1fr", "320px 1fr", "340px 1fr"],
                    spacing="4",
                    width="100%",
                    max_width="1080px",
                    align_items="stretch",
                    class_name="animate-fade-up delay-200",
                ),
                rx.script(DOSSIER_JS),
                width="100%",
                max_width="1120px",
                align_items="center",
                padding_x=["4", "6", "8"],
                padding_top=["12px", "16px", "0px", "0px"],
                padding_bottom=["60px", "60px", "0px", "0px"],
            ),
            width="100%",
            min_height="100%",
            display="flex",
            flex_direction="column",
            align_items="center",
            justify_content=["flex-start", "flex-start", "center", "center"],
        )
    )