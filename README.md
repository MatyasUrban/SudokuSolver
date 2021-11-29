# Sudoku Solver
This program takes a variable sudoku_board, applies the **backtracking algorithm** to solve the sudoku, and prints the resulting board.
## Prerequisites
You need to have **Python 3** installed on your device to run the script.
## How to use it
Change the numbers in the variable **sudoku_board** so they correspond to the sudoku you are trying to solve and run the program. The solution will be printed.
## How it works
The program solves the sudoku from the first position in the top row to the last position in the bottom row in a backtracking fashion. When it stumbles upon an empty place, it tries to fill it with a number from 1 to 9 that satisfies the rules of the puzzle.

1.  Unique number in the row
2.  Unique number in the column
3.  Unique number in the 3 by 3 area

When no such number exists, the algorithm backtracks, meaning go to the previous position and tries a different number. If it backtracks up to the initial position with no success, the sudoku is deemed inconsistent - with no possible solution.
