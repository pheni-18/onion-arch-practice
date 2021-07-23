from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from presentation.controllers import router


api = FastAPI()

api.include_router(router)


def custom_openapi():
    if api.openapi_schema:
        return api.openapi_schema

    openapi_schema = get_openapi(
        title='Onion arch practice',
        version='1.0.0',
        description='This is a practice of ddd and onion arch.',
        routes=api.routes,
    )
    openapi_schema['info']['x-logo'] = {
        'url': 'https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png',
    }
    api.openapi_schema = openapi_schema
    return api.openapi_schema


api.openapi = custom_openapi
