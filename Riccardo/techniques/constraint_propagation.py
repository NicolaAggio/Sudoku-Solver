# Useful import
import copy
from .utils import DIMENSION, getDomainCells


# We define the value for the empty domain value
EMPTYDOMAINVALUE = 10


# Function to get the lenght of a specific list domain 
def getLenghtDomain(domain, cellValue):
    if(len(domain) == 1 and domain[0] == cellValue): return EMPTYDOMAINVALUE
    else: return len(domain.remove(cellValue)) if cellValue != 0 else len(domain)


# Function to get the list of doamin length of each cell 
def getListMapDoamin(domain, bo):
    map = []
    for row in range(DIMENSION):
        map.extend(
            getLenghtDomain(domain[row * DIMENSION + col], bo[row][col])
            for col in range(DIMENSION))
    return map


# Function to get the position of the cell with the minimum length domain 
def getNextMinimumDomain(domain, bo):
    listMapDomain = getListMapDoamin(domain, bo)
    minimumFirstList = min(listMapDomain)
    if minimumFirstList == EMPTYDOMAINVALUE: return None
    index = listMapDomain.index(minimumFirstList)
    return(int(index / DIMENSION), index % DIMENSION)
    

# Function to verify if the actual assign produce an empty domain
def checkValidAssign(bo, row, col, val):
    bo[row][col] = val
    return [] not in getDomainCells(bo)
    

# Main function to solve the sudoku board using Constraint Propagation and Back Tracking
def solveConstraintPropagation(bo, exp, back):
    domain = getDomainCells(bo)    
    location = getNextMinimumDomain(domain, bo)
    if(location is None): return (True, bo, exp, back)
    row, col = location
    for val in domain[row * DIMENSION + col]:
        if checkValidAssign(copy.deepcopy(bo), row, col, val):            
            bo[row][col] = val
            solved, board, expanded, backword = solveConstraintPropagation(bo, exp+1, back)
            if(solved): return (True, board, exp + expanded, back + backword)
        back += 1
        bo[row][col] = 0
    return (False, bo, exp, back)