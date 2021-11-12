import random

PROBABILITY_K = 0.75

def selection_by_tournament(population: list, population_fitness: list, individuals_number: int, better_function) -> list:
    k = PROBABILITY_K
    selecteds = []

    remaining = list(population)
    for i in range(individuals_number):
        pos1 = random.randint(0, len(remaining))
        remaining.pop(pos1)
        pos2 = random.randint(0, len(remaining))
        remaining.pop(pos2)

        better = better_function(population_fitness[pos1], population_fitness[pos2])
        r = random.random()
        selected = None

        if r < k: #  escolhe o melhor individuo
            selected = better
        else: # escolhe o pior individuo
            if better == population_fitness[pos1]:
                selected = population[pos2]
            else:
                selected = population[pos1] 

        selecteds.append(selected)
    return selecteds
