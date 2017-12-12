import sys
path="D:\libsvm-3.22\python"
sys.path.append(path)
from svmutil import *
from Generate_data import *
from plot_boundary import *

def main(type):
    if type==1:
        datafile=generate_data()
        interval=[-10,10]
    elif type==2:
        datafile = generate_circle()
        interval=[-5,5]
    else:
        print('wrong options!')

    y, x = svm_read_problem(datafile)  # 读入训练数据
    m = svm_train(y[:300], x[:300])  # 训练
    svm_save_model('model_file.txt', m)
    model_file='model_file.txt'
    p_label, p_acc, p_val = svm_predict(y, x, m)  # 测试

    X = []
    Xi = []
    for xi in x:
        Xi = [xi[1], xi[2]]
        X += [Xi]
    idx1=[i for i in range(len(y)) if p_label[i]==1]
    idx2=[i for i in range(len(y)) if p_label[i]==0]
    class1=[X[i] for i in idx1]
    #print('class1=',class1[0])
    class2=[X[i] for i in idx2]
    c1_x1=[x[0] for x in class1]
    c1_x2=[x[1] for x in class1]
    c2_x1 = [x[0] for x in class2]
    c2_x2 = [x[1] for x in class2]
    #print('c1_x1=',c1_x1)
    #绘制预测结果
    plt.figure("classification ")
    plt.plot(c1_x1, c1_x2, "c.",c2_x1, c2_x2, "r.")
    plt.savefig('classification.png')

    plot_boundary(interval,100,model_file)
    plt.show()
if __name__ == '__main__':
    main(2)

