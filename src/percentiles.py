import math
from typing import Callable, Iterable


def percentile(N: Iterable, percent: float, key: Callable = lambda x: x):
    """
    Find the percentile of a list of values.
    Stolen from http://code.activestate.com/recipes/511478-finding-the-percentile-of-the-values/
    """
    if not N:
        raise ValueError('N must be non-empty iterable')

    if not 0.0 < percent < 1:
        raise ValueError('percent parameter must be in from 0.0 to 1.0')

    N.sort()

    k = (len(N) - 1) * percent
    f = math.floor(k)
    c = math.ceil(k)

    if f == c:
        return key(N[int(k)])

    d0 = key(N[int(f)]) * (c - k)
    d1 = key(N[int(c)]) * (k - f)

    return d0 + d1