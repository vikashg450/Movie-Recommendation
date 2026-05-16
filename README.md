````markdown
# 🎬 MovieRec — Movie Recommendation System

A full-stack movie recommendation app built with **Streamlit**, **FastAPI**, and a **TF-IDF Machine Learning model** to deliver smart movie suggestions along with live movie data from TMDB.

---

## 🚀 Features

- 🎯 TF-IDF based movie recommendation engine
- 🌍 Live movie data from TMDB API
- ⚡ FastAPI backend with async requests
- 🎨 Streamlit frontend UI
- 🔥 Trending, Popular, Top Rated, Upcoming movies
- 🧠 Cosine similarity recommendation model
- 🛡️ Genre-based fallback recommendation system
- 🚀 Fast response time with cached ML models

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- Streamlit
- scikit-learn
- Pandas
- httpx
- TMDB API

---

# 📂 Project Architecture

```text
Frontend (Streamlit app.py)
        ⇅
Backend (FastAPI main.py)
        ⇅
TMDB API

ML Layer:
- movies.pkl
- similarity.pkl
````

---

# 🧠 ML Recommendation Engine

The recommendation system uses:

* TF-IDF Vectorization
* Cosine Similarity Matrix
* Movie overview + metadata embeddings

When a movie is selected:

1. The similarity matrix finds nearest movies
2. Results are ranked by cosine similarity score
3. TMDB API fetches posters and live metadata

---

# 📦 Quick Start

## 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd movie-recommendation-system
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Add TMDB API Key

Create a `.env` file in the root directory:

```env
TMDB_API_KEY=your_tmdb_api_key
```

Get free API key from:

[https://developer.themoviedb.org](https://developer.themoviedb.org)

---

## 5️⃣ Start FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

## 6️⃣ Start Streamlit Frontend

```bash
API_BASE="http://localhost:8000" streamlit run app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# 📁 Important Files

| File               | Description              |
| ------------------ | ------------------------ |
| `app.py`           | Streamlit frontend       |
| `main.py`          | FastAPI backend          |
| `movies.pkl`       | Movie dataset            |
| `similarity.pkl`   | Cosine similarity matrix |
| `requirements.txt` | Python dependencies      |

---

# 🌐 TMDB Integration

The app fetches:

* Posters
* Trending movies
* Popular movies
* Upcoming movies
* Ratings
* Metadata

using the TMDB v3 API.

---

# ⚡ Performance

* Async FastAPI requests with `httpx`
* Startup model caching
* Low latency recommendation generation
* Sparse similarity matrix optimization

---

# 🎯 Future Improvements

* User authentication
* Personalized watchlists
* Collaborative filtering
* Hybrid recommendation model
* Docker deployment
* Cloud hosting support

---

# 📸 Preview

```text
🎬 Trending Movies
⭐ Personalized Recommendations
🔥 Top Rated Films
📅 Upcoming Releases
```

---

# 🤝 Contributing

Contributions are welcome!

Fork the repository and submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

# ❤️ Built With

* FastAPI
* Streamlit
* scikit-learn
* TMDB API
* Python

---

```
```
