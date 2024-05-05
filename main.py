from fastapi import FastAPI
from models import Player

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/player/{player_id}")
async def get_players(player_id: int):
    return {"player_id": player_id,
            "player_name": "Player1"}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/player")
def player2(player: Player):
    return player


