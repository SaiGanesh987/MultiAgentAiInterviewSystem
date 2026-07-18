# 🎯 Multi-Agent AI Interview System

An intelligent **AI-powered interview system** built using **LangGraph, LangChain, and Gemini**, where multiple specialized AI agents collaborate to conduct a complete interview based on a candidate's **Resume** and **Job Description**.

---

# 🚀 Features

- 📄 Resume skill extraction using AI
- 💼 Job Description skill extraction
- 🔄 Automatic skill merging and duplicate removal
- 💻 Technical interview based on extracted skills
- 🧩 Dynamic DSA question generation
- 👥 Behavioral HR interview
- 🤖 Conditional Generative AI interview (for AI/ML roles)
- 📊 AI-powered answer evaluation after every question
- 📝 Interview memory to store responses, scores, and feedback
- 📈 Final hiring report with strengths, weaknesses, learning recommendations, and hiring decision
- 🏗️ Modular Multi-Agent Architecture using LangGraph

---

# 🧠 Multi-Agent Workflow

```
                Resume
                   │
                   ▼
            ResumeAgent
                   │
                   ▼
          Extract Resume Skills
                   │
                   ▼
              JDAgent
                   │
                   ▼
           Extract JD Skills
                   │
                   ▼
        Merge & Remove Duplicates
                   │
                   ▼
     TechnicalInterviewAgent
        │
        ├── Skill Questions
        ├── DSA Questions
        ├── EvaluatorAgent
        └── InterviewMemory
                   │
                   ▼
              HRAgent
        │
        ├── Behavioral Questions
        ├── EvaluatorAgent
        └── InterviewMemory
                   │
          AI/ML Role?
          ├───────────────┐
          │               │
         Yes              No
          │               │
          ▼               │
      GenAIAgent          │
        │                 │
        ├── GenAI Questions
        ├── EvaluatorAgent
        └── InterviewMemory
          │
          ▼
      JudgeAgent
          │
          ▼
  Final Interview Report
```

---

# 🤖 Agents

## 📄 ResumeAgent
- Extracts technical skills from the candidate's resume.

## 💼 JDAgent
- Extracts required technical skills from the Job Description.

## 💻 TechnicalInterviewAgent
- Conducts technical interviews.
- Generates questions from merged skills.
- Generates DSA questions.
- Evaluates every answer.

## 👥 HRAgent
- Conducts behavioral interviews.
- Evaluates communication and soft skills.

## 🤖 GenAIAgent
- Activated only for AI/ML-related roles.
- Conducts Generative AI interviews.

## 📊 EvaluatorAgent
Evaluates every candidate response and returns:
- Score (0–10)
- Feedback
- Ideal Answer
- Relevance

## 📝 InterviewMemory
Stores:
- Question
- Candidate Answer
- Score
- Feedback
- Ideal Answer
- Relevance

## 🧑‍⚖️ JudgeAgent
Generates the final interview report using all stored interview results.

---

# 🛠️ Tech Stack

- Python
- LangGraph
- LangChain
- Google Gemini
- LangChain Google Generative AI
- Pydantic
- Python Dotenv

---

# 📂 Project Structure

```
MultiAgentAiInterviewSystem/
│
├── agents/
│   ├── resume_agent.py
│   ├── jd_agent.py
│   ├── technical_agent.py
│   ├── hr_agent.py
│   ├── genai_agent.py
│   ├── evaluator_agent.py
│   └── judge_agent.py
│
├── memory/
│   └── interview_memory.py
│
├── graph.py
├── llm.py
├── requirements.txt
└── README.md
```

---

# ▶️ Installation

```bash
git clone https://github.com/SaiGanesh987/MultiAgentAiInterviewSystem.git

cd MultiAgentAiInterviewSystem

pip install -r requirements.txt
```

---

# 📈 Future Improvements

- Streamlit Web Interface
- Voice-Based Interview
- Webcam & Emotion Analysis
- PDF Interview Report
- Interview Analytics Dashboard
- Interview History Database
- Authentication System
- Resume Ranking
- Multi-language Interview Support

---

# ⭐ Highlights

- Multi-Agent AI Architecture
- Resume-Aware Interview Generation
- Job Description Matching
- Adaptive Technical Interview
- Automatic Answer Evaluation
- AI-Powered Hiring Decision
- Built using LangGraph & LangChain
