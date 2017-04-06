import matplotlib.pyplot as plt
import numpy as np
import random


sources = [
"""
Bonoli, G., 2003. Two Worlds of Pension Reform in Western Europe. Comparative Politics, Volume 35, pp. 399-416.
Coleman, D., The Political Economy of GlobalPopulation Change. Europe's Demographic Future: Determinants, Dimensions, and Challenges. Population and Development Review, Volume 32, p. 71.
""",
"""
Esping-Andersen, 2014. The Three Worlds of Welfare Capitalism. In: Welfare State Reader. s.l.:s.n., pp. 135-141.
OECD, 2014. [Online] 
Available at: https://data.oecd.org/pop/fertility-rates.htm
[Accessed 2017].
""",
"""
OECD, 2014. CO1.2: Life expectancy at birth. [Online] 
Available at: https://www.oecd.org/els/family/CO_1_2_Life_expectancy_at_birth.pdf
[Accessed 2017].
""",
"""
Trut, L., 1999. Early Canid Domestication: The Farm-Fox Experiment. [Online] 
Available at: https://www.americanscientist.org/issues/feature/1999/2/early-canid-domestication-the-farm-fox-experiment
[Accessed 2017].
""",
"""
Wolfgang Lutz, W. S. &. S. S., 2008. The coming acceleration of global population ageing. Nature, Volume 451, p. 716-719.
"""
,]

def prove(title, sentiment, categories=[]):
    with plt.xkcd():
        source = random.choice([
            "OECD 2016",
            "Fox News, Apr 1 2017",
            "HMRC",
            "Pravda",
            "Daily Mail Investigations",
            "World Bank, 2008",
            "xkcd",
        ])
        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        ax.bar(range(len(categories)), [sentiment, 1-sentiment], 0.25)
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
        fig.text(0.2, 0.05, random.choice(sources), ha='center')

    plt.show()

prove("Immigrants are stealing your jobs.", .2, categories=["jobs stolen before", "jobs stolen after"])

