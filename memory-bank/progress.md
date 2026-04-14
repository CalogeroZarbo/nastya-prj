# Progress

## Done
- [x] Flask app with full model set (User, Patient, Appointment, Session, TreatmentPlan, ProgressTracking)
- [x] All web routes (login, dashboard, patients CRUD, appointments CRUD, treatment plans list)
- [x] Templates complete and consistent (no broken url_for calls)
- [x] Static files (CSS, JS)
- [x] Password hashing with werkzeug
- [x] AI analysis module skeleton (sentiment_analysis, patient_data_model, health_metrics, progress_analyzer, visualization, main)
- [x] requirements.txt includes all Flask + data science dependencies
- [x] Node.js/Express scaffolding removed

## Backlog
- [ ] TreatmentPlan create/edit UI
- [ ] Session notes web UI (record notes after appointment completion)
- [ ] ProgressTracking web UI (log mood/anxiety/stress scores per session)
- [ ] Connect sentiment analysis to session notes
- [ ] Move SECRET_KEY to environment variable (python-dotenv)
- [ ] Add CSRF protection (flask-wtf already installed)
- [ ] Clean up orphaned files: `app.py`, `app_temp.py`, `demo.py`, `final_demo.py`, `sample_app.py`
- [ ] Add routes for `patient_dashboard.html` and `therapist_dashboard.html` templates
- [ ] Role-based access control (admin vs therapist)
- [ ] Proper Flask test suite
