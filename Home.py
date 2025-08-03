import streamlit as st
from docx import Document

st.set_page_config(page_title="Rohita's Research Hub", layout="wide")

st.title("📚 Rohita's Research Hub")
st.write(
    "Welcome! This hub showcases my academic research in AI Ethics, Cloud Computing, "
    "Software Safety, and Technology History. Select a paper below to read it."
)

# ✅ Map paper titles to filenames (since you put all .docx in root)
papers = {
    "AI & Intellectual Property: Art, Ethics, and Ownership": "paper 1.docx",
    "Therac-25 Case Study: Software Ethics & Responsibility": "paper 2.docx",
    "Pioneer Profile: Susan L. Graham": "paper 3.docx",
    "Digital Divide and Global Equity in Internet Access": "paper 4.docx",
    "Microsoft Azure vs. Red Hat: Comparative Cloud Platforms": "CLOUD PROJECT 1.docx",
    "Amazon Privacy Issues": "IOW2.docx",
}

# ✅ Helper function to read DOCX
def read_docx(file_path):
    doc = Document(file_path)
    return [para.text.strip() for para in doc.paragraphs if para.text.strip()]

# ✅ UI Dropdown
paper_choice = st.selectbox("Select a paper to read", list(papers.keys()))

# ✅ Display the chosen paper
if paper_choice:
    st.header(paper_choice)
    file_path = papers[paper_choice]

    try:
        paragraphs = read_docx(file_path)
        for para in paragraphs:
            st.write(para)
    except Exception as e:
        st.error(f"❌ Failed to load paper: {e}")

    # ✅ Download button
    try:
        with open(file_path, "rb") as file:
            st.download_button(
                label="⬇️ Download Full Paper (.docx)",
                data=file,
                file_name=file_path,  # keep the original filename
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
    except FileNotFoundError:
        st.warning("⚠️ Download unavailable: File not found.")
