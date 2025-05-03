# core/sentiment/analyzer.py

from abc import ABC, abstractmethod

class SentimentAnalyzer(ABC):
    @abstractmethod
    def analyze(self, text: str) -> tuple[str, float]:
        """Returns a sentiment label and polarity score."""
        pass
