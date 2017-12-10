import sys
path="D:\libsvm-3.22\python"
sys.path.append(path)

#import os
#os.chdir('C:\libsvm-3.18\windows')#设定路径

from svmutil import *

y, x = svm_read_problem('dataset1.txt')#读入训练数据
#yt, xt = svm_read_problem('test1.txt')#训练测试数据
m = svm_train(y[:300], x[:300] )#训练
svm_save_model('model_file1.txt', m)
#svm_save_model('model_file', model)
#print('m=',m)
p_label, p_acc, p_val =svm_predict(y[300:],x[300:],m)#测试