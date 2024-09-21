from models.medication_model import Medication
from database import db

class MedicationService:
    def add_medication(self, user_id, data):
        medication = Medication(
            user_id=user_id,
            medication_name=data.get('medication_name'),
            dosage=data.get('dosage'),
            purpose=data.get('purpose'),
            side_effects=data.get('side_effects'),
            precautions=data.get('precautions'),
            warnings=data.get('warnings')
        )
        db.session.add(medication)
        db.session.commit()
        return {"id": medication.id, "medication_name": medication.medication_name, "dosage": medication.dosage}

    def get_medications(self, user_id):
        return Medication.query.filter_by(user_id=user_id).all()
