import random
from llm import llm


class GenAIAgent:

    def __init__(self):

        self.topics = [

            "Transformers",

            "Attention Mechanism",

            "Embeddings",

            "LLMs",

            "Prompt Engineering",

            "RAG",

            "Vector Databases",

            "Fine Tuning",

            "LangChain",

            "LangGraph"

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
You are a Senior Generative AI Interviewer.

Generate ONE medium difficulty interview question.

Topic:

{topic}

Return only the question.
"""

        response = llm.invoke(prompt)

        return {

            "round": "Generative AI",

            "topic": topic,

            "question": response.content.strip()

        }