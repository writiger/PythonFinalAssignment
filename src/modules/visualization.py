import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def visualize(data):
    fig, axes = plt.subplots(6, 6, figsize=(18, 18))
    for i in range(1, 36):
        if data.visualData[i - 1][0][1] != '-':
            xList = list()
            yList = list()
            for item in data.visualData[i - 1]:
                xList.append(item[1])
                yList.append(item[0])
            x = np.asarray(xList)
            y = np.asarray(yList)
            plt.subplot(6, 6, i)
            plt.plot(x, y)
            plt.title("plot " + str(i))

    plt.suptitle("RUNOOB subplot Test")
    fig.tight_layout()
    plt.show()
