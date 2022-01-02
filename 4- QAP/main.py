# genetic algorithm search for continuous function optimization
from lib.GA import genetic_algorithm
from lib.objective_function import obj_func


def GA_main(population_size, n_perm, p_crossover, p_mutation):
    # define the total iterations
    n_iter = 1000
    # define the population size
    n_pop = population_size
    # crossover rate
    r_cross = p_crossover
    # mutation rate
    r_mut = p_mutation

    best, score = genetic_algorithm(obj_func, n_perm, n_iter, n_pop, r_cross, r_mut)

    return best, score


def main():

    best_solution, objective_function_score = GA_main(population_size=370,
                                                      n_perm=25, p_crossover=0.7, p_mutation=0.1)
    print(f"best_solution:\n {best_solution}")
    print(f"objective_function:\n {objective_function_score}")
    print("------------")


if __name__ == '__main__':
    main()
