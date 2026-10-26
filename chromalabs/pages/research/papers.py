import reflex as rx
from chromalabs.components.layout import base_layout
from chromalabs.components.buttons import primary_gold_button

def papers() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "ACADEMIC & DEFENSE PUBLICATIONS",
                    font_size="0.75rem", weight="bold", color="#DFBC61", letter_spacing="0.15em",
                    class_name="animate-fade-up", text_align="center", font_family="JetBrains Mono, monospace"
                ),
                rx.text(
                    "Formal Manuscripts & Proof Suites.", 
                    font_size=["1.8rem", "2.2rem", "2.6rem"], weight="bold", letter_spacing="-0.03em", line_height="1.1",
                    color="white", font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100", margin_bottom="2", text_align="center"
                ),
                rx.text(
                    "Theoretical derivations, Lean 4 machine-checked proofs, and physical telemetry manuscripts.",
                    font_size="0.9rem", color="slate.11", max_width="680px", text_align="center", margin_bottom="4", line_height="1.5",
                    class_name="animate-fade-up delay-200"
                ),
                # Institutional Placeholder Card
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon(tag="file-lock-2", color="#DFBC61", size=18),
                            rx.text("CONTROLLED SCIENTIFIC ARCHIVE // INSTITUTIONAL CLEARANCE", font_family="JetBrains Mono, monospace", font_size="0.75rem", font_weight="bold", color="#DFBC61", letter_spacing="0.1em"),
                            rx.spacer(),
                            rx.badge("ITAR / BILATERAL NDA", color_scheme="amber", variant="surface", size="1"),
                            width="100%",
                            align_items="center",
                            margin_bottom="2",
                        ),
                        rx.text(
                            "Scientific Manuscripts Withheld from Public Dissemination",
                            font_size=["1.1rem", "1.25rem"],
                            font_weight="bold",
                            color="white",
                            font_family="'EB Garamond', 'Playfair Display', serif",
                            letter_spacing="-0.01em",
                            margin_bottom="2",
                        ),
                        rx.text(
                            "Chroma Labs withholds academic preprints, mathematical derivations, and machine-checked Lean 4 verification suites from unrestricted public repositories. Core theoretical assets remain governed under strict security protocols and federal defense export compliance (ITAR / EAR). Formal papers, proof suites, and validation telemetry are provisioned strictly upon execution of an institutional bilateral Non-Disclosure Agreement (NDA), verified defense clearance, or as findings become cleared and declassified for public consumption.",
                            font_size="0.84rem",
                            color="slate.11",
                            line_height="1.6",
                            margin_bottom="3",
                        ),
                        rx.hstack(
                            rx.hstack(
                                rx.icon(tag="badge-check", color="#DFBC61", size=14),
                                rx.text("Lean 4 Mathematical Proof Suites", font_family="JetBrains Mono, monospace", font_size="0.72rem", color="slate.12"),
                                spacing="2", align_items="center",
                            ),
                            rx.hstack(
                                rx.icon(tag="badge-check", color="#DFBC61", size=14),
                                rx.text("Thermodynamic Dissipation Models", font_family="JetBrains Mono, monospace", font_size="0.72rem", color="slate.12"),
                                spacing="2", align_items="center",
                            ),
                            rx.hstack(
                                rx.icon(tag="badge-check", color="#DFBC61", size=14),
                                rx.text("Defense Side-Channel Immunity", font_family="JetBrains Mono, monospace", font_size="0.72rem", color="slate.12"),
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
                                    rx.icon(tag="scroll-text", size=15),
                                    rx.text("REQUEST ACADEMIC & DEFENSE MANUSCRIPTS", font_size="0.78rem", font_family="JetBrains Mono, monospace", font_weight="bold"),
                                    rx.icon(tag="arrow-right", size=15),
                                    spacing="2",
                                    align_items="center",
                                ),
                                size="3",
                                width="100%",
                            ),
                            href="/contact?topic=Academic%20Manuscript%20Request",
                            width="100%",
                            _hover={"text_decoration": "none"}
                        ),
                        rx.text(
                            "NOTICE: Academic & defense disclosures are provisioned exclusively to accredited university faculties, defense laboratories, and sovereign computing partners, or published as information becomes available for public consumption.",
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