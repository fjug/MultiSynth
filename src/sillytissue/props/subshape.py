import numpy as np


class Subshape:
    """Defines the Subshape (i.e. fluorescent expression) statistics and
    how samples are generated from it.
    A Subshape is defined as a distribution of sinusoidal gratings
    that are given by angle, frequency, amplitude, and phase.
    """

    def __init__(
        self, 
        angle_mean, angle_sigma, 
        frequency_mean, frequency_sigma, 
        amplitude_mean, amplitude_sigma, 
        phase_mean, phase_sigma
    ):
        self.angle_mean = angle_mean
        self.angle_sigma = angle_sigma
        self.frequency_mean = frequency_mean
        self.frequency_sigma = frequency_sigma
        self.amplitude_mean = amplitude_mean
        self.amplitude_sigma = amplitude_sigma
        self.phase_mean = phase_mean
        self.phase_sigma = phase_sigma

    def sample(self):
        """Sample from the Subshape distribution"""

        angle = np.random.normal(self.angle_mean, self.angle_sigma)
        frequency = np.random.normal(self.frequency_mean, self.frequency_sigma)
        amplitude = np.random.normal(self.amplitude_mean, self.amplitude_sigma)
        phase = np.random.normal(self.phase_mean, self.phase_sigma)

        return angle, frequency, amplitude, phase