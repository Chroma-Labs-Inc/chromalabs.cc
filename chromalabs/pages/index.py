import reflex as rx
from chromalabs.components.layout import base_layout
from chromalabs.components.chroma_crystal import chroma_crystal
from chromalabs.components.buttons import primary_gold_button, secondary_white_button

def index() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                chroma_crystal(),
                rx.text(
                    "Illuminating the Next Generation of Compute.", 
                    font_size=["2.0rem", "2.6rem", "3.2rem", "3.8rem"],
                    weight="bold",
                    letter_spacing="-0.02em",
                    line_height="1.15",
                    max_width="860px",
                    color="white",
                    text_align="center",
                    class_name="animate-fade-up delay-100",
                    margin_top="3",
                    font_family="'EB Garamond', 'Playfair Display', serif",
                    text_shadow="0 6px 30px rgba(0, 0, 0, 0.9)",
                ),

                rx.hstack(
                    rx.link(
                        secondary_white_button(
                            "Request Beta Access", 
                            font_size="0.95rem", 
                            padding="16px 30px", 
                        ),
                        href="/developer", _hover={"text_decoration": "none"}
                    ),
                    rx.link(
                        primary_gold_button(
                            "Explore Capabilities", 
                            font_size="0.95rem", 
                            padding="16px 30px", 
                        ),
                        href="/capabilities", _hover={"text_decoration": "none"}
                    ),
                    spacing="5",
                    class_name="animate-fade-up delay-200",
                    pointer_events="auto",
                    flex_wrap="wrap",
                    justify_content="center",
                    margin_top=["28px", "36px", "44px"],
                ),
                align_items="center",
                justify_content="center",
                width="100%",
                padding_x=["4", "8", "12"],
                min_height="calc(100vh - 220px)",
                height="auto",
                padding_bottom=["40px", "50px", "60px"],
                pointer_events="none", 
                z_index="5", 
            ),
            sx={"& a": {"pointer_events": "auto"}},
            width="100%",
            position="relative",
            flex_grow="1",
        )
    )