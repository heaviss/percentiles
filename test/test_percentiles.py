from decimal import Decimal
from functools import partial

import numpy as np
import pytest

from percentiles import percentile


percentile_75 = partial(percentile, percent=75)


@pytest.mark.parametrize(
    "values, expected",
    (
        ([100, 200, 400], 300),
        ([1, 7, 5, 3], 5.5),
        ([1.1, 700.5, 2.3], 351.4),
        ((1.1, 700.5, 2.3), 351.4),  # tuple
        ({1.1, 700.5, 2.3}, 351.4),  # set
        ([1.1, 700.5, 2.3, 0.1, 4, 6, 90, 24, 33.45], 33.45),
        ([100], 100),
        ([100, 100], 100),
    ),
)
def test_75_percentile_function(values, expected):
    assert percentile_75(values) == expected


def test_percentile_takes_decimals():
    assert (
        percentile_75(
            [Decimal("1.1"), 700.5, 2.3],
        )
        == 351.4
    )


@pytest.mark.parametrize("value", (0.5, 142, -5, 0, 100))
def test_raises_when_percent_is_incorrect(value):
    with pytest.raises(ValueError):
        percentile([100], value)


def test_raises_value_error_on_empty_input():
    with pytest.raises(ValueError):
        percentile([], 5)


@pytest.mark.parametrize("percent", range(1, 100))
def test_returns_same_result_as_numpy(percent):
    sequence = [1.1, 700.5, 2.3, 0.1, 4, 6, 90, 24, 33.45]

    numpy_result = round(np.percentile(sequence, percent), 3)
    result = round(percentile(sequence, percent), 3)

    assert result == numpy_result
