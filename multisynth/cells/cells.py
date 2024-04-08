from types import CellType

import numpy as np
from scipy.stats import norm

from multisynth.cells.celltypes import CCType, LC1Type, LC2Type, LWCType, NCType

class CircleCell:
    """A Circle Cell"""

    def __init__(self, cct:CCType, x:float, y:float, r:float):
        self.cct = cct
        self.x = x
        self.y = y
        self.radius = r
        self.color = cct.color

    def __str__(self):
        return "Celltype " + self.cct.name + " at " + str(self.x) + ", " + str(self.y)
    

class LumenCell1:
    """Lumen Cell 1 - the one to prefer the center of the lumen."""

    def __init__(self, lc1t:LC1Type, x:float, y:float, r:float):
        self.lc1t = lc1t
        self.x = x
        self.y = y
        self.radius = r
        self.color = lc1t.color

    def __str__(self):
        return "Celltype " + self.lc1t.name + " at " + str(self.x) + ", " + str(self.y)


class LumenCell2:
    """Lumen Cell 2 - the one to prefer the periphery of the lumen."""

    def __init__(self, lc2t:LC2Type, x:float, y:float, r:float):
        self.lc2t = lc2t
        self.x = x
        self.y = y
        self.radius = r
        self.color = lc2t.color

    def __str__(self):
        return "Celltype " + self.lc2t.name + " at " + str(self.x) + ", " + str(self.y)


class LoneleyWolfCell:
    """Lone Wolf Cells - the ones to prefer to be alone, away from the cirlces."""

    def __init__(self, lwct:LWCType, x:float, y:float, r:float):
        self.lwct = lwct
        self.x = x
        self.y = y
        self.radius = r
        self.color = lwct.color

    def __str__(self):
        return "Celltype " + self.lwct.name + " at " + str(self.x) + ", " + str(self.y)


class NearbyCells:
    """Nearby Cells - the ones that like to be around circles but outside the lumen."""

    def __init__(self, nct:NCType, x:float, y:float, r:float):
        self.nct = nct
        self.x = x
        self.y = y
        self.radius = r
        self.color = nct.color

    def __str__(self):
        return "Celltype " + self.nct.name + " at " + str(self.x) + ", " + str(self.y)


class RandomLittleCell:
    """Random Little Cell"""

    def __init__(self, rlct:NCType, x:float, y:float, radius:float):
        self.rlct = rlct
        self.x = x
        self.y = y
        self.radius = radius
        self.color = rlct.color

    def __str__(self):
        return "Celltype " + self.rlct.name + " at " + str(self.x) + ", " + str(self.y)
