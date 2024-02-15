from fastapi import APIRouter, Depends, HTTPException, status
from src.domain.interfaces.user_interface import UserInterface
from src.domain.interfaces.chat_interface import ChatInterface
from src.domain.use_cases.user_service import UserService
from src.infastructure.repositories.user_repository import UserRepository
from src.infastructure.repositories.chat_repository import ChatRepository
from fastapi.security import OAuth2PasswordBearer
from src.domain.interfaces.auth_interface import AuthInterface

from src.infastructure.repositories.auth_repository import AuthRepository
from src.domain.use_cases.chat_service import ChatService
from src.domain.use_cases.auth_service import AuthenticationService

from src.domain.entities.user import Question


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
user_repository = UserRepository()
user_service = UserService(user_repository)
auth_repository = AuthRepository()
auth_service = AuthenticationService()
chat_repository = ChatRepository()
chat_service = ChatService(chat_repository)


def get_current_user(token: str = Depends(oauth2_scheme)):
    return token


@router.post("/askquestion")
async def ask_question(
    question: Question,
    current_user: str = Depends(get_current_user),
    chat_interface: ChatInterface = Depends(chat_service),
    user_interface: UserInterface = Depends(user_service),
    auth_interface: AuthInterface = Depends(auth_service),
):
    try:
        user = auth_interface.get_current_user(current_user)
        response = chat_interface.chat_response(question.question)

        print(response)

        if response == False:
            return HTTPException(status_code=500, detail="Something went wrong")

        # Now save the data
        session_data = {"question": question.question, "answer": response}
        save_data = user_interface.save_data(user, question.session_id, session_data)

        return {"status": True, "response": response}

    except Exception as e:
        print(e)


@router.post("/session-data")
async def get_sessions(
    question: Question,
    current_user: str = Depends(get_current_user),
    chat_interface: ChatInterface = Depends(chat_service),
    user_interface: UserInterface = Depends(user_service),
    auth_interface: AuthInterface = Depends(auth_service),
):

    try:
        user = auth_interface.get_current_user(current_user)
        get_sessions=user_interface.get_user_data(question.session_id)
        return get_sessions

    except Exception as e:
        print(e)


@router.post("/sessions")
async def get_sessions(
    question: Question,
    current_user: str = Depends(get_current_user),
    chat_interface: ChatInterface = Depends(chat_service),
    user_interface: UserInterface = Depends(user_service),
    auth_interface: AuthInterface = Depends(auth_service),
):

    try:
        user = auth_interface.get_current_user(current_user)
        get_sessions=user_interface.get_all_sessions(user)
        return get_sessions

    except Exception as e:
        print(e)