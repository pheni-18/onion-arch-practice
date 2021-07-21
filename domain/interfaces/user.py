from abc import ABCMeta, abstractmethod
from typing import List

import domain.models as domain_models


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self) -> List[domain_models.User]:
        pass

    @abstractmethod
    def create(self, user: domain_models.User):
        pass
