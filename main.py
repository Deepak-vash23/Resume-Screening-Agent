import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Candidate Selection Tool")
st.subheader("NLP Based Resume Screening")

st.caption(
    "Aim of this project is to check whether a candidate is qualified "
    "for a role based on education, experience, and skills."
)

uploadedJD = st.file_uploader("Upload Job Description", type="pdf")
uploadedResume = st.file_uploader("Upload Resume", type="pdf")

click = st.button("Process")

# SAFE initialization
job_description = None
resume = None

# Extract JD
if uploadedJD is not None:
    with pdfplumber.open(uploadedJD) as pdf:
        job_description = pdf.pages[0].extract_text()

# Extract Resume
if uploadedResume is not None:
    with pdfplumber.open(uploadedResume) as pdf:
        resume = pdf.pages[0].extract_text()

# Logic
def getResult(JD_txt, resume_txt):
    content = [JD_txt, resume_txt]

    cv = CountVectorizer()
    matrix = cv.fit_transform(content)

    similarity_matrix = cosine_similarity(matrix)
    match = similarity_matrix[0][1] * 100

    return match

# Button action
if click:
    if job_description is None or resume is None:
        st.error("Please upload both Job Description and Resume.")
    else:
        match = getResult(job_description, resume)
        match = round(match, 2)
        st.success(f"Match Percentage: {match}%")

import os

port = int(os.environ.get("PORT", 8501))
st.set_page_config(layout="wide")
