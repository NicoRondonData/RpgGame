from enum import Enum


class Moves(Enum):
    W = "UP"
    S = "DOWN"
    A = "LEFT"
    D = "RIGHT"


class Attacks(Enum):
    P = "FIST"
    K = "KICK"


def replace_values_string(my_str):
    new_str_list = []
    instructions = {
        "W": "UP",
        "S": "DOWN",
        "A": "LEFT",
        "D": "RIGHT",
        "P": "FIST",
        "K": "KICK",
    }
    for c in my_str:
        new_str_list.append(instructions[c])

    return "-".join(new_str_list)
