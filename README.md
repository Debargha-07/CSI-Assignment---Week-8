# CSI-Assignment---Week-8

# 🤖 Loan Document Q&A Chatbot

An intelligent chatbot that answers questions about loan applications using both retrieval and logic-based reasoning. This system combines natural language understanding with simple data reasoning — useful for analytics, documentation, or even automating internal queries.

---

## 📌 Project Overview

This chatbot allows users to ask questions about loan applicant data such as loan amounts, approval rates, applicant income, education levels, and more. It retrieves relevant information and applies logic-based rules or fallback generation to respond naturally.

---

## 🚀 Features

- 📄 Converts tabular CSV loan data into readable text chunks
- 🔍 Retrieves relevant context using semantic search (FAISS + embeddings)
- 🧠 Answers using rules (for known patterns) or fallback generation
- 🧹 Filters nonsense questions using spellchecking
- 🧪 Interactive console chatbot interface

---

## 📂 Project Structure

```
Week 8/
│
├── app.py # Main chatbot script
├── retriever.py # Retrieves top matching documents
├── generator.py # Generates answers using logic
├── utils.py # Utilities for loading & formatting data
├── prepare_docs.py # Pre-processes and embeds CSV data
│
├── data/
│ └── training.csv # Raw loan data file
│
├── docs/
│ └── embedded_docs.pkl # Serialized documents and embeddings
│
├── requirements.txt # Required Python packages
└── README.md # This file
```


---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/loan-chatbot.git
cd loan-chatbot
```
### 2️⃣ Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Prepare the document embeddings
Make sure **training.csv** is in the data/ folder, then run:
```
python prepare_docs.py
```
### 5️⃣ Start the chatbot
```
python app.py
```
---
## 💬 How It Works
1. **Preprocessing**: Converts rows from training.csv into readable text ("documents") and generates sentence embeddings using SentenceTransformers.

2. **Retrieval**: Uses FAISS to find the most relevant documents based on the user’s query.

3. **Answering**:

  - If the question matches a known pattern (e.g., average, count, approval), it uses rule-based logic with Pandas.

  - Otherwise, it falls back to a generative model (like FLAN-T5) for natural answers.

4. **Input validation**: Uses a spell checker (pyenchant) to reject nonsense queries before processing.
---

## 🧪 Sample Questions
Try these:

- ❓ What is the average loan amount overall?

- ❓ How many married applicants are there?

- ❓ What is the loan approval rate?

- ❓ How many self-employed applicants exist?

- ❓ What is the average loan term?

- ❓ How many graduate applicants are in the dataset?
---

## ⚙️ Technologies Used
- `Python 3.8+`

- `pandas, numpy` — data handling

- `sentence-transformers, faiss-cpu` — semantic document retrieval

- `transformers, torch` — generative model fallback

- `pyenchant` — gibberish filtering

- `scikit-learn` — optional preprocessing
---

## 👨‍💻 Author
### Debargha Karmakar
This chatbot was developed as a part of Week 8 assignment at Celebal Technologies, combining document retrieval with generative AI for natural language question answering.

---
