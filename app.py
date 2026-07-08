import streamlit as st

from graph import graph

from agents.technical_agent import TechnicalInterviewAgent
from agents.hr_agent import HRAgent
from agents.genai_agent import GenAIAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.judge_agent import JudgeAgent


# --------------------------
# Agents
# --------------------------

technical_agent = TechnicalInterviewAgent()

hr_agent = HRAgent()

genai_agent = GenAIAgent()

evaluator = EvaluatorAgent()

judge = JudgeAgent()


# --------------------------
# Page Config
# --------------------------

st.set_page_config(

    page_title="AI Interview Platform",

    page_icon="🤖",

    layout="wide"

)

st.title("🤖 Multi-Agent AI Interview Platform")

st.markdown("---")


# --------------------------
# Session State
# --------------------------

if "started" not in st.session_state:

    st.session_state.started = False

if "history" not in st.session_state:

    st.session_state.history = []

if "question_no" not in st.session_state:

    st.session_state.question_no = 0

if "questions" not in st.session_state:

    st.session_state.questions = []

if "graph_state" not in st.session_state:

    st.session_state.graph_state = None

if "technical_count" not in st.session_state:

    st.session_state.technical_count = 5

if "hr_count" not in st.session_state:

    st.session_state.hr_count = 3

if "genai_count" not in st.session_state:

    st.session_state.genai_count = 2


# --------------------------
# User Inputs
# --------------------------

resume = st.text_area(

    "Paste Resume",

    height=250

)

jd = st.text_area(

    "Paste Job Description",

    height=250

)

role = st.text_input(

    "Job Role",

    placeholder="Machine Learning Engineer"

)


# --------------------------
# Start Interview
# --------------------------

if st.button("Start Interview"):

    initial_state = {

        "resume": resume,

        "job_description": jd,

        "role": role,

        "resume_skills": [],

        "jd_skills": [],

        "technical_ready": False,

        "hr_ready": False,

        "genai_required": False,

        "history": [],

        "final_report": ""

    }

    result = graph.invoke(initial_state)

    st.session_state.graph_state = result

    technical_agent.prepare_topics(

        result["resume_skills"],

        result["jd_skills"]

    )

    st.session_state.started = True

    st.session_state.question_no = 0

    st.session_state.history = []

    st.success("Interview Initialized Successfully!")

    st.rerun()


# --------------------------
# Waiting for Part B
# --------------------------

if st.session_state.started:

    st.info(

        "Interview Ready. Loading questions..."

    )


# --------------------------
# Interview Flow
# --------------------------

if st.session_state.started:

    q_no = st.session_state.question_no

    # --------------------
    # Technical Round
    # --------------------

    if q_no < st.session_state.technical_count:

        current = technical_agent.generate_question()

    # --------------------
    # HR Round
    # --------------------

    elif q_no < (
        st.session_state.technical_count
        + st.session_state.hr_count
    ):

        current = hr_agent.generate_question()

    # --------------------
    # GenAI Round
    # --------------------

    elif (
        st.session_state.graph_state["genai_required"]
        and
        q_no
        <
        st.session_state.technical_count
        + st.session_state.hr_count
        + st.session_state.genai_count
    ):

        current = genai_agent.generate_question()

    else:

        current = None


    # --------------------
    # Ask Question
    # --------------------

    if current is not None:

        st.markdown("---")

        st.subheader(

            f"Question {q_no+1}"

        )

        st.write(

            current["question"]

        )

        answer = st.text_area(

            "Your Answer",

            key=f"answer_{q_no}"

        )

        if st.button("Submit Answer"):

            if answer.strip() == "":

                st.warning(

                    "Please answer the question."

                )

                st.stop()

            evaluation = evaluator.evaluate(

                current["question"],

                answer

            )

            st.session_state.history.append(

                {

                    "round": current["round"],

                    "topic": current["topic"],

                    "question": current["question"],

                    "answer": answer,

                    "score": evaluation["score"],

                    "feedback": evaluation["feedback"],

                    "ideal_answer": evaluation["ideal_answer"],

                    "relevance": evaluation["relevance"]

                }

            )

            st.success(

                f"Score : {evaluation['score']}/10"

            )

            st.info(

                evaluation["feedback"]

            )

            with st.expander(

                "Ideal Answer"

            ):

                st.write(

                    evaluation["ideal_answer"]

                )

            st.session_state.question_no += 1

            st.rerun()



# --------------------------
# Interview Completed
# --------------------------

if st.session_state.started:

    total_questions = (
        st.session_state.technical_count
        + st.session_state.hr_count
    )

    if st.session_state.graph_state["genai_required"]:
        total_questions += st.session_state.genai_count

    if st.session_state.question_no >= total_questions:

        st.balloons()

        st.success("Interview Completed Successfully!")

        scores = [

            item["score"]

            for item in st.session_state.history

        ]

        average_score = round(

            sum(scores) / len(scores),

            2

        )

        report = judge.final_feedback(

            st.session_state.history

        )

        st.markdown("---")

        st.header("Interview Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Questions Answered",

                len(st.session_state.history)

            )

        with col2:

            st.metric(

                "Average Score",

                average_score

            )

        st.markdown("---")

        st.subheader("Detailed Results")

        for i, item in enumerate(

            st.session_state.history,

            start=1

        ):

            with st.expander(

                f"Question {i}"

            ):

                st.write(

                    f"**Round:** {item['round']}"

                )

                st.write(

                    f"**Topic:** {item['topic']}"

                )

                st.write(

                    f"**Question:** {item['question']}"

                )

                st.write(

                    f"**Your Answer:** {item['answer']}"

                )

                st.write(

                    f"**Score:** {item['score']}/10"

                )

                st.write(

                    f"**Feedback:** {item['feedback']}"

                )

                st.write(

                    f"**Ideal Answer:** {item['ideal_answer']}"

                )

        st.markdown("---")

        st.header("Hiring Manager Report")

        st.write(report)

        st.download_button(

            label="Download Report",

            data=report,

            file_name="Interview_Report.txt",

            mime="text/plain"

        )

        if st.button("Start New Interview"):

            st.session_state.started = False

            st.session_state.question_no = 0

            st.session_state.history = []

            st.session_state.graph_state = None

            st.rerun()