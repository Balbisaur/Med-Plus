from flask import request, jsonify
from services.reminder_service import add_reminder, get_upcoming_reminders
from utils.jwt_utils import decode_token

# Adds a reminder for a specific medication
def add_reminder_route():
    try:
        data = request.get_json()
        # Extract token from headers to identify user
        token = request.headers.get('Authorization').split(" ")[1]
        user_id = decode_token(token)['user_id']

        medication_id = data.get('medication_id')
        time_to_take = data.get('time_to_take')

        # Validate request
        if not medication_id or not time_to_take:
            return jsonify({"message": "Missing medication_id or time_to_take"}), 400

        # Add the reminder using service
        if add_reminder(user_id, medication_id, time_to_take):
            return jsonify({"message": "Reminder added successfully!"}), 201
        else:
            return jsonify({"message": "Failed to add reminder"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Gets the upcoming reminders for the logged-in user
def get_upcoming_reminders_route():
    try:
        # Extract token from headers
        token = request.headers.get('Authorization').split(" ")[1]
        payload = decode_token(token)

        if payload is None:
            return jsonify({"message": "Unauthorized"}), 401
        
        user_id = payload['user_id']

        # Fetch upcoming reminders for the user
        reminders = get_upcoming_reminders(user_id)
        
        if reminders:
            return jsonify(reminders), 200
        else:
            return jsonify({"message": "No upcoming reminders found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500
