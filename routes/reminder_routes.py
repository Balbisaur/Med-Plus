from flask import Blueprint, request, jsonify
from services.reminder_service import ReminderService

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
    result = reminder_service.get_reminders(user_id)
    return jsonify(result), 200
