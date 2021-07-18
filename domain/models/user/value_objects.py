from dataclasses import dataclass

import uuid


@dataclass(frozen=True)
class UserID:
    value: str = str(uuid.uuid4())
