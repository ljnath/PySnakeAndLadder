"""
Primary game play script in the package
"""
import os
import sys

from py_snake_and_ladder.handlers.game_board import GameBoard
from py_snake_and_ladder.handlers.console import Console
from py_snake_and_ladder.handlers.logger import Logger
from py_snake_and_ladder.models.game_assets import GameAssets
from py_snake_and_ladder.models.player import Player

sys.path.append(os.path.realpath('.'))


class PySnakeAndLadder:
    """
    Main game play class
    """
    def __init__(self):
        """
        Default constructor
        """
        self.__logger = Logger().get()
        self.__logger.info('Starting Snake And Ladder 0.1')
        self.__game_assets = GameAssets()

        self.__player = None
        self.__game_board = None

    def play(self):
        """
        Game play method, handles the game flow
        """
        Console.clear()
        print('Welcome to SNAKE & LADDER 0.1\nLets begin by gathering a few details about you ...\n\n')
        player_name = Console.get_player_name()         # getting player name from console
        dice_type = Console.get_dice_type()             # getting the dice type choice from console

        self.__player = Player(player_name, dice_type)  # creating instance of player with given name and dice-type
        self.__game_board = GameBoard(self.__player)    # creating instace of game-board with player name

        # main game loop
        while not self.__game_board.has_ended:
            self.__game_board.draw()
            self.__game_board.notification_msg = None

            self.__game_board.roll_dice()

            # game notification based on game or player actions
            self.__game_board.notification_msg = f'New dice value is {self.__player.dice.value}.\n'

            if self.__player.position + self.__player.dice.value > 100:
                self.__game_board.notification_msg += 'Dice value is too large !'
                continue

            self.__player.position += self.__player.dice.value          # updating player position
            self.__check_for_hit()                                      # checking if player has either hit a snake or ladder

            if self.__player.position == 100:                           # ending game when player reaches the end position
                self.__game_board.has_ended = True

        # notifying player of game status and ending game
        if self.__game_board.has_ended:
            self.__game_board.notification_msg += f'Congratulations {self.__player.name}! You have won the game.'
            self.__game_board.draw()

    def __check_for_hit(self):
        """
        Method to check if player has hit either a snake or ladder and update players position accordingly
        """
        # checking if player has hit the foot of the ladder, if yes then player position to updated to the top of ladder
        for index, ladder in enumerate(self.__game_assets.ladders):
            if ladder.start == self.__player.position:
                self.__player.position = ladder.end
                self.__logger.info(f'{self.__player.name} has climbed ladder {index+1} from {ladder.start} to {ladder.end}')
                self.__game_board.notification_msg += f'Great, you just hit a ladder and climbed from {ladder.start} to {ladder.end}'
                break

        # checking if player has hit the head of snake, if yes then player position to updated to the tail of the snake
        for index, snake in enumerate(self.__game_assets.snakes):
            if snake.head == self.__player.position:
                self.__player.position = snake.tail
                self.__logger.info(f'{self.__player.name} has been swallowed by a snake at {snake.head} ; your new position is {snake.tail}')
                self.__game_board.notification_msg += f'Oops!, you have been bitten by snake at {snake.head}, your new position is {snake.tail}'
                break
        