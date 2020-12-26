import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
tips.head()

sns.countplot(x='day', data=tips)
plt.show()