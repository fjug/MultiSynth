import numpy as np

class Shape:
    ''' Defines the Shape statistics and how samples are generated from it.'''

    class Ellipse:
        def __init__(self, major_axis, minor_axis, angle):
            self.major_axis = major_axis
            self.minor_axis = minor_axis
            self.angle = angle

        def area(self):
            from math import pi
            return pi * self.major_axis * self.minor_axis

        def circumference(self):
            from math import pi, sqrt
            # Approximation
            return 2 * pi * sqrt((self.major_axis**2 + self.minor_axis**2) / 2)
        
    def __init__(self, major_axis_mean, major_axis_sigma, minor_axis_mean, minor_axis_sigma, discrete_angle_distribution):
        assert isinstance(discrete_angle_distribution, list), 'Discrete angle distribution must be a list'  
        assert np.sum(discrete_angle_distribution) == 1, 'Discrete angle distribution must sum to 1'

        self.major_axis_mean = major_axis_mean
        self.major_axis_sigma = major_axis_sigma
        self.minor_axis_mean = minor_axis_mean
        self.minor_axis_sigma = minor_axis_sigma
        self.discrete_angle_distribution = discrete_angle_distribution

    def sample(self):
        ''' Sample from the Mu distribution '''

        major_axis = np.random.normal(self.major_axis_mean, self.major_axis_sigma)
        minor_axis = np.random.normal(self.minor_axis_mean, self.minor_axis_sigma)
        angle = np.random.choice(range(len(self.discrete_angle_distribution)), p=self.discrete_angle_distribution)
        angle = 2 * np.pi * angle / len(self.discrete_angle_distribution)

        return major_axis, minor_axis, angle