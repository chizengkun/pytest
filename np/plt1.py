import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi, 0.1)
y = np.sin(x)
y_= np.cos(x)

plt.plot(x,y)
plt.plot(x,y_)
plt.legend(['Sine','Coine'])
plt.show()