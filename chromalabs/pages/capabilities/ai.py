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

def ai() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text("FRONTIER INTELLIGENCE & COGNITIVE COMPUTATION", font_family="JetBrains Mono, monospace", font_size=["0.65rem", "0.75rem"], color="#DFBC61", margin_bottom="1", letter_spacing="0.15em", class_name="animate-fade-up"),
                rx.text(
                    "Artificial Intelligence.", 
                    font_size=["1.6rem", "2.2rem", "2.8rem"], font_weight="800", line_height="1.1", color="white", letter_spacing="-0.03em", margin_bottom="2", text_align="center", font_family="'EB Garamond', 'Playfair Display', serif", class_name="animate-fade-up delay-100"
                ),
                rx.text(
                    "Frontier machine intelligence is hitting a catastrophic thermodynamic scaling wall. Chroma Labs restructures cognitive computation from first principles, decoupling processing capability from exponential power draw to deliver exascale capability within a fraction of the thermal footprint.",
                    color="slate.11", font_size=["0.82rem", "0.9rem", "0.95rem"], line_height="1.55", max_width="760px", text_align="center", margin_bottom=["3", "4"], class_name="animate-fade-up delay-200"
                ),
                rx.grid(
                    feature_card(
                        "zap",
                        "Thermodynamic Decarbonization",
                        "Drastically reducing the thermal dissipation of model training and inferencing, shifting datacenter infrastructure requirements from gigawatts to megawatts."
                    ),
                    feature_card(
                        "layers",
                        "Overcoming Planar Bottlenecks",
                        "Standard architectures spend over 90% of their energy moving weights back and forth across planar copper buses. We eliminate redundant memory movement at the foundational physical layer."
                    ),
                    feature_card(
                        "cpu",
                        "Native Structural Sparsity",
                        "Architected natively for extreme mathematical sparsity. Systems evaluate only active computational pathways, eliminating non-contributing states without synthetic pruning penalties."
                    ),
                    feature_card(
                        "badge-check",
                        "Formally Proven Invariants (Lean 4)",
                        "Core mathematical invariants are formally machine-checked in Lean 4 to guarantee bounded execution, eliminating runtime edge-case failure and numerical drift."
                    ),
                    grid_template_columns=["1fr", "repeat(2, 1fr)", "repeat(2, 1fr)", "repeat(4, 1fr)"],
                    gap="3",
                    width="100%",
                    max_width="1200px",
                    class_name="animate-fade-up delay-300"
                ),
                rx.vstack(
                    rx.link(
                        rx.button("REQUEST INSTITUTIONAL BRIEFING", bg="#DFBC61", color="black", border_radius="4px", font_size="0.8rem", font_weight="bold", letter_spacing="0.08em", padding="14px 28px", cursor="pointer", transition="all 0.2s", _hover={"bg": "#e6c455", "transform": "translateY(-2px)"}),
                        href="/contact?topic=Artificial%20Intelligence%20Inquiry", _hover={"text_decoration": "none"}
                    ),
                    rx.text(
                        "DISCLOSURE: Full architectural specifications and proof suites are available under bilateral NDA for verified enterprise and defense partners.",
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