import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')
print(tips.head())

sns.residplot(x='total_bill', y='tip', data=tips, lowess=False)
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')

plt.show()
