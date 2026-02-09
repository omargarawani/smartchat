🧠 Remote LLM Inference with Kaggle + Streamlit

This project demonstrates how to run a large language model (LLM) remotely on Kaggle GPU and interact with it using a local Streamlit frontend.

The goal is to separate model inference from the user interface, simulating a real-world AI deployment setup.

🚀 Project Overview
Architecture
Local Machine (Streamlit UI)
|
|  HTTP Requests (ngrok)
v
Kaggle GPU (FastAPI + LLM)


The backend runs on Kaggle using GPU

The frontend runs locally using Streamlit

Communication happens via a REST API

No heavy models are run locally

🧩 Components
🔹 Backend (Kaggle)

FastAPI server

Large Language Model: mistralai/Mistral-Nemo-Instruct-2407

GPU inference using PyTorch

API key authentication

Public access via ngrok

🔹 Frontend (Local)

Streamlit web interface

Prompt input + token length control

Sends requests to the remote API

Displays generated responses

📂 Project Structure
.
├── backend.py          # FastAPI backend (run on Kaggle)
├── streamlit_app.py    # Streamlit frontend (run locally)
├── requirements.txt
└── README.md

⚙️ Backend Setup (Kaggle)

Create a Kaggle Notebook with GPU enabled

Install dependencies:

pip install fastapi uvicorn pyngrok transformers accelerate torch


Run backend.py

Copy the generated ngrok public URL, for example:

https://abc123.ngrok-free.app


The backend exposes:

POST /generate

💻 Frontend Setup (Local)

Install dependencies:

pip install streamlit requests


Update the backend URL in streamlit_app.py:

URL = "https://abc123.ngrok-free.app/generate"


Run Streamlit:

streamlit run streamlit_app.py


Open the browser at:

http://localhost:8501

🔐 API Authentication

Requests must include an API key in the header:

Authorization: Bearer secret123


This is handled automatically in the Streamlit frontend.

🧪 Example API Request
import requests

URL = "https://YOUR_NGROK_LINK/generate"
headers = {"Authorization": "Bearer secret123"}
payload = {
"prompt": "Who is Lionel Messi?",
"max_length": 300
}

res = requests.post(URL, headers=headers, json=payload)
print(res.json()["response"])

📌 Key Learnings

Deploying ML models as REST APIs

Client–server architecture for AI systems

Using remote GPUs efficiently

Integrating FastAPI with Streamlit

Moving beyond notebook-only ML workflows

⚠️ Notes & Limitations

Kaggle notebooks may sleep, causing the API to go offline

ngrok URLs change on every restart

Initial request may be slow due to model loading

🔮 Possible Improvements

Token-by-token streaming

Chat memory support

Better authentication (JWT)

Persistent deployment (HF Spaces / VPS)

UI enhancements (chat-style interface)

🙏 Acknowledgment

Special thanks to the company/team that taught and guided me — the practical knowledge and support I received played a key role in building this project.

📬 Feedback

Feedback, suggestions, and improvements are always welcome!
