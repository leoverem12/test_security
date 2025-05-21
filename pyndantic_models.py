from pydantic import Field, BaseModel
from typing import Optional


class User(BaseModel):

    name: Optional[str] = Field(None, description="IMYA")
    email: str = Field(..., description="emil")
    orders: str = Field(..., description="замовленна")


class Order(User):
    name: str = Field(..., description="name")
    kilkist: int = Field(..., description="kilka")
    price: int = Field(..., description="cina")