import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

random.seed(42)

# 产生2x5的标准正态分布样本
a=random.normal(5,1,(100,1))
b=random.normal(-5,1,(100,1))

plt.plot(a,b,"r.")
plt.plot(a,-b,"b.")
plt.plot(b,a,"g.")
plt.plot(b,-a,"y.")
#for x,y in a:
    #plt.plot(x,y,"r.")
#for x,y in b:
    #plt.plot(x,y,"b.")
plt.show()
