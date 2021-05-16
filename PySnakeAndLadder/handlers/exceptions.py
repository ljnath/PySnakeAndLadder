from logger import Logger

class game_assets(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.logger = Logger().get(name = 'snake&ladder')
        
        
class MissingPlayerNameException(game_assets):
    def __init__(self):
        game_assets.__init__(self)
        self.logger.exception('Player name is a mandatory property and it cannot be left empty.')
        
class UnsupportedDiceTypeException(game_assets):
    def __init__(self, type):
        game_assets.__init__(self)
        self.logger.exception(f'{type} is an un-supported dice type')