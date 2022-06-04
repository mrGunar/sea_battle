"""
Game objects
"""
from random import randint
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Coord:
    """Class heandler for coords"""
    coord_x: int
    coord_y: int


class ObjectShip(ABC):
    """Abstract ship"""
    @abstractmethod
    def set_start_coords(self, coord: Coord) -> None:
        """Set start coords"""

    @abstractmethod
    def get_start_coords(self) -> Coord:
        """Get ship's coords"""


class Ship(ObjectShip):
    """Class for object Ship"""
    def __init__(self, length: int, coord=Coord(None, None), tp=1) -> None:
        self._coord_x = coord.coord_x
        self._coord_y = coord.coord_y
        self._length = length
        self._tp = tp
        self._cells = [1] * length

    def set_start_coords(self, coord: Coord) -> None:
        self._coord_x = coord.coord_x
        self._coord_y = coord.coord_y

    def get_start_coords(self) -> Coord:
        return Coord(self._coord_x, self._coord_y)

    def __getitem__(self, indx):
        return self._cells[indx]

    def __setitem__(self, indx, value):
        self._cells[indx] = value


class OneDeckShip:
    """Class for create one-deck ship"""
    @classmethod
    def create_ship(cls):
        return Ship(1, tp=randint(1, 2))


class DoubleDeckShip:
    """Class for create double-deck ship"""
    @classmethod
    def create_ship(cls):
        return Ship(2, tp=randint(1, 2))


class ThreeDeckShip:
    """Class for create three-deck ship"""
    @classmethod
    def create_ship(cls):
        return Ship(3, tp=randint(1, 2))


class FourDeckShip:
    """Class for create four-deck ship"""
    @classmethod
    def create_ship(cls):
        return Ship(4, tp=randint(1, 2))


class GamePole:
    """Class for provide work with game field"""
    def __init__(self, size=10):
        self._size = size

    def init(self):
        self._ships = [
            FourDeckShip.create_ship(),
            ThreeDeckShip.create_ship(),
            ThreeDeckShip.create_ship(),
            DoubleDeckShip.create_ship(),
            DoubleDeckShip.create_ship(),
            DoubleDeckShip.create_ship(),
            OneDeckShip.create_ship(),
            OneDeckShip.create_ship(),
            OneDeckShip.create_ship(),
            OneDeckShip.create_ship(),
        ]

    def arrange_ships(self):
        """Function for arrange ships on field"""

    def get_ship(self) -> None:
        return self._ships

    def show(self): pass
