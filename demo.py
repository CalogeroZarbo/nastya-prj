"""
Demo script for the patient progress tracking system
"""

from main import PatientProgressTrackingSystem
from datetime import datetime, timedelta


def demo_system():
    """Demonstration of the progress tracking system"""
    
    print("=== AI-Driven Patient Progress Tracking System Demo ===")
    
    # Initialize system
    system = PatientProgressTrackingSystem()
    
    # Add a sample patient
    print("Adding sample patient...")
    patient = system.add_patient("P001", "John Doe")
    
    # Add sample health records
    print("Adding health records...")
    
    # Sample data with different metrics
    sample_records = [
        {
            "timestamp": datetime.now() - timedelta(days=30),
            "blood_pressure_systolic": 140,
            "blood_pressure_diastolic": 90,
            "heart_rate": 75,
            "weight": 80,
            "glucose_level": 110
        },
        {
            "timestamp": datetime.now() - timedelta(days=20),
            "blood_pressure_systolic": 135,
            "blood_pressure_diastolic": 85,
            "heart_rate": 72,
            "weight": 79,
            "glucose_level": 105
        },
        {
            "timestamp": datetime.now() - timedelta(days=10),
            "blood_pressure_systolic": 130,
            "blood_pressure_diastolic": 82,
            "heart_rate": 70,
            "weight": 78,
            "glucose_level": 100
        },
        {
            "timestamp": datetime.now(),
            "blood_pressure_systolic": 125,
            "blood_pressure_diastolic": 80,
            "heart_rate": 68,
            "weight": 77,
            "glucose_level": 95
        }
    ]
    
    # Add records to patient
    for record in sample_records:
        system.add_health_record("P001", record)
        
    # Generate analysis
    print("Generating progress analysis...")
    analysis = system.analyze_patient_progress("P001")
    
    # Print results
    print("\n=== ANALYSIS RESULTS ===")
    print(f"Patient: {analysis.get('patient_name', 'Unknown')}")
    print(f"Total Records: {analysis.get('total_records', 0)}")
    print("\nTrends:")
    for metric, trend_data in analysis.get('trends', {}).items():
        print(f"  {metric}: {trend_data.get('trend', 'N/A')}")
        
    print("\nInsights:")
    for insight in analysis.get('insights', [])[:5]:  # Show first 5 insights
        print(f"  - {insight.get('message', 'No message')}")
        
    print("\nRecommendations:")
    for rec in analysis.get('recommendations', [])[:3]:  # Show first 3 recommendations
        print(f"  - {rec.get('message', 'No message')}")
        
    # Generate dashboard
    print("\nGenerating dashboard...")
    dashboard = system.generate_dashboard("P001")
    
    # System summary
    print("\n=== SYSTEM SUMMARY ===")
    summary = system.get_system_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")
        
    print("\nDemo completed successfully!")


if __name__ == "__main__":
    # Run demo
    demo_system()