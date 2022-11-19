from utils import DIMENSION, createBoard, generateRandomStates, printBoard, numberOfDuplicates, generateNewRandomState, checkSolution
import statistics, copy, random, math
# import sys, threading
# sys.setrecursionlimit(100000000)
# threading.stack_size(2**27)

def costFunctionRow(board):
    cost = 0
    for row in range(0, DIMENSION):
        l = []
        for col in range(0, DIMENSION):
            l.append(board[row][col])
        cost += len(numberOfDuplicates(l))
    return cost

def costFunctionCol(board):
    cost = 0
    for col in range(0, DIMENSION):
        l = []
        for row in range(0, DIMENSION):
            l.append(board[row][col])
        cost += len(numberOfDuplicates(l))
    return cost

def costFunction(board):
    return costFunctionRow(board) + costFunctionCol(board)

def initialTemp(board, posList):
    listOfDifferences = []
    for i in range(0,20):
        new = generateNewRandomState(board, posList)
        if new is not None:
            listOfDifferences.append(costFunction(new))
    return statistics.pstdev(listOfDifferences)

def numberOfIterations(board):
    count = 0
    for row in range(0, DIMENSION):
        for col in range(0, DIMENSION):
            if board[row][col] == 0:
                count += 1
    return count^2

def solve_sa(board):
    coolingRate = 0.9949

    res = generateRandomStates(board)
    current = res[0]
    generatedStates = res[1]

    temp = initialTemp(current, generatedStates)
    score = costFunction(current)
    iter = 0

    while iter < 100000 and temp != 0.00 and score != 0: 
        iter += 1
        random.shuffle(generatedStates)
        next = generateNewRandomState(current, generatedStates)
        if next is not None:
            nextScore = costFunction(next)
            delta = nextScore - score
            if delta < 0 or random.random() < math.exp(-delta/temp):
                score = nextScore
                current = copy.deepcopy(next)
            temp *= coolingRate
        else:
            return None

    return current, iter

def rec_solve_sa(current, temp, scoreCurrent, positionsList, n_iter):
    coolingRate = 0.9949

    if scoreCurrent == 0  or temp == 0.0 : # or n_iter == 1000000 or temp == 0.0:
        # solved
        print("Return")
        return current, n_iter

    # if not solved, i have to generate another random state
    next = generateNewRandomState(current, positionsList)
    if next is not None:
        # random swap is done
        scoreNext = costFunction(next)
        delta = scoreNext - scoreCurrent
        if delta < 0 or random.random() < math.exp((-delta)/temp):
            # next state is accepted
            return rec_solve_sa(next, temp*coolingRate, scoreNext, positionsList, n_iter + 1)
        else:
            # next state is not accepted
            return rec_solve_sa(current, temp*coolingRate, scoreCurrent, positionsList, n_iter + 1)
    else:
        return current, n_iter
    
# file = f"boards/normal/normal1.txt"
# board = createBoard(file)
# # res = generateRandomStates(board)
# # current = res[0]
# # list = res[1]
# # initial_temp = initialTemp(current, list)
# # initial_score = costFunction(current)
# # print(generateNewRandomState(board, list))
# # printBoard(board)
# # print(initialTemp(current, list))
# solution = solve_sa(board)
# if solution is not None:
#     solvedBoard = solution[0]
#     iterations = solution[1]
#     if checkSolution(solvedBoard):
#         printBoard(solvedBoard)
#         print("Sudoku risolto")
#         print("Numero di iterazioni = ", iterations)
#     else:
#         print("Sudoku non risolto!")
# else:
#     print("Sudoku non risolto!")