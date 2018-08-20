

import sys

class Sudoku:
    __slots__ = {'_tiles'}
    def __init__(self):
        self._tiles = [[]]
    def addRow(self):
        self._tiles.append([])
    def addTiles(self,i, x):
        self._tiles[i].append(x)
    def setTile (self,x,y,value):
        self._tiles[x][y] = value
    def getTile (self,x,y):
        return self._tiles[x][y]

def readPuzzle(input_file):     
    f = open(input_file, 'r')    
    puzzle_list = []
    for line in f:
        x = Sudoku()
        for i in range(9):
            x.addRow()
            for j in range(9):
                tile = f.read(1)
                #convert tiles into integers
                if tile != '.' and tile !='\x1a' and tile !='\n' and tile !='':
                    tile = int(tile)
                x.addTiles(i,tile)
        puzzle_list.append(x)
    f.flush( )
    f.close( )
    return puzzle_list

def writePuzzle(x, input_file):
    output_file = input_file[:-4] + '-solved.txt'
    f = open(output_file, 'w')
    for puzzle in x: 
        for x in range(9):
            for y in range(9):
                k = puzzle.getTile(x,y)
                k = str(k)
                f.write(k)
        f.write('\n')
    f.flush( )
    f.close( )

def findBlankTile(puzzle, row, col):
    for x in range(row,9):
        for y in range(col,9):
            if puzzle.getTile(x,y) == '.':
                return x,y
    for x in range(9):
        for y in range(9):
            if puzzle.getTile(x,y) == '.':
                return x,y
    return 'complete', 'complete'

def checkRow(puzzle,row,test_num):
    for y in range(9):
        if test_num == puzzle.getTile(row,y):
            return False
    return True    

def checkCol(puzzle,col,test_num):
    for x in range(9):
        if test_num == puzzle.getTile(x,col):
            return False
    return True    

def checkSubboards(puzzle,row,col,test_num):
    subboard_row = 3*(row//3)
    subboard_column = 3*(col//3)
    for x in range(subboard_row, subboard_row+3):
        for y in range(subboard_column, subboard_column+3):
            if puzzle.getTile(x,y) == test_num:
                return False
    return True

def solvePuzzle(puzzle, row=0, col=0):
    row,col = findBlankTile(puzzle, row, col)
    #ends function call if there are no more "blank tiles"
    if row == 'complete' or col == 'complete':
        return True
    #guess number and see if it is valid with row, column and subboard
    for test_num in range(1,10):
        if checkRow(puzzle,row,test_num) and checkCol(puzzle,col,test_num) and checkSubboards(puzzle,row,col,test_num):
            puzzle.setTile(row,col,test_num)
            #recursively call this function until there are no more blank tiles
            if solvePuzzle(puzzle, row, col):
                return True
            #rolls back if guess doesnt not work
            puzzle.setTile(row,col, '.')
    return False

def main():
    
    #read puzzle(s) from file
    puzzles = readPuzzle(sys.argv[1]) 

    #cycles through and solves list of puzzles
    for i in puzzles:
        solvePuzzle(i):


    #write solved puzzle(s) to file
    writePuzzle(puzzles,sys.argv[1])

if __name__== "__main__":
    main()

