import os
from pymongo import MongoClient

MONGO_URL = os.environ.get("MONGO_URL")  # Must match Railway variable
client = MongoClient(MONGO_URL)

db = client.confessionDB
confessions = db.confessions
