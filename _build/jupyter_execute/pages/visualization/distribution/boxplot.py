#!/usr/bin/env python
# coding: utf-8

# # Boxplot

# A boxplot summarizes the distribution of a numeric variable for one or several groups. It allows to quickly get the median, quartiles and outliers but also hides the dataset individual data points. In python, boxplots are most of time done thanks to the boxplot function of the Seaborn library.
# 
# [Source](https://www.python-graph-gallery.com/boxplot/)

# In[4]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


df = sns.load_dataset('iris')
df.head()


# In[6]:


sns.boxplot(x=df["species"], y=df["sepal_length"])
plt.show()

