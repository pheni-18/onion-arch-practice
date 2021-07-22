from dataclasses import dataclass

import domain.models as domain_models


@dataclass
class UserBaseDTO:
    first_name: str
    last_name: str
    age: int


@dataclass
class UserDTO(UserBaseDTO):
    id: str

    # TODO: type annotation of return
    @classmethod
    def from_domain(cls, user: domain_models.User):
        return cls(
            id=user.id.value,
            first_name=user.first_name,
            last_name=user.last_name,
            age=user.age,
        )


@dataclass
class UserCreateDTO(UserBaseDTO):
    pass


@dataclass
class UserUpdateDTO(UserBaseDTO):
    id: str
