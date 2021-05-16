import random

from handlers.exceptions import UnsupportedDiceType
from dice_type import DiceType
    
class Dice:
    def __init__(self, type: DiceType):
        self.__dice_type = type
        self.__current_value = 0
        
        self.__normal_faces = (1, 2, 3, 4, 5, 6)
        self.__crooked_faces = tuple([i for i in self.__normal_faces if i % 2 == 0 ])
        
    @property
    def type(self):
        return self.__dice_type.value
        
    @property
    def current_value(self) -> int:
        return self.__current_value
    
    @current_value.setter
    def current_value(self, value:int ):
        self.__current_value = value
    
    def roll(self) -> int:
        if self.type == DiceType.NORMAL.value:
            return random.choice(self.__normal_faces)
        elif self.type == DiceType.CROOKED.value:
            return random.choice(self.__crooked_faces)
        else:
            raise UnsupportedDiceType(self.type)