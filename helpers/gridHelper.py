import random
import math

class GridHelper:
    
    # Create empty grid
    @staticmethod
    def generateEmptyGrid(horizontal, vertical):
        grid = []
        for _ in range(vertical):
            grid.append([0] * horizontal)
        
        return grid

    # Create a seeded grid
    @staticmethod
    def generateSeedGrid(horizontal, vertical, seed):
        grid = GridHelper.generateEmptyGrid(horizontal, vertical)

        # seed the grid
        for _ in range(seed):
            while True:
                row = random.randint(0, vertical - 1)
                column = random.randint(0, horizontal - 1)
                if grid[row][column] == 0:
                    grid[row][column] = 1
                    break

        return grid