from fastapi import APIRouter
from app.models import Notification
from app.crud import create_notification, list_notifications_for_user, mark_notification_as_read, delete_notification

router = APIRouter()

@router.post("/", response_model=str)
def api_create_notification(notification: Notification):
    return create_notification(notification)

@router.get("/user/{user_id}", response_model=list[Notification])
def api_list_notifications_for_user(user_id: str):
    return list_notifications_for_user(user_id)

@router.put("/{notification_id}/read")
def api_mark_notification_as_read(notification_id: str):
    return mark_notification_as_read(notification_id)

@router.delete("/{notification_id}")
def api_delete_notification(notification_id: str):
    return delete_notification(notification_id)