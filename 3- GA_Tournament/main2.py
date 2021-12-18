import numpy as np
from geneticalgorithm import geneticalgorithm as ga

from lib.objective_functions import funcs


def GA_main2(population_size, n_inside_parent, p_crossover, p_mutation, func_num):
    objective_func = funcs[func_num]

    varbound = np.array([objective_func['bounds']] * n_inside_parent)
    crossover_probability = 0.5

    algorithm_param = {'max_num_iteration': 1000,
                       'population_size': population_size,
                       'mutation_probability': p_mutation,
                       'elit_ratio': 0.01,
                       'crossover_probability': p_crossover,
                       'parents_portion': 0.3,
                       'crossover_type': 'uniform',
                       'max_iteration_without_improv': None}

    model = ga(function=objective_func['function_name'],
               dimension=n_inside_parent,
               variable_type='real',
               variable_boundaries=varbound,
               algorithm_parameters=algorithm_param)
    return model


def main():
    for j in range(10):
        print(f"FUNCTION {j + 1}")
        for i in [10, 30, 50]:
            print(f"N = {i}")
            model = GA_main2(population_size=250, n_inside_parent=i, p_crossover=0.5,
                             p_mutation=0.1, func_num=j + 1)
            model.run()
        print("------------")


if __name__ == '__main__':
    main()
