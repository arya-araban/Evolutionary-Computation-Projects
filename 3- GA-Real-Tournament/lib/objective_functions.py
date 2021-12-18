import math
import random

import numpy as np


def f1(v):
    total = 0
    for i in range(len(v)):
        xi = v[i] ** 2
        total = total + xi
    return np.abs(total)


def f2(v):
    return np.sum(np.abs(v)) + np.prod(np.abs(v))


def f3(v):
    total = 0
    for i in range(len(v)):
        total = total + (np.sum(v[:(i+1)]) ** 2)
    return total


def f4(v):
    return np.max(np.abs(v))


def f5(v):
    ### ROSENBROCK ###
    total = 0
    for i in range(len(v) - 1):
        xi = v[i]
        x_next = v[i + 1]
        new = 100 * (x_next - xi ** 2) ** 2 + (xi - 1) ** 2
        total = total + new
    return total


def f6(v):
    total = 0
    for i in range(len(v)):
        total = total + ((v[i] + 0.5) ** 2)
    return total


def f7(v):
    total = 0
    for i in range(len(v)):
        total = total + (i+1) * (v[i] ** 4) + random.uniform(0, 1)
    return total


def f8(v):
    total = 0
    for i in range(len(v)):
        total = total - (v[i] * math.sin(math.sqrt(np.abs(v[i]))))
    return total


def f9(v):
    total = 0
    for i in range(len(v)):
        total = total + ((v[i] ** 2) - (10 * math.cos(2 * math.pi * v[i])) + 10)
    return total


def f10(v):
    ttl1 = 0
    ttl2 = 0
    for i in range(len(v)):
        ttl1 = ttl1 + (v[i] ** 2)
        ttl2 = ttl2 * math.cos(2 * math.pi * v[i])

    total = -20 * math.exp(-0.2 * math.sqrt(ttl1)) - math.exp((1 / len(v)) * ttl2) + 20 + math.e
    return total


def f11(v):
    ttl1 = 0
    ttl2 = 0
    for i in range(len(v)):
        ttl1 = ttl1 + (v[i] ** 2)
        ttl2 = ttl2 * math.cos(v[i] / math.sqrt(i+1))
    total = (1 / 4000) * ttl1 - ttl2 + 1
    return total



funcs = {
    1: {'function_name': f1, 'bounds': [-100, 100]},
    2: {'function_name': f2, 'bounds': [-10, 10]},
    3: {'function_name': f3, 'bounds': [-100, 100]},
    4: {'function_name': f4, 'bounds': [-100, 100]},
    5: {'function_name': f5, 'bounds': [-30, 30]},
    6: {'function_name': f6, 'bounds': [-100, 100]},
    7: {'function_name': f7, 'bounds': [-1.28, 1.28]},
    8: {'function_name': f8, 'bounds': [-500, 500]},
    9: {'function_name': f9, 'bounds': [-5.12, 5.12]},
    10: {'function_name': f10, 'bounds': [-32, 32]},
    11: {'function_name': f11, 'bounds': [-600, 600]},
}
