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


def zdt2_f1(x):  # bound [0,1]
    return x[0]


def zdt2_f2(x):
    g = 1 + 9 * (np.sum(x[1:])) / (len(x) - 1)
    f = g * (1 - (math.sqrt(x[0] / g)) ** 2)
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
    f = g * (1 - math.sqrt(x[0] / g))
    return f


def zdt6_f1(x):  # bound [0,1]
    f = 1 - math.exp(-4 * x[0]) * math.sin(6 * math.pi * x[0]) ** 6
    return f


def zdt6_f2(x):
    g = 1 + 9 * (np.sum(x[1:]) / (len(x) - 1)) ** 0.25
    f = g * (1 - (zdt6_f1(x) / g) ** 2)
    return f

#
# funcs = {
#     1: {'function_name': f1, 'bounds': [-100, 100]},
#     2: {'function_name': f2, 'bounds': [-10, 10]},
#     3: {'function_name': f3, 'bounds': [-100, 100]},
#     4: {'function_name': f4, 'bounds': [-100, 100]},
#     5: {'function_name': f5, 'bounds': [-30, 30]},
#     6: {'function_name': f6, 'bounds': [-100, 100]},
#     7: {'function_name': f7, 'bounds': [-1.28, 1.28]},
#     8: {'function_name': f8, 'bounds': [-500, 500]},
#     9: {'function_name': f9, 'bounds': [-5.12, 5.12]},
#     10: {'function_name': f10, 'bounds': [-32, 32]},
#     11: {'function_name': f11, 'bounds': [-600, 600]},
# }
