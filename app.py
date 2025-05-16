import pdfplumber
import streamlit as st

ISO_14155_CHECKLIST = [
    "Is the protocol approved by an Ethics Committee?",
    "Are informed consent procedures described and compliant?",
    "Are risk-benefit analyses included and clearly documented?",
    "Is there a monitoring plan described?",
    "Are adverse event reporting procedures detailed?"
]

FDA_CFR_812_CHECKLIST = [
    "Does the protocol identify the investigational device?",
    "Are investigator responsibilities clearly defined?",
    "Is subject protection adequately addressed?",
    "Does the plan include IRB approval documentation?",
    "Are sponsor responsibilities documented?"
]

def analyze_text_against_checklist(text, checklist):
    results = []
    text_lower = text.lower()
    for item in checklist:
        keywords = item.lower().split()
        match_score = sum(1 for word in keywords if word in text_lower) / len(keywords)
        results.append((item, "✅ Likely Addressed" if match_score > 0.5 else "❌ Possibly Missing"))
    return results

st.set_page_config(page_title="Clinical AI Gap Analyzer", layout="wide")
st.title("🧠 Clinical AI Gap Analyzer")
st.markdown("Upload a clinical trial **Protocol** or **SOP**, and check for potential compliance gaps.")

uploaded_file = st.file_uploader("📎 Upload your document (TXT or PDF):", type=["txt", "pdf"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    else:
        text = uploaded_file.read().decode("utf-8")

    st.subheader("📋 ISO 14155 Compliance Check")
    iso_results = analyze_text_against_checklist(text, ISO_14155_CHECKLIST)
    for item, result in iso_results:
        st.markdown(f"- **{item}** — {result}")

    st.subheader("📋 FDA 21 CFR Part 812 Compliance Check")
    fda_results = analyze_text_against_checklist(text, FDA_CFR_812_CHECKLIST)
    for item, result in fda_results:
        st.markdown(f"- **{item}** — {result}")

