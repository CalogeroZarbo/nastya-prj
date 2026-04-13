"""
AI-driven Patient Progress Tracking System
Main application module for tracking patient health data over time
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any
import json

# Import our modules
from patient_data_model import PatientData, PatientProgressTracker
from health_metrics import HealthMetric, COMMON_METRICS
from progress_analyzer import ProgressAnalyzer
from visualization import PatientVisualizer


class PatientProgressTrackingSystem:
    """Main system for AI-driven patient progress tracking"""
    
    def __init__(self):
        self.tracker = PatientProgressTracker()
        self.analyzer = ProgressAnalyzer()
        self.visualizer = PatientVisualizer()
        
        # Register common metrics
        for metric in COMMON_METRICS:
            self.tracker.add_health_metric(metric)
            
    def add_patient(self, patient_id: str, patient_name: str = None) -> PatientData:
        """Add a new patient to the system"""
        patient = PatientData(patient_id, patient_name)
        self.tracker.register_patient(patient)
        return patient
        
    def add_health_record(self, patient_id: str, record: Dict) -> bool:
        """Add a health record for a patient"""
        if patient_id in self.tracker.patients:
            self.tracker.patients[patient_id].add_health_record(record)
            return True
        return False
        
    def analyze_patient_progress(self, patient_id: str) -> Dict[str, Any]:
        """Analyze progress for a specific patient"""
        return self.tracker.get_patient_progress(patient_id)
        
    def generate_dashboard(self, patient_id: str) -> Dict[str, Any]:
        """Generate comprehensive dashboard for patient progress"""
        progress_data = self.analyze_patient_progress(patient_id)
        
        if 'error' in progress_data:
            return progress_data
            
        # Format data for dashboard
        dashboard_data = {
            'patient_id': progress_data['patient_id'],
            'patient_name': progress_data.get('patient_name', 'Unknown'),
            'analysis_date': progress_data.get('timestamp', datetime.now().isoformat()),
            'summary': {
                'total_records': progress_data.get('total_records', 0),
                'trend_metrics': len(progress_data.get('trends', {})),
                'insights_count': len(progress_data.get('insights', [])),
                'recommendations_count': len(progress_data.get('recommendations', []))
            },
            'trends': progress_data.get('trends', {}),
            'insights': progress_data.get('insights', []),
            'recommendations': progress_data.get('recommendations', [])
        }
        
        return dashboard_data
        
    def get_system_summary(self) -> Dict[str, Any]:
        """Get summary of the entire system"""
        return {
            'total_patients': len(self.tracker.patients),
            'registered_metrics': len(self.tracker.health_metrics),
            'timestamp': datetime.now().isoformat()
        }