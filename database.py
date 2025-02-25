from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    """Initialize MongoDB connection."""
    global mongo
    mongo.init_app(app)  # Properly attach to Flask app
