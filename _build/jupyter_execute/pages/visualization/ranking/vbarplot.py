#!/usr/bin/env python
# coding: utf-8

# # Vertical Barplot

# A barplot shows the relationship between a numeric and a categoric variable. Each entity of the categoric variable is represented as a bar. The size of the bar represents its numeric value. 
# 
# [Source](https://www.python-graph-gallery.com/barplot/)

# In[4]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


df = sns.load_dataset('tips')
df.head()


# In[7]:


sns.barplot(x='day', y='total_bill', data=df, estimator=sum, ci=None)
plt.show()

