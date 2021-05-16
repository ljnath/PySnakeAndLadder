from logger import Logger

class BaseException(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.logger = Logger().get()
        
class MissingPlayerNameException(BaseException):
    def __init__(self):
        BaseException.__init__(self)
        self.logger.exception('Player name is a mandatory property and it cannot be left empty.')
        
class UnsupportedDiceTypeException(BaseException):
    def __init__(self, type):
        BaseException.__init__(self)
        self.logger.exception(f'{type} is an un-supported dice type')
        
class InvalidGameAssetException(BaseException):
    def __init__(self, message):
        BaseException.__init__(self)
        self.logger.exception(f'Invalid game asset. {message if message else ""}')