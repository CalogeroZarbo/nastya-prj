"""
Visualization utilities for patient progress data.
Generates charts and plots using matplotlib/plotly.
"""

from typing import Dict, List, Any
import pandas as pd


class PatientVisualizer:
    """Generates visualizations for patient health progress"""

    def plot_metric_trend(self, records: List[Dict], metric: str) -> Dict[str, Any]:
        """Return chart-ready data for a single metric over time"""
        if not records:
            return {}

        df = pd.DataFrame(records)
        if metric not in df.columns or 'timestamp' not in df.columns:
            return {}

        series = df[['timestamp', metric]].dropna()
        return {
            'labels': [str(t) for t in series['timestamp'].tolist()],
            'values': series[metric].tolist(),
            'metric': metric,
        }

    def generate_summary_chart(self, trends: Dict[str, Any]) -> Dict[str, Any]:
        """Return a summary bar-chart payload for all tracked metrics"""
        return {
            'metrics': list(trends.keys()),
            'latest_values': [v.get('latest', 0) for v in trends.values()],
            'changes': [v.get('change', 0) for v in trends.values()],
        }
