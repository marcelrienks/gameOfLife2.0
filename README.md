# Game of Life v2.0
Simple console app to test Conway's game of life, but rather than using multiple 2 dimentional arrays to keep track of, and calculate the next life cycle of live and dead cells, version 2 calculates all live and dead cells on the fly.

## Theroy of version 2.0:
The theory behind this version is rather to simply know the dimensions of the grid (x,y), and a one dimentional array with one-based index of live cells.

### Square Grid:
0 0 0 0  
0 0 1 0  
0 0 0 0  
1 0 0 0  

grid: 4x4  
array: [7,13] of a _**one-based array index**_ list of live cells

Using the above values, the formula for calculating the live cells x,y coordinate is:
live cell / number of columns in grid = decimal  
where the whole number portion represents the y coordinate of a _**zero-based row index**_ column.

The fractional remainder can then be used in the following formula
(number of columns * remainder) - 1 = whole number
where the resultant whole number represents the x coordinate of a _**zero-based column index**_ row.

e.g.  
7/4 = 1.75 => y = 1  
(4*0.75)-1 = 2 => x = 2

13/4 = 3.25 => y = 3  
(4*0.25)-1 = 0 => x = 0

### Non-Square Grid:
This formula also applies to non square grids

0 1 0 0 0  
0 0 0 1 0  
0 0 0 0 0  

grid: 5x3  
array: [2,9] of a _**one-based array index**_ list of live cells

2/5 = 0.4 => y = 0  
(5*0.4)-1 = 1 => x = 1

9/5 = 1.8 => y = 1  
(5*0.8)-1 = 3 => x = 3
