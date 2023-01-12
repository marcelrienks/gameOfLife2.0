import time
from helpers.printHelper import PrintHelper
from helpers.gridHelper import GridHelper
from helpers.utilHelper import UtilHelper

class GameHandler():

    def __init__(self, columns, rows, liveCells):
        self.columns = columns
        self.rows = rows
        self.liveCells = liveCells
    
    # Run conways game of life
    def run(self):
        iteration = 0
        while True:
            self.liveCells = self.calculateNextLifeCycle(self.columns, self.rows, self.liveCells)
            if self.liveCells != None:
                # Print the new grid
                iteration += 1
                PrintHelper.printGridLifeCycle(self.columns, self.rows, self.liveCells, iteration)
                time.sleep(0.3)

            else:
                break

        print('Complete!')
    
    # Calculate the next life cycle grid
    def calculateNextLifeCycle(columns, rows, liveCells):
        nextLiveCells = []
        cells = columns * rows

        for cell in cells:
            neighbours = GridHelper.findNeighbours(columns, cells)
            for neighbour in neighbours:
                liveNeighbours = 0
                liveNeighbours += 1 if UtilHelper.safeIndex(liveCells, neighbour) != -1 else 0

            # calculate the current cells next cycle life
            if UtilHelper.safeIndex(liveCells, cell) != -1:
                # Any live cell with two or three live neighbours lives on to the next generation.
                if liveNeighbours > 1 and liveNeighbours < 4:
                    nextLiveCells.append()

            else:
                # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                if liveNeighbours == 3:
                    nextLiveCells.append()

        return nextLiveCells if nextLiveCells != liveCells else None