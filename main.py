from costraint_propagation import solve_cp, getAllDomains, checkSolution, printBoard, writeBoard
from utils import createBoard

l = ["easy", "medium", "normal", "hard"]
i = 1

for item in l:
    board_collection = []
    for i in range(1, 6):
        file = f"boards/{item}/{item + str(i)}.txt"
        board_collection.append(createBoard(file))
    i = 1
    for board in board_collection:
        if solve_cp(board, getAllDomains(board)) and checkSolution(board):
            # printBoard(board)
            writeBoard("cp", f"{item + str(i)}.txt", board)
            i += 1
        else:
            print("SUDOKU NON RISOLTO")