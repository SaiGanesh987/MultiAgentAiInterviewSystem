import random

from llm import llm
from agents.evaluator_agent import EvaluatorAgent


class TechnicalInterviewAgent:
    """
    Conducts the technical interview.

    Responsibilities:
    - Ask technical questions from merged skills.
    - Ask two DSA questions.
    - Evaluate every answer.
    - Store results in InterviewMemory.
    """

    def __init__(self, memory):

        self.memory = memory
        self.evaluator = EvaluatorAgent()

        self.skills = []
        self.asked_skills = []

    

    def prepare_topics(self, skills: list[str]):

        self.skills = list(set(skills))
        random.shuffle(self.skills)
        self.asked_skills = []


    def generate_skill_question(self):

        remaining = [

            skill

            for skill in self.skills

            if skill not in self.asked_skills

        ]

        if not remaining:
            return None

        topic = random.choice(remaining)

        self.asked_skills.append(topic)

        prompt = f"""
You are a Senior Software Engineer conducting an interview.

Generate ONE medium-level technical interview question.

Topic:
{topic}

Rules:
- Ask only one question.
- Do NOT provide hints.
- Do NOT provide the answer.
- Question should test practical understanding.
- Return ONLY the interview question.
"""

        response = llm.invoke(prompt)

        return {

            "round": "Technical",
            "topic": topic,
            "question": response.content.strip()

        }

    

    def generate_dsa_question(self):

        prompt = """
You are a Senior Software Engineer.

Generate ONE medium-level Data Structures and Algorithms interview question.

Rules:
- Cover arrays, strings, linked lists, stacks, queues,
  trees, graphs, recursion, dynamic programming,
  hashing or sorting.
- Do NOT provide hints.
- Do NOT provide solution.
- Return ONLY the interview question.
"""

        response = llm.invoke(prompt)

        return {

            "round": "Technical",
            "topic": "DSA",
            "question": response.content.strip()

        }

    

    def evaluate_answer(self, question_data, answer):

        evaluation = self.evaluator.evaluate(

            question_data["question"],
            answer

        )

        self.memory.add_response(

            round_name=question_data["round"],
            topic=question_data["topic"],
            question=question_data["question"],
            answer=answer,
            score=evaluation["score"],
            feedback=evaluation["feedback"],
            ideal_answer=evaluation["ideal_answer"],
            relevance=evaluation["relevance"]

        )

        return evaluation

    

    def conduct_interview(self, answer_callback):

        """
        answer_callback(question) -> candidate answer

        Example:

        answer = answer_callback(question_text)
        """

        # Skill Questions

        while True:

            question = self.generate_skill_question()

            if question is None:
                break

            answer = answer_callback(question["question"])

            self.evaluate_answer(

                question,

                answer

            )

        # Two DSA Questions

        for _ in range(2):

            question = self.generate_dsa_question()

            answer = answer_callback(question["question"])

            self.evaluate_answer(

                question,

                answer

            )