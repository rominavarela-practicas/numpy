from matplotlib import pyplot as plt
import numpy as np

PI = np.pi
x= np.linspace( -PI , PI , 256 , endpoint=True )
sin, cos = np.sin(x) , np.cos(x)
plt.plot( x , sin )
plt.plot( x , cos )
plt.show()
