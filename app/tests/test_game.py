import pytest

from app.talana_kombat_jrpg.fighters.arnaldor.main import Arnaldor
from app.talana_kombat_jrpg.fighters.tony.main import Tony
from app.talana_kombat_jrpg.main import Game
from app.talana_kombat_jrpg.utils import open_json

instructions_mapper = {
    "app/tests/data/arnaldor.json": {
        "player": "Arnaldor",
        "player_energy": 2,
        "enemy": "Tony",
        "enemy_energy": 0,
        "message": " Welcome to Talana Kombat JRPG  \n Tony go to the RIGHT and  attack with a KICK \n The health of Arnaldor is 5  while health of Tony is 6 \n Arnaldor use REMUYUKEN \n The health of Tony is 3  while health of Arnaldor is 5 \n Tony use TALADOKEN \n The health of Arnaldor is 2  while health of Tony is 3 \n Arnaldor go to the DOWN and LEFT then  stop \n The health of Tony is 3  while health of Arnaldor is 2 \n Tony go to the DOWN then  stop \n The health of Arnaldor is 2  while health of Tony is 3 \n Arnaldor use REMUYUKEN \n The health of Tony is 0  while health of Arnaldor is 2 \n Arnaldor  killed Tony the energy of Arnaldor is 2 \n There is no more moves, the battle has ended and the winner is Arnaldor with 2 while Tony has only 0 of life ",
        "winner": "Arnaldor",
        "loser": "Tony",
    },
    "app/tests/data/arnaldor2.json": {
        "player": "Arnaldor",
        "player_energy": 3,
        "enemy": "Tony",
        "enemy_energy": -1,
        "message": " Welcome to Talana Kombat JRPG  \n Tony use TALADOKEN \n The health of Arnaldor is 3  while health of Tony is 6 \n Arnaldor  attack with a FIST \n The health of Tony is 5  while health of Arnaldor is 3 \n Tony go to the DOWN then  stop \n The health of Arnaldor is 3  while health of Tony is 5 \n Arnaldor go to the LEFT and DOWN and LEFT then  stop \n The health of Tony is 5  while health of Arnaldor is 3 \n Arnaldor go to the RIGHT and LEFT and  attack with a FIST \n The health of Tony is 4  while health of Arnaldor is 3 \n Arnaldor go to the LEFT and LEFT and LEFT and  attack with a KICK \n The health of Tony is 3  while health of Arnaldor is 3 \n Arnaldor  attack with a KICK \n The health of Tony is 2  while health of Arnaldor is 3 \n Arnaldor use REMUYUKEN \n The health of Tony is -1  while health of Arnaldor is 3 \n Arnaldor  killed Tony the energy of Arnaldor is 3 \n There is no more moves, the battle has ended and the winner is Arnaldor with 3 while Tony has only -1 of life ",
        "winner": "Arnaldor",
        "loser": "Tony",
    },
    "app/tests/data/tony1.json": {
        "player": "Tony",
        "player_energy": 1,
        "enemy": "Arnaldor",
        "enemy_energy": -2,
        "message": " Welcome to Talana Kombat JRPG  \n Tony go to the DOWN and RIGHT and RIGHT and  attack with a KICK \n The health of Arnaldor is 5  while health of Tony is 6 \n Arnaldor go to the RIGHT and DOWN and RIGHT and  attack with a FIST \n The health of Tony is 5  while health of Arnaldor is 5 \n Tony use TALADOKEN \n The health of Arnaldor is 2  while health of Tony is 5 \n Arnaldor go to the UP and DOWN and LEFT and UP and  attack with a KICK \n The health of Tony is 4  while health of Arnaldor is 2 \n Tony go to the DOWN and LEFT and  attack with a KICK \n The health of Arnaldor is 1  while health of Tony is 4 \n Arnaldor go to the LEFT and  attack with a REMUYUKEN  \n The health of Tony is 1  while health of Arnaldor is 1 \n Tony use TALADOKEN \n The health of Arnaldor is -2  while health of Tony is 1 \n Tony  killed Arnaldor the energy of Tony is 1 \n There is no more moves, the battle has ended and the winner is Tony with 1 while Arnaldor has only -2 of life ",
        "winner": "Tony",
        "loser": "Arnaldor",
    },
}


@pytest.mark.parametrize("instruction, response", instructions_mapper.items())
def test_game(instruction, response):
    player1 = Tony()
    player2 = Arnaldor()
    game = Game(open_json(instruction).dict(), player_1=player1, player_2=player2)
    result = game.result
    assert {"winner": result["winner"], "loser": result["loser"]} == {
        "winner": response["winner"],
        "loser": response["loser"],
    }
