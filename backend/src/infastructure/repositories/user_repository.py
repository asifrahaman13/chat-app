# src/infrastructure/repositories/user_repository.py

from sqlmodel import Session, create_engine, select
from urllib.parse import quote
from src.domain.entities.user import UserSessionData, UserSession
from sqlmodel import SQLModel
from src.domain.entities.user import Vadata
from config.config import SQL_DB_URL

class UserRepository:

    def __init__(self):
        DATABASE_URL = SQL_DB_URL
        connect_args = {}
        self.engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)

        # The following line of code is very important to actually create table corresponding to the ORMs.
        SQLModel.metadata.create_all(self.engine)

    def save_user(self, membername: str, memberpass: str):
        with Session(self.engine) as session:
            statement = select(Vadata).where(Vadata.membername == membername)
            results = session.exec(statement).first()
            print(results)
            if results == None:
                user_data = Vadata(membername=membername, memberpass=memberpass)
                session.add(user_data)
                session.commit()
                session.close()
                return True
            else:
                return False

    def check_user(self, membername: str, memberpass: str) -> bool:
        with Session(self.engine) as session:
            statement = select(Vadata).where(Vadata.membername == membername)
            results = session.exec(statement).first()
            print("the result", results)
            print("the other", memberpass)
            if results.memberpass == memberpass:
                print("yes")
                return True
        return False

    def save_data(self, user_id, session_id, session_data):
        try:
            # Add the session id.
            with Session(self.engine) as session:
                statement = select(UserSession).where(UserSession.user_id == user_id)
                user = session.exec(statement).all()

                if user == None:
                    user_data = UserSession(user_id=user_id, session_id=session_id)
                    session.add(user_data)

                    session.commit()
                    session.close()

                else:
                    append = True

                    for item in user:

                        if item.session_id == session_id:
                            append = False

                    if append == True:
                        user_data = UserSession(user_id=user_id, session_id=session_id)
                        session.add(user_data)

                        session.commit()
                        session.close()

            # Now add the questions and answers
            with Session(self.engine) as session:
                user = session.exec(select(UserSessionData).where(UserSessionData.session_id == session_id)).first()
                if user:

                    session_data_append = {
                        "question": session_data["question"],
                        "answer": session_data["answer"],
                    }

                    existing_data = user.session_data

                    updated_data = list(existing_data)

                    updated_data.append(session_data_append)
                    user.session_data = updated_data

                    session.add(user)
                    session.commit()
                    session.refresh(user)

                    return True
                else:
                    session_data_append = [
                        {
                            "question": session_data["question"],
                            "answer": session_data["answer"],
                        }
                    ]
                    new_user_data = UserSessionData(session_id=session_id, session_data=session_data_append)
                    session.add(new_user_data)
                    print(new_user_data)
                    session.commit()
                    session.close()
                    return True

        except Exception as e:
            print(e)
            return False

    def get_user_data(self, session_id: str):
        try:
            with Session(self.engine) as session:
                statement = select(UserSessionData).where(UserSessionData.session_id == session_id)
                results = session.exec(statement).all()
                session.close()
                print(results)
                return results
        except Exception as e:
            print(e)
        return False

    def get_all_sessions(self, user_id):
        try:
            with Session(self.engine) as session:
                statement = select(UserSession).where(UserSession.user_id == user_id)
                results = session.exec(statement).all()
                session.close()
                return results

        except Exception as e:
            print(e)
