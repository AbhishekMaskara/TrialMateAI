# ============================================================
# TrialMate AI
# AI-Powered Clinical Trial Site Copilot
#
# Developer: Abhishek Maskara
# Agilisium MVP Submission
# ============================================================

import streamlit as st
import google.generativeai as genai

from gemini_config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-flash-lite-latest")

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="TrialMate AI",
    page_icon="🩺",
    layout="wide"
)

# ------------------------------------------------------------
# Header
# ------------------------------------------------------------

st.title("🩺 TrialMate AI")

st.subheader(
    "AI-Powered Clinical Trial Site Copilot"
)

# ------------------------------------------------------------
# Introduction
# ------------------------------------------------------------

st.write("""
Welcome to TrialMate AI.

TrialMate AI is designed to support newly onboarded
Clinical Research Coordinators (CRCs) by simplifying:

✅ Clinical Research Terminology

✅ Protocol Interpretation

✅ Patient Eligibility Screening

✅ Investigator Communication

The platform leverages Generative AI to reduce the learning
curve and improve productivity at clinical trial sites.
""")

# ------------------------------------------------------------
# MVP Features
# ------------------------------------------------------------

st.markdown("## 🚀 MVP Features")

col1, col2 = st.columns(2)

with col1:
    st.success("🔍 Clinical Research Knowledge Assistant")
    st.success("📋 Protocol Interpreter")

with col2:
    st.success("📑 Patient Eligibility Screener")
    st.success("📝 Investigator Brief Generator")
# ------------------------------------------------------------
# Status
# ------------------------------------------------------------

st.success("TrialMate AI MVP Successfully Running")

# ------------------------------------------------------------
# Clinical Research Knowledge Assistant
# ------------------------------------------------------------

st.markdown("---")

st.header("🔍 Clinical Research Knowledge Assistant")

question = st.text_input(
    "Ask a Clinical Research Question",
    placeholder="Ask any Clinical Research question..."
)
if st.button("Get Answer"):

    if question.strip() == "":
        st.warning("Please enter a clinical research question.")

    else:

        
        prompt = f"""
          You are TrialMate AI.

          You are a Clinical Research Coordinator (CRC) onboarding assistant.

          Your role is to help newly hired CRCs understand:

          • Clinical trial terminology
          • Protocol requirements
          • Inclusion/Exclusion criteria
          • Adverse event reporting
          • GCP requirements
          • Regulatory documentation
          • Site operations
          • Investigator interactions

          Guidelines:

          1. Assume all questions relate to clinical research.
          2. Explain concepts for newly onboarded CRCs.
          3. Use the following structure:

          Definition:
          Why it matters:
          CRC Example:

          4. Keep answers under 250 words per concept.
          5. Use bullet points when possible.
          6. Avoid unnecessary regulatory detail unless requested.
          7. When explaining a term, provide:
           - Definition
           - Why it matters
           - CRC Action Point
          Question:
          {question}
        """
        try:
             
             with st.spinner("TrialMate AI is thinking..."):
                response = model.generate_content(prompt)

                st.markdown("### 🧠 TrialMate AI Response")
                st.markdown(response.text)
        except Exception as e:
                st.error(f"AI Service Error: {e}")    

# ------------------------------------------------------------
# Protocol Interpreter
# ------------------------------------------------------------

st.markdown("---")

st.header("📋 Protocol Interpreter")

protocol_text = st.text_area(
    "Paste Protocol Section",
    height=250,
    placeholder="Paste Inclusion/Exclusion Criteria or Protocol Text Here..."
)

if st.button("Interpret Protocol"):

    if protocol_text.strip() == "":
        st.warning("Please paste protocol text.")

    else:

        protocol_prompt = f"""
        You are TrialMate AI.

        You are helping a newly onboarded Clinical Research Coordinator (CRC).

         Analyze the protocol section below and provide:

         1. Plain Language Summary
         2. Inclusion Criteria
         3. Exclusion Criteria
         4. CRC Action Points

         Provide the output using the following format.

        ## Plain Language Summary

        (2-3 sentences only)
        Each bullet point must appear on a separate line.
        Do not combine multiple bullet points in one sentence.

        ## Inclusion Criteria

        • bullet points
        Each bullet point must appear on a separate line.
        Do not combine multiple bullet points in one sentence.

        ## Exclusion Criteria

        • bullet points
        Each bullet point must appear on a separate line.
        Do not combine multiple bullet points in one sentence.

        ## CRC Action Points

        • bullet points
        Each bullet point must appear on a separate line.
        Do not combine multiple bullet points in one sentence.

        Keep the entire response under 300 words.

        Do not include greetings, introductions,
        motivational text, or conversational language.

        Be concise and professional.


        Protocol Text:

         {protocol_text}
        """
        try:
            with st.spinner("Analyzing Protocol..."):
    
   
             response = model.generate_content(protocol_prompt)

            st.markdown("### 📑 Protocol Interpretation")

            st.markdown(response.text)
        except Exception as e:
            st.error(f"AI Service Error: {e}")
# ------------------------------------------------------------
# Eligibility Screener
# ------------------------------------------------------------

st.markdown("---")

st.header("📑 Eligibility Screener")

age = st.number_input(
    "Patient Age",
    min_value=0,
    max_value=120,
    value=18
)

diabetes = st.selectbox(
    "Type 2 Diabetes Diagnosis",
    ["Yes", "No"]
)

hba1c = st.number_input(
    "HbA1c (%)",
    min_value=0.0,
    max_value=20.0,
    value=7.0
)

pregnant = st.selectbox(
    "Pregnant",
    ["No", "Yes"]
)

renal = st.selectbox(
    "Severe Renal Disease",
    ["No", "Yes"]
)

if st.button("Evaluate Eligibility"):

    reasons = []

    eligible = True

    if age < 18 or age > 65:
        eligible = False
        reasons.append("Age not within 18-65 years")

    if diabetes == "No":
        eligible = False
        reasons.append("Type 2 Diabetes diagnosis missing")

    if hba1c <= 7:
        eligible = False
        reasons.append("HbA1c must be greater than 7%")

    if pregnant == "Yes":
        eligible = False
        reasons.append("Pregnancy is an exclusion criterion")

    if renal == "Yes":
        eligible = False
        reasons.append("Severe renal disease is an exclusion criterion")

    if eligible:

        st.success("✅ Preliminary Eligibility Criteria Met")

        st.markdown("""
### Screening Summary

• Inclusion criteria satisfied

• No exclusion criteria detected

• Candidate may proceed for investigator review
""")

    else:

        st.error("❌ Not Eligible")

        st.markdown("### Reasons")

        for reason in reasons:
            st.write(f"• {reason}")

# ------------------------------------------------------------
# Investigator Brief Generator
# ------------------------------------------------------------

st.markdown("---")

st.header("📝 Investigator Brief Generator")

patient_id = st.text_input(
    "Patient ID",
    placeholder="PT-001"
)

patient_age = st.number_input(
    "Patient Age",
    min_value=0,
    max_value=120,
    value=18,
    key="brief_age"
)

diagnosis = st.text_input(
    "Diagnosis",
    placeholder="Type 2 Diabetes"
)

patient_hba1c = st.text_input(
    "HbA1c",
    placeholder="8.5%"
)

eligibility_status = st.selectbox(
    "Eligibility Status",
    ["Eligible", "Not Eligible"]
)

if st.button("Generate Investigator Brief"):

    brief_prompt = f"""
    You are TrialMate AI.

    Generate a professional investigator briefing note.

Patient Information:

Patient ID: {patient_id}
Patient Age: {patient_age}
Diagnosis: {diagnosis}
HbA1c: {patient_hba1c}
Eligibility Status: {eligibility_status}

You MUST use the exact values provided above.
Do not replace them with "Not Provided" unless the field is empty.

    Create the report using:

    1. Patient Summary
    2. Eligibility Assessment
    3. Key Findings
    4. Recommended Next Steps

    Keep the report concise and professional.
    Important Rules:

1. Do not invent trial names.
2. Do not invent report IDs.
3. Do not invent dates.
4. Use only the information provided.
5. If information is unavailable, write:
   "Not Provided".
    """

    try:
        with st.spinner("Generating Brief..."):
    
           response = model.generate_content(brief_prompt)

           st.markdown("### 📄 Investigator Brief")

           st.markdown(response.text)
    except Exception as e:
      st.error(f"AI Service Error: {e}")
st.markdown("---")

st.caption(
    "TrialMate AI | AI-Assisted Development MVP | Developed by Abhishek Maskara"
)