# CONSTANT VALUES

DIMENSION = 9
EMPTY_VALUE = 0

## --- FUNCTIONS ---

# intersection of two lists
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# given a .txt file, create the matrix
def createBoard(file):
    board = []
    f = open(file, "r")
    text = f.readlines()
    for row in text:
        board.append(list(map(int, row.replace('\n',''))))
    f.close()
    return board

# given the name of the algorithm, the file name and the board, writes the board in a new .txt file in the results/technique folder
def writeBoard(technique, filename, board):
    f = open(f"./results/{technique}/{filename}", "w+")
    for row in board:
        f.write(str(row).replace('[', '').replace(']','').replace(', ', '') + '\n')
    f.close()

# printing the matrix
def printBoard(board):
    for row in board:
        print(str(row).replace('[', '').replace(']','').replace(', ', ''))



## --- COSTRAINTS ---

# counts the number of occurrences of a value in a row: if the count >= 1, then the value cannot be inserted in the row; otherwise it can.
def checkRow(value, row, board):
    count = 0
    for col in range(0, DIMENSION):
        if board[row][col] == value:
            count += 1
    if count >= 1:
        return False
    return True

# counts the number of occurrences of a value in a column: if the count >= 1, then the value cannot be inserted in the column; otherwise it can.
def checkColumn(value, col, board):
    count = 0
    for row in range(0, DIMENSION):
        if board[row][col] == value:
            count += 1
    if count >= 1:
        return False
    return True

# counts the number of occurrences of a value in a box: if the count >= 1, then the value cannot be inserted in the box; otherwise it can.
def checkBox(value, row, col, board):
    count = 0
    for i in range((row//3) * 3, (row//3) * 3 + 3):
        for j in range((col//3) * 3, (col//3) * 3 + 3):
            if board[i][j] == value:
                count += 1
    if count >= 1:
        return False
    return True

# check if a value in a given position can be inserted in the board, according to the costraints of the game
def checkCostraints(val, row, col, board):
    if not checkRow(val, row, board) or not checkColumn(val, col, board) or not checkBox(val, row, col, board):
        return False
    return True

# check if the solution is completed and if it is corrected.. 
# def checkSolution(board):
#     for row in range(DIMENSION):
#         for col in range(DIMENSION):
#             if board[row][col] == 0 or not checkCostraints(board[row][col], row, col, board):
#                 return False
#     return True


## --- DOMAINS ---

# given a row, returns the list of possible values that can be inserted
def getRowDomain(row, board):
    domain = [int(x) for x in range(1, DIMENSION + 1)]
    for col in range(0, DIMENSION):
        val = board[row][col]
        if val in domain:
            domain.remove(val)
    return domain

# given a column, returns the list of possible values that can be inserted
def getColDomain(col, board):
    domain = [int(x) for x in range(1, DIMENSION + 1)]
    for row in range(0, DIMENSION):
        val = board[row][col]
        if val in domain:
            domain.remove(val)
    return domain

# given a box, returns the list of possible values that can be inserted
def getBoxDomain(row, col, board):
    domain = [int(x) for x in range(1, DIMENSION + 1)]
    for i in range((row//3) * 3, (row//3) * 3 + 3):
        for j in range((col//3) * 3, (col//3) * 3 + 3):
            val = board[i][j]
            if val in domain:
                domain.remove(val)
    return domain

# given a position in the board, returns the list of possible values that can be inserted
def getDomainCell(row, col, board):
    l1 = getRowDomain(row, board)
    l2 = getColDomain(col, board)
    l3 = getBoxDomain(row, col, board)
    return intersection(intersection(l1, l2), l3)

# given a board, returns the list of all the possible values that each position can take. The domain of a non-empty cell is the value of the cell
def getAllDomains(board):
    domains = []
    for row in range(0, DIMENSION):
        for col in range(0, DIMENSION):
            if board[row][col] == EMPTY_VALUE:
                domains.append(getDomainCell(row, col, board))
            else:
                domains.append([board[row][col]])
    return domains

# given a domain of a cell and the value of the cell, the function returns the number of possible values that the cell can take
def getLenDomain(domain, cellValue):
    if (len(domain) == 1 and domain[0] == cellValue): 
        return 10
    else:
        if cellValue != 0:
            return len(domain.remove(cellValue)) 
        else:
            return len(domain)

# gets the list of the length of the domain of each cell 
def getListMapDoamin(domain, board):
    map = []
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            map.append(getLenDomain(domain[row * DIMENSION + col], board[row][col]))
    return map

# Function to get the position of the cell with the minimum length domain 
def getNextMinimumDomain(domain, bo):
    listMapDomain = getListMapDoamin(domain, bo)
    minimumFirstList = min(listMapDomain)
    if minimumFirstList == 10 : return None
    index = listMapDomain.index(minimumFirstList)
    return(int(index / DIMENSION), index % DIMENSION)

def getMostCostrainedCell(allDomains):
    if allDomains != []:
        min_len = -1
        idx = 0
        ret_dom = []
        return_idx = -1
        row = -1
        col = -1

        for domain in allDomains:
            if domain != []:
                min_len = len(domain)
                ret_dom = domain
                return_idx = idx
            idx += 1
    
        idx = 0

        for domain in allDomains:
            if domain != []:
                if len(domain) < min_len:
                    min_len = len(domain)
                    return_idx = idx
                    ret_dom = domain
            idx += 1
        if return_idx != -1:
            row = return_idx // 9
            col = return_idx % 9
        return row, col, ret_dom, return_idx

# board = createBoard("./boards/easy/prova.txt")
# # print(getAllDomains(board))
# row, col, dom = getMostCostrainedCell(getAllDomains(board))
# print("RIGA = ",row)
# print("COLONNA = ",col)
# print("POSSIBILI VALORI = ", dom)
