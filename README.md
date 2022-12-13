# Sudoku-solver

A sudoku puzzle is composed of a square 9x9 board divided into 3 rows and 3 columns of smaller 3x3 boxes. The goal is to fill the board with digits from 1 to 9 such that:

- each number appears only once for each row column and 3x3 box;
- each row, column, and 3x3 box should containing all 9 digits.
The solver should take as input a matrix where empty squares are represented by a standard symbol (e.g., ".", "_", or "0"), while known square should be represented by the corresponding digit (1,...,9).

Write a solver for sudoku puzzles using a constraint satisfaction approach based on constraint propagation and backtracking, and any one of your choice between the following approaches:
1) simulated annealing;
2) genetic algorithms;
3) continuous optimization using gradient projection.
