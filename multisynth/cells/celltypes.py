from abc import ABC

import numpy as np
from scipy.stats import norm

class CellType(ABC):
    """Class that defines the cell type object"""

    def __init__(self, name, props=None):
        self.name = name
        self.props = props
        self.instances = []

    def __str__(self):
        return "Celltype " + self.name
    
    def add_instance(self, instance):
        self.instances.append(instance)

    def purge_instances(self):
        self.instances = []


class CCType(CellType):
    """Circle Cell"""

    def __init__(self, attempts_to_add:int, dist_from_circle_sigma:float, r_mean:float, r_sigma:float, color:tuple):
        """Circle Cell Constructor"""
        super().__init__("CC")
        self.attempts_to_add = attempts_to_add
        self.dist_from_circle_sigma = dist_from_circle_sigma
        self.r_mean = r_mean
        self.r_sigma = r_sigma
        self.color = color

    def sample_radius(self)->float:
        return np.random.normal(self.r_mean, self.r_sigma)    

    def get_location_prob(self, distance_from_circle):
        """Calculate the probability of a location based on the distance from a circle."""
        value = norm.pdf(distance_from_circle, 0, self.dist_from_circle_sigma)
        maximum = norm.pdf(0,0,self.dist_from_circle_sigma)
        return value/maximum


class LC1Type(CellType):
    """Lumen Cells Type 1"""

    def __init__(self,attempts_to_add:int, norm_dist_from_center_sigma:float, r_mean:float, r_sigma:float, color:tuple ):
        super().__init__("LC1")
        self.attempts_to_add = attempts_to_add
        self.norm_dist_from_center_sigma = norm_dist_from_center_sigma
        self.r_mean = r_mean
        self.r_sigma = r_sigma
        self.color = color

    def sample_radius(self)->float:
        return np.random.normal(self.r_mean, self.r_sigma)    

    def get_location_prob(self, norm_distance_from_center):
        """Calculate the probability of a location based on the distance from a circle."""
        value = norm.pdf(norm_distance_from_center, 0, self.norm_dist_from_center_sigma)
        maximum = norm.pdf(0,0,self.norm_dist_from_center_sigma)
        return value/maximum


class LC2Type(CellType):
    """Lumen Cells Type 2"""

    def __init__(self,attempts_to_add:int, norm_dist_from_center_mu: float, norm_sigma:float, r_mean:float, r_sigma:float, color:tuple ):
        super().__init__("LC2")
        self.attempts_to_add = attempts_to_add
        self.norm_dist_from_center_mu = norm_dist_from_center_mu
        self.norm_sigma = norm_sigma
        self.r_mean = r_mean
        self.r_sigma = r_sigma
        self.color = color

    def sample_radius(self)->float:
        return np.random.normal(self.r_mean, self.r_sigma)    

    def get_location_prob(self, norm_distance_from_center):
        """Calculate the probability of a location based on the distance from a circle."""
        if norm_distance_from_center > 1:
            return 0
        value = norm.pdf(norm_distance_from_center, self.norm_dist_from_center_mu, self.norm_sigma)
        maximum = norm.pdf(0,0,self.norm_sigma)
        return value/maximum


class NCType(CellType):
    """Nearby Cells"""

    def __init__(self,attempts_to_add:int, norm_dist_from_center_mu: float, norm_sigma:float, r_mean:float, r_sigma:float, color:tuple ):
        super().__init__("NC")
        self.attempts_to_add = attempts_to_add
        self.norm_dist_from_center_mu = norm_dist_from_center_mu
        self.norm_sigma = norm_sigma
        self.r_mean = r_mean
        self.r_sigma = r_sigma
        self.color = color

    def sample_radius(self)->float:
        return np.random.normal(self.r_mean, self.r_sigma)    

    def get_location_prob(self, norm_distance_from_center):
        """Calculate the probability of a location based on the distance from a circle."""
        if norm_distance_from_center <= 1:
            return 0
        value = norm.pdf(norm_distance_from_center, self.norm_dist_from_center_mu, self.norm_sigma)
        maximum = norm.pdf(0,0,self.norm_sigma)
        return value/maximum


class LWCType(CellType):
    """Random Little Cell"""

    def __init__(self, attempts_to_add:int, norm_min_dist_from_center:float, r_mean:float, r_sigma:float, color:tuple):
        super().__init__("LWC")
        self.attempts_to_add = attempts_to_add
        self.norm_min_dist_from_center = norm_min_dist_from_center
        self.r_mean = r_mean
        self.r_sigma = r_sigma
        self.color = color

    def sample_radius(self)->float:
        return np.random.normal(self.r_mean, self.r_sigma)    

    def get_location_prob(self, norm_distance_from_center):
        """Calculate the probability of a location based on the distance from a circle."""
        if norm_distance_from_center < self.norm_min_dist_from_center:
            return 0
        else:
            return 1


class RLCType(CellType):
    """Random Little Cell"""

    def __init__(self, num_mean:float, num_sigma:float, r_mean:float, r_sigma:float, color:tuple)->None:
        super().__init__("RLC")
        self.num_mean = num_mean
        self.num_sigma = num_sigma
        self.r_mean = r_mean
        self.r_sigma = r_sigma
        self.color = color

    def sample_count(self)->int:
        return int( np.round(np.random.normal(self.num_mean, self.num_sigma) ) )

    def sample_radius(self)->float:
        return np.random.normal(self.r_mean, self.r_sigma)    
