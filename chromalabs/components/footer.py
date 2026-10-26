import reflex as rx

def footer() -> rx.Component:
    return rx.box(
        rx.box(
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="1px",
            background="linear-gradient(90deg, rgba(223, 188, 97, 0) 0%, rgba(223, 188, 97, 0.15) 20%, rgba(223, 188, 97, 0.75) 50%, rgba(223, 188, 97, 0.15) 80%, rgba(223, 188, 97, 0) 100%)",
            box_shadow="0 0 16px rgba(223, 188, 97, 0.45), 0 0 4px rgba(223, 188, 97, 0.7)",
            pointer_events="none",
        ),
        rx.flex(
            rx.text(
                "© 2026 Chroma Labs, Inc.™",
                color="slate.8",
                font_family="JetBrains Mono, monospace",
                font_size="0.75rem",
                letter_spacing="0.08em",
                text_align=["center", "center", "left"]
            ),
            rx.spacer(display=["none", "none", "block"]),
            rx.text(
                "17350 STATE HWY 249, STE 220 #37670 · HOUSTON, TX 77064",
                color="slate.8",
                font_size="0.75rem",
                font_family="JetBrains Mono, monospace",
                text_align=["center", "center", "right"]
            ),
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding_x=["4", "8", "16"],
            height="56px",
            flex_direction=["column", "column", "row"],
            align_items="center",
            justify_content="center",
            spacing="2"
        ),
        width="100%",
        height="56px",
        position="fixed",
        bottom="0",
        left="0",
        background="rgba(0, 0, 0, 0.6)",
        backdrop_filter="blur(24px)",
        z_index="50",
    )