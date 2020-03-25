import math
from typing import Iterable


def percentile(N: Iterable, percent: int):
    """
    Find the percentile of a list of values.
    Stolen from http://code.activestate.com/recipes/511478-finding-the-percentile-of-the-values/
    """
    if not N:
        raise ValueError('N must be non-empty iterable')

    if not (0 < percent < 100 and type(percent) == int):
        raise ValueError('percent parameter must be integer from 0 to 100')

    N = sorted(N)

    k = (len(N) - 1) * percent / 100
    prev_index = math.floor(k)
    next_index = math.ceil(k)

    if prev_index == next_index:
        return N[int(k)]

    d0 = N[prev_index] * (next_index - k)
    d1 = N[next_index] * (k - prev_index)

    return d0 + d1
