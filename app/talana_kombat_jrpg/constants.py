from app.talana_kombat_jrpg.moves import Moves, Attacks

INITIAL_MESSAGE = " Welcome to Talana Kombat JRPG "

ENERGY = 6
BASIC_ATTACK = 1
ALLOWED_KEYS = "AWSDKP"
ALLOWED_NUMBER_OF_MOVES = 5
ALLOWED_NUMBER_OF_ATTACKS = 1
TALADOKEN_NAME ="TALADOKEN"
REMUYUKEN_NAME = "REMUYUKEN"

ARNOLD_TALADOKEN_ENERGY =2
ARNOLD_TALADOKEN_COMBINATION = f"{Moves.A.value}-{Moves.S.value}-{Moves.A.value}-{Attacks.P.value}"
ARNOLD_REMUYUKEN_ENERGY = 3
ARNOLD_REMUYUKEN_COMBINATION = f"{Moves.S.value}-{Moves.A.value}-{Attacks.K.value}"


TONY_TALADOKEN_ENERGY =3
TONY_TALADOKEN_COMBINATION = f"{Moves.D.value}-{Moves.S.value}-{Moves.D.value}-{Attacks.P.value}"
TONY_REMUYUKEN_ENERGY = 2
TONY_REMUYUKEN_COMBINATION = f"{Moves.S.value}-{Moves.D.value}-{Attacks.K.value}"


