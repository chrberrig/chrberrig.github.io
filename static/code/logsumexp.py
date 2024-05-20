import numpy as np

xs = np.array([1000, 1000, 1000])

# Calculating p values the naive way will cause an overflow for large values in xs
p = lambda xs: np.exp(xs)/np.sum(np.exp(xs))

# Note that according to the arguments, the mapping p should give equal probability measure to each of the entries (as they are equanl in size).

def logsumexp(x):
    c = x.max()
    return c + np.log(np.sum(np.exp(x - c)))

# These two will not cause overflow
print(np.exp(xs - logsumexp(xs)))
print(p(xs - max(xs)))

# This will cause an overflow
print(p(xs)) 

