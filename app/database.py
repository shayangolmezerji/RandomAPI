# app/database.py
from pymongo import MongoClient

MONGO_URI = "mongodb://mongo-db:27017/"
DB_NAME = "analytics"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def get_db():
    return db
