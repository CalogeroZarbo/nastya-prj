"""
Test file for the Patient Sentiment Analysis system
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sentiment_analysis import PatientSentimentAnalyzer, analyze_sentiment
from analysis_utils import format_analysis_output, generate_analysis_report

def test_basic_sentiment_analysis():
    """Test basic sentiment analysis functionality"""
    print("Testing basic sentiment analysis...")
    
    analyzer = PatientSentimentAnalyzer()
    
    # Test cases
    test_cases = [
        "I am feeling extremely happy and excited about my future!",
        "I feel so sad and disappointed in myself.",
        "The weather is okay, nothing special.",
        "I'm really scared and anxious about the upcoming exam.",
        "I hate this situation, it's absolutely terrible!"
    ]
    
    for i, text in enumerate(test_cases, 1):
        print(f"\nTest case {i}: '{text}'")
        try:
            result = analyzer.analyze_text(text)
            print(f"  Polarity: {result.polarity.value}")
            print(f"  Score: {result.sentiment_score:.3f}")
            print(f"  Confidence: {result.confidence:.3f}")
            print(f"  Psychological State: {result.psychological_state}")
            
            if result.emotions:
                print(f"  Emotions detected: {[e['emotion'] for e in result.emotions]}")
            else:
                print("  No specific emotions detected")
                
        except Exception as e:
            print(f"  Error: {e}")

def test_simple_function():
    """Test the simple analysis function"""
    print("\n\nTesting simple analysis function...")
    
    test_texts = [
        "I love this new treatment!",
        "I'm feeling really down and hopeless",
        "The appointment went fine, nothing exciting"
    ]
    
    for text in test_texts:
        result = analyze_sentiment(text)
        print(f"Text: '{text}'")
        print(f"  Result: {result}")
        print()

def test_conversation_analysis():
    """Test conversation analysis"""
    print("\n\nTesting conversation analysis...")
    
    analyzer = PatientSentimentAnalyzer()
    
    conversation = [
        "I'm really worried about my condition.",
        "The doctor said I'm doing well.",
        "I feel so anxious and stressed.",
        "Thank you for the support, I appreciate it."
    ]
    
    result = analyzer.analyze_conversation(conversation)
    print("Conversation Analysis Results:")
    print(generate_analysis_report(result))

if __name__ == "__main__":
    test_basic_sentiment_analysis()
    test_simple_function()
    test_conversation_analysis()
    print("\n=== All tests completed ===")