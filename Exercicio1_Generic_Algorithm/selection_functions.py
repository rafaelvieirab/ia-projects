import random

PROBABILITY_K = 0.75

def selection_by_tournament(population: list, population_fitness: list, better_function) -> list:
    k = PROBABILITY_K
    selecteds = []

    remaining = [i for i in range(len(population))]

    while(len(remaining) > 1):
        pos1 = random.choice(remaining)
        remaining.remove(pos1)
        
        pos2 = random.choice(remaining)
        remaining.remove(pos2)

        (better, worse) = better_function(population_fitness, pos1, pos2)
        r = random.random()
        selected = None

        if r < k:
            selected = better
        else:
            selected = worse

        selecteds.append(selected)

    if(len(remaining) == 1):
        selecteds.append(remaining[0])
    return selecteds
