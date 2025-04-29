import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from pymongo import MongoClient
import haiku_generation

load_dotenv()
mongo_uri = os.environ.get("MONGO_URI")
mongo_db  = os.environ.get("MONGO_DB")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["haiku"]              
haikus_collection = db["haikus"]

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path="/"
)

@app.route('/')
def index():
    return render_template('homeHaiku.html')

@app.route('/about')
def about():
    return render_template('aboutHaikus.html')

@app.route('/browse')
def browse_haikus():
    haikus = list(haikus_collection.find())  
    return render_template('browseHaikus.html', haikus=haikus)

@app.route('/saved')
def saved():
    return render_template('savedHaikus.html')

@app.route('/search')
def search():
    return render_template('searchHaikus.html')

@app.route('/write')
def write():
    return render_template('writeHaiku.html')

@app.route('/submit', methods=['POST'])
def submit():
    haiku_text = request.form.get('haiku_text')
    return render_template('submitHaiku.html', haiku_text=haiku_text)


@app.route('/generate-haiku', methods=['POST'])
def generate_haiku():
    theme = request.form.get('theme')
    generated = haiku_generation.generate_haiku(theme) 
    lines = generated.strip().split("\n")

    if len(lines) < 3:
        lines += [""] * (3 - len(lines))

    line1, line2, line3 = lines[0], lines[1], lines[2]

    # Save to MongoDB
    haikus_collection.insert_one({
        "theme": theme,
        "line1": line1,
        "line2": line2,
        "line3": line3
    })

    return render_template('writeHaiku.html', line1=line1, line2=line2, line3=line3)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
    print("App running on port " + str(port))
