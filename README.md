Medication Reminder Application
Overview
This Medication Reminder Application is a full-stack system designed to manage medication schedules, user profiles, and prescription data. The backend, built with Flask and MySQL, allows users to log in (including child, user, and caregiver roles), view upcoming medication reminders, and add medications to their profiles using QR codes. The system includes pages to view detailed medication information, manage prescriptions, and set reminders.

Features
User Roles: Login functionality for three user types: Child, User, and Caregiver.
Upcoming Medications: A list of upcoming scheduled medication reminders set by the user.
Medication Details: A page displaying medication purpose, dosage, side effects, precautions, and warnings.
QR Code Integration: Users can scan QR codes to automatically add medications to their profiles and routines.
Prescription Management: A page where users can see added medications and their instructions.
Reminders: A page displaying the medication name, dosage, and time reminders.
Custom Error Handling: Backend returns JSON error responses in case of issues, preventing frontend errors.
Project Structure
bash
Copy code
.
├── app.py                   # Main Flask application file
├── database.py              # Database connection and session setup
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── static/
│   └── swagger.yaml         # API documentation using OpenAPI/Swagger
├── controllers/
│   ├── user_controller.py   # Controller for user-related routes
│   ├── medication_controller.py # Controller for medication routes
│   └── reminder_controller.py   # Controller for reminder-related routes
├── models/
│   ├── user_model.py        # User model definition
│   ├── prescription_model.py# Prescription model definition
│   └── reminder_model.py    # Reminder model definition
├── services/
│   ├── user_service.py      # Business logic for user management
│   ├── medication_service.py# Business logic for medication management
│   └── reminder_service.py  # Business logic for reminders
├── utils/
│   ├── jwt_utils.py         # JWT encoding/decoding utilities
│   └── qr_code_service.py   # QR code generation and decoding
Installation and Setup
Prerequisites
Python 3.x
MySQL Workbench
Flask
