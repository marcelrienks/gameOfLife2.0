import time
from helpers.printHelper import PrintHelper
from helpers.gridHelper import GridHelper

class GameHandler():

    def __init__(self, horizontal, vertical, liveCells):
        self.horizontal = horizontal
        self.vertical = vertical
        self.liveCells = liveCells
    
    # TODO: rewrite run
    # Run conways game of life
    def run(self):
        iteration = 0
        while True:
            # Skip the seed grid, else calculate next lifecycle
            if iteration > 0:
                self.liveCells = self.calculateNextLifeCycle(self.liveCells)
                if nextLiveCellCycle != None:
                    # Print the new grid
                    iteration += 1
                    PrintHelper.printGridLifeCycle(self.horizontal, self.vertical, self.liveCells, iteration)
                    time.sleep(0.3)

                else:
                    break

        print('Complete!')
    
    # TODO: Complete this method
    # Calculate the next life cycle grid
    def calculateNextLifeCycle(self, liveCells):
        #calculate row

        #calculate column

        #TempTesting Code
        liveCells = liveCells.append(2)
        return liveCells