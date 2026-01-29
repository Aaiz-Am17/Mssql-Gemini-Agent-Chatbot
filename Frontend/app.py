import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables (if any)
load_dotenv()

# Config: Set FastAPI endpoint URL
FASTAPI_URL = os.getenv("FASTAPI_URL", "http://localhost:8000/ask")

# ─────────────────────────────────────────────
# PAGE CONFIG & CUSTOM STYLING (minimalist, modern)
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="📊 MSSQL Gemini Agent Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown(
    """
    <style>
        .chat-message {
            padding: 0.8rem 1rem;
            border-radius: 0.8rem;
            margin-bottom: 0.6rem;
            max-width: 80%;
            line-height: 1.5;
            font-size: 0.95rem;
        }
        .user {
            background-color: #50C878;
            align-self: flex-end;
            margin-left: auto;
        }
        .bot {
            background-color: #A9A9A9;
            align-self: flex-start;
            margin-right: auto;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .stTextInput > div > div > input {
            border-radius: 0.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💬 MSSQL Gemini Agent Chatbot")
st.caption("Ask questions about attendance records, courses, or students. Read-only access and safe querying guaranteed.")

# ─────────────────────────────────────────────
# CHAT HISTORY (session state)
# ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages in a chat-style view
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "bot"
    st.markdown(
        f"<div class='chat-message {role_class}'>{msg['content']}</div>",
        unsafe_allow_html=True
    )

# ─────────────────────────────────────────────
# USER INPUT FORM (clears automatically on submit)
# ─────────────────────────────────────────────
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here...")
    submit_button = st.form_submit_button(label="Send")

# When the form is submitted and non-empty input provided, process the message.
if submit_button and user_input:
    # Save the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("Thinking..."):
        try:
            response = requests.post(FASTAPI_URL, json={"question": user_input}, timeout=120)
            result = response.json()
            if result.get("success"):
                # The result may be plain text or a dict with a "text" key
                answer_text = (
                    result["answer"].get("text", str(result["answer"]))
                    if isinstance(result["answer"], dict)
                    else str(result["answer"])
                )
            else:
                answer_text = f"⚠️ Error: {result.get('error', 'Unknown error')}"
        except Exception as e:
            answer_text = f"❌ Connection error: {str(e)}"
    
    # Save the assistant's response
    st.session_state.messages.append({"role": "assistant", "content": answer_text})
    st.rerun()  # Rerun the app to display the new messages
