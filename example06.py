import numpy as np

# return y = func applied to each element in x
def map(x, func):
    numel = len(x)
    y = np.zeros( numel )
    for i in xrange(0, numel):
        y[i] = func( x[i])
    return y

def power(x):
    return x**2
#
x = [1,2,3,4,5]
print map(x,power)
