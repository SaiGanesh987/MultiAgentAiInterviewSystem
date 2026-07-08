from llm import llm


class JDAgent:

    def extract_skills(self, jd):

        prompt = f"""
You are an expert Hiring Manager.

Extract ONLY technical skills required for this Job Description.

Rules

- Ignore company information
- Ignore salary
- Ignore responsibilities
- Remove duplicates
- Return ONLY comma separated skills.

Job Description

{jd}
"""

        response = llm.invoke(prompt)

        skills = response.content.split(",")

        return [

            skill.strip().lower()

            for skill in skills

            if skill.strip()

        ]