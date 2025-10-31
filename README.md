# Find x-th percentile of a sequence without numpy 

[![codecov](https://codecov.io/gh/heaviss/percentiles/branch/master/graph/badge.svg)](https://codecov.io/gh/heaviss/percentiles)

Because sometimes you need one function only.

## Install
```
pip install percentiles
```

## Use
```pycon
>>> import percentiles
>>> percentiles.percentile([100, 120, 130, 1000], 75)
347.5
>>> from numpy import percentile
>>> percentile([100, 120, 130, 1000], 75)
347.5

```

## Credits

Original code was posted on http://code.activestate.com/recipes/511478-finding-the-percentile-of-the-values/