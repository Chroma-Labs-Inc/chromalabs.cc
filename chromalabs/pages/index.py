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
                    font_size=["1.65rem", "2.2rem", "2.8rem", "3.6rem"],
                    weight="bold",
                    letter_spacing="-0.02em",
                    line_height="1.15",
                    max_width="860px",
                    color="white",
                    text_align="center",
                    class_name="animate-fade-up delay-100",
                    margin_top=["18px", "14px", "8px", "6px"],
                    font_family="'EB Garamond', 'Playfair Display', serif",
                    text_shadow="0 6px 30px rgba(0, 0, 0, 0.9)",
                ),

                rx.hstack(
                    rx.link(
                        secondary_white_button(
                            "Request Beta Access", 
                            font_size=["0.85rem", "0.95rem"], 
                            padding=["12px 22px", "14px 26px", "16px 30px"], 
                        ),
                        href="/developer", _hover={"text_decoration": "none"}
                    ),
                    rx.link(
                        primary_gold_button(
                            "Explore Capabilities", 
                            font_size=["0.85rem", "0.95rem"], 
                            padding=["12px 22px", "14px 26px", "16px 30px"], 
                        ),
                        href="/capabilities", _hover={"text_decoration": "none"}
                    ),
                    spacing="4",
                    class_name="animate-fade-up delay-200",
                    pointer_events="auto",
                    flex_wrap="wrap",
                    justify_content="center",
                    margin_top=["18px", "24px", "36px"],
                ),
                align_items="center",
                justify_content="center",
                width="100%",
                padding_x=["4", "6", "8", "12"],
                height="auto",
                min_height="auto",
                padding_bottom=["20px", "30px", "40px"],
                z_index="5", 
            ),
            width="100%",
            min_height="100%",
            display="flex",
            flex_direction="column",
            align_items="center",
            justify_content="center",
            position="relative",
        )
    )