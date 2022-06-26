import matplotlib.pyplot as plt
import numpy as np
import random

plt.ion()  # 开启交互模式
plt.subplots()

for j in range(20):
    plt.clf()  # 清空画布
    plt.xlim(0, 10)  # 因为清空了画布，所以要重新设置坐标轴的范围
    plt.ylim(0, 10)

    x = [random.randint(1, 9) for i in range(10)]
    y = [random.randint(1, 9) for i in range(10)]

    plt.scatter(x, y)
    plt.pause(0.1)

plt.ioff()
plt.show()
