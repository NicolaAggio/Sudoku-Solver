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
    copyB = copy.deepcopy(board)
    listOfDifferences = []
    for i in range(0,20):
        copyB = generateNewRandomState(copyB, posList)
        if copyB is not None:
            listOfDifferences.append(costFunction(copyB))
    return statistics.pstdev(listOfDifferences)

def numberOfIterations(board):
    count = 0
    for row in range(0, DIMENSION):
        for col in range(0, DIMENSION):
            if board[row][col] == 0:
                count += 1
    return count^2

def solve_sa(board):
    # cooling rate
    coolingRate = 0.9949

    # generates the first candidate solution
    res = generateRandomStates(board)
    current = res[0]
    generatedStates = res[1]

    # computes the initial temperature
    initial_temp = initialTemp(current, generatedStates)
    temp = initial_temp

    # computes the cost function of the first candidate solution
    score = costFunction(current)

    # number of iterations and number of reheats
    iter = 0
    nReheat = 1

    # repeat untile either we reach 1,000,000 iterations, or 
    # the temperature reaches 0 or the score reaches 0 (i.e. a solution is found)
    while iter < 1000000 and temp != 0.00 and score != 0: 

        # reheat after 10,000 iterations
        if (iter == nReheat * 10000):
            nReheat += 1
            temp = initialTemp(res[0], generatedStates)
        iter += 1

        # shuffle of the non-fixed cells
        random.shuffle(generatedStates)

        # generates the neighbour state
        next = generateNewRandomState(current, generatedStates)
        if next is not None:
            nextScore = costFunction(next)
            delta = nextScore - score

            # conditions in which we accept the neighbour 
            if delta < 0 or random.random() < math.exp(-delta/temp):
                score = nextScore
                current = copy.deepcopy(next)

            # cooling down the temperature
            temp *= coolingRate
        else:
            return None
    return current, iter, nReheat-1

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