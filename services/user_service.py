from models.user_model import User
from models.medication_model import Medication  
from database import db
from utils.jwt_utils import encode_token
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    def __init__(self):
        pass

    def register(self, user_data):
        # Validate user data
        if not all(key in user_data for key in ("username", "password", "email")):
            raise ValueError("Missing required fields")

        # Example: Check for existing user (pseudo-code)
        existing_user = User.query.filter_by(email=user_data['email']).first()
        if existing_user:
            raise ValueError("User with this email already exists")

        # Create and save new user
        new_user = User(
            username=user_data['username'],
            password=user_data['password'],  # Hash password in a real app
            email=user_data['email']
        )
        db.session.add(new_user)
        db.session.commit()

        return {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }

    def create_user(self, username, password, email, role):
        # Creating a new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, email=email, role=role)

        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error creating user: {str(e)}")

    def login(self, username, password):
        # User authentication
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            # Generate JWT token on successful login
            token = encode_token(user.id)
            return {"user": user, "token": token}
        return None

    def get_user_by_id(self, user_id):
        # Fetching user by ID
        return User.query.get(user_id)

    def update_user(self, user_id, new_data):
        # Update user information
        user = self.get_user_by_id(user_id)
        
        if user:
            user.username = new_data.get('username', user.username)
            user.email = new_data.get('email', user.email)
            user.password = generate_password_hash(new_data['password']) if 'password' in new_data else user.password
            try:
                db.session.commit()
                return user
            except Exception as e:
                db.session.rollback()
                raise Exception(f"Error updating user: {str(e)}")
        return None

    def delete_user(self, user_id):
        # Delete a user
        user = self.get_user_by_id(user_id)
        
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                raise Exception(f"Error deleting user: {str(e)}")
        return False

    def get_medication_by_id(self, user_id, medication_id):
        # Fetch medication details by user_id and medication_id
        user = self.get_user_by_id(user_id)
        
        if user:
            medication = Medication.query.filter_by(user_id=user.id, id=medication_id).first()
            return medication
        return None

    def add_medication(self, user_id, medication_info):
        # Adding a medication to the user's profile
        user = self.get_user_by_id(user_id)
        
        if user:
            medication = Medication(
                user_id=user.id,
                medication_name=medication_info.get('medication_name'),
                dosage=medication_info.get('dosage'),
                instructions=medication_info.get('instructions'),
                side_effects=medication_info.get('side_effects'),
                purpose=medication_info.get('purpose'),
                precautions=medication_info.get('precautions'),
                warnings=medication_info.get('warnings')
            )
            try:
                db.session.add(medication)
                db.session.commit()
                return medication
            except Exception as e:
                db.session.rollback()
                raise Exception(f"Error adding medication: {str(e)}")
        return None

    def delete_medication(self, user_id, medication_id):
        # Deleting a medication from user's profile
        medication = self.get_medication_by_id(user_id, medication_id)
        
        if medication:
            try:
                db.session.delete(medication)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                raise Exception(f"Error deleting medication: {str(e)}")
        return False

    def get_all_medications(self, user_id):
        # Retrieve all medications for a user
        user = self.get_user_by_id(user_id)
        
        if user:
            medications = Medication.query.filter_by(user_id=user.id).all()
            return medications
        return None
