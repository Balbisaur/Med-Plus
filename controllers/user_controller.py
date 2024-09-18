from flask import Blueprint, request, jsonify
from services.user_service import UserService
from utils.jwt_utils import decode_token

# Define the blueprint for user-related routes
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

# Define the user registration route
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    role = data.get('role', 'user')  # Default to 'user' role if not provided

    try:
        new_user = user_service.create_user(username, password, email, role)
        return jsonify({'id': new_user.id, 'username': new_user.username}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Define the route to get a user's information
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        }), 200
    return jsonify({'error': 'User not found'}), 404

# Define the route to update user information
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = user_service.update_user(user_id, data)
    
    if updated_user:
        return jsonify({
            'id': updated_user.id,
            'username': updated_user.username,
            'email': updated_user.email,
            'role': updated_user.role
        }), 200
    return jsonify({'error': 'User not found or update failed'}), 404

# Define the route to delete a user
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = user_service.delete_user(user_id)
    
    if success:
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'error': 'User not found or deletion failed'}), 404

# Define the route to get all medications for a user
@user_bp.route('/users/<int:user_id>/medications', methods=['GET'])
def get_medications(user_id):
    medications = user_service.get_all_medications(user_id)
    
    if medications:
        return jsonify([{
            'id': med.id,
            'medication_name': med.medication_name,
            'dosage': med.dosage,
            'instructions': med.instructions
        } for med in medications]), 200
    return jsonify({'error': 'No medications found'}), 404

# Define the route to add a medication to a user's profile
@user_bp.route('/users/<int:user_id>/medications', methods=['POST'])
def add_medication(user_id):
    data = request.get_json()
    
    medication_info = {
        'medication_name': data.get('medication_name'),
        'dosage': data.get('dosage'),
        'instructions': data.get('instructions'),
        'side_effects': data.get('side_effects'),
        'purpose': data.get('purpose'),
        'precautions': data.get('precautions'),
        'warnings': data.get('warnings')
    }
    
    medication = user_service.add_medication(user_id, medication_info)
    
    if medication:
        return jsonify({
            'id': medication.id,
            'medication_name': medication.medication_name,
            'dosage': medication.dosage,
            'instructions': medication.instructions
        }), 201
    return jsonify({'error': 'Failed to add medication'}), 400

# Define the route to delete a medication from a user's profile
@user_bp.route('/users/<int:user_id>/medications/<int:medication_id>', methods=['DELETE'])
def delete_medication(user_id, medication_id):
    success = user_service.delete_medication(user_id, medication_id)
    
    if success:
        return jsonify({'message': 'Medication deleted successfully'}), 200
    return jsonify({'error': 'Medication not found or deletion failed'}), 404
