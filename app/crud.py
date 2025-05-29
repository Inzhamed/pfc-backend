from typing import List, Optional
from bson import ObjectId
from datetime import datetime
from app.models import User, Defect, Notification, Report
from app.utils import hash_password
from app.db import db

SEVERITY_MAP = {
    3: "critical",
    2: "high",
    1: "medium",
    0: "low"
}

def fix_mongo_id_and_severity(document):
    if document and "_id" in document:
        document["_id"] = str(document["_id"])
    if document and "severity" in document and isinstance(document["severity"], int):
        document["severity"] = SEVERITY_MAP.get(document["severity"], "low")
    return document

def fix_mongo_ids_and_severity(documents):
    return [fix_mongo_id_and_severity(doc) for doc in documents]


# --- USER CRUD ---
def create_user(user: User):
    user_dict = user.dict(by_alias=True, exclude_unset=True)
    if db.users.find_one({"email": user_dict["email"]}):
        raise ValueError("Email already registered")
    # Use provided password or default
    password = user_dict.get("password") or "password123"
    user_dict["password_hash"] = hash_password(password)
    user_dict.pop("password", None)  # Remove plain password
    result = db.users.insert_one(user_dict)
    return str(result.inserted_id)  

# get all users
def list_users() -> List[dict]:
    users = list(db.users.find())
    return fix_mongo_ids_and_severity(users)

def get_user_by_email(email: str) -> Optional[dict]:
    user = db.users.find_one({"email": email})
    return fix_mongo_id_and_severity(user)

def get_user_by_id(user_id: str) -> Optional[dict]:
    user = db.users.find_one({"_id": ObjectId(user_id)})
    return fix_mongo_id_and_severity(user)

def update_user(user_id: str, update_data: dict):
    # If password is being updated, hash it and update password_hash instead
    if "password" in update_data:
        from app.utils import hash_password
        update_data["password_hash"] = hash_password(update_data.pop("password"))
    result = db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    return {"matched_count": result.matched_count, "modified_count": result.modified_count}

def delete_user(user_id: str):
    result = db.users.delete_one({"_id": ObjectId(user_id)})
    return {"deleted_count": result.deleted_count}

# --- DEFECT CRUD ---
def create_defect(defect: Defect):
    defect_dict = defect.dict(by_alias=True, exclude_unset=True)
    result = db.defects.insert_one(defect_dict)
    return str(result.inserted_id)

def get_defect_by_id(defect_id: str) -> Optional[dict]:
    defect = db.defects.find_one({"_id": ObjectId(defect_id)})
    return fix_mongo_id_and_severity(defect)

def list_defects() -> List[dict]:
    defects = list(db.defects.find())
    return fix_mongo_ids_and_severity(defects)

def update_defect(defect_id: str, update_data: dict):
    result = db.defects.update_one({"_id": ObjectId(defect_id)}, {"$set": update_data})
    return {"matched_count": result.matched_count, "modified_count": result.modified_count}

def delete_defect(defect_id: str):
    result = db.defects.delete_one({"_id": ObjectId(defect_id)})
    return {"deleted_count": result.deleted_count}

# --- NOTIFICATION CRUD ---
def create_notification(notification: Notification):
    notif_dict = notification.dict(by_alias=True, exclude_unset=True)
    result = db.notifications.insert_one(notif_dict)
    return str(result.inserted_id)

def list_notifications_for_user(user_id: str) -> List[dict]:
    notifications = list(db.notifications.find({"user_id": user_id}))
    return fix_mongo_ids_and_severity(notifications)

def mark_notification_as_read(notification_id: str):
    result = db.notifications.update_one({"_id": ObjectId(notification_id)}, {"$set": {"read": True}})
    return {"matched_count": result.matched_count, "modified_count": result.modified_count}

def delete_notification(notification_id: str):
    result = db.notifications.delete_one({"_id": ObjectId(notification_id)})
    return {"deleted_count": result.deleted_count}

# --- REPORT CRUD ---
def create_report(report: Report):
    report_dict = report.dict(by_alias=True, exclude_unset=True)
    result = db.reports.insert_one(report_dict)
    update_defect(report.defect_id, {"status": "resolved"})
    return str(result.inserted_id)

def get_report_by_id(report_id: str) -> Optional[dict]:
    report = db.reports.find_one({"_id": ObjectId(report_id)})
    return fix_mongo_id_and_severity(report)

def list_reports_for_defect(defect_id: str) -> List[dict]:
    reports = list(db.reports.find({"defect_id": defect_id}))
    return fix_mongo_ids_and_severity(reports)

def list_reports() -> List[dict]:
    reports = list(db.reports.find())
    return fix_mongo_ids_and_severity(reports)

def update_report(report_id: str, update_data: dict):
    result = db.reports.update_one({"_id": ObjectId(report_id)}, {"$set": update_data})
    return {"matched_count": result.matched_count, "modified_count": result.modified_count}

def delete_report(report_id: str):
    result = db.reports.delete_one({"_id": ObjectId(report_id)})
    return {"deleted_count": result.deleted_count}