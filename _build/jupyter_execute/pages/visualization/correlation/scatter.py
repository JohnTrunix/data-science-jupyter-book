#!/usr/bin/env python
# coding: utf-8

# # Scatterplot

# A scatter plot displays the relationship between 2 numeric variables. Each data point is represented as a circle.
# 
# [Source](https://www.python-graph-gallery.com/scatter-plot/)

# In[9]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[10]:


df = sns.load_dataset('iris')
df.head()


# In[11]:


sns.regplot(x=df["sepal_length"], y=df["sepal_width"], fit_reg=False)
plt.show()

