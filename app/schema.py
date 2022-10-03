
from pydantic import BaseModel

from typing import Optional, List

class Car(BaseModel):
    make: Optional[str]
    model: Optional[str]
    year: Optional[int]
    price: Optional[float]
    engine: Optional[str]
    autonomus: Optional[bool]
    sold: List[Optional[str]]
    