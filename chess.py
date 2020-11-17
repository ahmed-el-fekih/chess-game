### Ahmed El Fekih
### Andrew ID: aelfekih
### Final Project
### Chess


# making the board
# consists of all chess pieces (each has a specific letter)
# first letter is color second is piece
# board is a list of lists
# printing a piece with x,y coordinates ==> board[y][x]
# we are viewing the board from the POV of white
# 8 columns, 8 rows.

board = [['bR', 'bk', 'bB', 'bQ', 'bK', 'bB', 'bk', 'bR'],
         ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
         ['__', '__', '__', '__', '__', '__', '__', '__'],
         ['__', '__', '__', '__', '__', '__', '__', '__'],
         ['__', '__', '__', '__', '__', '__', '__', '__'],
         ['__', '__', '__', '__', '__', '__', '__', '__'],
         ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
         ['wR', 'wk', 'wB', 'wQ', 'wK', 'wB', 'wk', 'wR']]


# printing the board, x and y coords for easier use
def printB():
    print(['', '00', '01', '02', '03', '04', '05', '06', '07'])
    for row in range(len(board)):
        print([row]+board[row])


# class that contains rules for all pieces
class Pieces:
    def __init__(self, board, input):
        self.x1 = int(input[0])
        self.y1 = int(input[1])
        self.x2 = int(input[2])
        self.y2 = int(input[3])
        self.b = board
        self.color = board[self.y1][self.x1][0]
        self.piece = board[self.y1][self.x1]
        self.eaten = []

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
            if board[self.y1-plr][self.x1] == '__':
                moves.append(str(self.x1) + str(self.y1-plr))
                # making sure that 2 squares are empty so it can move there
                if board[self.y1-2*plr][self.x1] == '__':
                    moves.append(str(self.x1) + str(self.y1-2*plr))

        # pawn isn't in the start position
        else:
            # if square in front is empty, the piece can move there
            # also check for border cases
            if self.y1 != 0 and self.y1 != 7 and board[self.y1-plr][self.x1] == '__':
                moves.append(str(self.x1) + str(self.y1-plr))

        # pawn can eat diagonally
        # check for border cases
        # can only move diagonally if there is a piece of opposing color there
        if self.x1 != 0 and board[self.y1-plr][self.x1-1][0] != self.color and board[self.y1-plr][self.x1-1][0] != '_':
            moves.append(str(self.x1-1) + str(self.y1-plr))

        if self.x1 != 7 and board[self.y1-plr][self.x1+1][0] != self.color and board[self.y1-plr][self.x1+1][0] != '_':
            moves.append(str(self.x1+1) + str(self.y1-plr))

        return moves


    def knight(self):
        moves = []

        # moving one square up or down and 2 squares to the right or left
        # accounting for all border cases
        if self.y1 != 7 and self.x1 < 6 and board[self.y1 + 1][self.x1 + 2] != self.color:
            moves.append(str(self.x1 + 2) + str(self.y1 + 1))

        if self.y1 != 7 and self.x1 > 1 and board[self.y1 + 1][self.x1 - 2] != self.color:
            moves.append(str(self.x1 - 2) + str(self.y1 + 1))

        if self.y1 != 0 and self.x1 < 6 and board[self.y1 - 1][self.x1 + 2] != self.color:
            moves.append(str(self.x1 + 2) + str(self.y1 - 1))

        if self.y1 != 0 and self.x1 > 2 and board[self.y1 - 1][self.x1 - 2] != self.color:
            moves.append(str(self.x1 - 2) + str(self.y1 - 1))

        # moving 2 squares up or down and 1 square to the right or left
        if self.x1 != 7 and self.y1 < 6 and board[self.y1 + 2][self.x1 + 1] != self.color:
            moves.append(str(self.x1 + 1) + str(self.y1 + 2))

        if self.x1 != 7 and self.y1 > 1 and board[self.y1 - 2][self.x1 + 1] != self.color:
            moves.append(str(self.x1 + 1) + str(self.y1 - 2))

        if self.x1 != 0 and self.y1 < 6 and board[self.y1 + 2][self.x1 - 1] != self.color:
            moves.append(str(self.x1 - 1) + str(self.y1 + 2))

        if self.x1 != 0 and self.y1 > 1 and board[self.y1 - 2][self.x1 - 1] != self.color:
            moves.append(str(self.x1 - 1) + str(self.y1 - 2))

        return moves

    # still not working need to debug
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
                        if board[self.y1 + j][self.x1 + i][0] != self.color:
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
                        if h != self.x1 and board[self.y1][h][0] != '_':
                            p = False
                        if i > 0:
                            h += 1
                        elif i < 0:
                            h -= 1
                    # adding horizontal moves if rook isn't eating pieces from same color
                    # and isn't jumping over pieces
                    if p == True and board[self.y1][self.x1 + i][0] != self.color:
                        moves.append(str(self.x1 + i) + str(self.y1))

            # accounting for border cases
            if 0 <= self.y1 + i <= 7:
                # if rook moves vertically
                if i != 0:
                    r = True
                    v = self.y1
                    # making sure that rook isn't jumpint over any pieces
                    while v != self.y1 + i:
                        if v != self.y1 and board[v][self.x1][0] != '_':
                            r = False
                        if i > 0:
                            v += 1
                        else:
                            v -= 1
                    # adding horizontal moves if rook isn't eating pieces from same color
                    # and isn't jumping over any pieces
                    if r == True and board[self.y1 + i][self.x1][0] != self.color:
                        moves.append(str(self.x1) + str(self.y1 + i))
        return moves

    def bishop(self):






    # helper that will be used in the main movePiece function
    # basically moves the pieces
    def move(self,piece,function):
        # pawn
        if self.piece[1] == piece:
            if (str(self.x2) + str(self.y2)) in function:
                # move it and change initial position to '__'
                board[self.y1][self.x1] = '__'
                # check if a piece was eaten
                # if so add it to the eaten list
                if board[self.y2][self.x2] != '__':
                    self.eaten.append(board[self.y2][self.x2])
                # move piece
                board[self.y2][self.x2] = self.piece

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

        # code used for debugging
        if self.piece[1] != 'k' and self.piece[1] != 'P' and self.piece[1] != 'K' and self.piece[1] != 'R':
            board[self.y1][self.x1] = '__'
            board[self.y2][self.x2] = self.piece


# far from complete code
# implements the class pieces and lets 2 players play
# still missing conditions, winner condition, and much more
while True:
    printB()
    inp1 = input('White make your move: ')
    p1 = Pieces(board,inp1)
    p1.movePiece()
    printB()
    inp2 = input('Black make your move: ')
    p2 = Pieces(board,inp2)
    p2.movePiece()

