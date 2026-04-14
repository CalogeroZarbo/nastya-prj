"""
Progress Analyzer for AI-driven patient progress tracking.
Analyzes trends in patient health data and generates insights.
"""

from typing import Dict, List, Any
import pandas as pd
import numpy as np


class ProgressAnalyzer:
    """Analyzes patient health data to detect trends and generate insights"""

    def analyze_trends(self, records: List[Dict]) -> Dict[str, Any]:
        """Analyze trends across all numeric metrics in the records"""
        if not records:
            return {}

        df = pd.DataFrame(records)
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        trends = {}
        for col in numeric_cols:
            series = df[col].dropna()
            if len(series) < 2:
                continue
            change = float(series.iloc[-1] - series.iloc[0])
            pct_change = (change / float(series.iloc[0])) * 100 if series.iloc[0] != 0 else 0
            trends[col] = {
                'mean': float(series.mean()),
                'std': float(series.std()),
                'min': float(series.min()),
                'max': float(series.max()),
                'latest': float(series.iloc[-1]),
                'change': change,
                'pct_change': pct_change,
            }
        return trends

    def generate_insights(self, trends: Dict[str, Any]) -> List[str]:
        """Generate human-readable insights from trend data"""
        insights = []
        for metric, data in trends.items():
            direction = 'increased' if data['change'] > 0 else 'decreased'
            insights.append(
                f"{metric} has {direction} by {abs(data['pct_change']):.1f}% "
                f"(current: {data['latest']:.1f})"
            )
        return insights
