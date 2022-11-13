from app.talana_kombat_jrpg.constants import (
    ARNOLD_REMUYUKEN_COMBINATION,
    ARNOLD_REMUYUKEN_ENERGY,
    ARNOLD_TALADOKEN_COMBINATION,
    ARNOLD_TALADOKEN_ENERGY,
    ENERGY,
    REMUYUKEN_NAME,
    TALADOKEN_NAME,
)
from app.talana_kombat_jrpg.fighters.base import Player
from app.talana_kombat_jrpg.moves import Attacks, replace_values_string
from app.talana_kombat_jrpg.utils import GenerateMoves


class Arnaldor(Player):
    def __init__(self):
        self.energy = ENERGY
        self.name = self.__class__.__name__

    def get_moves(self, moves):
        moves_message = replace_values_string(moves)
        if ARNOLD_TALADOKEN_COMBINATION in moves_message:
            return GenerateMoves.special(
                self.name,
                moves_message,
                ARNOLD_TALADOKEN_COMBINATION,
                ARNOLD_TALADOKEN_ENERGY,
                TALADOKEN_NAME,
            )

        elif ARNOLD_REMUYUKEN_COMBINATION in moves_message:
            return GenerateMoves.special(
                self.name,
                moves_message,
                ARNOLD_REMUYUKEN_COMBINATION,
                ARNOLD_REMUYUKEN_ENERGY,
                REMUYUKEN_NAME,
            )
        elif Attacks.K.value in moves_message or Attacks.P.value in moves_message:
            if Attacks.K.value in moves_message:
                return GenerateMoves.basic_attack(self.name, moves_message, Attacks.K)

            if Attacks.P.value in moves_message:
                return GenerateMoves.basic_attack(self.name, moves_message, Attacks.P)
        else:
            return GenerateMoves.basic_moves(self.name, moves_message)

        return {}
