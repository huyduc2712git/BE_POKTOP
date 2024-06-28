from flask import Flask
from flask_cors import CORS

# Create the Flask application instance
app = Flask(__name__)
cors = CORS(app, resource={r"/*": {"origins": "*"}})
# Import routes
# from app import routes
from app.routes import shortVideo
