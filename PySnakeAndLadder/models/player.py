import os
import sys

from PySnakeAndLadder.handlers.exceptions import MissingPlayerNameException
from PySnakeAndLadder.models.dice import Dice
from PySnakeAndLadder.models.dice_type import DiceType

sys.path.append(os.path.realpath('..'))

class Player:
    def __init__(self, name, dice_type = DiceType.NORMAL):
        self.__name = None
        self.__position = 0
        self.__dice = Dice(dice_type)
    
    @property
    def name(self) -> str:
        if not self.__name:
            raise MissingPlayerNameException()
        return self.__name
    
    @name.setter
    def name(self, value:str):
        self.__name = value
        
    @property
    def position(self) -> int:
        return self.__position
    
    @position.setter
    def position(self, value:int):
        self.__position = value
        
    @property
    def dice(self) -> Dice:
        return self.__dice
    
    @dice.setter
    def dice(self, value:Dice):
        self.__dice = value
