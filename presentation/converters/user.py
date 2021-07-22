from ..schemas import User, UserCreate, UserUpdate

import application.dtos as app_dtos


class UserConverter:
    @staticmethod
    def to_schema(user_dto: app_dtos.UserDTO) -> User:
        return User(
            id=user_dto.id,
            firstName=user_dto.first_name,
            lastName=user_dto.last_name,
            age=user_dto.age,
        )

    @staticmethod
    def to_create_dto(user_create: UserCreate) -> app_dtos.UserCreateDTO:
        return app_dtos.UserCreateDTO(
            first_name=user_create.firstName,
            last_name=user_create.lastName,
            age=user_create.age,
        )

    @staticmethod
    def to_update_dto(id: str, user_update: UserUpdate) -> app_dtos.UserUpdateDTO:
        return app_dtos.UserUpdateDTO(
            id=id,
            first_name=user_update.firstName,
            last_name=user_update.lastName,
            age=user_update.age,
        )
