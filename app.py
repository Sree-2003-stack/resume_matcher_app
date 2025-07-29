import streamlit as st
from extractor import extract_text_from_pdf, extract_skills
from matcher import match_job_roles

st.title("📄 Resume Parser + Job Role Matcher")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    skills = extract_skills(text)
    matched_jobs = match_job_roles(skills)

    st.subheader("✅ Extracted Skills:")
    st.write(", ".join(skills) if skills else "No matching skills found.")

    st.subheader("🎯 Suggested Job Roles:")
    st.write(", ".join(matched_jobs) if matched_jobs else "No matching job roles found.")
