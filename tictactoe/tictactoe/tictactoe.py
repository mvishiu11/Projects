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
    if sum([i.count(X) for i in board]) > sum([i.count(O) for i in board]):
      return O
    else:
      return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    i = 0 
    j = 0
    for row in board:
      for column in row:
        if board[i][j] == EMPTY:
          actions.append((i, j))
        j += 1
      j = 0  
      i += 1
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if action is None:
      return board
    if action[0] > 2 or action[-1] > 2 or action[0] < 0 or action[-1] < 0:
      raise Exception("Invalid action")
    if player(board) == X:
      new_board[action[0]][action[-1]] = X
    else:
      new_board[action[0]][action[-1]] = O
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == board[1][1] == board[2][2]):
      return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]):
      return board[0][2]
    for i in range(3):
      if (board[i][0] == board[i][1] == board[i][2]):
        return board[i][0]
      elif (board[0][i] == board[1][i] == board[2][i]):
        return board[0][i]
    return EMPTY

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != EMPTY:
      return True
    elif sum([i.count(EMPTY) for i in board]) == 0:
      return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
      return 1
    elif winner(board) == O:
      return -1
    else:
      return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
      v = -2
      if terminal(board):
        return utility(board)
      for action in actions(board):
        v = max(v, min_value(result(board, action)))
      return v

    def min_value(board):
      v = 2
      if terminal(board):
        return utility(board)
      for action in actions(board):
       v = min(v, max_value(result(board, action)))
      return v

    optimal_action = ()
    v = 0
    v_p = 0
    if terminal(board):
      return None
    if player(board) == X:
      for action in actions(board):
        v_p = v
        v = max_value(result(board, action))
        if v_p >= v:
          optimal_action = action
      return optimal_action
    else:
      for action in actions(board):
        v_p = v
        v = min_value(result(board, action))
        if v_p <= v:
          optimal_action = action
      return optimal_action