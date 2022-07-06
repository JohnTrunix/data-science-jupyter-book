#!/usr/bin/env python
# coding: utf-8

# # Density

# Those chart types allow to visualize the combined distribution of two quantitative variables.
# 
# [Source](https://www.python-graph-gallery.com/2d-density-plot/)

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = sns.load_dataset('iris')
df.head()


# In[3]:


sns.kdeplot(x=df.sepal_width, y=df.sepal_length, cmap="Reds", shade=True, bw_adjust=0.5)
plt.show()

