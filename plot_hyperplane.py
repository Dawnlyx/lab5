import numpy as np
import matplotlib.pyplot as plt
import sys
path="D:\libsvm-3.22\python"
sys.path.append(path)

from svmutil import *
y,x=svm_read_problem('dataset2.txt')
m=svm_load_model('model_file2.txt')

with open("model_file2.txt", 'r') as f:
    tmp=f.readlines()[5].strip()
    b=tmp.split()[1]
    b=np.array(b)
    print('b=',b)

def plot_hyperplane(y,x,model):
    x1 = np.linspace(-10, 10, 100)
    x2 = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x1, x2)
    vals = np.zeros_like(X)

    for i in range(100):
        raw_data = np.vstack((vals[:,i],X[:, i], Y[:, i])).T
        #print(raw_data)
        with open("testset.txt", 'w') as f:
            for data in raw_data:
                newline = str(data[0]) + '\t' + '1:' + str(data[1]) + '\t' + '2:' + str(data[2]) + '\n'
                f.write(newline)
        y_l, x_l = svm_read_problem('testset.txt')
        a,b,pre_vals = svm_predict(y_l, x_l, m)
       # for value in pre_vals:
           # print(np.array(value))
           # if np.abs(np.array(value)-b)<0.0001:
              #  idx=np.argwhere(pre_vals)
            #print(x_l[idx])



    #plt.contour(X, Y, vals)

    plt.xticks(())
    plt.yticks(())
    plt.show()



plot_hyperplane(x,y,m)

