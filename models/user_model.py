from database import db
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)# 'child', 'user', or 'caregiver'
    email = db.Column(db.String(50), nullable=False)  

    medications = db.relationship('Medication', backref='owner', lazy=True)
    prescriptions = db.relationship('Prescription', backref='user', lazy=True)
    doctor = db.relationship('Doctor', backref='user', lazy=True)
    reminders = db.relationship('Reminder', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
