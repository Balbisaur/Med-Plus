from flask import Blueprint, request, jsonify
from services.user_service import UserService
from services.qr_code_service import generate_qr_code, decode_qr_code

user_blueprint = Blueprint('user', __name__)

# UserService instance
user_service = UserService()

# Login route
@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    token = user_service.login(username, password)
    
    if token:
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401


# Route to get QR code for medication
@user_blueprint.route('/users/<int:user_id>/medications/<int:medication_id>/qr', methods=['GET'])
def get_medication_qr(user_id, medication_id):
    medication = user_service.get_medication_by_id(user_id, medication_id)
    
    if medication:
        medication_info = {
            'medication_name': medication.medication_name,
            'dosage': medication.dosage,
            'instructions': medication.instructions
        }
        qr_code = generate_qr_code(medication_info)
        return jsonify({'qr_code': qr_code}), 200
    
    return jsonify({'error': 'Medication not found'}), 404


# Route to scan and add medication via QR code
@user_blueprint.route('/users/<int:user_id>/medications/add-via-qr', methods=['POST'])
def add_medication_via_qr(user_id):
    data = request.get_json()
    qr_code_data = data.get('qr_code_data')
    
    medication_info = decode_qr_code(qr_code_data)
    if medication_info:
        added = user_service.add_medication(user_id, medication_info)
        if added:
            return jsonify({'message': 'Medication added successfully'}), 201
        return jsonify({'error': 'Failed to add medication'}), 400
    
    return jsonify({'error': 'Invalid QR code data'}), 400
