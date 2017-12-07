import numpy as np
import matplotlib.pyplot as plt

r = 2.0
center=[3.0,3.0]
np.random.seed(10)
fig = plt.figure("concentrics circles ")
axes = fig.add_subplot(111)
#axes.set_title("data")
theta = np.arange(0, 2 * np.pi, 0.03)[:,np.newaxis]

x = center[0] + r * np.cos(theta)
y = center[1] + r * np.sin(theta)
x1= center[0] + 2*r * np.cos(theta)
y1 = center[1] + 2*r * np.sin(theta)

n=np.shape(x)
x_data=np.zeros(n)
y_data=np.zeros(n)
x1_data=np.zeros(n)
y1_data=np.zeros(n)

for i,j in enumerate(x):
    x_data[i]=j+ np.random.normal(scale=0.5, size=1)#x_data[i] = j + np.random.uniform(0,0.5)
for i,j in enumerate(y):
    y_data[i]=j+ np.random.normal(scale=0.5, size=1)
for i,j in enumerate(x1):
    x1_data[i]=j+ np.random.normal(scale=0.5, size=1)
for i,j in enumerate(y1):
    y1_data[i]=j+ np.random.normal(scale=0.5, size=1)

plt.scatter(x_data, y_data,s=10,c="c")
plt.scatter(x1_data, y1_data,s=10,c="orange")
fig.savefig('result1.png')
axes.axis('equal')#绘制出的坐标系长宽不会压缩
plt.show()
