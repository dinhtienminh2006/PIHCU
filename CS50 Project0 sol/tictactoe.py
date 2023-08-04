"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == X:
                countX +=1
            elif board[row][col] == O:
                countO +=1
        return X if countX == countO else 0


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            # If the cell is empty, add the action (i, j)
            if board[row][col] == EMPTY:
                possible_actions.add(row, col)

            return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid action")
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] == player(board)
    return board_copy

def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
        return False

def checkCol(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
        return False

def checkFirstDig(board, player):
    for col in range(len(board[row])):
        for row in range(len(board)):
            if row == col and board[row] == player:
                count += 1
        if count == 3:
            return True
        else:
            return False

def checkSecondDig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False
            


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkCol(board, X) or checkFirstDig(board, X) or checkSecondDig(board,X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or checkFirstDig(board, O) or checkSecondDig(board,O):
        return O
    else:
        return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(all(cell is not EMPTY for cell in row) for row in board)
        

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0  


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reserve = True)[0][1]
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key =lambda x: x[0])[0][1]
 

def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v

