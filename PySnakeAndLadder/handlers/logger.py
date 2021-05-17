import logging
import os
import sys

from PySnakeAndLadder.common.singleton import Singleton

sys.path.append(os.path.realpath('..'))

class Logger(metaclass=Singleton):

    def __init__(self):
        self.__filename = 'game.log'
        
    def get(self, name = 'snake&ladder'):
        """
        method to get an instance of the logger class with a given name
        :param name: name of logger
        :return: logger - instance of logging
        """
        logger = logging.getLogger(name)
        log_formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        logger.setLevel(logging.DEBUG)

        if not logger.hasHandlers():
            file_log_handler = logging.FileHandler(filename=self.__filename)
            file_log_handler.setFormatter(log_formatter)
            logger.addHandler(file_log_handler)
            
        return logger
