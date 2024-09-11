from flask import request, jsonify
from services.auth_service import authenticate_user, register_user

def login():
    data = request.get_json()
    token = authenticate_user(data['username'], data['password'])
    if token:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

def register():
    data = request.get_json()
    if register_user(data['username'], data['password'], data['role']):
        return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'message': 'User already exists'}), 409
