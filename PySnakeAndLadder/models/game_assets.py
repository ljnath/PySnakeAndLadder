import sys
import os

from common.singleton import Singleton

sys.path.append(os.path.realpath('..'))

class GameAssets(metaclass=Singleton):
    
    def __init__(self):
        self._snakes = {
            0 : (14, 7),
            1 : (50, 3),
            2 : (93, 32)
        }
        
        self._ladder = {
            0 : (5, 10),
            1 : (23, 66),
            2 : (72, 95)
        }
    
    @property
    def snakes(self) -> dict:
        return self._snakes
    
    @property
    def ladders(self) -> dict:
        return self.get_ladder
    