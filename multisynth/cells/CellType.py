from abc import ABC, abstractmethod

class CellType(ABC):
    """Class that defines the cell type object"""

    @staticmethod
    @abstractmethod
    def sample_location(sample_phantom, phantom_sample):
        ''' Given a SamplePhantom instance and a PhantomSample instance, 
        find a good location for a next cell to be placed.'''

    def __init__(self, name):
        self.name = name
        self.x = -1
        self.y = -1

    def __str__(self):
        return 'Cell of type '+self.name+' at '+str(self.x)+','+str(self.y)

