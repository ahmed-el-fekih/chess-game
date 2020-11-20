### Ahmed El Fekih
### Andrew ID: aelfekih
### Final Project
### Chess



# class that contains all details regarding the game
class Chess:
    def __init__(self):
        self.board = [['bR', 'bk', 'bB', 'bQ', 'bK', 'bB', 'bk', 'bR'],
                  ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                  ['__', '__', '__', '__', '__', '__', '__', '__'],
                  ['__', '__', '__', '__', '__', '__', '__', '__'],
                  ['__', '__', '__', '__', '__', '__', '__', '__'],
                  ['__', '__', '__', '__', '__', '__', '__', '__'],
                  ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                  ['wR', 'wk', 'wB', 'wQ', 'wK', 'wB', 'wk', 'wR']]
        Chess.printB(self)
        self.input = input('White make a move: ')
        self.x1 = int(self.input[0])
        self.y1 = int(self.input[1])
        self.x2 = int(self.input[2])
        self.y2 = int(self.input[3])
        # making the board
        # consists of all chess pieces (each has a specific letter)
        # first letter is color second is piece
        # board is a list of lists
        # printing a piece with x,y coordinates ==> board[y][x]
        # we are viewing the board from the POV of white
        # 8 columns, 8 rows.

        self.color = self.board[self.y1][self.x1][0]
        self.piece = self.board[self.y1][self.x1]
        self.eaten = []
        self.player = 'w'

    # gets input from the user and changes the properties according to input
    def getinput(self):
        if self.player == 'w':
            playerInp = input("White make a move: ")
        else:
            playerInp = input('Black make a move: ')
        self.x1 = int(playerInp[0])
        self.y1 = int(playerInp[1])
        self.x2 = int(playerInp[2])
        self.y2 = int(playerInp[3])
        self.color = self.board[self.y1][self.x1][0]
        self.piece = self.board[self.y1][self.x1]

    # changes the player
    def changePlayer(self):
        if self.player == 'w':
            self.player = 'b'
        else:
            self.player = 'w'
        self.printB()

    # printing the board, x and y coords for easier use
    def printB(self):
        print(['', '00', '01', '02', '03', '04', '05', '06', '07'])
        for row in range(len(self.board)):
            print([row] + self.board[row])

    def pawn(self):
        # gives back all of possible moves for a single piece
        # moves will be an int
        # first digit is x pos, second digit is y pos
        moves = []
        if self.color == 'b':
            plr = -1
        if self.color == 'w':
            plr = 1

        # initial position
        if (self.y1 == 1 and plr == -1) or (self.y1 == 6 and plr == 1):
            # making sure that the square in front is empty
            if self.board[self.y1-plr][self.x1] == '__':
                moves.append(str(self.x1) + str(self.y1-plr))
                # making sure that 2 squares are empty so it can move there
                if self.board[self.y1-2*plr][self.x1] == '__':
                    moves.append(str(self.x1) + str(self.y1-2*plr))

        # pawn isn't in the start position
        else:
            # if square in front is empty, the piece can move there
            # also check for border cases
            if self.y1 != 0 and self.y1 != 7 and self.board[self.y1-plr][self.x1] == '__':
                moves.append(str(self.x1) + str(self.y1-plr))

        # pawn can eat diagonally
        # check for border cases
        # can only move diagonally if there is a piece of opposing color there
        if self.x1 != 0 and self.board[self.y1-plr][self.x1-1][0] != self.color and self.board[self.y1-plr][self.x1-1][0] != '_':
            moves.append(str(self.x1-1) + str(self.y1-plr))

        if self.x1 != 7 and self.board[self.y1-plr][self.x1+1][0] != self.color and self.board[self.y1-plr][self.x1+1][0] != '_':
            moves.append(str(self.x1+1) + str(self.y1-plr))

        return moves


    def knight(self):
        moves = []

        # moving one square up or down and 2 squares to the right or left
        # accounting for all border cases
        if self.y1 != 7 and self.x1 < 6 and self.board[self.y1 + 1][self.x1 + 2][0] != self.color:
            moves.append(str(self.x1 + 2) + str(self.y1 + 1))

        if self.y1 != 7 and self.x1 > 1 and self.board[self.y1 + 1][self.x1 - 2][0] != self.color:
            moves.append(str(self.x1 - 2) + str(self.y1 + 1))

        if self.y1 != 0 and self.x1 < 6 and self.board[self.y1 - 1][self.x1 + 2][0] != self.color:
            moves.append(str(self.x1 + 2) + str(self.y1 - 1))

        if self.y1 != 0 and self.x1 > 2 and self.board[self.y1 - 1][self.x1 - 2][0] != self.color:
            moves.append(str(self.x1 - 2) + str(self.y1 - 1))

        # moving 2 squares up or down and 1 square to the right or left
        if self.x1 != 7 and self.y1 < 6 and self.board[self.y1 + 2][self.x1 + 1][0] != self.color:
            moves.append(str(self.x1 + 1) + str(self.y1 + 2))

        if self.x1 != 7 and self.y1 > 1 and self.board[self.y1 - 2][self.x1 + 1][0] != self.color:
            moves.append(str(self.x1 + 1) + str(self.y1 - 2))

        if self.x1 != 0 and self.y1 < 6 and self.board[self.y1 + 2][self.x1 - 1][0] != self.color:
            moves.append(str(self.x1 - 1) + str(self.y1 + 2))

        if self.x1 != 0 and self.y1 > 1 and self.board[self.y1 - 2][self.x1 - 1][0] != self.color:
            moves.append(str(self.x1 - 1) + str(self.y1 - 2))

        return moves

    def king(self):
        # list of all possible moves based on the initial position
        moves = []
        # king can move in any direction but only one square each time
        # using 2 loops helps make the code compact while accounting for all moves

        for i in range(-1,2):
            for j in range(-1,2):
                # user has to move
                if not(i == j == 0):
                    # accounting for border cases
                    if 0 <= self.x1 + i <= 7 and 0 <= self.y1 + j <= 7:
                        # making sure that king can't eat pieces from the same color
                        if self.board[self.y1 + j][self.x1 + i][0] != self.color:
                            moves.append(str(self.x1 + i) + str(self.y1 + j))
        return moves

    def rook(self):
        # list of all possible moves
        moves = []
        for i in range(-7,8):
            # accounting for border cases
            if 0 <= self.x1 + i <= 7:
                # if rook moves horizontally
                if i != 0:
                    p = True
                    h = self.x1
                    # making sure that rook isn't jumping over any pieces
                    while h != self.x1 + i:
                        if h != self.x1 and self.board[self.y1][h][0] != '_':
                            p = False
                        if i > 0:
                            h += 1
                        elif i < 0:
                            h -= 1
                    # adding horizontal moves if rook isn't eating pieces from same color
                    # and isn't jumping over pieces
                    if p == True and self.board[self.y1][self.x1 + i][0] != self.color:
                        moves.append(str(self.x1 + i) + str(self.y1))

            # accounting for border cases
            if 0 <= self.y1 + i <= 7:
                # if rook moves vertically
                if i != 0:
                    r = True
                    v = self.y1
                    # making sure that rook isn't jumping over any pieces
                    while v != self.y1 + i:
                        if v != self.y1 and self.board[v][self.x1][0] != '_':
                            r = False
                        if i > 0:
                            v += 1
                        else:
                            v -= 1
                    # adding horizontal moves if rook isn't eating pieces from same color
                    # and isn't jumping over any pieces
                    if r == True and self.board[self.y1 + i][self.x1][0] != self.color:
                        moves.append(str(self.x1) + str(self.y1 + i))
        return moves


    def bishop(self):

        moves = []

        for i in range(-7,8):
            if 0 <= self.x1 + i <= 7 and 0 <= self.y1 + i <= 7:
            # staying in the same position isn't a move
                if i != 0:
                    # moving diagonally down right (+1,+1)
                    p = True
                    # nwse is north west, south east represents the possible diagonal movements
                    nwse = self.x1
                    nwseY = self.y1
                    while nwse != self.x1 + i:
                        # making sure that bishop doesn't jump over pieces
                        if nwse != self.x1 and self.board[nwseY][nwse][0] != '_':
                            p = False
                        if i > 0:
                            nwse += 1
                            nwseY += 1
                        else:
                            nwse -= 1
                            nwseY -= 1
                    if p == True and self.board[self.y1 + i][self.x1 + i][0] != self.color:
                        moves.append(str(str(self.x1 + i) + str(self.y1 + i)))
        for i in range(-7,8):
            if 0 <= self.x1 + i <= 7 and 0 <= self.y1 - i <= 7:
                if i != 0:
                    n = True
                    # nesw is north east, south west, represents the other possible movements
                    nesw = self.x1
                    neswY = self.y1
                    while nesw != self.x1 + i:
                        # making sure that bishop doesn't jump over pieces
                        if nesw != self.x1 and self.board[neswY][nesw][0] != '_':
                            n = False
                        if i > 0:
                            nesw += 1
                            neswY -= 1
                        else:
                            nesw -= 1
                            neswY += 1
                    # making sure that it doesn't eat pieces of same color
                    if n == True and self.board[self.y1 - i][self.x1 + i][0] != self.color:
                        moves.append(str(str(self.x1 + i) + str(self.y1 - i)))
        return moves


    def queen(self):
        move = self.bishop() + self.rook()
        return move



    # helper that will be used in the main movePiece function
    # basically moves the pieces
    def move(self,piece,function):
        # pawn
        if self.piece[1] == piece:
            if (str(self.x2) + str(self.y2)) in function:
                # move it and change initial position to '__'
                self.board[self.y1][self.x1] = '__'
                # check if a piece was eaten
                # if so add it to the eaten list
                if self.board[self.y2][self.x2] != '__':
                    self.eaten.append(self.board[self.y2][self.x2])
                # move piece
                self.board[self.y2][self.x2] = self.piece

    # helper used in checkmoves
    def check(self,moves):
        wantedMove = (str(self.x2) + str(self.y2))
        if wantedMove not in moves:
            return False

    # checks all the avaliable moves
    def checkmoves(self):
        # pawn
        if self.piece[1] == 'P':
            P = self.pawn()
            if self.check(P) == False:
                return False
            return True

        # knight
        if self.piece[1] == 'k':
            k = self.knight()
            if self.check(k) == False:
                return False
            return True
        # king
        if self.piece[1] == 'K':
            K = self.king()
            if self.check(K) == False:
                return False
            return True
        # rook
        if self.piece[1] == 'R':
            R = self.rook()
            if self.check(R) == False:
                return False
            return True

        # bishop
        if self.piece[1] == 'B':
            B = self.bishop()
            if self.check(B) == False:
                return False
            return True

        # queen
        if self.piece[1] == 'Q':
            Q = self.queen()
            if self.check(Q) == False:
                return False
            return True
        return False


    # moves the piece
    def movePiece(self):
        # pawn
        if self.piece[1] == 'P':
            P = self.pawn()
            self.move('P',P)


        # knight
        if self.piece[1] == 'k':
            k = self.knight()
            self.move('k',k)

        # king
        if self.piece[1] == 'K':
            K = self.king()
            self.move('K',K)

         # rook
        if self.piece[1] == 'R':
            R = self.rook()
            self.move('R',R)

        # bishop
        if self.piece[1] == 'B':
            B = self.bishop()
            self.move('B',B)

        # queen
        if self.piece[1] == 'Q':
            Q = self.queen()
            self.move('Q',Q)

    # should check if the move is valid
    # not working for some reason
    def isValid(self):
        if self.player != self.color or self.checkmoves() == False:
            return False
        return True

    # True means the game is done
    # False means the game is still ongoing
    # the game is only done when either of the kings is eaten
    def done(self):
        wKing = False
        for i in self.board:
            for j in i:
                if j == 'wK':
                    wKing = True
        bKing = False
        for i in self.board:
            for j in i:
                if j == 'bK':
                    bKing = True
        if bKing == True and wKing == True:
            return False
        else:
            return True

    # alternates between white and black while checking for valid moves
    # stops when either king is dead
    def run(self):
        while self.done() != True:
            while self.player != self.color or self.checkmoves() == False:
                print("invalid move")
                self.printB()
                self.getinput()
            self.movePiece()
            if self.done() == True:
                break
            self.changePlayer()
            self.getinput()
        print('Congratsss!! '+ self.player + ' wins!!')



chess = Chess()
chess.run()


