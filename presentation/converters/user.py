from ..schemas import User, UserCreate

import application.dtos as app_dtos


class UserConverter:
    @staticmethod
    def to_schema(user: app_dtos.UserDTO) -> User:
        return User(
            id=user.id,
            firstName=user.first_name,
            lastName=user.last_name,
            age=user.age,
        )

    @staticmethod
    def to_create_dto(user: UserCreate) -> app_dtos.UserCreateDTO:
        return app_dtos.UserCreateDTO(
            first_name=user.firstName,
            last_name=user.lastName,
            age=user.age,
        )
