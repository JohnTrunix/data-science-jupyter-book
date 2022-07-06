#!/usr/bin/env python
# coding: utf-8

# # Horizontal Barplot

# Barplots are useful to represent the relationship between a categorical and a numerical variable.
# 
# [Source](https://www.python-graph-gallery.com/basic-barplot-with-seaborn)

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = sns.load_dataset('tips')
df.head()


# In[4]:


sns.barplot(x='total_bill', y='day', data=df, estimator=sum, ci=None)
plt.show()

