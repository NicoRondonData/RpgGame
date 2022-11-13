from app.talana_kombat_jrpg.constants import REMUYUKEN_NAME, TALADOKEN_NAME
from app.talana_kombat_jrpg.fighters.base import Special


class Taladoken(Special):

    def __init__(self,  combination, energy ):
        self.__combination = combination
        self.__energy = energy
        self.__name = REMUYUKEN_NAME

    @property
    def combination(self):
        return self.__combination

    @property
    def energy(self):
        return self.__energy

    @property
    def name(self):
        return self.__name


class Remuyuken(Special):
    def __init__(self, combination, energy):
        self.__combination = combination
        self.__energy = energy
        self.__name = TALADOKEN_NAME

    @property
    def combination(self):
        return self.__combination

    @property
    def energy(self):
        return self.__energy

    @property
    def name(self):
        return self.__name

