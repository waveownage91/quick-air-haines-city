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
:root { --bg: #eef7ff; --surface: #ffffff; --primary: #0d6efd; --primary-soft: rgba(13, 110, 253, 0.14); --text: #0f172a; --muted: #4b5b79; --accent: #0b5ed7; }
body {background: radial-gradient(circle at top right, rgba(13, 110, 253, 0.09), transparent 24%), linear-gradient(180deg, #f7fbff 0%, #eef6ff 100%); color: var(--text);}
section.main {padding: 0; max-width: 100%;}
.block-container {padding: 1rem 1.2rem 4rem; max-width: 1200px; margin: 0 auto;}
.hero {position: relative; overflow: hidden; border-radius: 32px; background: linear-gradient(180deg, #ffffff 0%, #e9f3ff 100%); box-shadow: 0 25px 60px rgba(15, 23, 42, 0.12); padding: 2.5rem; margin-bottom: 1.5rem; border: 1px solid rgba(13, 110, 253, 0.12);}
.hero::before {content: ''; position: absolute; inset: 0; background: radial-gradient(circle at top right, rgba(13, 110, 253, 0.18), transparent 24%), radial-gradient(circle at bottom left, rgba(13, 110, 253, 0.08), transparent 20%); pointer-events: none;}
.hero h1 {position: relative; font-size: clamp(2.8rem, 5vw, 4.2rem); line-height: 1.02; margin-bottom: 0.75rem; z-index: 1;}
.hero p, .hero .subtitle, .hero .note {position: relative; z-index: 1; font-size: 1.05rem; color: var(--muted); margin-bottom: 1.1rem;}
.hero .meta-row {position: relative; z-index: 1; display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center; margin-bottom: 1.5rem;}
.hero .badge-pill {background: rgba(13, 110, 253, 0.1); color: var(--accent); border-radius: 999px; padding: 0.75rem 1rem; font-weight: 700; font-size: 0.95rem;}
.hero .cta-group {position: relative; z-index: 1; display: flex; flex-wrap: wrap; gap: 0.9rem; align-items: center;}
.cta-button, .secondary-button {display: inline-flex; align-items: center; justify-content: center; border-radius: 999px; padding: 1rem 1.8rem; font-weight: 700; text-decoration: none; transition: transform 0.2s ease, box-shadow 0.2s ease; white-space: nowrap;}
.cta-button {background: var(--primary); color: #fff !important; box-shadow: 0 18px 30px rgba(13, 110, 253, 0.22);}
.cta-button:hover {transform: translateY(-2px); box-shadow: 0 22px 40px rgba(13, 110, 253, 0.3);}
.secondary-button {background: rgba(13, 110, 253, 0.12); color: var(--accent) !important;}
.secondary-button:hover {transform: translateY(-2px);}
.section-card, .assistant-card, .footer-card, .spanish-block, .service-area, .impact-card, .testimonials-card {border-radius: 28px; background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%); box-shadow: 0 18px 48px rgba(15, 23, 42, 0.08); padding: 1.9rem; margin-bottom: 1rem; border: 1px solid rgba(13, 110, 253, 0.08);}
.impact-card {display: flex; flex-wrap: wrap; gap: 1rem; align-items: stretch; justify-content: space-between;}
.impact-item {flex: 1 1 240px; background: #fff; border-radius: 22px; padding: 1.2rem; border: 1px solid rgba(13, 110, 253, 0.08);}
.impact-item strong {display: block; font-size: 1.05rem; margin-bottom: 0.65rem; color: var(--text);}
.impact-item p {margin: 0; color: var(--muted);}
.badge-grid, .service-grid, .why-grid, .testimonial-grid {display: grid; gap: 1rem;}
.badge-grid {grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); margin-top: 1rem;}
.badge {background: linear-gradient(180deg, #fbfdff 0%, #f4f9ff 100%); border: 1px solid rgba(13, 110, 253, 0.16); padding: 1rem 1.1rem; border-radius: 20px; text-align: center; color: var(--text); min-height: 110px; display: flex; align-items: center; justify-content: center; font-weight: 700;}
.badge strong {font-size: 1rem;}
.service-grid {grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));}
.service-card {background: #ffffff; border-radius: 24px; border: 1px solid rgba(13, 110, 253, 0.12); padding: 1.3rem; min-height: 180px; display: flex; flex-direction: column; justify-content: space-between;}
.service-card strong {display: block; font-size: 1.1rem; margin-bottom: 0.75rem;}
.service-card p {margin: 0; color: var(--muted);}
.why-grid {grid-template-columns: 1fr;}
.info-grid {display: grid; gap: 1rem;}
.info-grid .section-card {padding: 1.6rem;}
.assistant-card {border: 1px solid rgba(13, 110, 253, 0.16);}
.assistant-card h2, .section-card h2, .spanish-block h2, .service-area h3, .testimonials-card h3 {margin-top: 0;}
.assistant-step {font-weight: 700; margin-bottom: 0.35rem; color: var(--accent);}
.assistant-note, .small-note {font-size: 0.95rem; color: var(--muted); margin-bottom: 1rem;}
.testimonial-grid {grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));}
.testimonial-card {background: #0d6efd; color: #fff; padding: 1.4rem; border-radius: 24px; min-height: 170px; display: flex; flex-direction: column; justify-content: space-between;}
.testimonial-card p {margin: 0 0 1rem; line-height: 1.6;}
.testimonial-card .name {font-weight: 700; font-size: 0.98rem;}
.footer-card {text-align: center; font-size: 0.95rem; color: #475569;}
.footer-links {display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; margin-top: 1rem;}
.footer-links span {color: #6b7280;}
@media (min-width: 768px) { .why-grid {grid-template-columns: repeat(2, minmax(0, 1fr));} .info-grid {grid-template-columns: repeat(2, minmax(0, 1fr));} .hero .meta-row {justify-content: space-between;} .assistant-card {margin-top: 1rem;} }
</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

st.markdown("<div class='hero'>", unsafe_allow_html=True)
st.markdown("<div class='meta-row'><span class='badge-pill'>Same-day AC response in Haines City</span><span class='badge-pill'>Friendly bilingual support</span></div>", unsafe_allow_html=True)
st.markdown("<h1>Get Fast AC Help in Haines City</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>A local HVAC specialist reviews your request and connects with you quickly by text, phone, or email.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='note'><strong>Servicio en Español Disponible</strong> — Tell us your issue and we’ll match you with local cooling help.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<div class='cta-group'><a class='cta-button' href='#assistant-form'>Get Fast AC Help</a>"
    f"<a class='secondary-button' href='tel:{CALL_TRACKING_NUMBER}'>Call Now</a></div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
st.markdown(
    "<div class='impact-item'><strong>Reliable local service</strong><p>We focus on Haines City homes and Polk County heat, delivering trusted HVAC care when you need it most.</p></div>"
    "<div class='impact-item'><strong>Clear pricing & communication</strong><p>Know what to expect before technicians arrive, with fast follow-up by phone, text, or email.</p></div>"
    "<div class='impact-item'><strong>Prepared for emergencies</strong><p>Same-day attention for no cooling, leaks, and urgent AC breakdowns.</p></div>",
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

st.markdown("<div class='testimonials-card'>", unsafe_allow_html=True)
st.markdown("<h3>Community feedback</h3>", unsafe_allow_html=True)
st.markdown(
    "<div class='testimonial-grid'>"
    "<div class='testimonial-card'><p>“Quick Air helped us the same day and kept our home comfortable during the heat wave. Professional and easy to work with.”</p><div class='name'>— Local homeowner</div></div>"
    "<div class='testimonial-card'><p>“Fast follow-up, clear pricing, and bilingual support made the process stress-free. Highly recommended for Haines City AC issues.”</p><div class='name'>— Florida resident</div></div>"
    "<div class='testimonial-card'><p>“They arrived prepared, explained the repair, and solved the problem quickly. Felt like the team genuinely cared about our home.”</p><div class='name'>— Repeat customer</div></div>"
    "</div>",
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
