# Evolutionary-Computation-Projects
The projects/homework completed for the Evolutionary Computation course of Fall 2021 @ FUM 

## Project 1

Implementation of the three main algorithms for Evolution Strategies. The [Rosenbrock](https://en.wikipedia.org/wiki/Rosenbrock_function) benchmark function has been used to test each of the methods.

**Classic ES:**  In each generation the population size is always equal to only one. If the child scores better than its parent in a certain generation, then it'll be selected as the parent for the next generation.

 **ES(μ, λ):** In each generation we select μ best parents, and λ is the size of the population.In this version of ES, each selected parent has λ\μ children, which these children becomes the population for the next generation.

 **ES(μ + λ):** This method is similar to ES(μ, λ), with the only difference being that for the next generation, the population is chosen between the children AND their parents.

## Project 2 
 
### Task 1 
Implementation Of a simple GA, and making use of that GA in order to try to find the minimum of multiple test functions.

### Task 2 
Using GA in order to solve a problem which might occur in the real world. The proposed problem to solve is the [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)


## Project 3

