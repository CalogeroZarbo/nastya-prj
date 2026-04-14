"""
Patient Data Model for AI-driven Progress Tracking
This module defines the data structures and models for patient data analysis.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class PatientData:
    """Represents a patient's longitudinal health data"""
    
    def __init__(self, patient_id: str, patient_name: str = None):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.health_records = []
        self.data_history = []
        
    def add_health_record(self, record: Dict):
        """Add a health record for this patient"""
        record['timestamp'] = datetime.now()
        self.health_records.append(record)
        self.data_history.append(record)
        
    def get_records_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Dict]:
        """Get health records within a specific date range"""
        return [record for record in self.health_records 
                if start_date <= record.get('timestamp', datetime.min) <= end_date]
                
    def get_all_records(self) -> List[Dict]:
        """Get all health records"""
        return self.health_records.copy()


class PatientProgressTracker:
    """Tracks progress for multiple patients across registered health metrics"""

    def __init__(self):
        self.patients: Dict[str, PatientData] = {}
        self.health_metrics: Dict[str, object] = {}

    def register_patient(self, patient: PatientData):
        self.patients[patient.patient_id] = patient

    def add_health_metric(self, metric):
        self.health_metrics[metric.name] = metric

    def get_patient_progress(self, patient_id: str) -> Dict:
        if patient_id not in self.patients:
            return {'error': f'Patient {patient_id} not found'}

        patient = self.patients[patient_id]
        records = patient.get_all_records()

        if not records:
            return {
                'patient_id': patient_id,
                'patient_name': patient.patient_name,
                'total_records': 0,
                'trends': {},
                'insights': [],
                'recommendations': [],
                'timestamp': datetime.now().isoformat(),
            }

        # Simple trend analysis per metric
        import pandas as pd
        df = pd.DataFrame(records)
        trends: Dict[str, Dict] = {}
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        for col in numeric_cols:
            if col in self.health_metrics:
                series = df[col].dropna()
                if len(series) >= 2:
                    delta = float(series.iloc[-1] - series.iloc[0])
                    trends[col] = {
                        'latest': float(series.iloc[-1]),
                        'change': delta,
                        'direction': 'improving' if delta <= 0 else 'worsening',
                    }

        return {
            'patient_id': patient_id,
            'patient_name': patient.patient_name,
            'total_records': len(records),
            'trends': trends,
            'insights': [f'{k} has changed by {v["change"]:.2f}' for k, v in trends.items()],
            'recommendations': [],
            'timestamp': datetime.now().isoformat(),
        }