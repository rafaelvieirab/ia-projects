import random
from selection_functions import selection_by_tournament
import utils

def generate_initial_population(elementInitial, elementFinal):
    population = [i for i in range(elementInitial, elementFinal+1)]
    return population

def aux(elementInitial, elementFinal, individuals_number, fitness_function, generation_limits, better_function):
    generation = generate_initial_population(elementInitial, elementFinal)

    for i in range(generation_limits):
        chromosomes = random.choices(generation, k=individuals_number)
        chromosomesBytes = list(map(bin, chromosomes))
        evaluated_chromosomes = list(map(fitness_function, chromosomes))

        selecteds_chromosomes = selection_by_tournament(chromosomesBytes, evaluated_chromosomes, individuals_number, better_function)
        crossed_chromosomes = crossover(selecteds_chromosomes)
        mutant_chromosomes = mutation(crossed_chromosomes)
        generation = mutant_chromosomes
    return generation

def mix_bytes(byte1:bytes, byte2: bytes):
    cross_point = random.randint(3, len(byte1))

    mixed1 = byte1[0:cross_point] + byte2[cross_point:]
    mixed2 = byte2[0:cross_point] + byte1[cross_point:]

    return (mixed1, mixed2)

def crossover(chromosomes: list, tax = 0.6) -> list:
    crossed_chromosomes = []

    while(len(chromosomes) > 1):
        (c1, c2) = random.choices(chromosomes, k=2)
        (mixed1, mixed2) = mix_bytes(c1, c2)

        crossed_chromosomes.append(mixed1)
        crossed_chromosomes.append(mixed2)

        chromosomes.pop(c1)
        chromosomes.pop(c2)

    if chromosomes != []:
        crossed_chromosomes.append(chromosomes[0])

    return crossed_chromosomes

def mutation(chromosomes: list, tax = 0.01) -> list:
    def mutation2(chromosome: bytes):
        pos = random.randint(2, len(chromosome))
        if chromosome[pos] == '0':
            chromosome[pos] = '1'
        else:
            chromosome[pos] = '0'

    mutant_chromosomes = list(map(mutation2, chromosomes))
    return mutant_chromosomes

def main():
    fitness_function = lambda x : x^2 - 3*x + 4
    better_function = lambda x,y : x if x < y else y
    generation_limits = 5
    aux(-10, 10, 4, fitness_function, generation_limits, better_function)
    return

