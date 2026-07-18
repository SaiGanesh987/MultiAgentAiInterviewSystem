from llm import llm


class JudgeAgent:
    """
    Generates the final interview report
    based on InterviewMemory.
    """

    def generate_report(self, interview_memory) -> str:

        memory = interview_memory.get_all_responses()

        prompt = f"""
You are a Senior Hiring Manager.

Below is the complete interview evaluation.

Interview Memory:

{memory}

Analyze the candidate's overall interview performance.

Generate a professional interview report with the following sections.

1. Overall Score (out of 10)

2. Technical Performance
- Overall technical ability
- Strong technical skills
- Weak technical skills

3. HR Performance
- Communication
- Behaviour
- Confidence
- Professionalism

4. Generative AI Performance
(Only if GenAI questions were asked)

5. Strong Areas

6. Weak Areas

7. Learning Recommendations

8. Hiring Decision

Choose exactly one:

- Strong Hire
- Hire
- Maybe Hire
- Reject

Rules:
- Base your decision ONLY on the interview memory.
- Use the evaluator scores and feedback.
- Keep the report professional and concise.
"""

        response = llm.invoke(prompt)

        return response.content.strip()