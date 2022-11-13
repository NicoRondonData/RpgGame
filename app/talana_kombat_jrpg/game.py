from typing import List
import itertools

from app.talana_kombat_jrpg.buffer.buffeer import Buffer
from app.talana_kombat_jrpg.constants import INITIAL_MESSAGE
from app.talana_kombat_jrpg.utils import concatenate_message


class ConstructGameInstructions:
    def __init__(self, data):
        self.data = data
        self.player1 = None
        self.player2 = None

    def __values_for_player(self, player: str):
        print(player)
        player = {
            "attacks": len("".join(self.data[player]["golpes"])),
            "instructions": len("".join(self.data[player]["instructions"])),
            "moves": len("".join(self.data[player]["movimientos"])),
            "player": player,
            "game_moves": self.data[player]["instructions"]
        }
        return player

    def __get_minimun(self, player1: dict, player2: dict, action: str) -> List:
        value = sorted([player1, player2], key=lambda d: d[action])
        return value

    def verify_start(self):

        self.player1 = self.__values_for_player("player1")
        self.player2 = self.__values_for_player("player2")
        self.player1["enemy"] = "player2"
        self.player2["enemy"] = "player1"
        players_instructions = self.__get_minimun(self.player1, self.player2, "instructions")
        players_moves = self.__get_minimun(self.player1, self.player2, "moves")
        players_attacks = self.__get_minimun(self.player1, self.player2, "attacks")
        if self.player1["instructions"] != self.player2["instructions"]:
            return players_instructions
        elif self.player1["instructions"] == self.player2["instructions"]:
            return players_moves
        elif self.player1["moves"] == self.player2["moves"]:
            return players_attacks
        elif self.player1["attacks"] == self.player2["attacks"]:
            return [self.player1, self.player2]

    @classmethod
    def get_instructions(cls, player):
        return [
            {
                "player": player["player"],
                "enemy": player["enemy"],
                "move": move
            } for move in player["game_moves"]
        ]


class PlayGame:
    def __init__(self, first_player, second_player, fighters):
        self.first_player = first_player
        self.second_player = second_player
        self.__result = None
        self.fighters = fighters

    def __make_buffer(self,
                      buffer_instruction: str = "FIFO"):
        buffer = Buffer(buffer_instruction)
        for x, y in itertools.zip_longest(self.first_player, self.second_player):
            if x:
                buffer.insert(x)
            if y:
                buffer.insert(y)
        return buffer

    def __sort_fighters(self, fighters):
        fighters_sorted = sorted(fighters, key=lambda x: x.energy, reverse=True)
        return  fighters_sorted

    def __generate_result(self, buffer):
        principal_fighter = None
        enemy_fighter = None
        full_message = [INITIAL_MESSAGE]

        while buffer.count > 0:
            fighter_info = buffer.extract()
            principal_fighter = self.fighters[fighter_info["player"]]
            enemy_fighter = self.fighters[fighter_info["enemy"]]
            move = principal_fighter.get_moves(fighter_info["move"])
            enemy_fighter.energy -= move["energy"]
            move_message = move["message"]
            full_message.append(move_message)
            explanation_message = f"The health of {enemy_fighter.name} is {enemy_fighter.energy}  while health of {principal_fighter.name} is {principal_fighter.energy}"
            full_message.append(explanation_message)
            if enemy_fighter.energy <= 0:
                kill_message = f"{principal_fighter.name}  killed {enemy_fighter.name} the energy of {principal_fighter.name} is {principal_fighter.energy}"
                full_message.append(kill_message)
                break

        fighters_sorted = self.__sort_fighters([principal_fighter, enemy_fighter])
        final_message = f"There is no more moves, the battle has ended and the winner is {fighters_sorted[0].name} with {fighters_sorted[0].energy} while {fighters_sorted[-1].name} has only {fighters_sorted[-1].energy} of life "
        full_message.append(final_message)
        message = concatenate_message(full_message)
        return {
            "player": principal_fighter.name,
            "player_energy": principal_fighter.energy,
            "enemy": enemy_fighter.name,
            "enemy_energy": enemy_fighter.energy,
            "message": message,
            "winner": fighters_sorted[0].name,
            "loser": fighters_sorted[-1].name
        }

    @property
    def result(self):
        buffer = self.__make_buffer()
        result = self.__generate_result(buffer)
        return result