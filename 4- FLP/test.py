from itertools import islice
import numpy as np
import random
from lib.useful_funcs import remove_values_from_lists, read_lines_into_arr


def get_neighbourhoods(list1, list2):
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


def _crossover(p1, p2, r_cross):
    if np.random.rand() > r_cross:
        return [p1, p2]

    c1, c2 = [], []

    for idx, cur_child in enumerate([c1, c2]):
        neighbourhoods = get_neighbourhoods(p1, p2)
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


# print(_crossover([0, 1, 5, 4, 3, 6, 2],
#                  [6, 5, 0, 1, 2, 3, 4],
#                  1))


def f1(v, distance_matrix, flow_matrix):
    matrices_size = distance_matrix.shape[0]
    fitness_sum = 0
    for x in range(matrices_size):
        for y in range(matrices_size):
            fitness_sum += distance_matrix[x, y] * flow_matrix[v[x], v[y]]
            print(fitness_sum)
    return fitness_sum


v = np.random.permutation(25)
f1(v, read_lines_into_arr("nug25.dat", 3, 27), read_lines_into_arr("nug25.dat", 29, 53))
