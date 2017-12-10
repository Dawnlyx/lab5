import sys
path="D:\libsvm-3.22\python"
sys.path.append(path)

from svmutil import *
y,x=svm_read_problem('dataset2.txt')
m = svm_train(y[:200], x[:200])
svm_save_model('model_file2.txt', m)

p_label, p_acc, p_val = svm_predict(y[200:], x[200:], m)