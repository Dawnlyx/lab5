import matplotlib.pyplot as plt
import numpy as np
import math
# 生成双月
def point_sample(N,r,w,d):
    x_sample = []
    y_sample = []
    inner_r = r - (w/2)
    outer_r = r + (w/2)

    #point the area A
    while True:
        data_x_A = np.random.uniform(-outer_r,outer_r)
        data_y_A = np.random.uniform(0,outer_r)
        r_A = math.sqrt((data_x_A**2) + (data_y_A**2))
        if r_A >= inner_r and r_A <= outer_r:
            x_sample.append(data_x_A)
            y_sample.append(data_y_A)
            if len(x_sample) == N:
                break
            else:
                continue
        else:
            continue

    #point the area B
    while True:
        data_x_B = np.random.uniform(-outer_r + r,outer_r + r)
        data_y_B = np.random.uniform(-d - outer_r,-d)
        r_B = math.sqrt(((data_x_B - r)**2) + ((data_y_B + d)**2))
        if r_B >= inner_r and r_B <= outer_r:
            x_sample.append(data_x_B)
            y_sample.append(data_y_B)
            if len(x_sample) == 2 * N:
                break
            else:
                continue
        else:
            continue
    plt.figure(1)
    plt.plot(x_sample,y_sample,'b*')

    plt.show()

    data_xy = np.array([np.reshape(x_sample,len(x_sample)),np.reshape(y_sample,len(y_sample))]).transpose()

    return data_xy
