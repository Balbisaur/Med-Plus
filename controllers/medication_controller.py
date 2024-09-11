from flask import request, jsonify
from services.medication_service import add_medication, get_medication_info

def add_medication_route():
    data = request.get_json()
    if add_medication(data):
        return jsonify({'message': 'Medication added successfully'}), 201
    return jsonify({'message': 'Failed to add medication'}), 400

def get_medication_route(med_id):
    med_info = get_medication_info(med_id)
    if med_info:
        return jsonify(med_info), 200
    return jsonify({'message': 'Medication not found'}), 404
