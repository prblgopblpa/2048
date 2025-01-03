import random


def init_board():
    board = []
    for i in range(4):
        board += [["0"] * 4]

    addNewNum(board, 2)
    
    return board    
                       
                                                
def addNewNum(board, n):

    
    for i in range(n):
        newNum = str(random.choice([2,4]))
        randomx = random.randrange(4)
        randomy = random.randrange(4)
        while board[randomy][randomx] != "0":
            randomx = random.randrange(4)
            randomy = random.randrange(4)
        board[randomy][randomx] = newNum 
        
    
def checkWin(board):

    
    win = False
    for line in board:
        for num in line:
            if num == "2048":
                win = True
    return win

                
def add(board, i_list, j_list, i_direction, j_direction):
    


    move = 0
    for i in i_list:
        for j in j_list:

            if board[i][j] == board[i + i_direction][j + j_direction]:
                board[i+ i_direction][j + j_direction] = str(int(board[i][j])+int(board[i+ i_direction][j+j_direction]))
                if board[i][j] != 0:
                    move += 1
                board[i][j] = "0"
    return move

    
def push(board, i_list, j_list, i_direction, j_direction):
    


    move = 0
    for i in i_list:
        for j in j_list:
            if board[i + i_direction][j + j_direction] == "0":
                board[i + i_direction][j + j_direction] = board[i][j]
                if board[i][j] != 0:
                    move += 1
                board[i][j] = "0"
    return move


def pushDirection(board, UserInput):


    global i_list, j_list, i_direction, j_direction
    move = 0
    if UserInput == "u":
        i_list, j_list = range(1,4), range(4)
        i_direction, j_direction = -1, 0
    elif UserInput == "d":
        i_list, j_list = range(2,-1,-1), range(4)
        i_direction, j_direction = 1, 0
    elif UserInput == "l":
        i_list, j_list = range(4), range(1,4)
        i_direction, j_direction = 0, -1
    elif UserInput == "r":
        i_list, j_list = range(4), range(2,-1,-1)
        i_direction, j_direction = 0, 1
       
    for i in range(4):
        move += push(board, i_list, j_list, i_direction, j_direction)
    move += add(board, i_list, j_list, i_direction, j_direction)
    for i in range(4):
        move += push(board, i_list, j_list, i_direction, j_direction)
    
    return move


def checkCell(board, i, j):

    
    move_i = []
    move_j = []
    board_size = len(board)
    if i > 0:
        move_i.append(-1)
        move_j.append(0)
    if i < (board_size - 1):
        move_i.append(1)
        move_j.append(0)
    if j > 0:
        move_j.append(-1)
        move_i.append(0)
    if j < (board_size - 1):
        move_j.append(1)
        move_i.append(0)
    for k in range(len(move_i)):
        if board[i + move_i[k]][j + move_j[k]] == board[i][j]:
            return True
    return False


def canMove(board):


    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                return True
            if checkCell(board, i, j):
                return True
    return False

def checkLose(board):

    
    nozero = False
    
    for elt in board:
        nozero = nozero or ("0" in elt)

    if not nozero:
        return not canMove(board)
    return False      
        
    
def main(board, UserInput):
                                         
    if not checkLose(board) and not checkWin(board):
                                                                  
        move = pushDirection(board, UserInput)        
        if move != 0:
            addNewNum(board, 1)            
    return board
        
    

