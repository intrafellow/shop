from fastapi import APIRouter
from users.schemas import CreateUser
from users import crud

roter = APIRouter(prefix="/users", tags=["Users"])

@roter.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
