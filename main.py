import time
import csv
from costraint_propagation import solve_cp
from simulated_annealing import solve_sa
from utils import createBoard, checkSolution, writeBoard

l = ["easy", "normal", "medium", "hard"]
i = 1
cp_results = []
sa_results = []

for item in l:
    board_collection = []
    for i in range(1, 6):
        file = f"boards/{item}/{item + str(i)}.txt"
        board_collection.append(createBoard(file))
    i = 1
    for board in board_collection:
        start_time = time.time()
        solved, board, back = solve_cp(board, 0)
        execution_time = time.time() - start_time
        if solved and checkSolution(board):
            writeBoard("cp", f"{item + str(i)}.txt", board)
            cp_results.append((solved,f"{item + str(i)}.txt", execution_time, back))
            i += 1
        else:
            print("SUDOKU NON RISOLTO_BACKPROPAGATION")

header = ['solved','filename', 'execution_time', 'backpropagation']
with open('./results/cp/results.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for elem in cp_results:
        writer.writerow(elem)

for item in l:
    board_collection = []
    for i in range(1, 6):
        file = f"boards/{item}/{item + str(i)}.txt"
        board_collection.append(createBoard(file))
    i = 1
    for board in board_collection:
        start_time = time.time()
        solution = solve_sa(board)
        execution_time = time.time() - start_time
        if solution is not None:
            solvedBoard = solution[0]
            iterations = solution[1]
            numberReheat = solution[2]
            if checkSolution(solvedBoard):
                writeBoard("annealing", f"{item + str(i)}.txt", solvedBoard)
                sa_results.append((True,f"{item + str(i)}.txt", execution_time, iterations, numberReheat))              
            else:
                sa_results.append((False,f"{item + str(i)}.txt", execution_time, iterations, numberReheat))
                print("Sudoku non risolto!")
        else:
            sa_results.append((False,f"{item + str(i)}.txt", execution_time, iterations, numberReheat))
            print("Sudoku non risolto!") 

        i += 1

header = ['solved','filename', 'execution_time', 'number_of_iterations', 'number_of_reheats']
with open('./results/annealing/results.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for elem in sa_results:
        writer.writerow(elem)