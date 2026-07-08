import json

from llm import llm


class EvaluatorAgent:

    def evaluate(self, question, answer):

        prompt = f"""
You are an experienced technical interviewer.

Question

{question}

Candidate Answer

{answer}

Evaluate the answer.

Return ONLY valid JSON.

{{
    "score": 8,
    "feedback": "Short constructive feedback",
    "ideal_answer": "Expected interview answer",
    "relevance": "High/Medium/Low"
}}

Do not return markdown.

Do not return explanation.

Only JSON.
"""

        response = llm.invoke(prompt)

        content = response.content.strip()

        if content.startswith("```json"):
            content = content.replace("```json", "")
            content = content.replace("```", "").strip()

        elif content.startswith("```"):
            content = content.replace("```", "").strip()

        return json.loads(content)