# Useful constant
DIMENSION = 9
FREECELLVALUE = 0


# Function to check the correctness of the final solution of Relaxation Labelling Technique
def checkSolution(board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            if(notValidRow(row, board[row][col], board) or
                notValidCol(col, board[row][col], board) or
                notValidBox(row, col, board[row][col], board)):
                return False
    return True

def notValidRow(row, value, board):
    c = 0
    for col in range(DIMENSION):
        if board[row][col] == value:
            c+=1
            if c > 1: return True
    return False

def notValidCol(col, value, board):
    c = 0
    for row in range(DIMENSION):
        if board[row][col] == value:
            c+=1
            if c > 1: return True
    return False

def notValidBox(row, col, value, board):
    f = 0
    for r in range((row // 3) * 3, (row // 3) * 3 + 3):
        for c in range((col // 3) * 3, (col // 3) * 3 + 3):
            if board[r][c] == value:
                f+=1
                if f > 1: return True
    return False


# FUnction to retreive the possible values domain of each cells
def getDomainCells(bo):
        newDomain = []
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                if bo[row][col] != FREECELLVALUE: newDomain.append([bo[row][col]])
                else: newDomain.append(getDomain(row,col, bo))
        return newDomain
    
    
# Function to get the list of possible values domain for a specific cell
def getDomain(row, col, board):
        domain = [int(i) for i in range(1, DIMENSION + 1)]
        domainRow(row, domain, board)
        domainCol(col, domain, board)
        domainBox(row, col, domain, board)
        return domain
    
def domainRow(row, domain, board):
    for c in range(DIMENSION):
        if board[row][c] in domain: domain.remove(board[row][c])
        
def domainCol(col, domain, board):
    for row in range(DIMENSION):
        if board[row][col] in domain: domain.remove(board[row][col])

def domainBox(row, col, domain, board):
    for r in range(int(row/3)*3, int(row/3)*3+3):
        for c in range(int(col/3)*3, int(col/3)*3+3):
                if board[r][c] in domain: domain.remove(board[r][c])


# Function to print the sudoku board
def print_board(mat):
    for i in range(len(mat)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(mat[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(str(mat[i][j]))
            else:
                print(str(mat[i][j]) + " ", end="")


# Function to read the sudoku board using its path file
def readFile(filename):
    board = []
    with open(filename) as f:
        text = f.readlines()
        board = [list(map(int, x.strip())) for x in text]
    return board


# Function to store the final sudoku board
def writeFile(technique, filename, board):
    f = open(f"./results/{technique}/{filename}", "w+")
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j == 8:
                f.write(str(board[i][j]) + "\n")
            else:
                f.write(str(board[i][j]))