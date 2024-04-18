import copy


def print_board(board):
    for i in range(len(savedboards)):
        for a in range(8):
            print((savedboards[i][a]))
        print(" ")


def validate_queen_position(board, row, col): 
    # validate columns
    queen_counter = 0
    for i in range(8):
        if board[i][col] == 'R':
            queen_counter += 1

    if queen_counter > 1:
        return False

    # validate diagonal
    # for i in range(1, 8):
    #     if row + i < 8 and col + i < 8:
    #         if board[row + i][col + i] == 'R':
    #             return False

    for i in range(1, 8):
        if row - i >= 0 and col - i >= 0:
            if board[row - i][col - i] == 'R':
                return False

    # validate diagonal-invertida
    for i in range(1, 8):
        if row - i >= 0 and col + i < 8:
            if board[row - i][col + i] == 'R':
                return False

    return True


def eight_queens_solver_rec(board, row, savedboards, col):
    if row == 8 and col == 8:
        return True
    if row == 8:
        if board not in savedboards:
            savedboards.append(copy.deepcopy(board))
            return False
        else:
            return Tlrue

    for col in range(8):
        board[row][col] = 'R'
        if validate_queen_position(board, row, col):
            if eight_queens_solver_rec(board, row + 1, savedboards, col):
                return True
            else:
                board[row][col] = '-'
        else:
            board[row][col] = '-'
    else:
        return False


def eight_queens_solver():
    board = [['-' for j in range(8)] for i in range(8)]
    eight_queens_solver_rec(board, 0, savedboards, 0)
    return savedboards


# user code
savedboards = []
savedboards = eight_queens_solver()
print_board(savedboards)
