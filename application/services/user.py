from typing import List

import domain.interfaces as domain_interfaces
import domain.models as domain_models
import pinject


class AppUserService:
    _user_repo: domain_interfaces.IUserRepository

    @pinject.inject()
    def __init__(self, user_repo: domain_interfaces.IUserRepository):
        self._user_repo = user_repo

    def get_all(self) -> List[domain_models.User]:
        return self._user_repo.get_all()
