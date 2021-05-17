
import pytest
import logging
from py_snake_and_ladder.handlers.exceptions import (
    InvalidGameAssetException, MissingPlayerNameException,
    UnsupportedDiceTypeException)

from py_snake_and_ladder.handlers.console import Console
from py_snake_and_ladder.handlers.logger import Logger
from py_snake_and_ladder.handlers.game_board import GameBoard
from py_snake_and_ladder.models.player import Player


def test_logger_singleton():
    """
    test if logger class is singleton
    """
    logger_1 = Logger()
    logger_2 = Logger()
    
    assert logger_1 == logger_2

def test_logger_multiple_handlers():
    """
    test if logger class returns the same file handler for same name
    """
    logger_1 = Logger().get('foo')
    logger_2 = Logger().get('bar')
    logger_3 = Logger().get('foo')
    
    assert logger_1 != logger_2
    assert logger_1 == logger_3
    
def test_game_board_instance():
    """
    test to check instance of game board
    """
    game_board = GameBoard(Player('foobar'))
    
    assert type(game_board) == GameBoard
    assert game_board.has_ended == False
    
def test_game_board_roll(mocker):
    """
    test to check if the roll has actually happened via game_board
    """
    def get_roll_confirmation_mocked():
        return
        
    player = Player('foobar')
    game_board = GameBoard(player)
    old_dice_value = player.dice.value
    
    mocker.patch('py_snake_and_ladder.handlers.console.Console.get_roll_confirmation', get_roll_confirmation_mocked)
    game_board.roll_dice()
    new_dice_value = player.dice.value
        
    assert old_dice_value != new_dice_value
    
def test_console_instance(mocker):
    """
    test to check console class
    """    
    mocker.patch('input()', return_value="foo")
    assert Console.get_player_name() == 'foo'