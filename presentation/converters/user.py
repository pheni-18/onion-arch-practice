from ..schemas import User

import domain.models as domain_models


class UserConverter:
    @staticmethod
    def to_schema(user: domain_models.User) -> User:
        return User(
            id=str(user.id.value),
            firstName=user.first_name,
            lastName=user.last_name,
            age=user.age,
        )
