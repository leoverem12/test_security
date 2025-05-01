from pydantic import Field, BaseModel
from typing import Optional


class UserModelResponce(BaseModel):

    name: Optional[str] = Field(None, description="IMYA")
    email: str = Field(..., description="emil")


class UserModel(UserModelResponce):
    password: str = Field(..., description="parol")