
def forward_checking(sudoku):
    blocks = []
    i = 0
    while i < len(sudoku):
        j = 0
        while j < len(sudoku[i]):
            if int(sudoku[i][j]) == 0:
                blocks.append(Empty_Block(i,j,get_possible_values(i, j, sudoku)))
            j = j+1
        i = i+1
    if not blocks:
        return sudoku
    else: 
        target = blocks[0]
        for val, i in enumerate(target.possible):
            val = val + 1
            if(i == True):
                if check(val, target.x, target.y, blocks):
                    sudoku[target.x][target.y] = val
                    tempSud = forward_checking(sudoku)
                    if tempSud:
                        return tempSud
                    else:
                        sudoku[target.x][target.y] = 0
        return []

    


class Empty_Block:
  def __init__(self, x, y, possible):
    self.x = x
    self.y = y
    self.possible = possible

def get_possible_values(x, y, sudoku):
    bool_vals = [True for i in range(9)]
    i = 0
    small_x = int(x/3)
    small_y = int(y/3)
    while i < 9:
        if int(sudoku[x][i]) > 0:
            bool_vals[int(sudoku[x][i]) - 1] = False
        if int(sudoku[i][y]) > 0:
            bool_vals[int(sudoku[i][y]) - 1] = False
        i = i+1
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if int(sudoku[small_x*3 + i][small_y*3+j]) > 0:
                bool_vals[int(sudoku[small_x*3 + i][small_y*3+j])-1] = False
            j = j + 1
        i = i + 1
    return bool_vals

def check(val, x, y, blocks):
    numTrue = 0
    index = 0
    for i in blocks:
        for num, j in enumerate(i.possible):
            if j == True:
                numTrue = numTrue + 1
                index = num
        if numTrue == 1:
            if val == index:
                if x == i.x:
                    return False
                if y == i.y:
                    return False
                if x/3 == i.x/3 and y/3 == i.y/3:
                    return False
    return True