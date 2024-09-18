from database import db


class Medication(db.Model):
    __tablename__ = 'medications'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)
    purpose = db.Column(db.String(255))
    side_effects = db.Column(db.String(255))
    precautions = db.Column(db.String(255))
    warnings = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    reminders = db.relationship('Reminder', backref='medication', lazy=True)
    prescriptions = db.relationship('Prescription', backref='medication', lazy=True)



    
    def __repr__(self):
        return f'<Medication {self.name}>'

