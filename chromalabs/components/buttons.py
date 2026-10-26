import reflex as rx

def primary_gold_button(*children, **kwargs) -> rx.Component:
    default_hover = {
        "bg": "#e6c455",
        "transform": "translateY(-2px)",
        "box_shadow": "0 0 35px rgba(223, 188, 97, 0.5), 0 0 20px rgba(168, 85, 247, 0.4)",
    }
    custom_hover = kwargs.pop("_hover", {})
    merged_hover = {**default_hover, **custom_hover}

    return rx.button(
        *children,
        bg=kwargs.pop("bg", "#DFBC61"),
        border=kwargs.pop("border", "none"),
        color=kwargs.pop("color", "black"),
        border_radius=kwargs.pop("border_radius", "4px"),
        font_weight=kwargs.pop("font_weight", "600"),
        cursor=kwargs.pop("cursor", "pointer"),
        transition=kwargs.pop("transition", "all 0.3s ease"),
        _hover=merged_hover,
        **kwargs
    )

def secondary_white_button(*children, **kwargs) -> rx.Component:
    default_hover = {
        "bg": "#f0f0f2",
        "transform": "translateY(-2px)",
        "box_shadow": "0 0 30px rgba(6, 182, 212, 0.4), 0 0 15px rgba(223, 188, 97, 0.3)",
    }
    custom_hover = kwargs.pop("_hover", {})
    merged_hover = {**default_hover, **custom_hover}

    return rx.button(
        *children,
        bg=kwargs.pop("bg", "white"),
        border=kwargs.pop("border", "none"),
        color=kwargs.pop("color", "black"),
        border_radius=kwargs.pop("border_radius", "4px"),
        font_weight=kwargs.pop("font_weight", "600"),
        cursor=kwargs.pop("cursor", "pointer"),
        transition=kwargs.pop("transition", "all 0.3s ease"),
        _hover=merged_hover,
        **kwargs
    )
