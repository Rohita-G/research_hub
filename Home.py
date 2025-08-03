import streamlit as st
from docx import Document

st.set_page_config(page_title="Rohita's Research Hub", layout="wide")

st.title("📚 Rohita's Research Hub")
st.write(
    "Welcome! This hub showcases my academic research in AI Ethics, Cloud Computing, "
    "Software Safety, and Technology History."
)

papers = {
    "AI & Intellectual Property: Art, Ethics, and Ownership": "papers/paper 1.docx",
    "Digital Divide and Global Equity in Internet Access": "papers/paper 4.docx",
    "Microsoft Azure vs. Red Hat: Comparative Cloud Platforms": "papers/CLOUD PROJECT 1.docx",
    "Therac-25 Case Study: Software Ethics & Responsibility": "papers/paper 2.docx",
    "AI in Healthcare: GHRI Case Study": "papers/IOW2.docx",   # adjust if you have this file
    "Pioneer Profile: Susan L. Graham": "papers/paper3.docx",
}

def read_docx(file_path):
    doc = Document(file_path)
    paragraphs = [para.text.strip() for para in doc.paragraphs if para.text.strip()]
    return paragraphs

paper_choice = st.selectbox("Select a paper to read", list(papers.keys()))

if paper_choice:
    st.header(paper_choice)
    try:
        paragraphs = read_docx(papers[paper_choice])
        for para in paragraphs:
            st.write(para)
    except Exception as e:
        st.error(f"Failed to load paper content: {e}")

    try:
        with open(papers[paper_choice], "rb") as file:
            st.download_button(
                label="⬇️ Download Full Paper (.docx)",
                data=file,
                file_name=paper_choice.replace(" ", "_") + ".docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
    except Exception:
        st.warning("Download unavailable.")
