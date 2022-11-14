from utils import checkCostraints, getAllDomains, getNextMinimumDomain, printBoard, createBoard

# backtracking and costraint propagation with most costrained variable (cell with the fewest possible values)

def solve_cp(board):
    if getMostCostrainedCell(allDomains):
        row, col, dom, idx = getMostCostrainedCell(allDomains)
        if dom == []:
            return True
        for val in dom:
            if checkCostraints(val, row, col, board):
                board[row][col] = val  
                if solve_cp(board, getAllDomains(board)):
                    return True
                else:
                    new_domains = getAllDomains(board)
                    board[row][col] = 0
                    return(solve_cp(board, new_domains))
            else:
                # print("Provato con ", val)
                # board[row][col] = 0
                domains = getAllDomains(board)
                domains[idx] = domains[idx].remove(val)
                # print("Nuovi domains dopo aver eliminato val", domains)
                return(solve_cp(board, domains))
        return False
    else:
        return True

board = createBoard("./boards/medium/medium3.txt")

if solve_cp(board, getAllDomains(board)):
    printBoard(board)
else:
    print("SUDOKU NON RISOLTO")