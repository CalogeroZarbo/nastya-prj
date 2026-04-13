"""
AI-powered Sentiment Analysis for Patient Session Transcripts and Communications
"""

__version__ = "0.1.0"
__author__ = "AI Healthcare Team"

# Import the main analyzer
from .sentiment_analysis import PatientSentimentAnalyzer, analyze_sentiment

__all__ = ["PatientSentimentAnalyzer", "analyze_sentiment"]