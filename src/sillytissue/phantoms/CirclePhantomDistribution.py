import numpy as np


class CirclePhantomDistribution:
    """The CirclePhantomDistribution class represents a distribution of worlds of circles we cann draw CirclePhantoms from."""

    def __init__(
        self, num_circles_min, num_cirlces_mean, num_circles_sigma, radius_mean, radius_sigma
    ) -> None:
        self.num_circles_min = num_circles_min
        self.num_circles_mean = num_cirlces_mean
        self.num_circles_sigma = num_circles_sigma
        self.radius_mean = radius_mean
        self.radius_sigma = radius_sigma
        self.sample_parameters()

    def sample_parameters(self) -> int:
        """Sample the parameters of the CirclePhantomDistribution."""
        self.num_circles = int(
            np.round(np.random.normal(self.num_circles_mean, self.num_circles_sigma))
        )
        if self.num_circles <= self.num_circles_min:
            self.num_circles = self.num_circles_min
        return self.num_circles

