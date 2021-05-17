"""
Python module for game assets model
"""
import os
import sys

from py_snake_and_ladder.common.singleton import Singleton
from py_snake_and_ladder.handlers.exceptions import InvalidGameAssetException
from py_snake_and_ladder.handlers.logger import Logger

sys.path.append(os.path.realpath('..'))

class Snake():
    """
    Snake model
    """
    def __init__(self, head, tail):
        self._head = head
        self._tail = tail

    @property    
    def head(self):
        return self._head
    
    @property
    def tail(self):
        return self._tail

class Ladder():
    """
    Ladder model
    """
    def __init__(self, start, end):
        self._start = start
        self._end = end

    @property    
    def start(self):
        return self._start
    
    @property
    def end(self):
        return self._end
        
class GameAssets(metaclass=Singleton):
    """
    Game assets model class.
    Holds property of game assets used in the game
    """
    def __init__(self):
        self.__logger = Logger().get()

        # creating snakes assets as dict type where key is the snake count,
        # and the value is a tuple showing the start and end of the snake
        self._snakes = (
            Snake(14, 7),
            Snake(50, 3),
            Snake(93, 32)
        )

        # creating ladder assets as dict type where key is the ladder count,
        # and the value is a tuple showing the start and end of the ladder
        self._ladder = (
            Ladder(5, 30),
            Ladder(23, 66),
            Ladder(72, 95)
        )

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

    def validate(self):
        self.__logger.info('Validating "snake" game asset')
        for snake in self.snakes:
            self.__logger.debug(f'Validating snake game-asset: head={snake.head} ; tail={snake.tail}')
            if snake.head < snake.tail:
                raise InvalidGameAssetException('Snake should always be from top to bottom')
            if snake.head == 100:
                raise InvalidGameAssetException('Snakes head at at game end point is not pratical enough !')
            
            snake_positions = (snake.head, snake.tail)
            if any(snake_positions) > 100 and any(snake_positions) <  1:
                raise InvalidGameAssetException('Snake head or tail is outside the board range (1-100)')
            
        self.__logger.info('Validating "ladders" game asset')
        for ladder in self.ladders:
            self.__logger.debug(f'Validating ladder game-asset: start={ladder.start} ; end={ladder.end}')
            if ladder.start > ladder.end:
                raise InvalidGameAssetException('Ladders are suppose to to be climbed up and not down')
            if ladder.end - ladder.start < 20:
                raise InvalidGameAssetException('Horizontal or too small ladder are not practical enough !')
            
            ladder_position = (ladder.start, ladder.end)
            if 100 in ladder_position or 1 in ladder_position:
                raise InvalidGameAssetException('Ladders cannot start or end at position 0 and 100')
            if any(ladder_position) > 100 and any(ladder_position) <  1:
                raise InvalidGameAssetException('Ladder head or tail is outside the board range (1-100)')
