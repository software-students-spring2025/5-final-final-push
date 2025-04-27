# flask app
import os
import pymongo
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.environ.get("MONGO_URI") # made an initial db, we can replace with actual db later
mongo_db = os.environ.get("MONGO_DB")

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
def index():
    return render_template('homeHaiku.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5001), debug=False)