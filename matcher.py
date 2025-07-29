def match_job_roles(skills):
    job_roles = {
        "Data Analyst": {"python", "excel", "sql", "power bi", "tableau", "data analysis", "pandas", "numpy"},
        "Frontend Developer": {"html", "css", "javascript", "react"},
        "Backend Developer": {"python", "django", "flask", "sql"},
        "Machine Learning Engineer": {"python", "machine learning", "deep learning", "pandas", "numpy"},
        "Full Stack Developer": {"html", "css", "javascript", "react", "node.js", "flask", "django"},
        "DevOps Engineer": {"linux", "git", "python"},
    }

    matched_roles = []

    for role, role_skills in job_roles.items():
        match_count = len(skills & role_skills)
        if match_count >= 2:
            matched_roles.append((role, match_count))

    matched_roles.sort(key=lambda x: x[1], reverse=True)

    return [role for role, _ in matched_roles]
