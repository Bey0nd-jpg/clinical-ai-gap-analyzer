# Clinical AI Gap Analyzer (Pre-Audit Tool)

A Streamlit-based application that uses AI to identify gaps in clinical trial documentation and procedures based on key global regulatory standards (e.g., ISO 14155, FDA CFR 812, ICH GCP).

---

## 🔍 What It Does

This tool is designed to help investigator sites, sponsors, and clinical QA teams:

- ✅ Pre-screen documentation (e.g., protocols, SOPs) before audits
- 🔎 Identify regulatory and procedural inconsistencies
- 📊 Receive audit confidence scores and readiness recommendations
- 🧠 Promote a culture of self-correction and proactive quality assurance

---

## 💡 Key Features

- **📂 Upload Multiple Files**  
  Analyze multiple PDFs or text documents in one session.

- **🧾 Document Classification**  
  Automatically detect and label document type: Protocol, SOP, or Unknown.

- **🧠 AI-Powered Rule Matching**  
  Uses NLP and logic to check documents against international compliance frameworks.

- **✅ Regulatory Coverage**  
  Evaluates against ISO 14155:2020, ICH GCP E6(R2), FDA 21 CFR Part 812, and the Declaration of Helsinki.

- **📋 Custom Checklists**  
  Upload your own checklist to compare documents to internal SOPs or quality standards.

- **📈 Audit Confidence Scoring**  
  Get a numeric score (0–100%) with visual cues for readiness: High, Medium, Low.

- **📤 Exportable Results**  
  Download summary reports in CSV or PDF and full gap analysis as TXT.

---

## 🛠️ Technologies Used

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- `pdfplumber` for document parsing
- `pandas` for data handling
- `fpdf` for PDF report generation
- Regex and simple NLP for rule-based detection

---

## 🔐 Legal & IP Notice

© 2025 Kelsie Tinker. All rights reserved.

This repository and its contents are protected under U.S. copyright law. Redistribution or commercial use is prohibited without explicit permission.

This application is **patent-pending** (USPTO Provisional Patent #ToBeFiled).

---

## 📈 Future Features (Roadmap)

- 🔄 Integration with eTMF and CTMS platforms
- 🌍 Multi-language support for international teams
- 🧠 Advanced AI scoring using LLMs like GPT-4
- 📌 Rule annotation within document context
- 🧩 Modular rule plug-ins for customizable compliance logic

---

## 🤝 Licensing / Business Inquiries

For licensing, customization, or enterprise deployment, contact:  
📧 mkelsie.tinker@gmail.com
