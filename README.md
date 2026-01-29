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
