import matplotlib.pyplot as pl
import numpy as np

x = np.arange(0,10,0.1)
a = np.cos(x)
b = np.sin(x)

pl.plot(x,a,'r')
pl.plot(x,b,'b')
pl.show()