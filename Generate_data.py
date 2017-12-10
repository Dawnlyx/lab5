import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

random.seed(10)

a=random.normal(5,1,(100,1))
b=random.normal(-5,1,(100,1))

data1 = np.hstack((a, b))
data2 = np.hstack((b, a))
data3 = np.hstack((a, -b))
data4 = np.hstack((b,-a))
label1 = np.ones((200, 1))
label2 = np.zeros((200, 1))
data = np.vstack((data1, data2, data3, data4))
label = np.vstack((label1, label2))
dataset=np.hstack((label,data))
random.shuffle(dataset)
print(len(dataset))

with open("dataset1.txt",'w') as f:
    for data in dataset:
        newline=str(data[0])+'\t'+'1:'+str(data[1])+'\t'+'2:'+str(data[2])+'\n'
        f.write(newline)


plt.figure("fig7 ")
plt.plot(a,b,"c.",b,a,"c.",a,-b,"r.",b,-a,"r.")
plt.savefig('fig7.png')
plt.show()
