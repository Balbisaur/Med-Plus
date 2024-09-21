from flask import Blueprint, request, jsonify
from services.user_service import UserService
from utils.jwt_utils import decode_token

# Define the blueprint for user-related routes
user_bp = Blueprint('user_bp', __name__)
user_service = UserService()

@user_bp.route('/users/register', methods=['POST'])
def register_user():
    data = request.json
    try:
        result = user_service.register(data)
        return jsonify(result), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route('/users/login', methods=['POST'])
def login_user():
    data = request.json
    try:
        result = user_service.login(data)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
