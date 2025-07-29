# skills.py

import re

# A simple list of tech-related skills (you can expand this)
SKILLS_DB = [
    "python", "java", "c++", "sql", "javascript", "react", "nodejs", "html", "css",
    "excel", "power bi", "tableau", "django", "flask", "pandas", "numpy", "matplotlib",
    "tensorflow", "keras", "scikit-learn", "nlp", "git", "github", "aws", "azure", "linux"
]

def extract_skills(text):
    """
    Extract skills from resume text using keyword matching.
    """
    text = text.lower()
    extracted = []

    for skill in SKILLS_DB:
        # Use word boundaries to avoid partial matches (e.g., "java" inside "javascript")
        if re.search(rf'\b{re.escape(skill)}\b', text):
            extracted.append(skill)

    return list(set(extracted))
