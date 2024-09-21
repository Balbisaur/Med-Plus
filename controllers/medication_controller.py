from flask import request, jsonify, Blueprint
from services.medication_service import MedicationService



medication_bp = Blueprint('medication_bp', __name__)
medication_service = MedicationService()

@medication_bp.route('/medications', methods=['POST'])
def add_medication():
    data = request.json
    user_id = request.args.get('user_id')  # Assuming user ID is passed as a query parameter
    result = medication_service.add_medication(user_id, data)
    return jsonify(result), 201

@medication_bp.route('/medications', methods=['GET'])
def get_medications():
    user_id = request.args.get('user_id')
    medications = medication_service.get_medications(user_id)
    return jsonify([med.to_dict() for med in medications]), 200
