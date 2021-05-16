import os
import sys

from models.dice_type import DiceType

sys.path.append(os.path.realpath('..'))

class ConsoleHandler:
    def __init__(self):
        pass
    
    @staticmethod
    def clear():
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')
    
    @staticmethod
    def get_player_name(self):
        player_name = None
        while not player_name:
            player_name = input('> Please enter your name: ')
            if len(player_name.strip()) == 0:
                player_name = None
        return player_name
        
    @staticmethod
    def get_dice_type(self):
        dice_type_as_list = DiceType.to_list()
        
        user_choice = 0
        valid_choice = range(1, len(dice_type_as_list) + 1)
        
        message = 'Please choose dice-type - '
        for index, type in enumerate(dice_type_as_list):
            message += f'{index+1}. {type} ;'
        message += f'. Your choice ({valid_choice}): '
            
        while user_choice not in valid_choice:
            user_choice = input(message)
            
        return user_choice
            