sudoku_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find
    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i
            if solve(board):
                return True
            board[row][column] = 0
    return False


def valid(board, number, position):
    # unique in the row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    # unique in the column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    # unique in the 3x3 section
    section_x = position[1] // 3
    section_y = position[0] // 3
    for i in range(section_y * 3, section_y * 3 + 3):
         for j in range(section_x * 3, section_x * 3 + 3):
             if board[i][j] == number and (i, j) != position:
                 return False
    return True


# function to print the list representing sudoku entries in a nice visual way
def print_board(board):
    for i in range(len(board)):
        # print visual divisor after 3rd and 6th row
        if i % 3 == 0 and i != 0:
            print("- - -    - - -    - - -")

        for j in range(len(board[0])):
            # print visual divisor after three entries
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # print entry and a space
            if j != 8:
                print(str(board[i][j]) + " ", end="")
            # regarding the last entry, just print it and go to the new line
            else:
                print(board[i][j])


# function to find first next empty position
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


# putting it all together
print_board(sudoku_board)
solve(sudoku_board)
print("=======================")
print_board(sudoku_board)
