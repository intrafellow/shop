from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    username: Annotated[str, MaxLen(40), MinLen(3)]
    email: EmailStr