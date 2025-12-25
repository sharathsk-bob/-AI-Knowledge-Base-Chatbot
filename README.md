📄 AI Knowledge Base Chatbot

A RAG-based Intelligent Document Question Answering System using LangChain, FAISS, Streamlit & Groq LLaMA

📌 Overview

AI Knowledge Base Chatbot is an intelligent document question-answering system that allows users to upload PDFs and interact with them using natural language.
It uses RAG (Retrieval Augmented Generation) + Vector Search to extract context from uploaded files and generate answers that are grounded in document content, not general AI guesses.

This project is perfect for:

✔ Students summarizing textbooks
✔ Teams managing internal documentation
✔ Research papers & legal contract Q&A
✔ Company knowledge base automation
✔ Helpdesk and customer support systems

🚀 Features
Feature	Description
Upload PDF documents	Index and analyze files instantly
Semantic Vector Search	Uses embeddings to find relevant text
RAG-based response generation	Answers using actual document context
Groq LLaMA integration	Super-fast free inference
Streamlit UI Frontend	Simple & modern interface
🔥 ChatGPT-like copy answer button	Copies responses instantly
🧠 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
AI Model	Groq LLaMA
Embeddings	SentenceTransformers
Vector DB	FAISS
RAG Framework	LangChain
PDF Processing	PyPDF
📁 Project Structure
AI-Knowledge-Base-Chatbot/
│── app.py
│── utils.py
│── requirements.txt
│── business_cases.txt (optional)
│── .env (ignored)
│── README.md

🔧 Installation
git clone 
cd AI-Knowledge-Base-Chatbot
pip install -r requirements.txt


Add your Groq API Key to .env:

GROQ_API_KEY="your_key_here"

▶ Run the Application
streamlit run app.py
