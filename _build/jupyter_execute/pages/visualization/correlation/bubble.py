#!/usr/bin/env python
# coding: utf-8

# # Bubble

# A bubble plot is a scatterplot where the circle size is mapped to the value of a third numeric variable.
# 
# [Source](https://www.python-graph-gallery.com/bubble-plot/)

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = sns.load_dataset('iris')
df.head()


# In[3]:


sns.scatterplot(data=df, x='sepal_length', y='sepal_width', size='petal_length', hue='species', legend=False)
plt.show()

