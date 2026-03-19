from pydantic import BaseModel, EmailStr, Field

# This is what the user SENDS us
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    # Set a maximum length of 72 characters to stay safe with Bcrypt
    password: str = Field(..., max_length=72)

# This is what we SEND BACK to the user
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

    # This tells Pydantic to stay compatible with SQLAlchemy objects
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    item_name: str
    quantity: int = 1
    price: float

class OrderCreate(OrderBase):
    pass # Data coming in from the user

class OrderResponse(OrderBase):
    id: int
    owner_id: int # Tells the user who owns this order

    class Config:
        from_attributes = True