# ai-sql-query-assistant


This project is a **Generative AI powered SQL chatbot** that allows users to interact with a database using **natural language questions**.  
The system converts user queries into SQL statements using a **Large Language Model (LLM)** and retrieves results from the database.

---

## Project Overview

The chatbot enables users to ask questions such as:

- How many students are there?
- Show all student names
- Students in section A
- Students with marks greater than 80

The system automatically converts these natural language queries into SQL queries and fetches results from the database.

---

## Features

- Natural Language to SQL conversion
- Chat-based interface using Streamlit
- LLM-based intent classification (Database vs Normal Chat)
- Executes generated SQL queries on a SQLite database
- Displays results interactively
- Maintains chat history

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Groq LLM (Llama 3.1)
- SQLite
- Prompt Engineering

---

## Project Architecture

User Question  
↓  
LLM Intent Classifier (DATABASE or CHAT)  
↓  
SQL Generation using LLM  
↓  
SQLite Database Execution  
↓  
Streamlit Chat Interface  

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/genai-sql-chatbot.git
