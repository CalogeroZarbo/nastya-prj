# Active Context

## Current state (2026-04-14)
The Flask web app is functional end-to-end:
- Login/logout works (`admin` / `admin`)
- Patients: list, add, view detail, edit
- Appointments: list, schedule, view detail, mark complete
- Treatment plans: list view
- Dashboard: patient summary with counts

## What was recently fixed (in this session)
- `app_simple.py` was a skeleton with no routes — all 13 routes implemented
- `Patient` model was missing 13 fields used by templates — all added
- `app.py` model stubs merged into `app_simple.py`
- `patient_form.html` and `patient_edit.html` were truncated (no submit buttons) — completed
- 3 missing templates created: `appointment_form.html`, `appointment_detail.html`, `treatment_plans.html`
- Static files created: `static/css/style.css`, `static/js/main.js`
- `PatientProgressTracker` added to `patient_data_model.py`
- `progress_analyzer.py` and `visualization.py` created (were missing, imported by `main.py`)
- `requirements.txt` updated to include Flask dependencies
- Entire Node.js/Express scaffolding removed (was unused)
- Stale SQLite DB deleted so schema is recreated fresh on next run

## Immediate priorities
- TreatmentPlan create UI (listing works, no way to add one via web)
- Session notes web UI
- ProgressTracking web UI (mood/anxiety/stress logging)
- Move SECRET_KEY out of source code

## Open questions
- Should sentiment analysis be integrated into the session notes workflow?
- Is role-based access (therapist vs admin) needed?
- Are the orphaned files (`app.py`, `app_temp.py`, `demo.py`, etc.) safe to delete?
