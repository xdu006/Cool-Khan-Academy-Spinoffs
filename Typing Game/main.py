import typer

# Play three rounds of a speed typing game.
def play_level(time, difficulty):
    for round in range(1, 4):
        print("Round " + str(round))
    
        words_to_type = typer.pick_random_words(round, difficulty)
        passed = typer.play_round(words_to_type, time)
        if not passed:
            print("Oops!")
            return 0
    return 1

level = 0
print("Type the words and hit enter within the time limit!\n")

level += play_level(10, "easy")

if level == 1 : 
    print(f"\n--------LEVEL {level} PASSED--------\n")
    level += play_level(10, "medium")

if level == 2 : 
    print(f"\n--------LEVEL {level} PASSED--------\n")
    level += play_level(10, "hard")

if level == 3 : 
    print(f"\n--------LEVEL {level} PASSED--------\n")
    level += play_level(5, "medium")

if level == 4 : 
    print(f"\n--------LEVEL {level} PASSED--------\n")
    level += play_level(5, "hard")
   

print(f"\nHIGHEST LEVEL CONQURED: level {level}! \nThanks for playing.")
