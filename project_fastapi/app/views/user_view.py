from fastapi import APIRouter
from app.controllers import user_controller

router = APIRouter()

@router.get("/user")
def get_user():
    return user_controller.get_user_data()
