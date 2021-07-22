from ..dtos.user import UserDTO, UserCreateDTO
from typing import List

import domain.interfaces as domain_interfaces
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
        user = user_create_dto.create_domain()
        self._user_repo.create(user)
        return UserDTO.from_domain(user)
