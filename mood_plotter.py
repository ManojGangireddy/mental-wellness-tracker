# mental_wellness_tracker/mood_plotter.py
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

def plot_mood_trend(entries):
    df = pd.DataFrame(entries, columns=["entry", "sentiment", "polarity", "timestamp"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    st.subheader("📅 Mood Over Time")
    mood_map = {"Positive": 1, "Neutral": 0, "Negative": -1}
    df["mood_score"] = df["sentiment"].map(mood_map)

    plt.figure(figsize=(10, 4))
    plt.plot(df["timestamp"], df["mood_score"], marker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel("Mood Score")
    plt.grid(True)
    st.pyplot(plt)

def show_wordcloud(entries):
    st.subheader("☁️ Word Cloud of Your Journal")
    text = " ".join([entry[0] for entry in entries])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)
