from .value_objects import UserID
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    age: int

    id: UserID = UserID()

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def set_first_name(self, new_value):
        self.first_name = new_value

    def set_last_name(self, new_value):
        self.last_name = new_value

    def set_age(self, new_value):
        self.age = new_value
