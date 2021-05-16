class Assets:
    
    def __init__(self):
        self._snakes = {
            0 : (14, 7),
            1 : (50, 3),
            2 : (93, 32)
        }
        
        self._ladder = {
            0 : (5, 10),
            1 : (23, 66),
            2 : (72, 95)
        }
    
    def get_snakes(self):
        return self._snakes
    
    def get_ladder(self):
        return self.get_ladder
    