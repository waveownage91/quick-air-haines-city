# Quick Air Haines City

A Streamlit landing page for Quick Air Haines City, designed to generate HVAC repair leads through a bilingual intake assistant and contact form.

## What’s included

- Modern blue/white HVAC landing page
- Bilingual English/Spanish support
- Chatbot-style intake assistant
- Standard fallback contact form
- Local lead storage in `leads.csv`
- Placeholder integration for Zapier, Twilio, and email

## Deployment

1. Push this repository to GitHub.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Select `waveownage91/quick-air-haines-city`.
4. Set the main file to `app.py`.
5. Deploy.

## Local Run

Install dependencies and run locally:

```bash
python -m pip install streamlit
streamlit run app.py
```

## Lead storage

- Submitted leads are stored locally in `leads.csv`.
- Each lead includes timestamp, language, contact details, issue, emergency level, and preferred contact method.
- The app also logs the lead to stdout for later integration with Zapier, Make, Twilio, or an email workflow.

## Placeholder variables

- `CALL_TRACKING_NUMBER`
- `LEAD_EMAIL`
- `ZAPIER_WEBHOOK_URL`
- `TWILIO_PHONE_NUMBER`

