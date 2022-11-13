
from app.talana_kombat_jrpg.fighters.arnaldor.main import Arnaldor
from app.talana_kombat_jrpg.fighters.tony.main import Tony
from app.talana_kombat_jrpg.game import ConstructGameInstructions, PlayGame

mapper_fighter = {
    "player1": Tony(),
    "player2": Arnaldor(),
}


class Game:
    def __init__(self, data):
        self.data = data

    def play(self):
        start = ConstructGameInstructions(data=self.data).verify_start()
        first_player = start[0]
        second_player = start[1]
        first_player_game_instructions = ConstructGameInstructions.get_instructions(first_player)
        second_player_game_instructions = ConstructGameInstructions.get_instructions(second_player)
        game = PlayGame(
            first_player_game_instructions,
            second_player_game_instructions,
            mapper_fighter
        )
        return game.result


