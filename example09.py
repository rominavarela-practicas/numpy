import numpy as np
import sympy as sym
from matplotlib import pyplot as plt

pi = sym.pi;
x = sym.Symbol('x');

fx = x**2;
f = sym.lambdify(x, fx, "numpy") # <function numpy.<lambda>>

X = np.linspace(0,9,10); # [0,1,2...9]
Y = f(X) # [0,1,4...81]

# PLOT !
plt.plot( X , Y )
plt.show()
