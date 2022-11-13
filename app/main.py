from fastapi import FastAPI

from app.talana_kombat_jrpg.fighters.arnaldor.main import Arnaldor
from app.talana_kombat_jrpg.fighters.tony.main import Tony
from app.talana_kombat_jrpg.main import Game
from app.talana_kombat_jrpg.serializers import GameSchema as GameSchema
from app.talana_kombat_jrpg.serializers import GameResponseSchema
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
app = FastAPI()


@app.post("/play/")
def insert_item(
    game_info: GameSchema,
):
    player1 = Tony()
    player2 = Arnaldor()
    body = game_info.dict()
    game = Game(body, player_1=player1, player_2=player2)
    result = game.result
    response = GameResponseSchema(**result)

    return {"data":response}

