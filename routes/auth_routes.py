from flask import Blueprint
from controllers.auth_controller import login, register

auth_bp = Blueprint('auth', __name__)

# User login route
@auth_bp.route('/login', methods=['POST'])
def login_route():
    return login()

# User registration route
@auth_bp.route('/register', methods=['POST'])
def register_route():
    return register()
