import math
import numpy as np


def kursawe_f1(x):
    s = 0
    for i in range(len(x) - 1):
        s += -10 * math.exp(-0.2 * math.sqrt(x[i] ** 2 + x[i + 1] ** 2))
    return s


def kursawe_f2(x):
    s = 0
    for i in range(len(x)):
        s += abs(x[i]) ** 0.8 + 5 * math.sin(x[i] ** 3)
    return s


def schaffer_f1(x):
    return x ** 2


def schaffer_f2(x):
    return (x - 2) ** 2


def zdt1_f1(x):  # bound [0,1]
    return x[0]


def zdt1_f2(x):
    g = 1 + 9 * (np.sum(x[1:])) / (len(x) - 1)
    f = g * (1 - (math.sqrt(x[0] / g)))
    return f


def zdt2_f1(x):  # bound [0,1]
    return x[0]


def zdt2_f2(x):
    g = 1 + 9 * (np.sum(x[1:])) / (len(x) - 1)
    f = g * (1 - (x[0] / g) ** 2)
    return f


def zdt3_f1(x):  # bound [0,1]
    return x[0]


def zdt3_f2(x):
    g = 1 + 9 / (len(x) - 1) * np.sum(x[1:])
    f = g * (1 - (math.sqrt(x[0] / g)) - (x[0] / g) * (math.sin(10 * math.pi * x[0])))
    return f


def zdt4_f1(x):  # bound [0,1]
    return x[0]


def zdt4_f2(x):
    ttl = 0
    for i in range(1, len(x)):
        ttl += x[i] ** 2 - 10 * math.cos(4 * math.pi * x[i])

    g = 91 + ttl
    print(g)
    f = g * (1 - math.sqrt(x[0] / g))
    return f


def zdt6_f1(x):  # bound [0,1]
    f = 1 - math.exp(-4 * x[0]) * math.sin(6 * math.pi * x[0]) ** 6
    return f


def zdt6_f2(x):
    g = 1 + 9 * (np.sum(x[1:]) / (len(x) - 1)) ** 0.25
    f = g * (1 - (zdt6_f1(x) / g) ** 2)
    return f


_schaffer_A = 1000  # between 10 and 100K

funcs = {
    'kursawe': {'f1': kursawe_f1, 'f2': kursawe_f2, 'bounds': [(-5, 5)], 'same_range': True, 'expand': False},
    'schaffer': {'f1': schaffer_f1, 'f2': schaffer_f2, 'bounds': [(-_schaffer_A, _schaffer_A)], 'same_range': False,
                 'expand': True},
    'zdt1': {'f1': zdt1_f1, 'f2': zdt1_f2, 'bounds': [(0, 1)], 'same_range': True, 'expand': False},
    'zdt2': {'f1': zdt2_f1, 'f2': zdt2_f2, 'bounds': [(0, 1)], 'same_range': True, 'expand': False},
    'zdt3': {'f1': zdt3_f1, 'f2': zdt3_f2, 'bounds': [(0, 1)], 'same_range': True, 'expand': False},
    'zdt4': {'f1': zdt4_f1, 'f2': zdt4_f2, 'bounds': [(-5, 5)], 'same_range': False, 'expand': False},
    'zdt6': {'f1': zdt6_f1, 'f2': zdt6_f2, 'bounds': [(0, 1)], 'same_range': True, 'expand': False}
}
