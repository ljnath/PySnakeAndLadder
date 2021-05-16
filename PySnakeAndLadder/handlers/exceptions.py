from .logger import Logger

class BaseError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.logger = Logger().get(name = 'snake&ladder')
        
        
class MissingPlayerNameError(BaseError):
    def __init__(self):
        BaseError.__init__(self)
        self.logger.exception('Player name is a mandatory property and it cannot be left empty.')