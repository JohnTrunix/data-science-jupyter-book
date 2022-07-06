#!/usr/bin/env python
# coding: utf-8

# # Heatmap

# A heatmap is a graphical representation of data where each value of a matrix is represented as a color.
# 
# [Source](https://www.python-graph-gallery.com/heatmap/)

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


df = pd.DataFrame(np.random.random((5,5)), columns=["a","b","c","d","e"])
df.head()


# In[4]:


sns.heatmap(df, annot=True, annot_kws={"size": 10})
plt.show()

