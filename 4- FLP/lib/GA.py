# genetic algorithm search for continuous function optimization
import random
import numpy as np
from numpy.random import randint
from numpy.random import rand
from useful_funcs import remove_values_from_lists, swap_random


# genetic algorithm
def genetic_algorithm(objective, perm_max, n_iter, n_pop, n_inside_parent, r_cross, r_mut, sigma_mut):
    # initial population of random numbers in permutation
    pop = [np.random.permutation(n_pop) for _ in range(perm_max)]
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
            for c in _erx_crossover(p1, p2, r_cross):
                # mutation
                _swap_mutation(c, r_mut)
                # store for next generation

                children.append(c)
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


def _erx_crossover(p1, p2, r_cross):
    if np.random.rand() > r_cross:
        return [p1, p2]

    c1, c2 = [], []

    for idx, cur_child in enumerate([c1, c2]):
        neighbourhoods = _get_neighbourhoods(p1, p2)
        chosen = eval(f"p{idx + 1}[0]")
        cur_child.append(chosen)
        while len(cur_child) != len(p1):

            neighbourhoods = remove_values_from_lists(neighbourhoods, chosen)
            d = {x: len(neighbourhoods[x]) for x in neighbourhoods[chosen]}

            if bool(d):
                min_val = min(d.values())
                mn1 = list(filter(lambda x: d[x] == min_val, d))
                chosen = random.choice(mn1)
                cur_child.append(chosen)
            else:
                for num in p1:
                    if num not in cur_child:
                        cur_child.append(num)
    return [c1, c2]


# mutation operator
def _swap_mutation(child, r_mut):
    # check for a mutation
    if rand() < r_mut:
        swap_random(child)

    return child


def _get_neighbourhoods(list1, list2):
    """This function takes as input two parents which has only unique values 0 to N,
     and output the 2D neighbourhood list.  0's neighbours will be the first list,
      1's neighbours will be the second list, and so on...
    """
    N = len(list1)
    arr = [[] for _ in range(len(list1))]
    for i in range(N):
        idx1 = list1.index(i)
        idx2 = list2.index(i)

        arr[i].extend({list1[idx1 - 1], list1[(idx1 + 1) % N], list2[idx2 - 1], list2[(idx2 + 1) % N]})

    return arr
