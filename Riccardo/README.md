# Sudoku-Solver

## Task
Write a solver for sudoku puzzles using a constraint satisfaction approach based on constraint propagation and backtracking, and one based on Relaxation Labeling. compare the approaches, their strengths and weaknesses.

A sudoku puzzle is composed of a square 9x9 board divided into 3 rows and 3 columns of smaller 3x3 boxes. The goal is to fill the board with digits from 1 to 9 such that:
* Each number appears only once for each row column and 3x3 box;
* Each row, column, and 3x3 box should containg all 9 digits.

The solver should take as input a matrix withwhere empty squares are represented by a standars symbol (e.g., ".", "_", or "0"), while known square should be represented by the corresponding digit (1,...,9). For example:

370 500 006<br/>
000 360 012<br/>
000 091 750<br/>
000 154 070<br/>
003 070 600<br/>
050 638 000<br/>
064 980 000<br/>
590 026 000<br/>
200 005 064<br/>

Hints for Constraint Propagation and Backtracking:
* Each cell should be a variable that can take values in the domain (1,...,9).
* The two types of constraints in the definition form as many types of constraints:
    * Direct constraints impose that no two equal digits appear for each row, column, and box;
    * Indirect constrains impose that each digit must appear in each row, column, and box.
* You can think of other types of (pairwise) constraints to further improve the constraint propagation phase.
* Note: most puzzles found in the magazines can be solved with only the constraint propagation step.


Hints for Relaxation Labeling:
* Each cell should be an object, the values between 1 and 9 labels.
* The compatibility rij(λ,μ) should be 1 if the assignments satisfy direct constraints, 0 otherwise.


## How to start the Application Bechmark
* You need to install numpy and pandas by typing: ```
pip3 install numpy``` and ```
pip3 install pandas ```
* Enter in the main directory of the project
* Type ```python3 solver.py ```
* After the computation the results and statistics of solved Sudoku puzzle will be stored in the *results* directory
