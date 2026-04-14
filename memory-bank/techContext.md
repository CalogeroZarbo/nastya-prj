# Tech Context

## Stack
| Layer | Technology |
|---|---|
| Web framework | Flask 3.x |
| ORM | Flask-SQLAlchemy 3.x (SQLAlchemy 2.x API) |
| Auth | Flask-Login + werkzeug `generate_password_hash` / `check_password_hash` |
| Database | SQLite (`instance/session_tracking.db`) |
| Templates | Jinja2 via Flask, Bootstrap 5.3 CDN, Font Awesome 6 CDN, Chart.js CDN |
| Static assets | `static/css/style.css`, `static/js/main.js` (minimal, locally served) |
| AI/analysis | pandas, numpy, scikit-learn, matplotlib, seaborn, plotly, statsmodels, scipy |
| Sentiment NLP | nltk (VADER), textblob, transformers — all optional, graceful degradation |

## Entry point
```
python app_simple.py   →   http://localhost:5000
```
Default credentials: `admin` / `admin`

## Database models (all in `app_simple.py`)
- `User` — system users (role: admin/therapist/patient), hashed passwords
- `Patient` — full demographic + clinical profile (21 fields)
- `Appointment` — scheduled appointments linked to patient + therapist
- `Session` — therapy sessions, optionally linked to an appointment
- `TreatmentPlan` — goals/interventions linked to patient + therapist
- `ProgressTracking` — mood/anxiety/stress scores (1–10) per session

## AI/analysis modules (standalone, not wired to web app)
| File | Purpose |
|---|---|
| `sentiment_analysis.py` | Multi-approach NLP sentiment on session text (NLTK/TextBlob/Transformers) |
| `analysis_utils.py` | Formatting/reporting utilities for sentiment results |
| `patient_data_model.py` | `PatientData` + `PatientProgressTracker` classes |
| `health_metrics.py` | `HealthMetric` definitions + `COMMON_METRICS` registry |
| `progress_analyzer.py` | Trend analysis over patient records |
| `visualization.py` | Chart-data generation from trends |
| `main.py` | `PatientProgressTrackingSystem` — orchestrates the above |

## Orphaned / legacy files (safe to ignore or delete)
- `app.py`, `app_temp.py` — disconnected model stubs (already merged into `app_simple.py`)
- `demo.py`, `final_demo.py`, `sample_app.py` — demo scripts, not imported anywhere
- `simple_test.py`, `test_simple.py`, `test_sample.py`, `pytest_runner.py`, `test_sentiment_analysis.py` — incomplete test files

## Known gaps
- SECRET_KEY is hardcoded — move to env var before any shared deployment
- No CSRF protection on forms
- SQLite only — not suitable for multi-user production
- Session notes and ProgressTracking have no web UI
- TreatmentPlan create/edit UI not built
- Sentiment analysis not connected to the Flask app
