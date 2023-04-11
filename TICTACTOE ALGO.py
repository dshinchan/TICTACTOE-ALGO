def printing(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()

def check(win , board , player):
    i,j=0,0
    while(i!=3):
        if(board[i][0] == player and board[i][1]== player and board[i][2] == player):
            win = player
            return win
        i=i+1
    
    while(j!=3):
        if(board[0][j] == player and board[1][j]==player and board[2][j] == player):
            win = player
            return win
        j=j+1

    if(board[0][0] == player and board[1][1]  == player and board[2][2]  == player ):
        win = player
        return win

    if(board[0][2] == player and board[1][1]  == player and board[2][0] == player ):
        win = player
        return win
    return 0
    
def place(board,player,count):
    cheated = False
    if(count == 3 or count == 6 or count == 9):
        i = int((count)/3)-1
    else:
        i = int((count)/3)
    j = int((count)%3)
    if(j == 0):
        j = j+2
    else:
        j=j-1
    if(board[i][j] == 0):
        board[i][j] = player
    else:
        print("oopss!don't cheat")
        cheated = True
    return board,cheated
    

def play_game():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    printing(board)
    winner = 0
    turn = 1

    while(winner == 0):
        x = int(input(f"chance of user {turn} - "))
        board, cheated= place(board , turn ,x)
        if(turn == 1 and not cheated):
            turn = 2
        elif(turn == 2 and not cheated):
            turn = 1
        printing(board)
        winner = check(winner,board,turn)
        
        if(winner == 1):
            print("JEETGYA player 1")
            return 0
        if(winner == 2):
            print("JEETGYA player 2")
            return 0
           
play_game()