## Name: Ava Sherry
## Date: 11/10/17
## Problem 2: Connect Four - The Board Class
import random


class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s+= '\n'
        for i in range(W):
            s += ' '+ str(i)  # and the numbers underneath here
        
        return s       # the board is complete, return it


    def addMove(self, col, ox):
        """ adds a checker to specified column """
        H = self.height
        for row in range(H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return 
        
        self.data[H-1][col] = ox
    

    def clear(self):
        """ clears the board """
        H = self.height
        W = self.width
        for row in range(0,H):
            for col in range(0,W):
                self.data[row][col] = ' '
        return 
    

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'


    def allowsMove(self, col):
        """ return True if the calling object (of type 
        Board) does allow a move into column c. It returns 
        False if column c is not a legal column number for 
        the calling object. It also returns False if column 
        c is full.
        """
        H = self.height
        W = self.width
        D = self.data

        if col < 0 or col >= W:
            return False 
        elif D[0][col] != ' ':
            return False
        else:
            return True
    

    def isFull(self):
        """ return True if the calling object 
        (of type Board) is completely full of checkers
        """
        H = self.height
        W = self.width
        D = self.data

        count = 0
        for col in range(W):
            if D[0][col] != ' ':
                count += 1
        if count == W:
            return True 
        else:
            return False
    

    def delMove(self, col): 
        """ It should remove the top checker from the column 
        c. If the column is empty, then delMove should do 
        nothing.
        """
        H = self.height
        for row in range(H):
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                return 

    def winsFor(self, ox):
        """  True if there are four checkers of type ox 
        in a row on the board. It should return False 
        othwerwise.
        """
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row][col+1] == ox and \
                   D[row][col+2] == ox and \
                   D[row][col+3] == ox:
                    return True
        
        # check for vertical wins
        for row in range(0,H-3):
            for col in range(0,W):
                if D[row][col] == ox and \
                   D[row+1][col] == ox and \
                   D[row+2][col] == ox and \
                   D[row+3][col] == ox:
                    return True
        
        # check for diagonal wins (south east)
        for row in range(0,H-3):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row+1][col+1] == ox and \
                   D[row+2][col+2] == ox and \
                   D[row+3][col+3] == ox:
                    return True
        
        # check for diagonal wins (northeast)
        for row in range(3,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row-1][col+1] == ox and \
                   D[row-2][col+2] == ox and \
                   D[row-3][col+3] == ox:
                    return True
        
        else:
            return False
    
    def colsToWin (self, ox):
        """ input: ox, which will be either the string 
        'X' or the string 'O'. 
        output: the list of columns where ox can move 
        in the next turn in order to win and finish 
        the game
        """
        W = self.width
        L = []
        for col in range(W):
            if self.allowsMove(col) == True:
                self.addMove(col, ox)
                if self.winsFor(ox) == True:
                    L += [col]
                self.delMove(col)
        return L


    def aiMove(self,ox):
        """ input: string 'X' or the string 'O'
        output: single integer, which must be a legal 
        column in which to make a move
        """
        import random
        W = self.width
        L = self.colsToWin(ox)
        if ox == 'O':
            if L != []:
                r=random.randrange(len(L))
                return int(L[r])
            elif self.colsToWin('X') != []:
                r=random.randrange(len(self.colsToWin('X')))
                return int(self.colsToWin('X')[r])
            else:
                r=random.randrange(W)
                return r
        else:
            if L != []:
                r=random.randrange(len(L))
                return int(L[r])
            elif self.colsToWin('O') != []:
                r=random.randrange(len(self.colsToWin('O')))
                return int(self.colsToWin('O')[r])
            else:
                r=random.randrange(W)
                return r


    def playGame(self, px, po):
        """ plays a game either Computer vs Computer
        or Human va Computer"""
        print("Welcome to Connect Four!")
 
        user = input("Choose (Human vs po) or (px vs po)? ")
        while True:
            if user == "px vs po":
                px_col = px.nextMove(self)
                self.addMove (px_col,'X')

                if self.winsFor('X') == True:
                    print()
                    print("Computer X Wins!")
                    print(self)
                    break

                po_col = po.nextMove(self)
                self.addMove(po_col,'O')

                if self.winsFor('O') == True:
                    print()
                    print("Computer O Wins!")
                    print(self)
                    break
        
                if self.isFull() == True:
                    print()
                    print("Tie Game")
                    print(self)
                    break

                print()
                print("Computer X Chooses: Col", px_col)
                print("Computer O Chooses: Col",po_col)
                print(self)
                

            if user == "Human vs po":
                users_col = int(input( "Choose a column: " ))

                if users_col == -1:
                    break

                while self.allowsMove(users_col) == False:
                    users_col = input("Choose a column: ")
                
                self.addMove (users_col,'X')

                if self.winsFor('X') == True:
                    print()
                    print("Human Wins!")
                    print(self)
                    break

                po_col = po.nextMove(self)
                self.addMove(po_col,'O')

                if self.winsFor('O') == True:
                    print()
                    print("Computer Wins!")
                    print(self)
                    break
        
                if self.isFull() == True:
                    print()
                    print("Tie Game")
                    print(self)
                    break

                print()
                print("Human Chooses: Col", users_col)
                print("Computer Chooses: Col",po_col)
                print(self)


            
class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply


    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s       


    def oppCh(self):
        """ return the other kind of checker or playing 
        piece """
        if self.ox=='O':
            return 'X'
        else :
            return 'O'
    

    def scoreBoard(self,b):
        """ return a single float value representing the 
        score of the input b, which you may assume will be 
        an object of type Board. This should return 100.0 
        if the board b is a win for self. It should return 
        50.0 if it is neither a win nor a loss for self, 
        and it should return 0.0 if it is a loss for self
        """
        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppCh()):
            return 0.0
        else:
            return 50.0


    def tiebreakMove(self,scores):
        """ in scores, which will be a nonempty list of 
        floating-point numbers. If there is only one 
        highest score in that scores list, this method 
        should return its COLUMN number, not the actual 
        score
        """

        W = []
        for i in list(range(len(scores))):
            if scores[i] == max(scores):
                W += [i]

        if W == []:
            if self.tbt=='LEFT':
                return 0
            elif self.tbt == 'RIGHT':
                return 6
            elif self.tbt=='RANDOM':
                r = int(random.randrange(7))
                return r
        elif len(W) == 1:
            return W[0]
        else: 
            if self.tbt=='LEFT':
                return W[0]
            elif self.tbt == 'RIGHT':
                return W[-1]
            elif self.tbt=='RANDOM':
                r = random.randrange(0,len(W)-1)
                return W[r]
    
        
        

    

    def scoresFor(self,b):
        """scoresFor returns a list of scores
        """
        opp = self.oppCh()
        scores = [50]*b.width
        for col in range(b.width):
            if b.winsFor(self.ox) == True:
                scores[col] = 100.0
            elif b.winsFor(self.oppCh()) == True:
                scores[col] = 0.0
            elif b.allowsMove(col) == False:
                scores[col] = -1.0
            elif self.ply == 0:
                scores[col] = self.scoreBoard(b)
            else:
                b.addMove(col,self.ox)
                opp = Player(self.oppCh(),self.tbt,self.ply-1)
                s = opp.scoresFor(b)
                scores[col] = (100 - max(s))
                b.delMove(col)
        return scores
    
    def nextMove(self,b):
        """ b, an object of type Board and returns an integer 
        -- namely, the column number that the calling object 
        (of class Player) chooses to move to"""

        scores = self.scoresFor(b)
        move = self.tiebreakMove(scores)
        return move

    
    
