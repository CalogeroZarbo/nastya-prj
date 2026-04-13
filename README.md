# Session Tracking System

A comprehensive session tracking system for mental health care professionals with features including appointment scheduling, session notes, progress tracking, and treatment plan management.

## Features Implemented

### 1. Appointment Scheduling
- Schedule appointments for patients
- Track appointment types (initial, follow-up, session)
- Manage appointment status (scheduled, completed, cancelled)
- View upcoming appointments for therapists

### 2. Session Notes
- Record detailed session notes
- Track progress updates during sessions
- Link sessions to specific appointments
- Maintain session history

### 3. Progress Tracking
- Mood score tracking (1-10 scale)
- Anxiety score tracking (1-10 scale)
- Stress score tracking (1-10 scale)
- Custom notes for progress tracking
- Visual dashboards for patient progress

### 4. Treatment Plan Management
- Create and manage treatment plans
- Define goals and interventions
- Track plan status (active, completed, on-hold)
- Link plans to specific patients

### 5. Visual Dashboards
- Patient progress over time visualizations
- Therapist dashboard with overview statistics
- Charts and graphs for tracking patient improvement
- Upcoming appointment management

## Technical Components

### Database Models
- **User**: System users (admins, therapists, patients)
- **Patient**: Patient information and records
- **Appointment**: Scheduled appointments
- **Session**: Individual therapy sessions
- **TreatmentPlan**: Long-term treatment plans
- **ProgressTracking**: Patient progress data

### Technologies Used
- Flask (Web Framework)
- Flask-SQLAlchemy (Database ORM)
- Flask-Login (Authentication)
- SQLite (Database)
- Bootstrap (Frontend Styling)
- Chart.js (Data Visualization)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Access at `http://localhost:5000`

## Usage

### Login Credentials
- Username: `admin`
- Password: `admin`

### Features Accessible
- **Dashboard**: Overview of system
- **Patients**: Manage patient records
- **Appointments**: Schedule and manage appointments
- **Treatment Plans**: Create and manage treatment plans
- **Progress Tracking**: View patient progress over time

## Project Structure

```
session-tracking-system/
├── app.py                 # Main application
├── requirements.txt       # Dependencies
├── templates/             # HTML Templates
│   ├── base.html
│   ├── login.html
│   ├── therapist_dashboard.html
│   ├── patient_dashboard.html
│   ├── patients.html
│   └── appointments.html
├── static/                # Static files (CSS, JS, Images)
│   ├── css/
│   └── js/
└── session_tracking.db    # SQLite database
```

## Future Enhancements
- Secure password hashing
- Email notifications
- Mobile application support
- Advanced analytics and reporting
- Integration with electronic health records (EHR)
- Multi-language support
- Export functionality for reports