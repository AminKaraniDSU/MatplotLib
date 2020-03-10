from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0,10,10)
y = np.linspace(0,10,10)
plt.plot(x,y,marker='*',markeredgecolor='r',markerfacecolor='g',markersize=25,ls='-',url='www.fb.com')
plt.title("First Plot")
plt.xlabel('X-Axis')
plt.ylabel('y-Axis')
plt.show()