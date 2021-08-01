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

    if terminal(board):
        return 7

    numX = 0
    numO = 0

    for i in board:
        for j in i:
            if j == X:
                numX = numX + 1
            elif j == O:
                numO = numO + 1

    if numX == numO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return 7

    possible = {}
    possible = set()

    x = 0
    for i in board:
        y = 0
        for j in i:
            if j == EMPTY:
                index = (x, y)
                possible.add(index)
            y = y+1
        x=x+1

    return possible



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    play = player(board)
    board2 = copy.deepcopy(board)

    if play != 'X' and play != 'O':
        raise Exception

    if board2[action[0]][action[1]] != EMPTY:
        raise Exception
    
    board2[action[0]][action[1]] = play

    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal win check

    for i in board:
        if i[0] == i[1] and i[0] == i[2] and i[0] != EMPTY:
            if i[0] == X:
                return X
            else:
                return O
            
    # Vertical win check
    
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        if board[0][0] != EMPTY:
            if board[0][0] == X:
                return X
            else:
                return O
    if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        if board[0][1] != EMPTY:
            if board[0][1] == X:
                return X
            else:
                return O
    if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        if board[0][2] != EMPTY:
            if board[0][2] == X:
                return X
            else:
                return O

    # Diagonal win check

    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] != EMPTY:
            if board[0][0] == X:
                return X
            else:
                return O
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if board[0][2] != EMPTY:
            if board[0][2] == X:
                return X
            else:
                return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    noVal = False
    for i in board:
        for j in i:
            if j == EMPTY:
                noVal = True
    if not noVal:
        return True
    
    if winner(board) == X or winner(board) == O:
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
    play = player(board)

    bestMove = (-1, -1)
    if play == X:
        bestVal = -1000
        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3) :    
            for j in range(3) :
            
                # Check if cell is empty
                if (board[i][j] == EMPTY) :
                
                    # Make the move
                    board[i][j] = play
    
                    # compute evaluation function for this
                    # move.
                    moveVal = minimaxScore(board)
    
                    # Undo the move
                    board[i][j] = EMPTY
    
                    # If the value of the current move is
                    # more than the best value, then update
                    # best/
                    if (moveVal > bestVal) :               
                        bestMove = (i, j)
                        bestVal = moveVal
    else:
        bestVal = 1000
        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3) :    
            for j in range(3) :
            
                # Check if cell is empty
                if (board[i][j] == EMPTY) :
                
                    # Make the move
                    board[i][j] = play
    
                    # compute evaluation function for this
                    # move.
                    moveVal = minimaxScore(board)
    
                    # Undo the move
                    board[i][j] = EMPTY
    
                    # If the value of the current move is
                    # more than the best value, then update
                    # best/
                    if (moveVal < bestVal) :               
                        bestMove = (i, j)
                        bestVal = moveVal
 
    return bestMove
    
def minimaxScore(board) :
    play = player(board)
    score = utility(board)
 
    # If Maximizer has won the game return his/her
    # evaluated score
    if (score == 1) :
        return score
 
    # If Minimizer has won the game return his/her
    # evaluated score
    if (score == -1) :
        return score
 
    # If there are no more moves and no winner then
    # it is a tie
    if (terminal(board) == True) :
        return 0
 
    # If this maximizer's move
    if (play == X) :    
        best = -1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (board[i][j]==EMPTY) :
                 
                    # Make the move
                    board[i][j] = play
 
                    # Call minimax recursively and choose
                    # the maximum value
                    best = max( best, minimaxScore(board) )
 
                    # Undo the move
                    board[i][j] = EMPTY
        return best
        # If this minimizer's move
    else :
        best = 1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (board[i][j] == EMPTY) :
                 
                    # Make the move
                    board[i][j] = play
 
                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimaxScore(board))
 
                    # Undo the move
                    board[i][j] = EMPTY
        return best
        
        



