# Ahmed El Fekih
# aelfekih
# user interface + AI
from tkinter import *
from chess import Chess
import random
from tkinter import messagebox
LIGHTCOLOR = '#feffed'

## GUI
## User interface test


class mainMenu:
    def __init__(self):
        self.wnd = Tk()
        self.wnd.title('Chess Game')
        self.wnd.geometry('400x340')
        self.bg = PhotoImage(file='ch.png')
        self.label = Label(self.wnd, image=self.bg)
        self.label.place(x=0, y=0, relwidth=1)
        self.button1 = Button(self.wnd, text='player vs player',command = lambda mode = 1: self.runGame(mode))
        self.button2 = Button(self.wnd, text='player vs dumb AI',command = lambda mode = 2:self.runGame(mode))
        self.button3 = Button(self.wnd, text='Player vs always eat AI',command = lambda mode = 3:self.runGame(mode))
        self.button4 = Button(self.wnd, text='Player vs minimax AI',command = lambda mode = 4:self.runGame(mode))
        self.button5 = Button(self.wnd,text='Antichess: P vs P',command = lambda mode = 5:self.runGame(mode))
        self.button1.place(x=20, y=30)
        self.button2.place(x=20, y=100)
        self.button3.place(x=20, y=170)
        self.button4.place(x=20, y=240)
        self.button5.place(x=30,y=310)

    # opening the game windown and drawing the broad
    def runGame(self,mode):
        a = ChessInterface(mode)
        a.draw()


    def runTk(self):
        self.wnd.mainloop()

class ChessInterface(Chess):
    def __init__(self,mode):
        Chess.__init__(self)
        self.mode = mode
        self.unit = 60
        self.height = self.unit*8
        self.width = self.unit*8
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
        self.gameWnd = Toplevel()
        self.gameWnd.geometry('490x510')
        self.canvas = Canvas(self.gameWnd, height=self.height, width=self.width)
        self.canvas.bind('<Button-1>', self.mousepress)
        #self.button = Button(self.gameWnd, text='redo', command=self.redo)
        self.canvas.pack()
        #self.button.pack()
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
                    self.tags[(i,j)] = (self.canvas.create_rectangle(i*self.unit,
                                                                     j*self.unit,
                                                                     i*self.unit+self.unit,
                                                                     j*self.unit+self.unit,
                                                                     fill='grey'),'grey')
                else:
                    self.tags[(i,j)] = (self.canvas.create_rectangle(i * self.unit,
                                                                     j * self.unit,
                                                                     i * self.unit + self.unit,
                                                                     j * self.unit + self.unit,
                                                                     fill= LIGHTCOLOR), LIGHTCOLOR)
                self.textTags[(i,j)] = self.canvas.create_text(i * self.unit + self.unit // 2,
                                                               j * self.unit + self.unit // 2,
                                                               text=self.pieces[self.board[j][i]],
                                                               font=('DejaVu Sans', self.unit // 2))

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

    # this AI only either makes a random move or eats the strongest possible piece if possible
    def mediumAI(self):
        maxValue = 0
        bestPiece = ()
        for i in range(8):
            for j in range(8):
                if self.board[i][j][0] == self.player and self.board[i][j][0] != '_':

                    self.x1 = j
                    self.y1 = i
                    self.piece = self.board[i][j]
                    self.color = self.board[i][j][0]
                    if self.possibleMoves() != []:
                        for move in self.possibleMoves():
                            if self.pieceValue(self.board[int(move[1])][int(move[0])][1]) > maxValue:
                                bestPiece = (self.x1,self.y1)
                                self.x2 = int(move[0])
                                self.y2 = int(move[1])
                                maxValue = self.pieceValue(self.board[int(move[1])][int(move[0])][1])

        if maxValue == 0:
            self.dumbAI()
        else:
            self.x1 = bestPiece[0]
            self.y1 = bestPiece[1]
            self.piece = self.board[self.y1][self.x1]
            self.color = self.board[self.y1][self.x1][0]
            self.movePiece()
            self.updatePieces((self.x1,self.y1),(self.x2,self.y2))
            if self.done() == True:
                if self.player == 'b':
                    messagebox.showinfo('Result', 'Black wins!!')
                else:
                    messagebox.showinfo('Resutl', 'White wins!!')
            self.changePlayer()

    # AI that uses the minimax algorithm
    def strongAI(self):
        bestMove = self.minimax(3,True,'b')
        self.x1 = bestMove[0][0][0]
        self.y1 = bestMove[0][0][1]
        self.piece = self.board[self.y1][self.x1]
        self.color = self.board[self.y1][self.x1][0]
        self.x2 = bestMove[0][1][0]
        self.y2 = bestMove[0][1][1]
        self.movePiece()
        self.updatePieces((self.x1, self.y1), (self.x2, self.y2))
        if self.done() == True:
            if self.player == 'b':
                messagebox.showinfo('Result', 'Black wins!!')
            else:
                messagebox.showinfo('Result', 'White wins!!')
            self.gameWnd.destroy()
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


        else:
            # making sure that the user doesnt choose to move an opponents piece
            if (self.board[y][x][0] == self.player and len(self.clicks) == 0) or len(self.clicks) == 1:
                self.selected = (x, y)
                self.clicks.append(self.selected)

    def partOfAntiMain(self, x, y):
        # dehighlight the highlighted squares
        if len(self.clicks) == 1:
            a = self.x1
            b = self.y1
            self.x2 = x
            self.y2 = y
            piece = self.piece
            color = self.color
            if not self.checkmoves() or not self.checkAntiMoves() :
                self.change(a,b,self.x2,self.y2,color,piece)
                for i in self.possibleMoves():
                    self.canvas.itemconfig(self.tags[(int(i[0]), int(i[1]))][0],
                                           fill=self.tags[(int(i[0]), int(i[1]))][1])
            self.change(a,b,x,y,color,piece)
        # user can deselect the piece if he clicks twice
        if self.selected == (x, y):
            self.selected = ()
            self.clicks = []
            # making the square turn back to original color if it was deselected
            self.canvas.itemconfig(self.tags[(x, y)][0], fill=self.tags[(x, y)][1])


        else:
            # making sure that the user doesnt choose to move an opponents piece
            if (self.board[y][x][0] == self.player and len(self.clicks) == 0) or len(self.clicks) == 1:
                self.selected = (x, y)
                self.change(x,y,self.x2,self.y2,self.board[y][x][0],self.board[y][x])
                print(self.selected)
                self.clicks.append(self.selected)

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

    def antiHighlight(self,x,y):
        if self.clicks != []:
            # highlight square to show where player clicked
            # if player clicks an empty square or one not containing his pieces, dont highlight
            print('self.x1,self.y1,self.x2,self.y2',self.x1,self.y1,self.x2,self.y2)
            print('player: ',self.player)
            print('color: ',self.color)
            print('piece: ',self.piece)
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
            piece = self.piece = self.board[self.y1][self.x1]
            color = self.color = self.board[self.y1][self.x1][0]
            for i in self.antiChessMoves():
                self.change(x, y, self.x2, self.y2, color, piece)
                if [(self.x1,self.y1),(i[1][0],i[1][1])] == i:
                    print(self.possibleMoves())
                    self.canvas.itemconfig(self.tags[(i[1][0], i[1][1])][0], fill='light blue')
            return
    # function that runs the full game based on the event given to it
    def mousepress(self,event):
        if self.mode != 1 and self.mode!= 5:
            if self.player == 'b':
                return
        # calculate which square the user clicks on
        x = event.x//self.unit
        y = event.y//self.unit

        if self.mode != 5:
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
                    # announce winner when game ends
                    if self.done() == True:
                        if self.player == 'b':
                            messagebox.showinfo('Result', 'Black wins!!')
                        else:
                            messagebox.showinfo('Resutl','White wins!!')
                        self.gameWnd.destroy()
                    self.printB()
                    self.changePlayer()
                    if self.mode == 1:
                        print('player vs player')
                    elif self.mode == 2:
                        self.canvas.after(1000,self.dumbAI)
                    elif self.mode == 3:
                        self.canvas.after(1000,self.mediumAI)
                    elif self.mode == 4:
                        self.canvas.after(10,self.strongAI)

                else:
                    self.canvas.itemconfig(self.tags[self.clicks[0]][0], fill= self.tags[self.clicks[0]][1])
                    self.canvas.itemconfig(self.tags[self.clicks[0]][1], fill= self.tags[self.clicks[0]][1])
                self.clicks = []
                self.selected = ()
        else:
            self.partOfAntiMain(x,y)
            self.antiHighlight(x,y)

            a = self.x1
            b = self.y1
            c = self.x2
            d = self.y2
            print(a,b,c,d)
            piece = self.board[self.y1][self.x1]
            color = piece[0]
            if len(self.clicks) == 2:
                print('self.clicks: ',self.clicks)
                self.changeInfo(self.clicks)
                if self.player == self.color and self.checkmoves() != False and [(self.x1,self.y1),(self.x2,self.y2)] in self.antiChessMoves():
                    # dehighlight the previously highlighted squares
                    piece = self.board[self.clicks[0][1]][self.clicks[0][0]]
                    color = piece[0]
                    self.change(self.clicks[0][0],self.clicks[0][1],self.clicks[1][0],self.clicks[1][1],color,piece)
                    print(self.x1,self.y1,self.x2,self.y2)

                    for i in self.possibleMoves():
                        self.canvas.itemconfig(self.tags[(int(i[0]), int(i[1]))][0],
                                               fill=self.tags[(int(i[0]), int(i[1]))][1])
                    self.canvas.itemconfig(self.tags[(self.clicks[0][0], self.clicks[0][1])][0]
                                           , fill=self.tags[(self.clicks[0][0], self.clicks[0][1])][1])
                    self.movePiece()
                    self.updatePieces(self.clicks[0], self.clicks[1])
                    # announce winner when game ends
                    if self.antiDone() == True:
                        if self.player == 'b':
                            messagebox.showinfo('Result', 'White wins!!')
                        else:
                            messagebox.showinfo('Resutl', 'Black wins!!')
                        self.gameWnd.destroy()
                    self.printB()
                    self.changePlayer()

                else:
                    self.canvas.itemconfig(self.tags[self.clicks[0]][0], fill=self.tags[self.clicks[0]][1])
                    self.canvas.itemconfig(self.tags[self.clicks[0]][1], fill=self.tags[self.clicks[0]][1])
                self.clicks = []
                self.selected = ()

a = mainMenu()
a.runTk()