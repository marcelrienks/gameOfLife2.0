# Game of Life
Conways game of life, ...

## Version 2.0:
The theory behind this version is that it is not necesary to store multiple grids (or two dimensional arrays) in memory tocompare and calculate a cells life or death. But rather to simply know the dimensions of the grid (x,y), and a one dimentional array with one-based index of live cells.

### Square Grid:
0 0 0 0  
0 0 1 0  
0 0 0 0  
1 0 0 0  

grid: 4x4  
list: [7,13] (_**one-based array index**_)

Using the above values, the formula for calculating the live cells x,y coordinate is:
live cell / number of columns = decimal  
where the whole number portion represents the x coordinate (_**zero-based row index**_).

The fractional remainder can then be used in the following formula
(number of columns * remainder) - 1 = whole number
where the resultant whole number represents the y coordinate (_**zero-based column index**_).

e.g.  
7/4 = 1.75 => x = 1  
(4*0.75)-1 = 2 => y = 2

13/7 = 3.25 => x = 3  
(4*0.25)-1 = 0 => y = 0

### Non-Square Grid:
This formula also applies to non square grids

0 1 0 0 0  
0 0 0 1 0  
0 0 0 0 0  

grid: 5x3  
list: [2,9] (one-based list index)

2/5 = 0.4 => x = 0  
(5*0.4)-1 = 1 => y = 1

9/5 = 1.8 => x = 1  
(5*0.8)-1 = 3 => y = 3
