from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, JSON
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    user_id: str | None = None
    username: str | None = None


class Vadata(SQLModel, table=True):
    __tablename__ = "vadata"
    membername: str | None = Field(primary_key=True)
    memberpass: str | None = None


class UserBase(BaseModel):
    membername: str | None = None
    memberpass: str | None = None


class UserData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = None
    details: list[str] = Field(sa_type=JSON, default=[])  # Using JSON type for details
    patient_id: str
    patient_name: str
    date: str
    prev: list[str] = Field(sa_type=JSON, default=["{}"])


class Question(BaseModel):
    question: str | None = None
    session_id: str | None = None


class UserSessionData(SQLModel, table=True):
    __tablename__ = "user_session_data"
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: str | None = None
    session_data: list[str] = Field(sa_type=JSON, default=[])


class UserSession(SQLModel, table=True):
    __tablename__ = "user_sessions"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str | None = None
    session_id: str | None = None
