# Usefull Import
from cmath import e
from techniques.constraint_propagation import solveConstraintPropagation
from techniques.relaxation_labelling import solveRelaxationLabeling
from os import listdir
import pandas as pd
from techniques.utils import checkSolution, readFile, writeFile
from time import time

#https://printablecreative.com/sudoku-generator
#solveSudoku("./examples/easy/easy1.txt".format())

# List where the results will be stored
resultCP = []
resultRL = []


# List of initial sudoku cofiguration for each difficulty 
easySudoku = listdir("./examples/easy")
normalSudoku = listdir("./examples/normal")
mediumSudoku = listdir("./examples/medium")
hardSudoku = listdir("./examples/hard")


# Function to solve the sudoku board using the Constraint Propagation and Back Tracking technique
def solveCP(filename):
    board = readFile(filename)
    print(f"Constraint Propagation - Solving: {filename}")
    try:
        start = time()
        solved, board, exp, back = solveConstraintPropagation(board, 0, 0)
        end = time()
    except Exception as e:
        print(f"Exception appear: {e}")
        return
    print("DONE\n")
    resultCP.append([filename.split("/")[3], str(round((end - start), 6)), exp, back, solved]) # Information that we store for each sudoku after computation
    writeFile("cp_solved_boards", filename.split("/")[3], board)
    
    
# Function to solve the sudoku board using the Relaxation Labelling technique
def solveRL(filename):
    board = readFile(filename)
    print(f"Relaxation Labelling - Solving: {filename}")
    try:
        start = time()
        board, n_iter = solveRelaxationLabeling(board)
        end = time()
    except Exception as e:
        print(f"Exception appear: {e}")
        return
    print("DONE\n")
    resultRL.append([filename.split("/")[3], str(round((end - start), 6)), n_iter, checkSolution(board)]) # Information that we store for each sudoku after computation
    writeFile("rl_solved_boards", filename.split("/")[3], board) 


def solveSudoku(filename):
    solveCP(filename)
    solveRL(filename)


if __name__ == "__main__":
    print("EASY SUDOKU:")
    for easy in sorted(easySudoku): solveSudoku(f"./examples/easy/{easy}".format())    

    print("\n\nNORMAL SUDOKU:")
    for normal in sorted(normalSudoku): solveSudoku(f"./examples/normal/{normal}".format())

    print("\n\nMEDIUM SUDOKU:")
    for medium in sorted(mediumSudoku): solveSudoku(f"./examples/medium/{medium}".format())
        
    print("\n\nHARD SUDOKU:")
    for hard in sorted(hardSudoku): solveSudoku(f"./examples/hard/{hard}".format())
       
    print("\n\nRESULTS FOR CONSTRAINT PROPAGATION")
    df_resultCP = pd.DataFrame(resultCP, columns=["Filename", "Execution_Time", "Expanded_Nodes", "Backward_Nodes", "Solved"])
    print(df_resultCP.to_string(index=False))

    print("\n\nRESULTS FOR RELAXATION LABELLING")
    df_resultRL = pd.DataFrame(resultRL, columns=["Filename", "Execution_Time", "Number_of_Iteration", "Solved"])
    print(df_resultRL.to_string(index=False))

    df_resultCP.to_csv("./results/cp_result.csv", index=False)
    df_resultRL.to_csv("./results/rl_result.csv", index=False)