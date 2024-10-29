"""
dictionary.py

Handles loading and managing a dictionary of valid words.

Functions:
    read_dictionary(filename): Reads a list of valid words from a text file.
"""


def read_dictionary(filename):
    """
    Reads a dictionary of words from a file. Each word should be on a new line.

    Parameters:
        filename (str): Path to the dictionary file.

    Returns:
        set: A set of valid words in lowercase.
    """
    with open(filename, 'r') as file:
        return set(line.strip().lower() for line in file if line.strip())
