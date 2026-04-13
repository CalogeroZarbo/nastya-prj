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