from types import CellType
from abc import ABC
from sillytissue.cells.celltypes import CellType

class Cell(ABC):
    """Abstract Cell class"""
    def __init__(self, ct:CellType, x:float, y:float, z:float, r:float):
        self.ct = ct
        self.x = x
        self.y = y
        self.z = z
        self.radius = r
        self.color = ct.color

    def __str__(self):
        return "Celltype " + self.ct.name + " at " + str(self.x) + ", " + str(self.y) + ", " + str(self.z)

class CircleCell(Cell):
    """A Circle Cell"""
    def __init__(self, ct:CellType, x:float, y:float, z:float, r:float):
        self.ct = ct
        self.x = x
        self.y = y
        self.z = z
        self.radius = r
        self.color = ct.color

class LumenCell1:
    """Lumen Cell 1 - the one to prefer the center of the lumen."""
    def __init__(self, ct:CellType, x:float, y:float, z:float, r:float):
        self.ct = ct
        self.x = x
        self.y = y
        self.z = z
        self.radius = r
        self.color = ct.color

class CircleCell(Cell):
    """A Circle Cell"""
    def __init__(self, ct:CellType, x:float, y:float, z:float, r:float):
        self.ct = ct
        self.x = x
        self.y = y
        self.z = z
        self.radius = r
        self.color = ct.color
 

class LumenCell2(Cell):
    """Lumen Cell 2 - the one to prefer the periphery of the lumen."""
    def __init__(self, ct:CellType, x:float, y:float, z:float, r:float):
        self.ct = ct
        self.x = x
        self.y = y
        self.z = z
        self.radius = r
        self.color = ct.color


class LoneleyWolfCell(Cell):
    """Lone Wolf Cells - the ones to prefer to be alone, away from the cirlces."""
    def __init__(self, ct:CellType, x:float, y:float, z:float, r:float):
        self.ct = ct
        self.x = x
        self.y = y
        self.z = z
        self.radius = r
        self.color = ct.color


class NearbyCells(Cell):
    """Nearby Cells - the ones that like to be around circles but outside the lumen."""
    def __init__(self, ct:CellType, x:float, y:float, z:float, r:float):
        self.ct = ct
        self.x = x
        self.y = y
        self.z = z
        self.radius = r
        self.color = ct.color


class RandomLittleCell(Cell):
    """Random Little Cell"""
    def __init__(self, ct:CellType, x:float, y:float, z:float, r:float):
        self.ct = ct
        self.x = x
        self.y = y
        self.z = z
        self.radius = r
        self.color = ct.color
