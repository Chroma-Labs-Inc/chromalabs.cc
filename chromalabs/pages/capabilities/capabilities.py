import reflex as rx
from chromalabs.components.layout import base_layout

def capability_card(tag: str, title: str, description: str, link_url: str, icon_tag: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon(tag=icon_tag, color="#DFBC61", size=20),
                rx.text(tag, font_family="JetBrains Mono, monospace", font_size=["0.65rem", "0.7rem"], color="#DFBC61", letter_spacing="0.12em", font_weight="bold"),
                spacing="2",
                align_items="center",
                margin_bottom="1",
            ),
            rx.text(title, font_size=["1.05rem", "1.15rem"], font_weight="bold", color="white", margin_bottom="1", line_height="1.2"),
            rx.text(description, color="slate.11", font_size=["0.78rem", "0.82rem"], line_height="1.5", flex_grow="1"),
            rx.link(
                rx.hstack(
                    rx.text("EXPLORE SECTOR", font_family="JetBrains Mono, monospace", font_size="0.75rem", font_weight="bold", color="#DFBC61"),
                    rx.icon(tag="arrow-right", color="#DFBC61", size=14),
                    spacing="2",
                    align_items="center",
                    margin_top="3",
                    _hover={"transform": "translateX(3px)"},
                    transition="transform 0.2s ease",
                ),
                href=link_url,
                _hover={"text_decoration": "none"},
            ),
            align_items="flex-start",
            height="100%",
        ),
        padding=["14px 16px", "16px 18px", "20px 20px"],
        background="rgba(10, 10, 14, 0.6)",
        border="1px solid rgba(255, 255, 255, 0.06)",
        border_radius="8px",
        height="100%",
        transition="all 0.2s ease",
        _hover={"bg": "rgba(18, 18, 24, 0.8)", "border": "1px solid rgba(223, 188, 97, 0.3)", "transform": "translateY(-2px)"},
    )

def capabilities() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text("FOUNDATIONAL CAPABILITIES & DOMAINS", font_family="JetBrains Mono, monospace", font_size=["0.65rem", "0.75rem"], color="#DFBC61", margin_bottom="1", letter_spacing="0.15em", class_name="animate-fade-up"),
                rx.text(
                    "Architecting Thermodynamic Scale.", 
                    font_size=["1.6rem", "2.2rem", "2.8rem"], weight="bold", letter_spacing="-0.03em", line_height="1.1",
                    text_align="center", margin_bottom="2",
                    color="white",
                    font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100",
                ),
                rx.text(
                    "For eighty years, computing has been bounded by the linear movement of data across resistive physical buses. Chroma Labs eliminates this architectural ceiling. Grounded in formally verified mathematics (Lean 4), we engineer sovereign computing architectures that collapse power consumption, maximize computational density, and ensure unassailable cryptographic security.",
                    font_size=["0.82rem", "0.9rem", "0.95rem"], color="slate.11", max_width="820px", text_align="center", margin_bottom=["3", "4"], line_height="1.55",
                    class_name="animate-fade-up delay-200",
                ),
                rx.grid(
                    capability_card(
                        "THERMODYNAMIC SAVINGS",
                        "Thermodynamic Scaling",
                        "Shifting the energy baseline of frontier machine intelligence from gigawatts to megawatts. Bypassing planar thermal scaling walls through decoupled data movement.",
                        "/capabilities/thermodynamics",
                        "zap"
                    ),
                    capability_card(
                        "COGNITIVE COMPUTE",
                        "Artificial Intelligence",
                        "Decoupled cognitive scale. Native structural sparsity without synthetic pruning penalties, eliminating planar memory bus shuttling with provable mathematical stability.",
                        "/capabilities/ai",
                        "cpu"
                    ),
                    capability_card(
                        "SOVEREIGN DEFENSE",
                        "Defense & Security",
                        "USML Category XI compliant sovereign edge architectures. Engineered for physical-layer cryptographic isolation, Zero-TEMPEST resilience, and post-quantum integrity.",
                        "/capabilities/defense",
                        "shield-check"
                    ),
                    capability_card(
                        "AUTONOMOUS SYSTEMS",
                        "Autonomous Robotics",
                        "Milliwatt-budget perception and visual-inertial odometry. RF-silent, GPS-denied tactical swarm navigation fully immune to electronic warfare jamming.",
                        "/capabilities/robotics",
                        "crosshair"
                    ),
                    grid_template_columns=["1fr", "repeat(2, 1fr)", "repeat(2, 1fr)", "repeat(4, 1fr)"],
                    spacing="3",
                    width="100%",
                    max_width="1220px",
                    class_name="animate-fade-up delay-300",
                ),
                rx.box(
                    rx.text(
                        "NOTICE: Detailed architectural blueprints, formal proof suites, and silicon benchmark telemetry are disclosed exclusively under institutional bilateral NDA following verification of interest and compliance with applicable export controls (ITAR / EAR).",
                        font_size=["0.65rem", "0.7rem"],
                        color="slate.9",
                        line_height="1.5",
                        text_align="center",
                        max_width="780px",
                        font_family="JetBrains Mono, monospace"
                    ),
                    margin_top="3",
                    padding=["8px 14px", "10px 20px"],
                    background="rgba(255, 255, 255, 0.02)",
                    border="1px solid rgba(255, 255, 255, 0.05)",
                    border_radius="6px",
                    class_name="animate-fade-up delay-400",
                ),
                width="100%",
                max_width="1220px",
                padding_x=["4", "6", "8"],
                padding_top=["20px", "24px", "0px", "0px"],
                padding_bottom=["80px", "80px", "0px", "0px"],
                align_items="center",
            ),
            width="100%",
            min_height="100%",
            display="flex",
            flex_direction="column",
            align_items="center",
            justify_content=["flex-start", "flex-start", "center", "center"],
        )
    )
