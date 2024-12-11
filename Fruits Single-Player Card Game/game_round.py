"""Deals fruits cards and scores current hand based on number of each card type."""

import random
import time

def get_score(cards_per_suite):
    """Returns a player's total score based on their cards of each type."""
    banana_score = get_banana_score(cards_per_suite[0])
    apple_score = get_apple_score(cards_per_suite[1], cards_per_suite[4]>0)
    cherry_score = get_cherry_score(cards_per_suite[2])
    mango_score = get_mango_score(cards_per_suite[3])

    return banana_score + apple_score + cherry_score + mango_score

def get_banana_score(num_bananas):
    """ Returns the banana score based on the number of bananas. """   
    # Bananas are worth more in bunches.
    if num_bananas == 1:
        return 1
    elif num_bananas == 2:
        return 4
    elif num_bananas >= 3:
        return 10
    else:
        return 0

def get_apple_score(num_apples, has_poison_apple):
    """ Returns the apple score based on the number of apples. """
    # Each apple give players 2 points, but gives -2 points if they have a poison apple.
    if has_poison_apple: 
        return num_apples * -2
    return num_apples * 2
    
def get_cherry_score(num_cherries): 
    """ Each pair of cherries get 5 point. Returns the cherry score based on the number of cherries. """
    return num_cherries // 2 * 5

def get_mango_score(num_mangos):
    """ Returns the mango score based on the number of mangos. """
    # Mango are only worth points if they are all in pairs. 
    if num_mangos % 2 == 0:
        return num_mangos * 3
    else: 
        return 0


def pick_a_card(card_suites):
    """ Deals 2 cards based on inputted card suites and asks player to pick one. Returns the index of the card chosen. """

    # Generate and display cards
    choice = None
    card_A = random.randint(0, len(card_suites)-2)
    card_B = random.randint(0, len(card_suites)-2)
    print(f"Card A: {card_suites[card_A]} \nCard B: {card_suites[card_B]}")

    # Apple cards have a chance of mutating into a poison apple card
    mutation_threshold = 0.85
    if 1 in (card_A, card_B):
        if random.random() > mutation_threshold:
            print("FUROONNNG: What's this, your Apple card mutated into a Poisoned Apple card! \n" +
                  "Unfortunetly, you do not get a choice this round. \n" +
                  "The Poisoned Apple card has been added to your hand.")
            return 4

    # Players can choose a card and the choice is returned
    while not (choice == "A" or choice == "B"):
        choice = input("You may pick one card to keep. " +
                       "Enter A to keep Card A, Enter B to keep Card B: ")
    if choice == "A": 
        return card_A
    else:
        return card_B
