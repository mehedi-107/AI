import math
import copy
import random

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
    countX=0
    countO=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                countX+=1
            if board[i][j]==O:
                countO+=1
    if countX==countO:
        return X  
    else:
        return O 


def actions(board):
    all_actions=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                all_actions.append([i,j])
    if len(all_actions)==0:
        raise Exception("No actions left")
    return all_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    Player=player(board)
    temp_board=copy.deepcopy(board)
    temp_board[action[0]][action[1]]=Player
    return temp_board

def winner(board):

    #Returns the winner of the game, if there is one.
    
    for i in range(3):
        if(board[i][0]==board[i][1]==board[i][2]!=EMPTY):
            return board[i][0]
    for j in range(3):
        if(board[0][j]==board[1][j]==board[2][j]!=EMPTY):
            return board[0][j]
    if board[1][1]==board[0][2]==board[2][0]!=EMPTY or board[1][1]==board[0][0]==board[2][2]!=EMPTY:
        return board[1][1]
    return EMPTY

def terminal(board):
    
    #Returns True if game is over, False otherwise.
    
    if winner(board) != EMPTY:
        return True
    empty_count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                empty_count+=1
    if empty_count==0:
        return True
    else:
        return False


def utility(board):
    
    #Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    
    Winner=winner(board)
    if Winner==X:
        return 1
    elif Winner==O:
        return -1
    else:
        return 0

def help_minimax(board):
    if terminal(board)==True:
        return utility(board)
    action=actions(board)
    values=[]
    for i in range(len(action)):
        temp_board=result(board,action[i])
        values.append(help_minimax(temp_board))
    if player(board)==X:
        return max(values)
    else:
        return min(values)
        
    

def minimax(board):

    #Returns optimal move (i,j) 
    
    action=actions(board)
    if len(action)==9:
        return action[random.randint(1,100000)%len(action)]
    values=[]
    for i in range(len(action)):
        temp_board=result(board,action[i])
        values.append([help_minimax(temp_board),action[i]])
    final_values=[]
    if player(board)==X:
        for i in range(len(values)):
            if values[i][0]==1:
                final_values.append(values[i][1])
    else:
        for i in range(len(values)):
            if values[i][0]==-1:
                final_values.append(values[i][1])
    if len(final_values)!=0:
        return final_values[random.randint(1,100000)%len(final_values)]
    for i in range(len(values)):
        if values[i][0]==0:
            final_values.append(values[i][1])
    return final_values[random.randint(1,100000)%len(final_values)]