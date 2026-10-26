import reflex as rx
from chromalabs.components.layout import base_layout

def feature_card(icon_tag: str, title: str, description: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.icon(tag=icon_tag, color="#DFBC61", size=22, margin_bottom="1"),
            rx.text(title, font_size=["1.0rem", "1.1rem"], font_weight="bold", color="white", margin_bottom="1", line_height="1.2"),
            rx.text(description, color="slate.11", font_size=["0.78rem", "0.85rem"], line_height="1.5"),
            align_items="flex-start",
            height="100%",
        ),
        padding=["14px 16px", "16px 18px", "20px 22px"],
        background="rgba(10, 10, 14, 0.6)",
        border="1px solid rgba(255, 255, 255, 0.06)",
        border_radius="8px",
        height="100%",
        _hover={"border": "1px solid rgba(223, 188, 97, 0.3)", "bg": "rgba(18, 18, 24, 0.8)"},
        transition="all 0.2s ease",
    )

def robotics() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text("AUTONOMOUS ROBOTICS & EDGE COMPUTATION", font_family="JetBrains Mono, monospace", font_size=["0.65rem", "0.75rem"], color="#DFBC61", margin_bottom="1", letter_spacing="0.15em", class_name="animate-fade-up"),
                rx.text(
                    "Autonomous Robotics.", 
                    font_size=["1.6rem", "2.2rem", "2.8rem"], font_weight="800", line_height="1.1", color="white", letter_spacing="-0.03em", margin_bottom="2", text_align="center", font_family="'EB Garamond', 'Playfair Display', serif", class_name="animate-fade-up delay-100"
                ),
                rx.text(
                    "Sovereign cognitive systems at the physical edge. Engineered for extreme low-SWaP constraints, Chroma Labs enables high-speed visual perception, continuous spatial awareness, and real-time motion planning operating on milliwatt battery budgets.",
                    color="slate.11", font_size=["0.82rem", "0.9rem", "0.95rem"], line_height="1.55", max_width="760px", text_align="center", margin_bottom=["3", "4"], class_name="animate-fade-up delay-200"
                ),
                rx.grid(
                    feature_card(
                        "crosshair",
                        "Milliwatt Perception & Odometry",
                        "High-speed visual-inertial odometry executing at thousands of frames per second on battery power—enabling continuous autonomous navigation on ultra-compact robotic platforms."
                    ),
                    feature_card(
                        "shield-off",
                        "RF-Silent, Jam-Immune Navigation",
                        "Operates in completely GPS-denied and radio-silent environments without reliance on external radio uplinks, rendering systems immune to electronic warfare and spoofing."
                    ),
                    feature_card(
                        "zap",
                        "Zero-Latency Physical Reaction",
                        "Direct execution of perception and kinematic models collapses control latency, providing instantaneous obstacle avoidance and trajectory resolution in contested physical spaces."
                    ),
                    feature_card(
                        "badge-check",
                        "Formally Proven Kinematic Bounds",
                        "Motion invariants and spatial safety constraints are formally machine-checked in Lean 4 to eliminate edge-case control instability and guarantee bounded physical execution."
                    ),
                    grid_template_columns=["1fr", "repeat(2, 1fr)", "repeat(2, 1fr)", "repeat(4, 1fr)"],
                    gap="3",
                    width="100%",
                    max_width="1200px",
                    class_name="animate-fade-up delay-300"
                ),
                rx.vstack(
                    rx.link(
                        rx.button("REQUEST ROBOTICS BRIEFING", bg="#DFBC61", color="black", border_radius="4px", font_size="0.8rem", font_weight="bold", letter_spacing="0.08em", padding="14px 28px", cursor="pointer", transition="all 0.2s", _hover={"bg": "#e6c455", "transform": "translateY(-2px)"}),
                        href="/contact?topic=Autonomous%20Robotics%20Inquiry", _hover={"text_decoration": "none"}
                    ),
                    rx.text(
                        "DISCLOSURE: Full architectural specifications and edge integration guidelines are provisioned under bilateral NDA for verified robotics partners and defense program offices.",
                        font_size=["0.65rem", "0.7rem"],
                        color="slate.9",
                        margin_top="2",
                        font_family="JetBrains Mono, monospace",
                        text_align="center"
                    ),
                    align_items="center",
                    margin_top="4",
                    class_name="animate-fade-up delay-400"
                ),
                align_items="center",
                width="100%",
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
