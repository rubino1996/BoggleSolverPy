# BoggleSolverPy
 BoggleSolverPy efficiently finds words on Boggle boards up to 4x4 using an input dictionary, with optimized search and categorization. It can also handle larger boards, though performance may decrease with larger dictionaries. 

 ## Features
- Efficient word-finding for boards up to 4x4 in size
- Supports custom dictionaries, allowing exploration of word patterns
- Optimized recursive search to identify words and categorize by length
- Configurable to work with larger boards, albeit with longer processing times
- Command-line utility for loading boards and running the solver
- Outputs discovered words, sorted by length and alphabetically

## Installation
git clone https://github.com/rubino1996/BoggleSolverPy.git

## Usage
1. **Board File**: Create a text file with your Boggle board layout (e.g., board.txt), using spaces to separate letters and each line as a row.
[here](board_4x4_v1.txt)

2. **Dictionary File**: Prepare a text file with valid words, one per line (e.g., [here](dictionary.txt)).

## Runing the Solver
- python main.py

## Example Output
- Starting Boggle Game!
- Board NxN Loads
- Completed in "x" seconds with "x" moves.
- Words Found:.....
- Total Words Found: x
