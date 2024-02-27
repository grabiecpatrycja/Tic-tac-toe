import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    if board == initial_state:
        return X
    
    sum_x = 0
    sum_o = 0
    for row in board:
        sum_x += row.count('X')
        sum_o += row.count('O')

    return X if sum_x == sum_o else O

def actions(board):

    actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))
    return actions

def result(board, action):

    i, j = action
    copy_board = copy.deepcopy(board)
    copy_board[i][j] = player(board)

    return copy_board


def winner(board):

    #horizontally
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY: return row[0]

    #vertically
    for i in range(3):
        col = [row[i] for row in board]
        if len(set(col)) == 1 and col[0] != EMPTY: return col[0]

    # diagonally
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY: return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY: return board[0][2]

    else: return None


def terminal(board):

    terminal = False
    if winner(board): terminal = True

    if all(cell != EMPTY for row in board for cell in row): terminal = True

    return terminal

def utility(board):

    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    else: return 0


def minimax(board):

    if terminal(board):
        return utility(board), None
    if player(board) == X:
        max_v = -math.inf
        best_move = None
        for action in actions(board):
            v, _ = minimax(result(board, action))
            if v > max_v:
                max_v = v
                best_move = action
        return max_v, best_move
    else:
        min_v = math.inf
        best_move = None
        for action in actions(board):
            v, _ = minimax(result(board, action))
            if v < min_v:
                min_v = v
                best_move = action
        return min_v, best_move