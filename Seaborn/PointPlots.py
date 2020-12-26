import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


diamond = sns.load_dataset('diamonds')
print(diamond.head())

sns.displot(diamond['price'], kde=True)
plt.show()
