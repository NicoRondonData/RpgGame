import abc


class Special(abc.ABC):
    @abc.abstractmethod
    def __init__(self, combination, energy):
        pass

    @abc.abstractmethod
    def combination(self):
        pass

    @abc.abstractmethod
    def energy(self):
        pass

    @abc.abstractmethod
    def name(self):
        pass


class Player(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_moves(self, moves) -> dict:
        pass
