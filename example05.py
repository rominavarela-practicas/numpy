def sumatoria(x):
    y = 0;
    for i in xrange(1, x+1, 1):
        y += i
    return y

print sumatoria(5)
