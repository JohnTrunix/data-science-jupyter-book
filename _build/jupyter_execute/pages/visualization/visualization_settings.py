#!/usr/bin/env python
# coding: utf-8

# # Visualization Settings

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = sns.load_dataset('iris')
df.head()


# ## Visualization Frame

# ### Figure Size

# In[11]:


plt.figure(figsize=(14, 6))
sns.regplot(x=df["sepal_length"], y=df["sepal_width"], fit_reg=False)
plt.show()


# ### Grid

# In[17]:


plt.grid(color='r', linestyle='-', linewidth=1)


# In[19]:


#or
sns.set(style="darkgrid")
sns.regplot(x=df["sepal_length"], y=df["sepal_width"], fit_reg=False)
plt.show()


# ### Title

# In[6]:


sns.regplot(x=df["sepal_length"], y=df["sepal_width"], fit_reg=False)
plt.title("Iris Dataset")
plt.show()


# ### Axis Labels

# In[7]:


sns.regplot(x=df["sepal_length"], y=df["sepal_width"], fit_reg=False)
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()


# ### Legend

# In[8]:


plt.bar(df["species"].unique(), df["species"].value_counts())
plt.legend(["Species"])
plt.show()


# ## Color

# ### Single Color

# In[9]:


plt.bar(df["species"].unique(), df["species"].value_counts(), color="green")


# ### Color Palette

# In[10]:


# plot with colormap virdis
sns.barplot(x=df["species"].unique(), y=df["species"].value_counts(), palette="viridis")

