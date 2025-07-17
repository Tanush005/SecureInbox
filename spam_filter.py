
import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import base64

nltk.download('stopwords')
nltk.download('punkt')

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    y = [ps.stem(i) for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    return " ".join(y)


# Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Page settings
st.set_page_config(page_title="SpamShield AI", layout="centered")


# Function to convert image to base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


# Apple-inspired design with visible background
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;500;700&display=swap');

    /* Background with minimal overlay */
    .stApp {{
        background: 
            linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)),
            url("data:image/png;base64,{get_base64_of_image('background.png')}") center/cover fixed;
    }}

    /* Main content container */
    .main-container {{
        background-color: rgba(20, 20, 20, 0.85);
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        border-radius: 20px;
        padding: 2rem;
        max-width: 620px;
        margin: 3rem auto;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}

    /* Text styling */
    h1 {{
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 42px;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
        text-align: center;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    }}

    h3 {{
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 21px;
        font-weight: 400;
        color: #bbbbbb;
        margin-bottom: 32px;
        text-align: center;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
    }}

    /* Text area */
    .stTextArea textarea {{
        background-color: rgba(30, 30, 30, 0.8);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px;
        font-size: 17px;
        min-height: 120px;
    }}

    .stTextArea label {{
        font-size: 17px;
        color: #bbbbbb;
    }}

    /* Button */
    .stButton button {{
        width: 100%;
        background: linear-gradient(to right, #0071e3, #00a1ff);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 17px;
        font-weight: 500;
        transition: all 0.3s ease;
    }}

    .stButton button:hover {{
        background: linear-gradient(to right, #0062c4, #008ceb);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0, 97, 255, 0.3);
    }}

    /* Results */
    .result-spam {{
        background-color: rgba(255, 69, 58, 0.9);
        color: white;
        padding: 16px;
        border-radius: 12px;
        font-size: 20px;
        font-weight: 500;
        text-align: center;
        margin-top: 24px;
        border: 1px solid rgba(255, 69, 58, 0.3);
        box-shadow: 0 4px 12px rgba(255, 69, 58, 0.2);
    }}

    .result-ham {{
        background-color: rgba(48, 209, 88, 0.9);
        color: white;
        padding: 16px;
        border-radius: 12px;
        font-size: 20px;
        font-weight: 500;
        text-align: center;
        margin-top: 24px;
        border: 1px solid rgba(48, 209, 88, 0.3);
        box-shadow: 0 4px 12px rgba(48, 209, 88, 0.2);
    }}

    /* Remove Streamlit branding */
    footer {{visibility: hidden;}}
    .st-emotion-cache-cio0dv {{padding: 0;}}
    </style>
""", unsafe_allow_html=True)

# App UI structure
st.markdown("""
    <div class="main-container">
        <h1>SpamShield AI</h1>
        <h3>Your personal AI-powered Spam Email & SMS detector</h3>
""", unsafe_allow_html=True)

input_sms = st.text_area("Paste your message here to check if it's spam:")

if st.button("Predict"):
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]

    if result == 1:
        st.markdown('<div class="result-spam">🚫 This is SPAM</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-ham">✅ This is NOT Spam</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)