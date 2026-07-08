import time
import streamlit as st

def stream_text(text: str, speed: float = 0.01):
    placeholder = st.empty()
    output = ""

    for char in text:
        output += char
        placeholder.markdown(output)
        time.sleep(speed)