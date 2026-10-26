import reflex as rx
from chromalabs.components.layout import base_layout
from chromalabs.components.buttons import primary_gold_button, secondary_white_button

CONTACT_JS = """
(function() {
    const FORMSPREE_ENDPOINT = "https://formspree.io/f/xrpppbay";

    function initContact() {
        const form = document.getElementById("chromaContactForm");
        const topicInput = document.getElementById("contactTopic");
        const emailInput = document.getElementById("contactEmail");
        const companyInput = document.getElementById("contactCompany");
        const messageInput = document.getElementById("contactMessage");
        const submitBtn = document.getElementById("contactSubmitBtn");
        const statusBox = document.getElementById("contactStatusBox");
        const directCopyBtn = document.getElementById("directCopyBtn");
        const statusTitle = document.getElementById("contactStatusTitle");
        const statusMsg = document.getElementById("contactStatusMsg");
        const statusActions = document.getElementById("contactStatusActions");
        const copyRecordBtn = document.getElementById("contactCopyRecordBtn");
        const resetBtn = document.getElementById("contactResetBtn");

        if (directCopyBtn && !directCopyBtn.__bound) {
            directCopyBtn.__bound = true;
            directCopyBtn.addEventListener("click", function(e) {
                e.preventDefault();
                navigator.clipboard.writeText("michael@chromalabs.cc").then(function() {
                    const orig = directCopyBtn.innerText;
                    directCopyBtn.innerText = "✓ Copied";
                    directCopyBtn.style.color = "#DFBC61";
                    setTimeout(function() {
                        directCopyBtn.innerText = orig;
                        directCopyBtn.style.color = "";
                    }, 2000);
                });
            });
        }

        if (!form) return;
        if (form.__bound) return;
        form.__bound = true;

        // Auto-fill topic from URL params if present
        try {
            const urlParams = new URLSearchParams(window.location.search);
            const topicParam = urlParams.get("topic");
            if (topicParam && topicInput && !topicInput.value) {
                topicInput.value = topicParam;
            }
        } catch (e) {}

        let lastRecordText = "";

        form.addEventListener("submit", async function(e) {
            e.preventDefault();
            const topic = (topicInput ? topicInput.value : "").trim();
            const email = (emailInput ? emailInput.value : "").trim();
            const company = (companyInput ? companyInput.value : "").trim();
            const msg = (messageInput ? messageInput.value : "").trim();

            if (!topic || !email || !company || !msg) {
                alert("Please complete all inquiry fields before transmitting.");
                return;
            }

            const origBtnText = submitBtn ? submitBtn.innerText : "TRANSMIT TO LEAD ARCHITECT";
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerText = "TRANSMITTING...";
                submitBtn.style.opacity = "0.7";
            }

            lastRecordText = `INSTITUTIONAL COMMUNIQUE RECORD\\n` +
                             `RECIPIENT: michael@chromalabs.cc\\n` +
                             `SUBJECT: ${topic}\\n` +
                             `AGENCY / ORGANIZATION: ${company}\\n` +
                             `SENDER: ${email}\\n\\n` +
                             `SCOPE OF INQUIRY:\\n${msg}\\n\\n` +
                             `---\\nTransmitted via Chroma Labs Portal (chromalabs.cc)`;

            let sentDirectly = false;

            try {
                const response = await fetch(FORMSPREE_ENDPOINT, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Accept": "application/json"
                    },
                    body: JSON.stringify({
                        _subject: `[Institutional Inquiry] ${topic} (${company})`,
                        topic: topic,
                        email: email,
                        company: company,
                        message: msg,
                    })
                });

                if (response.ok) {
                    sentDirectly = true;
                }
            } catch (err) {
                console.warn("Background transmission error, using client fallback:", err);
            }

            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerText = origBtnText;
                submitBtn.style.opacity = "1";
            }

            if (sentDirectly) {
                // Success - sent directly in background!
                if (statusTitle) statusTitle.innerText = "✓ COMMUNIQUE TRANSMITTED DIRECTLY";
                if (statusMsg) statusMsg.innerText = "Your communique has been delivered directly to Lead Architect Michael Reser (michael@chromalabs.cc). Institutional materials and bilateral NDA workflows are initiated following verification of credentials.";
                if (statusActions) statusActions.style.display = "flex";
                form.style.display = "none";
                if (statusBox) statusBox.style.display = "block";
            } else {
                // Fallback to mailto client dispatch
                const mailtoUrl = "mailto:michael@chromalabs.cc?subject=" + encodeURIComponent(topic) + "&body=" + encodeURIComponent(lastRecordText);
                try {
                    window.location.href = mailtoUrl;
                } catch (e) {}

                if (statusTitle) statusTitle.innerText = "COMMUNIQUE PREPARED";
                if (statusMsg) statusMsg.innerText = "Direct gateway was unreachable; your default email client was dispatched with your pre-filled inquiry. You can also copy the record below.";
                if (statusActions) statusActions.style.display = "flex";
                form.style.display = "none";
                if (statusBox) statusBox.style.display = "block";
            }
        });

        if (copyRecordBtn && !copyRecordBtn.__bound) {
            copyRecordBtn.__bound = true;
            copyRecordBtn.addEventListener("click", function(e) {
                e.preventDefault();
                if (lastRecordText) {
                    navigator.clipboard.writeText(lastRecordText).then(function() {
                        const orig = copyRecordBtn.innerText;
                        copyRecordBtn.innerText = "✓ COPIED TO CLIPBOARD";
                        copyRecordBtn.style.color = "#DFBC61";
                        setTimeout(function() {
                            copyRecordBtn.innerText = orig;
                            copyRecordBtn.style.color = "";
                        }, 2500);
                    });
                }
            });
        }

        if (resetBtn && !resetBtn.__bound) {
            resetBtn.__bound = true;
            resetBtn.addEventListener("click", function(e) {
                e.preventDefault();
                if (form && statusBox) {
                    form.reset();
                    statusBox.style.display = "none";
                    form.style.display = "block";
                }
            });
        }
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initContact);
    } else {
        initContact();
    }
    setTimeout(initContact, 200);
    setTimeout(initContact, 600);
})();
"""

class ContactState(rx.State):
    form_topic: str = ""

    def load_topic(self):
        t = self.router.page.params.get("topic", "")
        if isinstance(t, list) and len(t) > 0:
            self.form_topic = t[0]
        else:
            self.form_topic = str(t)

def contact() -> rx.Component:
    return base_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "INSTITUTIONAL ENGAGEMENT",
                    font_size=["0.65rem", "0.75rem"], weight="bold", color="#DFBC61", letter_spacing="0.15em",
                    class_name="animate-fade-up", text_align="center", font_family="JetBrains Mono, monospace"
                ),
                rx.text(
                    "Contact the Lab.", 
                    font_size=["1.6rem", "2.0rem", "2.6rem"], weight="bold", letter_spacing="-0.03em", line_height="1.1",
                    color="white", font_family="'EB Garamond', 'Playfair Display', serif",
                    class_name="animate-fade-up delay-100", margin_bottom=["2", "3"], text_align="center"
                ),
                
                # Direct route banner
                rx.box(
                    rx.hstack(
                        rx.text("DIRECT DISPATCH:", font_size=["0.7rem", "0.75rem"], font_family="JetBrains Mono, monospace", color="#DFBC61", font_weight="bold"),
                        rx.link(
                            "michael@chromalabs.cc",
                            href="mailto:michael@chromalabs.cc",
                            font_size=["0.72rem", "0.78rem"],
                            font_family="JetBrains Mono, monospace",
                            color="white",
                            text_decoration="underline",
                            _hover={"color": "#DFBC61"}
                        ),
                        rx.button(
                            "Copy",
                            id="directCopyBtn",
                            size="1",
                            variant="ghost",
                            color="slate.9",
                            _hover={"color": "#DFBC61"},
                            font_family="JetBrains Mono, monospace",
                            font_size="0.68rem",
                            cursor="pointer",
                            padding="1px 6px"
                        ),
                        spacing="2",
                        align_items="center",
                        justify_content="center",
                        flex_wrap="wrap",
                    ),
                    margin_bottom=["2", "3"],
                    class_name="animate-fade-up delay-100",
                ),

                rx.box(
                    rx.form(
                        rx.vstack(
                            rx.text("SECURE COMMUNIQUE", font_size="0.85rem", font_weight="bold", color="white", letter_spacing="0.1em", margin_bottom="1", font_family="JetBrains Mono, monospace"),
                            rx.input(id="contactTopic", name="topic", placeholder="Subject / Technical Inquiry", default_value=ContactState.form_topic, width="100%", size="2", bg="rgba(0,0,0,0.5)", border_color="rgba(255,255,255,0.1)", color="white", required=True, auto_complete=False),
                            rx.input(id="contactEmail", name="email", type="email", placeholder="Institutional / Defense / Enterprise Email", width="100%", size="2", bg="rgba(0,0,0,0.5)", border_color="rgba(255,255,255,0.1)", color="white", required=True, auto_complete=False),
                            rx.input(id="contactCompany", name="company", placeholder="Organization / Agency / Defense Prime", width="100%", size="2", bg="rgba(0,0,0,0.5)", border_color="rgba(255,255,255,0.1)", color="white", required=True, auto_complete=False),
                            rx.text_area(id="contactMessage", name="message", placeholder="Scope of inquiry, operational requirements, or alignment context...", width="100%", size="2", bg="rgba(0,0,0,0.5)", border_color="rgba(255,255,255,0.1)", color="white", min_height="80px", max_height="100px", required=True, auto_complete=False),
                            primary_gold_button("TRANSMIT TO LEAD ARCHITECT", type="submit", id="contactSubmitBtn", size="2", width="100%", margin_top="2", font_weight="bold"),
                            rx.text(
                                "NOTICE: Technical architecture specifications, formal verification suites, and hardware evaluations are provisioned strictly under bilateral NDA following verification of institutional interest and compliance with applicable export controls (ITAR / EAR).",
                                font_size=["0.62rem", "0.68rem"],
                                color="slate.9",
                                line_height="1.45",
                                text_align="center",
                                margin_top="2",
                                font_family="JetBrains Mono, monospace"
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        id="chromaContactForm",
                        width="100%"
                    ),
                    
                    # Status confirmation card (revealed on submit)
                    rx.box(
                        rx.vstack(
                            rx.text("✓ COMMUNIQUE TRANSMITTED DIRECTLY", id="contactStatusTitle", font_size="0.85rem", font_weight="bold", color="#DFBC61", letter_spacing="0.1em", font_family="JetBrains Mono, monospace"),
                            rx.text(
                                "Your communique has been delivered directly to Lead Architect Michael Reser (michael@chromalabs.cc). Institutional materials and bilateral NDA workflows are initiated following verification of credentials.",
                                id="contactStatusMsg",
                                font_size=["0.78rem", "0.85rem"],
                                color="white",
                                text_align="center",
                                line_height="1.45"
                            ),
                            rx.hstack(
                                secondary_white_button("COPY COMMUNIQUE RECORD", id="contactCopyRecordBtn", size="2", font_size="0.75rem", padding="10px 16px"),
                                primary_gold_button("TRANSMIT ANOTHER INQUIRY", id="contactResetBtn", size="2", font_size="0.75rem", padding="10px 16px"),
                                id="contactStatusActions",
                                spacing="3",
                                justify_content="center",
                                flex_wrap="wrap",
                                width="100%",
                                margin_top="3"
                            ),
                            spacing="3",
                            align_items="center",
                            width="100%",
                            padding_y="4"
                        ),
                        id="contactStatusBox",
                        style={"display": "none"},
                        width="100%"
                    ),

                    rx.script(CONTACT_JS),
                    width="100%", max_width="520px", padding=["20px 16px", "24px 28px"],
                    border="1px solid rgba(255,255,255,0.06)", background="rgba(10,10,14,0.7)", border_radius="8px",
                    class_name="animate-fade-up delay-200",
                ),
                align_items="center",
                width="100%",
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