""" Main Program for running a single fruits card game"""

import game_round

card_suites = {0:"Banana", 1:"Apple", 2:"Cherry", 3:"Mango", 4:"Poison Apple"}
cards_per_suite = [0, 0, 0, 0, 0] # Index correlates to card suites
player_hand = ""
max_rounds = 10
pausetime_between_prints = 0.1

for round in range(max_rounds):
    
    # Begin new round, players pick a card from two options
    print(f"\nRound {round+1} -------------") 
    time.sleep(pausetime_between_prints)
    new_card = game_round.pick_a_card(card_suites)
    cards_per_suite[new_card] += 1
    player_hand += f"{card_suites[new_card]}, "

    # Display current game status
    print(f"Your current hand is: {player_hand}") 
    time.sleep(pausetime_between_prints)
    print("You currently have: ") 
    for suite in range(len(cards_per_suite)):
        time.sleep(pausetime_between_prints)
        print(f"\t {cards_per_suite[suite]} {card_suites[suite]} Card(s), ", sep="")
    
    # Calculate the score after each round.
    player_score = game_round.get_score(cards_per_suite)
    time.sleep(pausetime_between_prints)
    print(f"Your score: {player_score} pts")
    time.sleep(pausetime_between_prints)

print  (f"\nFINAL SCORE: {player_score} pts")
