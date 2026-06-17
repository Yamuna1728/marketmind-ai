from fastapi import APIRouter, HTTPException
from auth.jwt_handler import create_access_token
from models.user_model import (
    UserRegister,
    UserLogin
)

from database.mongodb import users_collection
from auth.password_handler import (
    hash_password,
    verify_password
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
async def register_user(
    user: UserRegister
):

    existing_user = users_collection.find_one(
        {"email": user.email}
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(
        user.password
    )

    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }

    users_collection.insert_one(
        new_user
    )

    return {
        "message":
        "User registered successfully"
    }


@router.post("/login")
async def login_user(
    user: UserLogin
):

    existing_user = users_collection.find_one(
        {"email": user.email}
    )

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    valid_password = verify_password(
        user.password,
        existing_user["password"]
    )

    if not valid_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={"email": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "name": existing_user["name"],
            "email": existing_user["email"]
        }
    }