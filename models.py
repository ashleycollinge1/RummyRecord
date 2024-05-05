from pydantic import BaseModel

class Player(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class Game(BaseModel):
    id: int
