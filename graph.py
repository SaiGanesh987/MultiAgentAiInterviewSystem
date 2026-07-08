from typing import TypedDict, List

from langgraph.graph import StateGraph, END

from agents.resume_agent import ResumeAgent
from agents.jd_agent import JDAgent
from agents.technical_agent import TechnicalInterviewAgent
from agents.hr_agent import HRAgent
from agents.genai_agent import GenAIAgent
from agents.judge_agent import JudgeAgent


# -----------------------------
# Agents
# -----------------------------

resume_agent = ResumeAgent()
jd_agent = JDAgent()
technical_agent = TechnicalInterviewAgent()
hr_agent = HRAgent()
genai_agent = GenAIAgent()
judge_agent = JudgeAgent()


# -----------------------------
# Graph State
# -----------------------------

class InterviewState(TypedDict):

    resume: str
    job_description: str
    role: str

    resume_skills: List[str]
    jd_skills: List[str]

    technical_ready: bool
    hr_ready: bool
    genai_required: bool

    history: list

    final_report: str


# -----------------------------
# Nodes
# -----------------------------

def resume_node(state):

    skills = resume_agent.extract_skills(
        state["resume"]
    )

    return {

        **state,

        "resume_skills": skills

    }


def jd_node(state):

    skills = jd_agent.extract_skills(
        state["job_description"]
    )

    return {

        **state,

        "jd_skills": skills

    }


def technical_node(state):

    technical_agent.prepare_topics(

        state["resume_skills"],

        state["jd_skills"]

    )

    return {

        **state,

        "technical_ready": True

    }


def hr_node(state):

    return {

        **state,

        "hr_ready": True

    }


def route_genai(state):

    role = state["role"].lower()

    ai_keywords = [

        "machine learning",

        "ml",

        "ai",

        "genai",

        "llm",

        "deep learning",

        "computer vision",

        "nlp",

        "data scientist"

    ]

    for keyword in ai_keywords:

        if keyword in role:

            return "genai"

    return "judge"


def genai_node(state):

    return {

        **state,

        "genai_required": True

    }


def judge_node(state):

    report = judge_agent.final_feedback(

        state["history"]

    )

    return {

        **state,

        "final_report": report

    }


# -----------------------------
# Build Graph
# -----------------------------

builder = StateGraph(InterviewState)

builder.add_node("resume", resume_node)

builder.add_node("jd", jd_node)

builder.add_node("technical", technical_node)

builder.add_node("hr", hr_node)

builder.add_node("genai", genai_node)

builder.add_node("judge", judge_node)


builder.set_entry_point("resume")

builder.add_edge("resume", "jd")

builder.add_edge("jd", "technical")

builder.add_edge("technical", "hr")

builder.add_conditional_edges(

    "hr",

    route_genai,

    {

        "genai": "genai",

        "judge": "judge"

    }

)

builder.add_edge("genai", "judge")

builder.add_edge("judge", END)

graph = builder.compile()