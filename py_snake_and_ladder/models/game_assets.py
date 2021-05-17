"""
Python module for game assets model
"""
import os
import sys

from py_snake_and_ladder.common.singleton import Singleton
from py_snake_and_ladder.handlers.exceptions import InvalidGameAssetException
from py_snake_and_ladder.handlers.logger import Logger

sys.path.append(os.path.realpath('..'))

class GameAssets(metaclass=Singleton):
    """
    Game assets model class.
    Holds property of game assets used in the game
    """
    def __init__(self):
        self.__logger = Logger().get()

        # creating snakes assets as dict type where key is the snake count,
        # and the value is a tuple showing the start and end of the snake
        self._snakes = {
            0 : (14, 7),
            1 : (50, 3),
            2 : (93, 32)
        }

        # creating ladder assets as dict type where key is the ladder count,
        # and the value is a tuple showing the start and end of the ladder
        self._ladder = {
            0 : (5, 30),
            1 : (23, 66),
            2 : (72, 95)
        }

        self.__validate_snakes()
        self.__validate_ladders()

    def __validate_snakes(self):
        """
        Private method for validating snakes
        """
        self.__logger.info('Validating "snake" game asset')
        for key, value in self.snakes.items():
            self.__logger.debug(f'Validating snake asset - key = {key} ; value = {value}')
            if value[0] < value[1]:
                raise InvalidGameAssetException('Snake should always be from top to bottom')
            if value[1] == 100:
                raise InvalidGameAssetException('Snakes head at at game end point is not pratical enough !')
            # if value[0] - value[1] < 20:
            #     raise InvalidGameAssetException('Horizontal or too small snakes are not practical enough !')
            if any(value) > 100 or any(value) <  1:
                raise InvalidGameAssetException('Snake head or tail is outside the board range (1-100)')

    def __validate_ladders(self):
        """
        Private method for validating ladders
        """
        self.__logger.info('Validating "ladders" game asset')
        for key, value in self.ladders.items():
            self.__logger.debug(f'Validating ladder asset - key = {key} ; value = {value}')
            if value[0] > value[1]:
                raise InvalidGameAssetException('Ladders are suppose to to be climbed up and not down')
            if 100 in value or 1 in value:
                raise InvalidGameAssetException('Ladders cannot start or end at position 0 and 100')
            if value[1] - value[0] < 20:
                raise InvalidGameAssetException('Horizontal or too small ladder are not practical enough !')
            if any(value) > 100 or any(value) <  1:
                raise InvalidGameAssetException('Ladder head or tail is outside the board range (1-100)')

    @property
    def snakes(self) -> dict:
        """
        Property for setting the snake game asset
        """
        return self._snakes

    @property
    def ladders(self) -> dict:
        """
        Property for setting the ladder game asset
        """
        return self._ladder
