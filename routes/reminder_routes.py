from flask import Blueprint
from controllers.reminder_controller import add_reminder_route, get_upcoming_reminders_route

reminder_bp = Blueprint('reminder', __name__)

# Route to add a reminder for a medication
@reminder_bp.route('/reminder/add', methods=['POST'])
def add_reminder():
    return add_reminder_route()

# Route to get upcoming reminders for the logged-in user
@reminder_bp.route('/reminders/upcoming', methods=['GET'])
def get_upcoming_reminders():
    return get_upcoming_reminders_route()
