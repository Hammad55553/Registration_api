from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    date_of_birth: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
