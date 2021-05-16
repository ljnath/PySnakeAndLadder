from enum import Enum

class DiceType(Enum):
    NORMAL = 'normal'
    CROOKED = 'crooked'
    
    @staticmethod
    def to_list(self):
        return list(map(lambda dt: dt.value,  DiceType))