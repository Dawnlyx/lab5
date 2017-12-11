import numpy as np
import matplotlib.pyplot as plt
import sys
path="D:\libsvm-3.22\python"
sys.path.append(path)
from svmutil import *

a1 = np.linspace(-5, 5, 500)
a2 = np.linspace(-5, 5, 500)
raw_data = [(x1,x2)  for x1 in a1 for x2 in a2]
raw_data=np.array(raw_data)
Y = np.zeros(250000)
X=[]
X=[{1:data[0],2:data[1]} for data in raw_data]

m = svm_load_model('model_file1.txt')
p, q, pre_vals = svm_predict(Y,X, m) #p_val= <class 'list'>
pre_vals=np.array(pre_vals)
print('p_val=',pre_vals)

with open("model_file2.txt", 'r') as f:
    tmp=f.readlines()[5].strip()
    b=tmp.split()[1]
    b=float(b)
    print('b=',b)
n=np.shape(pre_vals)[0]

F=np.abs(pre_vals-b)
print('F=',F)
idx=[]
for i,f in enumerate(F):
    if f<0.001:
        idx.append(i)
        print('f=',f)
print('idx=',idx)