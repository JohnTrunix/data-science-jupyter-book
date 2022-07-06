#!/usr/bin/env python
# coding: utf-8

# # Density

# Density plots allow to visualize the distribution of a numeric variable for one or several groups. They are very well adapted for large dataset, as stated in data-to-viz.com. Note that 2 approaches exist to build them in python: the first one consists in computing a kernel density estimate, the second one in building a high resolution histogram.
# 
# [Source](https://www.python-graph-gallery.com/density-plot/)

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = sns.load_dataset('iris')
df.head()


# In[3]:


sns.kdeplot(df['sepal_width'])
plt.show()

