#!/usr/bin/env python
# coding: utf-8

# # Correlogram

# A correlogram or correlation matrix allows to analyse the relationship between each pair of numeric variables of a matrix. The correlation is visualised as a scatterplot. The diagonal represents the distribution of each variable with a histogram or a density plot.
# 
# [Source](https://www.python-graph-gallery.com/correlogram/)

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = sns.load_dataset('iris')
df.head()


# In[3]:


sns.pairplot(df)
plt.show()


# In[4]:


sns.pairplot(df, hue='species')
plt.show()

