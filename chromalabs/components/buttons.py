import reflex as rx

def primary_gold_button(*children, **kwargs) -> rx.Component:
    default_hover = {
        "bg": "#e6c455",
        "transform": "translateY(-2px)",
        "box_shadow": "0 0 35px rgba(223, 188, 97, 0.5), 0 0 20px rgba(168, 85, 247, 0.4)",
    }
    default_active = {
        "bg": "#DFBC61",
        "transform": "scale(0.98)",
        "box_shadow": "0 0 25px rgba(223, 188, 97, 0.6)",
        "outline": "none",
    }
    custom_hover = kwargs.pop("_hover", {})
    custom_active = kwargs.pop("_active", {})
    merged_hover = {**default_hover, **custom_hover}
    merged_active = {**default_active, **custom_active}

    return rx.button(
        *children,
        bg=kwargs.pop("bg", "#DFBC61"),
        border=kwargs.pop("border", "none"),
        color=kwargs.pop("color", "black"),
        border_radius=kwargs.pop("border_radius", "4px"),
        font_weight=kwargs.pop("font_weight", "600"),
        cursor=kwargs.pop("cursor", "pointer"),
        transition=kwargs.pop("transition", "all 0.25s ease"),
        _hover=merged_hover,
        _active=merged_active,
        _focus={"outline": "2px solid #DFBC61", "outline_offset": "2px"},
        **kwargs
    )

def secondary_white_button(*children, **kwargs) -> rx.Component:
    default_hover = {
        "bg": "#f0f0f2",
        "transform": "translateY(-2px)",
        "box_shadow": "0 0 30px rgba(6, 182, 212, 0.4), 0 0 15px rgba(223, 188, 97, 0.3)",
    }
    default_active = {
        "bg": "#e4e4e7",
        "transform": "scale(0.98)",
        "box_shadow": "0 0 20px rgba(223, 188, 97, 0.4)",
        "outline": "none",
    }
    custom_hover = kwargs.pop("_hover", {})
    custom_active = kwargs.pop("_active", {})
    merged_hover = {**default_hover, **custom_hover}
    merged_active = {**default_active, **custom_active}

    return rx.button(
        *children,
        bg=kwargs.pop("bg", "white"),
        border=kwargs.pop("border", "none"),
        color=kwargs.pop("color", "black"),
        border_radius=kwargs.pop("border_radius", "4px"),
        font_weight=kwargs.pop("font_weight", "600"),
        cursor=kwargs.pop("cursor", "pointer"),
        transition=kwargs.pop("transition", "all 0.25s ease"),
        _hover=merged_hover,
        _active=merged_active,
        _focus={"outline": "2px solid #DFBC61", "outline_offset": "2px"},
        **kwargs
    )
