"""
Word Puzzle Solver

This script solves a word puzzle by finding valid words that contain a central letter
and are composed of a given set of letters.

Usage:
    python main.py <all_letters> <central_letter> [--min_length MIN_LENGTH]

Example:
    python main.py AOPLYMG G --min_length 4

Arguments:
    all_letters    : All letters to use in the puzzle
    central_letter : The central letter that must be included in each word
    --min_length   : Minimum word length (default: 4)
"""

import re
import nltk
from nltk.corpus import words
import argparse

# Download the words corpus if it's not already available
nltk.download('words', quiet=True)

def solve_word_puzzle(letters, central_letter, min_length):
    # Convert letters to lowercase for case-insensitive matching
    letters = letters.lower()
    central_letter = central_letter.lower()
    
    # Create a set of valid letters
    valid_letters = set(letters)
    
    valid_words = []
    
    for word in words.words():
        word = word.lower()
        if (len(word) >= min_length and
            central_letter in word and
            all(letter in valid_letters for letter in word)):
            valid_words.append(word)
    
    return valid_words

# Set up argument parser
parser = argparse.ArgumentParser(description="Solve a word puzzle")
parser.add_argument("all_letters", help="All letters to use in the puzzle")
parser.add_argument("central_letter", help="The central letter that must be included in each word")
parser.add_argument("--min_length", type=int, default=4, help="Minimum word length (default: 4)")

args = parser.parse_args()

# Solve the puzzle using command-line arguments
solution = solve_word_puzzle(args.all_letters, args.central_letter, args.min_length)

# Print the results
print(f"Valid words (at least {args.min_length} letters long, including '{args.central_letter}', using only letters from '{args.all_letters}'):")
for word in sorted(solution):
    print(word)

print(f"\nTotal words found: {len(solution)}")