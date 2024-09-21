from flask import Blueprint, request, jsonify
from services.user_service import UserService

auth_bp = Blueprint('auth_bp', __name__)
user_service = UserService()

@auth_bp.route('/auth/register', methods=['POST'])
def register():
    data = request.json
    result = user_service.register(data)
    return jsonify(result), 201

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    result = user_service.login(data)
    return jsonify(result), 200
