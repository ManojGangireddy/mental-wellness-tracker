# tests/test_analyzers.py

import pytest
from core.sentiment.textblob_analyzer import TextBlobAnalyzer
from core.sentiment.vader_analyzer import VaderAnalyzer

@pytest.mark.parametrize("text, expected_sentiment", [
    ("I am so happy today!", "Positive"),
    ("This is the worst day ever.", "Negative"),
    ("I went to the store.", "Neutral"),
])
def test_textblob_analyzer(text, expected_sentiment):
    analyzer = TextBlobAnalyzer()
    sentiment, score = analyzer.analyze(text)
    assert sentiment == expected_sentiment

@pytest.mark.parametrize("text, expected_sentiment", [
    ("I love coding!", "Positive"),
    ("Everything is horrible", "Negative"),
    ("Just an average day.", "Neutral"),
])
def test_vader_analyzer(text, expected_sentiment):
    analyzer = VaderAnalyzer()
    sentiment, score = analyzer.analyze(text)
    assert sentiment == expected_sentiment
