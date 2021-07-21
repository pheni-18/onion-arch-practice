from ..schemas import User, UserCreate

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

    @staticmethod
    def create_domain(user: UserCreate) -> domain_models.User:
        return domain_models.User(
            first_name=user.firstName,
            last_name=user.lastName,
            age=user.age,
        )
