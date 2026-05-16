````markdown
# 🎬 Movie Recommendation System

<p align="center">
  <img src="https://movie-recommendation-djmft2wgujs97bbrzsma7q.streamlit.app/" width="100%" alt="Movie Recommendation Banner"/>
</p>

<p align="center">
  <a href="https://movie-recommendation-djmft2wgujs97bbrzsma7q.streamlit.app/?view=details&id=1669050">
    <img src="https://img.shields.io/badge/Live-Demo-yellow?style=for-the-badge&logo=streamlit">
  </a>

  <a href="https://github.com/your-username/movie-recommendation-system">
    <img src="https://img.shields.io/github/stars/your-username/movie-recommendation-system?style=for-the-badge">
  </a>

  <a href="https://github.com/your-username/movie-recommendation-system/network/members">
    <img src="https://img.shields.io/github/forks/your-username/movie-recommendation-system?style=for-the-badge">
  </a>
</p>

---

# 🚀 Live Demo

## 🌐 Streamlit App

🔗 https://movie-recommendation-djmft2wgujs97bbrzsma7q.streamlit.app/?view=details&id=1669050

---

# 📸 Application Preview

![Movie Recommendation App](./assets/movie-rec-preview.png)

---

# ✨ Features

- 🎬 Smart Movie Recommendation Engine
- 🧠 TF-IDF + Cosine Similarity
- ⚡ FastAPI Backend
- 🎨 Streamlit Frontend
- 🌍 TMDB API Integration
- 🔥 Trending Movies
- ⭐ Top Rated Movies
- 📅 Upcoming Releases
- 🚀 Fast Recommendation System

---

# 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python | Core Language |
| FastAPI | Backend API |
| Streamlit | Frontend UI |
| scikit-learn | Recommendation Engine |
| Pandas | Data Processing |
| TMDB API | Movie Data |
| httpx | Async Requests |

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
````

---

# 🧠 How Recommendation Works

The recommendation engine uses:

* TF-IDF Vectorization
* Cosine Similarity Matrix
* Movie Metadata Analysis

### Workflow

1. User selects a movie
2. Similarity matrix compares vectors
3. Top matching movies are returned
4. TMDB API fetches posters and ratings

---

# ⚙️ Installation

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

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Add TMDB API Key

Create `.env` file:

```env
TMDB_API_KEY=your_tmdb_api_key
```

Get free API key from:

🔗 [https://developer.themoviedb.org](https://developer.themoviedb.org)

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

# 📸 UI Preview

## 🔥 Trending Movies

* Dune: Part Two
* Oppenheimer
* Deadpool & Wolverine
* Inside Out 2
* Furiosa

---

## ⭐ Personalized Recommendations

* Interstellar
* Arrival
* Blade Runner 2049
* Ex Machina
* The Martian

---

# 🏗️ Architecture

```text
Frontend (Streamlit)
        ⇅
Backend (FastAPI)
        ⇅
TMDB API

ML Layer:
- movies.pkl
- similarity.pkl
```

---

# ⚡ Performance

* Async FastAPI Requests
* Cached ML Models
* Optimized Similarity Matrix
* Fast Search & Recommendation

---

# 📌 Future Improvements

* 👤 User Authentication
* ❤️ Watchlist Feature
* 🤖 AI-based Recommendations
* ☁️ Cloud Deployment
* 🐳 Docker Support

---

# 🤝 Contributing

Contributions are welcome.

1. Fork Repository
2. Create Branch
3. Commit Changes
4. Push Changes
5. Open Pull Request

---

# 📜 License

MIT License

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.

---

```
```
