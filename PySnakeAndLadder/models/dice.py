import os
import random
import sys

from PySnakeAndLadder.handlers.exceptions import UnsupportedDiceTypeException
from PySnakeAndLadder.models.dice_type import DiceType

sys.path.append(os.path.realpath('..'))

class Dice:
    """
    Dice model class
    Holds dice information and method for using the dice in the gameplay
    """
    def __init__(self, type: DiceType):
        self.__dice_type = type
        self.__value = 0
        
        # faces of dice in normal mode
        self.__normal_faces = (1, 2, 3, 4, 5, 6)
        
        # faces of dice in crooked mode; in crooked mode only even numbers are considerd
        self.__crooked_faces = tuple([i for i in self.__normal_faces if i % 2 == 0 ])
        
    @property
    def type(self):
        """
        Property for getting the type of dice
        """
        return self.__dice_type.value
        
    @property
    def value(self) -> int:
        """
        Property for getting the value of the dice
        """
        return self.__value
    
    @value.setter
    def value(self, value: int) -> None:
        """
        Property for setting the value of the dice
        """
        self.__value = value
    
    def roll(self) -> None:
        """
        Roll method used for roling the dice.
        The new dice value is stored as value of the dice
        """
        if self.type == DiceType.NORMAL.value:
            self.value = random.choice(self.__normal_faces)
        elif self.type == DiceType.CROOKED.value:
            self.value = random.choice(self.__crooked_faces)
        else:
            raise UnsupportedDiceTypeException(self.type)
