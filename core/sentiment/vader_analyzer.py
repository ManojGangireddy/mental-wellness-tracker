# core/sentiment/vader_analyzer.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from .analyzer import SentimentAnalyzer

class VaderAnalyzer(SentimentAnalyzer):
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text: str) -> tuple[str, float]:
        scores = self.analyzer.polarity_scores(text)
        compound = scores["compound"]

        if compound > 0.1:
            sentiment = "Positive"
        elif compound < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return sentiment, compound
