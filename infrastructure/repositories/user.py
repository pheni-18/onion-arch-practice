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
            users = session.query(User).all()
            return [
                domain_models.User(
                    id=domain_models.UserID(value=user.id),
                    first_name=user.first_name,
                    last_name=user.last_name,
                    age=user.age,
                )
                for user in users
            ]
