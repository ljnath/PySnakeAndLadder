import os
import sys

from handlers.exceptions import InvalidGameAssetException

from models.player import Player
from models.game_assets import GameAssets
from hanlders.console import ConsoleHandler
from logger import Logger

sys.path.append(os.path.realpath('..'))

class GameBoard:
    def __init__(self, player: Player):
        self.__game_assets = GameAssets()
        self.__player = player
        self.__logger = Logger().get()
        
        self.__logger.info(f'Created game board for player {self.__player.name}; selected dice type is {self.__player.dice.type}')
        self.__validate_game_assets()
    
    def __validate_game_assets(self):
        self.__logger.info('Validating game asset data')
        
        # validating snake data
        for _, value in self.__game_assets.snakes.items():
            if value[1] < value[0]:
                raise InvalidGameAssetException('Snake should always be from top to bottom')
            elif value[1] == 100:
                raise InvalidGameAssetException('Snakes head at at game end point is not pratical enough !')
            elif value[1] - value[0] < 20:
                raise InvalidGameAssetException('Horizontal or too small snakes are not practical enough !')
            elif any(value) > 100 or any(value) <  1:
                raise InvalidGameAssetException('Snake head or tail is outside the board range (1-100)')
            
        # validating ladder data
        for _, value in self.__game_assets.ladder.items():
            if value[1] < value[0]:
                raise InvalidGameAssetException('Snake should always be from top to bottom')
            elif 100 in value or 1 in value:
                raise InvalidGameAssetException('Ladders cannot start or end at position 0 and 100')
            elif value[1] - value[0] < 20:
                raise InvalidGameAssetException('Horizontal or too small ladder are not practical enough !')
            elif any(value) > 100 or any(value) <  1:
                raise InvalidGameAssetException('Ladder head or tail is outside the board range (1-100)')
        
            
    def draw(self):
        ConsoleHandler.clear()
        print(f'\nSNAKE & LADDER 0.1\n\nGame board\n\n')
        
        positions = list(range(1, 101))
        
        for key, value in self.__game_assets.snakes.items():
            positions[value[1] - 1] = f'S{key+1}_HEAD'
            positions[value[0] - 1] = f'S{key+1}_TAIL'
        
        for key, value in self.__game_assets.ladder.items():
            positions[value[1] - 1] = f'L{key+1}_START'
            positions[value[0] - 1] = f'L{key+1}_END'
       
        positions[self.__player.current_value] = 'PLAYER'
        self.__draw_board(positions.reverse())
        
        
    def __draw_board(self, board_data):
        cell_length = 20
        seperator_length = 211                                              # cell_length * item_count + seperator_count
        print('-' * seperator_length, end='')
        
        for i in range(10):                                                 # total number of rows 100 / 10 = 10
            row_start_position = i * 10
            items = board_data[row_start_position, row_start_position + 10] # 10 element in each row
            if (i % 2 != 0):
                items.reverse()                                             # flipping row items incase of odd rows
            
            print('')
            [print(f'|{str(item).center(cell_length)}', end = '') for item in items]
            print(f'|\n{"-"*seperator_length}', end='')
