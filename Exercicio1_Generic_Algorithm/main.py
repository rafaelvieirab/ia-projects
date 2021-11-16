import random
from genetic_operators import crossover, mutation
from selection_functions import selection_by_tournament
from utils import binary_to_decimal, decimal_to_binary


def generate_initial_population(limits):
    (initial, final) = limits
    population = [i for i in range(initial, final+1)]
    return population

def get_better_generation(generation: list, better_function):
    while len(generation) > 1:
        (_, worse) = better_function(generation, 0, 1)
        generation.pop(worse)
    better = generation[0]
    return better

def main(limits, individuals_number, fitness_function, generation_limits, better_function):
    population = generate_initial_population(limits)

    generation = random.choices(population, k=individuals_number)
    print('\nGeração 0:')
    print(generation)

    for i in range(generation_limits):
        chromosomes = list(map(decimal_to_binary, generation))
        evaluated_chromosomes = list(map(fitness_function, generation))
        
        selecteds_chromosomes = selection_by_tournament(chromosomes, evaluated_chromosomes, better_function)
        new_generation = [chromosomes[selected] for selected in selecteds_chromosomes]
        
        crossed_chromosomes = crossover(chromosomes, selecteds_chromosomes)
        new_generation += crossed_chromosomes

        mutant_chromosomes = mutation(new_generation)
        generation = list(map(binary_to_decimal, mutant_chromosomes))

        print(f'\nGeração {i + 1}:')
        print(generation)
    
    better = get_better_generation(generation, better_function)
    print(f'\nMelhor valor de x encontrado: {better}, com f({better}) = {fitness_function(better)}')
    return better


if __name__ == "__main__":
    limits = (-10, 10)
    individuals_number = 4
    fitness_function = lambda x : x^2 - 3*x + 4
    better_function = lambda array,x,y : (x,y) if array[x] < array[y] else (y, x)
    generation_limits = 5
    main(limits, individuals_number, fitness_function, generation_limits, better_function)

