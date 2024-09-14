from database import db
from datetime import datetime

class Reminder(db.Model):
    __tablename__ = 'reminders'
    
    id = db.Column(db.Integer, primary_key=True)
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.id'), nullable=False)
    time_to_take = db.Column(db.DateTime, nullable=False)
    taken = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    dosage = db.Column(db.String(20), nullable=False)
    status = db.Column(db.string(50), nullable=False)

    def __init__(self, medication_id, time_to_take):
        self.medication_id = medication_id
        self.time_to_take = time_to_take
        self.taken = False
