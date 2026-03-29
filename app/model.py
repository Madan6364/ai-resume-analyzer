from app.skills import skills_list
import spacy

nlp = spacy.load("en_core_web_sm")


def analyze_resume(text):

    text = text.lower()
    doc = nlp(text)

    # -----------------------------------
    # 1. SKILL DETECTION (max 40 marks)
    # -----------------------------------

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text:
            found_skills.append(skill)

    total_skills = len(skills_list)
    skill_score = (len(found_skills) / total_skills) * 40


    # -----------------------------------
    # 2. PROFESSIONAL SUMMARY (10 marks)
    # -----------------------------------

    summary_score = 0

    if "summary" in text or "profile" in text or "objective" in text:
        summary_score = 10


    # -----------------------------------
    # 3. EXPERIENCE SECTION (15 marks)
    # -----------------------------------

    experience_score = 0

    if "experience" in text:
        experience_score += 5

    if "internship" in text:
        experience_score += 5

    if "worked" in text or "developed" in text or "implemented" in text:
        experience_score += 5


    # -----------------------------------
    # 4. PROJECT SECTION (15 marks)
    # -----------------------------------

    project_score = 0

    if "project" in text:
        project_score += 5

    if "machine learning project" in text:
        project_score += 5

    if "built" in text or "created" in text:
        project_score += 5


    # -----------------------------------
    # 5. EDUCATION SECTION (10 marks)
    # -----------------------------------

    education_score = 0

    if "education" in text:
        education_score += 5

    if "btech" in text or "bachelor" in text:
        education_score += 5


    # -----------------------------------
    # 6. RESUME STRUCTURE (10 marks)
    # -----------------------------------

    structure_score = 0

    sections = ["skills", "education", "projects", "experience"]

    for section in sections:
        if section in text:
            structure_score += 2.5


    # -----------------------------------
    # FINAL ATS SCORE (out of 100)
    # -----------------------------------

    ats_score = (
        skill_score
        + summary_score
        + experience_score
        + project_score
        + education_score
        + structure_score
    )

    # -----------------------------------
    # Missing skills automatically
    # -----------------------------------

    missing_skills = []

    for skill in skills_list:
        if skill not in found_skills:
            missing_skills.append(skill)

    return {
        "ATS_score": round(ats_score),
        "skills_found": found_skills,
        "missing_skills": missing_skills,
        "skill_score": round(skill_score),
        "summary_score": summary_score,
        "experience_score": experience_score,
        "project_score": project_score,
        "education_score": education_score,
        "structure_score": structure_score,
        "status": "Resume analyzed successfully"
    }