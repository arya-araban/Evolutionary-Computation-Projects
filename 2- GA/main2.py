import numpy as np
from geneticalgorithm import geneticalgorithm as ga

from lib.objective_functions import funcs
from lib.useful_funcs import split_list


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


def GA_divide2(population_size, n_inside_parent, p_crossover, p_mutation, func_num):
    objective_func = funcs[func_num]

    splt = split_list(objective_func['bounds'])
    bounds1 = splt[0]
    bounds2 = splt[1]
    varbound1 = np.array([bounds1] * n_inside_parent)
    varbound2 = np.array([bounds2] * n_inside_parent)

    algorithm_param = {'max_num_iteration': 1000,
                       'population_size': population_size,
                       'mutation_probability': p_mutation,
                       'elit_ratio': 0.01,
                       'crossover_probability': p_crossover,
                       'parents_portion': 0.3,
                       'crossover_type': 'uniform',
                       'max_iteration_without_improv': None}

    model1 = ga(function=objective_func['function_name'],
                dimension=n_inside_parent,
                variable_type='real',
                variable_boundaries=varbound1,
                algorithm_parameters=algorithm_param)

    model2 = ga(function=objective_func['function_name'],
                dimension=n_inside_parent,
                variable_type='real',
                variable_boundaries=varbound2,
                algorithm_parameters=algorithm_param)
    return model1, model2


def main():
    for j in range(10):
        print(f"FUNCTION {j + 1}")
        for i in [10, 30, 50]:
            print(f"N = {i}")
            model = GA_main2(population_size=250, n_inside_parent=i, p_crossover=0.5,
                             p_mutation=0.1, func_num=j + 1)
            model.run()
        print("------------")


def divide_main():
    model1, model2 = GA_divide2(population_size=250, n_inside_parent=3, p_crossover=0.5,
                                p_mutation=0.1, func_num=1)
    model = GA_main2(population_size=250, n_inside_parent=3, p_crossover=0.5,
                     p_mutation=0.1, func_num=1)
    model1.run()
    print('------')
    model2.run()
    print('------')
    model.run()


if __name__ == '__main__':
    divide_main()
