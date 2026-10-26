import reflex as rx
from chromalabs.components.layout import base_layout
from chromalabs.components.buttons import primary_gold_button

def log() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "RESEARCH & DISCLOSURES",
                    font_size="0.75rem", weight="bold", color="#DFBC61", letter_spacing="0.15em",
                    class_name="animate-fade-up", text_align="center", font_family="JetBrains Mono, monospace"
                ),
                rx.text(
                    "Architectural Intelligence.", 
                    font_size=["1.8rem", "2.2rem", "2.6rem"], weight="bold", letter_spacing="-0.03em", line_height="1.1",
                    color="white", font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100", margin_bottom="2", text_align="center"
                ),
                rx.text(
                    "Archival records, execution telemetry, and formal mathematical verification suites.",
                    font_size="0.9rem", color="slate.11", max_width="680px", text_align="center", margin_bottom="4", line_height="1.5",
                    class_name="animate-fade-up delay-200"
                ),
                # Institutional Placeholder Card
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon(tag="shield-alert", color="#DFBC61", size=18),
                            rx.text("CLASSIFIED ARCHIVE // RESTRICTED ACCESS", font_family="JetBrains Mono, monospace", font_size="0.75rem", font_weight="bold", color="#DFBC61", letter_spacing="0.1em"),
                            rx.spacer(),
                            rx.badge("ITAR / EAR COMPLIANT", color_scheme="amber", variant="surface", size="1"),
                            width="100%",
                            align_items="center",
                            margin_bottom="2",
                        ),
                        rx.text(
                            "Research Disclosures Withheld from Public Indexing",
                            font_size=["1.1rem", "1.25rem"],
                            font_weight="bold",
                            color="white",
                            font_family="'EB Garamond', 'Playfair Display', serif",
                            letter_spacing="-0.01em",
                            margin_bottom="2",
                        ),
                        rx.text(
                            "Chroma Labs withholds technical research disclosures, microarchitectural telemetry, and formal verification suites from unrestricted public distribution. Foundational technical materials are governed by strict security protocols and federal defense export controls (ITAR / EAR). Research disclosures and architectural specifications are published and shared strictly upon execution of an institutional bilateral Non-Disclosure Agreement (NDA), verified government or defense clearance, or as information is formally approved and declassified for public consumption.",
                            font_size="0.84rem",
                            color="slate.11",
                            line_height="1.6",
                            margin_bottom="3",
                        ),
                        rx.hstack(
                            rx.hstack(
                                rx.icon(tag="badge-check", color="#DFBC61", size=14),
                                rx.text("Lean 4 Machine-Checked Invariants", font_family="JetBrains Mono, monospace", font_size="0.72rem", color="slate.12"),
                                spacing="2", align_items="center",
                            ),
                            rx.hstack(
                                rx.icon(tag="badge-check", color="#DFBC61", size=14),
                                rx.text("Thermodynamic Scaling Telemetry", font_family="JetBrains Mono, monospace", font_size="0.72rem", color="slate.12"),
                                spacing="2", align_items="center",
                            ),
                            rx.hstack(
                                rx.icon(tag="badge-check", color="#DFBC61", size=14),
                                rx.text("Sovereign Physical-Layer Isolation", font_family="JetBrains Mono, monospace", font_size="0.72rem", color="slate.12"),
                                spacing="2", align_items="center",
                            ),
                            spacing="4",
                            wrap="wrap",
                            margin_bottom="4",
                            padding="8px 14px",
                            background="rgba(255, 255, 255, 0.02)",
                            border="1px solid rgba(255, 255, 255, 0.05)",
                            border_radius="4px",
                            width="100%",
                        ),
                        rx.link(
                            primary_gold_button(
                                rx.hstack(
                                    rx.icon(tag="lock-keyhole", size=15),
                                    rx.text("REQUEST RESEARCH ACCESS & BILATERAL NDA", font_size="0.78rem", font_family="JetBrains Mono, monospace", font_weight="bold"),
                                    rx.icon(tag="arrow-right", size=15),
                                    spacing="2",
                                    align_items="center",
                                ),
                                size="3",
                                width="100%",
                            ),
                            href="/contact?topic=Research%20and%20Intelligence%20Access",
                            width="100%",
                            _hover={"text_decoration": "none"}
                        ),
                        rx.text(
                            "NOTICE: Disclosures are provisioned exclusively to accredited defense program managers, sovereign computing partners, and qualified institutional research directors, or published as materials become cleared for public consumption.",
                            font_size="0.67rem",
                            color="slate.9",
                            text_align="center",
                            margin_top="2",
                            font_family="JetBrains Mono, monospace",
                            line_height="1.4",
                            width="100%",
                        ),
                        width="100%",
                        align_items="flex-start",
                    ),
                    padding=["20px 22px", "24px 28px"],
                    background="rgba(10, 10, 14, 0.75)",
                    border="1px solid rgba(223, 188, 97, 0.2)",
                    border_radius="8px",
                    width="100%",
                    max_width="720px",
                    box_shadow="0 8px 32px rgba(0, 0, 0, 0.5), inset 0 0 24px rgba(223, 188, 97, 0.03)",
                    class_name="animate-fade-up delay-300"
                ),
                width="100%",
                max_width="900px",
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