from ..db_session import SessionGenerator
from ..models import User
from typing import List

import domain.interfaces as domain_interfaces
import domain.models as domain_models
import pinject


class UserRepository(domain_interfaces.IUserRepository):
    _session_generator: SessionGenerator

    @pinject.inject()
    def __init__(self, session_generator: SessionGenerator):
        self._session_generator = session_generator

    def get_all(self) -> List[domain_models.User]:
        with self._session_generator.generate() as session:
            db_users = session.query(User).all()
            return [
                domain_models.User(
                    id=domain_models.UserID(value=db_user.id),
                    first_name=db_user.first_name,
                    last_name=db_user.last_name,
                    age=db_user.age,
                )
                for db_user in db_users
            ]

    def get(self, id: domain_models.UserID) -> domain_models.User:
        with self._session_generator.generate() as session:
            db_user = session.query(User).filter(User.id == id.value).first()
            return domain_models.User(
                id=domain_models.UserID(value=db_user.id),
                first_name=db_user.first_name,
                last_name=db_user.last_name,
                age=db_user.age,
            )

    def create(self, user: domain_models.User):
        with self._session_generator.generate() as session:
            db_user = User(
                id=user.id.value,
                first_name=user.first_name,
                last_name=user.last_name,
                age=user.age,
            )
            session.add(db_user)
            session.commit()

    def update(self, user: domain_models.User):
        with self._session_generator.generate() as session:
            db_user = session.query(User).filter(User.id == user.id.value).first()
            db_user.first_name = user.first_name
            db_user.last_name = user.last_name
            db_user.age = user.age
            session.commit()

    def delete(self, id: domain_models.UserID):
        with self._session_generator.generate() as session:
            db_user = session.query(User).filter(User.id == id.value)
            db_user.delete()
            session.commit()
