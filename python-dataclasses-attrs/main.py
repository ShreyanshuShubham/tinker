from dataclasses import dataclass,field
from datetime import date
from enum import Enum, auto

@dataclass
class Product:
    name: str = field(compare=True)
    category: str = field(compare=True)
    weight: int = field(compare=False)
    unit_price: int = field(compare=False)
    tax_rate: int = field(compare=False)

    def __post_init__(self) -> None:
        if self.unit_price <= 0:
            raise ValueError("invalid unit price")
        
class Status(Enum):
    OPEN = auto()
    CLOSED = auto()
    PENDING = auto()

@dataclass
class Orders:
    status: Status 
    creation_date: date = date.today()
    products: list[Product] = field(default_factory=list)

    