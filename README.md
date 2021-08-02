# HoH-LO-Puzzle-Solver
In Heroes of Hammerwatch, there is a 3x3 puzzle that is a variant of Lights Out. When you touch a cell, it toggles the adjacent cells around it as on or off. The goal is to flip all the cells on. While I like puzzles I am also pretty lazy, so I coded up a puzzle solver for this.

The 3x3 grid is broken down in like this
0 1 2
3 4 5
6 7 8


To use the script:

 1. edit the toggles.txt file with the appropriate index (See above).
 2. run in cmd or terminal `python puzzle_solve.py toggles.txt`
 3. See the output and follow the sequence of numbers in the order it is given.
 4. Have fun.  
