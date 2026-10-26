import reflex as rx
from chromalabs.components.layout import base_layout
from chromalabs.components.buttons import primary_gold_button

def mission() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "MISSION DIRECTIVE",
                    font_size=["0.65rem", "0.75rem"], weight="bold", color="#DFBC61", letter_spacing="0.15em",
                    class_name="animate-fade-up", text_align="center", font_family="JetBrains Mono, monospace"
                ),
                rx.text(
                    "Rewriting the Physics of Computation.", 
                    font_size=["1.6rem", "2.2rem", "2.8rem", "3.2rem"], weight="bold", letter_spacing="-0.03em", line_height="1.1",
                    color="white", font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100", margin_bottom="1", text_align="center"
                ),
                rx.text(
                    "Escaping the 80-Year Von Neumann Bottleneck.", 
                    font_size=["1.0rem", "1.2rem", "1.5rem"], weight="bold", letter_spacing="-0.02em", line_height="1.2",
                    color="#DFBC61", font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-200", margin_bottom=["3", "4"], text_align="center"
                ),
                rx.text(
                    "For eighty years, modern computing has remained constrained by the linear shuffling of data across resistive electrical buses. Frontier machine intelligence and high-performance computing have now collided with a catastrophic thermodynamic scaling wall—requiring gigawatts of power to overcome architectural inefficiencies.",
                    font_size=["0.82rem", "0.9rem", "0.95rem"], color="slate.11", max_width="800px", text_align="center", margin_bottom="3", line_height="1.55",
                    class_name="animate-fade-up delay-300"
                ),
                rx.text(
                    "At Chroma Labs, we believe incremental hardware optimization is insufficient. We fundamentally alter the physics of computation. Grounded in formally verified mathematics (Lean 4) and novel substrate execution paradigms, we eliminate redundant data movement and collapse thermodynamic dissipation from gigawatts to megawatts—establishing sovereign, provably secure foundations for the future.",
                    font_size=["0.82rem", "0.9rem", "0.95rem"], color="slate.11", max_width="800px", text_align="center", margin_bottom=["4", "5"], line_height="1.55",
                    class_name="animate-fade-up delay-300"
                ),
                rx.link(
                    primary_gold_button(
                        "EXPLORE CAPABILITIES", 
                        font_size="0.85rem",
                        letter_spacing="0.08em",
                        padding="14px 28px", 
                    ),
                    href="/capabilities", _hover={"text_decoration": "none"},
                    class_name="animate-fade-up delay-400"
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