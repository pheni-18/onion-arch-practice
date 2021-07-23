from ..converters import UserConverter
from ..schemas import UserCreate, UserUpdate, User, UserNotFound
from depends_provider import DependsProvider
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_utils.cbv import cbv
from typing import ClassVar, List

import application.exceptions as app_exceptions
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

    def __init__(
        self,
        app_user_service: app_services.AppUserService = Depends(lambda: app_user_service),
        user_converter: UserConverter = Depends(lambda: UserConverter())
    ):
        self._app_user_service = app_user_service
        self._user_converter = user_converter

    @router.get(
        _prefix + '/',
        response_model=List[User]
    )
    async def get_users(self):
        user_dtos = self._app_user_service.get_all()
        return [self._user_converter.to_schema(user_dto) for user_dto in user_dtos]

    @router.get(
        _prefix + '/{id}',
        response_model=User,
        responses={
            status.HTTP_404_NOT_FOUND: {'model': UserNotFound, 'description': 'The user was not found'},
        },
    )
    async def get_user(self, id: str):
        try:
            user_dto = self._app_user_service.get(id)
        except app_exceptions.UserNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

        return self._user_converter.to_schema(user_dto)

    @router.post(
        _prefix + '/',
        status_code=status.HTTP_201_CREATED,
        response_model=User,
    )
    async def create_user(self, user_create: UserCreate):
        user_create_dto = self._user_converter.to_create_dto(user_create)
        user_dto = self._app_user_service.register(user_create_dto)
        return self._user_converter.to_schema(user_dto)

    @router.patch(
        _prefix + '/{id}',
        response_model=User,
        responses={
            status.HTTP_404_NOT_FOUND: {'model': UserNotFound, 'description': 'The user was not found'},
        },
    )
    async def update_user(self, id: str, user_update: UserUpdate):
        user_update_dto = self._user_converter.to_update_dto(id, user_update)
        try:
            user_dto = self._app_user_service.update(user_update_dto)
        except app_exceptions.UserNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

        return self._user_converter.to_schema(user_dto)

    @router.delete(
        _prefix + '/{id}',
        status_code=status.HTTP_204_NO_CONTENT,
    )
    async def delete_user(self, id: str):
        self._app_user_service.delete(id)
        return
