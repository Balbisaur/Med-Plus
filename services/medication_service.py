from models.medication_model import Medication
from database import db

def add_medication(data):
    medication = Medication(
        name=data['name'],
        dosage=data['dosage'],
        purpose=data['purpose'],
        side_effects=data.get('side_effects'),
        precautions=data.get('precautions'),
        warnings=data.get('warnings'),
        user_id=data['user_id']
    )
    db.session.add(medication)
    db.session.commit()
    return True

def get_medication_info(med_id):
    return Medication.query.filter_by(id=med_id).first()
