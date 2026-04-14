import streamlit as st
from app.rag_pipeline import retrieve_context


st.title("AI-Powered Credit Risk Explanation Assistant")

query = st.text_input("Ask a question")

if st.button("Run"):
    if query:
        context = retrieve_context(query)

        st.subheader(" Retrieved Context")
        st.write(context)

        # Simple response (for now)
        response = f"Based on data: {context}"

        st.subheader(" AI Explanation")
        st.write(response)