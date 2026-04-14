# System Patterns

## Data flow
```
Browser → Flask route (app_simple.py)
         → db.session.get() / Model.query.order_by()
         → Jinja2 template (templates/)
         → Bootstrap 5 HTML response
```
Forms POST to the same URL as the GET; route handles both with `if request.method == 'POST'`.

## Route naming conventions
| Pattern | Example |
|---|---|
| List view | `@app.route('/patients')` → `def patients()` |
| Add form | `@app.route('/patients/add', methods=['GET','POST'])` → `def add_patient()` |
| Detail | `@app.route('/patients/<int:patient_id>')` → `def patient_detail(patient_id)` |
| Edit form | `@app.route('/patients/<int:patient_id>/edit', ...)` → `def edit_patient(patient_id)` |
| Action | `@app.route('/appointments/<int:appointment_id>/complete')` |

**url_for rule:** always pass named parameter (`patient_id=x`, `appointment_id=x`), never bare `id=x`.

## SQLAlchemy style
```python
# Use (SQLAlchemy 2.x)
db.session.get(Patient, patient_id)

# Avoid (legacy 1.x)
Patient.query.get(patient_id)
```

## Flash messages
All user feedback via `flash('message')` + `{% with messages %}` block in `base.html`. Auto-dismiss after 4s via `static/js/main.js`.

## Auth pattern
All non-auth routes decorated with `@login_required`. Unauthenticated → redirect to `/login`. Passwords verified with `check_password_hash`.

## Template inheritance
All pages `{% extends "base.html" %}` with two blocks: `{% block title %}` and `{% block content %}`.

## Coding style (observed in codebase)
- snake_case everywhere
- Type hints in analysis modules (`sentiment_analysis.py`, `patient_data_model.py`, `progress_analyzer.py`)
- Docstrings with Args/Returns in public functions of analysis modules
- Section dividers `# ── Section ──` in `app_simple.py`
- Inline enum comments on model columns (e.g. `# 'active', 'completed'`)
- Strip whitespace + coerce empty string to `None` before saving form data
- Optional dependencies wrapped in try/except with boolean availability flags

## Adding a new feature — checklist
1. Add model column(s) to `app_simple.py` if needed
2. Delete `instance/session_tracking.db` to let SQLAlchemy recreate the schema
3. Add route(s) following the naming convention above
4. Create template(s) extending `base.html`
5. Add nav links to `templates/base.html` if needed
6. Update `memory-bank/activeContext.md` and `memory-bank/progress.md`
