import time
from helpers.printHelper import PrintHelper
from helpers.gridHelper import GridHelper

class GameHandler():

    def __init__(self, horizontal, vertical, liveCells):
        self.horizontal = horizontal
        self.vertical = vertical
        self.liveCells = liveCells
    
    # Run conways game of life
    def run(self):
        iteration = 0
        while True:
            self.liveCells = self.calculateNextLifeCycle(self.liveCells)
            if self.liveCells != None:
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