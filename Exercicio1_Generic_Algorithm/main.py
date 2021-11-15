import random
from selection_functions import selection_by_tournament
from utils import binary_to_decimal, decimal_to_binary


def generate_initial_population(elementInitial, elementFinal):
    population = [i for i in range(elementInitial, elementFinal+1)]
    return population


def main(elementInitial, elementFinal, individuals_number, fitness_function, generation_limits, better_function):
    population = generate_initial_population(elementInitial, elementFinal)

    generation = random.choices(population, k=individuals_number)
    print('\nGeração 0:')
    print(generation)

    for i in range(generation_limits):
        chromosomes = list(map(decimal_to_binary, generation))
        evaluated_chromosomes = list(map(fitness_function, generation))
        selecteds_chromosomes = selection_by_tournament(chromosomes, evaluated_chromosomes, better_function)
        crossed_chromosomes = crossover(chromosomes, selecteds_chromosomes)
        print("Crossed chromosomes: ", crossed_chromosomes)

        mutant_chromosomes = mutation(crossed_chromosomes)
        generation = list(map(binary_to_decimal, mutant_chromosomes))

        print(f'\nGeração {i}:')
        print(generation)
    return generation


def mix_chromosomes(byte1:str, byte2: str):
    cross_point = random.randint(1, len(byte1) - 2)
    mixed1 = byte1[:cross_point] + byte2[cross_point:]
    mixed2 = byte2[:cross_point] + byte1[cross_point:]
    return (mixed1, mixed2)


def crossover(chromosomes: list, selecteds: list, tax = 0.6) -> list:
    crossed_chromosomes = []

    while(len(selecteds) > 1):
        c1 = random.choice(selecteds)
        selecteds.remove(c1)
        c2 = random.choice(selecteds)
        selecteds.remove(c2)

        # Todo tem que ver como mudar a quantidade de elementosP
        (mixed1, mixed2) = mix_chromosomes(chromosomes[c1], chromosomes[c2])

        crossed_chromosomes.append(mixed1)
        crossed_chromosomes.append(mixed2)

    if len(selecteds) == 1:
        crossed_chromosomes.append(chromosomes[selecteds[0]])

    return crossed_chromosomes


def mutation(chromosomes: list, tax = 0.01) -> list:
    def mutation2(chromosome: str):
        pos = random.randint(1, len(chromosome) - 1)
        new_bit = ''
        if chromosome[pos] == '0':
            new_bit = '1'
        else:
            new_bit = '0'
        chromosome = chromosome[:pos-1] + new_bit + chromosome[pos:]
        return chromosome

    mutant_chromosomes = list(chromosomes)
    mutant_chromosomes = list(map(mutation2, mutant_chromosomes))
    return mutant_chromosomes


if __name__ == "__main__":
    elementInitial = -10
    elementFinal = 10
    individuals_number = 4
    fitness_function = lambda x : x^2 - 3*x + 4
    better_function = lambda array,x,y : (x,y) if array[x] < array[y] else (y, x)
    generation_limits = 5
    main(elementInitial, elementFinal, individuals_number, fitness_function, generation_limits, better_function)

