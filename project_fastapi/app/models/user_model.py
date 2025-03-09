from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    name: str
    email: str
    age: int
    city: str
