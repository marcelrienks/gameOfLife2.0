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
    def printGrid(columns, rows, liveCells):
        PrintHelper.clearScreen()
        count = 0
        for row in range(rows):
            printRow = ''
            for element in range(columns):
                count += 1
                printRow += '□ ' if UtilHelper.safeIndex(liveCells, count) == -1 else '■ '
                printRow.strip()
            print(printRow)
    
    # Print the next lifecycle grid
    @staticmethod
    def printGridLifeCycle(columns, rows, liveCells, iteration):
        PrintHelper.printGrid(columns, rows, liveCells)
        print('\nLifecycle', iteration)