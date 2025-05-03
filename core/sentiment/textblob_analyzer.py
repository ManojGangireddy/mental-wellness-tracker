# core/sentiment/textblob_analyzer.py

from textblob import TextBlob
from .analyzer import SentimentAnalyzer

class TextBlobAnalyzer(SentimentAnalyzer):
    def analyze(self, text: str) -> tuple[str, float]:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return sentiment, polarity
