import os
import sys

from models.player import Player
from models.game_assets import GameAssets
from hanlders.console import ConsoleHandler

sys.path.append(os.path.realpath('..'))

class GameBoard:
    def __init__(self, player: Player):
        self.__game_assets = GameAssets()
        self.__player = player
    