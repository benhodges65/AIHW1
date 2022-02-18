import re
def Sudoku_solver(grid):
  squares = re.findall(r'\d', grid)
  print(len(squares))
  for i in squares:
      print(i)