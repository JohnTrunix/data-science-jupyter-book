#!/usr/bin/env python
# coding: utf-8

# # Histogram

# A Histogram represents the distribution of a numeric variable for one or several groups. The values are split in bins, each bin is represented as a bar.
# 
# [Source](https://www.python-graph-gallery.com/histogram/)

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = sns.load_dataset('iris')
df.head()


# In[3]:


sns.histplot(x=df['sepal_length'], kde=True)
plt.show()

