from models.reminder_model import Reminder
from models.medication_model import Medication
from database import db
from datetime import datetime

# Adds a new reminder for a specific medication
class ReminderService:
    def add_reminder(self, user_id, data):
        reminder = Reminder(
            user_id=user_id,
            medication_id=data.get('medication_id'),
            time=data.get('time'),
            dosage=data.get('dosage')
        )
        db.session.add(reminder)
        db.session.commit()
        return {"id": reminder.id, "time": reminder.time, "dosage": reminder.dosage}

    def get_reminders(self, user_id):
        return Reminder.query.filter_by(user_id=user_id).all()

# Gets upcoming reminders for a specific user
def get_upcoming_reminders(user_id):
    try:
        # Join Reminder and Medication tables to fetch reminders and medication info for the user
        upcoming_reminders = db.session.query(Reminder, Medication).join(Medication).filter(
            Medication.user_id == user_id,
            Reminder.time_to_take > datetime.now(),
            Reminder.taken == False
        ).all()

        # Format the reminders for the response
        reminders_list = []
        for reminder, medication in upcoming_reminders:
            reminders_list.append({
                "medication_name": medication.name,
                "dosage": medication.dosage,
                "time_to_take": reminder.time_to_take.strftime('%Y-%m-%d %H:%M:%S'),
                "taken": reminder.taken
            })

        return reminders_list
    except Exception as e:
        print(f"Error fetching reminders: {str(e)}")
        return []

