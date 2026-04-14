# Project Brief

## What it is
A **session tracking system for mental health care professionals** (therapists, admins). It lets practitioners manage patients, schedule appointments, record session notes, track patient progress over time, and maintain treatment plans.

## Purpose
Provide therapists with a centralised web tool to track the full lifecycle of patient care: intake → appointments → sessions → progress monitoring → treatment planning.

## Core features
| Feature | Status |
|---|---|
| Patient management (add, view, edit) | Working |
| Appointment scheduling & completion | Working |
| Treatment plan listing | Working (create UI not yet built) |
| Session notes | Model exists, no UI yet |
| Progress tracking (mood/anxiety/stress scores) | Model exists, no UI yet |
| AI sentiment analysis on session transcripts | Module exists (`sentiment_analysis.py`), not wired to web app |
| Health metric trend analysis | Module exists (`main.py`, `patient_data_model.py`), not wired to web app |

## Target users
Mental health practitioners: therapists, clinical administrators.

## CRITICAL — Sensitive domain constraints
This system handles **clinical and psychological patient data**, including:
- Full patient PII (name, DOB, address, phone, email)
- Medical and psychological history
- Diagnoses, current medications, allergies
- Mood, anxiety, and stress scores
- Session transcripts (if sentiment analysis is used)
- Suicidal ideation keyword detection (built into `sentiment_analysis.py`)

**These constraints apply at all times:**
- Never log, print, or expose patient PII in plaintext outside the app context
- Never hardcode patient data, test data with real-looking PII, or clinical details in source files
- Treat any text field that could contain patient communication as sensitive
- The `suicidal` keyword group in `sentiment_analysis.py` is a clinical safety signal — any changes to it require explicit user approval
- Do not add analytics, telemetry, or external HTTP calls that could leak patient data
