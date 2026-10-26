import reflex as rx
import urllib.parse
from chromalabs.components.layout import base_layout
from chromalabs.components.buttons import primary_gold_button

class ContactState(rx.State):
    form_topic: str = ""

    def load_topic(self):
        t = self.router.page.params.get("topic", "")
        if isinstance(t, list) and len(t) > 0:
            self.form_topic = t[0]
        else:
            self.form_topic = str(t)

    def handle_submit(self, form_data: dict):
        topic = form_data.get("topic", "")
        email = form_data.get("email", "")
        company = form_data.get("company", "")
        msg = form_data.get("message", "")
        
        body = f"Agency/Org: {company}\nEmail: {email}\n\nMessage:\n{msg}"
        encoded_subject = urllib.parse.quote(topic)
        encoded_body = urllib.parse.quote(body)
        
        return rx.redirect(f"mailto:michael@chromalabs.cc?subject={encoded_subject}&body={encoded_body}")

def contact() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "INSTITUTIONAL ENGAGEMENT",
                    font_size="0.75rem", weight="bold", color="#DFBC61", letter_spacing="0.15em",
                    class_name="animate-fade-up", text_align="center", font_family="JetBrains Mono, monospace"
                ),
                rx.text(
                    "Contact the Lab.", 
                    font_size=["1.8rem", "2.2rem", "2.6rem"], weight="bold", letter_spacing="-0.03em", line_height="1.1",
                    color="white", font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100", margin_bottom="3", text_align="center"
                ),
                rx.box(
                    rx.form(
                        rx.vstack(
                            rx.text("SECURE COMMUNIQUE", font_size="0.85rem", font_weight="bold", color="white", letter_spacing="0.1em", margin_bottom="1", font_family="JetBrains Mono, monospace"),
                            rx.input(name="topic", placeholder="Subject / Technical Inquiry", default_value=ContactState.form_topic, width="100%", size="2", bg="rgba(0,0,0,0.5)", border_color="rgba(255,255,255,0.1)", color="white", required=True, auto_complete=False),
                            rx.input(name="email", type="email", placeholder="Institutional / Defense / Enterprise Email", width="100%", size="2", bg="rgba(0,0,0,0.5)", border_color="rgba(255,255,255,0.1)", color="white", required=True, auto_complete=False),
                            rx.input(name="company", placeholder="Organization / Agency / Defense Prime", width="100%", size="2", bg="rgba(0,0,0,0.5)", border_color="rgba(255,255,255,0.1)", color="white", required=True, auto_complete=False),
                            rx.text_area(name="message", placeholder="Scope of inquiry, operational requirements, or alignment context...", width="100%", size="2", bg="rgba(0,0,0,0.5)", border_color="rgba(255,255,255,0.1)", color="white", min_height="80px", max_height="100px", required=True, auto_complete=False),
                            primary_gold_button("TRANSMIT TO LEAD ARCHITECT", type="submit", size="2", width="100%", margin_top="2", font_weight="bold"),
                            rx.text(
                                "NOTICE: Technical architecture specifications, formal verification suites, and hardware evaluations are provisioned strictly under bilateral NDA following verification of institutional interest and compliance with applicable export controls (ITAR / EAR).",
                                font_size="0.68rem",
                                color="slate.9",
                                line_height="1.45",
                                text_align="center",
                                margin_top="2",
                                font_family="JetBrains Mono, monospace"
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        on_submit=ContactState.handle_submit,
                        width="100%"
                    ),
                    width="100%", max_width="520px", padding="24px 28px",
                    border="1px solid rgba(255,255,255,0.06)", background="rgba(10,10,14,0.7)", border_radius="8px",
                    class_name="animate-fade-up delay-200",
                ),
                align_items="center",
                justify_content="center",
                width="100%",
                padding_x=["4", "6", "8"],
            ),
            width="100%",
            height="100%",
            display="flex",
            align_items="center",
            justify_content="center"
        )
    )