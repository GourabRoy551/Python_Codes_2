import numpy as np
import pandas as pd
import plotly as pl
import cufflinks as cf
import plotly.offline as po
import matplotlib.pyplot as plt

po.init_notebook_mode(connected=True)
cf.go_offline()

df = pd.DataFrame(np.random.rand(100, 5), columns=['a', 'b', 'c', 'd', 'e'])
df2 = pd.DataFrame({'x': ['a', 'b', 'c', 'd', 'e'], 'y': [1, 2, 3, 4, 5], 'z': [6, 7, 8, 4, 3]})
df.iplot(kind='scatter', x='a', y='b')
plt.show()
