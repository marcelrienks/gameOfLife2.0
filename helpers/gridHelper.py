import random
import math

class GridHelper:
    # create an array of live cells within a range
    @staticmethod
    def generateLiveCells(horizontal, vertical, seed):
        return random.sample(range(horizontal * vertical), seed)