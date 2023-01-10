import time
from helpers.printHelper import PrintHelper
from helpers.gridHelper import GridHelper

class GameHandler():

    def __init__(self, grid):
        self.grid = grid
    
    # TODO: rewrite run
    # Run conways game of life
    def run(self):
        iteration = 0
        while True:
            # Skip the seed grid, else calculate next lifecycle
            if iteration > 0:
                newGrid = self.calculateNextLifeCycle(self.grid)
                if newGrid != None:
                    self.grid = newGrid

                else:
                    break

            # Print the new grid
            iteration += 1
            PrintHelper.printGridLifeCycle(self.grid, iteration)
            time.sleep(0.3)

        print('Complete!')
    
    # TODO: Complete this method
    # Calculate the next life cycle grid
    def calculateNextLifeCycle(self, currentGrid):
        #calculate row

        #calculate column