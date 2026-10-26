import reflex as rx
from chromalabs.components.chroma_crystal import chroma_nav_crystal

def menu_item(text: str, url: str) -> rx.Component:
    return rx.box(
        rx.link(
            rx.text(text, color="slate.11", font_size="1.1rem", transition="color 0.2s ease", _hover={"color": "white"}),
            href=url,
            width="100%",
            display="block", color="inherit", _hover={"text_decoration": "none"}
        ),
        bg="transparent",
        _hover={"bg": "rgba(255, 255, 255, 0.05)"},
        padding_y="16px",
        padding_x="20px",
        cursor="pointer",
        transition="background 0.2s ease",
        border_radius="4px",
    )

def navbar_dropdown(title: str, items: list[tuple[str, str]]) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.button(
                rx.text(title, color="slate.11", font_size="0.9rem", font_weight="500", letter_spacing="0.05em", transition="color 0.2s ease"),
                bg="transparent",
                border="1px solid transparent",
                padding="8px 16px",
                border_radius="6px",
                cursor="pointer",
                transition="all 0.2s ease",
                _hover={
                    "bg": "rgba(255, 255, 255, 0.05)", 
                    "border": "1px solid rgba(255, 255, 255, 0.1)",
                    "box_shadow": "0 0 15px rgba(255, 255, 255, 0.05)",
                    "color": "white"
                },
                height="auto",
            )
        ),
        rx.hover_card.content(
            *[menu_item(label, url) for label, url in items],
            bg="rgba(5, 5, 5, 0.95)",
            border="1px solid rgba(255, 255, 255, 0.08)",
            backdrop_filter="blur(24px)",
            padding="6px",
            border_radius="8px",
            box_shadow="0 10px 40px rgba(0,0,0,0.5)",
            min_width="220px",
        )
    )

def navbar() -> rx.Component:
    desktop_nav = rx.hstack(
        navbar_dropdown("CAPABILITIES", [
            ("Capabilities Overview", "/capabilities"),
            ("Thermodynamic Scaling", "/capabilities/thermodynamics"),
            ("Artificial Intelligence", "/capabilities/ai"),
            ("Defense & Security", "/capabilities/defense"),
            ("Autonomous Robotics", "/capabilities/robotics"),
        ]),
        navbar_dropdown("RESEARCH", [
            ("Research Log", "/research/log"),
            ("Published Papers", "/research/papers"),
        ]),
        navbar_dropdown("COMPANY", [
            ("Mission", "/company/mission"),
            ("Careers", "/company/careers"),
            ("Staff Directory", "/company/directory"),
            ("Contact Us", "/contact"),
        ]),
        rx.link(
            rx.button(
                rx.text("DEVELOPER PORTAL", color="slate.11", font_size="0.9rem", font_weight="500", letter_spacing="0.05em", transition="color 0.2s ease"),
                bg="transparent",
                border="1px solid transparent",
                padding="8px 16px",
                border_radius="6px",
                cursor="pointer",
                transition="all 0.2s ease",
                _hover={
                    "bg": "rgba(255, 255, 255, 0.05)", 
                    "border": "1px solid rgba(255, 255, 255, 0.1)",
                    "box_shadow": "0 0 15px rgba(255, 255, 255, 0.05)",
                    "color": "white"
                },
                height="auto",
            ),
            href="/developer", _hover={"text_decoration": "none"},
            margin_right=["0px", "4px", "12px", "16px"],
        ),
        display=["none", "none", "flex", "flex"],
        align_items="center",
        spacing="4",
    )

    mobile_nav = rx.box(
        rx.menu.root(
            rx.menu.trigger(
                rx.icon(tag="menu", color="white", size=32, cursor="pointer")
            ),
            rx.menu.content(
                rx.text("CAPABILITIES", padding="8px 12px", color="#DFBC61", font_size="0.75rem", font_weight="bold", letter_spacing="0.1em"),
                rx.menu.item(rx.link("Capabilities Overview", href="/capabilities", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.item(rx.link("Thermodynamic Scaling", href="/capabilities/thermodynamics", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.item(rx.link("Artificial Intelligence", href="/capabilities/ai", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.item(rx.link("Defense & Security", href="/capabilities/defense", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.item(rx.link("Autonomous Robotics", href="/capabilities/robotics", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.separator(),
                rx.text("RESEARCH", padding="8px 12px", color="#DFBC61", font_size="0.75rem", font_weight="bold", letter_spacing="0.1em"),
                rx.menu.item(rx.link("Research Log", href="/research/log", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.item(rx.link("Published Papers", href="/research/papers", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.separator(),
                rx.text("COMPANY", padding="8px 12px", color="#DFBC61", font_size="0.75rem", font_weight="bold", letter_spacing="0.1em"),
                rx.menu.item(rx.link("Mission", href="/company/mission", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.item(rx.link("Careers", href="/company/careers", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.item(rx.link("Staff Directory", href="/company/directory", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.item(rx.link("Contact Us", href="/contact", width="100%", display="block", color="inherit", _hover={"text_decoration": "none"})),
                rx.menu.separator(),
                rx.menu.item(rx.link("DEVELOPER PORTAL", href="/developer", width="100%", display="block", color="inherit", font_weight="bold", _hover={"text_decoration": "none"})),
                bg="rgba(10, 10, 10, 0.95)",
                color="slate.11",
                border="1px solid rgba(255, 255, 255, 0.08)",
            )
        ),
        display=["block", "block", "none", "none"]
    )

    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    chroma_nav_crystal(),
                    rx.hstack(
                        rx.text("CHROMA", font_weight="800", font_size=["1.05rem", "1.15rem"], color="white", letter_spacing="0.12em"),
                        rx.text("LABS", font_weight="400", font_size=["1.05rem", "1.15rem"], color="#DFBC61", letter_spacing="0.12em"),
                        spacing="2",
                        align_items="center",
                    ),
                    align_items="center",
                    spacing="3",
                ),
                href="/", _hover={"text_decoration": "none"}
            ),
            rx.spacer(),
            desktop_nav,
            mobile_nav,
            width="100%",
            padding_x=["16px", "24px", "36px", "48px"],
            height="56px",
            align_items="center",
        ),
        rx.box(
            position="absolute",
            bottom="0",
            left="0",
            width="100%",
            height="1px",
            background="linear-gradient(90deg, rgba(223, 188, 97, 0) 0%, rgba(223, 188, 97, 0.15) 20%, rgba(223, 188, 97, 0.75) 50%, rgba(223, 188, 97, 0.15) 80%, rgba(223, 188, 97, 0) 100%)",
            box_shadow="0 0 16px rgba(223, 188, 97, 0.45), 0 0 4px rgba(223, 188, 97, 0.7)",
            pointer_events="none",
        ),
        width="100%",
        height="56px",
        position="fixed",
        top="0",
        left="0",
        background="rgba(0, 0, 0, 0.6)",
        backdrop_filter="blur(24px)",
        z_index="50",
    )