def forward_checking(sudoku):
    blocks = []
    i = 0
    while i < len(sudoku):
        j = 0
        while j < len(sudoku[i]):
            if int(sudoku[i][j]) == 0:
                blocks.append(Empty_Block(i,j))
                bool_vals = get_possible_values(i, j, sudoku)
                for i in bool_vals:
                    print(i)
            j = j+1
        i = i+1


class Empty_Block:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def get_possible_values(x, y, sudoku):
    bool_vals = [True for i in range(9)]
    i = 0
    small_x = x/3
    small_y = y/3
    while i < 9:
        if int(sudoku[x][i]) > 0:
            bool_vals[int(sudoku[x][i]) - 1] = False
        if int(sudoku[i][y]) > 0:
            bool_vals[int(sudoku[y][x]) - 1] = False
        i = i+1
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if int(sudoku[small_x*3 + i][small_y*3+j]) > 0:
                bool_vals[sudoku[small_x*3 + i][small_y*3+j]-1] = False
            j = j + 1
        i = i + 1
    return bool_vals
