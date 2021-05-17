import os
import sys

from PySnakeAndLadder.handlers.exceptions import MissingPlayerNameException
from PySnakeAndLadder.models.dice import Dice
from PySnakeAndLadder.models.dice_type import DiceType

sys.path.append(os.path.realpath('..'))

class Player:
    """
    Player model class
    Holds basic player information like name, current position and dice-type
    """
    def __init__(self, name, dice_type = DiceType.NORMAL):
        self.__name = name
        self.__position = 0
        self.__dice = Dice(dice_type)
    
    @property
    def name(self) -> str:
        """
        Property for getting player name
        """
        if not self.__name:
            raise MissingPlayerNameException()
        return self.__name
    
    @property
    def position(self) -> int:
        """
        Property for getting current player position
        """
        return self.__position
    
    @position.setter
    def position(self, value:int) -> None:
        """
        Property for setting position for the player
        """
        self.__position = value
        
    @property
    def dice(self) -> Dice:
        """
        Property for getting the player's instance of dice used in the gameplay
        """
        return self.__dice
    
    @dice.setter
    def dice(self, value:Dice) -> None:
        """
        Property for setting the player's instance of dice used in the gameplay
        """
        self.__dice = value
