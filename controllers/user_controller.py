from flask import Blueprint, request, jsonify
from services.user_service import UserService
from services.qr_code_service import generate_qr_code, decode_qr_code
from services.user_service import UserService


user_bp = Blueprint('user_bp', __name__)

# Initialize the user service
user_service = UserService()

# Define the login route
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Call the login function in the UserService
    result = user_service.login(username, password)
    
    if result:
        return jsonify(result), 200
    return jsonify({'error': 'Invalid credentials'}), 401

# Example route to get all medications for a user
@user_bp.route('/users/<int:user_id>/medications', methods=['GET'])
def get_medications(user_id):
    medications = user_service.get_all_medications(user_id)
    
    if medications:
        return jsonify([med.to_dict() for med in medications]), 200
    return jsonify({'error': 'No medications found'}), 404
