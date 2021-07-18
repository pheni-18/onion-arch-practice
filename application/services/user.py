from typing import List

import domain.models as domain_models
import domain.services as domain_services
import pinject


class AppUserService:
    _user_service: domain_services.UserService

    @pinject.inject()
    def __init__(self, user_service: domain_services.UserService):
        self._user_service = user_service

    def get_all_users(self) -> List[domain_models.User]:
        return self._user_service.get_all_users()
