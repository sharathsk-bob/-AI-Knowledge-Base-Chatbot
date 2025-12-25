import streamlit as st
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
from utils import load_pdf, create_vector_store
from dotenv import load_dotenv
load_dotenv()
import os
st.set_page_config(page_title="AI RAG Chatbot", layout="wide")

st.title("📄 AI Knowledge Base Chatbot")
st.write("Ask questions from your documents using AI")
api_key = os.getenv("GROQ_API_KEY")
# Sidebar
with st.sidebar:
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with st.spinner("Processing document..."):
        text = load_pdf(uploaded_file)
        vector_store = create_vector_store(text)

        llm = ChatGroq(
            groq_api_key=api_key,
            model_name="llama-3.1-8b-instant"  # ✅ current supported model
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vector_store.as_retriever(),
            chain_type="stuff"
        )

    st.success("Document processed successfully!")

    query = st.text_input("Ask a question")

    if query:
        with st.spinner("Thinking..."):
            response = qa_chain.run(query)

        st.markdown("### 🤖 Answer")
        st.write(response)

else:
    st.info("Upload a PDF to begin")
