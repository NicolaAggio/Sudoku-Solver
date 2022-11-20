from utils import DIMENSION, generateRandomStates, numberOfDuplicates, generateNewRandomState
import statistics, copy, random, math

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

    # repeat until either we reach 1,000,000 iterations, or 
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