import numpy as np
import matplotlib.pyplot as plt
import sys
path="D:\libsvm-3.22\python"
sys.path.append(path)
from svmutil import *

def  plot_boundary(model_file):
    a1 = np.linspace(-10, 10, 100)
    a2 = np.linspace(-10, 10, 100)
    raw_data = [(x1,x2)  for x1 in a1 for x2 in a2]
    raw_data=np.array(raw_data)
    Y = np.zeros(10000)
    X=[]
    X=[{1:data[0],2:data[1]} for data in raw_data]
    X1, Y1 = np.meshgrid(a1, a2)

    m = svm_load_model('model_file2.txt')
    p_labels, q, pre_vals = svm_predict(Y,X, m) #p_val= <class 'list'>
    print('p_labels=',p_labels)
    F=np.array(p_labels)
    F=F.reshape(np.shape(X1))

    plt.contour(X1, Y1, F)
    plt.xticks(())
    plt.yticks(())
    plt.show()