from functools import partial

import pytest

from src.percentiles import percentile


percentile_75 = partial(percentile, percent=0.75)


@pytest.mark.parametrize('values, expected', (
    ([100, 200, 400], 300),
    ([1, 7, 5, 3], 5.5),
    ([1.1, 700.5, 2.3], 351.4),
    ([1.1, 700.5, 2.3, 0.1], 176.85),
    ([100], 100),
    ([100, 100], 100),
))
def test_75_percentile_function(values, expected):

    assert percentile_75(values) == expected


def test_raises_when_percent_is_incorrect():
    with pytest.raises(ValueError):
        percentile([100], 142)


def test_raises_when_on_empty_input():
    with pytest.raises(ValueError):
        percentile([], 0.5)
