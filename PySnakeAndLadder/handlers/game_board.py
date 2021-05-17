import os
import sys

from PySnakeAndLadder.handlers.exceptions import InvalidGameAssetException
from PySnakeAndLadder.handlers.logger import Logger
from PySnakeAndLadder.handlers.console import Console
from PySnakeAndLadder.models.game_assets import GameAssets
from PySnakeAndLadder.models.player import Player

sys.path.append(os.path.realpath('..'))

class GameBoard:
    def __init__(self, player: Player):
        self.__player = player
        self.__has_ended = False
        self.__player_notification = None
        self.__game_assets = GameAssets()
        self.__logger = Logger().get()
        
        self.__logger.info(f'Created game board for player {self.__player.name}; selected dice type is {self.__player.dice.type}')
        self.__validate_game_assets()
    
    @property
    def has_ended(self):
        return self.__has_ended
    
    @has_ended.setter
    def has_ended(self, value:bool):
        self.__has_ended = value
        
    @property
    def player_notification(self):
        return self.__player_notification
    
    @player_notification.setter
    def player_notification(self, value:str):
        self.__player_notification = value
    
    def __validate_game_assets(self):
        self.__logger.info('Validating game asset data')
        
        # validating snake data
        for key, value in self.__game_assets.snakes.items():
            self.__logger.debug(f'Validating snake asset - key = {key} ; value = {value}')
            if value[0] < value[1]:
                raise InvalidGameAssetException('Snake should always be from top to bottom')
            elif value[1] == 100:
                raise InvalidGameAssetException('Snakes head at at game end point is not pratical enough !')
            # elif value[0] - value[1] < 20:
            #     raise InvalidGameAssetException('Horizontal or too small snakes are not practical enough !')
            elif any(value) > 100 or any(value) <  1:
                raise InvalidGameAssetException('Snake head or tail is outside the board range (1-100)')
            
        # validating ladder data
        for key, value in self.__game_assets.ladders.items():
            self.__logger.debug(f'Validating ladder asset - key = {key} ; value = {value}')
            if value[0] > value[1]:
                raise InvalidGameAssetException('Ladders are suppose to to be climbed up and not down')
            elif 100 in value or 1 in value:
                raise InvalidGameAssetException('Ladders cannot start or end at position 0 and 100')
            elif value[1] - value[0] < 20:
                raise InvalidGameAssetException('Horizontal or too small ladder are not practical enough !')
            elif any(value) > 100 or any(value) <  1:
                raise InvalidGameAssetException('Ladder head or tail is outside the board range (1-100)')
        
    def draw(self):
        Console.clear()
        print(f'\n{"SNAKE & LADDER 0.1".center(131)}')
        
        positions = list(range(1, 101))
        
        for key, value in self.__game_assets.snakes.items():
            positions[value[0] - 1] = f'S{key+1}_HEAD'
            positions[value[1] - 1] = f'S{key+1}_TAIL'
        
        for key, value in self.__game_assets.ladders.items():
            positions[value[0] - 1] = f'L{key+1}_START'
            positions[value[1] - 1] = f'L{key+1}_END'
            
        if self.__player.position > 0:
            positions[self.__player.position - 1] = f'* {self.__player.name[:10].upper()} *'
            
        self.__draw_board(positions)
        self.__draw_legend()
        
        if self.player_notification:
            print(f'\nINFO: {self.player_notification}\n')
        
    def __draw_board(self, board_data):
        board_data.reverse()
        cell_length = 12
        seperator_length = cell_length * 10 + 11                            # cell_length * item_count + seperator_count
        print('-' * seperator_length, end='')
        
        for i in range(10):                                                 # total number of rows 100 / 10 = 10
            row_start_pos = i * 10
            items = board_data[row_start_pos : row_start_pos + 10]          # 10 element in each row
            if (i % 2 != 0):
                items.reverse()                                             # flipping row items incase of odd rows
            
            print('')
            [print(f'|{str(item).center(cell_length)}', end = '') for item in items]
            print(f'|\n{"-"*seperator_length}', end='')
        
    def __draw_legend(self):
        print('\n\n  GAME LEGEND:')
        for key, value in self.__game_assets.snakes.items():
            print(f'\t* Snake {key+1} : {value[0]}-{value[1]}', end = '\t')
        print()
        for key, value in self.__game_assets.ladders.items():
            print(f'\t* Ladder {key+1} : {value[0]}-{value[1]}', end = '\t')
        print('\n\t* LX_START : start of ladder\n\t* LX_END : end of ladder\n\t* SX_HEAD : start or head of snake\n\t* SX_TAIL : end or tail of snake')
        print('\n')
            
    def roll_dice(self):
        Console.get_roll_confirmation()
        self.__player.dice.roll()
        self.__logger.debug(f'Roll complete, dice value is {self.__player.dice.current_value}')
        print(f'Dice value is {self.__player.dice.current_value}')
        