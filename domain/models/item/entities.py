from .value_objects import ItemID
from dataclasses import dataclass


@dataclass
class Item:
    id: ItemID
    name: str
    price: int


@dataclass
class Stock:
    item_id: ItemID
    quantity: int
