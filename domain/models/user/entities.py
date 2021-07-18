from .value_objects import UserID
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    age: int

    id: UserID = UserID()
