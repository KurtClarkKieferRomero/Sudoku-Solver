#create an existing board
#get existing board from sudoku.com
sudoku_board= [
    [0, 0, 0, 0, 0, 8, 0, 6, 0],
    [9, 4, 0, 0, 7, 0, 1, 0, 0],
    [6, 0, 0, 0, 0, 0, 7, 8, 0],
    [8, 0, 3, 0, 5, 1, 0, 4, 9],
    [0, 0, 0, 0, 9, 0, 0, 2, 1],
    [1, 6, 9, 4, 0, 0, 3, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 3, 7],
    [4, 9, 2, 0, 0, 0, 0, 0, 0]
]
# 0 meant blank space
# Visual representation for the sudoku board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range (len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# Function for finding empty cells or blocks
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # i = row, j = col

