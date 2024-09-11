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
from flask_cors import CORS

app = Flask(__name__)

CORS(app) # allows frontend to make requests to the flask backend

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



if __name__ == '__main__':
    app.run(debug=True)
