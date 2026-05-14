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
:root { --bg: #eef7ff; --surface: #ffffff; --primary: #0d6efd; --primary-soft: rgba(13, 110, 253, 0.14); --text: #0f172a; --muted: #475569; --accent: #0b5ed7; }
body {background: radial-gradient(circle at top right, rgba(13, 110, 253, 0.08), transparent 22%), linear-gradient(180deg, #f7fbff 0%, #eef6ff 100%); color: var(--text); font-family: Inter, system-ui, sans-serif;}
section.main {padding: 0; max-width: 100%;}
.block-container {padding: 1rem 1rem 7rem; max-width: 1080px; margin: 0 auto;}
.hero {position: relative; overflow: hidden; border-radius: 32px; background: linear-gradient(180deg, #ffffff 0%, #e8f4ff 100%); box-shadow: 0 24px 60px rgba(15, 23, 42, 0.12); padding: 2rem 1.8rem 2rem; margin-bottom: 1.5rem; border: 1px solid rgba(13, 110, 253, 0.12);}
.hero::before {content: ''; position: absolute; inset: 0; background: radial-gradient(circle at top right, rgba(13, 110, 253, 0.18), transparent 18%), radial-gradient(circle at bottom left, rgba(13, 110, 253, 0.08), transparent 20%); pointer-events: none;}
.hero .eyebrow {position: relative; z-index: 1; display: inline-flex; align-items: center; gap: 0.5rem; font-weight: 700; color: #0b5ed7; margin-bottom: 1rem;}
.hero h1 {position: relative; z-index: 1; font-size: clamp(2.8rem, 5vw, 4rem); line-height: 1.02; margin-bottom: 0.75rem;}
.hero .subheadline {position: relative; z-index: 1; color: #334155; font-size: 1.05rem; line-height: 1.6; margin-bottom: 1rem; max-width: 760px;}
.hero .spanish-line {position: relative; z-index: 1; font-weight: 700; color: #0b5ed7; margin-bottom: 1rem;}
.hero .trust-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 0.85rem; margin-bottom: 1.2rem;}
.hero .trust-pill {background: #ffffff; border: 1px solid rgba(13, 110, 253, 0.14); border-radius: 999px; padding: 0.85rem 1rem; color: #0f172a; font-weight: 700; text-align: center; box-shadow: 0 10px 28px rgba(13, 110, 253, 0.08);}
.hero .cta-group {position: relative; z-index: 1; display: flex; flex-wrap: wrap; gap: 0.85rem; margin-bottom: 1rem;}
.cta-button, .secondary-button {display: inline-flex; align-items: center; justify-content: center; border-radius: 999px; padding: 1rem 1.6rem; font-weight: 700; text-decoration: none; transition: transform 0.15s ease, box-shadow 0.15s ease; white-space: nowrap;}
.cta-button {background: var(--primary); color: #fff !important; box-shadow: 0 16px 32px rgba(13, 110, 253, 0.2);}
.cta-button:hover {transform: translateY(-2px);}
.secondary-button {background: rgba(13, 110, 253, 0.12); color: var(--accent) !important;}
.secondary-button:hover {transform: translateY(-2px);}
.response-line {font-size: 0.95rem; color: #334155; margin-bottom: 0.75rem; font-weight: 700;}
.section-card, .assistant-card, .footer-card, .spanish-block, .service-area, .next-steps-card {border-radius: 28px; background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%); box-shadow: 0 18px 48px rgba(15, 23, 42, 0.08); padding: 1.8rem; margin-bottom: 1rem; border: 1px solid rgba(13, 110, 253, 0.08);}
.next-steps-card ol {padding-left: 1.2rem; margin: 0; color: #334155;}
.next-steps-card li {margin-bottom: 0.85rem; line-height: 1.6;}
.next-steps-card .step-note {margin-top: 1rem; color: #475569; font-size: 0.95rem;}
.info-grid {display: grid; gap: 1rem;}
.info-grid .section-card {padding: 1.8rem;}
.assistant-card {border: 1px solid rgba(13, 110, 253, 0.16); padding: 1.8rem;}
.assistant-card h2 {margin-top: 0; margin-bottom: 0.85rem;}
.assistant-step {font-weight: 700; margin-bottom: 0.45rem; color: var(--accent);}
.assistant-note {font-size: 0.98rem; color: #475569; margin-bottom: 1rem;}
.sticky-cta {display: none;}
.footer-card {text-align: center; font-size: 0.95rem; color: #475569;}
.footer-links {display: flex; flex-wrap: wrap; gap: 0.75rem; justify-content: center; margin-top: 1rem;}
.footer-links span {color: #6b7280;}
@media (min-width: 768px) { .info-grid {grid-template-columns: repeat(2, minmax(0, 1fr));} }
@media (max-width: 768px) {
  .block-container {padding-left: 0.75rem; padding-right: 0.75rem; padding-bottom: 8rem;}
  .hero {padding: 1.6rem 1.2rem 1.6rem;}
  .hero h1 {font-size: 2.4rem;}
  .hero .subheadline {font-size: 1rem;}
  .hero .trust-pill {font-size: 0.95rem; padding: 0.75rem 0.9rem;}
  .cta-button, .secondary-button {width: 100%; justify-content: center;}
  .assistant-card {padding: 1.5rem;}
  .assistant-step {font-size: 1rem;}
  .sticky-cta {display: flex; position: fixed; bottom: 0; left: 0; right: 0; justify-content: center; padding: 0.8rem 1rem; background: rgba(255,255,255,0.96); box-shadow: 0 -10px 30px rgba(15, 23, 42, 0.12); z-index: 999;}
  .sticky-cta a {width: 100%;}
}
</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

st.markdown("<div class='hero'>", unsafe_allow_html=True)
st.markdown("<div class='eyebrow'>Emergency AC Repair in Haines City</div>", unsafe_allow_html=True)
st.markdown("<h1>Emergency AC Repair in Haines City</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subheadline'>Fast help for AC problems, cooling issues, and urgent HVAC repairs.</p>",
    unsafe_allow_html=True,
)
st.markdown("<p class='spanish-line'>🇪🇸 Hablamos Español</p>", unsafe_allow_html=True)
st.markdown(
    "<div class='trust-grid'>"
    "<div class='trust-pill'>Same-Day Service</div>"
    "<div class='trust-pill'>Local Haines City Area</div>"
    "<div class='trust-pill'>English & Spanish Support</div>"
    "<div class='trust-pill'>Fast Response Times</div>"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='response-line'>Average response time: under 5 minutes</p>"
    "<p class='response-line'>Tiempo promedio de respuesta: menos de 5 minutos</p>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<div class='cta-group'><a class='cta-button' href='#assistant-form'>🚨 Get Fast AC Help</a>"
    f"<a class='secondary-button' href='tel:{CALL_TRACKING_NUMBER}'>🚨 Obtener Ayuda Rápida</a></div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='next-steps-card'>", unsafe_allow_html=True)
st.markdown("<h2>What Happens Next?</h2>", unsafe_allow_html=True)
st.markdown(
    "<ol>"
    "<li><strong>Submit your AC issue</strong><br>Envíe su problema con el aire acondicionado</li>"
    "<li><strong>We review your request</strong><br>Revisamos su solicitud</li>"
    "<li><strong>A local AC specialist contacts you shortly</strong><br>Un especialista local se comunicará pronto</li>"
    "</ol>",
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
st.markdown("<h2>What We Do</h2>", unsafe_allow_html=True)
st.markdown(
    "<div class='service-grid'>"
    "<div class='service-card'><strong>AC Repair</strong><p>Fast repair for no cooling, weak airflow, or strange HVAC noise.</p></div>"
    "<div class='service-card'><strong>Emergency Service</strong><p>Priority help for urgent cooling failures and leaks.</p></div>"
    "<div class='service-card'><strong>Maintenance</strong><p>Preventive checks and seasonal safety tune-ups.</p></div>"
    "<div class='service-card'><strong>Thermostat Support</strong><p>Replacement, programming, and thermostat troubleshooting.</p></div>"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='why-grid'>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-card'><h3>Why Quick Air Haines City</h3><ul>"
    "<li>Local team focused on Haines City homes</li>"
    "<li>Fast response and same-day attention</li>"
    "<li>Bilingual support in English and Spanish</li>"
    "<li>Clear estimates before service begins</li>"
    "</ul></div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='section-card'><h3>Trusted by Homeowners</h3><ul>"
    "<li>Real local service, no national call center</li>"
    "<li>Licensed technicians and friendly support</li>"
    "<li>Transparent communication every step</li>"
    "<li>Designed for Florida heat and humidity</li>"
    "</ul></div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='spanish-block'>", unsafe_allow_html=True)
st.markdown("<h2>Servicio en Español</h2>", unsafe_allow_html=True)
st.markdown(
    "<p>Reparación de aire acondicionado en Haines City con servicio rápido y confiable. Hablamos español y podemos responder por texto, llamada o correo electrónico.</p>",
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
st.markdown("<h2>Hi 👋 What seems to be going on with your AC?</h2>", unsafe_allow_html=True)
st.markdown(
    "<p class='assistant-note'>This quick request takes under 30 seconds. A local AC specialist will review it fast.</p>",
    unsafe_allow_html=True,
)

with st.form(key="assistant_form"):
    preferred_language = st.selectbox("Preferred language", ["English", "Español"], index=0)
    name = st.text_input("Full name", placeholder="Juan Perez / Jane Smith")
    phone = st.text_input("Phone number", placeholder="(123) 456-7890")
    email = st.text_input("Email address", placeholder="you@example.com")
    city_zip = st.text_input("City or ZIP code", placeholder="Haines City, FL or 33844")
    issue = st.text_area("What’s happening with your AC?", placeholder="No cool air, leak, strange noise, etc.")
    emergency_level = st.selectbox(
        "Emergency level",
        ["Routine check", "Needs service soon", "Urgent — no cooling"],
        index=2,
    )
    contact_method = st.radio(
        "Preferred contact method",
        ["Text message", "Phone call", "Email"],
        index=0,
        horizontal=True,
    )
    submit_request = st.form_submit_button("🚨 Get Fast AC Help")

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

st.markdown(
    "<div class='sticky-cta'>"
    "<a class='cta-button' href='#assistant-form'>🚨 Get Fast AC Help</a>"
    "</div>",
    unsafe_allow_html=True,
)

st.markdown("<div class='footer-card'>", unsafe_allow_html=True)
st.markdown(
    f"<p><strong>{BUSINESS_NAME}</strong> — Trusted AC repair leads for Haines City homeowners.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='footer-links'>"
    f"<span>Lead email: {LEAD_EMAIL}</span>"
    f"<span>Call: <a href='tel:{CALL_TRACKING_NUMBER}' style='color:#0d6efd;text-decoration:none;'>{CALL_TRACKING_NUMBER}</a></span>"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
