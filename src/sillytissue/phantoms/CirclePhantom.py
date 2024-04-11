import random
import numpy as np

from sillytissue.cells.celltypes import RLCType, CCType, LC1Type, LC2Type, NCType, LWCType
from sillytissue.phantoms import CirclePhantomDistribution


class CirclePhantom:
    """The CirclePhantom class represents a sample of worlds of circles defined by CirclePhantomDistribution."""

    def __init__(self, cpd: CirclePhantomDistribution) -> None:
        self.cpd = cpd
        self.circles = []
        self.sample_circles()

    def sample_circles(self):
        """Sample from the CirclePhantom distribution and returns one circle world sample.
        The number of circles is sampled from a normal distribution with mean num_circles_mean but will always be at least 1"""

        self.circles = []
        for _ in range(self.cpd.num_circles):
            x = np.random.uniform(0, 1)
            y = np.random.uniform(0, 1)
            z = np.random.uniform(0, 1)
            radius = np.random.normal(self.cpd.radius_mean, self.cpd.radius_sigma)
            self.circles.append((x, y, z, radius))

    def get_RLC_location(self) -> tuple:
        """Sample a location for a RLC cell. Those cells are placed uar in the unit square."""

        return np.random.uniform(0, 1), np.random.uniform(0, 1), np.random.uniform(0, 1)

    def get_CC_location(self, cct:CCType, attempts=1000) -> tuple:
        """Sample a location for a CC cell. Those cells are placed nearby circles."""

        min_prob = np.random.uniform(.5,1)

        while attempts > 0:
            x = np.random.uniform(0, 1)
            y = np.random.uniform(0, 1)
            z = np.random.uniform(0, 1)
            for cx, cy, cz, r in self.circles:
                dist_from_circle = np.sqrt((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2)
                prob = cct.get_location_prob(dist_from_circle)
                if prob >= min_prob:
                    return x, y, z
            attempts -= 1
        return -1, -1, -1

    def get_LC1_location(self, lc1t:LC1Type, attempts=100) -> tuple:
        """Sample a location for a LC1 cell. Those cells are placed nearby circle centers."""

        min_prob = np.random.uniform(0,1)

        while attempts > 0:
            cx,cy,cz,r = random.choice(self.circles)
            x = np.random.uniform( max(0,cx-r), min(1,cx+r) )
            y = np.random.uniform( max(0,cy-r), min(1,cy+r) )
            z = np.random.uniform( max(0,cz-r), min(1,cz+r) )
            norm_dist_from_center = np.sqrt((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2) / r
            prob = lc1t.get_location_prob(norm_dist_from_center)
            if prob >= min_prob:
                return x, y, z
            attempts -= 1
        return -1, -1, -1

    def get_LC2_location(self, lc2t:LC2Type, attempts=100) -> tuple:
        """Sample a location for a LC2 cell. Those cells are placed inside circles but nearby the outside."""

        min_prob = np.random.uniform(0,1)

        while attempts > 0:
            cx,cy,cz,r = random.choice(self.circles)
            x = np.random.uniform( max(0,cx-r), min(1,cx+r) )
            y = np.random.uniform( max(0,cy-r), min(1,cy+r) )
            z = np.random.uniform( max(0,cz-r), min(1,cz+r) )
            norm_dist_from_center = np.sqrt((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2) / r
            prob = lc2t.get_location_prob(norm_dist_from_center)
            if prob >= min_prob:
                return x, y, z
            attempts -= 1
        return -1, -1, -1

    def get_NC_location(self, nct:NCType, attempts=1000) -> tuple:
        """Sample a location for a NC cell. Those cells are placed outside circles but nearby the rim."""

        min_prob = np.random.uniform(0,1)

        while attempts > 0:
            x = np.random.uniform(0, 1)
            y = np.random.uniform(0, 1)
            z = np.random.uniform(0, 1)
            go = True
            for cx,cy,cz,r in self.circles:
                dist_to_center = np.sqrt((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2)
                if dist_to_center < r:
                    go = False
                    break
            if go:
                for cx,cy,cz,r in self.circles:
                    dist_to_center = np.sqrt((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2)
                    norm_dist_from_center = dist_to_center / r
                    prob = nct.get_location_prob(norm_dist_from_center)
                    if prob >= min_prob:
                        return x, y, z
            attempts -= 1
        return -1, -1
    
    def get_LWC_location(self, lwct:LWCType, attempts=1000) -> tuple:
        """Sample a location for a NC cell. Those cells are placed outside circles but nearby the rim."""

        min_prob = np.random.uniform(0,1)

        while attempts > 0:
            x = np.random.uniform(0, 1)
            y = np.random.uniform(0, 1)
            z = np.random.uniform(0, 1)
            go = True
            for cx,cy,cz,r in self.circles:
                dist_to_center = np.sqrt((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2)
                if dist_to_center < r * lwct.norm_min_dist_from_center:
                    go = False
                    break
            if go:
                for cx,cy,cz,r in self.circles:
                    dist_to_center = np.sqrt((x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2)
                    norm_dist_from_center = dist_to_center / r
                    prob = lwct.get_location_prob(norm_dist_from_center)
                    if prob >= min_prob:
                        return x, y, z
            attempts -= 1
        return -1, -1, -1
