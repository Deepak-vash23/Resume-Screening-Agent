# AI Resume Screening Tool

A simple AI-powered Resume Screening Tool built using Python and Streamlit.  
This application compares a Job Description and a Resume using NLP techniques and calculates a similarity score (match percentage).

---

## 🚀 Features

- Upload Job Description (PDF)
- Upload Resume (PDF)
- NLP-based similarity calculation
- Match percentage scoring
- Simple and clean single-page UI
- Automatic validation for missing or invalid files

---

## 🧠 How It Works

1. Extracts text from both PDFs.
2. Converts text into numerical vectors using NLP (CountVectorizer / TF-IDF).
3. Computes cosine similarity between Job Description and Resume.
4. Displays a match percentage score.

Match Interpretation Example:
- 70–100% → Strong Match
- 40–69% → Partial Match
- Below 40% → Low Match

---

## 🛠️ Tech Stack

- Python 3.10+
- Streamlit
- pdfplumber
- scikit-learn

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd <your-project-folder>
