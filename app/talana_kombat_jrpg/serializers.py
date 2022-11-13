from typing import List, Optional

from pydantic import BaseModel, ValidationError, validator

from app.talana_kombat_jrpg.constants import (
    ALLOWED_KEYS,
    ALLOWED_NUMBER_OF_ATTACKS,
    ALLOWED_NUMBER_OF_MOVES,
)


class GameBase(BaseModel):
    movimientos: List[str]
    golpes: List[str]
    instructions: Optional[str] = None

    @classmethod
    def __allow_moves(self, v):
        v = [x.upper() for x in v]
        for instruction in v:
            if any(c not in ALLOWED_KEYS for c in instruction):
                raise ValidationError(
                    f"The only keys allowed are {ALLOWED_KEYS} you are using {v}"
                )

        return v

    @validator("movimientos")
    def moves_allowed_are(cls, v):
        for move in v:
            if len(move) > ALLOWED_NUMBER_OF_MOVES:
                raise ValueError(
                    f"The max number of moves are {ALLOWED_NUMBER_OF_MOVES}"
                )
        return cls.__allow_moves(v)

    @validator("golpes")
    def attacks_allowed_are(cls, v):
        for move in v:
            if len(move) > ALLOWED_NUMBER_OF_ATTACKS:
                raise ValueError(
                    f"The max number of attacks are {ALLOWED_NUMBER_OF_ATTACKS}"
                )
        return cls.__allow_moves(v)

    @validator("instructions", always=True)
    def generate_instruction(cls, v, values):
        try:
            if "movimientos" in values:
                moves = values["movimientos"]
            else:
                raise ValueError()
            if "golpes" in values:
                attack = values["golpes"]
            else:
                raise ValueError()
            z = list(map("".join, zip(moves, attack)))
            return z
        except IndexError:
            pass


class GameSchema(BaseModel):
    player1: GameBase
    player2: GameBase


class GameResponseSchema(BaseModel):
    player: str
    player_energy: int
    enemy: str
    enemy_energy: int
    message: str
    winner: str
    loser: str
