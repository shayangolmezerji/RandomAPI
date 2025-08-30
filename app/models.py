# app/models.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DataEntry(BaseModel):
    user_id: str
    event_type: str
    value: int
    timestamp: Optional[datetime] = None
