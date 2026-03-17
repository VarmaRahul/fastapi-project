from fastapi import APIRouter
from app.models.schemas import UserBase

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
def register_user(user: UserBase):
    return {"message": f"User {user.username} registered successfully"}

@router.get("/me")
def get_profile():
    return {"username": "rahul_varma", "role": "Senior DevOps Engineer"}