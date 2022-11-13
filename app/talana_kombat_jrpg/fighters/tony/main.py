from app.talana_kombat_jrpg.constants import ENERGY, TONY_REMUYUKEN_COMBINATION, TONY_REMUYUKEN_ENERGY, TONY_TALADOKEN_ENERGY, \
    TONY_TALADOKEN_COMBINATION, TALADOKEN_NAME, REMUYUKEN_NAME
from app.talana_kombat_jrpg.fighters.base import Player
from app.talana_kombat_jrpg.utils import GenerateMoves
from app.talana_kombat_jrpg.moves import Attacks, replace_values_string


class Tony(Player):
    def __init__(self):
        self.energy = ENERGY
        self.name = self.__class__.__name__

    def get_moves(self, moves):
        moves_message = replace_values_string(moves)
        if TONY_TALADOKEN_COMBINATION in moves_message:
            return GenerateMoves.special(self.name, moves_message, TONY_TALADOKEN_COMBINATION,
                                         TONY_TALADOKEN_ENERGY, TALADOKEN_NAME)
        elif TONY_REMUYUKEN_COMBINATION in moves_message:
            return GenerateMoves.special(self.name, moves_message, TONY_REMUYUKEN_COMBINATION,
                                         TONY_REMUYUKEN_ENERGY, REMUYUKEN_NAME)

        elif Attacks.K.value in moves_message or Attacks.P.value in moves_message:
            if Attacks.K.value in moves_message:
                return GenerateMoves.basic_attack(self.name, moves_message, Attacks.K)

            if Attacks.P.value in moves_message:
                return GenerateMoves.basic_attack(self.name, moves_message, Attacks.P)
        else:
            return GenerateMoves.basic_moves(self.name, moves_message)
        return {}
