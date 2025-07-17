#SecureInbox


**SecureInbox** is a cutting-edge AI-powered web application that detects whether a message (SMS or email text) is spam or not. Built with Python and Streamlit, this solution leverages natural language processing (NLP) and machine learning (ML) to offer a sleek, fast, and user-friendly experience for spam detection.

---

## 🚀 Why This Project Is Important

In the digital age, spam communication isn't just an annoyance—it's a security threat. From phishing scams to malicious payloads embedded in messages, spam can cause significant harm to individuals and organizations. Existing spam filters are either embedded in systems or too complex for the average user to access. **SpamShield AI** offers a simple, elegant, and effective way for anyone to scan a message for potential spam using state-of-the-art AI—all from their browser.

✅ **Protects users from phishing attacks**  
✅ **Educates about message safety**  
✅ **Useful for both personal and corporate users**  
✅ **Helps improve awareness of social engineering risks**

---

## 🧠 Features

- 🔍 **Instant Spam Detection** — Classifies messages as "Spam" or "Not Spam" in real-time.
- 🎨 **Apple-Inspired UI** — Clean, minimalistic, and responsive interface.
- 🧬 **NLP-Powered** — Uses tokenization, stemming, stopword removal, and TF-IDF vectorization.
- 📦 **ML Model Integration** — Trained and optimized using historical spam/ham datasets.
- 🌐 **Deployed with Streamlit** — Easily accessible via any browser.

---

## 🛠️ Tech Stack

| Layer              | Tools Used                    |
|-------------------|-------------------------------|
| **Frontend**       | Streamlit (custom CSS styling)|
| **Backend**        | Python, Pickle, NLTK, Scikit-learn |
| **ML Model**       | TF-IDF Vectorizer + Classifier |
| **Preprocessing**  | Tokenization, Stemming, Stopword Removal |
| **UI Aesthetics**  | Google Fonts + Custom HTML/CSS |

---

## 🧪 How It Works

1. **Text Preprocessing**  
   The input message is:
   - Lowercased
   - Tokenized
   - Stripped of stopwords and punctuation
   - Stemmed using PorterStemmer

2. **Vectorization**  
   The cleaned message is converted into a numeric feature vector using TF-IDF.

3. **Prediction**  
   The trained model (loaded from `model.pkl`) classifies the message as spam (1) or not spam (0).

4. **Result Display**  
   Stylish and intuitive result cards show if the input is spam or ham.

---

