"""
Primary game play script in the package
"""
import os
import sys

from PySnakeAndLadder.handlers.game_board import GameBoard
from PySnakeAndLadder.handlers.console import Console
from PySnakeAndLadder.handlers.logger import Logger
from PySnakeAndLadder.models.game_assets import GameAssets
from PySnakeAndLadder.models.player import Player

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
        while(not self.__game_board.has_ended):
            self.__game_board.draw()
            self.__game_board.player_notification = None
            
            self.__game_board.roll_dice()
            
            # game notification based on game or player actions
            self.__game_board.player_notification = f'New dice value is {self.__player.dice.current_value}.\n'
            
            if self.__player.position + self.__player.dice.current_value > 100:
                self.__game_board.player_notification += f'Dice value cannot be used as it exceeds board limit.'
                continue
            
            self.__player.position += self.__player.dice.current_value  # updating player position
            self.__check_for_hit()                                      # checking if player has either hit a snake or ladder
            
            if self.__player.position == 100:                           # ending game when player reaches the end position
                self.__game_board.has_ended = True

        # notifying player of game status and ending game
        if self.__game_board.has_ended:
            self.__game_board.player_notification += f'Congratulations {self.__player.name}! You have won the game.'
            self.__game_board.draw()
    
    def __check_for_hit(self):
        """
        Method to check if player has hit either a snake or ladder and update players position accordingly
        """
        # checking if player has hit the foot of the ladder, if yes then player position to updated to the top of ladder
        for key, value in self.__game_assets.ladders.items():
            if value[0] == self.__player.position:
                self.__player.position = value[1]
                self.__logger.info(f'{self.__player.name} has climbed ladder {key+1} from {value[0]} to {value[1]}')
                self.__game_board.player_notification += f'Great, you have climbed ladder {key+1} from position {value[0]} to {value[1]}'
                break
        
        # checking if player has hit the head of snake, if yes then player position to updated to the tail of the snake
        for key, value in self.__game_assets.snakes.items():
            if value[0] == self.__player.position:
                self.__player.position = value[1]
                self.__logger.info(f'{self.__player.name} has been bitten by snake {key+1} in position {value[1]} ; your new position is {value[0]}')
                self.__game_board.player_notification += f'Oops!, you have been bitten by snake {key+1} in position {value[1]}, your new position is {value[0]}'
                break
        