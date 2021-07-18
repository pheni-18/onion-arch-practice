from fastapi import FastAPI
from presentation.controllers import router


api = FastAPI()

api.include_router(router)
