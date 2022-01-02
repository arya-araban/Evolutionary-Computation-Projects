from nsga2.problem import Problem
from nsga2.evolution import Evolution
import matplotlib.pyplot as plt
import math
import numpy as np
from lib.objective_functions import *

problem = Problem(num_of_variables=50, objectives=[zdt6_f1, zdt6_f2], variables_range=[(0, 1)], same_range=True,
                  expand=False)
evo = Evolution(problem, mutation_param=20)
func = [i.objectives for i in evo.evolve()]

function1 = [i[0] for i in func]
function2 = [i[1] for i in func]
print(function1)
print(function2)
plt.xlabel('Function 1', fontsize=15)
plt.ylabel('Function 2', fontsize=15)
plt.scatter(function1, function2)
plt.show()
