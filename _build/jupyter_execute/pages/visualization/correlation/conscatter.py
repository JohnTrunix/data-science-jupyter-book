#!/usr/bin/env python
# coding: utf-8

# # Connected Scatterplot

# A connected scatterplot is a line chart where each data point is shown by a circle or any type of marker.
# 
# [Source](https://www.python-graph-gallery.com/connected-scatter-plot/)

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[3]:


df = pd.DataFrame({
    'x': range(1,10),
    'y': np.random.randn(9)
})
df.head()


# In[4]:


plt.plot(df['x'], df['y'], linestyle='-', marker='o')
plt.show()

