import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

tips.head()
flights.head()

tip2 = tips.corr()
sns.heatmap(tip2, annot=True)
print(tip2)

flight2 = flights.pivot_table(index='month', columns='year', values='passengers')
print(flight2)
sns.heatmap(flight2, lw=1, cmap='cool')
plt.show()