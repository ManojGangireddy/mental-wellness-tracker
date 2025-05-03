# 🧠 Mental Wellness Journal Tracker

A real-time emotional journaling web app that helps users log, track, and reflect on their mental wellness using sentiment analysis, mood visualizations, and intelligent insights.

> Built with 💚 Streamlit, Python, and NLP — Inspired by real-life experiences.

---

## 🚀 Features

### ✅ Core Functionality
- 📝 Daily journal input
- 🧠 Sentiment analysis using:
  - TextBlob
  - VADER (Valence Aware Dictionary)
- 📊 Mood trend visualizations (line graph, word cloud)
- 💾 SQLite-backed journal storage with timestamps
- ✅ Unit-tested sentiment engines

### 🔜 Upcoming Features (Phased Build)
- 😊 Quick emoji-based mood selector
- 🎤 Voice input journaling
- 🌍 Language detection + multilingual support
- 📆 GitHub-style mood calendar
- 📊 Insights dashboard: top moods, mood by weekday, word triggers
- 🔐 User login system (Firebase/Auth)
- 🧱 Pluggable sentiment models (TextBlob, VADER, OpenAI)
- 📤 Export to CSV/PDF
- 📧 Daily email summaries (optional)

---

## 🧱 Tech Stack

| Tech       | Use                            |
|------------|---------------------------------|
| Python     | Core logic                     |
| Streamlit  | UI & front-end                 |
| SQLite     | Database for journaling        |
| TextBlob   | Sentiment analysis engine      |
| VADER      | Alternative sentiment analyzer |
| pytest     | Unit testing                   |

---

## 📦 Project Structure

```
mental-wellness-tracker/
├── app.py                        # Main Streamlit App
├── core/
│   └── sentiment/               # Analyzer strategies
│       ├── analyzer.py
│       ├── textblob_analyzer.py
│       └── vader_analyzer.py
├── database.py                  # SQLite entry handling
├── mood_plotter.py              # Visualizations
├── tests/
│   └── test_analyzers.py        # Unit tests
├── DEV_NOTES.md                 # Build log by phase
├── README.md                    # You’re here!
└── .gitignore
```

---

## 🧪 Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/mental-wellness-tracker.git
cd mental-wellness-tracker
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 🧪 Running Tests
```bash
PYTHONPATH=. pytest tests/
```

---

## 📄 Developer Notes
This project is being built in **phases**. Each new feature is tracked in `DEV_NOTES.md` with a clear goal and change log.

---

## 🙌 Contributing
Pull requests are welcome! If you'd like to contribute a new analyzer, plugin, or visualization, feel free to fork and propose your changes.

---

## 📜 License
This project is open-source under the [MIT License](LICENSE).

---

## 💡 Inspiration
Created by Manoj Reddy — based on personal experiences and a passion for mental wellness, data, and self-improvement through journaling.
```

---

Would you like me to generate the `requirements.txt` now to freeze all your installed packages?
