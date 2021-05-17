"""
Python module for exception handling
"""
import os
import sys

from py_snake_and_ladder.handlers.logger import Logger

sys.path.append(os.path.realpath('..'))

class BaseGameException(Exception):
    """
    Base exception class for handling exceptions in the game
    """
    def __init__(self):
        Exception.__init__(self)
        self.logger = Logger().get()

class MissingPlayerNameException(BaseGameException):
    """
    Exception thrown when player name is not defined
    """
    def __init__(self):
        BaseGameException.__init__(self)
        self.logger.error('Player name is a mandatory property and it cannot be left empty.')

class UnsupportedDiceTypeException(BaseGameException):
    """
    Exception thrown dice-type is unsupported
    """
    def __init__(self, dice_type):
        BaseGameException.__init__(self)
        self.logger.error(f'{dice_type} is an un-supported dice type')

class InvalidGameAssetException(BaseGameException):
    """
    Exception thrown when any of the game asset is invalid
    """
    def __init__(self, message):
        BaseGameException.__init__(self)
        self.logger.error(f'Invalid game asset. {message if message else ""}')
