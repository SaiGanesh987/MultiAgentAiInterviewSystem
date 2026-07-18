import json

from llm import llm


class EvaluatorAgent:
    """
    Evaluates a candidate's answer for a single interview question.
    """

    def evaluate(self, question: str, answer: str) -> dict:

        prompt = f"""
You are a Senior Technical Interview Evaluator.

Evaluate the candidate's answer professionally.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate using the following criteria:
- Technical correctness
- Completeness
- Clarity
- Relevance

Return ONLY valid JSON.

{{
    "score": 8,
    "feedback": "Brief constructive feedback.",
    "ideal_answer": "A concise ideal interview answer.",
    "relevance": "High"
}}

Rules:
- Score must be between 0 and 10.
- Do not return markdown.
- Do not explain anything.
- Return only valid JSON.
"""

        response = llm.invoke(prompt)

        content = response.content.strip()

        # Remove markdown if Gemini returns it
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "").strip()

        elif content.startswith("```"):
            content = content.replace("```", "").strip()

        try:
            return json.loads(content)

        except Exception:

            return {

                "score": 0,

                "feedback": "Unable to evaluate the answer.",

                "ideal_answer": "",

                "relevance": "Low"

            }