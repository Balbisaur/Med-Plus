from models.user_model import User
from models.medication_model import Medication  
from database import db
from utils.jwt_utils import encode_token
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    def register(self, data):
        # Validate and create user
        if not all(key in data for key in ("username", "password", "email", "role")):
            raise ValueError("Missing required fields")

        # Check if user already exists
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            raise ValueError("User already exists")

        # Create user
        hashed_password = generate_password_hash(data['password'])
        new_user = User(username=data['username'], password=hashed_password, email=data['email'], role=data['role'])
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id, "username": new_user.username, "email": new_user.email}

    def login(self, data):
        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            token = encode_token(user.id)
            return {"token": token, "user": {"username": user.username, "email": user.email, "role": user.role}}
        raise ValueError("Invalid credentials")
