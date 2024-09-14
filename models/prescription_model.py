from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import db  

class Prescription(db.Model):
    __tablename__ = 'prescriptions'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(Integer, ForeignKey('users.id'), nullable=False)
    medication_id = db.Column(Integer, ForeignKey('medications.id'), nullable=False)
    prescribed_by = db.Column(db.String(50), unique=True, nullable=False)  
    instructions = db.Column(String(255), nullable=True)

    # Relationships 
    user = relationship("User", back_populates="prescriptions")
    medication = relationship("Medication", back_populates="prescriptions")
    doctor = relationship("Doctor", back_populates="prescriptions")

    def __repr__(self):
        return f"<Prescription(user_id={self.user_id}, medication_id={self.medication_id}, prescribed_by={self.prescribed_by})>"
