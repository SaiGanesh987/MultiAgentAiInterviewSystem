from llm import llm


class JudgeAgent:

    def final_feedback(self, history):

        prompt = f"""
You are a Senior Hiring Manager.

Interview History:

{history}

Generate a professional interview report.

Include:

1. Overall Score (out of 10)

2. Technical Performance

3. HR Performance

4. GenAI Performance (if available)

5. Strong Areas

6. Weak Areas

7. Communication Skills

8. Suggested Learning Path

9. Hiring Decision

Choose ONE:

- Strong Hire
- Hire
- Maybe
- Reject

Keep the report concise and professional.
"""

        response = llm.invoke(prompt)

        return response.content