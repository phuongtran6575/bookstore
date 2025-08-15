from fastapi import APIRouter, Depends
from service.auth_service import get_user_by_username, create_user
from service import auth_service
from database.sqlite_database import SessionDepends
from models.user_model import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter(prefix="/auth", tags=["auth"] )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


@router.get("/user/")
async def get_user(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: SessionDepends):
    user_db = await get_user_by_username(form_data.username, session)
    if user_db.password == form_data.password:
        return {"access_token": user_db.username}
    
@router.post("/register")
async def register(user: User, session: SessionDepends ):
    return await auth_service.create_user(user, session)