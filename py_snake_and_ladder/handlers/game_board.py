"""
Python module for handing game board
"""
import os
import sys

from py_snake_and_ladder.handlers.console import Console
from py_snake_and_ladder.handlers.logger import Logger
from py_snake_and_ladder.models.game_assets import GameAssets
from py_snake_and_ladder.models.player import Player

sys.path.append(os.path.realpath('..'))

class GameBoard:
    """
    GameBoard class for hanlding interaction with the gameboard
    """
    def __init__(self, player: Player):
        self.__player = player              # player name
        self.__has_ended = False            # game has not ended yet
        self.__notification_msg = None        # game has not started so there is not game notification

        self.__logger = Logger().get()
        self.__logger.info(f'Created game board for player {self.__player.name}; selected dice type is {self.__player.dice.dice_type}')

        self.__game_assets = GameAssets()
        self.__game_assets.validate()

    @property
    def has_ended(self) -> bool:
        """
        Property for geting the game end status
        """
        return self.__has_ended

    @has_ended.setter
    def has_ended(self, value:bool) -> None:
        """
        Property for setting the game end status
        """
        self.__has_ended = value

    @property
    def notification_msg(self) -> str:
        """
        Property for getting notification message for the player
        """
        return self.__notification_msg

    @notification_msg.setter
    def notification_msg(self, value:str) -> None:
        """
        Property for setting a notification message for the player
        """
        self.__notification_msg = value

    def roll_dice(self):
        """
        Method to wait for user to roll the dice
        """
        Console.get_roll_confirmation()
        self.__player.dice.roll()
        self.__logger.debug(f'Player has rolled the dice from position {self.__player.position}; dice value is {self.__player.dice.value}')

    def draw(self) -> None:
        """
        Method for drawing the game board for the gameplay
        """
        Console.clear()
        print(f'\n{"SNAKE & LADDER 0.1".center(131)}')          # welcome game title

        board_numbers = list(range(1, 101))                     # all possible board numbers 1 to 100

        # updating snake head & tail in the board_numbers,
        # SX_HEAD is the head of the snake while SX_TAIL is its end
        for index, snake in enumerate(self.__game_assets.snakes):
            board_numbers[snake.head - 1] = f'S{index+1}_HEAD'
            board_numbers[snake.tail - 1] = f'S{index+1}_TAIL'

        # updating ladder start & end in the board_numbers,
        # LX_START is the start of the ladder while LX_END is the end of it
        for index, ladder in enumerate(self.__game_assets.ladders):
            board_numbers[ladder.start - 1] = f'L{index+1}_START'
            board_numbers[ladder.end - 1] = f'L{index+1}_END'

        # updating board_numbers with player position if player has moved
        # board_number is updated to player name in upper case enclosed with '*' character
        if self.__player.position > 0:
            board_numbers[self.__player.position - 1] = f'* {self.__player.name[:8].upper()} *'

        # draw the game board with the board_numbers
        self.__draw_board(board_numbers)
        # draw the game legends
        self.__draw_legend()

        # show notification message is anything is set
        if self.notification_msg:
            print(f'\nINFO: {self.notification_msg}\n')

    def __draw_board(self, board_data : list) -> None:
        """
        Private method for drawing the game board
        """
        board_data.reverse()
        cell_length = 12
        seperator_length = cell_length * 10 + 11                            # cell_length * item_count + seperator_count
        print('-' * seperator_length, end='')

        for i in range(10):                                                 # total number of rows 100 / 10 = 10
            row_start_pos = i * 10
            items = board_data[row_start_pos : row_start_pos + 10]          # 10 element in each row
            if i % 2 != 0:
                items.reverse()                                             # flipping row items incase of odd rows

            print('')
            _ = [print(f'|{str(item).center(cell_length)}', end = '') for item in items]
            print(f'|\n{"-"*seperator_length}', end='')

    def __draw_legend(self) -> None:
        """
        Private method for drawing the game legends
        """
        print('\n\n  GAME LEGEND:')
        for index, snake in enumerate(self.__game_assets.snakes):
            print(f'\t* Snake {index+1} : {snake.head} - {snake.tail}', end = '\t')
        print()
        for index, ladder in enumerate(self.__game_assets.ladders):
            print(f'\t* Ladder {index+1} : {ladder.start} - {ladder.end}', end = '\t')
        print('\n\t* LX_START : start of ladder\n\t* LX_END : end of ladder\n\t* SX_HEAD : start or head of snake\n\t* SX_TAIL : end or tail of snake')
        print('\n')
