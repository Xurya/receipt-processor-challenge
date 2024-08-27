from typing import List
from dataclasses import dataclass

@dataclass
class Item:
    short_description: str
    price: str

@dataclass
class Receipt:
    retailer: str
    purchase_date: str
    purchase_time: str
    items: List[Item]
    total: str
    points: int = 0