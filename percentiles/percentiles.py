import math
from decimal import Decimal
from typing import Iterable


def percentile(numbers: Iterable[int | float | Decimal], percent: int) -> float:
    """
    Find the percentile of a list of values.
    Stolen from http://code.activestate.com/recipes/511478-finding-the-percentile-of-the-values/
    """
    if not numbers:
        raise ValueError("N must be non-empty iterable")

    if not (0 < percent < 100 and isinstance(percent, int)):
        raise ValueError("percent parameter must be integer from 0 to 100")

    numbers = sorted(numbers)

    k = (len(numbers) - 1) * percent / 100
    prev_index = math.floor(k)
    next_index = math.ceil(k)

    if prev_index == next_index:
        return float(numbers[int(k)])

    d0 = float(numbers[prev_index]) * (next_index - k)
    d1 = float(numbers[next_index]) * (k - prev_index)

    return d0 + d1
