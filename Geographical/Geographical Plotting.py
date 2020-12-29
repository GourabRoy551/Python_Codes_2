#!/usr/bin/env python
# coding: utf-8

# In[1]:


import chart_studio.plotly as py
import plotly.graph_objs as go 
import pandas as pd


# In[2]:


from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot


# In[3]:


init_notebook_mode(connected = True) 


# In[4]:


data = dict(type = 'choropleth', 
  
            # location: Arizoana, California, Newyork 
            locations = ['AZ', 'CA', 'NY'], 
              
            # States of USA 
            locationmode = 'USA-states', 
              
            # colorscale can be added as per requirement 
            colorscale = 'Portland', 
              
            # text can be given anything you like 
            text = ['text 1', 'text 2', 'text 3'], 
            z = [1.0, 2.0, 3.0], 
            colorbar = {'title': 'Colorbar Title Goes Here'}) 
              
layout = dict(geo ={'scope': 'usa'})


# In[5]:


choromap = go.Figure(data = [data], layout = layout) 


# In[6]:


iplot(choromap)


# In[ ]:




