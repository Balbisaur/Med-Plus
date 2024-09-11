from flask import Blueprint
from controllers.medication_controller import add_medication_route, get_medication_route

medication_bp = Blueprint('medication', __name__)

# Route to add medication
@medication_bp.route('/medication/add', methods=['POST'])
def add_medication():
    return add_medication_route()

# Route to get medication details by ID
@medication_bp.route('/medication/<int:med_id>', methods=['GET'])
def get_medication(med_id):
    return get_medication_route(med_id)
