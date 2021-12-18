# genetic algorithm search for continuous function optimization
from lib.GA import genetic_algorithm
from lib.objective_functions import funcs


def GA_main(population_size, n_inside_parent, p_crossover, p_mutation, sigma_mutation, func_num):
    # define the total iterations
    n_iter = 1000
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
