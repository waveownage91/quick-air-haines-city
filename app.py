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
section.main {padding: 1.5rem 0 0; max-width: 100%;}
.block-container {padding: 1.5rem 1rem 7rem; max-width: 1080px; margin: 0 auto;}
.hero {position: relative; overflow: hidden; border-radius: 32px; background: linear-gradient(180deg, #ffffff 0%, #e8f4ff 100%); box-shadow: 0 24px 60px rgba(15, 23, 42, 0.12); padding: 2rem 1.8rem 1.8rem; margin-bottom: 1.5rem; border: 1px solid rgba(13, 110, 253, 0.12);}
.hero::before {content: ''; position: absolute; inset: 0; background: radial-gradient(circle at top right, rgba(13, 110, 253, 0.18), transparent 18%), radial-gradient(circle at bottom left, rgba(13, 110, 253, 0.08), transparent 20%); pointer-events: none;}
.hero-layout {display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(300px, 1fr); gap: 1.5rem; align-items: center;}
.hero-copy {position: relative; z-index: 1;}
.hero-image-grid {display: grid; gap: 1rem;}
.hero-image {position: relative; min-height: 220px; border-radius: 28px; background-color: #eaf3ff; background-size: cover; background-position: center; box-shadow: 0 18px 48px rgba(15, 23, 42, 0.12); overflow: hidden;}
.hero-image::after {content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(15, 23, 42, 0.04), rgba(15, 23, 42, 0.18));}
.hero-image.tall {min-height: 360px;}
.hero-image.small {min-height: 180px;}
.hero-visual-label {position: absolute; left: 1rem; bottom: 1rem; z-index: 2; background: rgba(255, 255, 255, 0.92); color: #0f172a; padding: 0.7rem 1rem; border-radius: 999px; font-size: 0.95rem; font-weight: 700; box-shadow: 0 12px 24px rgba(15, 23, 42, 0.12);}
.hero .eyebrow {position: relative; z-index: 1; display: inline-flex; align-items: center; gap: 0.5rem; font-weight: 700; color: #0b5ed7; margin-bottom: 1rem;}
.hero h1 {position: relative; z-index: 1; font-size: clamp(2.8rem, 5vw, 4rem); line-height: 1.02; margin-bottom: 0.75rem;}
.hero .subheadline {position: relative; z-index: 1; color: #334155; font-size: 1.05rem; line-height: 1.6; margin-bottom: 1rem; max-width: 760px;}
.hero .spanish-line {position: relative; z-index: 1; font-weight: 700; color: #0b5ed7; margin-bottom: 1rem;}
.hero .trust-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 0.85rem; margin-bottom: 1.2rem;}
.hero .trust-pill {background: #ffffff; border: 1px solid rgba(13, 110, 253, 0.14); border-radius: 999px; padding: 0.85rem 1rem; color: #0f172a; font-weight: 700; text-align: center; box-shadow: 0 10px 28px rgba(13, 110, 253, 0.08);}
.hero .cta-group {position: relative; z-index: 1; display: flex; flex-wrap: wrap; gap: 0.85rem; margin-bottom: 1.2rem;}
.cta-button, .secondary-button {display: inline-flex; align-items: center; justify-content: center; border-radius: 999px; padding: 1rem 1.6rem; font-weight: 700; text-decoration: none; transition: transform 0.15s ease, box-shadow 0.15s ease; white-space: nowrap;}
.cta-button {background: var(--primary); color: #fff !important; box-shadow: 0 16px 32px rgba(13, 110, 253, 0.2);}
.cta-button:hover {transform: translateY(-2px);}
.secondary-button {background: rgba(13, 110, 253, 0.12); color: var(--accent) !important;}
.secondary-button:hover {transform: translateY(-2px);}
.response-line {font-size: 0.95rem; color: #334155; margin-bottom: 0.75rem; font-weight: 700;}
.story-section {position: relative; overflow: hidden; border-radius: 32px; background: linear-gradient(180deg, #ffffff 0%, #eef7ff 100%); box-shadow: 0 24px 60px rgba(15, 23, 42, 0.08); padding: 2rem; margin-bottom: 1.5rem; border: 1px solid rgba(13, 110, 253, 0.12);}
.story-panel {display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(320px, 1fr); gap: 1.5rem; align-items: center;}
.story-copy {position: relative; z-index: 1;}
.story-heading {font-size: clamp(2.4rem, 4.5vw, 3.4rem); line-height: 1.05; margin-bottom: 0.85rem;}
.story-text {color: #334155; line-height: 1.75; margin-bottom: 1.2rem; max-width: 720px;}
.story-note {font-size: 0.98rem; color: #475569; margin-top: 0.5rem;}
.story-image {position: relative; min-height: 260px; border-radius: 28px; background-color: #eaf3ff; background-size: cover; background-position: center; box-shadow: 0 18px 48px rgba(15, 23, 42, 0.12); overflow: hidden;}
.story-overlay {position: absolute; inset: 0; background: linear-gradient(180deg, rgba(14, 69, 150, 0.08), rgba(255, 255, 255, 0.26));}
.section-divider {height: 2px; margin: 1.5rem 0; background: linear-gradient(90deg, transparent, rgba(13, 110, 253, 0.18), transparent);}
.final-cta {text-align: center; padding: 2rem 1.25rem; border-radius: 28px; background: linear-gradient(180deg, #fff 0%, #e9f4ff 100%); border: 1px solid rgba(13, 110, 253, 0.14); box-shadow: 0 18px 48px rgba(15, 23, 42, 0.08); margin-bottom: 1.5rem;}
.final-cta h2 {margin-bottom: 1rem; font-size: clamp(2.2rem, 4vw, 3rem);}
@media (max-width: 768px) {
  .story-panel {grid-template-columns: 1fr;}
  .story-image {min-height: 220px;}
  .story-heading {font-size: 2rem;}
}
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
.badge-grid {display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); margin-bottom: 1rem;}
.badge {display: flex; align-items: center; gap: 0.85rem; padding: 1rem 1rem 1rem 0.95rem; border-radius: 24px; background: rgba(13, 110, 253, 0.06); border: 1px solid rgba(13, 110, 253, 0.12);}
.badge::before {content: '✓'; display: inline-flex; width: 32px; height: 32px; align-items: center; justify-content: center; background: #0d6efd; color: #fff; border-radius: 50%; font-size: 0.9rem; font-weight: 700;}
.small-note {font-size: 0.9rem; color: #64748b; margin-top: 1rem;}
.intro-splash {position: fixed; inset: 0; z-index: 9999; display: flex; align-items: center; justify-content: center; background: radial-gradient(circle at top left, rgba(221, 237, 255, 0.96), rgba(255, 255, 255, 0.98)); color: #0f172a; flex-direction: column; text-align: center; padding: 2rem; animation: introFade 1.5s ease forwards; overflow: hidden;}
.intro-splash::before {content: ''; position: absolute; inset: 0; background: radial-gradient(circle at top right, rgba(255,255,255,0.62), transparent 45%);}
.intro-sun {position: absolute; top: 16%; right: 16%; width: 110px; height: 110px; border-radius: 50%; background: radial-gradient(circle, #fff9c8 0%, #fde68a 48%, #f59e0b 100%); box-shadow: 0 0 50px rgba(245, 158, 11, 0.35); animation: sunGlow 4s ease-in-out infinite;}
.intro-wind {position: absolute; top: 52%; left: -20%; width: 140%; height: 88px; background: linear-gradient(135deg, rgba(255,255,255,0.35), rgba(255,255,255,0.08) 40%, rgba(255,255,255,0.35)); border-radius: 999px; opacity: 0.8; filter: blur(0.5px); animation: windSlide 3s linear infinite;}
.intro-wind:nth-child(3) {top: 64%; opacity: 0.55; animation-duration: 3.8s;}
.intro-splash h1 {margin: 0; font-size: clamp(2.5rem, 6vw, 4rem); letter-spacing: 0.03em;}
.intro-splash p {margin-top: 1rem; font-size: 1.05rem; opacity: 0.92;}
@keyframes introFade {0% {opacity: 1; transform: translateY(0);} 80% {opacity: 1; transform: translateY(0);} 100% {opacity: 0; transform: translateY(-32px); visibility: hidden;}}
@keyframes sunGlow {0%, 100% {transform: scale(1);} 50% {transform: scale(1.05);} }
@keyframes windSlide {0% {transform: translateX(-10%);} 100% {transform: translateX(100%);} }
@keyframes drift {0% {transform: translateX(0);} 50% {transform: translateX(8px);} 100% {transform: translateX(0);}}
.hero .eyebrow {animation: drift 6s ease-in-out infinite;}
@media (min-width: 768px) { .info-grid {grid-template-columns: repeat(2, minmax(0, 1fr));} }
@media (max-width: 768px) {
  .block-container {padding-left: 0.75rem; padding-right: 0.75rem; padding-bottom: 8rem;}
  .hero {padding: 1.4rem 1rem 1rem;}
  .hero-layout {grid-template-columns: 1fr;}
  .hero-image-grid {grid-template-columns: 1fr;}
  .hero-image.tall {min-height: 240px;}
  .hero-image.small {min-height: 140px;}
  .hero h1 {font-size: 2.4rem;}
  .hero .subheadline {font-size: 1rem;}
  .hero .trust-pill {font-size: 0.95rem; padding: 0.75rem 0.9rem;}
  .cta-button, .secondary-button {width: 100%; justify-content: center;}
  .assistant-card {padding: 1.5rem;}
  .assistant-step {font-size: 1rem;}
  .badge-grid {grid-template-columns: 1fr;}
  .service-grid {grid-template-columns: 1fr;}
  .sticky-cta {display: flex; position: fixed; bottom: 0; left: 0; right: 0; justify-content: center; padding: 0.8rem 1rem; background: rgba(255,255,255,0.96); box-shadow: 0 -10px 30px rgba(15, 23, 42, 0.12); z-index: 999;}
  .sticky-cta a {width: 100%;}
}
</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

st.markdown(
    "<div class='intro-splash'>"
    "<div class='intro-sun'></div>"
    "<div class='intro-wind'></div>"
    "<div class='intro-wind'></div>"
    "<h1>Quick Air Haines City</h1>"
    "<p>Fresh breeze, cool comfort, fast local service.</p>"
    "</div>",
    unsafe_allow_html=True,
)

page_language = st.radio(
    "Language / Idioma",
    ["English", "Español"],
    index=0,
    key="page_language",
    horizontal=True,
)

if page_language not in ["English", "Español"]:
    page_language = "English"

tr = lambda en, es: es if page_language == "Español" else en

st.markdown(
    "<div class='story-section'>"
    "<div class='story-panel'>"
    f"<div class='story-copy'>"
    f"<div class='eyebrow'>{tr('AC Not Cooling in Haines City?','¿El AC no enfría en Haines City?')}</div>"
    f"<h1 class='story-heading'>{tr('AC Not Cooling in Haines City?','¿El AC no enfría en Haines City?')}</h1>"
    f"<p class='story-text'>{tr('Hot home in the Florida heat? We offer fast repair, same-day service, and a local team that answers in English and Spanish.','¿Casa caliente con el calor de Florida? Ofrecemos reparación rápida, servicio el mismo día y un equipo local que responde en inglés y español.')}</p>"
    f"<p class='spanish-line'>{tr('🇪🇸 Hablamos Español','🇪🇸 Hablamos Español')}</p>"
    "<div class='cta-group'>"
    f"<a class='cta-button' href='#assistant-form'>{tr('🚨 Get Fast AC Help','🚨 Obtener ayuda rápida')}</a>"
    f"<a class='secondary-button' href='tel:{CALL_TRACKING_NUMBER}'>{tr('🚨 Call Now','🚨 Llamar ahora')}</a>"
    "</div>"
    f"<p class='response-line'>{tr('Average response time: under 5 minutes','Tiempo promedio de respuesta: menos de 5 minutos')}</p>"
    "</div>"
    f"<div class='story-image' style=\"background-image: url('assets/broken-ac-home.jpg');\">"
    f"<div class='story-overlay'></div>"
    "</div>"
    "</div>"
    "</div>"
    "<div class='section-divider'></div>"
    "<div class='story-section'>"
    "<div class='story-panel'>"
    f"<div class='story-image' style=\"background-image: url('assets/ac-technician-diagnose.jpg');\">"
    f"<div class='story-overlay'></div>"
    "</div>"
    f"<div class='story-copy'>"
    f"<h2 class='story-heading'>{tr('We quickly diagnose the problem','Diagnosticar rápidamente el problema')}</h2>"
    f"<p class='story-text'>{tr('Our local technician arrives fast, inspects your system, and explains the repair plan in clear terms.','Nuestro técnico local llega rápido, inspecciona su sistema y explica el plan de reparación con claridad.')}</p>"
    f"<p class='story-note'>{tr('No jargon. No surprise fees. Just practical, honest repair guidance.','Sin jerga. Sin tarifas sorpresa. Solo orientación práctica y honesta de reparación.')}</p>"
    "</div>"
    "</div>"
    "</div>"
    "<div class='section-divider'></div>"
    "<div class='story-section'>"
    "<div class='story-panel'>"
    f"<div class='story-copy'>"
    f"<h2 class='story-heading'>{tr('Fast and reliable repair service','Servicio de reparación rápido y confiable')}</h2>"
    f"<p class='story-text'>{tr('We fix the cooling issue with a trusted local crew, using quality parts and a safety-first approach.','Reparamos el problema de enfriamiento con un equipo local de confianza, utilizando piezas de calidad y un enfoque de seguridad primero.')}</p>"
    f"<p class='story-note'>{tr('Same-day repair when possible, and clear communication every step of the way.','Reparación el mismo día cuando sea posible y comunicación clara en cada paso.')}</p>"
    "</div>"
    f"<div class='story-image' style=\"background-image: url('assets/ac-technician-repair.jpg');\">"
    f"<div class='story-overlay'></div>"
    "</div>"
    "</div>"
    "</div>"
    "<div class='section-divider'></div>"
    "<div class='story-section'>"
    "<div class='story-panel'>"
    f"<div class='story-image' style=\"background-image: url('assets/cool-family-home.jpg');\">"
    f"<div class='story-overlay'></div>"
    "</div>"
    f"<div class='story-copy'>"
    f"<h2 class='story-heading'>{tr('Comfort restored. Cool air back.','Confort restaurado. Aire frío de regreso.')}</h2>"
    f"<p class='story-text'>{tr('Enjoy a comfortable home again after a trusted local repair — with quick scheduling and follow-up support.','Disfrute de un hogar cómodo nuevamente después de una reparación local confiable, con programación rápida y soporte de seguimiento.')}</p>"
    f"<p class='story-note'>{tr('Ready for Florida heat with reliable cooling you can count on.','Listo para el calor de Florida con enfriamiento confiable en el que puede confiar.')}</p>"
    "</div>"
    "</div>"
    "</div>"
    "<div class='section-divider'></div>"
    "<div class='final-cta'>"
    f"<h2>{tr('Ready to fix your AC now?','¿Listo para reparar su AC ahora?')}</h2>"
    f"<p class='story-text'>{tr('Submit your request and our local Haines City team will respond quickly to schedule your service.','Envíe su solicitud y nuestro equipo local de Haines City responderá rápidamente para programar su servicio.')}</p>"
    f"<a class='cta-button' href='#assistant-form'>{tr('🚨 Get Fast AC Help','🚨 Obtener ayuda rápida')}</a>"
    "</div>"
    "<div class='service-area'>"
    f"<h3>{tr('Service Area','Área de servicio')}</h3>"
    f"<p>{tr('Serving Haines City, Lake Wales, Davenport, Winter Haven, Polk City, Babson Park, and nearby Polk County neighborhoods.','Atendemos Haines City, Lake Wales, Davenport, Winter Haven, Polk City, Babson Park y vecindarios cercanos del condado de Polk.')}</p>"
    "</div>",
    unsafe_allow_html=True,
)

st.markdown("<div id='assistant-form' class='assistant-card'>", unsafe_allow_html=True)
st.markdown(f"<h2>{tr('What Happens Next?','¿Qué sucede después?')}</h2>", unsafe_allow_html=True)
st.markdown(
    "<ol>"
    f"<li>{tr('Submit your AC issue','Envíe su problema con el aire acondicionado')}</li>"
    f"<li>{tr('We review your request','Revisamos su solicitud')}</li>"
    f"<li>{tr('A local AC specialist contacts you shortly','Un especialista local se comunicará pronto')}</li>"
    "</ol>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='section-card'>", unsafe_allow_html=True)
st.markdown(f"<h2>{tr('Emergency AC Help','Ayuda de AC de emergencia')}</h2>", unsafe_allow_html=True)
st.markdown(
    f"<p>{tr('Urgent cooling problems are dangerous in Florida. Tell us what’s wrong now and we’ll route your request to a qualified local technician.','Los problemas de refrigeración urgentes son peligrosos en Florida. Díganos qué está mal ahora y dirigiremos su solicitud a un técnico local calificado.')}</p>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='badge-grid'>", unsafe_allow_html=True)
for label in [
    tr("Fast local response","Respuesta local rápida"),
    tr("Trusted HVAC technicians","Técnicos HVAC de confianza"),
    tr("Bilingual support","Soporte bilingüe"),
    tr("Transparent service pricing","Precios transparentes"),
]:
    st.markdown(
        f"<div class='badge'><strong>{label}</strong></div>",
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='section-card'>", unsafe_allow_html=True)
st.markdown(f"<h2>{tr('What We Do','Lo que hacemos')}</h2>", unsafe_allow_html=True)
st.markdown(
    "<div class='service-grid'>"
    f"<div class='service-card'><strong>{tr('AC Repair','Reparación de AC')}</strong><p>{tr('Fast repair for no cooling, weak airflow, or strange HVAC noise.','Reparación rápida para falta de enfriamiento, flujo de aire débil o ruidos extraños del HVAC.')}</p></div>"
    f"<div class='service-card'><strong>{tr('Emergency Service','Servicio de emergencia')}</strong><p>{tr('Priority help for urgent cooling failures and leaks.','Ayuda prioritaria para fallas de enfriamiento urgentes y fugas.')}</p></div>"
    f"<div class='service-card'><strong>{tr('Maintenance','Mantenimiento')}</strong><p>{tr('Preventive checks and seasonal safety tune-ups.','Revisiones preventivas y ajustes de seguridad de temporada.')}</p></div>"
    f"<div class='service-card'><strong>{tr('Thermostat Support','Soporte de termostatos')}</strong><p>{tr('Replacement, programming, and thermostat troubleshooting.','Reemplazo, programación y solución de problemas de termostatos.')}</p></div>"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='why-grid'>", unsafe_allow_html=True)
st.markdown(
    f"<div class='section-card'><h3>{tr('Why Quick Air Haines City','Por qué Quick Air Haines City')}</h3><ul>"
    f"<li>{tr('Local team focused on Haines City homes','Equipo local enfocado en hogares de Haines City')}</li>"
    f"<li>{tr('Fast response and same-day attention','Respuesta rápida y atención el mismo día')}</li>"
    f"<li>{tr('Bilingual support in English and Spanish','Soporte bilingüe en inglés y español')}</li>"
    f"<li>{tr('Clear estimates before service begins','Presupuestos claros antes de comenzar el servicio')}</li>"
    "</ul></div>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<div class='section-card'><h3>{tr('Trusted by Homeowners','Confiado por los propietarios')}</h3><ul>"
    f"<li>{tr('Real local service, no national call center','Servicio local real, no centro de llamadas nacional')}</li>"
    f"<li>{tr('Licensed technicians and friendly support','Técnicos con licencia y soporte amable')}</li>"
    f"<li>{tr('Transparent communication every step','Comunicación transparente en cada paso')}</li>"
    f"<li>{tr('Designed for Florida heat and humidity','Diseñado para el calor y la humedad de Florida')}</li>"
    "</ul></div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='spanish-block'>", unsafe_allow_html=True)
st.markdown(f"<h2>{tr('Servicio en Español','Servicio en Español')}</h2>", unsafe_allow_html=True)
st.markdown(
    f"<p>{tr('Haines City AC repair with fast, reliable service. We speak Spanish and can respond by text, call, or email.','Reparación de aire acondicionado en Haines City con servicio rápido y confiable. Hablamos español y podemos responder por texto, llamada o correo electrónico.')}</p>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='service-area'>", unsafe_allow_html=True)
st.markdown(f"<h3>{tr('Service Area','Área de servicio')}</h3>", unsafe_allow_html=True)
st.markdown(
    f"<p>{tr('Serving Haines City, Lake Wales, Davenport, Winter Haven, Polk City, Babson Park, and nearby Polk County neighborhoods.','Atendemos Haines City, Lake Wales, Davenport, Winter Haven, Polk City, Babson Park y vecindarios cercanos del condado de Polk.')}</p>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div id='assistant-form' class='assistant-card'>", unsafe_allow_html=True)
st.markdown(f"<h2>{tr('Hi 👋 What seems to be going on with your AC?','Hola 👋 ¿Qué está pasando con su aire acondicionado?')}</h2>", unsafe_allow_html=True)
st.markdown(
    f"<p class='assistant-note'>{tr('This quick request takes under 30 seconds. A local AC specialist will review it fast.','Esta solicitud rápida toma menos de 30 segundos. Un especialista local de AC lo revisará pronto.')}</p>",
    unsafe_allow_html=True,
)

with st.form(key="assistant_form"):
    preferred_language = st.selectbox(
        tr("Preferred language","Idioma preferido"),
        ["English", "Español"],
        index=0 if page_language == "English" else 1,
    )
    name = st.text_input(tr("Full name","Nombre completo"), placeholder=tr("Juan Perez / Jane Smith","Juan Pérez / Jane Smith"))
    phone = st.text_input(tr("Phone number","Teléfono"), placeholder=tr("(123) 456-7890","(123) 456-7890"))
    email = st.text_input(tr("Email address","Correo electrónico"), placeholder=tr("you@example.com","usted@ejemplo.com"))
    city_zip = st.text_input(tr("City or ZIP code","Ciudad o código postal"), placeholder=tr("Haines City, FL or 33844","Haines City, FL o 33844"))
    issue = st.text_area(tr("What’s happening with your AC?","¿Qué está pasando con su aire acondicionado?"), placeholder=tr("No cool air, leak, strange noise, etc.","Sin aire frío, fuga, ruido extraño, etc."))
    emergency_level = st.selectbox(
        tr("Emergency level","Nivel de emergencia"),
        [tr("Routine check","Revisión rutinaria"), tr("Needs service soon","Necesita servicio pronto"), tr("Urgent — no cooling","Urgente — sin enfriamiento")],
        index=2,
    )
    contact_method = st.radio(
        tr("Preferred contact method","Método de contacto preferido"),
        [tr("Text message","Mensaje de texto"), tr("Phone call","Llamada telefónica"), tr("Email","Correo electrónico")],
        index=0,
        horizontal=True,
    )
    submit_request = st.form_submit_button(tr("🚨 Get Fast AC Help","🚨 Obtener ayuda rápida"))

if submit_request:
    if not name.strip() or not phone.strip() or not email.strip() or not city_zip.strip() or not issue.strip():
        st.error(tr("Please complete all fields so we can route your request quickly.","Por favor complete todos los campos para que podamos enviar su solicitud rápidamente."))
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
            f"<p class='small-note'>{tr('Lead saved to','Lead guardado en')} <strong>{LEADS_FILE.name}</strong>. {tr('Ready for email, SMS, Zapier, or Twilio integration.','Listo para integración por correo electrónico, SMS, Zapier o Twilio.')}</p>",
            unsafe_allow_html=True,
        )
        st.code(log_line)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    f"<div class='sticky-cta'>"
    f"<a class='cta-button' href='#assistant-form'>{tr('🚨 Get Fast AC Help','🚨 Obtener ayuda rápida')}</a>"
    "</div>",
    unsafe_allow_html=True,
)

st.markdown("<div class='footer-card'>", unsafe_allow_html=True)
st.markdown(
    f"<p><strong>{BUSINESS_NAME}</strong> — {tr('Trusted AC repair leads for Haines City homeowners.','Leads de reparación de AC confiables para propietarios de Haines City.')}</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='footer-links'>"
    f"<span>{tr('Lead email','Correo de prospecto')}: {LEAD_EMAIL}</span>"
    f"<span>{tr('Call','Llamada')}: <a href='tel:{CALL_TRACKING_NUMBER}' style='color:#0d6efd;text-decoration:none;'>{CALL_TRACKING_NUMBER}</a></span>"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
