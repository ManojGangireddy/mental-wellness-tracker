# app.py
import streamlit as st
from core.sentiment.textblob_analyzer import TextBlobAnalyzer
from core.sentiment.vader_analyzer import VaderAnalyzer
from database import insert_entry, get_entries
from mood_plotter import plot_mood_trend, show_wordcloud

# Sidebar for selecting analyzer
st.sidebar.title("⚙️ Settings")
analyzer_option = st.sidebar.radio("Choose Sentiment Analyzer:", ("TextBlob", "VADER"))

# Set analyzer based on choice
if analyzer_option == "TextBlob":
    analyzer = TextBlobAnalyzer()
else:
    analyzer = VaderAnalyzer()

# App Title
st.title("🧠 Mental Wellness Journal Tracker")
st.subheader("Log your thoughts. Track your moods. Understand yourself.")

# Journal Input
journal_text = st.text_area("How are you feeling today?", height=150)

if st.button("Submit Entry"):
    if journal_text.strip() == "":
        st.warning("Please enter something before submitting.")
    else:
        sentiment, polarity = analyzer.analyze(journal_text)
        insert_entry(journal_text, sentiment, polarity)
        st.success(f"Entry saved with mood: {sentiment} (Polarity Score: {polarity:.2f})")

# Divider
st.markdown("---")
st.header("📈 Your Mood Trends")

entries = get_entries()
if entries:
    plot_mood_trend(entries)
    show_wordcloud(entries)
else:
    st.info("No journal entries found yet. Start writing today!")
