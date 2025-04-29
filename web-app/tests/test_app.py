import os
import pytest
from pymongo import MongoClient

def test_mongo_ping():
    uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
    client = MongoClient(uri)
    assert client.admin.command("ping")["ok"] == 1.0