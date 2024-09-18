from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Initialize Flask-Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# route with rate limiting
@app.route('/example')
@limiter.limit("10 per minute")
def example():
    return "This is an example route with rate limiting."
