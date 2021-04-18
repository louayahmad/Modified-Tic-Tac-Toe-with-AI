board = [' ' for x in range(10)]

#inserts letter X into the correct postion
def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#determines the winner of the game by checking if each place on the board is occupied and if it satifies tic tac toe game winning conditions
#For example, three X's or three O's 
def determineWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

#this is the player 
#lets player input position on board in the grid, if its full, they must choose another
def playerMove():
    run = True
    while run:
        move = input('Place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('This space is full!')
            else:
                print('Number not in range')
        except:
            print('Type a number!')

#How Game AI works:         
#this is the part of the in game computer or AI payer
#determines if there is a move that it could take to win the game first
#if not, it takes into account player move and blocks there move
#if no moves let player or computer win, computer will choose a corner or center depending on which is empty
def aiPlayerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if determineWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

#selects a random position to input computer 
def selectsRandomPosition(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    
#checks if the board is full
def fullBoard(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

#checks which player has one, and return a message stating it
def main():
    print('Get ready to play some Tic Tac Toe!')
    printBoard(board)

    while not(fullBoard(board)):
        if not(determineWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('O\'s won!')
            break

        if not(determineWinner(board, 'X')):
            move = aiPlayerMove()
            if move == 0:
                print('Game is a tie!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('X\'s won!')
            break

#checks if the board is full before the game ends, leading to a tie!
    if checkIfBoardFull(board):
        print('Tie Game!')

#this is the start game loop, asking the player if they want to play
while True:
    answer = input('Start the game? (Y/N')
    if answer.lower() == 'y' or answer.lower == 'yes' or answer.upper == 'YES' or answer.upper == 'Y':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
