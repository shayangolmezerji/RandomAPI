# app/main.py
from fastapi import FastAPI, Depends
from .models import DataEntry
from .database import get_db
from pymongo import database
from typing import List
from datetime import datetime

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    print("Connecting to MongoDB...")

@app.on_event("shutdown")
def shutdown_db_client():
    print("Disconnecting from MongoDB...")

@app.post("/data", status_code=201)
def create_data_entry(entry: DataEntry, db: database.Database = Depends(get_db)):
    """
    Accepts a new data entry and stores it in the database.
    """
    collection = db["entries"]
    entry.timestamp = entry.timestamp or datetime.utcnow()
    result = collection.insert_one(entry.dict())
    return {"id": str(result.inserted_id)}

@app.get("/data", response_model=List[DataEntry])
def get_all_data(db: database.Database = Depends(get_db)):
    """
    Retrieves all data entries from the database.
    """
    collection = db["entries"]
    entries = list(collection.find({}))
    for entry in entries:
        entry["id"] = str(entry["_id"])
    return entries
