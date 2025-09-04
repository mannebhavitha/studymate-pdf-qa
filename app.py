import streamlit as st
from pdf_utils import extract_text_from_pdf
from qa_utils import ask_question

st.title("📘 StudyMate: PDF Q&A")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    st.success("✅ PDF uploaded successfully!")

    # Extract text
    pdf_text = extract_text_from_pdf(uploaded_file)

    question = st.text_input("Ask a question about the PDF:")

    if st.button("Get Answer"):
        if question.strip():
            with st.spinner("Thinking..."):
                answer = ask_question(pdf_text, question)
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question.")
