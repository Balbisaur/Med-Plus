from models.user_model import User
from database import db
from utils.jwt_utils import encode_token
from werkzeug.security import check_password_hash, generate_password_hash

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return encode_token(user)
    return None

def register_user(username, password, role):
    if User.query.filter_by(username=username).first():
        return False
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return True
