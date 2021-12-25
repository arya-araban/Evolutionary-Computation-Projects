import math
import random

import numpy as np


def f1(v):
    total = 0
    for i in range(len(v)):
        xi = v[i] ** 2
        total = total + xi
    return np.abs(total)

