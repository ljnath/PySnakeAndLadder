import random

from handlers.exceptions import UnsupportedDiceType
from dice_type import DiceType
    
class Dice:
    def __init__(self, type: DiceType):
        self._dice_type = type
        
        self._normal_values = (1, 2, 3, 4, 5, 6)
        self._crooked_values = tuple([i for i in self._normal_values if i % 2 == 0 ])
    
    def roll(self) -> int:
        if self._dice_type == DiceType.NORMAL:
            return random.choice(self._normal_values)
        elif self._dice_type == DiceType.CROOKED:
            return random.choice(self._crooked_values)
        else:
            raise UnsupportedDiceType(self._dice_type)