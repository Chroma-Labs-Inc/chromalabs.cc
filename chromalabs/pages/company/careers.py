import reflex as rx
from chromalabs.components.layout import base_layout
from chromalabs.components.buttons import primary_gold_button

def careers() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "JOIN THE LAB",
                    font_size="0.75rem", weight="bold", color="#DFBC61", letter_spacing="0.15em",
                    class_name="animate-fade-up", text_align="center", font_family="JetBrains Mono, monospace"
                ),
                rx.text(
                    "Engineering & Research.", 
                    font_size=["2.0rem", "2.6rem", "3.2rem"], weight="bold", letter_spacing="-0.03em", line_height="1.1",
                    color="white", font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100", margin_bottom="2", text_align="center"
                ),
                rx.text(
                    "We are building a highly concentrated, elite technical cadre across mathematical formalization, deep-silicon engineering, and sovereign defense infrastructure.",
                    font_size="0.95rem", color="slate.11", max_width="740px", text_align="center", margin_bottom="4", line_height="1.55",
                    class_name="animate-fade-up delay-200"
                ),
                rx.center(
                    rx.vstack(
                        rx.icon(tag="briefcase", color="#DFBC61", size=32, margin_bottom="2"),
                        rx.text("Targeted Institutional Recruiting", color="white", font_size="1.2rem", font_weight="700"),
                        rx.text(
                            "Positions are opened on a mission-specific basis aligned with deployment schedules and defense partnerships. We welcome inquiries from elite contributors with backgrounds in Lean 4 formal verification, compiler architecture, and low-SWaP systems engineering.",
                            color="slate.11", text_align="center", max_width="560px", margin_top="1", font_size="0.85rem", line_height="1.55"
                        ),
                        rx.link(
                            primary_gold_button(
                                "SUBMIT RESEARCHER CV", 
                                font_size="0.82rem", 
                                letter_spacing="0.08em", 
                                padding="12px 24px", 
                                margin_top="4",
                            ),
                            href="/contact?topic=Research%20and%20Engineering%20Candidacy", _hover={"text_decoration": "none"}
                        ),
                        align_items="center",
                    ),
                    bg="rgba(10, 10, 14, 0.6)",
                    border="1px solid rgba(255, 255, 255, 0.06)",
                    border_radius="8px",
                    padding="32px 28px",
                    width="100%",
                    max_width="720px",
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