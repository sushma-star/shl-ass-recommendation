# 🚀 SHL RAG Recommendation System

An AI-powered assessment recommendation system that suggests relevant SHL assessments based on a given Job Description using **Retrieval-Augmented Generation (RAG)** and semantic similarity search.

---

## 📌 Overview

This project helps recruiters and hiring managers automatically find the most relevant SHL assessments based on a job description.

Instead of manually searching through hundreds of assessments, this system:

- Accepts a Job Description
- Converts it into semantic embeddings
- Compares it with SHL assessment embeddings
- Returns the top matching assessments ranked by similarity

---

## 🧠 How It Works

1. Load SHL assessment data from `products.json`
2. Extract textual fields (name + description)
3. Generate embeddings using Sentence Transformers
4. Convert user query into embedding
5. Compute cosine similarity
6. Rank top matches
7. Return structured JSON response

---
## 🤖 Model Used

### `all-MiniLM-L6-v2`

This model is used inside the RAG engine to generate semantic embeddings.

It is loaded using:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
```

### Why This Model?

- Lightweight and fast
- High-quality semantic embeddings
- Optimized for similarity search
- Suitable for production

The model converts both:

- SHL assessment descriptions
- User Job Description

into dense vector embeddings for similarity comparison.

---

## ⚙️ Technology Stack

| Layer | Technology |
|--------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| NLP Model | SentenceTransformers |
| Model Used | all-MiniLM-L6-v2 |
| Similarity Search | Cosine Similarity |
| Deployment | Render / Streamlit Cloud |

---
# ▶️ How To Run The Application (Local Setup)

## 1️⃣ Clone Repository

```
git clone https://github.com/sushma-star/shl-rag-recommendation.git
cd shl-rag-recommendation
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows:
```
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install fastapi uvicorn streamlit sentence-transformers scikit-learn numpy
```

OR

```
pip install -r requirements.txt
```

---

## 🚀 Run Backend (FastAPI)

```
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Health check:

```
http://127.0.0.1:8000/health
```

---

## 🎨 Run Frontend (Streamlit)

Open new terminal:

```
streamlit run app.py
```

Frontend runs at:

```
http://localhost:8501
```

---

## 📡 API Endpoints

### Health Check

```
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

### Recommendation Endpoint

```
POST /recommend
```

### Request Body

```json
{
  "query": "Python Developer with REST API experience"
}
```

### Response Format

```json
{
  "recommended_assessments": [
    {
      "url": "https://www.shl.com/products/product-catalog/view/interpersonal-communications/",
      "adaptive_support": "Yes",
      "description": "Measures Python skills",
      "duration": 60,
      "remote_support": "Yes",
      "test_type": ["Technical"]
    }
  ]
}
```

---

## 🎨 Frontend (Streamlit)

The Streamlit UI:

- Accepts job description input
- Calls FastAPI backend
- Displays recommended assessments
- Shows URL and test type
- Handles empty input & API errors

### Run Locally

```
streamlit run app.py
```

---

## 📊 Evaluation

Evaluation results are stored in:

```
evaluation/sushma_akula.csv
```

### Metrics Considered

- Relevance Accuracy
- Semantic Match Quality
- Top-K Recommendation Precision
- Response Time

---

## ⚡ Performance

- Precomputed embeddings for faster search
- Lightweight transformer model
- In-memory vector similarity
- Low response latency
- Suitable for small to medium datasets

---

## 🌍 Deployment Guide

### Backend Deployment (Render)

1. Push project to GitHub
2. Create new Web Service on Render
3. Use start command:

```
uvicorn backend.main:app --host 0.0.0.0 --port 10000
```

4. Deploy

---

### Frontend Deployment (Streamlit Cloud)

1. Connect GitHub repository
2. Select `app.py`
3. Deploy

---

## 🔐 Future Improvements

- Use FAISS for large-scale vector search
- Add vector database
- Add authentication
- Add ranking fine-tuning
- Add caching layer
- Add confidence score display

---

## 🧪 Example Use Case

### Input

```
Looking for a backend developer with Python, REST APIs, and problem-solving skills.
```

### Output

- Python Programming Test
- REST API Assessment
- Cognitive Ability Test

---
## 🎥 Demo  output image 

https://github.com/sushma-star/shl-ass-recommendation/issues/1

## 🎥 Demo Video

[![Watch Demo](https://img.youtube.com/vi/40V-SYnpBt0/0.jpg)](https://youtu.be/40V-SYnpBt0)

---


## 👩‍💻 Author

**Sushma Akula**

GitHub:  
https://github.com/sushma-star

---

## 🎯 Project Highlights

✔ NLP-based semantic search  
✔ RAG system implementation  
✔ FastAPI backend  
✔ Streamlit frontend  
✔ Production-ready structure  
✔ Deployment-ready  

---

## 📜 License

This project is developed for educational and evaluation purposes.
