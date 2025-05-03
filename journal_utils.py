# journal_utils.py
from textblob import TextBlob

def analyze_mood(text):
    """
    Analyze the sentiment of the journal entry using TextBlob.
    Returns:
        sentiment (str): Positive / Neutral / Negative
        polarity (float): Polarity score (-1.0 to 1.0)
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, polarity
