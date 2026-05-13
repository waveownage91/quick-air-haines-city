import streamlit as st

st.set_page_config(page_title="Quick Air Haines City", layout="centered")

CALL_TRACKING_NUMBER = "+1XXXXXXXXXX"
LEAD_EMAIL = "info@quickairhainescity.com"
BUSINESS_NAME = "Quick Air Haines City"

st.markdown(
    "<style>"
    "body {background: #f4fbff; color: #0f172a;}"
    "section.main {padding: 0; max-width: 100%;}"
    ".block-container {padding-top: 0.75rem; padding-bottom: 4rem; padding-left: 1rem; padding-right: 1rem;}"
    ".hero, .info-card, .service-card, .footer-card, .spanish-block, .service-area {border-radius: 28px; background: linear-gradient(180deg, #f8fcff 0%, #ffffff 100%); box-shadow: 0 18px 48px rgba(15, 23, 42, 0.08); padding: 1.75rem; margin-bottom: 1rem;}"
    ".hero h1 {font-size: clamp(2.3rem, 6vw, 3.4rem); margin-bottom: 0.2rem; line-height: 1.02;}"
    ".hero p, .hero .subtitle {font-size: 1.05rem; color: #2f4367; margin-bottom: 1rem;}"
    ".cta-button, .secondary-button {display: inline-block; border-radius: 999px; padding: 0.95rem 1.5rem; font-weight: 700; text-decoration: none; margin-right: 0.75rem; margin-bottom: 0.75rem;}"
    ".cta-button {background: #0d6efd; color: white !important;}"
    ".secondary-button {background: rgba(13, 110, 253, 0.12); color: #0d6efd !important;}"
    ".badge-grid, .service-grid, .why-grid {display: grid; gap: 1rem;}"
    ".badge-grid {grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); margin-top: 1rem;}"
    ".badge {background: white; border: 1px solid rgba(13, 110, 253, 0.14); padding: 1rem; border-radius: 18px; text-align: center; color: #0f172a;}"
    ".badge strong {display: block; margin-bottom: 0.35rem;}"
    ".service-grid {grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));}"
    ".service-card {background: white; border-radius: 22px; border: 1px solid rgba(13, 110, 253, 0.12); padding: 1rem;}"
    ".service-card strong {display: block; margin-bottom: 0.5rem;}"
    ".why-grid {grid-template-columns: 1fr;}"
    ".info-card h2, .info-card h3, .spanish-block h2, .service-area h3 {margin-top: 0;}"
    ".spanish-block {border: 1px solid #b7d5ff;}"
    ".service-area {border: 1px solid rgba(13, 110, 253, 0.14);}"
    ".footer-card {text-align: center; font-size: 0.95rem; color: #475569;}"
    ".sticky-call {position: fixed; left: 50%; transform: translateX(-50%); bottom: 1rem; width: min(92%, 420px); z-index: 999;}"
    ".sticky-call a {display: block; padding: 1rem 1.25rem; border-radius: 999px; background: #0d6efd; color: white !important; text-align: center; font-size: 1.05rem; font-weight: 700; box-shadow: 0 18px 40px rgba(13, 110, 253, 0.25);}"
    "@media (min-width: 768px) { .why-grid {grid-template-columns: repeat(2, minmax(0, 1fr));} }"
    "</style>",
    unsafe_allow_html=True,
)

st.markdown("<div class='hero'>", unsafe_allow_html=True)
st.markdown("<h1>❄️ 24/7 AC Repair in Haines City</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>Fast, affordable, reliable AC repair when your home needs it most.</p>", unsafe_allow_html=True
)
st.markdown(
    "<p><strong>Servicio en Español Disponible</strong> 🇪🇸</p>", unsafe_allow_html=True
)
st.markdown(
    f"<a class='cta-button' href='tel:{CALL_TRACKING_NUMBER}'>Call Now</a>"
    f"<a class='secondary-button' href='#request-service'>Request Service</a>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='info-card'>", unsafe_allow_html=True)
st.markdown("<h2>Emergency HVAC Service</h2>", unsafe_allow_html=True)
st.markdown(
    "<p>Same-day AC repair, emergency cooling service, and fast dispatch for Haines City homeowners.</p>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='badge-grid'>", unsafe_allow_html=True)
for label in [
    "Same-Day HVAC Repair",
    "Licensed Technicians",
    "Transparent Pricing",
    "English + Español",
]:
    st.markdown(
        f"<div class='badge'><strong>{label}</strong></div>",
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='service-card'>", unsafe_allow_html=True)
st.markdown("<h2>Our Services</h2>", unsafe_allow_html=True)
st.markdown(
    "<div class='service-grid'>"
    "<div class='service-card'><strong>AC Repair</strong><p>Fast diagnostics and repairs for reliable home comfort.</p></div>"
    "<div class='service-card'><strong>AC Installation</strong><p>Quality equipment installed with care.</p></div>"
    "<div class='service-card'><strong>Maintenance</strong><p>Seasonal tune-ups to keep your system running strong.</p></div>"
    "<div class='service-card'><strong>Emergency HVAC</strong><p>24/7 support for urgent cooling problems.</p></div>"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='why-grid'>", unsafe_allow_html=True)
st.markdown(
    "<div class='info-card'><h3>Why Choose Us</h3><ul>"
    "<li>Fast arrival and honest, upfront pricing</li>"
    "<li>Experienced HVAC technicians who explain every step</li>"
    "<li>Clear communication and no surprise fees</li>"
    "<li>Designed for Florida heat and humidity</li>"
    "</ul></div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='info-card'><h3>Trusted HVAC Support</h3><ul>"
    "<li>Service built to protect your home comfort</li>"
    "<li>Fast repairs, maintenance, and system checks</li>"
    "<li>Bilingual support in English and Spanish</li>"
    "<li>Focused on homeowner satisfaction</li>"
    "</ul></div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='spanish-block'>", unsafe_allow_html=True)
st.markdown("<h2>Reparación de aire acondicionado en Haines City</h2>", unsafe_allow_html=True)
st.markdown(
    "<p>Servicio rápido, confiable y económico. Hablamos español para apoyar a su hogar y familia.</p>",
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

st.markdown("<div id='request-service' class='info-card'>", unsafe_allow_html=True)
st.markdown("<h2>Request Service</h2>", unsafe_allow_html=True)

name = st.text_input("Name", key="name")
phone = st.text_input("Phone", key="phone")
issue = st.text_area("What’s the issue?", key="issue")
preferred_language = st.selectbox(
    "Preferred language",
    ["English", "Español"],
    index=0,
    key="preferred_language",
)

if st.button("Submit Request", key="submit"):
    if not name.strip() or not phone.strip() or not issue.strip():
        st.error("Please fill in your name, phone, and issue so we can help right away.")
    else:
        st.success(
            "Thank you! Your request was submitted. We’ll contact you shortly to confirm your service details."
        )
        st.markdown(
            f"<p style='margin-top:0.75rem; color:#64748b;'>Lead email: {LEAD_EMAIL} • Call tracking: {CALL_TRACKING_NUMBER}</p>",
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='footer-card'>", unsafe_allow_html=True)
st.markdown(
    f"<p><strong>{BUSINESS_NAME}</strong> — Built for Haines City homeowners who need fast AC repair.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<p>Call now for fast service: <a href='tel:{CALL_TRACKING_NUMBER}' style='color:#0d6efd; text-decoration:none;'>{CALL_TRACKING_NUMBER}</a></p>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    f"<div class='sticky-call'><a href='tel:{CALL_TRACKING_NUMBER}'>Call Now</a></div>",
    unsafe_allow_html=True,
)
