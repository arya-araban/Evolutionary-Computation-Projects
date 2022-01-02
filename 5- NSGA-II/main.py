from nsga2.problem import Problem
from nsga2.evolution import Evolution
import matplotlib.pyplot as plt
import math
import numpy as np
from lib.objective_functions import funcs, zdt4_f1
from lib.useful_funcs import individual_merge


def NSGA_II_main(func, N):
    if zdt4_f1 == func['f1']:
        bnds = [(-5, 5)] * N
        bnds[0] = (0, 1)
        problem = Problem(num_of_variables=N, objectives=[func['f1'], func['f2']], variables_range=bnds,
                          same_range=func['same_range'],
                          expand=func['expand'])
    else:
        problem = Problem(num_of_variables=N, objectives=[func['f1'], func['f2']], variables_range=func['bounds'],
                          same_range=func['same_range'],
                          expand=func['expand'])
    evo = Evolution(problem, mutation_param=20)
    func = [i.objectives for i in evo.evolve()]

    function1 = [i[0] for i in func]
    function2 = [i[1] for i in func]
    entire_func = individual_merge(function1, function2)
    print(entire_func)
    plt.title(f"N={N}")
    plt.xlabel('Function 1', fontsize=15)
    plt.ylabel('Function 2', fontsize=15)
    plt.scatter(function1, function2)
    plt.show()


def main():
    func_name = 'zdt4'

    print(f"** {func_name} **")

    NSGA_II_main(funcs[func_name], 30)


if __name__ == "__main__":
    main()
