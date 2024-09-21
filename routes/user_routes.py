from flask import Blueprint, request, jsonify
from services.user_service import UserService

# Define the blueprint for user routes
user_bp = Blueprint('user_bp', __name__)

# Initialize the UserService
user_service = UserService()

# Route for user registration
@user_bp.route('/register', methods=['POST'])
def register_user():
    try:
        # Extract user data from request
        user_data = request.get_json()
        # Call the register method in the service layer
        new_user = user_service.register(user_data)
        return jsonify({"message": "User registered successfully", "user": new_user}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

# Route for user login
@user_bp.route('/login', methods=['POST'])
def login_user():
    try:
        # Extract login data from request
        login_data = request.get_json()
        username = login_data.get('username')
        password = login_data.get('password')
        
        # Call the login method in the service layer
        result = user_service.login(username, password)
        if result:
            return jsonify({"message": "Login successful", "token": result['token'], "user": result['user'].username}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

# Route to fetch a user by ID
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        # Call the get_user_by_id method in the service layer
        user = user_service.get_user_by_id(user_id)
        if user:
            return jsonify({"user": user.username, "email": user.email}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

# Route to update user data
@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        # Extract the new data from the request
        new_data = request.get_json()
        # Call the update_user method in the service layer
        updated_user = user_service.update_user(user_id, new_data)
        if updated_user:
            return jsonify({"message": "User updated successfully", "user": updated_user.username}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

# Route to delete a user
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # Call the delete_user method in the service layer
        if user_service.delete_user(user_id):
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500
