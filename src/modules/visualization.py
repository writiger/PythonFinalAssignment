import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def vis():
    x = 0.5 + np.arange(8)
    y = np.random.uniform(2, 7, len(x))

    fig, axes = plt.subplots(1, 2, figsize=(16, 5))
    ax1 = axes[0]
    ax2 = axes[1]

    ax1.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
    ax1.bar(x, y, width=1)
    ax2.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
    ax2.barh(x, y, height=1, edgecolor="white", linewidth=1)
    plt.show()