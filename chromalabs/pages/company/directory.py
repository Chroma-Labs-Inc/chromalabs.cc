import reflex as rx
from chromalabs.components.layout import base_layout

def staff_card(name: str, role: str, spec: str, github: str = "", linkedin: str = "") -> rx.Component:
    links = []
    if github:
        links.append(rx.link(rx.text("GITHUB", font_size="0.65rem", font_family="JetBrains Mono, monospace", font_weight="bold", color="slate.10", _hover={"color": "#DFBC61"}), href=github, is_external=True))
    if linkedin:
        links.append(rx.link(rx.text("LINKEDIN", font_size="0.65rem", font_family="JetBrains Mono, monospace", font_weight="bold", color="slate.10", _hover={"color": "#DFBC61"}), href=linkedin, is_external=True))
        
    return rx.box(
        rx.vstack(
            rx.box(width="28px", height="2px", bg="#DFBC61", margin_bottom="1"),
            rx.text(name, color="white", font_size=["0.95rem", "1.05rem"], font_weight="700", line_height="1.2"),
            rx.text(role, color="#DFBC61", font_size=["0.7rem", "0.75rem"], font_family="JetBrains Mono, monospace", margin_top="0"),
            rx.text(spec, color="slate.11", font_size=["0.73rem", "0.78rem"], margin_top="2", line_height="1.45", flex_grow="1"),
            rx.hstack(*links, margin_top="2", spacing="3") if links else rx.box(),
            align_items="flex-start",
            height="100%",
        ),
        bg="rgba(10, 10, 14, 0.6)",
        border="1px solid rgba(255, 255, 255, 0.06)",
        border_radius="6px",
        padding=["12px 14px", "14px 16px", "16px 18px"],
        width="100%",
        height="100%",
        transition="all 0.2s ease",
        _hover={"bg": "rgba(18, 18, 24, 0.8)", "border": "1px solid rgba(223, 188, 97, 0.3)", "transform": "translateY(-2px)"},
    )

def directory() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "EXECUTIVE CADRE & ADVISORY COUNCIL",
                    font_size=["0.65rem", "0.75rem"], weight="bold", color="#DFBC61", letter_spacing="0.15em",
                    class_name="animate-fade-up", text_align="center", font_family="JetBrains Mono, monospace"
                ),
                rx.text(
                    "Leadership & Strategic Direction.", 
                    font_size=["1.5rem", "2.0rem", "2.6rem"], weight="bold", letter_spacing="-0.03em", line_height="1.15",
                    color="white", font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100", margin_bottom=["2", "3"], text_align="center"
                ),
                rx.grid(
                    staff_card(
                        "Michael Reser", 
                        "Founder, CEO, CTO & Systems Architect", 
                        "US Army Veteran and principal architect of Chroma Labs' computing physics. With foundational roots in robotics programs, STEM, and applied algorithms, Reser engineered the underlying mathematical frameworks and Lean 4 formal verification proofs de-risking the architecture.",
                        github="https://github.com/I-Am-Finite",
                        linkedin="https://www.linkedin.com/in/michaelreser/"
                    ),
                    staff_card(
                        "Bryan C. Coward", 
                        "Co-Founder, VP & Quantitative Architecture", 
                        "Quantitative systems and infrastructure architect. Coward directs global operations and enterprise financial architecture scaling Chroma's infrastructure.",
                        github="https://github.com/bmasterc",
                        linkedin="https://www.linkedin.com/in/cowardbryan/"
                    ),
                    staff_card(
                        "Connor Dudek", 
                        "Chief Marketing Officer (CMO)", 
                        "Directs corporate positioning, high-velocity brand architecture, strategic communications, and institutional market alignment across global technology sectors.",
                        linkedin="https://www.linkedin.com/in/connordudek/"
                    ),
                    staff_card(
                        "Megan F. Teague", 
                        "Secretary of the Board", 
                        "Directs corporate governance, intellectual property compliance, and strategic administration across Chroma Labs' operations and sovereign defense contracts.",
                    ),
                    grid_template_columns=["1fr", "repeat(2, 1fr)", "repeat(2, 1fr)", "repeat(4, 1fr)"],
                    spacing="3",
                    width="100%",
                    max_width="1220px",
                    class_name="animate-fade-up delay-200",
                    margin_bottom=["2", "3"]
                ),
                rx.text(
                    "ADVISORY COUNCIL",
                    font_size=["0.65rem", "0.7rem"], weight="bold", color="#DFBC61", letter_spacing="0.12em",
                    class_name="animate-fade-up delay-200", text_align="center", font_family="JetBrains Mono, monospace", margin_bottom="1"
                ),
                rx.grid(
                    staff_card(
                        "Dr. David Lary", 
                        "Scientific Validation & Defense Liaison", 
                        "Professor of Physics at UT Dallas and Director of the MINTS Lab (NASA AutoChem, SOFWERX). Dr. Lary advises on physical and thermodynamic validation across defense programs.",
                        linkedin="https://www.linkedin.com/in/davidlary/"
                    ),
                    staff_card(
                        "Houston Keene", 
                        "Legislative, Policy & Regulatory Strategy", 
                        "Founder of Keene Communications LLC, former Congressional Staffer and Capitol Hill correspondent. Advises on federal engagement and ITAR/EAR regulatory compliance.",
                        linkedin="https://www.linkedin.com/in/houston-k-15317799/"
                    ),
                    grid_template_columns=["1fr", "repeat(2, 1fr)"],
                    spacing="3",
                    width="100%",
                    max_width="750px",
                    class_name="animate-fade-up delay-300"
                ),
                width="100%",
                max_width="1220px",
                align_items="center",
                padding_x=["4", "6", "8"],
                padding_top=["20px", "24px", "0px", "0px"],
                padding_bottom=["80px", "80px", "0px", "0px"],
            ),
            width="100%",
            min_height="100%",
            display="flex",
            flex_direction="column",
            align_items="center",
            justify_content=["flex-start", "flex-start", "center", "center"],
        )
    )