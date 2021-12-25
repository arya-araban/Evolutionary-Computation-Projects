from lib.useful_funcs import read_lines_into_arr

distance_matrix = read_lines_into_arr("nug25.dat", 3, 27)
flow_matrix = read_lines_into_arr("nug25.dat", 29, 53)


def obj_func(v):
    matrices_size = distance_matrix.shape[0]
    fitness_sum = 0
    for x in range(matrices_size):
        for y in range(matrices_size):
            fitness_sum += distance_matrix[x, y] * flow_matrix[v[x], v[y]]

    return fitness_sum
