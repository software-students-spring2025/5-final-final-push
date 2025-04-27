import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_pymongo import PyMongo

load_dotenv()
mongo_uri = os.environ.get("MONGO_URI")
mongo_db  = os.environ.get("MONGO_DB")

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
def browse():
    return render_template('browseHaikus.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
    print("App running on port " + str(port))
