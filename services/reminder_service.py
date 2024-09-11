from models.reminder_model import Reminder
from models.medication_model import Medication
from database import db
from datetime import datetime

# Adds a new reminder for a specific medication
def add_reminder(user_id, medication_id, time_to_take):
    try:
        # Convert the time to take to a datetime object
        time_to_take_dt = datetime.strptime(time_to_take, '%Y-%m-%d %H:%M:%S')

        # Check if the medication exists and belongs to the user
        medication = Medication.query.filter_by(id=medication_id, user_id=user_id).first()
        if not medication:
            return False

        # Create the reminder entry
        new_reminder = Reminder(
            medication_id=medication_id,
            time_to_take=time_to_take_dt,
            taken=False
        )

        # Add the new reminder to the database
        db.session.add(new_reminder)
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error adding reminder: {str(e)}")
        return False

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
