"""
AI-powered Sentiment Analysis for Patient Session Transcripts and Communications
This module provides natural language processing capabilities to analyze patient emotions,
mood patterns, and psychological states from text inputs.
"""

import re
import logging
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from enum import Enum
import statistics

# For sentiment analysis, we'll use multiple approaches
try:
    import nltk
    from nltk.sentiment import SentimentIntensityAnalyzer
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    import nltk.data
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False
    logging.warning("NLTK not available for sentiment analysis")

try:
    from textblob import TextBlob
    TEXTBLOB_AVAILABLE = True
except ImportError:
    TEXTBLOB_AVAILABLE = False
    logging.warning("TextBlob not available for sentiment analysis")

try:
    from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    logging.warning("Transformers not available for sentiment analysis")

class SentimentPolarity(Enum):
    """Enumeration for sentiment polarity levels"""
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"
    VERY_NEGATIVE = "very_negative"
    VERY_POSITIVE = "very_positive"

@dataclass
class SentimentResult:
    """Data class to store sentiment analysis results"""
    text: str
    polarity: SentimentPolarity
    confidence: float
    sentiment_score: float
    emotions: List[Dict[str, Any]]
    mood_patterns: List[str]
    psychological_state: str
    analysis_metadata: Dict[str, Any]

class PatientSentimentAnalyzer:
    """
    AI-powered sentiment analysis system for patient session transcripts and communications
    """
    
    def __init__(self):
        """Initialize the sentiment analyzer with multiple approaches"""
        self.logger = logging.getLogger(__name__)
        
        # Initialize analyzers
        self.nltk_analyzer = None
        self.textblob_analyzer = None
        self.transformer_analyzer = None
        
        # Load required NLTK data
        if NLTK_AVAILABLE:
            try:
                # Check if required NLTK data is downloaded
                nltk.data.find('vader_lexicon')
                nltk.data.find('punkt')
                nltk.data.find('stopwords')
                self.nltk_analyzer = SentimentIntensityAnalyzer()
                self.stop_words = set(stopwords.words('english'))
            except LookupError:
                # Download required NLTK data if not available
                nltk.download('vader_lexicon')
                nltk.download('punkt')
                nltk.download('stopwords')
                self.nltk_analyzer = SentimentIntensityAnalyzer()
                self.stop_words = set(stopwords.words('english'))
        
        # Initialize TextBlob if available
        if TEXTBLOB_AVAILABLE:
            try:
                self.textblob_analyzer = TextBlob
            except Exception as e:
                self.logger.error(f"Error initializing TextBlob: {e}")
                self.textblob_analyzer = None
        
        # Initialize Transformers if available
        if TRANSFORMERS_AVAILABLE:
            try:
                # Use a pre-trained model for sentiment analysis
                self.transformer_analyzer = pipeline("sentiment-analysis")
            except Exception as e:
                self.logger.error(f"Error initializing Transformers: {e}")
                self.transformer_analyzer = None
        
        # Emotion detection keywords
        self.emotion_keywords = {
            "fear": ['afraid', 'scared', 'terrified', 'frightened', 'panic', 'anxiety', 'worry'],
            "anger": ['angry', 'mad', 'furious', 'irate', 'annoyed', 'irritated', 'frustrated'],
            "disgust": ['disgusted', 'revolted', 'nauseated', 'repulsed', 'hate', 'resentful'],
            "joy": ['happy', 'joyful', 'delighted', 'excited', 'pleased', 'thrilled', 'elated'],
            "sadness": ['sad', 'depressed', 'unhappy', 'mournful', 'gloomy', 'downcast'],
            "surprise": ['surprised', 'shocked', 'amazed', 'astonished', 'bewildered'],
            "trust": ['trust', 'confident', 'reliable', 'dependable', 'faithful'],
            "anticipation": ['anticipate', 'expect', 'look forward', 'hope', 'wait'],
            "confidence": ['confident', 'sure', 'certain', 'assured', 'bold'],
            "overwhelmed": ['overwhelmed', 'swamped', 'stressed', 'overloaded'],
            "hopeful": ['hopeful', 'optimistic', 'positive', 'encouraged'],
            "frustrated": ['frustrated', 'irritated', 'disappointed', 'challenged'],
            "anxious": ['anxious', 'worried', 'nervous', 'uneasy', 'tense'],
            "calm": ['calm', 'peaceful', 'relaxed', 'serene', 'tranquil'],
            "confused": ['confused', 'puzzled', 'unclear', 'bewildered'],
            "supported": ['supported', 'helped', 'assisted', 'understood', 'comforted']
        }
        
        # Psychological indicators
        self.psychological_indicators = {
            'depression': ['sad', 'hopeless', 'empty', 'worthless', 'useless', 'despair'],
            'anxiety': ['nervous', 'worried', 'anxious', 'stressed', 'frightened', 'terrified'],
            'bipolar': ['up', 'down', 'high', 'low', 'mood', 'swing'],
            'ptsd': ['trauma', 'flashback', 'trigger', 'scared', 'relive', 'shock'],
            'eating_disorder': ['food', 'weight', 'body', 'image', 'shame', 'self'],
            'suicidal': ['kill', 'die', 'death', 'suicide', 'end', 'worthless', 'alone'],
            'addiction': ['addict', 'substance', 'drug', 'alcohol', 'craving', 'withdrawal']
        }
    
    def _get_sentiment_score(self, text: str) -> Tuple[float, SentimentPolarity, float]:
        """
        Get sentiment score using multiple approaches and combine them
        """
        scores = []
        polarities = []
        confidences = []
        
        # Approach 1: NLTK VADER
        if self.nltk_analyzer:
            try:
                scores_nltk = self.nltk_analyzer.polarity_scores(text)
                # VADER gives compound score between -1 and 1  
                compound_score = scores_nltk['compound']
                scores.append(compound_score)
                
                # Determine polarity based on compound score
                if compound_score >= 0.05:
                    polarity = SentimentPolarity.POSITIVE
                elif compound_score <= -0.05:
                    polarity = SentimentPolarity.NEGATIVE
                else:
                    polarity = SentimentPolarity.NEUTRAL
                
                polarities.append(polarity)
                # Confidence is derived from the magnitude of the compound score
                confidence = abs(compound_score)
                confidences.append(confidence)
            except Exception as e:
                self.logger.warning(f"NLTK sentiment analysis failed: {e}")
        
        # Approach 2: TextBlob
        if self.textblob_analyzer:
            try:
                blob = self.textblob_analyzer(text)
                # TextBlob gives polarity between -1 and 1
                blob_score = blob.sentiment.polarity
                scores.append(blob_score)
                
                # Determine polarity based on polarity score
                if blob_score >= 0.1:
                    polarity = SentimentPolarity.POSITIVE
                elif blob_score <= -0.1:
                    polarity = SentimentPolarity.NEGATIVE
                else:
                    polarity = SentimentPolarity.NEUTRAL
                
                polarities.append(polarity)
                # Confidence based on magnitude of polarity
                confidence = abs(blob_score)
                confidences.append(confidence)
            except Exception as e:
                self.logger.warning(f"TextBlob sentiment analysis failed: {e}")
        
        # Approach 3: Transformers
        if self.transformer_analyzer:
            try:
                result = self.transformer_analyzer(text)
                # This returns labels like 'POSITIVE' or 'NEGATIVE'
                # Convert to numerical score for consistency
                transform_score = 1.0 if result[0]['label'] == 'POSITIVE' else -1.0
                scores.append(transform_score)
                
                # Determine polarity and confidence
                if result[0]['label'] == 'POSITIVE':
                    polarity = SentimentPolarity.POSITIVE
                else:
                    polarity = SentimentPolarity.NEGATIVE
                
                polarities.append(polarity)
                # Confidence based on model's confidence score
                confidence = result[0]['score']
                confidences.append(confidence)
            except Exception as e:
                self.logger.warning(f"Transformers sentiment analysis failed: {e}")
        
        # Combine scores
        if scores:
            combined_score = sum(scores) / len(scores)
            final_polarity = max(set(polarities), key=polarities.count) if polarities else SentimentPolarity.NEUTRAL
            avg_confidence = statistics.mean(confidences) if confidences else 0.0
        else:
            combined_score = 0.0
            final_polarity = SentimentPolarity.NEUTRAL
            avg_confidence = 0.0
        
        # Further refine the polarity based on compound score
        if combined_score >= 0.1:
            final_polarity = SentimentPolarity.POSITIVE
        elif combined_score <= -0.1:
            final_polarity = SentimentPolarity.NEGATIVE
        else:
            final_polarity = SentimentPolarity.NEUTRAL
        
        return combined_score, final_polarity, avg_confidence