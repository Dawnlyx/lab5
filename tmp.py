
import numpy as np
import matplotlib.pyplot as plt
a = 0.0
r = 2.0
center=[3.0,3.0]
while a < 2*np.pi:        #画一个360度的圆
    x = center[0]+r*np.sin(a)+np.random.normal(scale=0.3, size=1)
    y = center[1]+r*np.cos(a)+np.random.normal(scale=0.3, size=1)
    a += 0.01#range()步长只能为整数
    plt.plot(x,y,"k.")
plt.show()