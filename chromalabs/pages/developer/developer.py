import reflex as rx
from chromalabs.components.layout import base_layout
from chromalabs.components.buttons import primary_gold_button

def developer() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "DEVELOPER PORTAL",
                    font_size=["0.65rem", "0.75rem"], weight="bold", color="#DFBC61", letter_spacing="0.15em",
                    class_name="animate-fade-up", text_align="center", font_family="JetBrains Mono, monospace"
                ),
                rx.text(
                    "Architecture & Toolchain Access.", 
                    font_size=["1.6rem", "2.2rem", "2.8rem"], weight="bold", letter_spacing="-0.03em", line_height="1.1",
                    color="white", font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100", margin_bottom=["2", "3"], text_align="center"
                ),
                rx.text(
                    "Direct access to Chroma Labs compilation toolchains, hardware architectures, and formal Lean 4 verification suites is strictly controlled under federal export regulations. Beta endpoints and integration pipelines are provisioned exclusively to vetted institutional partners under bilateral non-disclosure agreement.",
                    font_size=["0.82rem", "0.9rem", "0.95rem"], color="slate.11", max_width="780px", text_align="center", margin_bottom=["4", "5"], line_height="1.55",
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
                        font_size=["0.65rem", "0.7rem"],
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