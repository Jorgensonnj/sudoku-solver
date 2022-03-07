
def get_file_path(args):
    if len(args) == 1:
        print("Invalid use. Example: main path/to/sudoku/file\n")
        quit()
    else:
        return args[1]

def read_file(path):
    file = open(path, "r")
    lines = file.readlines()
    file.close()

    return lines

def sudoku_board(args):

    path = get_file_path(args)
    board = read_file(path)

    for x in range(len(board)):
        board[x] = board[x].replace(" ","")
        board[x] = board[x].replace("\n","")
        string = board[x]
        num_array = []

        for char in string:
            num_array.append(char)

        board[x] = num_array

    return board


def validate_x(board, row):
    duplicate = {}
    for index_x in range(len(board[row])):
        if board[row][index_x] != "0":
            if duplicate.get(board[row][index_x]) == 1:
                return False
            else:
                duplicate[board[row][index_x]] = 1
        else:
            return False

    for length in range(1, len(board[row])):
        if duplicate.get(length):
            return False

    return True

def validate_y(board, column):
    duplicate = {}
    for index_y in range(len(board)):
        if board[index_y][column] != "0":
            if duplicate.get(board[index_y][column]) == 1:
                return False
            else:
                duplicate[board[index_y][column]] = 1
        else:
            return False

    for length in range(1, len(board)):
        if duplicate.get(length):
            return False

    return True


def sudoku_solve(board):
    return board


def sudoku_print(board):

    for index_y in range(len(board)):
        row_string = ""
        if index_y == 3 or index_y == 6:
            print("---+---+---")
        for index_x in range(len(board[index_y])):
            if index_x == 3 or index_x == 6:
                row_string = row_string + "|"
            row_string = row_string + board[index_y][index_x]

        print(row_string)

