from depends_provider import DependsProvider
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from typing import ClassVar

import application.services as app_services


depends_provider = DependsProvider()
app_user_service = depends_provider.provide(app_services.AppUserService)

router = APIRouter(
    # prefix='/users',  https://github.com/dmontagu/fastapi-utils/issues/154
    tags=['users'],
)


@cbv(router)
class UserController:
    _prefix: ClassVar[str] = '/users'

    def __init__(self, app_user_service: app_services.AppUserService = Depends(lambda: app_user_service)):
        self._app_user_service = app_user_service

    @router.get(_prefix + '/')
    async def get_users(self):
        users = self._app_user_service.get_all()

        return {'result': users}
