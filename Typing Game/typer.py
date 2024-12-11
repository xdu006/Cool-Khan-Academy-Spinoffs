"""Plays a game where the user types random words within a time limit."""

import random
import time
import word_bank

def play_round(words, seconds):
    """Returns True if the user successfully completed the round."""
    # Run a stopwatch for the time it takes the user to respond.
    start = time.time()
    response = input("(" + str(seconds) + " seconds) " + words + "\n")
    stop = time.time()

    # Fail the round if a word is mispelled or if time runs out.
    within_time_limit = stop - start < seconds
    return response == words and within_time_limit

def pick_random_words(num_words, word_length):
    """Returns a random phrase containing the given number of words.""" 
    words = ""
    for word in range(num_words):
        word = get_random_word(word_length)
        words = words + " " + word

    return words.strip()

def get_random_word(mode):
    """Returns a random word with a word length based on the given mode."""
    if mode == "hard":
        words = word_bank.hard_words
    elif mode == "medium":
        words = word_bank.medium_words
    else:
        words = word_bank.easy_words

    return random.choice(words)
