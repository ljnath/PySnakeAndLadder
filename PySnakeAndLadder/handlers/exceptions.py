import os
import sys

from PySnakeAndLadder.handlers.logger import Logger

sys.path.append(os.path.realpath('..'))

class BaseException(Exception):
    """
    Base exception class for handling exceptions in the game
    """
    def __init__(self):
        Exception.__init__(self)
        self.logger = Logger().get()
        
class MissingPlayerNameException(BaseException):
    """
    Exception thrown when player name is not defined
    """
    def __init__(self):
        BaseException.__init__(self)
        self.logger.error('Player name is a mandatory property and it cannot be left empty.')
        
class UnsupportedDiceTypeException(BaseException):
    """
    Exception thrown dice-type is unsupported
    """
    def __init__(self, type):
        BaseException.__init__(self)
        self.logger.error(f'{type} is an un-supported dice type')
        
class InvalidGameAssetException(BaseException):
    """
    Exception thrown when any of the game asset is invalid
    """
    def __init__(self, message):
        BaseException.__init__(self)
        self.logger.error(f'Invalid game asset. {message if message else ""}')
