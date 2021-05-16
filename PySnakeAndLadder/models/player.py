from ..handlers.exceptions import MissingPlayerNameError

class Player:
    def __init__(self):
        self.__name = None
    
    @property
    def name(self):
        if not self.__name:
            raise MissingPlayerNameError()
        
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        