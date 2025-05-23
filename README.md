# Minesweeper Solver using Hill Climbing Algorithm

## Description
This project implements a Minesweeper game solver using the Hill Climbing algorithm combined with heuristic evaluation to minimize the risk of selecting a cell containing a mine. The solver uses NumPy for efficient data representation and computation.

## Features
- **Randomly Generated Board**: A customizable Minesweeper board is generated with randomly placed mines.
- **Heuristic Evaluation**: Each hidden cell is evaluated using a heuristic that estimates the risk of containing a mine based on adjacent revealed cells.
- **Hill Climbing Approach**: Iteratively selects the safest cell based on calculated heuristics to maximize the chance of successfully clearing the board.
- **Interactive Display**: The solver provides real-time feedback by displaying the state of the board after each move.

## Requirements
- Python 3.x
- NumPy

## Installation
Install the required dependencies using pip:
```bash
pip install numpy
```

## Usage
To run the Minesweeper solver:
```bash
python minesweeper_solver.py
```

## How It Works
1. **Board Initialization**: Randomly places mines on the board and calculates the number of adjacent mines for each cell.
2. **Heuristic Calculation**: Estimates the risk for each unopened cell based on adjacent revealed numbers.
3. **Cell Selection**: Chooses the unopened cell with the lowest estimated risk.
4. **Game Progression**: Reveals selected cells iteratively until all safe cells are uncovered or a mine is encountered.

## Example Output
```
Mở ô (3, 2) an toàn với rủi ro ước tính 0.1000.
?  ?  ?  ?  ?  ?  ?  ?  ?  ?
?  ?  ?  ?  ?  ?  ?  ?  ?  ?
?  ?  ?  ?  ?  ?  ?  ?  ?  ?
?  ?  0  ?  ?  ?  ?  ?  ?  ?
...
Chúc mừng, bạn đã thắng trò chơi!
```

## License
This project is licensed under the MIT License.

## Author
Your Name

