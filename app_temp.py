class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    therapist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    appointment_type = db.Column(db.String(100), nullable=False)  # 'initial', 'follow-up', 'session'
    status = db.Column(db.String(50), default='scheduled')  # 'scheduled', 'completed', 'cancelled'
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    patient = db.relationship('Patient', backref='appointments')
    therapist = db.relationship('User', backref='appointments')

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    therapist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=True)
    session_date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer)  # in minutes
    session_notes = db.Column(db.Text)
    progress_updates = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    patient = db.relationship('Patient', backref='sessions')
    therapist = db.relationship('User', backref='sessions')
    appointment = db.relationship('Appointment', backref='session')

class TreatmentPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    therapist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(50), default='active')  # 'active', 'completed', 'on-hold'
    goals = db.Column(db.Text)  # JSON string of goals
    interventions = db.Column(db.Text)  # JSON string of interventions
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    patient = db.relationship('Patient', backref='treatment_plans')
    therapist = db.relationship('User', backref='treatment_plans')

class ProgressTracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=True)
    date_recorded = db.Column(db.DateTime, default=datetime.utcnow)
    mood_score = db.Column(db.Integer)  # 1-10 scale
    anxiety_score = db.Column(db.Integer)  # 1-10 scale
    stress_score = db.Column(db.Integer)  # 1-10 scale
    notes = db.Column(db.Text)
    
    # Relationships
    patient = db.relationship('Patient', backref='progress_trackings')
    session = db.relationship('Session', backref='progress_tracking')