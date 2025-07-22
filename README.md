# 🚨 SpamShield AI – Real-Time Spam Detection in <10ms

**SpamShield AI** is a production-grade, ultra-fast spam detection system for SMS and email messages. Built with a focus on *performance*, *scalability*, and *software engineering best practices*, this application delivers **real-time predictions in under 10 milliseconds** and is fully deployable on the cloud.

---

## 📸 Demo Preview

> 📩 Paste any SMS or email message – get a real-time classification and latency breakdown.

<img width="2189" height="1411" alt="Screenshot 2025-07-22 212111" src="https://github.com/user-attachments/assets/e569ab47-178d-4959-8451-4ed300d7eaf2" />
<img width="2467" height="1361" alt="Screenshot 2025-07-22 212050" src="https://github.com/user-attachments/assets/40532637-a0c7-426d-b494-b4dfe043d75c" />



---

## 🎯 Why SpamShield AI?

Modern communication platforms are flooded with spam — from phishing attempts to promotional overloads. SpamShield AI was engineered as a complete SDE project to:

- Showcase real-time ML inference at production scale
- Build a fault-tolerant, full-stack system with robust UX
- Push the limits of latency, modularity, and reliability

---

## ⚙️ Key Features

✅ **Blazing-Fast Inference:**  
Predictions delivered in under **10ms** using optimized regex tokenization + TF-IDF vectorization.

🧠 **95%+ Accuracy:**  
Trained on 5K+ labeled SMS samples using a lightweight Naive Bayes model.

🧹 **Custom Preprocessing Pipeline:**  
Regex-based input cleaning, token filtering, and stemming — no runtime downloads.

🧪 **Live Latency Tracker:**  
See real-time latency for every classification.

🖥️ **Streamlit Frontend:**  
Fully interactive UI with built-in input validation and responsive performance.

☁️ **Cloud-Optimized:**  
Cached model/vectorizer, lightweight footprint, and instant readiness on Streamlit Cloud or other cloud platforms.

---

## 🧠 How It Works

1. 📨 **User Input** – Paste any SMS or email text  
2. 🔍 **Preprocessing** – Regex-based cleaning and tokenization  
3. 📊 **Vectorization** – TF-IDF transformation  
4. 🤖 **Prediction** – Lightweight Naive Bayes model (`model.pkl`) returns spam/ham  
5. 🕒 **Latency Calculated** – Inference time measured and displayed instantly

---

## 🧪 Example Predictions

| Message                                    | Prediction | Latency |
|-------------------------------------------|------------|---------|
| "You won a free iPhone! Click to claim!"  | 🛑 Spam     | 9.1 ms  |
| "Meeting moved to 3 PM. Bring your laptop"| ✅ Not Spam | 10.2 ms |

---


🚀 Engineering Highlights
🔧 System Design
Modular architecture with clear separation between preprocessing, inference, and frontend logic.

🛡️ Fault Tolerance
All inputs are sanitized, validated, and handled gracefully to prevent crashes and edge-case failures.

⚡ Performance Optimizations
Model and vectorizer are preloaded in memory, reducing I/O time. Minimal dependencies and optimized TF-IDF logic ensure sub-10ms latency.

🧰 Lightweight Deployment
No nltk.download() or heavy runtime loads. Built to boot instantly on Streamlit Cloud and portable enough for Docker-based deployment.



---

🛠️ Built With

Python 3.9+
Streamlit
scikit-learn
NLTK (pre-downloaded assets, no runtime load)
Regex + TF-IDF
Pickle for model serialization

---
✨ Future Enhancements
🌐 Add support for multilingual spam detection

📬 Integrate with email APIs like Gmail for real-time inbox filtering

🐳 Dockerize for portable container deployment

📊 Add monitoring/logging with Prometheus and Grafana for real-time metrics
