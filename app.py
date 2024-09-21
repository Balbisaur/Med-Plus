from flask import Flask
from database import db
from routes.auth_routes import auth_bp
from routes.medication_routes import medication_bp
from routes.reminder_routes import reminder_bp
from database import init_db
from flask_swagger_ui import get_swaggerui_blueprint
from models.user_model import User
from models.medication_model import Medication
from models.reminder_model import Reminder
from models.prescription_model import Prescription
from flask_cors import CORS
from flask import jsonify
from werkzeug.exceptions import HTTPException


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Swagger setup
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Medication Reminder API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(medication_bp)
app.register_blueprint(reminder_bp)


# Initialize DB
init_db()

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    else:
        return jsonify({"error": "Internal Server Error"}), 500



if __name__ == '__main__':
    app.run(debug=True)
