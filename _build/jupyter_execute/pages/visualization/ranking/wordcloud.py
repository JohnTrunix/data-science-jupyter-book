#!/usr/bin/env python
# coding: utf-8

# # Word Cloud

# A word cloud (also called tag cloud or weighted list) is a visual representation of text data. Words are usually single words, and the importance of each is shown with font size or color.
# 
# [Source](https://www.python-graph-gallery.com/wordcloud/)

# In[9]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[10]:


text=("Python Python Python Matplotlib Seaborn Seaborn Seaborn Seaborn Pandas Pandas Pandas Numpy Numpy plt plt plt plt plt plt plt plt")


# In[11]:


wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)


# In[12]:


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

