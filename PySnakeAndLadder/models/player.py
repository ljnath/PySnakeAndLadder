from ..handlers.exceptions import MissingPlayerNameError

class Player:
    def __init__(self):
        self.__name = None
        self.__score = 0 
    
    @property
    def name(self) -> str:
        if not self.__name:
            raise MissingPlayerNameError()
        return self.__name
    
    @name.setter
    def name(self, value:str):
        self.__name = value
        
        
    @property
    def score(self) -> int:
        return self.__score
    
    @score.setter
    def score(self, value:int):
        self.__score = value
        