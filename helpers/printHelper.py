from os import system, name
from helpers.utilHelper import UtilHelper

class PrintHelper:

    # Clear the console screen
    @staticmethod
    def clearScreen():
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    
    # Convert the dataset to a grid, and print it on the console
    @staticmethod
    def printGrid(horizontal, vertical, liveCells):
        PrintHelper.clearScreen()
        count = 0
        for row in vertical:
            printRow = ''
            for element in horizontal:
                count += 1
                printRow += '□ ' if (UtilHelper.safeIndex(liveCells, count)) == -1) else '■ '
                printRow.strip()
            print(printRow)
    
    # Print the next lifecycle grid
    @staticmethod
    def printGridLifeCycle(horizontal, vertical, liveCells, iteration):
        PrintHelper.printGrid(horizontal, vertical, liveCells)
        print('\nLifecycle', iteration)