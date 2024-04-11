import numpy as np


class Expressions:
    """Defines the Expression statistics and how samples are generated from it."""

    _EXPRESSION_DIMS = 100

    def __init__(self, expression_means, expression_sigmas):
        assert (
            len(expression_means) == self._EXPRESSION_DIMS
        ), "Expression means must be of length 100"
        assert (
            len(expression_sigmas) == self._EXPRESSION_DIMS
        ), "Expression sigmas must be of length 100"

        self.expression_means = expression_means
        self.expression_sigmas = expression_sigmas

    def sample(self):
        """Sample from the defined Expressions distribution."""
        return np.random.normal(self.expression_means, self.expression_sigmas)
