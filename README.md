# 🧠 Text Summarization NLP App

A multi-featured **Natural Language Processing (NLP)** web application for **text summarization, auto-correction, named entity recognition (NER)**, and **language detection**, built using **Streamlit**.

This project was developed by a team of four as part of the **AI Summer Training at NTI**.

---

## 📌 Features

- **Text Summarization** using:
  - LSA (Latent Semantic Analysis)
  - LUHN
  - LexRank
  - TextRank  
  *(Users can control the number of summary sentences)*

- **Text Uploading**  
  Upload `.txt` files and directly analyze content.

- **Auto-Correction**  
  Fixes grammar and spelling mistakes using **TextBlob**.

- **Named Entity Recognition (NER)**  
  Detects people, organizations, locations using **spaCy**.

- **Language Detection**  
  Detects input language using `langdetect` for better summarization results.

---

## 👩‍💻 My Contribution

- Implemented the **Auto-Correction** module using **TextBlob**.
- Handled grammar and spelling corrections for any given input text.
- Integrated the feature into the Streamlit app for real-time correction.

---

## 🚀 Installation & Running the App

```bash
# Clone the repo
git clone https://github.com/norannali/your-repo-name.git
cd your-repo-name

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run Text_Summarization.py

