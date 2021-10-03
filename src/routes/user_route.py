from http.client import HTTPException
from fastapi import APIRouter
from src.helper.response_helper import Response
from src.model.user import User
from src.routes.base_models.basemodels import UserResponse

user_router = APIRouter()

@user_router.post("/create_user")
async def create_user(user: UserResponse, status_code=201):
    user = User.filter(User.identity_number == user.identity_number).first()
    if len(user) > 0:
        raise HTTPException(status_code=400, detail="User already exists!")
    user = User.create(first_name = user.first_name, last_name = user.last_name, identity_number = user.identity_number)
    return Response(user,"New user created.",201)


@user_router.get("/list_users")
async def list_users(status_code=200):
    users = User.all()
    return Response(users,"All users fetched.")

@user_router.put("/update_user/{id}", status_code=200)
async def update_user_data(id: int, user: UserResponse):
    u = User.get_pk(id)
    if u is None:
        raise HTTPException(status_code=400, detail="User not found!")
    u.first_name = user.first_name
    u.last_name = user.last_name
    u.identity_number = user.identity_number
    u.save()
    return Response(u, "User updated succesfully.")

@user_router.delete("/delete_user/{id}")
async def delete_user(id:int):
    user = User.get_pk(id)
    if user is not None:
        user.delete()
        return Response([],"User deleted succesfully.")
    raise HTTPException(status_code=400, detail="User not found!")
