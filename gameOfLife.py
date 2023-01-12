import sys
from helpers.printHelper import PrintHelper
from helpers.gridHelper import GridHelper
from helpers.mathHelper import MathHelper
from handlers.gameHandler import GameHandler

# Main method
def main():
    columns, rows, liveCells = preload()

    # Run
    gameHandler = GameHandler(columns, rows, liveCells)
    gameHandler.run()

# Collect input, and preload seed grid    
def preload():
    PrintHelper.clearScreen()

    # Collect intput and validate
    gridInput = input("Please enter the columns, and rows size, followed by the seed of the grid in the following format: 0x0:0\nThe size is the number of cells columnsly and rowsly, and the seed is the number of randomly placed live cells to start with.\n(e.g. 40x40:200).\n")
    columns, rows, seed = validateGridInput(gridInput)    

    # Print grid and get confirmation to run
    liveCells = GridHelper.generateLiveCells(columns, rows, seed)
    PrintHelper.printGrid(columns, rows, liveCells)
    shouldRun = input("\nWould you like to run this seed?\ny or n\n")
    
    if shouldRun == 'y':
        return columns, rows, liveCells
    
    else:
        return preload()

# Validate input variables
def validateGridInput(gridInput):
    # Validate that there is a split character
    if "x" not in gridInput or ":" not in gridInput:
        raise Exception ('Invalid input, format must be 0x0:0 (e.g. 40x40:200)')

    size = gridInput.split(':')[0]
    columns = size.split('x')[0]
    rows = size.split('x')[1]
    seed = gridInput.split(':')[1]

    # validate that both inputs are integers
    if not MathHelper.isInt(columns) or not MathHelper.isInt(rows) or not MathHelper.isInt(seed):
        raise Exception ('Invalid input type, both size and seed must be integers (e.g. 40x40:200)')

    columns = int(columns)
    rows = int(rows)
    seed = int(seed)

    # validate that seed is not larger than the squared size
    if seed > (columns * rows):
        raise Exception ('Invalid input seed, must be smaller than the square of the size (e.g. 40x40:200)')

    return columns, rows, seed

if __name__ == '__main__':
    try:
        main()

    except Exception as ex:
        print('Exception:', ex)