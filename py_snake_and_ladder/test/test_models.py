"""
Python pytest module for testing models
"""
from enum import Enum
import pytest
from py_snake_and_ladder.handlers.exceptions import (
    InvalidGameAssetException, MissingPlayerNameException, UnsupportedDiceTypeException)
from py_snake_and_ladder.models.dice_type import DiceType
from py_snake_and_ladder.models.dice import Dice
from py_snake_and_ladder.models.game_assets import GameAssets, Snake, Ladder
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
    
def test_game_assets_snake_validation(mocker):
    """
    test to check snake validations
    """
    class GameAssetsMocked:
        def opposite_snake(self):
            return [Snake(10, 20)]
        
        def snake_at_100(self):
            return [Snake(100, 50)]
        
        def snake_with_same_head_and_tail(self):
            return [Snake(80, 80)]
        
        def snake_head_outside_board(self):
            return [Snake(102, 50)]

        def snake_tail_outside_board(self):
            return [Snake(60, 0)]
    
    game_assets = GameAssets()
    method_to_patch = "py_snake_and_ladder.models.game_assets.GameAssets.snakes"
    
    mocker.patch(method_to_patch, GameAssetsMocked().opposite_snake())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()
        
    mocker.patch(method_to_patch, GameAssetsMocked().snake_at_100())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()
    
    mocker.patch(method_to_patch, GameAssetsMocked().snake_with_same_head_and_tail())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()
    
    mocker.patch(method_to_patch, GameAssetsMocked().snake_head_outside_board())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()
        
    mocker.patch(method_to_patch, GameAssetsMocked().snake_tail_outside_board())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()

def test_game_assets_ladder_validation(mocker):
    """
    test to check ladder validations
    """
    class GameAssetsMocked:
        def opposite_ladder(self):
            return [Ladder(20, 10)]
        
        def ladder_at_0(self):
            return [Ladder(0, 50)]
        
        def ladder_at_100(self):
            return [Ladder(50, 100)]
        
        def ladder_starts_outside_board(self):
            return [Ladder(0, 100)]

        def ladder_ends_outside_board(self):
            return [Ladder(5, 101)]
        
        def ladder_is_too_small(self):
            return [Ladder(20, 25)]
    
    game_assets = GameAssets()
    method_to_patch = "py_snake_and_ladder.models.game_assets.GameAssets.ladders"
    
    mocker.patch(method_to_patch, GameAssetsMocked().opposite_ladder())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()
        
    mocker.patch(method_to_patch, GameAssetsMocked().ladder_at_0())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()
    
    mocker.patch(method_to_patch, GameAssetsMocked().ladder_at_100())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()
    
    mocker.patch(method_to_patch, GameAssetsMocked().ladder_starts_outside_board())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()
        
    mocker.patch(method_to_patch, GameAssetsMocked().ladder_ends_outside_board())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()
    
    mocker.patch(method_to_patch, GameAssetsMocked().ladder_is_too_small())
    with pytest.raises(InvalidGameAssetException):
        game_assets.validate()
        
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
        