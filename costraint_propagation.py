import copy
from utils import checkCostraints, getAllDomains, getNextMinimumDomain, DIMENSION

# backtracking and costraint propagation with most costrained variable (cell with the fewest possible values)

def solve_cp(board, back):
    domains = getAllDomains(board)
    cell = getNextMinimumDomain(domains, board)
    if cell is None:
        return (True, board, back)
    row, col = cell
    for val in domains[row * DIMENSION + col]:
        if checkCostraints(val, row, col, copy.deepcopy(board)):
            board[row][col] = val
            solved, bo, backpropagation = solve_cp(board, back)
            if solved:
                return (True, bo, back + backpropagation)
        board[row][col] = 0
        back += 1
    return (False, board, back)