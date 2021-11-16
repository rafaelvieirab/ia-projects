import random
from utils import binary_to_decimal, decimal_to_binary


def _mix_chromosomes(byte1:str, byte2: str):
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

        must_be_crossed = random.random() < tax

        if must_be_crossed:
            (mixed1, mixed2) = _mix_chromosomes(chromosomes[c1], chromosomes[c2])
            crossed_chromosomes.append(mixed1)
            crossed_chromosomes.append(mixed2)
        else: 
            crossed_chromosomes.append(chromosomes[c1])
            crossed_chromosomes.append(chromosomes[c2])

    if len(selecteds) == 1:
        crossed_chromosomes.append(chromosomes[selecteds[0]])

    return crossed_chromosomes


def mutation(chromosomes: list, tax = 0.01) -> list:
    mutant_chromosomes = list(chromosomes)
    mutant_chromosomes = list(map(_mutation, mutant_chromosomes))
    return mutant_chromosomes


def _mutation(chromosome: str, tax = 0.01):
    must_be_changed = random.random() < tax

    if must_be_changed:
        pos = random.randint(1, len(chromosome) - 1)
        new_bit = ''
        if chromosome[pos] == '0':
            new_bit = '1'
        else:
            new_bit = '0'

        temp = chromosome[:pos] + new_bit + chromosome[pos+1:]
        temp_decimal = binary_to_decimal(temp)

        if temp_decimal >= -10 and temp_decimal <= 10:
            chromosome = temp
        else:
            chromosome = _mutation(chromosome)

    return chromosome

