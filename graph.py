from typing import TypedDict, List

from langgraph.graph import StateGraph, START, END

from agents.resume_agent import ResumeAgent
from agents.jd_agent import JDAgent
from agents.technical_agent import TechnicalInterviewAgent
from agents.hr_agent import HRAgent
from agents.genai_agent import GenAIAgent
from agents.judge_agent import JudgeAgent

from memory.interview_memory import InterviewMemory


memory = InterviewMemory()

resume_agent = ResumeAgent()
jd_agent = JDAgent()

technical_agent = TechnicalInterviewAgent(memory)
hr_agent = HRAgent(memory)
genai_agent = GenAIAgent(memory)

judge_agent = JudgeAgent()



class InterviewState(TypedDict):

    resume: str
    job_description: str
    role: str

    resume_skills: List[str]
    jd_skills: List[str]
    merged_skills: List[str]

    final_report: str




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



def merge_skills_node(state):

    merged = list(

        set(

            state["resume_skills"]

            +

            state["jd_skills"]

        )

    )

    technical_agent.prepare_topics(merged)

    return {

        **state,

        "merged_skills": merged

    }




def technical_node(state):

    technical_agent.conduct_interview(

        answer_callback=state["answer_callback"]

    )

    return state



def hr_node(state):

    hr_agent.conduct_interview(

        answer_callback=state["answer_callback"]

    )

    return state




def route_genai(state):

    role = state["role"].lower()

    keywords = [

        "ai",

        "ml",

        "machine learning",

        "deep learning",

        "genai",

        "llm",

        "nlp",

        "computer vision",

        "data scientist",

        "artificial intelligence"

    ]

    for keyword in keywords:

        if keyword in role:

            return "genai"

    return "judge"




def genai_node(state):

    genai_agent.conduct_interview(

        answer_callback=state["answer_callback"]

    )

    return state



def judge_node(state):

    report = judge_agent.generate_report(

        memory

    )

    return {

        **state,

        "final_report": report

    }




builder = StateGraph(InterviewState)

builder.add_node("resume", resume_node)

builder.add_node("jd", jd_node)

builder.add_node("merge_skills", merge_skills_node)

builder.add_node("technical", technical_node)

builder.add_node("hr", hr_node)

builder.add_node("genai", genai_node)

builder.add_node("judge", judge_node)


builder.add_edge(START, "resume")

builder.add_edge("resume", "jd")

builder.add_edge("jd", "merge_skills")

builder.add_edge("merge_skills", "technical")

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


interview_graph = builder.compile()