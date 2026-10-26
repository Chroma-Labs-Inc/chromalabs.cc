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

def defense() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text("SOVEREIGN DEFENSE & SECURITY", font_family="JetBrains Mono, monospace", font_size="0.75rem", color="#DFBC61", margin_bottom="1", letter_spacing="0.15em", class_name="animate-fade-up"),
                rx.text(
                    "Defense & Security.", 
                    font_size=["2.0rem", "2.6rem", "3.2rem"], font_weight="800", line_height="1.1", color="white", letter_spacing="-0.03em", margin_bottom="2", text_align="center", font_family="'EB Garamond', 'Playfair Display', serif", class_name="animate-fade-up delay-100"
                ),
                rx.text(
                    "Sovereign computing architectures engineered under USML Category XI compliance. Delivering physical-layer cryptographic isolation, sub-ambient electromagnetic emissions, and uncontested edge superiority in contested peer-adversary environments.",
                    color="slate.11", font_size="0.95rem", line_height="1.55", max_width="760px", text_align="center", margin_bottom="4", class_name="animate-fade-up delay-200"
                ),
                rx.grid(
                    feature_card(
                        "shield-check",
                        "Physical-Layer Cryptographic Isolation",
                        "Security anchored in mathematical reversibility. Sub-ambient electromagnetic emanations (Zero-TEMPEST resilience) eliminate side-channel vulnerabilities, blinding overhead signals intelligence."
                    ),
                    feature_card(
                        "lock",
                        "Formally Proven Foundations (Lean 4)",
                        "Cryptographic structures and number-theoretic primitives formally verified in Lean 4, establishing machine-checked post-quantum mathematical soundness and resilience."
                    ),
                    feature_card(
                        "crosshair",
                        "RF-Silent Tactical Autonomy",
                        "Extreme low-power autonomous perception operating on milliwatt battery budgets—requiring zero radio uplinks and fully immune to electronic warfare jamming."
                    ),
                    feature_card(
                        "activity",
                        "Uncontested Edge Dominance",
                        "Real-time tactical processing directly at the physical point of need without reliance on vulnerable satellite communication networks or high-latency cloud architectures."
                    ),
                    grid_template_columns=["1fr", "repeat(2, 1fr)", "repeat(2, 1fr)", "repeat(4, 1fr)"],
                    gap="4",
                    width="100%",
                    max_width="1200px",
                    class_name="animate-fade-up delay-300"
                ),
                rx.vstack(
                    rx.link(
                        rx.button("REQUEST CLEARANCE & NDA", bg="#DFBC61", color="black", border_radius="4px", font_size="0.8rem", font_weight="bold", letter_spacing="0.08em", padding="14px 28px", cursor="pointer", transition="all 0.2s", _hover={"bg": "#e6c455", "transform": "translateY(-2px)"}),
                        href="/contact?topic=Defense%20and%20Cryptographic%20Clearance", _hover={"text_decoration": "none"}
                    ),
                    rx.text(
                        "ITAR / USML COMPLIANCE: Architectural briefings, test telemetry, and hardware evaluations are provisioned strictly to verified US defense entities, allied primes, and program offices under bilateral non-disclosure agreement.",
                        font_size="0.7rem",
                        color="slate.9",
                        max_width="740px",
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
