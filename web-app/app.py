import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
import haiku_generation
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path="/"
)

# Debug print to confirm Mongo URI loaded properly
mongo_uri = os.environ.get("MONGO_URI")
print("🔍 MONGO_URI =", mongo_uri)

app.config["MONGO_URI"] = mongo_uri
client = MongoClient(mongo_uri, tls=True, tlsAllowInvalidCertificates=True)
db = client[os.environ.get("MONGO_DB", "haiku")]

@app.route('/')
def index():
    return render_template('homeHaiku.html')

@app.route('/about')
def about():
    return render_template('aboutHaikus.html')

@app.route('/browse')
def browse():
    return render_template('browseHaikus.html')

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
    author = request.form.get('author')
    line1 = request.form.get('line1')
    line2 = request.form.get('line2')
    line3 = request.form.get('line3')

    db.haikus.insert_one({
    "author": author,
    "line1": line1,
    "line2": line2,
    "line3": line3,
    "timestamp": datetime.utcnow(),
})

    return render_template('submitHaiku.html', author=author, line1=line1, line2=line2, line3=line3)


@app.route('/generate-haiku', methods=['POST'])
def generate_haiku():
    theme = request.form.get('theme')
    generated = haiku_generation.generate_haiku(theme) 
    lines = generated.strip().split("\n")

    if len(lines) < 3:
        lines += [""] * (3 - len(lines))
    line1, line2, line3 = lines[0], lines[1], lines[2]
    #print(lines)
    return render_template('writeHaiku.html', line1=line1, line2=line2, line3=line3)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
    print("App running on port " + str(port))
