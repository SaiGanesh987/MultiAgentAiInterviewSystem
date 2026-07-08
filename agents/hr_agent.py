import random
from llm import llm


class HRAgent:

    def __init__(self):

        self.topics = [

            "Leadership",

            "Teamwork",

            "Communication",

            "Conflict Resolution",

            "Career Goals",

            "Adaptability",

            "Time Management",

            "Problem Solving",

            "Strengths and Weaknesses"

        ]

        self.asked = []

    def generate_question(self):

        remaining = [

            topic

            for topic in self.topics

            if topic not in self.asked

        ]

        if not remaining:

            self.asked = []

            remaining = self.topics

        topic = random.choice(remaining)

        self.asked.append(topic)

        prompt = f"""
You are an experienced HR interviewer.

Generate ONE behavioural interview question.

Topic:

{topic}

Return only the interview question.
"""

        response = llm.invoke(prompt)

        return {

            "round": "HR",

            "topic": topic,

            "question": response.content.strip()

        }