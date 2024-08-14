def main():

    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print("Player 1 (X) please enter you name")
    playerOne = "testOne"#input()
    print("Player 2 (O) please enter you name")
    playerTwo = "testTwo"#input()
    for x in range (9):
        currPlayer = ""
        #PlayerOne's turn
        if x % 2 == 0:
            board = updateBoard(board, "X", playerOne)
            currPlayer = playerOne
        #PlayerTwo's turn
        else:
            board = updateBoard(board, "O", playerTwo)
            currPlayer = playerTwo
        printBoard(board)
        if (winCheck(board)):
            print(currPlayer + " won this game of Tic Tac Toe")
            return

#function to ask players where to play for their turn
def updateBoard(board, character, player):
    print("It is " + player + "'s turn")
    flag = True
    while(flag):
        try:
            print("Please enter a row")
            row = int(input()) - 1
            print("Please enter a coloumn")
            col = int(input()) - 1
            if(board[row][col] != 0):
                raise Exception
            flag = False
        except:
            print("This space on the board is already occupied")
    board[row][col] = character
    return board

def printBoard(board):
    for row in range (3):
        for col in range (3):
            currVal = board[row][col]
            if (col != 2):
                if (currVal == 0):
                    print(" |", end="")
                else:
                    print(currVal + "|", end="")
            else:
                if (currVal != 0):
                    print(currVal)
                else:
                    print()
        if (row != 2):
            print("-----")

#funcion to check the board for wins
def winCheck(board):
    if (verticleCheck(board) or horizontalCheck(board) or diagonalCheck(board)):
        return True  

def verticleCheck(board):
    for col in range(3):
        initial = board[0][col]
        if (initial == 0):  #check if coloumn is incomplete
            break   #no reason to check rest of coloumn
        for row in range(1,3):
            if (initial != board[row][col]):
                break
            elif (row == 2):
                return True
            
    return False

def horizontalCheck(board):
    for row in range(3):
        initial = board[row][0]
        if (initial == 0):  #check if row is incomplete
            break   #no reason to check rest of that row
        for col in range(1,3):
            if (initial != board[row][col]):
                break
            elif (col == 2):
                return True
            
    return False

def diagonalCheck(board):
    initial = -1
    for x in range(3): #check diagonal to the right
        curr = board[x][x]
        if (x == 0 and curr != 0): #check if the first square has been filled in
            initial = curr
        elif (curr != initial): #if a square has not been filled in break
            break
        elif (x == 2 and curr == initial): #check if are on the last box and if the values are the same
            return True
    col = 2
    for x in range(3): #check diagonal to the left
        curr = board[col - x][x]
        if (x == 0 and curr != 0): #check if the first square has been filled in
            initial = curr
        elif (curr != initial): #if a square has not been filled in break
            break
        elif (x == 2 and curr == initial): #check if are on the last box and if the values are the same
            return True
    return False

if __name__ == "__main__":
    main()