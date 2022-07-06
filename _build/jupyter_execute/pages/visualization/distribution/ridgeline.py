#!/usr/bin/env python
# coding: utf-8

# # Ridgeline

# A ridgeline summarizes the distribution of a numeric variable for several groups. Each group is represented as a density chart, each density chart overlapping each other to use space more efficiently.
# 
# [Source](https://www.python-graph-gallery.com/ridgeline/)

# In[1]:


from joypy import joyplot
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = sns.load_dataset('iris')
df.head()


# In[3]:


joyplot(df, by='species', column='sepal_length')
plt.show()

