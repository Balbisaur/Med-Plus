from flask import request, jsonify, Blueprint
from services.reminder_service import ReminderService, get_upcoming_reminders
from utils.jwt_utils import decode_token

# Adds a reminder for a specific medication
reminder_bp = Blueprint('reminder_bp', __name__)
reminder_service = ReminderService()

@reminder_bp.route('/reminders', methods=['POST'])
def add_reminder():
    data = request.json
    user_id = request.args.get('user_id')
    result = reminder_service.add_reminder(user_id, data)
    return jsonify(result), 201

@reminder_bp.route('/reminders', methods=['GET'])
def get_reminders():
    user_id = request.args.get('user_id')
    reminders = reminder_service.get_reminders(user_id)
    return jsonify([rem.to_dict() for rem in reminders]), 200

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
