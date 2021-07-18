from dataclasses import dataclass

import uuid


@dataclass(frozen=True)
class ItemID:
    value: str = str(uuid.uuid4())
