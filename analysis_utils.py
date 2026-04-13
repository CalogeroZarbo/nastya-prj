"""
Utility functions for advanced sentiment analysis
"""

from typing import Dict, List, Any
import json

def format_analysis_output(result: Any, pretty_print: bool = True) -> str:
    """
    Format sentiment analysis results for display
    
    Args:
        result: Analysis result object
        pretty_print: If True, return formatted JSON string
        
    Returns:
        Formatted string representation of the analysis
    """
    if hasattr(result, '__dict__'):
        # It's a SentimentResult object
        data = {
            'text': result.text,
            'polarity': result.polarity.value,
            'confidence': result.confidence,
            'sentiment_score': result.sentiment_score,
            'emotions': result.emotions,
            'mood_patterns': result.mood_patterns,
            'psychological_state': result.psychological_state,
            'metadata': result.analysis_metadata
        }
    else:
        # It's already a dict
        data = result
    
    if pretty_print:
        return json.dumps(data, indent=2, ensure_ascii=False)
    else:
        return json.dumps(data, ensure_ascii=False)

def generate_analysis_report(results: Dict[str, Any]) -> str:
    """
    Generate a comprehensive analysis report
    
    Args:
        results: Analysis results dictionary
        
    Returns:
        Formatted report string
    """
    report = []
    report.append("=== PATIENT SENTIMENT ANALYSIS REPORT ===\n")
    
    # Overall sentiment
    if 'overall_sentiment' in results:
        sentiment = results['overall_sentiment']
        report.append(f"Overall Sentiment: {sentiment['polarity'].upper()}")
        report.append(f"Sentiment Score: {sentiment['score']:.3f}")
        report.append(f"Confidence: {sentiment['confidence']:.3f}\n")
    
    # Emotional analysis
    if 'emotional_analysis' in results:
        emotions = results['emotional_analysis']['emotions']
        patterns = results['emotional_analysis']['mood_patterns']
        state = results['emotional_analysis']['psychological_state']
        
        report.append("Emotional Analysis:")
        if emotions:
            report.append("  Detected Emotions:")
            for emotion in emotions:
                report.append(f"    - {emotion['emotion'].title()}: {emotion['confidence']:.2f}")
        else:
            report.append("  No specific emotions detected")
        
        if patterns:
            report.append("  Mood Patterns Detected:")
            for pattern in patterns:
                report.append(f"    - {pattern.replace('-', ' ').title()}")
        else:
            report.append("  No specific mood patterns detected")
        
        report.append(f"  Psychological State: {state.replace('-', ' ').title()}\n")
    
    return "\n".join(report)