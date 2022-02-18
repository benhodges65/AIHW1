from Sudoku_solver import *
i = 0
initial_S = ""
while i < 9:
    initial_S = initial_S + input("Enter Row " + str(i))
    i = i+1
Sudoku_solver(initial_S)