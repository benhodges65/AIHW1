def forward_checking(sudoku):
    blocks = []
    i = 0
    while i < len(sudoku):
        j = 0
        while j < len(sudoku[i]):
            if int(sudoku[i][j]) == 0:
                blocks.append(Empty_Block(i,j))
            j = j+1
        i = i+1


class Empty_Block:
  def __init__(self, x, y):
    self.x = x
    self.y = y