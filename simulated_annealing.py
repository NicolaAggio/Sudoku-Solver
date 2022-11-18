from utils import DIMENSION, createBoard, generateRandomStates, printBoard, numberOfDuplicates, generateNewRandomState, checkSolution
import statistics, copy, random, math
# 1) generating unique random values for each 3x3 block 
# 2) cost function = sum of duplicated values on rows and columns 
# 3) selecting starting temperature = standard deviation of the cost for 200 starting states
# 4) calculating iterations per T = (#free entries)^2
# 5) choosing a cooling rate = 0.99.. prova a fare delle comparazioni per vedere come si comporta l'algoritmo

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
    for i in range(0,200):
        copyB = copy.deepcopy(board)
        if generateNewRandomState(posList, copyB):
            listOfDifferences.append(costFunction(copyB))
    return statistics.pstdev(listOfDifferences)

# non so se serva
def numberOfIterations(board):
    count = 0
    for row in range(0, DIMENSION):
        for col in range(0, DIMENSION):
            if board[row][col] == 0:
                count += 1
    return count^2

def simulatedAnnealing(board):
    coolingRate = 0.99
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
        print("Iterazione = ", iter)
        # print("Temp = ", temp)
        iter += 1
        next = copy.deepcopy(current)
        if (generateNewRandomState(generatedStates, next)):
            # print("Board cambiata")
            # printBoard(next)
            nextScore = costFunction(next)
            # print("PUNTEGGIO SUCCESSIVO = ", nextScore)
            delta = nextScore - currentScore
            if delta < 0:
                currentScore = nextScore
                current = next
            else:
                if random.random() < math.exp(-delta/temp):
                    current = next
            temp *= coolingRate
        else:
            return None
    return (current, iter)

file = f"boards/easy/easy1.txt"
board = createBoard(file)
# print(numberOfIterations(board))
# print(getBoxes())
# res = []
# res += generateRandomStates(board)
# print("Posizioni riempite = ",res)
# printBoard(board)

# # swap = randomSwap(res, board)
# # print(swap)
# printBoard(board)
# # print(costFunction(board))
# print(initialTemp(board, res))

# res = generateRandomStates(board)
# current = res[0]
# list = res[1]
# print(initialTemp(current, list))
res = simulatedAnnealing(board)
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