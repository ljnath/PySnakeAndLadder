"""
Python pytest module for testing models
"""
from enum import Enum
import pytest
from py_snake_and_ladder.handlers.exceptions import (
    InvalidGameAssetException, MissingPlayerNameException, UnsupportedDiceTypeException)
from py_snake_and_ladder.models.dice_type import DiceType
from py_snake_and_ladder.models.dice import Dice
from py_snake_and_ladder.models.game_assets import GameAssets
from py_snake_and_ladder.models.player import Player


def test_player_model_instance_creations():
    """
    test instance creation with default value in Player model
    :return:
    """
    player = Player('foobar')
    
    assert player.name == 'foobar'
    assert player.position == 0
    assert player.dice.dice_type == DiceType.NORMAL.value

def test_player_without_name():
    """
    test exception handling in Player model
    :return:
    """
    player = Player(None)
    with pytest.raises(MissingPlayerNameException):
        player.name()
        
def test_player_property():
    """
    test property in Player model
    """
    player = Player('foo', dice_type = DiceType.CROOKED)
    player.position = 50
    
    assert player.name == 'foo'
    assert player.position == 50
    assert player.dice.dice_type == DiceType.CROOKED.value
    
    
def test_game_assets_singleton():
    """
    test singleton instance creation of the GameAssets model
    """
    game_assets_1 = GameAssets()
    game_assets_2 = GameAssets()
    
    assert game_assets_1 == game_assets_2
    
def test_game_assets_property():
    """
    test property of GameAssets model
    """
    game_assets = GameAssets()
    
    assert game_assets.snakes is not None
    assert game_assets.ladders is not None
    
# def test_game_assets_validation(mocker):
#     """
#     test validation in GameAssets model
#     """
#     mocker.patch("GameAssets().snakes", return_value={0:(0,0)})
    
    # with pytest.raises(InvalidGameAssetException):
    #     GameAssets()
    
def test_dice_type():
    """
    test DiceType instance
    """
    dice_type = DiceType.to_list()
    
    assert type(dice_type) == list
    assert len(dice_type) == len(DiceType)

def test_dice_instance():
    """
    test Dice instance
    """
    dice = Dice(DiceType.CROOKED)
    
    assert type(dice) == Dice
    assert dice.dice_type == 'crooked'
    
    
def test_dice_roll():
    """
    test Dice roll functionality
    """
    normal_dice = Dice(DiceType.NORMAL)
    crooked_dice = Dice(DiceType.CROOKED)
    
    max_roll_count = 100
    for _ in range(max_roll_count):
        normal_dice.roll()
        assert normal_dice.value > 0 and normal_dice.value < 7
        
    for _ in range(max_roll_count):
        crooked_dice.roll()
        assert crooked_dice.value in (2, 4, 6)
        
def test_dice_roll_exception(mocker):
    """
    test exception handling while rolling dice of unsupported type
    """
    class DiceTypePatched(Enum):
        NORMAL = 'foo'
        CROOKED = 'bar'

    dice = Dice(DiceTypePatched.NORMAL)
    with pytest.raises(UnsupportedDiceTypeException):
        dice.roll()
        