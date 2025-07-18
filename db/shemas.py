from pydantic import BaseModel

class CUser(BaseModel):
    name: str
    age: int
    city: str

class UserR(CUser):
    id: int

    model_config = {
        "from_attributes": True
    }

class Cmessage(BaseModel):
    message: str
    description: str

class Rmessage(Cmessage):
    id: int
    model_config = {
        "from_attributes": True
    }
