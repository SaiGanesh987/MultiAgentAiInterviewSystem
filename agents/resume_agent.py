from llm import llm


class ResumeAgent:
    """
    Extracts technical skills from a candidate's resume.
    """

    def extract_skills(self, resume: str) -> list[str]:

        prompt = f"""
You are an expert Technical Recruiter.

Your task is to extract ONLY the candidate's technical skills from the resume.

Instructions:
- Extract programming languages.
- Extract frameworks.
- Extract libraries.
- Extract databases.
- Extract cloud platforms.
- Extract developer tools.
- Extract AI/ML technologies.
- Extract operating systems if mentioned.
- Ignore education.
- Ignore projects.
- Ignore achievements.
- Ignore certifications.
- Ignore soft skills.
- Remove duplicates.
- Return ONLY a comma-separated list.
- Do not explain anything.

Resume:

{resume}
"""

        response = llm.invoke(prompt)

        skills = response.content.split(",")

        return list(
            {
                skill.strip().lower()
                for skill in skills
                if skill.strip()
            }
        )