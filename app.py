import csv
import datetime
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Quick Air Haines City", layout="centered")

CALL_TRACKING_NUMBER = "+1XXXXXXXXXX"
LEAD_EMAIL = "info@quickairhainescity.com"
ZAPIER_WEBHOOK_URL = "https://hooks.zapier.com/your-webhook-url"
TWILIO_PHONE_NUMBER = "+1XXXXXXXXXX"
BUSINESS_NAME = "Quick Air Haines City"
LEADS_FILE = Path(__file__).resolve().parent / "leads.csv"

STYLE = """
<style>
body {background: #f4fbff; color: #0f172a;}
section.main {padding: 0; max-width: 100%;}
.block-container {padding-top: 0.75rem; padding-bottom: 4rem; padding-left: 1rem; padding-right: 1rem;}
.hero, .section-card, .assistant-card, .footer-card, .spanish-block, .service-area {border-radius: 28px; background: linear-gradient(180deg, #f8fcff 0%, #ffffff 100%); box-shadow: 0 18px 48px rgba(15, 23, 42, 0.08); padding: 1.8rem; margin-bottom: 1rem;}
.hero h1 {font-size: clamp(2.4rem, 6vw, 3.6rem); margin-bottom: 0.35rem; line-height: 1.02;}
.hero p, .hero .subtitle, .hero .note {font-size: 1.05rem; color: #2f4367; margin-bottom: 1rem;}
.cta-button, .secondary-button {display: inline-block; border-radius: 999px; padding: 1rem 1.6rem; font-weight: 700; text-decoration: none; margin-right: 0.8rem; margin-bottom: 0.75rem;}
.cta-button {background: #0d6efd; color: white !important;}
.secondary-button {background: rgba(13, 110, 253, 0.12); color: #0d6efd !important;}
.badge-grid, .service-grid, .why-grid {display: grid; gap: 1rem;}
.badge-grid {grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); margin-top: 1rem;}
.badge {background: white; border: 1px solid rgba(13, 110, 253, 0.14); padding: 1rem; border-radius: 18px; text-align: center; color: #0f172a;}
.badge strong {display: block; margin-bottom: 0.35rem;}
.service-grid {grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));}
.service-card {background: white; border-radius: 22px; border: 1px solid rgba(13, 110, 253, 0.12); padding: 1rem;}
.service-card strong {display: block; margin-bottom: 0.5rem;}
.why-grid {grid-template-columns: 1fr;}
.info-grid {display: grid; gap: 1rem;}
.info-grid .section-card {padding: 1.5rem;}
.assistant-card {border: 1px solid rgba(13, 110, 253, 0.16);}
.assistant-card h2 {margin-top: 0;}
.assistant-step {font-weight: 700; margin-bottom: 0.2rem;}
.assistant-note {font-size: 0.95rem; color: #475569; margin-bottom: 1rem;}
.small-note {font-size: 0.95rem; color: #475569;}
.footer-card {text-align: center; font-size: 0.95rem; color: #475569;}
.footer-links {display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; margin-top: 1rem;}
@media (min-width: 768px) { .why-grid {grid-template-columns: repeat(2, minmax(0, 1fr));} .info-grid {grid-template-columns: repeat(2, minmax(0, 1fr));} }
</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

st.markdown("<div class='hero'>", unsafe_allow_html=True)
st.markdown("<h1>Get Fast AC Help in Haines City</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>A local HVAC specialist will review your request and reach out quickly by text, phone, or email.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='note'><strong>Servicio en Español Disponible</strong> — Fill out the intake form below or choose your preferred contact method.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<a class='cta-button' href='#assistant-form'>Get Fast AC Help</a>"
    f"<a class='secondary-button' href='tel:{CALL_TRACKING_NUMBER}'>Optional Call</a>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='section-card'>", unsafe_allow_html=True)
st.markdown("<h2>Emergency AC Help</h2>", unsafe_allow_html=True)
st.markdown(
    "<p>Urgent cooling problems are dangerous in Florida. Tell us what’s wrong now and we’ll route the request to a qualified local technician.</p>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='badge-grid'>", unsafe_allow_html=True)
for label in [
    "Fast local response",
    "Trusted HVAC technicians",
    "Bilingual support",
    "Transparent service pricing",
]:
    st.markdown(
        f"<div class='badge'><strong>{label}</strong></div>",
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='section-card'>", unsafe_allow_html=True)
st.markdown("<h2>Our HVAC Services</h2>", unsafe_allow_html=True)
st.markdown(
    "<div class='service-grid'>"
    "<div class='service-card'><strong>AC Repair</strong><p>Quick repairs for homeowners facing cooling loss or weak airflow.</p></div>"
    "<div class='service-card'><strong>Emergency Help</strong><p>Priority response for no cooling, leaks, or failed systems.</p></div>"
    "<div class='service-card'><strong>AC Maintenance</strong><p>Tune-ups to prevent breakdowns and extend your system life.</p></div>"
    "<div class='service-card'><strong>Thermostat Support</strong><p>Thermostat troubleshooting, replacement, and programming help.</p></div>"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='why-grid'>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-card'><h3>Why Quick Air Haines City</h3><ul>"
    "<li>Rapid response for emergency HVAC issues</li>"
    "<li>Experienced licensed technicians</li>"
    "<li>Clear communication and easy booking</li>"
    "<li>Designed for Haines City heat and humidity</li>"
    "</ul></div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='section-card'><h3>What Homeowners Trust</h3><ul>"
    "<li>Prompt follow-up via phone, text, or email</li>"
    "<li>Honest assessments and transparent estimates</li>"
    "<li>Friendly service with Spanish support</li>"
    "<li>Comfort-focused repairs and replacement advice</li>"
    "</ul></div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='spanish-block'>", unsafe_allow_html=True)
st.markdown("<h2>Servicio en Español</h2>", unsafe_allow_html=True)
st.markdown(
    "<p>Reparación de aire acondicionado en Haines City. Servicio rápido, confiable y económico. Hablamos español y podemos contactarlo por texto, llamada o correo electrónico.</p>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='service-area'>", unsafe_allow_html=True)
st.markdown("<h3>Service Area</h3>", unsafe_allow_html=True)
st.markdown(
    "<p>Serving Haines City, Lake Wales, Davenport, Winter Haven, Polk City, Babson Park, and nearby Polk County neighborhoods.</p>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div id='assistant-form' class='assistant-card'>", unsafe_allow_html=True)
st.markdown("<h2>Chatbot-style Intake Assistant</h2>", unsafe_allow_html=True)
st.markdown(
    "<p class='assistant-note'>Answer the quick questions below so a local AC specialist can reach out with the fastest help.</p>",
    unsafe_allow_html=True,
)

with st.form(key="assistant_form"):
    st.markdown("<div class='assistant-step'>1. Preferred language</div>", unsafe_allow_html=True)
    preferred_language = st.selectbox("Preferred language", ["English", "Español"], index=0)

    st.markdown("<div class='assistant-step'>2. Your name</div>", unsafe_allow_html=True)
    name = st.text_input("Full name")

    st.markdown("<div class='assistant-step'>3. Phone number</div>", unsafe_allow_html=True)
    phone = st.text_input("Phone number")

    st.markdown("<div class='assistant-step'>4. Email address</div>", unsafe_allow_html=True)
    email = st.text_input("Email address")

    st.markdown("<div class='assistant-step'>5. ZIP code or city</div>", unsafe_allow_html=True)
    city_zip = st.text_input("ZIP code or city")

    st.markdown("<div class='assistant-step'>6. AC issue</div>", unsafe_allow_html=True)
    issue = st.text_area("Describe what’s happening with your AC")

    st.markdown("<div class='assistant-step'>7. Emergency level</div>", unsafe_allow_html=True)
    emergency_level = st.selectbox(
        "Emergency level",
        ["Routine check", "Needs service soon", "Urgent — no cooling"],
        index=2,
    )

    st.markdown("<div class='assistant-step'>8. Preferred contact method</div>", unsafe_allow_html=True)
    contact_method = st.radio(
        "Preferred contact method",
        ["Text message", "Phone call", "Email"],
        index=0,
        horizontal=True,
    )

    submit_request = st.form_submit_button("Get Fast AC Help")

if submit_request:
    if not name.strip() or not phone.strip() or not email.strip() or not city_zip.strip() or not issue.strip():
        st.error("Please complete all fields so we can route your request quickly.")
    else:
        lead_data = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "preferred_language": preferred_language,
            "name": name.strip(),
            "phone": phone.strip(),
            "email": email.strip(),
            "city_zip": city_zip.strip(),
            "issue": issue.strip(),
            "emergency_level": emergency_level,
            "contact_method": contact_method,
            "source": "assistant",
            "call_tracking": CALL_TRACKING_NUMBER,
            "lead_email": LEAD_EMAIL,
            "zapier_webhook": ZAPIER_WEBHOOK_URL,
            "twilio_phone": TWILIO_PHONE_NUMBER,
        }

        file_exists = LEADS_FILE.exists()
        with LEADS_FILE.open("a", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=lead_data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(lead_data)

        log_line = (
            f"NEW LEAD | {lead_data['timestamp']} | {lead_data['name']} | {lead_data['phone']} | "
            f"{lead_data['email']} | {lead_data['city_zip']} | {lead_data['issue']} | "
            f"{lead_data['emergency_level']} | {lead_data['contact_method']}"
        )
        print(log_line)

        if preferred_language == "Español":
            st.success("¡Gracias! Recibimos su solicitud. Un especialista local de aire acondicionado se comunicará pronto.")
        else:
            st.success("Thanks! We received your request. A local AC specialist will contact you shortly.")

        st.markdown(
            f"<p class='small-note'>Lead saved to <strong>{LEADS_FILE.name}</strong>. Ready for email, SMS, Zapier, or Twilio integration.</p>",
            unsafe_allow_html=True,
        )
        st.code(log_line)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='assistant-card'>", unsafe_allow_html=True)
st.markdown("<h2>Standard Contact Form</h2>", unsafe_allow_html=True)
st.markdown(
    "<p class='assistant-note'>Prefer a simple form instead? Submit your contact details and issue description here.</p>",
    unsafe_allow_html=True,
)

with st.form(key="fallback_form"):
    fallback_name = st.text_input("Name", key="fallback_name")
    fallback_phone = st.text_input("Phone", key="fallback_phone")
    fallback_email = st.text_input("Email", key="fallback_email")
    fallback_language = st.selectbox(
        "Preferred language", ["English", "Español"], key="fallback_language"
    )
    fallback_issue = st.text_area("What’s the issue?", key="fallback_issue")
    fallback_submit = st.form_submit_button("Submit Lead")

if fallback_submit:
    if not fallback_name.strip() or not fallback_phone.strip() or not fallback_email.strip() or not fallback_issue.strip():
        st.error("Please provide your name, phone, email, and a brief issue description.")
    else:
        lead_data = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "preferred_language": fallback_language,
            "name": fallback_name.strip(),
            "phone": fallback_phone.strip(),
            "email": fallback_email.strip(),
            "city_zip": "",
            "issue": fallback_issue.strip(),
            "emergency_level": "",
            "contact_method": "Form",
            "source": "fallback_form",
            "call_tracking": CALL_TRACKING_NUMBER,
            "lead_email": LEAD_EMAIL,
            "zapier_webhook": ZAPIER_WEBHOOK_URL,
            "twilio_phone": TWILIO_PHONE_NUMBER,
        }

        file_exists = LEADS_FILE.exists()
        with LEADS_FILE.open("a", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=lead_data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(lead_data)

        print(
            f"NEW LEAD | {lead_data['timestamp']} | {lead_data['name']} | {lead_data['phone']} | {lead_data['email']} | {lead_data['issue']} | Fallback"
        )
        st.success("Thanks! We received your request. A local AC specialist will contact you shortly.")
        st.markdown(
            f"<p class='small-note'>Lead saved to <strong>{LEADS_FILE.name}</strong>. Ready for email, SMS, Zapier, or Twilio integration.</p>",
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='footer-card'>", unsafe_allow_html=True)
st.markdown(
    f"<p><strong>{BUSINESS_NAME}</strong> — Fast AC repair lead capture for Haines City homeowners.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<p class='small-note'>Optional phone support: <a href='tel:{CALL_TRACKING_NUMBER}' style='color:#0d6efd; text-decoration:none;'>{CALL_TRACKING_NUMBER}</a></p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='footer-links'>"
    f"<span>Lead email: {LEAD_EMAIL}</span>"
    f"<span>Zapier webhook placeholder</span>"
    f"<span>Twilio placeholder: {TWILIO_PHONE_NUMBER}</span>"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
