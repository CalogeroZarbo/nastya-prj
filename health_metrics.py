"""
Health Metrics definitions for patient progress tracking
"""

from typing import Dict, List, Optional
import pandas as pd
import numpy as np


class HealthMetric:
    """Represents a specific health metric tracked over time"""
    
    def __init__(self, name: str, unit: str, target_value: float = None):
        self.name = name
        self.unit = unit
        self.target_value = target_value
        
    def __repr__(self):
        return f"HealthMetric(name='{self.name}', unit='{self.unit}', target='{self.target_value}')"


class HealthMetricRegistry:
    """Registry for health metrics"""
    
    def __init__(self):
        self.metrics = {}
        
    def register_metric(self, metric: HealthMetric):
        """Register a health metric"""
        self.metrics[metric.name] = metric
        
    def get_metric(self, name: str) -> Optional[HealthMetric]:
        """Get a health metric by name"""
        return self.metrics.get(name)
        
    def get_all_metrics(self) -> List[HealthMetric]:
        """Get all registered metrics"""
        return list(self.metrics.values())


# Common health metrics
COMMON_METRICS = [
    HealthMetric("blood_pressure_systolic", "mmHg", 120),
    HealthMetric("blood_pressure_diastolic", "mmHg", 80),
    HealthMetric("heart_rate", "bpm", 70),
    HealthMetric("weight", "kg", 70),
    HealthMetric("height", "cm", 170),
    HealthMetric("bmi", "kg/m2", 22),
    HealthMetric("glucose_level", "mg/dL", 90),
    HealthMetric("cholesterol_total", "mg/dL", 150),
    HealthMetric("oxygen_saturation", "%", 98),
    HealthMetric("temperature", "°C", 37)
]