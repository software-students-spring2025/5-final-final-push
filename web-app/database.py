from flask_pymongo import PyMongo
import os
from bson.objectid import ObjectId

mongo = None

def init_app(app):
    """Initialize the MongoDB Atlas connection with the Flask app."""
    global mongo

    app.config['MONGO_URI'] = os.environ.get(
        'MONGODB_URI',
        'mongodb+srv://HaikuUser:SecretPassword@cluster0.6qmtcol.mongodb.net/HaikuDB?retryWrites=true&w=majority'
    )

    mongo = PyMongo(app)

    try:
        mongo.cx.server_info()  
        print(f"Connected to MongoDB Atlas: {mongo.db.name}")
    except Exception as e:
        print("MongoDB Atlas connection failed:", e)

    return mongo

