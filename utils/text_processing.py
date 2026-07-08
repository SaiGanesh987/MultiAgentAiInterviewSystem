import re

def clean_text(text: str) -> str:
    return text.lower().strip()


def extract_words(text: str):
    return set(re.findall(r"\w+", text.lower()))