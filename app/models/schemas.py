from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str

class OrderBase(BaseModel):
    item_name: str
    quantity: int
    price: float