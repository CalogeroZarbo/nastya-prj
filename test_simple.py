#!/usr/bin/env python3
"""
Simple test for the AI-powered treatment recommendation system
"""

import sys
sys.path.insert(0, '.')

from core.models import Patient
from core.recommendation_engine import RecommendationEngine

def test_basic_functionality():
    """Test basic functionality"""
    print("Testing AI Treatment Recommendation System")
    print("=" * 40)
    
    # Create recommendation engine
    engine = RecommendationEngine()
    print("✓ Recommendation engine created successfully")
    
    # Create a sample patient
    patient = Patient(
        patient_id="P001",
        name="John Smith",
        age=45,
        gender="male",
        medical_history=["hypertension", "diabetes"],
        current_symptoms=["headache", "fatigue"]
    )
    
    print("✓ Patient created successfully")
    print(f"Patient: {patient.name}")
    
    # Add patient to engine
    engine.add_patient(patient)
    print("✓ Patient added to system")
    
    print("All basic tests passed!")
    return True

if __name__ == "__main__":
    test_basic_functionality()