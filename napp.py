import os
import requests
import streamlit as st

# =============================
# CONFIG
# =============================
API_BASE = os.environ.get("API_BASE", "https://movie-recommendation-6ijc.onrender.com")
TMDB_IMG_W342 = "https://image.tmdb.org/t/p/w342"
TMDB_IMG_W780 = "https://image.tmdb.org/t/p/w780"

st.set_page_config(
    page_title="MovieRec — IMDb Style",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =============================
# GLOBAL STYLES (IMDb-inspired dark theme)
# =============================
st.markdown(
    """
<style>
/* ---- Reset & Base ---- */
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* Hide default streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ---- Top Nav Bar ---- */
.nav-bar {
    background: #1a1a1a;
    padding: 12px 32px;
    display: flex;
    align-items: center;
    gap: 24px;
    border-bottom: 3px solid #E8B923;
}
.nav-logo { font-size: 22px; font-weight: 700; color: #fff; letter-spacing: -0.5px; }
.nav-logo span {
    background: #E8B923; color: #1a1200;
    padding: 2px 8px; border-radius: 4px; font-size: 18px;
}
.nav-links { display: flex; gap: 20px; align-items: center; }
.nav-link { color: #ccc; font-size: 14px; font-weight: 500; text-decoration: none; transition: color 0.2s; }
.nav-link:hover { color: #E8B923; }

/* ---- Page wrapper ---- */
.page { padding: 24px 32px; }

/* ---- Section headers ---- */
.section-header { display: flex; align-items: center; gap: 8px; margin: 0 0 16px; }
.section-header h2 { font-size: 20px; font-weight: 600; color: #fff; margin: 0; }
.section-header .accent { color: #E8B923; font-size: 20px; }

/* ---- Movie cards grid ---- */
.movie-card {
    background: #1e1e1e;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #2c2c2c;
    transition: transform .18s, border-color .18s;
    margin-bottom: 4px;
}
.movie-card:hover { transform: translateY(-3px); border-color: #E8B923; }
.poster-wrap { position: relative; aspect-ratio: 2/3; overflow: hidden; background: #2a2a2a; }
.poster-wrap img { width: 100%; height: 100%; object-fit: cover; display: block; }
.poster-placeholder {
    width: 100%; height: 100%; display: flex; align-items: center;
    justify-content: center; font-size: 48px; color: #444; background: #1e1e1e;
    aspect-ratio: 2/3;
}
.rating-badge {
    position: absolute; top: 8px; left: 8px;
    background: rgba(0,0,0,0.78); color: #E8B923;
    font-size: 12px; font-weight: 600; padding: 3px 7px; border-radius: 5px;
}
.wl-badge {
    position: absolute; top: 8px; right: 8px;
    background: #E8B923; color: #1a1200;
    font-size: 11px; font-weight: 700; padding: 2px 6px; border-radius: 4px;
}
.card-body { padding: 10px 11px 12px; }
.card-title {
    font-size: 13px; font-weight: 600; color: #f0f0f0;
    line-height: 1.3; margin-bottom: 4px;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.card-meta { font-size: 11.5px; color: #888; }

/* ---- Detail hero ---- */
.detail-title { font-size: 28px; font-weight: 700; color: #fff; line-height: 1.2; margin-bottom: 6px; }
.detail-tagline { font-size: 15px; color: #888; font-style: italic; margin-bottom: 14px; }
.imdb-score-box {
    display: inline-flex; align-items: center; gap: 8px;
    background: #E8B923; color: #1a1200;
    border-radius: 8px; padding: 8px 14px; margin-bottom: 14px;
}
.imdb-score-box .score { font-size: 22px; font-weight: 700; }
.imdb-score-box .label { font-size: 11px; font-weight: 600; line-height: 1.3; }
.genre-tags { display: flex; flex-wrap: wrap; gap: 7px; margin-bottom: 14px; }
.genre-tag {
    font-size: 12px; padding: 4px 12px; border-radius: 14px;
    border: 1px solid #444; color: #bbb; background: #222;
}
.overview-text { font-size: 14.5px; line-height: 1.75; color: #ccc; margin-bottom: 18px; }

/* ---- Backdrop ---- */
.backdrop-wrap { border-radius: 12px; overflow: hidden; margin-bottom: 28px; position: relative; }
.backdrop-wrap img { width: 100%; max-height: 340px; object-fit: cover; display: block; }
.backdrop-overlay {
    position: absolute; bottom: 0; left: 0; right: 0;
    background: linear-gradient(transparent, rgba(0,0,0,0.7)); padding: 20px;
}
.backdrop-label { color: #E8B923; font-size: 12px; font-weight: 600; }

/* ---- Stats bar ---- */
.stats-bar {
    display: flex; gap: 20px; background: #1a1a1a;
    border: 1px solid #2c2c2c; border-radius: 10px;
    padding: 14px 20px; margin-bottom: 24px;
}
.stat-item { text-align: center; }
.stat-val { font-size: 20px; font-weight: 700; color: #E8B923; }
.stat-lbl { font-size: 11px; color: #888; margin-top: 2px; }

/* ---- Streamlit widget overrides ---- */
.stButton > button {
    background: #1e1e1e !important; color: #E8B923 !important;
    border: 1px solid #E8B923 !important; border-radius: 8px !important;
    font-weight: 600 !important; font-size: 12px !important;
    padding: 6px 12px !important; transition: background .15s !important;
}
.stButton > button:hover { background: rgba(232,185,35,0.15) !important; }
.stTextInput > div > div > input {
    background: #1e1e1e !important; color: #fff !important;
    border: 1px solid #444 !important; border-radius: 8px !important;
    font-size: 14px !important;
}
.stSelectbox > div > div {
    background: #1e1e1e !important; color: #fff !important;
    border: 1px solid #444 !important; border-radius: 8px !important;
}
div[data-testid="stSidebar"] {
    background: #111 !important; border-right: 1px solid #2c2c2c !important;
}

/* ---- Watchlist sidebar items ---- */
.wl-item {
    display: flex; gap: 10px; align-items: flex-start;
    padding: 10px 0; border-bottom: 1px solid #2c2c2c;
}
.wl-thumb {
    width: 44px; height: 66px; border-radius: 5px;
    overflow: hidden; background: #2a2a2a; flex-shrink: 0;
}
.wl-thumb img { width: 100%; height: 100%; object-fit: cover; }
.wl-info { flex: 1; min-width: 0; }
.wl-title { font-size: 13px; font-weight: 600; color: #eee; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.wl-year { font-size: 11px; color: #666; }
.watchlist-empty { text-align: center; color: #666; font-size: 13px; padding: 20px 0; }

/* ---- No results ---- */
.no-results { text-align: center; padding: 48px 24px; color: #666; font-size: 15px; }
.no-results .icon { font-size: 48px; margin-bottom: 12px; display: block; }
</style>
""",
    unsafe_allow_html=True,
)

# =============================
# SESSION STATE
# =============================
def init_state():
    defaults = {
        "view": "home",
        "selected_movie": None,
        "selected_tmdb_id": None,
        "active_tab": "trending",
        "watchlist": [],
        "search_query": "",
        "rec_tab": "tfidf",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
            
    # Deep-linking support
    qp_view = st.query_params.get("view")
    qp_id = st.query_params.get("id")
    
    if qp_view in ("home", "details", "tv", "top250", "watchlist"):
        st.session_state.view = qp_view
    
    if qp_id:
        try:
            st.session_state.selected_tmdb_id = int(qp_id)
            st.session_state.view = "details"
        except ValueError:
            pass

init_state()

# =============================
# API HELPERS
# =============================
@st.cache_data(ttl=60)
def api_get(path: str, params: dict | None = None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=20)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}"
        return r.json(), None
    except Exception as e:
        return None, str(e)


def to_card(m: dict) -> dict:
    """Normalize any movie dict into a standard card."""
    poster = m.get("poster_url") or (
        f"{TMDB_IMG_W342}{m['poster_path']}" if m.get("poster_path") else None
    )
    return {
        "tmdb_id": m.get("tmdb_id") or m.get("id"),
        "title": m.get("title", "Untitled"),
        "year": (m.get("release_date") or m.get("year") or "")[:4],
        "rating": m.get("vote_average") or m.get("rating"),
        "poster_url": poster,
        "overview": m.get("overview", ""),
        "genres": m.get("genres", []),
        "backdrop_url": m.get("backdrop_url") or (
            f"{TMDB_IMG_W780}{m['backdrop_path']}" if m.get("backdrop_path") else None
        ),
    }


def cards_from_tfidf(items):
    cards = []
    for x in items or []:
        t = x.get("tmdb") or {}
        if t.get("tmdb_id"):
            cards.append(to_card({**t, "title": t.get("title") or x.get("title", "")}))
    return cards


def parse_search_results(data, keyword: str):
    keyword_l = keyword.lower()
    if isinstance(data, dict) and "results" in data:
        raw = data["results"] or []
    elif isinstance(data, list):
        raw = data
    else:
        return []
    items = [to_card(m) for m in raw if m.get("title") or m.get("tmdb_id")]
    matched = [x for x in items if keyword_l in x["title"].lower()]
    return matched if matched else items


# =============================
# FALLBACK DATA  (when API is cold)
# =============================
FALLBACK = [
    {"tmdb_id": 872585,  "title": "Oppenheimer",           "year": "2023", "rating": 8.9,
     "poster_url": f"{TMDB_IMG_W342}/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
     "overview": "The story of J. Robert Oppenheimer and the development of the atomic bomb."},
    {"tmdb_id": 346698,  "title": "Barbie",                "year": "2023", "rating": 6.9,
     "poster_url": f"{TMDB_IMG_W342}/iuFNMS8U5cb6xfzi51Dbkovj7vM.jpg",
     "overview": "Barbie and Ken are having the time of their lives in Barbieland."},
    {"tmdb_id": 533535,  "title": "Deadpool & Wolverine",  "year": "2024", "rating": 7.7,
     "poster_url": f"{TMDB_IMG_W342}/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg",
     "overview": "Wade Wilson returns as Deadpool alongside Wolverine."},
    {"tmdb_id": 1022789, "title": "Inside Out 2",          "year": "2024", "rating": 7.7,
     "poster_url": f"{TMDB_IMG_W342}/vpnVM9B6NMmQpWeZvzLvDESb2QY.jpg",
     "overview": "Teenager Riley's mind headquarters faces brand-new Emotions!"},
    {"tmdb_id": 438631,  "title": "Dune: Part Two",        "year": "2024", "rating": 8.5,
     "poster_url": f"{TMDB_IMG_W342}/8b8R8l88Qje9dn9OE8PY05Nxl1X.jpg",
     "overview": "Paul Atreides unites with Chani and the Fremen."},
    {"tmdb_id": 786892,  "title": "Furiosa",               "year": "2024", "rating": 7.7,
     "poster_url": f"{TMDB_IMG_W342}/iADOJ8Zymht2JPMoy3R7xceZprc.jpg",
     "overview": "The origin story of the renegade warrior Furiosa."},
    {"tmdb_id": 519182,  "title": "Despicable Me 4",       "year": "2024", "rating": 6.8,
     "poster_url": f"{TMDB_IMG_W342}/3w84hCFJATpiCO5g8hpdWVPBbmq.jpg",
     "overview": "Gru and Lucy face a new super-villain and a new baby."},
    {"tmdb_id": 940551,  "title": "Migration",             "year": "2023", "rating": 6.8,
     "poster_url": f"{TMDB_IMG_W342}/ldfCF9RhR40mppkzmftxapaHeTo.jpg",
     "overview": "A duck family embarks on an adventurous vacation."},
    {"tmdb_id": 695721,  "title": "The Hunger Games: Ballad", "year": "2023", "rating": 7.0,
     "poster_url": f"{TMDB_IMG_W342}/mBaXZ95R2OxueZhvQbcEWy2DqyO.jpg",
     "overview": "The origin story of President Snow before the Hunger Games."},
    {"tmdb_id": 934632,  "title": "Alien: Romulus",        "year": "2024", "rating": 7.2,
     "poster_url": f"{TMDB_IMG_W342}/b33nnKl1GSFbao4l3fZDDqsMx0F.jpg",
     "overview": "Young space colonizers come face-to-face with the most terrifying life form."},
    {"tmdb_id": 891699,  "title": "Aquaman 2",             "year": "2023", "rating": 5.9,
     "poster_url": f"{TMDB_IMG_W342}/7lTnXOy0iNtBAdRP3TZvaKJ77F6.jpg",
     "overview": "Arthur Curry must forge an alliance to protect Atlantis."},
    {"tmdb_id": 848326,  "title": "Rebel Moon — Part Two", "year": "2024", "rating": 5.7,
     "poster_url": f"{TMDB_IMG_W342}/dkodEBPL6YPr5P1DVGHvVZAnOlP.jpg",
     "overview": "The warriors of Veldt prepare to fight back against the Motherworld."},
]

TAB_CONFIG = [
    ("trending",    "🔥 Trending"),
    ("popular",     "📈 Popular"),
    ("top_rated",   "⭐ Top Rated"),
    ("now_playing", "▶️ Now Playing"),
    ("upcoming",    "📅 Upcoming"),
]
TAB_ICONS = {"trending": "🔥", "popular": "📈", "top_rated": "⭐", "now_playing": "▶️", "upcoming": "📅"}

# =============================
# NAVIGATION
# =============================
def goto_home():
    st.session_state.view = "home"
    st.session_state.selected_movie = None
    st.session_state.selected_tmdb_id = None
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_details(card: dict):
    st.session_state.view = "details"
    st.session_state.selected_movie = card
    st.session_state.selected_tmdb_id = card.get("tmdb_id")
    st.query_params["view"] = "details"
    st.query_params["id"] = str(card.get("tmdb_id"))
    st.rerun()


def toggle_watchlist(card: dict):
    tid = card.get("tmdb_id")
    ids = [m.get("tmdb_id") for m in st.session_state.watchlist]
    if tid in ids:
        st.session_state.watchlist = [m for m in st.session_state.watchlist if m.get("tmdb_id") != tid]
    else:
        st.session_state.watchlist.append(card)

# =============================
# UI COMPONENTS
# =============================
def render_nav():
    st.markdown(
        """
        <div class="nav-bar">
            <a href="/?view=home" target="_self" style="text-decoration:none;">
                <div class="nav-logo"><span>🎬 Movie</span>Rec</div>
            </a>
            <div class="nav-links">
                <a href="/?view=home" target="_self" class="nav-link">Movies</a>
                <a href="/?view=tv" target="_self" class="nav-link">TV Shows</a>
                <a href="/?view=top250" target="_self" class="nav-link">Top 250</a>
                <a href="/?view=watchlist" target="_self" class="nav-link">Watchlist</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def poster_card_html(card: dict, in_watchlist: bool = False) -> str:
    tid    = card.get("tmdb_id", "")
    title  = card.get("title", "Untitled")
    year   = card.get("year", "")
    rating = card.get("rating")
    poster = card.get("poster_url", "")

    rating_html = f'<div class="rating-badge">⭐ {float(rating):.1f}</div>' if rating else ""
    wl_html     = '<div class="wl-badge">✓</div>' if in_watchlist else ""

    if poster:
        img_html = f'<img src="{poster}" alt="{title}" loading="lazy"/>'
    else:
        img_html = '<div class="poster-placeholder">🎬</div>'

    meta = year
    if rating:
        meta += f" · ⭐ {float(rating):.1f}"

    return f"""
<div class="movie-card">
    <div class="poster-wrap">
        {img_html}
        {rating_html}
        {wl_html}
    </div>
    <div class="card-body">
        <div class="card-title" title="{title}">{title}</div>
        <div class="card-meta">{meta}</div>
    </div>
</div>
"""


def render_movie_grid(cards, cols=6, key_prefix="grid"):
    if not cards:
        st.markdown('<div class="no-results"><span class="icon">🎬</span>No movies found.</div>', unsafe_allow_html=True)
        return

    wl_ids = {m.get("tmdb_id") for m in st.session_state.watchlist}
    rows = (len(cards) + cols - 1) // cols

    for r in range(rows):
        st_cols = st.columns(cols)
        for c in range(cols):
            idx = r * cols + c
            if idx >= len(cards):
                break
            card   = cards[idx]
            tid    = card.get("tmdb_id")
            in_wl  = tid in wl_ids
            with st_cols[c]:
                st.markdown(poster_card_html(card, in_wl), unsafe_allow_html=True)
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("Open", key=f"{key_prefix}_o_{r}_{c}_{tid}"):
                        goto_details(card)
                with c2:
                    lbl = "✓" if in_wl else "+"
                    if st.button(lbl, key=f"{key_prefix}_w_{r}_{c}_{tid}", help="Toggle watchlist"):
                        toggle_watchlist(card)
                        st.rerun()


def render_section_title(icon: str, title: str):
    st.markdown(
        f'<div class="section-header"><span class="accent">{icon}</span><h2>{title}</h2></div>',
        unsafe_allow_html=True,
    )


def render_stats_bar():
    wl_count = len(st.session_state.watchlist)
    st.markdown(
        f"""
        <div class="stats-bar">
            <div class="stat-item"><div class="stat-val">1M+</div><div class="stat-lbl">Movies</div></div>
            <div class="stat-item"><div class="stat-val">500K+</div><div class="stat-lbl">Reviews</div></div>
            <div class="stat-item"><div class="stat-val">50K+</div><div class="stat-lbl">Cast &amp; Crew</div></div>
            <div class="stat-item"><div class="stat-val">{wl_count}</div><div class="stat-lbl">In Watchlist</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =============================
# SIDEBAR
# =============================
with st.sidebar:
    st.markdown("## 🎬 MovieRec")
    st.markdown("---")

    st.markdown("### 🔍 Quick Search")
    sb_search = st.text_input("Quick Search", placeholder="Search title...", key="sidebar_search",
                               label_visibility="collapsed")
    if sb_search and len(sb_search.strip()) >= 2:
        if st.button("Search →", key="sb_search_btn"):
            st.session_state.search_query = sb_search.strip()
            st.session_state.view = "home"
            st.rerun()

    st.markdown("---")
    st.markdown("### 📂 Browse")
    for tab_id, tab_label in TAB_CONFIG:
        if st.button(tab_label, key=f"sb_tab_{tab_id}"):
            st.session_state.active_tab = tab_id
            st.session_state.view = "home"
            st.session_state.search_query = ""
            st.rerun()

    st.markdown("---")
    st.markdown("### 🎛️ Display")
    grid_cols = st.slider("Grid columns", 3, 8, 6)

    st.markdown("---")
    st.markdown("### 📌 My Watchlist")
    wl = st.session_state.watchlist
    if not wl:
        st.markdown('<div class="watchlist-empty">Your watchlist is empty.<br>Hit + on any movie card.</div>',
                    unsafe_allow_html=True)
    else:
        for m in wl:
            poster = m.get("poster_url", "")
            title  = m.get("title", "")
            year   = m.get("year", "")
            thumb  = f'<img src="{poster}" alt="{title}"/>' if poster else "🎬"
            st.markdown(
                f"""<div class="wl-item">
                    <div class="wl-thumb">{thumb}</div>
                    <div class="wl-info">
                        <div class="wl-title">{title}</div>
                        <div class="wl-year">{year}</div>
                    </div>
                </div>""",
                unsafe_allow_html=True,
            )
            if st.button("Remove", key=f"wl_rm_{m.get('tmdb_id')}"):
                toggle_watchlist(m)
                st.rerun()

# =============================
# MAIN CONTENT
# =============================
render_nav()
st.markdown('<div class="page">', unsafe_allow_html=True)

# ============================================================
# VIEW: HOME / SEARCH
# ============================================================
if st.session_state.view == "home":

    # Search bar
    s_col, b_col = st.columns([5, 1])
    with s_col:
        typed = st.text_input(
            "Search", value=st.session_state.search_query,
            placeholder="🔍  Search movies, actors, directors...",
            key="main_search", label_visibility="collapsed",
        )
    with b_col:
        search_clicked = st.button("Search", key="main_search_btn")

    if search_clicked and typed.strip():
        st.session_state.search_query = typed.strip()

    st.markdown("---")

    # ---- SEARCH MODE ----
    if st.session_state.search_query:
        q = st.session_state.search_query
        render_section_title("🔍", f'Results for "{q}"')

        if st.button("✕  Clear search", key="clear_search"):
            st.session_state.search_query = ""
            st.rerun()

        with st.spinner("Searching..."):
            data, err = api_get("/tmdb/search", params={"query": q})

        if err or data is None:
            st.info("API unavailable — showing offline results.")
            cards = [to_card(m) for m in FALLBACK if q.lower() in m["title"].lower()]
            if not cards:
                cards = [to_card(m) for m in FALLBACK]
        else:
            cards = parse_search_results(data, q)

        if cards:
            st.markdown(f'<div style="color:#888;font-size:13px;margin-bottom:12px">{len(cards)} result(s)</div>',
                        unsafe_allow_html=True)
            # Autocomplete dropdown
            suggestions = [
                (f"{c['title']} ({c['year']})" if c["year"] else c["title"], c)
                for c in cards[:10]
            ]
            labels  = ["— Jump to a movie —"] + [s[0] for s in suggestions]
            chosen  = st.selectbox("Autocomplete", labels, key="autocomplete", label_visibility="collapsed")
            if chosen != "— Jump to a movie —":
                lmap = {s[0]: s[1] for s in suggestions}
                goto_details(lmap[chosen])

            render_movie_grid(cards, cols=grid_cols, key_prefix="search")
        else:
            st.markdown('<div class="no-results"><span class="icon">🔍</span>No movies matched your search.</div>',
                        unsafe_allow_html=True)

    # ---- HOME FEED MODE ----
    else:
        # Category tab buttons
        tab_btn_cols = st.columns(len(TAB_CONFIG))
        for i, (tab_id, tab_label) in enumerate(TAB_CONFIG):
            with tab_btn_cols[i]:
                if st.button(tab_label, key=f"maintab_{tab_id}"):
                    st.session_state.active_tab = tab_id
                    st.rerun()

        st.markdown("")
        render_stats_bar()

        active_label = dict(TAB_CONFIG)[st.session_state.active_tab]
        render_section_title(TAB_ICONS[st.session_state.active_tab], active_label)

        with st.spinner("Loading movies..."):
            raw, err = api_get("/home", params={"category": st.session_state.active_tab, "limit": 24})

        if err or not raw:
            st.info("Using offline data (API is warming up — try again shortly).")
            cards = [to_card(m) for m in FALLBACK]
        else:
            cards = [to_card(m) for m in raw] if isinstance(raw, list) else []

        render_movie_grid(cards, cols=grid_cols, key_prefix=f"home_{st.session_state.active_tab}")


# ============================================================
# VIEW: DETAILS
# ============================================================
elif st.session_state.view == "details":
    movie    = st.session_state.selected_movie
    tmdb_id  = st.session_state.selected_tmdb_id

    if not tmdb_id:
        st.warning("No movie selected.")
        if st.button("← Back to Home"):
            goto_home()
        st.stop()

    if st.button("← Back to Home", key="back_top"):
        goto_home()

    # Fetch full details from API
    with st.spinner("Loading movie details..."):
        details, err = api_get(f"/movie/id/{tmdb_id}")

    card = to_card(details) if details else movie

    title    = card.get("title", "Unknown")
    year     = card.get("year", "")
    rating   = card.get("rating")
    overview = card.get("overview") or "No overview available."
    poster   = card.get("poster_url")
    backdrop = card.get("backdrop_url")
    genres   = card.get("genres") or (details or {}).get("genres") or []
    in_wl    = any(m.get("tmdb_id") == tmdb_id for m in st.session_state.watchlist)

    # Backdrop image
    if backdrop:
        st.markdown(
            f'<div class="backdrop-wrap"><img src="{backdrop}" alt="{title} backdrop"/>'
            f'<div class="backdrop-overlay"><span class="backdrop-label">🎬 BACKDROP</span></div></div>',
            unsafe_allow_html=True,
        )

    # Hero layout
    col_poster, col_info = st.columns([1, 2.8], gap="large")

    with col_poster:
        if poster:
            st.image(poster, use_column_width=True)
        else:
            st.markdown(
                '<div style="background:#2a2a2a;aspect-ratio:2/3;border-radius:10px;'
                'display:flex;align-items:center;justify-content:center;font-size:48px">🎬</div>',
                unsafe_allow_html=True,
            )

    with col_info:
        st.markdown(f'<div class="detail-title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-tagline">{year}</div>', unsafe_allow_html=True)

        if rating:
            st.markdown(
                f'<div class="imdb-score-box">'
                f'<span class="score">{float(rating):.1f}</span>'
                f'<span class="label">IMDb<br>Score</span></div>',
                unsafe_allow_html=True,
            )

        if genres:
            tags = "".join(
                f'<span class="genre-tag">{g["name"] if isinstance(g, dict) else g}</span>'
                for g in genres
            )
            st.markdown(f'<div class="genre-tags">{tags}</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="overview-text">{overview}</div>', unsafe_allow_html=True)

        act1, act2 = st.columns([1, 1])
        with act1:
            wl_lbl = "✓ In Watchlist" if in_wl else "+ Add to Watchlist"
            if st.button(wl_lbl, key="detail_wl"):
                toggle_watchlist(card)
                st.rerun()
        with act2:
            if st.button("🔗 Share", key="detail_share"):
                st.toast("Copy the URL from your browser to share this movie!", icon="✅")

    st.markdown("---")

    # ---- RECOMMENDATIONS ----
    render_section_title("🎯", "Recommendations")

    rec_col1, rec_col2 = st.columns(2)
    with rec_col1:
        if st.button("🔎 Similar Movies (TF-IDF)", key="rec_tfidf_btn"):
            st.session_state.rec_tab = "tfidf"
    with rec_col2:
        if st.button("🎭 Same Genre", key="rec_genre_btn"):
            st.session_state.rec_tab = "genre"

    with st.spinner("Loading recommendations..."):
        bundle, b_err = api_get(
            "/movie/search",
            params={"query": title, "tfidf_top_n": 12, "genre_limit": 12},
        )

    if not b_err and bundle:
        tfidf_cards = cards_from_tfidf(bundle.get("tfidf_recommendations"))
        genre_cards = [to_card(m) for m in (bundle.get("genre_recommendations") or [])]
    else:
        genre_only, _ = api_get("/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 12})
        tfidf_cards = []
        genre_cards = [to_card(m) for m in (genre_only or [])]

    if st.session_state.rec_tab == "genre":
        render_section_title("🎭", "More Like This — By Genre")
        if genre_cards:
            render_movie_grid(genre_cards, cols=grid_cols, key_prefix="rec_genre")
        else:
            st.info("No genre recommendations available.")
    else:
        render_section_title("🔎", "Similar Movies — Content Matching")
        if tfidf_cards:
            render_movie_grid(tfidf_cards, cols=grid_cols, key_prefix="rec_tfidf")
        elif genre_cards:
            st.info("Showing genre-based recommendations as fallback.")
            render_movie_grid(genre_cards, cols=grid_cols, key_prefix="rec_genre_fb")
        else:
            st.warning("No recommendations found right now.")

    st.markdown("---")
    if st.button("← Back to Home", key="back_bottom"):
        goto_home()

elif st.session_state.view == "tv":
    render_section_title("📺", "TV Shows")
    st.info("TV Shows feature coming soon! We are expanding our database.")
    if st.button("← Back to Home"): goto_home()

elif st.session_state.view == "top250":
    render_section_title("🏆", "IMDb Top 250")
    st.info("Top 250 list coming soon!")
    if st.button("← Back to Home"): goto_home()

elif st.session_state.view == "watchlist":
    render_section_title("📌", "My Watchlist")
    wl = st.session_state.watchlist
    if not wl:
        st.info("Your watchlist is empty. Go add some movies!")
    else:
        render_movie_grid(wl, cols=grid_cols, key_prefix="page_wl")
    if st.button("← Back to Home"): goto_home()

st.markdown("</div>", unsafe_allow_html=True)

# ---- Footer ----
st.markdown(
    """
    <div style="text-align:center;padding:24px;color:#444;font-size:12px;
                border-top:1px solid #222;margin-top:32px">
        🎬 MovieRec — Powered by TMDB &amp; FastAPI · Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
