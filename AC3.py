from queue import Queue
def arc_consistency(sudoku):
    solution = sudoku
    blocks = []
    i = 0
    q = []
    while i < len(sudoku):
        j = 0
        while j < len(sudoku[i]):
            if int(sudoku[i][j]) == 0:
                blocks.append(Empty_Block(i,j,get_possible_values(i, j, sudoku)))
            j = j+1
        i = i+1
    print("BREAK")
    q = createQueue(blocks)
    while q:
        arc = q.pop(0)
        change = removeValues(arc, blocks, q)
        if change > -1:
            blocks[arc.block1].possible[change] = False
            neighbors = getNeighbors(arc, blocks)
            while neighbors:
                q.append(neighbors.pop(0))
    for l in blocks:
        LEft = False
        numleft = 0 
        found = False
        for index, j in enumerate(l.possible):
            if j == True:
                found = True
                solution[l.x][l.y] = index + 1
                numleft = numleft + 1
        if numleft != 1:
            LEft = True
            solution[l.x][l.y] = 0
    if LEft == True:
        return arc_consistency(solution)
    else:
        return solution


class arc:
    def __init__(self, block1, block2):
        self.block1 = block1
        self.block2 = block2

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

def createQueue(blocks):
    tempQueue = []
    for num1, i in enumerate(blocks):
        for num2, j in enumerate(blocks):
            if num1 != num2:
                if j.x == i.x:
                    tempQueue.append(arc(num1,num2))
                if j.y == i.y:
                    tempQueue.append(arc(num1,num2))
                if int(j.x/3) == int(i.x/3) and int(j.y/3) == int(i.y/3):
                    tempQueue.append(arc(num1,num2))
    return tempQueue

def removeValues(arc, blocks, q):
    numTrue = 0
    numTrue2 = 0
    index = -1
    change = -1
    arcExists = False
    for arcs in q:
        if arcs.block1 == arc.block1 and arcs.block2 != arc.block2:
            arcExists = True
        elif arcs.block2 == arc.block1 and arcs.block1 != arc.block2:
            arcExists = True
    for num, i in enumerate(blocks[arc.block1].possible):
        if i == True:
            numTrue2 = numTrue2 + 1
    for num, i in enumerate(blocks[arc.block2].possible):
        if i == True:
            numTrue = numTrue + 1
    if numTrue == 1:
        for num, i in enumerate(blocks[arc.block2].possible):
            if i == True and blocks[arc.block1].possible[num] == True:
                index = num
    if index == -1 and numTrue2 == 2 and arcExists == False and numTrue == 2:
        for num, i in enumerate(blocks[arc.block2].possible):
            if i == False and blocks[arc.block1].possible[num] == True:
                index = num
        
    if index != -1:
        change = index
    else:
        change = -1
    return change
            
def getNeighbors(arc1, blocks):
    tempQueue = []
    for num, i in enumerate(blocks):
        if num != arc1.block2 and num != arc1.block1:
            if blocks[arc1.block1].x == blocks[num].x:
                tempQueue.append(arc(num, arc1.block1))
            if blocks[arc1.block1].y == blocks[num].y:
                tempQueue.append(arc(num, arc1.block1))
            if int(blocks[arc1.block1].x/3) == int(blocks[num].x/3) and int(blocks[arc1.block1].y/3) == int(blocks[num].y/3):
                tempQueue.append(arc(num, arc1.block1))
    return tempQueue