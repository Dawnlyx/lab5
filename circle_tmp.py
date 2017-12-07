
import numpy as np
import matplotlib.pyplot as plt

r = 2.0
center=[3.0,3.0]
np.random.seed(10)
fig = plt.figure()
axes = fig.add_subplot(111)

theta = np.arange(0, 2 * np.pi, 0.03)[:,np.newaxis]
print("theta=",np.shape(theta))
x = center[0] + r * np.cos(theta)
y = center[1] + r * np.sin(theta)

n=np.shape(x)
x_data=np.zeros(n)
y_data=np.zeros(n)

for i,j in enumerate(x):
    #x_data[i]=j+ np.random.normal(scale=0.3, size=1)
    x_data[i] = j + np.random.uniform(0,0.5)
for i,j in enumerate(y):
    #y_data[i]=j+ np.random.normal(scale=0.3, size=1)
    y_data[i]=j+ np.random.uniform(0,0.5)
#plt.plot(x_data, y_data, "b.")
plt.scatter(x_data, y_data,s=9)
plt.savefig('result1.png')
axes.axis('equal')#绘制出的坐标系长宽不会压缩
plt.show()
