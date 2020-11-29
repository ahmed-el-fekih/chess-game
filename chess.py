### Ahmed El Fekih
### Andrew ID: aelfekih
### Final Project
### Chess
import random
import time
from tkinter import *
from tkinter import messagebox



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
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
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
        # moves will be recorded as tuples
        self.moves = []
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
        if self.player == 'b':
            plr = -1
        if self.player == 'w':
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
        if self.x1 != 0 and self.y1 != 7 and self.board[self.y1-plr][self.x1-1][0] != self.color and self.board[self.y1-plr][self.x1-1][0] != '_':
            moves.append(str(self.x1-1) + str(self.y1-plr))

        if self.x1 != 7 and self.y1 != 7 and self.board[self.y1-plr][self.x1+1][0] != self.color and self.board[self.y1-plr][self.x1+1][0] != '_':
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
                    self.moves.append([(self.x1,self.y1),(self.x2,self.y2),()])
                else:
                    self.moves.append([(self.x1, self.y1), (self.x2, self.y2)])
                # move piece
                self.board[self.y2][self.x2] = self.piece
                print(self.moves)

    def undoMove(self):
        print('this is self.moves: ',self.moves[len(self.moves)-1])
        lastMove = self.moves[len(self.moves)-1]
        if len(lastMove) == 2:
            self.board[lastMove[0][1]][lastMove[0][0]] = self.board[lastMove[1][1]][lastMove[1][0]]
            self.board[lastMove[1][1]][lastMove[1][0]] = '__'
            self.moves.pop()
        elif len(lastMove) == 3:
            self.board[lastMove[0][1]][lastMove[0][0]] = self.board[lastMove[1][1]][lastMove[1][0]]
            self.board[lastMove[1][1]][lastMove[1][0]] = self.eaten[len(self.eaten)-1]
            self.moves.pop()
            self.eaten.pop()

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


    def possibleMoves(self):


        # pawn
        if self.piece[1] == 'P':
            return self.pawn()

        # knight
        if self.piece[1] == 'k':
            return self.knight()

        # king
        if self.piece[1] == 'K':
            return self.king()

         # rook
        if self.piece[1] == 'R':
            return self.rook()

        # bishop
        if self.piece[1] == 'B':
            return self.bishop()

        # queen
        if self.piece[1] == 'Q':
            return self.queen()

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
        if self.player == self.color and self.checkmoves() != False:
            return True
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
        self.printB()
        self.getinput()
        while self.done() != True:
            while self.player != self.color or self.checkmoves() == False:
                print("invalid move")
                self.printB()
                self.getinput()
            self.movePiece()
            if self.done() == True:
                break
            self.changePlayer()
            self.printB()
            self.getinput()
        print('Congratsss!! '+ self.player + ' wins!!')




#chess = Chess()
#chess.run()

########################################################################################
## GUI
## User interface test

darkColor = '#58ae8b'
lightColor = '#feffed'
class ChessInterface(Chess):
    def __init__(self,size=60):
        Chess.__init__(self)
        self.unit = size
        self.height = self.unit*8
        self.width = self.unit*8
        self.wnd = Tk()
        # original: '40x490'
        self.wnd.geometry('490x510')
        self.pieces = {'bP': '\u265F',
                       'bK': '\u265A',
                       'bQ': '\u265B',
                       'bk': '\u265E',
                       'bB': '\u265D',
                       'bR': '\u265C',
                       'wP': '\u2659',
                       'wK': '\u2654',
                       'wQ': '\u2655',
                       'wk': '\u2658',
                       'wB': '\u2657',
                       'wR': '\u2656',
                       '__': ''
                       }
        self.canvas = Canvas(self.wnd, height=self.height, width=self.width)
        self.canvas.bind('<Button-1>',self.mousepress)
        self.button = Button(self.wnd,text='redo',command = self.redo)
        self.canvas.pack()
        self.button.pack()
        self.selected = ()
        self.clicks = []
        self.extra = ()
        self.tags = {}
        self.textTags = {}

    # drawing the board on the interface
    def draw(self):
        self.canvas.delete()
        for i in range(8):
            for j in range(8):
                if (i%2 != 1 and j%2 == 1) or ((i%2 == 1 or i%2 == 2) and j%2 != 1):
                    self.tags[(i,j)] = (self.canvas.create_rectangle(i*self.unit, j*self.unit,i*self.unit+self.unit,j*self.unit+self.unit,fill='dark red'),'dark red')
                else:
                    self.tags[(i,j)] = (self.canvas.create_rectangle(i*self.unit, j*self.unit,i*self.unit+self.unit,j*self.unit+self.unit,fill= lightColor),lightColor)
                self.textTags[(i,j)] = self.canvas.create_text(i * self.unit + self.unit // 2, j * self.unit + self.unit // 2,text=self.pieces[self.board[j][i]],font=('DejaVu Sans', self.unit // 2))

    # updates the interface every time a move is made
    def updatePieces(self,start,end):
        self.canvas.delete(self.textTags[(start[0],start[1])])
        self.canvas.delete(self.textTags[(end[0],end[1])])
        self.textTags[(start[0],start[1])] = self.canvas.create_text(start[0] * self.unit + self.unit // 2,
                                                                     start[1] * self.unit + self.unit // 2,
                                                                     text=self.pieces[self.board[start[1]][start[0]]],
                                                                     font=('DejaVu Sans', self.unit // 2))
        self.textTags[(end[0],end[1])] = self.canvas.create_text(end[0] * self.unit + self.unit // 2,
                                                                 end[1] * self.unit + self.unit // 2,
                                                                 text=self.pieces[self.board[end[1]][end[0]]],
                                                                 font=('DejaVu Sans', self.unit // 2))

    def changeInfo(self,coord):
        self.x1 = coord[0][0]
        self.y1 = coord[0][1]
        self.x2 = coord[1][0]
        self.y2 = coord[1][1]
        self.color = self.board[self.y1][self.x1][0]
        self.piece = self.board[self.y1][self.x1]

    def redo(self):
        self.undoMove()
        self.draw()
        print('ohoy')

    # dumb AI that just makes a random valid move
    def dumbAI(self):
        i = random.randint(0, 7)
        j = random.randint(0, 7)
        self.x1 = i
        self.y1 = j
        self.color = self.board[self.y1][self.x1][0]
        self.piece = self.board[self.y1][self.x1]
        while self.color != self.player or self.possibleMoves() == []:
            # if self.color == '_':
            #     continue

            i = random.randint(0, 7)
            j = random.randint(0, 7)
            self.x1 = i
            self.y1 = j
            self.piece = self.board[self.y1][self.x1]
            self.color = self.board[self.y1][self.x1][0]

        move = random.choice(self.possibleMoves())
        self.x2 = int(move[0])
        self.y2 = int(move[1])
        self.movePiece()
        self.updatePieces((self.x1, self.y1), (self.x2, self.y2))
        if self.done() == True:
            if self.player == 'b':
                messagebox.showinfo('Result', 'Black wins!!')
            else:
                messagebox.showinfo('Resutl', 'White wins!!')
        self.changePlayer()

    # this is a helper that will be used in the mousepressed function
    # dehilights previously selected squares
    # deselect a piece by clicking twice
    # restricting user to only his pieces
    def partOfMain(self, x, y):
        # dehighlight the highlighted squares
        if len(self.clicks) == 1:
            self.x2 = x
            self.y2 = y
            if not self.checkmoves():
                for i in self.possibleMoves():
                    self.canvas.itemconfig(self.tags[(int(i[0]), int(i[1]))][0],
                                           fill=self.tags[(int(i[0]), int(i[1]))][1])

        # user can deselect the piece if he clicks twice
        if self.selected == (x, y):
            self.selected = ()
            self.clicks = []
            # making the square turn back to original color if it was deselected
            self.canvas.itemconfig(self.tags[(x, y)][0], fill=self.tags[(x, y)][1])

        if self.selected == (x, y):
            self.selected = ()
            self.clicks = []
            # making the square turn back to original color if it was deselected
            self.canvas.itemconfig(self.tags[(x, y)][0], fill=self.tags[(x, y)][1])

        else:
            # making sure that the user doesnt choose to move an opponents piece
            if (self.board[y][x][0] == self.player and len(self.clicks) == 0) or len(self.clicks) == 1:
                self.selected = (x, y)
                self.clicks.append(self.selected)
                print('self.clicks: ', self.clicks)

    # this is a part of mousepress function
    # takes care of most of the highlight rules and restrictions
    # modifies self.click and self.selected
    def highlightAndModify(self, x, y):
        if self.clicks != []:
            # highlight square to show where player clicked
            # if player clicks an empty square or one not containing his pieces, dont highlight
            if self.board[self.selected[1]][self.selected[0]][0] == self.player:
                self.canvas.itemconfig(self.tags[self.clicks[0]][0], fill='yellow')

        # if user clicks 2 pieces that belong to him twice, only choose and highlight the last one
        if len(self.clicks) == 2:
            if self.board[y][x][0] == self.board[self.clicks[0][1]][self.clicks[0][0]][0] == self.player:
                self.canvas.itemconfig(self.tags[self.clicks[0]][0], fill=self.tags[self.clicks[0]][1])
                self.canvas.itemconfig(self.tags[self.clicks[1]][0], fill='yellow')
                self.clicks = [self.selected]

        # highlighting possible moves with the selected piece
        if len(self.clicks) == 1 and self.board[y][x] != '__':
            self.x1 = x
            self.y1 = y
            self.piece = self.board[self.y1][self.x1]
            self.color = self.board[self.y1][self.x1][0]
            for i in self.possibleMoves():
                self.canvas.itemconfig(self.tags[(int(i[0]), int(i[1]))][0], fill='light blue')
            return

    def strongAI(self):
        pass


    # function that runs the full game based on the event given to it
    def mousepress(self,event):
        # calculate which square the user clicks on
        x = event.x//self.unit
        y = event.y//self.unit

        self.partOfMain(x,y)

        self.highlightAndModify(x,y)

        # changing board and moving the pieces if conditions met
        if len(self.clicks) == 2:
            self.changeInfo(self.clicks)
            if self.player == self.color and self.checkmoves() != False:
                # dehighlight the previously highlighted squares
                for i in self.possibleMoves():
                    self.canvas.itemconfig(self.tags[(int(i[0]),int(i[1]))][0], fill=self.tags[(int(i[0]),int(i[1]))][1])
                self.canvas.itemconfig(self.tags[(self.clicks[0][0],self.clicks[0][1])][0]
                                       , fill = self.tags[(self.clicks[0][0],self.clicks[0][1])][1])
                self.movePiece()
                self.updatePieces(self.clicks[0],self.clicks[1])
                self.printB()
                # announce winner when game ends
                if self.done() == True:
                    if self.player == 'b':
                        messagebox.showinfo('Result', 'Black wins!!')
                    else:
                        messagebox.showinfo('Resutl','White wins!!')
                self.changePlayer()
                # playing against the dumb AI
                # to play against other non computer player, comment out this line
                #self.dumbAI()
            else:
                self.canvas.itemconfig(self.tags[self.clicks[0]][0], fill= self.tags[self.clicks[0]][1])
                self.canvas.itemconfig(self.tags[self.clicks[0]][1], fill= self.tags[self.clicks[0]][1])
            self.clicks = []
            self.selected = ()

    def runTk(self):
        self.draw()
        self.wnd.mainloop()


    ## trying to make the stupid AI


a = ChessInterface()
a.runTk()

### to do:
### done 1- debug the mouse press function and make the interface more usable
### done 2- highlight the intended piece
### done 3- highlight the possible moves
### done 4- including the condition where king is dead
### 5- option of going back to the menu
### done 5- pop up that tells which player won
### 6- clean and nice main menu
### 7- try the rigidity of the program
### done 8- make the interface smoother and faster by only changing the text and not drawing every time again
### done this will require to divide draw into 2 functions and maybe using the configure for changing text
### done - dumb AI
### 10- make main menu, when a game is done, return back to the main menu after showing the messagebox


### done : undoMove
### done: tracing all moves
### done: tracing all eaten pieces
### small bug in dumb AI, if all pieces are eaten infinite while loop and program gets stuck