"""
main.py

Main entry point for running the Boggle game. This script loads a Boggle board and
a dictionary of valid words, then searches for all possible words on the board.

Usage:
    python main.py

Functions:
    run_boggle_game(board_file, dictionary_file): Runs the Boggle game with a specified board and dictionary file.
"""

import time
from board import load_board, print_board
from dictionary import read_dictionary
from game_logic import find_words


def run_boggle_game(board_file, dictionary_file):
    """
    Loads the board and dictionary, then finds and prints all valid words on the board.

    Parameters:
        board_file (str): Path to the text file containing the board layout.
        dictionary_file (str): Path to the text file containing valid dictionary words.
    """
    board = load_board(board_file)
    dictionary = read_dictionary(dictionary_file)
    max_word_length = max(len(word) for word in dictionary)

    print("\nStarting Boggle Game!")
    print_board(board)

    start_time = time.time()
    found_words, total_moves = find_words(board, dictionary, max_word_length)
    elapsed_time = time.time() - start_time

    print(
        f"\nCompleted in {elapsed_time:.3f} seconds with {total_moves} moves.")
    print(f"Words Found: {', '.join(sorted(found_words))}")
    print(f"Total Words Found: {len(found_words)}")


if __name__ == "__main__":
    run_boggle_game(r"C:\Users\ruben\Documents\NAU\PhD\Fall2024\CS570\Homework\Boggle\Part_2\board_4x4_v5.txt",
                    r"C:\Users\ruben\Documents\NAU\PhD\Fall2024\CS570\Homework\Boggle\Part_2\twl06.txt")
