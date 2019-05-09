#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This attemp is for Normal Distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


data1 = np.random.normal(50, 1, 100)


# In[29]:


plt.hist(data1, bins=20, color='r')
plt.show()


# In[30]:


plt.hist(data1, color='yellow', bins=20)
plt.axvline(data1.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(data1.mean()+data1.std(), color='b', linestyle='dashed',linewidth=2)
plt.axvline(data1.mean()-data1.std(), color='b', linestyle='dashed', linewidth=2)
plt.show()


# In[47]:


df = pd.DataFrame(data1)


# In[48]:


df.describe()


# In[33]:


##This attemp is for an additional task.
data2 = np.random.normal(5, 0.5, 100)
data3 = np.random.normal(10, 1, 100)


# In[44]:


fig = plt.figure(figsize=(15,6))

plt.subplot (1, 2, 1)
plt.hist(data2, bins=40, color='b')
plt.axvline(data2.mean(), color='r', linestyle='solid', linewidth='2')
plt.axvline(data2.mean()+data2.std(), color='r', linestyle='dashed', linewidth=2)
plt.axvline(data2.mean()-data2.std(), color='r', linestyle='dashed', linewidth=2)

plt.subplot (1, 2, 2)
plt.hist(data3, bins=40, color='r')
plt.axvline(data3.mean()+data3.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(data3.mean()-data3.std(), color='b', linestyle='dashed', linewidth=2)
plt.show()


# In[49]:


df['data2'] = pd.DataFrame(data2)
df['data3'] = pd.DataFrame(data3)


# In[52]:


df.columns = ['data1', 'data2', 'data3']


# In[56]:


df.describe()

