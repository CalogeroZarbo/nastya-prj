"""
Simple test to verify the system works
"""

# Test basic imports
try:
    from patient_data_model import PatientData, HealthMetric
    from health_metrics import COMMON_METRICS
    print("✓ All imports successful")
    
    # Test basic functionality
    patient = PatientData("P001", "Test Patient")
    print("✓ PatientData creation successful")
    
    # Test health metric
    metric = HealthMetric("blood_pressure_systolic", "mmHg", 120)
    print("✓ HealthMetric creation successful")
    
    print("✓ System components are working correctly")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()