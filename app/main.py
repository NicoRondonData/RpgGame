from fastapi import FastAPI
from app.talana_kombat_jrpg.serializers import Game as GameSchema, GameResponseSchema
from app.talana_kombat_jrpg.main import Game
app = FastAPI()


@app.post("/play/")
def insert_item(game_info:GameSchema, ):
    game = Game(game_info.dict()).play()

    return {
        "data": GameResponseSchema(**game)
    }
