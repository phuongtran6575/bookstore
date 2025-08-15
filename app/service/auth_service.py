from sqlmodel import Session, select
from repository import user_repository
from models.user_model import User
from repository.user_repository import get_user_by_username, create_user
from fastapi import Depends
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

async def get_user_by_username(username: str, session: Session):
    return await user_repository.get_user_by_username(username, session)

async def get_current_user(token: str, session: Session ):
    user = get_user_by_username(token, session )
    return user

async def create_user(user: User, session: Session):
    return await user_repository.create_user(user, session)
