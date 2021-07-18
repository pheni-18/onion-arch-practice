from abc import ABCMeta, abstractmethod
from typing import List

import domain.models as domain_models


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all_users(self) -> List[domain_models.User]:
        pass
