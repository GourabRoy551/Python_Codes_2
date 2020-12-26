import numpy as np
import seaborn as sns
import pandas as pd

df1 = sns.load_dataset('tips')
df2 = pd.read_csv('ece.csv')

x1 = np.random.rand(100, 5)
x2 = np.random.rand(10, 5)

df3 = pd.DataFrame(x1, columns=['a', 'b', 'c', 'd', 'e'])
df4 = pd.DataFrame(x2, columns=['a', 'b', 'c', 'd', 'e'])

print(df3)
print(df4)