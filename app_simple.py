from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime, date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'session-tracking-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///session_tracking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# ── Models ────────────────────────────────────────────────────────────────────

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), nullable=False)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(30))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    address = db.Column(db.Text)
    status = db.Column(db.String(50), default='active')
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    emergency_contact_name = db.Column(db.String(100))
    emergency_contact_phone = db.Column(db.String(20))
    medical_history = db.Column(db.Text)
    psychological_history = db.Column(db.Text)
    current_medications = db.Column(db.Text)
    allergies = db.Column(db.Text)
    previous_treatments = db.Column(db.Text)
    personality_traits = db.Column(db.Text)
    mental_status = db.Column(db.Text)
    diagnosis = db.Column(db.Text)
    treatment_plan = db.Column(db.Text)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    therapist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    appointment_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='scheduled')
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    patient = db.relationship('Patient', backref='appointments')
    therapist = db.relationship('User', backref='appointments')


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    therapist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=True)
    session_date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer)
    session_notes = db.Column(db.Text)
    progress_updates = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
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
    status = db.Column(db.String(50), default='active')
    goals = db.Column(db.Text)
    interventions = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    patient = db.relationship('Patient', backref='treatment_plans')
    therapist = db.relationship('User', backref='treatment_plans')


class ProgressTracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=True)
    date_recorded = db.Column(db.DateTime, default=datetime.utcnow)
    mood_score = db.Column(db.Integer)
    anxiety_score = db.Column(db.Integer)
    stress_score = db.Column(db.Integer)
    notes = db.Column(db.Text)
    patient = db.relationship('Patient', backref='progress_trackings')
    session = db.relationship('Session', backref='progress_tracking')


# ── Setup ─────────────────────────────────────────────────────────────────────

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        admin = User(
            username='admin',
            email='admin@example.com',
            password=generate_password_hash('admin'),
            role='admin',
        )
        db.session.add(admin)
        db.session.commit()
    print("Session tracking system initialized successfully!")


# ── Auth ──────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return redirect(url_for('dashboard'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# ── Dashboard ─────────────────────────────────────────────────────────────────

@app.route('/dashboard')
@login_required
def dashboard():
    patients = Patient.query.order_by(Patient.created_at.desc()).all()
    return render_template('dashboard.html', patients=patients)


# ── Patients ──────────────────────────────────────────────────────────────────

@app.route('/patients')
@login_required
def patients():
    all_patients = Patient.query.order_by(Patient.last_name).all()
    return render_template('patients.html', patients=all_patients)


@app.route('/patients/add', methods=['GET', 'POST'])
@login_required
def add_patient():
    if request.method == 'POST':
        dob = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()
        patient = Patient(
            first_name=request.form['first_name'].strip(),
            last_name=request.form['last_name'].strip(),
            date_of_birth=dob,
            gender=request.form.get('gender'),
            phone=request.form.get('phone', '').strip() or None,
            email=request.form.get('email', '').strip() or None,
            address=request.form.get('address', '').strip() or None,
        )
        db.session.add(patient)
        db.session.commit()
        flash('Patient added successfully')
        return redirect(url_for('patients'))
    return render_template('patient_form.html')


@app.route('/patients/<int:patient_id>')
@login_required
def patient_detail(patient_id):
    patient = db.session.get(Patient, patient_id)
    if patient is None:
        flash('Patient not found')
        return redirect(url_for('patients'))
    return render_template('patient_detail.html', patient=patient)


@app.route('/patients/<int:patient_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_patient(patient_id):
    patient = db.session.get(Patient, patient_id)
    if patient is None:
        flash('Patient not found')
        return redirect(url_for('patients'))
    if request.method == 'POST':
        patient.first_name = request.form['first_name'].strip()
        patient.last_name = request.form['last_name'].strip()
        patient.date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()
        patient.gender = request.form.get('gender')
        patient.phone = request.form.get('phone', '').strip() or None
        patient.email = request.form.get('email', '').strip() or None
        patient.address = request.form.get('address', '').strip() or None
        db.session.commit()
        flash('Patient updated successfully')
        return redirect(url_for('patient_detail', patient_id=patient.id))
    return render_template('patient_edit.html', patient=patient)


# ── Appointments ──────────────────────────────────────────────────────────────

@app.route('/appointments')
@login_required
def appointments():
    all_appointments = Appointment.query.order_by(Appointment.appointment_date.desc()).all()
    return render_template('appointments.html', appointments=all_appointments)


@app.route('/appointments/add', methods=['GET', 'POST'])
@login_required
def add_appointment():
    if request.method == 'POST':
        appt_date = datetime.strptime(request.form['appointment_date'], '%Y-%m-%dT%H:%M')
        appointment = Appointment(
            patient_id=int(request.form['patient_id']),
            therapist_id=current_user.id,
            appointment_date=appt_date,
            appointment_type=request.form['appointment_type'],
            notes=request.form.get('notes', '').strip() or None,
        )
        db.session.add(appointment)
        db.session.commit()
        flash('Appointment scheduled successfully')
        return redirect(url_for('appointments'))
    all_patients = Patient.query.order_by(Patient.last_name).all()
    return render_template('appointment_form.html', patients=all_patients)


@app.route('/appointments/<int:appointment_id>')
@login_required
def appointment_detail(appointment_id):
    appointment = db.session.get(Appointment, appointment_id)
    if appointment is None:
        flash('Appointment not found')
        return redirect(url_for('appointments'))
    return render_template('appointment_detail.html', appointment=appointment)


@app.route('/appointments/<int:appointment_id>/complete')
@login_required
def complete_appointment(appointment_id):
    appointment = db.session.get(Appointment, appointment_id)
    if appointment:
        appointment.status = 'completed'
        db.session.commit()
        flash('Appointment marked as completed')
    return redirect(url_for('appointments'))


# ── Treatment Plans ───────────────────────────────────────────────────────────

@app.route('/treatment_plans')
@login_required
def treatment_plans():
    plans = TreatmentPlan.query.order_by(TreatmentPlan.created_at.desc()).all()
    return render_template('treatment_plans.html', plans=plans)


# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Starting session tracking system...")
    app.run(debug=True, host='0.0.0.0', port=5000)
