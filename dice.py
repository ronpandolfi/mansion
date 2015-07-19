import numpy as np


def d6(size=None):
    roll = np.rand.randint(0, 6, size)
    return roll
