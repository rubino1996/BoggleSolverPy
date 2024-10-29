"""
game_logic.py

Contains core game logic for Boggle, including finding possible moves,
performing depth-first search (DFS) to discover words, and filtering valid words.

Functions:
    possible_moves(x, y, board): Generates all legal moves from a given position.
    find_words(board, dictionary, max_word_length): Finds all valid words on the board.

Helper Functions:
    dfs(x, y, path, current_word): Recursively searches for words using DFS.
"""

from board import load_board
from dictionary import read_dictionary


def possible_moves(x, y, board):
    """
    Generates all valid adjacent positions (including diagonals) on the board from a given position.

    Parameters:
        x (int): Row index of the current position.
        y (int): Column index of the current position.
        board (list): The 2D list representing the Boggle board.

    Returns:
        list: A list of tuples representing valid (x, y) moves from the current position.
    """
    moves = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                    moves.append((new_x, new_y))
    return moves


def find_words(board, dictionary, max_word_length):
    """
    Finds all valid words on the Boggle board using DFS.

    Parameters:
        board (list): The Boggle board as a 2D list.
        dictionary (set): A set of valid words.
        max_word_length (int): Maximum word length to consider.

    Returns:
        tuple: A set of valid words found on the board, and the total number of moves made.
    """
    found_words = set()
    total_moves = [0]  # Track total moves across all DFS calls

    def dfs(x, y, path, current_word):
        """
        Recursively explores the board to find all valid words starting from the given position.

        Parameters:
            x (int): Row index of the current position.
            y (int): Column index of the current position.
            path (list): List of (x, y) positions representing the path taken.
            current_word (str): Current word formed by following the path.
        """
        total_moves[0] += 1
        if len(current_word) > max_word_length:
            return
        if len(current_word) >= 2 and current_word in dictionary:
            found_words.add(current_word.upper())
        for new_x, new_y in possible_moves(x, y, board):
            if (new_x, new_y) not in path:
                dfs(new_x, new_y, path + [(new_x, new_y)],
                    current_word + board[new_x][new_y].lower())

    for x in range(len(board)):
        for y in range(len(board[0])):
            dfs(x, y, [(x, y)], board[x][y].lower())
    return found_words, total_moves[0]
