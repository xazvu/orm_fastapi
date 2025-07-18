from pydantic import BaseModel

class RUser(BaseModel):
    name: str
    age: int
    city: str

class UserR(RUser):
    id: int

    model_config = {
        "from_attributes": True
    }