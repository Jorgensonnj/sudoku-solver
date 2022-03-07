#!/usr/bin/env python3
import sys

from lib import *

board = sudoku_board(sys.argv)
sudoku_print(board)

print(validate_x(board, 0))
print(validate_y(board, 0))

#solved = sudoku_solve(board)
#
#print(solved)
