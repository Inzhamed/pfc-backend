from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.crud import get_user_by_email  
from app.utils import verify_password, create_access_token  

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/", response_model=LoginResponse)
def login(data: LoginRequest):
    user = get_user_by_email(data.email)
    if not user or not verify_password(data.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["email"], "role": user["role"], "user_id": str(user["_id"])})
    return {"access_token": token}