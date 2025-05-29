from fastapi import APIRouter, HTTPException, Depends
from app.models import User
from app.crud import create_user, get_user_by_email, get_user_by_id, update_user, delete_user, list_users
from app.utils import require_role

router = APIRouter()

@router.post("/", response_model=str)
def api_create_user(user: User):
    if get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(user)

@router.get("/", response_model=list[User])
def api_get_users():
    return list_users()

@router.get("/{user_id}", response_model=User)
def api_get_user(user_id: str):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
def api_update_user(user_id: str, update_data: dict):
    return update_user(user_id, update_data)

@router.delete("/{user_id}")
def api_delete_user(user_id: str):
    return delete_user(user_id)