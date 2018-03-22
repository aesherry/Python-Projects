#
# hw9pr1.py
#
# Name: Ava Sherry
# Date: 10/31/17
# Problem Lab 9: The Game of Life


import random
from copy import deepcopy

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [ createOneRow(width)]        
    return A



def printBoard(A):
    """ this function prints the 2d list-of-lists A
    """
    for row in A:               
        for col in row:         # col is the individual element
            print(col,end='')
        print()                 


def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
        but, only in the * interior * of the 2d array
    """
    A = createBoard(width, height)

    for row in range(1,height-1):
        for col in range(1,width-1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A
    

def innerCells(w,h):
    """ returns a 2d array that has all live 
    cells—with the value of 1—except for a 
    one-cell-wide border of empty cells (with 
    the value of 0) around the edge of the 2d 
    array.
    """
    A = createBoard(w, h)

    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = 1
    return A



def randomCells(w,h):
    """ which returns an array of randomly-assigned 
    1's and 0's except that the outer edge of the 
    array is still completely empty (all 0's) as 
    in the case of innerCells
    """
    A = createBoard(w, h)

    for row in range(1,h-1):
        for col in range(1,w-1):
            rand= random.randrange(0,2)
            A[row][col] = rand
    return A



def copy(A):
    """ returns a DEEP copy of the 2d array A """
    height = len(A)
    width = len(A[0])
    newA = createBoard( width, height )

    for row in range(1,height-1):
        for col in range(1,width-1):
            newA[row][col] = A[row][col]
    return newA


def innerReverse(A):
    """ takes an old 2d array A (an old "generation") 
    and then creates a new generation newA of the
    same shape and size. The new generation should 
    be the "opposite" of A's cells everywhere 
    except on the outer edge
    """
    newA= copy(A)
    height = len(A)
    width = len(A[0])

    for row in range(1,height-1):
        for col in range(1,width-1):
            if A[row][col] == 1:
                newA[row][col]= 0
            else:
                newA[row][col] = 1 
    return newA



def countNeighbors(row, col, A):
    """ return the number of live neighbors 
    for a cell in the board A at a particular 
    row and col
    """
    sum = 0
    if A[row+1][col] == 1:
        sum+=1
    if A[row-1][col] == 1:
        sum +=1
    if A[row][col+1] == 1:
        sum +=1 
    if A[row][col-1] == 1:
        sum +=1
    if A[row+1][col+1] == 1:
        sum +=1 
    if A[row+1][col-1] == 1:
        sum +=1 
    if A[row-1][col-1] == 1:
        sum +=1 
    if A[row-1][col+1] == 1:
        sum +=1 
    return sum



def next_life_generation(A):
    """ makes a copy of A and then advances one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays at 0.
    """
    newA= copy(A)
    height = len(A)
    width = len(A[0])

    for row in range(1,height-1):
        for col in range(1,width-1):
            if A[row][col] == 1:
                if countNeighbors(row,col,A) > 3:
                    newA[row][col]= 0
                if countNeighbors(row,col,A) < 2:
                    newA[row][col]= 0
            else:
                if countNeighbors(row,col,A) == 3:
                    newA[row][col]= 1
    return newA



