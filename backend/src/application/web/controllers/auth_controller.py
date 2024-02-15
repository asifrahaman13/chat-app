# src/application/web/controllers/user_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from src.domain.entities.user import UserBase
from src.domain.interfaces.user_interface import UserInterface
from src.domain.use_cases.user_service import UserService
from src.infastructure.repositories.user_repository import UserRepository
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta

from src.infastructure.repositories.auth_repository import AuthRepository
from src.domain.use_cases.auth_service import AuthenticationService
from src.domain.interfaces.auth_interface import AuthInterface

from src.infastructure.exceptions.exceptions import HttePrequestErrors


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
user_repository = UserRepository()
user_service = UserService(user_repository)
auth_repository = AuthRepository()
auth_service = AuthenticationService()


def get_current_user(token: str = Depends(oauth2_scheme)):
    return token


@router.post("/signup")
async def signup(user: UserBase, user_interface: UserInterface = Depends(user_service), auth_interface: AuthInterface = Depends(auth_service)):
    user_data = user.model_dump()
    membername = user_data["membername"]
    memberpass = user_data["memberpass"]

    if membername == "" or memberpass == "":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Plesae provide valid credential",
        )

    try:

        # Create the new user
        data = user_interface.save_user(membername, memberpass)

        # Generate an access token for the new user
        access_token_expires = timedelta(days=7)
        access_token = auth_interface.create_access_token(data={"sub": membername}, expires_delta=access_token_expires)

        return {"access_token": access_token, "token_type": "bearer", "data": data}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to signup user",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.post("/login")
async def all_data(
    user: UserBase,
    user_interface: UserInterface = Depends(user_service),
    auth_interface: AuthInterface = Depends(auth_service),
):
    user_data = user.model_dump()
    membername = user_data["membername"]
    memberpass = user_data["memberpass"]

    print(user_data)

    if membername == "" or memberpass == "":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Plesae provide valid credential",
        )

    is_authenticated = user_interface.check_user(membername, memberpass)
    if is_authenticated == False:
        return

    try:
        # Generate an access token
        access_token_expires = timedelta(days=7)
        access_token = auth_interface.create_access_token(data={"sub": membername}, expires_delta=access_token_expires)

        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.get("/authenticate")
async def get_protected_data(current_user: str = Depends(get_current_user), auth_interface: AuthInterface = Depends(auth_service)):
    user = auth_interface.get_current_user(current_user)

    if user == False:
        return HttePrequestErrors.unauthorized()
    return {"message": True, "user": user}
