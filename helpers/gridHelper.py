import random
import math

class GridHelper:
    # create an array of live cells within a range
    @staticmethod
    def generateLiveCells(columns, rows, seed):
        return random.sample(range(columns * rows), seed)

    # find all the neighbouring cells for a given live cell
    @staticmethod
    def findNeighbours(columns, liveCell):
        neighbours = []
        
        neighbours.append(liveCell - columns - 1)
        neighbours.append(liveCell - columns)
        neighbours.append(liveCell - columns + 1)

        neighbours.append(liveCell - 1)
        neighbours.append(liveCell + 1)

        neighbours.append(liveCell + columns - 1)
        neighbours.append(liveCell + columns)
        neighbours.append(liveCell + columns + 1)

        return neighbours