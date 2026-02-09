import streamlit as st
import requests
import re

# --------------------
# CONFIG
# --------------------
URL = "https://82e4-34-132-216-141.ngrok-free.app/generate"
API_KEY = "secret123"

# --------------------
# UI
# --------------------
st.set_page_config(page_title="Remote LLM", layout="centered")

st.title("🧠 smartChat")
st.caption("Type anything – model runs on Kaggle GPU")

prompt = st.text_area(
    "Enter your prompt",
    placeholder="Ask me anything...",
    height=200
)

max_length = st.slider(
    "Max tokens",
    min_value=50,
    max_value=1000,
    value=300,
    step=50
)


def _clean_response(text: str) -> str:
    return re.sub(r"^\s*user0\s*:\s*", "", text, flags=re.IGNORECASE)

if st.button("🚀 Generate"):
    if not prompt.strip():
        st.warning("Please type something first.")
    else:
        with st.spinner("Generating..."):
            res = requests.post(
                URL,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "prompt": prompt,
                    "max_length": max_length
                },
                timeout=300
            )

        if res.status_code == 200:
            answer = res.json().get("response", "")
            if isinstance(answer, str):
                answer = _clean_response(answer)
            st.subheader("Response")
            st.write(answer)
        else:
            st.error(f"Error {res.status_code}: {res.text}")