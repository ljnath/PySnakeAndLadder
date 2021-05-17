from enum import Enum

class DiceType(Enum):
    """
    Enum holding supported DiceType
    """
    NORMAL = 'normal'
    CROOKED = 'crooked'
    
    @staticmethod
    def to_list():
        """
        Static method to get the current Enum as a list
        """
        # creating a list of values of the Enum DiceType
        return list(map(lambda dt: dt.value, DiceType))