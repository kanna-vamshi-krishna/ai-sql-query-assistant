import streamlit as st
import sqlite3
from pathlib import Path
from langchain_groq import ChatGroq

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Chat with SQL Database", page_icon="🦜")
st.title("🦜 Chat with SQL Database")

# -----------------------------
# API Key
# -----------------------------
api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

if not api_key:
    st.info("Please enter your Groq API key")
    st.stop()

# -----------------------------
# Load LLM
# -----------------------------
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant"
)

# -----------------------------
# Connect database
# -----------------------------
db_path = Path(__file__).parent / "student.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# -----------------------------
# Chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me about the student database"}
    ]

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# -----------------------------
# User input
# -----------------------------
user_query = st.chat_input("Ask anything about students")

if user_query:

    st.session_state.messages.append({
        "role": "user",
        "content": user_query
    })

    st.chat_message("user").write(user_query)

    # -----------------------------
    # LLM Classification Step
    # -----------------------------
    classification_prompt = f"""
You are a classifier for a database assistant.

Database schema:
STUDENT(NAME, CLASS, SECTION, MARKS)

If the question is asking about students, names, marks, class, section,
count, total, or how many students respond ONLY with:
DATABASE

If the question is greeting or casual conversation (hi, hello, how are you),
respond ONLY with:
CHAT

Respond with exactly one word.

Question: {user_query}
"""

    query_type = llm.invoke(classification_prompt).content.strip()

    # -----------------------------
    # If DATABASE question
    # -----------------------------
    if query_type.upper() == "DATABASE":

        sql_prompt = f"""
You are a SQL assistant.

Database table:
STUDENT(NAME, CLASS, SECTION, MARKS)

Rules:
- Return ONLY a valid SQLite SQL query
- Table name is STUDENT
- Columns are NAME, CLASS, SECTION, MARKS
- If user asks count use: SELECT COUNT(*) FROM STUDENT
- Do NOT include explanations
- Do NOT include code blocks

Question: {user_query}
"""

        sql_query = llm.invoke(sql_prompt).content.strip()

        # Clean SQL
        sql_query = sql_query.replace("```sql", "")
        sql_query = sql_query.replace("```", "")
        sql_query = sql_query.replace("sql", "")
        sql_query = sql_query.strip()

        try:
            cursor.execute(sql_query)
            rows = cursor.fetchall()

            if rows:
                if len(rows[0]) == 1:
                    result = "\n".join([str(row[0]) for row in rows])
                else:
                    result = "\n".join([str(row) for row in rows])
            else:
                result = "No data found"

        except Exception as e:
            result = f"SQL Error: {e}"

    # -----------------------------
    # If normal conversation
    # -----------------------------
    else:

        chat_prompt = f"""
You are a friendly assistant.

User said: {user_query}

Respond naturally and briefly.
"""

        result = llm.invoke(chat_prompt).content.strip()

    # -----------------------------
    # Save response
    # -----------------------------
    st.session_state.messages.append({
        "role": "assistant",
        "content": result
    })

    st.chat_message("assistant").write(result)