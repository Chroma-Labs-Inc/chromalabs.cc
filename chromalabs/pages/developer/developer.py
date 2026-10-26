import reflex as rx
from chromalabs.components.layout import base_layout
from chromalabs.components.buttons import primary_gold_button

def developer() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "DEVELOPER PORTAL",
                    font_size="0.75rem", weight="bold", color="#DFBC61", letter_spacing="0.15em",
                    class_name="animate-fade-up", text_align="center", font_family="JetBrains Mono, monospace"
                ),
                rx.text(
                    "Architecture & Toolchain Access.", 
                    font_size=["2.0rem", "2.6rem", "3.2rem"], weight="bold", letter_spacing="-0.03em", line_height="1.1",
                    color="white", font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100", margin_bottom="3", text_align="center"
                ),
                rx.text(
                    "Direct access to Chroma Labs compilation toolchains, hardware architectures, and formal Lean 4 verification suites is strictly controlled under federal export regulations. Beta endpoints and integration pipelines are provisioned exclusively to vetted institutional partners under bilateral non-disclosure agreement.",
                    font_size="0.95rem", color="slate.11", max_width="780px", text_align="center", margin_bottom="5", line_height="1.55",
                    class_name="animate-fade-up delay-200"
                ),
                rx.vstack(
                    rx.link(
                        primary_gold_button(
                            "REQUEST INSTITUTIONAL CLEARANCE", 
                            font_size="0.82rem",
                            letter_spacing="0.08em",
                            padding="14px 28px",
                        ),
                        href="/contact?topic=Beta%20Access%20and%20API%20Clearance", 
                        _hover={"text_decoration": "none"},
                    ),
                    rx.text(
                        "ITAR / USML COMPLIANCE: Submissions are reviewed directly by leadership. Please transmit your request using your official institutional, defense, or enterprise email address.",
                        font_size="0.7rem",
                        color="slate.9",
                        max_width="680px",
                        margin_top="2",
                        font_family="JetBrains Mono, monospace",
                        text_align="center"
                    ),
                    align_items="center",
                    margin_top="3",
                    class_name="animate-fade-up delay-300"
                ),
                width="100%",
                max_width="1000px",
                align_items="center", justify_content="center",
                padding_x=["4", "6", "8"],
            ),
            width="100%",
            height="100%",
            display="flex",
            align_items="center",
            justify_content="center"
        )
    )