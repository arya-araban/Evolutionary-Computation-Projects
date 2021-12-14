import numpy as np
from numpy.random import randn, rand, seed
import random


def es_comma(objective, bounds, n_iter, step_size, n_selected_parents, population_size, n_parent_size):
    best, best_eval = None, 1e+10
    # calculate the number of children per parent
    n_children = int(population_size / n_selected_parents)
    # initial population
    population = list()
    for _ in range(population_size):
        population.append([random.uniform(bounds[0], bounds[1]) for _ in range(n_parent_size)])

    # perform the search
    for epoch in range(n_iter):
        # evaluate fitness for the population
        scores = [objective(c) for c in population]
        # rank scores in ascending order
        ranks = np.argsort(np.argsort(scores))  # doing argsort twice, we get the rank array corresponding to OG array
        # select the indexes for the top mu ranked solutions
        selected_indexes = [i for i, _ in enumerate(ranks) if ranks[i] < n_selected_parents]
        # create children from parents
        children = list()
        for i in selected_indexes:
            # check if this parent is the best solution ever seen
            if scores[i] < best_eval:
                best, best_eval = population[i], scores[i]  # we just use this info and print it
                print(f'{epoch}, Best: f({best}) = {best_eval:.5f}')
            # create children for parent
            for _ in range(n_children):
                child = None
                while child is None or not _in_bounds(child, bounds):
                    child = population[i] + randn(n_parent_size) * step_size
                children.append(child)
        # replace population with children
        population = children
    return [best, best_eval]


def es_plus(objective, bounds, n_iter, step_size, n_selected_parents, population_size, n_parent_size):
    best, best_eval = None, 1e+10
    # calculate the number of children per parent
    n_children = int(population_size / n_selected_parents)
    # initial population
    population = list()
    for _ in range(population_size):
        population.append([random.uniform(bounds[0], bounds[1]) for _ in range(n_parent_size)])
    # perform the search
    for epoch in range(n_iter):
        # evaluate fitness for the population
        scores = [objective(c) for c in population]
        # rank scores in ascending order
        ranks = np.argsort(np.argsort(scores))
        # select the indexes for the top mu ranked solutions
        selected_indexes = [i for i, _ in enumerate(ranks) if ranks[i] < n_selected_parents]
        # create children from parents
        children = list()
        for i in selected_indexes:
            # check if this parent is the best solution ever seen
            if scores[i] < best_eval:
                best, best_eval = population[i], scores[i]
                print(f'{epoch}, Best: f({best}) = {best_eval:.5f}')
            # keep the parent
            children.append(population[i])  # parent is also a part of the children so that scoring happens!
            # create children for parent
            for _ in range(n_children):
                child = None
                while child is None or not _in_bounds(child, bounds):
                    child = population[i] + randn(n_parent_size) * step_size
                children.append(child)
        # replace population with children
        population = children
    return [best, best_eval]


def es_classic(objective, bounds, n_iter, step_size, n_parent_size):
    best_score = 1e+10
    success_rate = 0  # The ratio between successful mutations and total number of iterations

    best_values = None
    # initial values
    parent_values = ([random.uniform(bounds[0], bounds[1]) for _ in range(n_parent_size)])

    # perform the search
    for epoch in range(n_iter):
        # evaluate fitness for the population
        parent_score = objective(parent_values)

        # check if this parent is the best solution ever seen
        if parent_score < best_score:
            best_score = parent_score  # we just use this info and print it
            best_values = parent_values
            if len(best_values) <= 4:
                print(f'epoch {epoch} -- Best Values: {best_values} -- Best score:({best_score:.5f})')
            else:
                print(
                    f"epoch {epoch} -- Best Values: [{str(best_values[0:2]).strip('[]')}, ..., {str(best_values[2:4]).strip('[')} -- Best score:({best_score:.5f})")
        # create children for parent
        child_values = None
        while child_values is None or not _in_bounds(child_values, bounds):
            child_values = parent_values + randn(n_parent_size) * step_size

        if objective(child_values) < parent_score:
            parent_values = child_values
            success_rate = success_rate + 1
    success_rate = success_rate / n_iter

    return best_score, success_rate


def _in_bounds(point, bounds):
    # enumerate all dimensions of the point
    for xi in point:
        if xi < bounds[0] or xi > bounds[1]:
            return False
    return True
