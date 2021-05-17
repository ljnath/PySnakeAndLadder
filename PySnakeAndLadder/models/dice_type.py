from enum import Enum

class DiceType(Enum):
    NORMAL = 'normal'
    CROOKED = 'crooked'
    
    @staticmethod
    def to_list():
        return list(map(lambda dt: dt.value,  DiceType))