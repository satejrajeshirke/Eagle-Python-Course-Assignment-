from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user1 = User(name="Satej", age=21)

print(user1)