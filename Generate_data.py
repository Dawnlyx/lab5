import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

random.seed(10)

a=random.normal(5,1,(100,1))
b=random.normal(-5,1,(100,1))

plt.plot(a,b,"c.",b,a,"c.",a,-b,"r.",b,-a,"r.")
plt.show()
