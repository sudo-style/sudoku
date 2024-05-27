import numpy as np

class Sudoku:
    def __init__(self):
        # needs to pull this from a generator
        self.startBoard = np.array([[0,0,4,5,0,9,0,1,0],
                                 [0,0,9,0,4,0,0,5,0],
                                 [6,8,0,1,0,3,0,0,9],
                                 [0,0,0,0,7,0,0,0,0],
                                 [0,4,0,0,5,1,0,6,0],
                                 [0,0,7,0,3,8,5,0,0],
                                 [0,0,0,0,0,0,0,8,0],
                                 [0,0,0,3,9,4,2,7,0],
                                 [9,2,6,8,0,0,0,0,0]])
        self.board = np.copy(self.startBoard)

        self.canidates = {}
        self.mode = 'fill'

        self.gameLoop()
        

    def addCanidate(self):
        self.tapRowCol()
        self.tapValue()

    # tap notes
    def modeCanidate(self):
        
        #if self.mode == 'canidate':
        if (self.mode == 'fill'):
            self.mode = 'canidate'
        else:
            self.mode = 'fill'

        print("mode is now " + self.mode)
    # undo
    def tapUndo(self):
        pass

    def tapHold(self):
        self.mode = "hold"

    def tapErase(self):
        self.mode = "erase"

    def printBoard(self):
        print("board")
        print(self.board)
        print()

    def tapRowCol(self):
        self.row = int(input("row: "))
        self.col = int(input("col: "))

    def restart(self):
        print("restarted")
        self.board = np.copy(self.startBoard)

    def tapValue(self):
        value = int(input("value"))
        self.value = value
        

        row = self.row
        col = self.col
        # check if the value is zero on start board
        
        if (self.startBoard[row][col] != 0):
            print("can\'t change starting ")
        elif(self.mode == 'canidate'):
            self.toggleCanidate()
        else:
            # remove the canidates
            key = (row,col)
            value = self.value
            dictionary = self.canidates
            dictionary[key] = []

            # fill the board
            self.board[row][col] = value
        
    def toggleCanidate(self):
        row = self.row
        col = self.col

        key = (row,col)
        value = self.value
        dictionary = self.canidates
        
        # board is cleared
        self.board[row][col] = 0

        if key not in dictionary:
            dictionary[key] = [value]
        elif key in dictionary and value in dictionary[key]:
            dictionary[key].remove(value)
        else:
            dictionary[key].append(value)

        print(dictionary)

        # check if row col value is in in the canidates
        # if it is remove it
        # otherwise add it
        
    

    def gameLoop(self):
        while True:
            self.printBoard()
            i = input("(e)rase, (f)ill, (h)ighlight (b)reak (r)estart (c)anidate: ")

            if (i == 'b'):
                break

            if (i == 'e'): 
                self.tapErase()
                continue
            
            if (i == 'f'):
                self.tapRowCol()
                self.tapValue()
                continue
            
            if (i == 'h'):
                self.tapRowCol()
                self.highlightValues()
                # self.get_cell_info()
                continue

            if (i == 'r'):
                self.restart()
                continue
            
            if (i == 'c'):
                self.modeCanidate()
                continue
                
        
    
    def get_cell_info(self):
        row = self.row
        col = self.col

        # Calculate the indices for the starting row and column of the cell
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        
        # Generate row indices for the cell
        row_indices = [(start_row, i) for i in range(start_col, start_col+9)]
        
        # Generate column indices for the cell
        col_indices = [(i, start_col) for i in range(start_row, start_row+9)]
        
        # Generate cell indices
        cell_indices = [(i, j) for i in range(start_row, start_row+3) for j in range(start_col, start_col+3)]
        
        print(row_indices)
        print(col_indices)
        print(cell_indices)




    def highlightValues(self):
        row = self.row
        col = self.col
        # left to right
        print("left to right")
        print(self.board[row])

        # up and down
        print("up and down")        
        print(self.board[:, col])
        

        # what cell
        print("cell")

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        
        # Extract the values from the cell
        cell_values = self.board[start_row:start_row+3, start_col:start_col+3]
        
        print("Cell values:")
        print(cell_values)
        # change the row,col to be in the same spot 
        
        

        






sudoku = Sudoku()
sudoku.printBoard()

    
