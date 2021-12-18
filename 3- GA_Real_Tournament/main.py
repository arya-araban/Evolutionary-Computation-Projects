# genetic algorithm search for continuous function optimization
import random

from numpy.random import randint
from numpy.random import rand
from lib.objective_functions import funcs
import numpy as np


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
        c1 = (p1 + random.uniform(0, 1) * (np.subtract(p2, p1))).tolist()
        c2 = (p2 + random.uniform(0, 1) * (np.subtract(p1, p2))).tolist()

    return [c1, c2]


# mutation operator
def mutation(child, r_mut, sigma_mut):
    # check for a mutation
    if rand() < r_mut:
        return child + np.random.normal(loc=0.0, scale=sigma_mut, size=len(child))

    return child


# genetic algorithm
def genetic_algorithm(objective, bounds, n_iter, n_pop, n_inside_parent, r_cross, r_mut, sigma_mut):
    # initial population of random numbers in bounds
    pop = [[randint(bounds[0], bounds[1]) for _ in range(n_inside_parent)] for _ in range(n_pop)]
    # keep track of best solution
    best, best_eval = 0, objective(pop[0])
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

                chd = mutation(c, r_mut, sigma_mut)
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
    # decoded = decode(objective_func['bounds'], n_bits, best)
    # print('f(%s) = %f' % (decoded, score))
    return best, score


def main():
    for i in range(10):
        print(f"FUNCTION {i + 1}")
        # for j in [10, 30, 50]:
        # print(f"N = {j}")

        best_solution, objective_function_score = GA_main(population_size=250,
                                                          n_inside_parent=20, p_crossover=0.5,
                                                          p_mutation=0.1, sigma_mutation=0.1, func_num=i + 1)

        print(f"best_solution:\n {best_solution}")
        print(f"objective_function:\n {objective_function_score}")
        print("------------")


if __name__ == '__main__':
    main()
