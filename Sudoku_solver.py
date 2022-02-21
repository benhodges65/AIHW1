import re
from forward_checking import *
from Utility import *
def Sudoku_solver(grid):
  squares = re.findall(r'\d', grid)
  sudoku = nest_list(squares, 9, 9)
  solution = forward_checking(sudoku)
  solutionFormatted = ""
  i = 0
  while i < len(solution):
    j = 0
    solutionFormatted = solutionFormatted + "["
    while j < len(solution[i])-1:
      solutionFormatted = solutionFormatted + str(solution[i][j]) + ", "
      j = j + 1
    if i == len(solution) - 1:
      solutionFormatted = solutionFormatted + str(solution[i][j]) + "]"
    else:
      solutionFormatted = solutionFormatted + str(solution[i][j]) + "],\n"
    i = i + 1
  return solutionFormatted
