"""
board.py

Handles loading and displaying the Boggle board.

Functions:
    load_board(filename): Loads a Boggle board from a text file.
    print_board(board): Prints the Boggle board to the console.
"""


def load_board(filename):
    """
    Loads a Boggle board from a file. Each row is a space-separated line in the file.

    Parameters:
        filename (str): Path to the file containing the board layout.

    Returns:
        list: A 2D list representing the board, with each cell containing an uppercase letter.
    """
    with open(filename, 'r') as file:
        return [line.strip().upper().split() for line in file if line.strip()]


def print_board(board):
    """
    Prints the Boggle board to the console.

    Parameters:
        board (list): A 2D list representing the board to print.
    """
    for row in board:
        print(' '.join(row))
