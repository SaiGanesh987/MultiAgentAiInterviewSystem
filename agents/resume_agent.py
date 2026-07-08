from llm import llm


class ResumeAgent:

    def extract_skills(self, resume):

        prompt = f"""
You are an expert Technical Recruiter.

Extract ONLY the technical skills from the following resume.

Rules:
- Ignore education
- Ignore projects
- Ignore certifications
- Ignore soft skills
- Remove duplicates
- Return ONLY comma separated skills.

Resume:

{resume}
"""

        response = llm.invoke(prompt)

        skills = response.content.split(",")

        return [

            skill.strip().lower()

            for skill in skills

            if skill.strip()

        ]