from CellType import CellType


class LWC(CellType):
    """Random Little Cell"""

    @staticmethod
    def sample_location(sample_phantom, phantom_sample):
        """Given a SamplePhantom instance and a PhantomSample instance,
        find a good location for a next cell to be placed."""
        return 0, 0

    def __init__(self):
        super().__init__("LWC")
