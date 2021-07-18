from ._fake_db import FakeDB
from typing import List

import domain.interfaces as domain_interfaces
import domain.models as domain_models


class UserRepository(domain_interfaces.IUserRepository):
    _db: FakeDB

    def __init__(self, db: FakeDB):
        self._db = db

    def get_all_users(self) -> List[domain_models.User]:
        users = self._db.find_all()
        return [
            domain_models.User(
                id=domain_models.UserID(value=user['id']),
                first_name=user['first_name'],
                last_name=user['last_name'],
                age=user['age'],
            )
            for user in users
        ]
