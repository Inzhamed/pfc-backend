from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict
from datetime import datetime

# User schema
class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    email: EmailStr
    password_hash: str
    role: str = "operator"
    language: Optional[str] = "en"
    notifications: Optional[Dict[str, bool]] = {
        "email": True,
        "push": True
    }

class Location(BaseModel):
    lat: float
    lng: float
    trackId: str
    mileMarker: float

# Defect schema
class Defect(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    type: str
    severity: str
    location: Location
    status: str = "open"
    image_url: Optional[str]
    detected_at: datetime

# Notification schema
class Notification(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    user_id: str
    defect_id: str
    message: str
    timestamp: datetime
    read: bool = False

# Report schema (linked to a defect)
class Report(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    defect_id: str  # The ID of the defect this report is about
    title: str
    description: str
    action: str
    materials: str
    technician: str
    time_required: str
    created_at: datetime = Field(default_factory=datetime.utcnow)