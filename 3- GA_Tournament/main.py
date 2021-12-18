# genetic algorithm search for continuous function optimization
import random

from numpy.random import randint
from numpy.random import rand
from lib.objective_functions import funcs
import numpy as np


# decode bitstrings of one person in the population to numbers
def decode(bounds, n_bits, bitstrings):
    decoded = list()
    largest = 2 ** n_bits
    for bts in bitstrings:
        substring = bts
        # convert bitstring to a string of chars
        chars = ''.join([str(s) for s in substring])

        # convert string to integer
        integer = int(chars, 2)
        # scale integer to desired range
        value = bounds[0] + (integer / largest) * (bounds[1] - bounds[0])
        # store
        decoded.append(value)
    return decoded


# tournament selection
def tournament_selection(pop, scores, k=3):
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k - 1):
        # check if better (e.g. perform a tournament)
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    # print(pop[selection_ix])
    return pop[selection_ix]


# crossover two parents to create two children
def crossover(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()

    # check for recombination
    if rand() < r_cross:
        c1 = p1 + random.uniform(0, 1) * (p2 - p1)
        c2 = p2 + random.uniform(0, 1) * (p1 - p2)

    return [c1, c2]


# crossover two parents to create two children
def crossover1(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()

    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string

        for i in range(len(c1)):
            pt = randint(1, len(p1[0]) - 2)
            # perform crossover
            c1[i] = p1[i][:pt] + p2[i][pt:]
            c2[i] = p2[i][:pt] + p1[i][pt:]

    return [c1, c2]


# mutation operator
def mutation(child, r_mut, sigma=0.1):
    # check for a mutation
    if rand() < r_mut:
        return child + np.random.normal(loc=0.0, scale=sigma, size=len(child))


# mutation operator
def mutation1(bitstrings, r_mut):
    for bts in bitstrings:
        for i in range(len(bts)):
            # check for a mutation
            if rand() < r_mut:
                # flip the bit

                bts[i] = 1 - bts[i]


# genetic algorithm
def genetic_algorithm(objective, bounds, n_iter, n_pop, n_inside_parent, r_cross, r_mut, sigma_mut):
    # initial population of random numbers in bounds
    pop = [[randint(bounds[0], bounds[1]) for _ in range(n_inside_parent)] for _ in range(n_pop)]
    # keep track of best solution
    best, best_eval = 0, pop[0]
    # enumerate generations
    for gen in range(n_iter):
        # evaluate all candidates in the population
        scores = [objective(d) for d in pop]
        # check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
            # print(">%d, new best f(%s) = %f" % (gen, decoded[i], scores[i]))
        # select parents
        selected = [tournament_selection(pop, scores, k=3) for _ in range(n_pop)]
        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i + 1]
            # crossover and mutation
            for c in crossover(p1, p2, r_cross):
                # mutation
                chd = mutation(c, r_mut, sigma=sigma_mut)
                # store for next generation
                children.append(chd)
        # replace population
        pop = children
    return [best, best_eval]


def GA_main(population_size, n_inside_parent, p_crossover, p_mutation, sigma_mutation, func_num):
    # define the total iterations
    n_iter = 1000
    # bits per variable
    n_bits = 16
    # define the population size
    n_pop = population_size
    # crossover rate
    r_cross = p_crossover
    # mutation rate
    r_mut = p_mutation
    # perform the genetic algorithm search
    sigma_mut = sigma_mutation

    n_inside_parent = n_inside_parent

    objective_func = funcs[func_num]  # g1t objective function and bound pair from the funcs dictionary, can be 1 to 10

    best, score = genetic_algorithm(objective_func['function_name'], objective_func['bounds'], n_iter, n_pop,
                                    n_inside_parent, r_cross, r_mut, sigma_mut)
    # print('Done!')
    decoded = decode(objective_func['bounds'], n_bits, best)
    # print('f(%s) = %f' % (decoded, score))
    return decoded, score


def main():
    for i in range(10):
        print(f"FUNCTION {i + 1}")
        for j in [10, 30, 50]:
            print(f"N = {j}")
            sols = []
            obj = []
            for k in range(10):
                best_solution, objective_function_score = GA_main(population_size=250,
                                                                  n_inside_parent=j, p_crossover=0.5,
                                                                  p_mutation=0.1, func_num=i + 1)
                obj.append(objective_function_score)
                sols.append(best_solution)
            print(f"best_solution:\n {np.mean(sols, axis=0)}")
            print(f"objective_function:\n {np.mean(obj)}")
            print("------------")


if __name__ == '__main__':
    main()
