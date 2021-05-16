import os
import sys

from handlers.exceptions import MissingPlayerNameError

from models.dice import Dice
from models.dice_type import DiceType

sys.path.append(os.path.realpath('..'))

class Player:
    def __init__(self):
        self.__name = None
        self.__score = 0
        self.__dice = Dice(DiceType.NORMAL)
    
    @property
    def name(self) -> str:
        if not self.__name:
            raise MissingPlayerNameError()
        return self.__name
    
    @name.setter
    def name(self, value:str):
        self.__name = value
        
    @property
    def score(self) -> int:
        return self.__score
    
    @score.setter
    def score(self, value:int):
        self.__score = value
        
    @property
    def dice(self) -> Dice:
        return self.__dice
    
    @dice.setter
    def dice(self, value:Dice):
        self.__dice = value
