# Evolutionary-Computation-Projects
The projects/homework completed for the Evolutionary Computation course of Fall 2021 @ FUM

Each of the projects contain a document detailing the methods used to reach a solution 

## Project 1

Implementation of the three main algorithms for Evolution Strategies. The [Rosenbrock](https://en.wikipedia.org/wiki/Rosenbrock_function) benchmark function has been used to test each of the methods.

**Classic ES:**  In each generation the population size is always equal to only one. If the child scores better than its parent in a certain generation, then it'll be selected as the parent for the next generation.

 **ES(μ, λ):** In each generation we select μ best parents, and λ is the size of the population.In this version of ES, each selected parent has λ\μ children, which these children becomes the population for the next generation.

 **ES(μ + λ):** This method is similar to ES(μ, λ), with the only difference being that for the next generation, the population is chosen between the children AND their parents.

## Project 2 
 
### Task 1 
Implementation of a simple GA with Binary Encoding and using Roulette wheel selection. After which, this GA is used in order to try to find the optimal (minimal) value of multiple test functions.

### Task 2 
Using GA in order to solve a problem which might occur in the real world. The proposed problem to solve is the [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)


## Project 3

Modifying the previous Implementation of GA so that it uses Real Encoding and [Tournament Selection](https://www.geeksforgeeks.org/tournament-selection-ga/). This new implementation is re-tested with the same test functions used in the previous project. 


## Project 4

Implementation of a solution to the [Quadratic assignment problem](https://en.wikipedia.org/wiki/Quadratic_assignment_problem) using GA. The encoding of the population for this problem is permutation based, and in order to keep permutations throughout GA opperations, Swap Mutation and [ERX Crossover](https://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/EdgeRecombinationCrossoverOperator.aspx) have been used 


## Project 5

Using the [NSGA-II](https://www.sciencedirect.com/science/article/pii/S1877705811022466) GA algorithm in order to find solutions to multiple objective problems. For each test, a pair of benchmark functions are specified for the algorithm to solve  
