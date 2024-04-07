from CellType import CellType


class NC(CellType):
    """Circle Cell"""

    @staticmethod
    def sample_location(sample_phantom, phantom_sample):
        """Given a SamplePhantom instance and a PhantomSample instance,
        find a good location for a next cell to be placed."""
        return 0, 0

    def __init__(self):
        super().__init__("NC")
