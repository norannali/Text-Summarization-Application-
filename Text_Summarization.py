import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from langdetect import detect, LangDetectException
from textblob import TextBlob
import spacy

# Load Spacy model for Named Entity Recognition (NER)
nlp = spacy.load('en_core_web_sm')

st.title('Text Summarization Application')

# Text Upload Feature
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.text_area("File Content", text)
else:
    text = st.text_area("Please, Enter the text to Summarize...", height=150)

# Summarizer Selection
summarizer_type = st.selectbox("Choose Summarizer Type", ('LSA', 'LUHN', 'LexRank', 'TextRank'))

# Sentence Count Slider
sentence_count = st.slider("Number Of Sentences", 1, 20, 5)

# Summarization Function
def Summarize_Text(text, summarizer_type='lsa', sentence_count=5, language="english"):
    try:
        # Set tokenization language dynamically
        parser = PlaintextParser.from_string(text, Tokenizer(language))
        
        if summarizer_type == 'LSA':
            summarizer = LsaSummarizer()
        elif summarizer_type == 'LUHN':
            summarizer = LuhnSummarizer()
        elif summarizer_type == 'LexRank':
            summarizer = LexRankSummarizer()
        elif summarizer_type == 'TextRank':
            summarizer = TextRankSummarizer()
        
        summary = summarizer(parser.document, sentence_count)
        return " ".join(str(sentence) for sentence in summary) # join sentences together
    except Exception as e:
        return f"Error in summarization: {str(e)}"

# Summarize Text
if st.button('Summarize Text'):
    if text:
        # Detect language for tokenization
        try:
            detected_language = detect(text)
            st.write(f"Detected language: {detected_language}")
        except LangDetectException:
            detected_language = "english"  # fallback to English if detection fails
        
        # Summarize the text based on detected language
        summary = Summarize_Text(text, summarizer_type, sentence_count, detected_language)
        st.subheader('Summary')
        st.write(summary)
    else:
        st.write('Please write a text to summarize.')

# Language Detection Button
def detect_language(text):
    try:
        language = detect(text)
        return language
    except LangDetectException:
        return "Could not detect language"

if st.button('Detect Language'):
    if text:
        detected_language = detect_language(text)
        st.write(f"Detected language: {detected_language}")
    else:
        st.write('Please enter text to detect language')

# Text Auto-Correction Feature
def auto_correct_text(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

if st.button('Auto-Correct Text'):
    if text:
        corrected_text = auto_correct_text(text)
        st.subheader('Corrected Text')
        st.write(corrected_text)
    else:
        st.write('Please write or upload text to correct.')

# Named Entity Recognition (NER) Feature
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

if st.button('Named Entity Recognition'):
    if text:
        entities = extract_entities(text)
        st.subheader('Named Entities')
        for entity, label in entities:
            st.write(f"{entity}: {label}")
    else:
        st.write('Please write or upload text for NER.')
