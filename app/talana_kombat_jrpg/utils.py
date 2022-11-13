import json

from app.talana_kombat_jrpg.constants import BASIC_ATTACK
from app.talana_kombat_jrpg.fighters.specials import Remuyuken, Taladoken
from app.talana_kombat_jrpg.moves import Attacks
from app.talana_kombat_jrpg.serializers import GameSchema


class GenerateMoves:
    @classmethod
    def special(
        cls,
        name_fighter: str,
        moves_message: str,
        combination: str,
        energy: int,
        special_name: str,
    ) -> dict:
        special = None
        if special_name == "TALADOKEN":
            special = Taladoken(combination, energy)
        if special_name == "REMUYUKEN":
            special = Remuyuken(combination, energy)
        prev_move = moves_message.split(combination)
        if prev_move[0]:
            move = prev_move[0].replace("-", " and ")
            final = (
                f"{name_fighter} go to the {move} attack with a {special.name.upper()} "
            )
        else:
            final = f"{name_fighter} use {special.name.upper()}"
        return {
            "energy": special.energy,
            "combination": special.combination,
            "name": special.name,
            "message": final,
        }

    @classmethod
    def basic_attack(cls, name_fighter, moves_message, type_attack):
        if type_attack.value in moves_message:
            if len(moves_message) > len(type_attack.value):
                prev_move = moves_message.split(type_attack.value)
                if prev_move[0]:
                    move = prev_move[0].replace("-", " and ")
                    final = f"{name_fighter} go to the {move} attack with a {type_attack.value}"
                    return {
                        "energy": BASIC_ATTACK,
                        "combination": Attacks.K.value,
                        "name": Attacks.K.value,
                        "message": final,
                    }
            else:
                return {
                    "energy": BASIC_ATTACK,
                    "combination": type_attack.value,
                    "name": type_attack.value,
                    "message": f"{name_fighter}  attack with a {type_attack.value}",
                }

    @classmethod
    def basic_moves(
        cls,
        name_fighter,
        moves_message,
    ):
        move = moves_message.replace("-", " and ")
        final = f"{name_fighter} go to the {move} then  stop"
        return {
            "energy": 0,
            "combination": moves_message,
            "name": "move",
            "message": final,
        }


def open_json(name_file):
    with open(name_file) as game_instructions:
        data = json.load(game_instructions)
        return GameSchema(**data)


def concatenate_message(message_list):
    return " \n ".join(message_list)
