import random

from llm import llm
from agents.evaluator_agent import EvaluatorAgent


class GenAIAgent:
    """
    Conducts the Generative AI interview.

    Responsibilities:
    - Ask GenAI interview questions.
    - Evaluate answers.
    - Store results in InterviewMemory.
    """

    def __init__(self, memory):

        self.memory = memory
        self.evaluator = EvaluatorAgent()

        self.topics = [

            "Transformers",

            "Attention Mechanism",

            "LLMs",

            "Prompt Engineering",

            "Embeddings",

            "RAG",

            "Vector Databases",

            "Fine Tuning",

            "LangChain",

            "LangGraph",

            "AI Agents",

            "MCP"

        ]

        self.asked_topics = []

    

    def generate_question(self):

        remaining = [

            topic

            for topic in self.topics

            if topic not in self.asked_topics

        ]

        if not remaining:
            return None

        topic = random.choice(remaining)

        self.asked_topics.append(topic)

        prompt = f"""
You are a Senior Generative AI Interviewer.

Generate ONE medium-level interview question.

Topic:
{topic}

Rules:
- Ask only one question.
- Do not provide hints.
- Do not provide answers.
- Return ONLY the interview question.
"""

        response = llm.invoke(prompt)

        return {

            "round": "Generative AI",
            "topic": topic,
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

    

    def conduct_interview(self, answer_callback, num_questions=5):

        for _ in range(num_questions):

            question = self.generate_question()

            if question is None:
                break

            answer = answer_callback(

                question["question"]

            )

            self.evaluate_answer(

                question,
                answer

            )