# Movie Recommendation System 🎬

A modern, full-stack Movie Recommendation application built with a **Streamlit** frontend and a **FastAPI** backend. It provides movie search, detailed information, and intelligent recommendations using both a local Machine Learning model (TF-IDF) and live data from the TMDB API.

## Features ✨
*   **Intelligent Recommendations:** 
    *   Finds similar movies based on plot and text similarity using a precomputed **TF-IDF Machine Learning** approach.
    *   Discovers related movies matching current genres dynamically via the TMDB API.
*   **Modern Frontend UI:** A sleek, fully responsive interface powered by Streamlit, featuring custom CSS styling and smooth dropdown suggestions.
*   **Blazing Fast Backend:** The FastAPI backend relies on asynchronous network requests (`httpx`) and caches the large ML models into memory upon startup to guarantee instant recommendation routing.
*   **Fail-Resilient Architecture:** Even if the local ML recommendation dataset misses a movie, the internal engine gracefully falls back to TMDB network queries to ensure users always receive content.

## Architecture Structure 🛠️
*   `app.py`: The Streamlit frontend client. Contains UI layouts, routing logic, and HTTP interaction.
*   `main.py`: The FastAPI backend server. Handles external TMDB calls and internal logic computation.
*   `.pkl` files: Pre-computed machine learning matrices and datasets (Pandas DataFrames, Sparse Matrices) representing the movie knowledge base.

## Local Setup & Installation 🚀

### 1. Prerequisites
Ensure you have Python 3.10+ installed.

### 2. Install Dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. API Key Setup
Create a `.env` file in the root of the project and add your TMDB API Key. You can get one for free at [The Movie Database (TMDB)](https://developer.themoviedb.org/docs/getting-started).
```env
TMDB_API_KEY=your_api_key_here
```

### 4. Running the Application locally
**Start the Backend:**
```bash
uvicorn main:app --reload
```
*The backend server will launch at `http://localhost:8000`*

**Start the Frontend:**
*In a separate terminal window, run the following based on your OS:*
```bash
# Windows
$env:API_BASE="http://localhost:8000"; streamlit run app.py

# Mac / Linux
API_BASE="http://localhost:8000" streamlit run app.py
```
*The frontend interface will become available at `http://localhost:8501`*

## Deployment 🌐
Currently, the default frontend setup connects to a hosted backend on Render. Modify the `API_BASE` variable inside `app.py` or through your host's environment settings if you wish to deploy the backend to your own production server.

---
*Created for portfolio and learning purposes.*
