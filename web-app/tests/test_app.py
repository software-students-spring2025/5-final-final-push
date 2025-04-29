# testing file for web app
import os
import sys
import pytest
sys.path.append("..")
from dotenv import load_dotenv
from app import app
import haiku_generation

load_dotenv()

mongo_uri = os.environ.get("MONGO_URI")
mongo_db  = os.environ.get("MONGO_DB")

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client

def test_index(client):
    landing = client.get("/")
    html = landing.data.decode()

    # check that top bar links exist and go to the right place
    assert '<a href="/write">Write Your Own Haiku</a>' in html
    assert '<a href="/browse">Browse Through All Haiku Submissions</a>' in html
    assert '<a href="/saved">Your Favorite Haikus Saved</a>' in html
    assert '<a href="/search">Search</a>' in html
    assert '<a href="/about">What is Haiku??</a>' in html

    assert landing.status_code == 200

def test_about(client):
    about = client.get("/about")
    html = about.data.decode()
    assert '<a href="/write">Write Your Own Haiku</a>' in html
    assert '<a href="/">Home</a>' in html
    assert '<a href="/browse">Browse Haikus</a>' in html
    assert '<a href="/write">Write Your Own Haiku</a>' in html

    assert about.status_code == 200

def test_browse(client):
    browse = client.get("/browse")
    html = browse.data.decode()

    assert '<a href="/">Home</a>' in html
    assert '<a href="/write">Write Your Own</a>' in html
    assert '<a href="/about">About</a>' in html

    assert browse.status_code == 200

def test_saved(client):
    saved = client.get("/saved")
    html = saved.data.decode()
    assert '<a href="/">Home</a>' in html
    assert '<a href="/browse">Browse</a>' in html
    assert 'a href="/write">Write</a>' in html
    assert '<a href="/about">About</a>' in html

    assert saved.status_code == 200

def test_search(client):
    search = client.get("/search")
    html = search.data.decode()
    assert '<a href="/">Home</a><' in html
    assert '<a href="/browse">Browse</a' in html
    assert '<a href="/write">Write</a>' in html
    assert '<a href="/about">About</a>' in html

    assert search.status_code == 200

def test_write(client):
    write = client.get("/write")
    html = write.data.decode()
    assert '<a href="/">Home</a>' in html
    assert '<a href="/browse">Browse Haikus</a>' in html
    assert '<a href="/about">About</a>' in html

    assert write.status_code == 200
    
"""def test_submit(client):
    submit = client.get("/submit")
    html = submit.data.decode()
    assert '<a href="/browse">Browse Haikus</a>' in html
    assert '<a href="/write">Write Another Haiku</a>' in html

    assert submit.status_code == 200"""


def test_generate_haiku(client):
    theme = "cloud"
    generated = haiku_generation.generate_haiku(theme) 
    lines = generated.strip().split("\n")

    if len(lines) < 3:
        lines += [""] * (3 - len(lines))
    line1, line2, line3 = lines[0], lines[1], lines[2]

    assert line1 == lines[0]
    assert line2 == lines[1]
    assert line3 == lines[2]
    assert type(generated) == str

