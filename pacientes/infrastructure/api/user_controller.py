# infrastructure/api/user_controller.py

from fastapi import APIRouter, HTTPException
from typing import List

from domain.usuario import User, UserCreate, UserUpdate
from application.services.user_service import UserService
from infrastructure.adapters.user_repository_impl import UserRepositoryImpl


router = APIRouter()

repository = UserRepositoryImpl()
service = UserService(repository)


@router.post("/users", response_model=User)
def create_user(user: UserCreate):
    try:
        return service.register_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users", response_model=List[User])
def get_all_users():
    return service.get_all_users()


@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, user_update: UserUpdate):
    try:
        updated_user = service.update_user(user_id, user_update)
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
