import fitz  # PyMuPDF
import re

# Predefined set of common skills
SKILLS_DB = {
    "python", "java", "c++", "html", "css", "javascript", "sql", "excel",
    "power bi", "tableau", "pandas", "numpy", "machine learning",
    "deep learning", "react", "node.js", "flask", "django", "git", "linux",
    "data analysis", "tensorflow", "keras"
}

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_skills(resume_text):
    resume_text = resume_text.lower()
    found_skills = set()
    for skill in SKILLS_DB:
        if re.search(r'\b' + re.escape(skill) + r'\b', resume_text):
            found_skills.add(skill)
    return found_skills
