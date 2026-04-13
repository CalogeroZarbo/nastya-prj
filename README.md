# Patient Data Management System

A secure patient data management system for psychological information with the following features:

## Features
- **User Authentication**: Secure login system with role-based access control
- **Patient Profiles**: Comprehensive patient information management
- **Medical History**: Detailed medical and psychological history tracking
- **Demographic Information**: Complete patient demographic data
- **Data Entry Forms**: User-friendly forms with data validation
- **Secure Data Storage**: Encrypted storage for sensitive psychological information
- **Responsive Interface**: Bootstrap-based responsive web interface

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install flask flask-sqlalchemy flask-login bcrypt
   ```
3. Run the application:
   ```
   python app.py
   ```

## Usage
- Default admin user: username: `admin`, password: `admin123`
- Access the application at `http://localhost:5000`

## Database
- Uses SQLite database (patient_data.db)
- Automatically creates database and default admin user on startup

## Security Features
- Password encryption using bcrypt
- Secure session management
- Data validation and sanitization
- Role-based access control