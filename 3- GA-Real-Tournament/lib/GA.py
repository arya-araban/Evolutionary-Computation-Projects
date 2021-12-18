# genetic algorithm search for continuous function optimization
import random
import numpy as np
from numpy.random import randint
from numpy.random import rand


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
        selected = [_tournament_selection(pop, scores, k=3) for _ in range(n_pop)]
        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i + 1]
            # crossover and mutation
            for c in _crossover(p1, p2, r_cross):
                # mutation

                chd = _mutation(c, r_mut, sigma_mut)
                # store for next generation

                children.append(chd)
        # replace population
        pop = children
    return [best, best_eval]


# tournament selection
def _tournament_selection(pop, scores, k=3):
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k - 1):
        # check if better (e.g. perform a tournament)
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    # print(pop[selection_ix])
    return pop[selection_ix]


# crossover two parents to create two children
def _crossover(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination
    if rand() < r_cross:
        c1 = (p1 + random.uniform(0, 1) * (np.subtract(p2, p1))).tolist()
        c2 = (p2 + random.uniform(0, 1) * (np.subtract(p1, p2))).tolist()

    return [c1, c2]


# mutation operator
def _mutation(child, r_mut, sigma_mut):
    # check for a mutation
    if rand() < r_mut:
        return child + np.random.normal(loc=0.0, scale=sigma_mut, size=len(child))

    return child
