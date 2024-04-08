import numpy as np

from multisynth.cells.cells import CircleCell, LoneleyWolfCell, LumenCell1, LumenCell2, NearbyCells, RandomLittleCell
from multisynth.cells.celltypes import RLCType, CCType, LC1Type, LC2Type, NCType, LWCType
from multisynth.phantoms.CirclePhantom import CirclePhantom


class CirclePhantomSample:
    """
    Represents a sample from a CirclePhantom which in turn is a sample from CirclePhantomDistribution.
    """

    def __init__(self, cp: CirclePhantom, rlct:RLCType, cct:CCType, lc1t:LC1Type, lc2t: LC2Type, nct:NCType, lwct:LWCType) -> None:
        self.circle_phantom = cp

        self.rlct = rlct
        self.cct = cct
        self.lc1t = lc1t
        self.lc2t = lc2t
        self.nct = nct
        self.lwct = lwct

        self.rlcs = []
        self.ccs = []
        self.lc1s = []
        self.lc2s = []
        self.ncs = []
        self.lwcs = []

        for _ in range(self.rlct.sample_count()):
            x,y = self.circle_phantom.get_RLC_location()
            rlc = RandomLittleCell( self.rlct, x, y, self.rlct.sample_radius() )
            self.rlcs.append(rlc)

        attempts_remaining = self.cct.attempts_to_add
        while attempts_remaining > 0:
            x,y = self.circle_phantom.get_CC_location(self.cct)
            if x == -1: 
                x,y = self.circle_phantom.get_RLC_location()

            r = self.cct.sample_radius()
            if self.is_location_free(x, y, r):
                self.ccs.append( CircleCell(self.cct, x, y, r) )
                attempts_remaining = self.cct.attempts_to_add
            attempts_remaining -= 1

        attempts_remaining = self.lc1t.attempts_to_add
        while attempts_remaining > 0:
            x,y = self.circle_phantom.get_LC1_location(self.lc1t)
            if x == -1: 
                x,y = self.circle_phantom.get_RLC_location()

            r = self.lc1t.sample_radius()
            if self.is_location_free(x, y, r):
                self.lc1s.append( LumenCell1(self.lc1t, x, y, r) )
                attempts_remaining = self.lc1t.attempts_to_add
            attempts_remaining -= 1

        attempts_remaining = self.lc2t.attempts_to_add
        while attempts_remaining > 0:
            x,y = self.circle_phantom.get_LC2_location(self.lc2t)
            if x == -1: 
                x,y = self.circle_phantom.get_RLC_location()

            r = self.lc2t.sample_radius()
            if self.is_location_free(x, y, r):
                self.lc2s.append( LumenCell2(self.lc2t, x, y, r) )
                attempts_remaining = self.lc2t.attempts_to_add
            attempts_remaining -= 1

        attempts_remaining = self.nct.attempts_to_add
        while attempts_remaining > 0:
            x,y = self.circle_phantom.get_NC_location(self.nct)
            if x == -1: 
                attempts_remaining -= 1
                continue

            r = self.nct.sample_radius()
            if self.is_location_free(x, y, r):
                self.ncs.append( NearbyCells(self.nct, x, y, r) )
                attempts_remaining = self.nct.attempts_to_add
            attempts_remaining -= 1

        attempts_remaining = self.lwct.attempts_to_add
        while attempts_remaining > 0:
            x,y = self.circle_phantom.get_LWC_location(self.lwct)
            if x == -1: 
                attempts_remaining -= 1
                continue

            r = self.lwct.sample_radius()
            if self.is_location_free(x, y, r):
                self.lwcs.append( LoneleyWolfCell(self.lwct, x, y, r) )
                attempts_remaining = self.lwct.attempts_to_add
            attempts_remaining -= 1


    def is_location_free(self, x:float, y:float, r:float)->bool:
        cell_list = [self.rlcs, self.ccs, self.lc1s, self.lc2s, self.ncs, self.lwcs]
        
        for cells in cell_list:
            for cell in cells:
                if np.sqrt((cell.x - x)**2 + (cell.y - y)**2) < cell.radius + r:
                    return False
        return True