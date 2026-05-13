import streamlit as st

st.set_page_config(page_title="Quick Air Haines City", layout="centered")

# HERO
st.title("❄️ 24/7 AC Repair in Haines City")
st.subheader("Fast, Affordable, Reliable Service")

st.markdown("**Servicio en Español Disponible** 🇪🇸")

phone_number = "+1XXXXXXXXXX"  # replace later

st.markdown(f"[📞 Call Now](tel:{phone_number})", unsafe_allow_html=True)

st.divider()

# TRUST
st.header("Why Choose Us")
st.write("""
✅ Same-Day & Emergency Service
✅ Honest, Upfront Pricing
✅ Experienced HVAC Technicians
✅ English & Spanish Support
✅ 100% Satisfaction Guaranteed
""")

st.divider()

# SERVICES
st.header("Our Services")
st.write("""
- AC Repair
- AC Installation
- AC Maintenance
- Emergency HVAC Service
- Thermostat Repair
""")

st.divider()

# URGENCY
st.header("AC Not Cooling?")
st.write("Don’t wait. Florida heat is no joke. Get help now.")

st.markdown(f"[📞 Call Now](tel:{phone_number})", unsafe_allow_html=True)

st.divider()

# SPANISH SECTION
st.header("Servicio en Español")
st.write("""
¿Tu aire acondicionado no enfría?
Servicio rápido, confiable y económico en Haines City.
Llámanos hoy mismo.
""")

st.markdown(f"[📞 Llamar Ahora](tel:{phone_number})", unsafe_allow_html=True)

st.divider()

# CONTACT FORM
st.header("Request Service")

name = st.text_input("Name")
phone = st.text_input("Phone")
issue = st.text_area("What’s the issue?")

if st.button("Submit"):
    st.success("Request sent! We'll contact you shortly.")
