#!/usr/bin/env python
# coding: utf-8

# # Violin

# A violint plot allow to visualize the distribution of a numeric variable for one or several groups. Seaborn is particularly adapted to build it thanks to its violin() function. Violinplots deserve more attention compared to boxplots that can sometimes hide features of the data.
# 
# [Source](https://www.python-graph-gallery.com/violin-plot/)

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = sns.load_dataset('iris')
df.head()


# In[3]:


sns.violinplot(x=df['species'], y=df['sepal_length'])
plt.show()

