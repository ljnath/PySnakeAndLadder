import os
import sys

from PySnakeAndLadder.models.dice_type import DiceType

sys.path.append(os.path.realpath('..'))

class Console:
    """
    Class for handling console interactions
    """
    
    @staticmethod
    def clear() -> None:
        """
        Static method to clear the console based on OS
        """
        os.system('clear' if os.name != 'nt' else 'cls')
    
    @staticmethod
    def get_player_name() -> str:
        """
        Static method to get the player name from the console
        """
        player_name = None
        while not player_name:
            player_name = input('* Please enter your name: ')
            if len(player_name.strip()) == 0:
                player_name = None
        return player_name
        
    @staticmethod
    def get_dice_type() -> DiceType:
        """
        Static method to create the menu of all the available dice types and get the user selected dice type
        """
        user_choice = 0
        dice_type_as_list = DiceType.to_list()                      # converting the enum to list
        valid_choice = tuple(range(1, len(dice_type_as_list) + 1))  # valid choices will be the serial number of the enum
        
        message = '* Please choose dice-type:'
        for index, type in enumerate(dice_type_as_list):
            message += f'\n\t{index+1} - {type}'
        message += f'\nYour choice {valid_choice}: '
            
        while user_choice not in valid_choice:
            try:
                user_choice = int(input(message))
            except ValueError:
                user_choice = 0
                
        return list(DiceType)[user_choice - 1]
            
    @staticmethod
    def get_roll_confirmation():
        """
        Static method to allow user to hit [ENTER] key
        """
        input('Press [ENTER] to roll the dice ...')
    