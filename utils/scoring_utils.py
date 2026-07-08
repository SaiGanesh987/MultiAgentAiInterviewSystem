from utils.text_processing import extract_words

def compute_relevance(question: str, answer: str):

    if not answer.strip():
        return 0

    q_words = extract_words(question)
    a_words = extract_words(answer)

    overlap = len(q_words.intersection(a_words))

    if overlap == 0:
        return 0

    return min(10, overlap * 3 + 2)


def normalize_score(score: float):
    return round(max(0, min(10, score)), 2)