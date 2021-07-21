from pydantic import BaseModel


class UserBase(BaseModel):
    firstName: str
    lastName: str
    age: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: str

    class Config:
        orm_mode = True
