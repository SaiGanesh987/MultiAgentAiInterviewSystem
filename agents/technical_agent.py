import random
from llm import llm


class TechnicalInterviewAgent:

    def __init__(self):
        self.skills = []
        self.asked_topics = []

    def prepare_topics(self, resume_skills, jd_skills):

        self.skills = list(set(resume_skills + jd_skills))
        random.shuffle(self.skills)

    def generate_question(self):

        if not self.skills:
            raise Exception("No technical skills available.")

        remaining = [
            skill
            for skill in self.skills
            if skill not in self.asked_topics
        ]

        if not remaining:
            self.asked_topics = []
            remaining = self.skills

        topic = random.choice(remaining)
        self.asked_topics.append(topic)

        prompt = f"""
You are a Senior Technical Interviewer.

Generate ONE medium-level interview question.

Topic:
{topic}

Rules:

- Ask only one question.
- Do not provide hints.
- Do not provide the answer.
- Return only the question.
"""

        response = llm.invoke(prompt)

        return {

            "round": "Technical",

            "topic": topic,

            "question": response.content.strip()

        }