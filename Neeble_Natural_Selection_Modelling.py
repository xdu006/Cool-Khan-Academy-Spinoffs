"""Simulates natural selection in the fictional Neebler population."""

import random

# Continue through some generations
generation = 1
max_gen = 50

# Starting population with each trait variation.
small_neeblers = 5
large_brood_neeblers = 5


while generation <= 50 and (small_neeblers+large_brood_neeblers) != 0:

    # Let's see how many offspring of each trait we can get for each generation
    baby_small_neeblers = 0
    baby_large_brood_neeblers = 0
    
    # when neebler population is too large, they become easier to hunt 
    # and resource depletion increases,  
    population_factor = 0
    if small_neeblers+large_brood_neeblers > 10000:
        population_factor = 1.5
    
    for neebler in range(small_neeblers):
        # Low chance of being spotted by predators since they're small.
        chance_of_survival = random.randint(0, 6) - population_factor
        if chance_of_survival <= 0:
            small_neeblers -= 1 # neebler died :(
        else: # Smallness trait gets passed to their babies.
            num_babies = random.randint(0, 3)
            baby_small_neeblers += num_babies
           
    for neebler in range(large_brood_neeblers):
        # Higher chance of being spotted by predators, but large family size
        chance_of_survival = random.randint(0, 2) - population_factor
        if chance_of_survival <= 0:
            large_brood_neeblers -= 1
        else: # Larger brood of babies
            num_babies = random.randint(0, 3) * 2 
            baby_large_brood_neeblers += num_babies

    # Babies become the starting population of the next generation.
    small_neeblers = baby_small_neeblers
    large_brood_neeblers = baby_large_brood_neeblers

    print("Generation " + str(generation) + "-----------------")
    print(str(small_neeblers) + " small Neeblers")
    print(str(large_brood_neeblers) + " large brood Neeblers")
    generation +=1
