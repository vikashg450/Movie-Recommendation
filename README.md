
<div align="center">

# 🎬 Movie Recommendation System

### AI-Powered Movie Discovery Platform

<p align="center">
  <a href="https://movie-recommendation-djmft2wgujs97bbrzsma7q.streamlit.app">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Streamlit_App-FFB000?style=for-the-badge&logo=streamlit&logoColor=white"/>
  </a>

  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>

  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

  <img src="https://img.shields.io/badge/ML-TF_IDF_Engine-6A5ACD?style=for-the-badge"/>
</p>

---

<img width="958" height="815" alt="image" src="https://github.com/user-attachments/assets/6a9a0818-fc15-4e63-babb-25d97565fe5a" />


</div>

---

# ✨ Overview

An intelligent **Movie Recommendation System** built with:

- ⚡ **FastAPI** for high-performance backend APIs  
- 🎨 **Streamlit** for beautiful interactive UI  
- 🧠 **TF-IDF + Cosine Similarity** for smart recommendations  
- 🌍 **TMDB API** for live movie data, posters, and ratings  

This project delivers personalized movie recommendations instantly with a modern Netflix-style interface.

---

# 🚀 Live Application

<div align="center">



</div>

---

# 🎯 Core Features

<table>
<tr>
<td width="50%">

## 🔥 Movie Discovery

- Trending Movies
- Popular Movies
- Top Rated Collection
- Upcoming Releases

</td>
<td width="50%">

## 🧠 AI Recommendations

- TF-IDF Recommendation Engine
- Cosine Similarity Matching
- Metadata-based Suggestions
- Fast Search System

</td>
</tr>
</table>

---

# 📸 Application Preview

## 🏠 Homepage

<img src="./assets/movie-rec-preview.png" width="100%"/>

---

# ⚙️ Tech Stack

<div align="center">

| Technology | Purpose |
|---|---|
| 🐍 Python | Core Programming |
| ⚡ FastAPI | Backend API |
| 🎨 Streamlit | Frontend UI |
| 🧠 scikit-learn | Machine Learning |
| 📊 Pandas | Data Processing |
| 🌍 TMDB API | Live Movie Data |
| 🚀 httpx | Async Requests |

</div>

---

# 🧠 Recommendation Engine

The recommendation engine works using:

```text
Movie Metadata
       ↓
TF-IDF Vectorization
       ↓
Cosine Similarity
       ↓
Top Similar Movies
```

### Recommendation Flow

1️⃣ User selects a movie  
2️⃣ TF-IDF converts metadata into vectors  
3️⃣ Cosine similarity finds related movies  
4️⃣ TMDB API fetches posters & ratings  
5️⃣ Results displayed instantly  

---

# 📂 Project Structure

```bash
movie-recommendation-system/
│
├── app.py
├── main.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── .env
├── assets/
│   └── movie-rec-preview.png
└── README.md
```

---

# 🚀 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Add TMDB API Key

Create `.env` file:

```env
TMDB_API_KEY=your_tmdb_api_key
```

Get your API key here:

🔗 https://developer.themoviedb.org

---

# ▶️ Run Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```bash
http://localhost:8000
```

---

# ▶️ Run Frontend

```bash
API_BASE="http://localhost:8000" streamlit run app.py
```

Frontend URL:

```bash
http://localhost:8501
```

---

# 🏗️ System Architecture

```text
          ┌──────────────────┐
          │   Streamlit UI   │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │  FastAPI Backend │
          └────────┬─────────┘
                   │
     ┌─────────────┴─────────────┐
     ▼                           ▼
┌──────────────┐         ┌────────────────┐
│ TF-IDF Model │         │   TMDB API     │
└──────────────┘         └────────────────┘
```



# 🤝 Contributing

Contributions are welcome!

```bash
Fork → Clone → Create Branch → Commit → Push → Pull Request
```




<div align="center">

# ⭐ If you like this project, give it a Star on GitHub ⭐

</div>
````
