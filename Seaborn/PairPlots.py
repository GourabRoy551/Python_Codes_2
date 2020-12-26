import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dots = sns.load_dataset('dots')
print(dots.head())

# sns.pairplot(dots, hue='choice')

tips = sns.load_dataset('tips')
tips.head()

x = sns.pairplot(tips, hue='day')
x.map_diag(sns.displot)
plt.show()