#!/usr/bin/env python
# coding: utf-8

# # Lollipop

# A lollipop chart is an alernative to the more usual barplot. Python allows to build lollipops thanks to the matplotlib library, as shown in the examples below. The strategy here is to use the stem() function or to hack the vline() function depending on your input format.
# 
# [Source](https://www.python-graph-gallery.com/lollipop-plot/)

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = sns.load_dataset('tips')
df.head()


# In[10]:


ordered_df = df.sort_values(by='total_bill').iloc[::10, :]
ordered_df.head()


# In[13]:


plt.figure(figsize=(16, 4))
plt.stem(ordered_df['total_bill'])
plt.xticks(range(len(ordered_df)), ordered_df['total_bill'])
plt.show()

