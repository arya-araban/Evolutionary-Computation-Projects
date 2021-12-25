import random
from itertools import islice
import numpy as np


def read_lines_into_arr(file_name, line_begin, line_end):
    with open(f"../{file_name}") as lines:
        array = np.genfromtxt(islice(lines, line_begin - 1, line_end))
        return array


def remove_values_from_lists(lists, val):
    # this function removes values from list of lists, and also returns the index list
    return [[value for value in i if value != val] for i in lists]


def swap_random(seq):
    # swap two random numbers in array
    idx = range(len(seq))
    i1, i2 = random.sample(idx, 2)
    seq[i1], seq[i2] = seq[i2], seq[i1]
