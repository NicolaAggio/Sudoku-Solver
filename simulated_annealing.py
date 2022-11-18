from utils import DIMENSION, createBoard, generateRandomStates, printBoard, numberOfDuplicates, generateNewRandomState, checkSolution
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
    listOfDifferences = []
    for i in range(0,20):
        copyB = copy.deepcopy(board)
        if generateNewRandomState(copyB, posList):
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
    numberIterations = numberOfIterations(board)
    coolingRate = 0.9949

    res = generateRandomStates(board)
    current = res[0]
    generatedStates = res[1]

    # print(generatedStates)
    # print("BOARD CON ASSEGNAMENTO INIZIALE")
    # printBoard(current)
    temp = initialTemp(current, generatedStates)
    currentScore = costFunction(current)
    # print("PUNTEGGIO INIZIALE = ", currentScore)
    # print("Temperatura iniziale = ", temp)
    iter = 0
    while currentScore != 0: 
        if temp == 0:
            print("Temperatura = 0")
            return current, iter
        # print("Iterazione = ", iter)
        # print("Temp = ", temp)
        iter += 1
        next = copy.deepcopy(current)
        if (generateNewRandomState(next, generatedStates)):
            # print("Board cambiata")
            # printBoard(next)
            nextScore = costFunction(next)
            # print("PUNTEGGIO SUCCESSIVO = ", nextScore)
            delta = nextScore - currentScore
            if delta < 0 or random.random() < math.exp(-delta/temp):
                currentScore = nextScore
                current = next
            temp *= coolingRate
        else:
            return None
    return current, iter

file = f"boards/easy/easy1.txt"
board = createBoard(file)
# res = generateRandomStates(board)
# printBoard(board)
# current = res[0]
# list = res[1]
# print(generateNewRandomState(board, list))
# printBoard(board)
# print(initialTemp(current, list))
res = solve_sa(board)
if (res):
    solved = res[0]
    iter = res[1]
    if checkSolution(solved):
        printBoard(solved)
        print("Numero di iterazioni = ", iter)
    else:
        print("Sudoku completato in maniera errata!")
else:
    print("Sudoku non risolto!")