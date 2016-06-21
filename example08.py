import math
import sympy as sym

pi = sym.pi;
x = sym.Symbol('x');
y = sym.Symbol('y');
z = sym.Symbol('z');
fx = sym.cos(x) - x; # -x + cos(x)
gx = lambda x: math.cos(x) - x # gx(5) = -4.7163...
fxyz = sym.sympify('x*y*z') # x*y*z

# sustitucion
fx.subs( x , pi ) # -pi - 1
fx.subs( x , y**2 ) # -y**2 + cos(y**2)
fxyx.subs( [(x,2),(y,3),(z,4)] ) # 24

# primera derivada
orden = 1;
dx = sym.diff( fx , x , orden ); # -sin(x) - 1

# integral indefinida
sym.integrate( fx , x ) # -x**2/2 + sin(x)

# integral definida
sym.integrate( fx , ( x , 0 , pi ) ) # -pi**2/2
