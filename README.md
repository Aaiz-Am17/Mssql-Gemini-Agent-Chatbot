# 🤖 MSSQL Gemini Agent Chatbot
### 🎯 Natural Language Analytics over SQL using Agentic AI (LangGraph + Gemini)

[![GitHub stars](https://img.shields.io/github/stars/Aaiz-Am17/Mssql-Gemini-Agent-Chatbot?style=social)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit)
![LangChain](https://img.shields.io/badge/Framework-LangChain-blue)
![LangGraph](https://img.shields.io/badge/Agent-LangGraph-purple)
![Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-orange?logo=google)

---

🎯 **Query complex SQL databases using plain English — safely and intelligently.**  
📊 This project demonstrates how **LLM agents** can reason over structured data while enforcing **strict read-only access**.

---

## 💡 Project Overview & Motivation

Querying relational databases often requires deep SQL knowledge and familiarity with schema details.  
This project explores how **agentic AI systems** can bridge that gap by allowing users to ask **natural language questions** and receive accurate, human-readable answers — without exposing raw SQL or sensitive data.

The **MSSQL Gemini Agent Chatbot** is a production-style AI system that:
- Translates natural language queries into structured reasoning steps
- Uses an **LLM agent (LangGraph ReAct)** to decide how to query data
- Enforces **read-only SQL execution** for security
- Returns concise, user-friendly answers via a chat interface

> ⚠️ **Client Safety Note**  
> Core backend logic, system prompts, SQL templates, and database schema are intentionally **not公开** due to client confidentiality and IP constraints.

---

## ✨ Key Features

🧠 **Agentic Reasoning with LangGraph**  
Uses a ReAct-style LLM agent to reason about user intent before querying data.

📊 **Natural Language → SQL Analytics**  
Users ask questions in plain English — no SQL knowledge required.

🔐 **Strict Read-Only Enforcement**  
All mutation queries (INSERT, UPDATE, DELETE, DROP) are blocked.

⚡ **FastAPI Backend**  
Clean, modular API layer designed for production use.

🖥️ **Streamlit Chat Interface**  
Simple, modern UI for interactive data exploration.

🔁 **Multi-LLM Ready Architecture**  
Designed to work with Gemini, GPT, or local LLMs (e.g., Ollama).

---

## 🚀 How It Works

1. User asks a question via the Streamlit chat UI  
2. FastAPI backend receives the query  
3. LangGraph agent interprets intent and plans a safe query  
4. Read-only SQL tools fetch relevant data  
5. LLM generates a clean, natural-language response  

---

## 🏗️ System Architecture

```text
       [ User (Streamlit UI) ]
                  │
                  ▼
       [ FastAPI Backend Layer ]
                  │
                  ▼
     [ LangGraph ReAct Agent (LLM) ]
                  │
                  ▼
       [ Read-Only SQL Toolkit ]
                  │
                  ▼
    [ Client MSSQL Database (Private) ]
```

---

## 📁 Project Structure

```text
mssql-gemini-agent-chatbot/
│
├── backend/
│   ├── main.py            # Sanitized FastAPI backend
│   ├── agent_stub.py      # Agent structure (logic omitted)
│   └── requirements.txt
│
├── frontend/
│   ├── app.py             # Streamlit chat UI
│   └── requirements.txt
│
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```



---


## 🔒 Confidentiality & IP Handling


To respect client agreements, the following are **intentionally excluded**:
- System prompts
- Database schema & table names
- SQL query templates
- Business logic & constraints


✅ What *is* shown:
- Overall architecture
- API design
- Agent structure
- Security practices
- Production-ready project layout


---


## 🛠️ Setup & Installation (Interface Demo)


### 1. Clone the Repository
```bash
git clone https://github.com/Aaiz-Am17/mssql-gemini-agent-chatbot.git
cd mssql-gemini-agent-chatbot
```
2. Backend
```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
3. Frontend
```
cd frontend
pip install -r requirements.txt
streamlit run app.py
```
### 🧪 Example Queries (Demonstration)
* "Show attendance for a student"
* "Average attendance of a batch"
* "Generate a monthly attendance report"
* "Overall attendance for a subject"

> _Note: Exact results depend on private backend logic._

### 🎯 Why This Project Matters
* 🚀 **Real-world Design:** Demonstrates production-grade LLM agent architecture.
* 🔐 **Secure Integration:** Shows safe, sanitized LLM + SQL integration.
* 🛡️ **Security-First:** Highlights strong security-first thinking and engineering.
* 🏗️ **Production Ready:** Mirrors how professional AI assistants are built.
* 💼 **Professionalism:** Reflects professional handling of client IP and data.

  
🙋‍♂️ Contributing

Contributions are welcome!
Fork the repo → create a branch → submit a PR 🚀

📜 License

This project is licensed under the MIT License.

👥 Credits

Developed by Aaiz Mohsin (BS Artificial Intelligence, GIKI)
Built as part of professional AI/LLM engineering work and experimentation with agentic systems.

⭐ If this project helped you, consider giving it a star!
