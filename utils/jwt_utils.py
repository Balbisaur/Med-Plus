import jwt
from flask import current_app
from datetime import datetime, timedelta

def encode_token(user_id, expires_in=3600):
    """
    Generates a JWT token for the given user_id.

    Args:
        user_id (int): The ID of the user.
        expires_in (int): The number of seconds until the token expires (default is 3600 seconds = 1 hour).

    Returns:
        str: The encoded JWT token.
    """
    try:
        # Retrieve the secret key from app configuration
        secret_key = current_app.config['SECRET_KEY']
        
        # Define the token payload with expiration time
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(seconds=expires_in)
        }
        
        # Encode the token
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token
    except Exception as e:
        print(f"Error encoding token: {str(e)}")
        return None

def decode_token(token):
    """
    Decodes the JWT token and verifies its validity.

    Args:
        token (str): The JWT token to decode.

    Returns:
        dict: The payload of the token if valid.
        None: If the token is invalid or expired.
    """
    try:
        # Retrieve the secret key from app configuration
        secret_key = current_app.config['SECRET_KEY']
        
        # Decode the token
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return None

