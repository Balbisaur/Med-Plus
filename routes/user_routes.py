from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/users/register', methods=['POST'])
def register_user():
    """
    Register a new user.
    ---
    tags:
      - User
    parameters:
      - name: user
        in: body
        description: The user to register
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: "johndoe"
            password:
              type: string
              example: "securepassword"
            email:
              type: string
              example: "john.doe@example.com"
    responses:
      201:
        description: User registered successfully
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            username:
              type: string
              example: "johndoe"
            email:
              type: string
              example: "john.doe@example.com"
      400:
        description: Invalid input
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Invalid input data"
    """
    data = request.json
    user_service = UserService()
    try:
        result = user_service.register(data)
        return jsonify(result), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
