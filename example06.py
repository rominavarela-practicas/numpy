import numpy as np

def map(x, func):
    numel = len(x)
    y = np.zeros( numel )
    for i in xrange(0, numel):
        y[i] = func( x[i])
    return y

x = [1,2,3,4,5]
func = lambda x: x**2
print map(x,func)
