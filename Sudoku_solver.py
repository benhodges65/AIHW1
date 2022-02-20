import re
from forward_checking import *
from Utility import *
def Sudoku_solver(grid):
  squares = re.findall(r'\d', grid)
  sudoku = nest_list(squares, 9, 9)
  forward_checking(sudoku)
