# Number Collapse Game

A simple number-collapse puzzle game implemented in Python. The game reads a board from an input file, where identical adjacent numbers can be selected to remove them. The removed numbers shift down, and empty rows/columns are deleted. The game continues until no more moves are possible.

## How to Play

1. Run the script with an input file containing the game board.

2. The game will display the board and prompt the user to enter row and column numbers to select a group of adjacent identical numbers.

3. If a valid move is made, the selected numbers are removed, and the board is updated.

4. The score is calculated based on the number of numbers removed.

5. The game continues until no more valid moves are possible.

## Installation & Usage

### Prerequisites

Ensure you have Python installed (Python 3 recommended).

### Running the Game

1. Clone the repository or download the script.

2. Prepare an input file (e.g., board.txt) containing a grid of space-separated numbers.

3. Run the script:
```

python game.py board.txt
```

4. Follow the on-screen instructions to play the game.

## Example Input File
```

1 2 3 4 5 6 7
1 2 2 2 2 4 5
5 5 5 5 5 5 5
```

## Features

- Breadth-first search (BFS) algorithm to traverse and remove connected identical numbers.

- Automatic downward shift of remaining numbers.

- Deletion of empty rows and columns.

- A scoring system based on the number of removed numbers.

- Game-over detection when no more moves are possible.

## Code Structure

- ``` traverse(board, row, column):```  Finds and removes adjacent identical numbers.

- ``` checker(board, row, column): ``` Validates user input.

- ```move_down(board): ``` Moves numbers downward to fill gaps.

- ```row_del(board):``` Removes empty rows.

- ```column_del(board):``` Removes empty columns.

- ```is_game_over(board):``` Checks if any moves are left.

- ```play(board, total):``` Main game loop.

- ```read_input_file():``` Reads the board from a file.

- ```main():``` Starts the game.

## Example Gameplay
```
1 2 3 4 5 6 7
1 2 2 2 2 4 5
5 5 5 5 5 5 5

Your score is: 0

Please enter a row and a column number: 1 1

  2 3 4 5 6 7 
  2 2 2 2 4 5
5 5 5 5 5 5 5

Your score is: 2

Please enter a row and a column number: 3 1

2 3 4 5 6
2 2 2 2 4 7

Your score is: 42

Please enter a row and a column number: 1 1

      6
3 4 5 4 7

Your score is: 52

Game over
```
## License

This project is open-source. Feel free to modify and improve it!
