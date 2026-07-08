from dataclasses import dataclass

@dataclass
class Question:
    topic: str
    question: str
    difficulty: str = "medium"


@dataclass
class Answer:
    question: str
    answer: str


@dataclass
class Evaluation:
    score: float
    feedback: str