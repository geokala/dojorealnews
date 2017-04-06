import matplotlib.pyplot as plt
import numpy as np


def prove(title, source, sentiment, categories=[]):
    with plt.xkcd():
        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        ax.bar(range(len(categories)), [1-sentiment, sentiment], 0.25)
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.set_xticks([0, 1])
        ax.set_xlim([-0.5, 1.5])
        #ax.set_ylim([0, 110])
        ax.set_xticklabels(categories)
        plt.yticks([])

        plt.title(title)

        fig.text(0.5, 0.05, source, ha='center')

    plt.show()

prove("Immigrants are stealing your jobs.", "OECD", .2, categories=["jobs before", "jobs after"])
