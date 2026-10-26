import reflex as rx
from chromalabs.components.layout import base_layout

def feature_card(icon_tag: str, title: str, description: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.icon(tag=icon_tag, color="#DFBC61", size=24, margin_bottom="2"),
            rx.text(title, font_size="1.1rem", font_weight="bold", color="white", margin_bottom="2", line_height="1.2"),
            rx.text(description, color="slate.11", font_size="0.85rem", line_height="1.55"),
            align_items="flex-start",
            height="100%",
        ),
        padding="20px 22px",
        background="rgba(10, 10, 14, 0.6)",
        border="1px solid rgba(255, 255, 255, 0.06)",
        border_radius="8px",
        height="100%",
        _hover={"border": "1px solid rgba(223, 188, 97, 0.3)", "bg": "rgba(18, 18, 24, 0.8)"},
        transition="all 0.2s ease",
    )

def thermodynamics() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text("THERMODYNAMIC SCALING & COMPUTATIONAL SAVINGS", font_family="JetBrains Mono, monospace", font_size="0.75rem", color="#DFBC61", margin_bottom="1", letter_spacing="0.15em", class_name="animate-fade-up"),
                rx.text(
                    "Thermodynamic Scaling.", 
                    font_size=["2.0rem", "2.6rem", "3.2rem"], font_weight="800", line_height="1.1", color="white", letter_spacing="-0.03em", margin_bottom="2", text_align="center", font_family="'EB Garamond', 'Playfair Display', serif", class_name="animate-fade-up delay-100"
                ),
                rx.text(
                    "Bypassing the global compute power wall. By eliminating redundant memory movement at the foundational execution layer, Chroma Labs decouples processing capability from exponential energy consumption—shifting infrastructure baselines from gigawatts to megawatts.",
                    color="slate.11", font_size="0.95rem", line_height="1.55", max_width="760px", text_align="center", margin_bottom="4", class_name="animate-fade-up delay-200"
                ),
                rx.grid(
                    feature_card(
                        "zap",
                        "Gigawatt-to-Megawatt Decarbonization",
                        "Radically reducing the thermal footprint of compute clusters, eliminating multi-billion dollar power and cooling liabilities for next-generation datacenter facilities."
                    ),
                    feature_card(
                        "layers",
                        "Overcoming the Memory Wall",
                        "Standard architectures waste over 90% of their energy shuffling numbers across planar copper buses. We eliminate redundant memory movement at the physical layer."
                    ),
                    feature_card(
                        "flame",
                        "Sub-Landauer Dissipation Targets",
                        "Grounded in mathematical reversibility, operations execute with near-zero thermal dissipation, collapsing heat generation and cooling power requirements."
                    ),
                    feature_card(
                        "badge-check",
                        "Formally Verified Invariants (Lean 4)",
                        "Core execution invariants are formally verified in Lean 4. Every numerical bound is machine-checked from first principles, ensuring deterministic hardware stability."
                    ),
                    grid_template_columns=["1fr", "repeat(2, 1fr)", "repeat(2, 1fr)", "repeat(4, 1fr)"],
                    gap="4",
                    width="100%",
                    max_width="1200px",
                    class_name="animate-fade-up delay-300"
                ),
                rx.vstack(
                    rx.link(
                        rx.button("REQUEST INSTITUTIONAL BRIEFING", bg="#DFBC61", color="black", border_radius="4px", font_size="0.8rem", font_weight="bold", letter_spacing="0.08em", padding="14px 28px", cursor="pointer", transition="all 0.2s", _hover={"bg": "#e6c455", "transform": "translateY(-2px)"}),
                        href="/contact?topic=Thermodynamic%20Scaling%20Inquiry", _hover={"text_decoration": "none"}
                    ),
                    rx.text(
                        "DISCLOSURE: Full architectural specifications and proof suites are available under bilateral NDA for verified enterprise and defense partners.",
                        font_size="0.7rem",
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
                justify_content="center",
                width="100%",
                padding_x=["4", "6", "8"],
            ),
            width="100%", height="100%", display="flex", align_items="center", justify_content="center"
        )
    )
