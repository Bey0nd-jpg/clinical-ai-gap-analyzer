import streamlit as st
import pdfplumber

# ----------------------------
# Checklist Definitions
# ----------------------------
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

ICH_GCP_CHECKLIST = [
    "Does the protocol follow the principles of ICH GCP?",
    "Are investigator qualifications documented?",
    "Is confidentiality of records maintained?",
    "Is the investigational product accountability plan clear?",
    "Are essential documents maintained and archived?"
]

DECLARATION_OF_HELSINKI_CHECKLIST = [
    "Is participant welfare prioritized over scientific interests?",
    "Is post-study access to treatment addressed?",
    "Is compensation for research-related injury included?",
    "Are vulnerable populations specially protected?",
    "Is ethical review documented and transparent?"
]

# ----------------------------
# Analysis Logic
# ----------------------------
def analyze_text_against_checklist(text, checklist):
    results = []
    text_lower = text.lower()
    matched_count = 0
    for item in checklist:
        keywords = item.lower().split()
        match_score = sum(1 for word in keywords if word in text_lower) / len(keywords)
        result = "✅ Likely Addressed" if match_score > 0.5 else "❌ Possibly Missing"
        if match_score > 0.5:
            matched_count += 1
        results.append((item, result))
    confidence = matched_count / len(checklist) * 100
    return results, confidence

def classify_document(text):
    text_lower = text.lower()
    if "protocol" in text_lower:
        return "Protocol"
    elif "standard operating procedure" in text_lower or "sop" in text_lower:
        return "SOP"
    else:
        return "Unknown"

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Clinical AI Gap Analyzer", layout="wide")
st.title("🧠 Clinical AI Gap Analyzer")
st.markdown("Upload one or more clinical trial **Protocols** or **SOPs**, then select standards to check for potential compliance gaps.")

uploaded_files = st.file_uploader(
    "📎 Upload your document(s) (TXT or PDF):",
    type=["txt", "pdf"],
    accept_multiple_files=True
)

st.sidebar.header("🔍 Select Compliance Standards")
check_iso = st.sidebar.checkbox("ISO 14155", value=True)
check_fda = st.sidebar.checkbox("FDA 21 CFR Part 812", value=True)
check_ich = st.sidebar.checkbox("ICH GCP E6(R2)", value=False)
check_helsinki = st.sidebar.checkbox("Declaration of Helsinki", value=False)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.markdown(f"### 📄 Document: {uploaded_file.name}")

        if uploaded_file.type == "application/pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        else:
            text = uploaded_file.read().decode("utf-8")

        doc_type = classify_document(text)
        st.markdown(f"**Document type:** {doc_type}")

        overall_confidences = []

        if check_iso:
            results, confidence = analyze_text_against_checklist(text, ISO_14155_CHECKLIST)
            st.subheader("ISO 14155 Compliance Check")
            for item, res in results:
                st.markdown(f"- **{item}** — {res}")
            st.markdown(f"**Audit Confidence Score:** {confidence:.1f}%")
            overall_confidences.append(("ISO 14155", confidence))

        if check_fda:
            results, confidence = analyze_text_against_checklist(text, FDA_CFR_812_CHECKLIST)
            st.subheader("FDA 21 CFR Part 812 Compliance Check")
            for item, res in results:
                st.markdown(f"- **{item}** — {res}")
            st.markdown(f"**Audit Confidence Score:** {confidence:.1f}%")
            overall_confidences.append(("FDA 21 CFR Part 812", confidence))

        if check_ich:
            results, confidence = analyze_text_against_checklist(text, ICH_GCP_CHECKLIST)
            st.subheader("ICH GCP E6(R2) Compliance Check")
            for item, res in results:
                st.markdown(f"- **{item}** — {res}")
            st.markdown(f"**Audit Confidence Score:** {confidence:.1f}%")
            overall_confidences.append(("ICH GCP E6(R2)", confidence))

        if check_helsinki:
            results, confidence = analyze_text_against_checklist(text, DECLARATION_OF_HELSINKI_CHECKLIST)
            st.subheader("Declaration of Helsinki Compliance Check")
            for item, res in results:
                st.markdown(f"- **{item}** — {res}")
            st.markdown(f"**Audit Confidence Score:** {confidence:.1f}%")
            overall_confidences.append(("Declaration of Helsinki", confidence))

        # Overall recommendations based on confidence
        if overall_confidences:
            avg_confidence = sum(c for _, c in overall_confidences) / len(overall_confidences)
            st.markdown(f"### 🔎 Overall Audit Confidence: {avg_confidence:.1f}%")
            if avg_confidence > 80:
                st.success("High audit readiness! 🎉")
            elif avg_confidence > 50:
                st.warning("Moderate audit readiness. Consider addressing flagged gaps.")
            else:
                st.error("Low audit readiness. Significant gaps found.")


