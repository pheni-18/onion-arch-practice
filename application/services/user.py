from ..dtos.user import UserDTO, UserCreateDTO, UserUpdateDTO
from typing import List

import domain.interfaces as domain_interfaces
import domain.models as domain_models
import pinject


class AppUserService:
    _user_repo: domain_interfaces.IUserRepository

    @pinject.inject()
    def __init__(self, user_repo: domain_interfaces.IUserRepository):
        self._user_repo = user_repo

    def get_all(self) -> List[UserDTO]:
        users = self._user_repo.get_all()
        return [UserDTO.from_domain(user) for user in users]

    def register(self, user_create_dto: UserCreateDTO) -> UserDTO:
        user = domain_models.User(
            first_name=user_create_dto.first_name,
            last_name=user_create_dto.last_name,
            age=user_create_dto.age,
        )
        self._user_repo.create(user)
        return UserDTO.from_domain(user)

    def update(self, user_update_dto: UserUpdateDTO) -> UserDTO:
        id = domain_models.UserID(value=user_update_dto.id)
        user = self._user_repo.get(id)
        if not user_update_dto.first_name == user.first_name:
            user.set_first_name(user_update_dto.first_name)

        if not user_update_dto.last_name == user.last_name:
            user.set_last_name(user_update_dto.last_name)

        if not user_update_dto.age == user.age:
            user.set_age(user_update_dto.age)

        self._user_repo.update(user)
        return UserDTO.from_domain(user)
