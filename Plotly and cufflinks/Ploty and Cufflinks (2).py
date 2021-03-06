#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import plotly as pl
import cufflinks as cf
import plotly.offline as po
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


po.init_notebook_mode(connected=True)


# In[4]:


cf.go_offline()


# In[5]:


df = pd.DataFrame(np.random.rand(100, 5), columns=['a', 'b', 'c', 'd', 'e'])


# In[6]:


df2 = pd.DataFrame({'x': [3,4,7,8,12], 'y': [1, 2, 3, 4, 5], 'z': [6, 7, 8, 4, 3]})


# In[9]:


df.iplot(kind='scatter', x='a', y='b', mode='markers', size=7, symbol='x', colorscale='paired')


# In[12]:


cf.datagen.sinwave(10,.25).iplot(kind='surface', theme='solar',colorscale='brbg', margin=(0,0,0,0))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




