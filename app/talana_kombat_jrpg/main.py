from app.talana_kombat_jrpg.fighters.arnaldor.main import Arnaldor
from app.talana_kombat_jrpg.fighters.tony.main import Tony
from app.talana_kombat_jrpg.game import ConstructGameInstructions, PlayGame

mapper_fighter = {"player1": Tony, "player2": Arnaldor}


class Game:
    def __init__(self, data, player_1, player_2):
        self.data = data
        self.player_1 = player_1
        self.player_2 = player_2

    @property
    def result(self):
        start = ConstructGameInstructions(data=self.data).verify_start()
        first_player = start[0]
        second_player = start[1]
        first_player_game_instructions = ConstructGameInstructions.get_instructions(
            first_player
        )
        second_player_game_instructions = ConstructGameInstructions.get_instructions(
            second_player
        )
        game = PlayGame(
            first_player_game_instructions,
            second_player_game_instructions,
            {"player1": self.player_1, "player2": self.player_2},
        )
        return game.result
