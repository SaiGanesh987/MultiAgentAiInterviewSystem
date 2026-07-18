from llm import llm


class JDAgent:
    """
    Extracts required technical skills from a Job Description.
    """

    def extract_skills(self, job_description: str) -> list[str]:

        prompt = f"""
You are an expert Hiring Manager.

Extract ONLY the required technical skills from the following Job Description.

Instructions:
- Extract programming languages.
- Extract frameworks.
- Extract libraries.
- Extract databases.
- Extract cloud technologies.
- Extract AI/ML technologies.
- Extract developer tools.
- Ignore company information.
- Ignore responsibilities.
- Ignore qualifications unrelated to technical skills.
- Ignore salary and benefits.
- Remove duplicates.
- Return ONLY a comma-separated list.
- Do not explain anything.

Job Description:

{job_description}
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