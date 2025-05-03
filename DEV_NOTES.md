# 🧠 Mental Wellness Journal Tracker – Development Notes

A real-time journal tracker built with Streamlit, analyzing emotional well-being through sentiment analysis and journaling trends.

---

## ✅ Phase 0 – Core App (Initial Commit)
**Status:** ✅ Completed and pushed to GitHub

### 📦 Features:
- Streamlit-based UI
- Journal text input
- Sentiment analysis using:
  - ✅ TextBlob
  - ✅ VADER
- Strategy Pattern for analyzer plug-and-play
- SQLite-based storage of:
  - Journal entry
  - Sentiment
  - Polarity
  - Timestamp
- Unit testing using `pytest` for both analyzers
- Tests passed using `PYTHONPATH=.` workaround
- `.gitignore` and virtual environment setup

### 📁 Folder Structure:
