#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Binomial Distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[78]:


pop1 = np.random.binomial(10, 0.2, 10000)
pop2 = np.random.binomial(10, 0.5, 10000)

df_origin = pd.DataFrame()
df_origin['pop1'] = pop1
df_origin['pop2'] = pop2
df_origin.describe()


# In[77]:


sample1 = np.random.choice(pop1, 100, replace=True)
sample2 = np.random.choice(pop2, 100, replace=True)


# In[10]:


sample1.mean()


# In[11]:


sample2.mean()


# In[12]:


sample1.std()


# In[13]:


sample2.std()


# In[14]:


df = pd.DataFrame()
df['Sample 1'] = sample1
df['Sample 2'] = sample2


# In[15]:


df.describe()


# In[17]:


sample1_1000 = np.random.choice(pop1, 1000, replace=True)
sample2_1000 = np.random.choice(pop2, 1000, replace=True)


# In[31]:


df_1000 = pd.DataFrame()

df_1000['Sample1_1000'] = sample1_1000
df_1000['Sample2_1000'] = sample2_1000
df_1000.describe()


# In[50]:


fig = plt.figure(figsize=(15, 8))


# In[56]:


plt.subplot(1, 2, 1)
plt.hist(sample1, alpha=0.5, label='Sample 1')
plt.hist(sample2, alpha=0.5, label='Sample 2')
plt.legend(loc='upper right')

plt.subplot(1, 2, 2)
plt.hist(sample1_1000, color='purple', alpha=0.5, label='Sample 1_1000')
plt.hist(sample2_1000, color='green', alpha=0.5, label='Sample 2_1000')
plt.legend(loc='upper right')

plt.show()


# In[57]:


sample1_20 = np.random.choice(pop1, 20, replace=True)
sample2_20 = np.random.choice(pop2, 20, replace=True)


# In[61]:


plt.figure(figsize=(30, 7))

plt.subplot(1, 3, 1)
plt.hist(sample1, alpha=0.5, label='Sample 1')
plt.hist(sample2, alpha=0.5, label='Sample 2')
plt.legend(loc='upper right')

plt.subplot(1, 3, 2)
plt.hist(sample1_1000, color='purple', alpha=0.5, label='Sample 1_1000')
plt.hist(sample2_1000, color='green', alpha=0.5, label='Sample 2_1000')
plt.legend(loc='upper right')

plt.subplot(1, 3, 3)
plt.hist(sample1_20, alpha=0.5, label='Sample 1_20')
plt.hist(sample2_20, alpha=0.5, label='Sample 2_20')
plt.legend(loc='upper right')
plt.show()


# In[62]:


pop1_new = np.random.binomial(10, 0.3, 10000)
pop2_new = np.random.binomial(10, 0.5, 10000)


# In[85]:


sample1_new = np.random.choice(pop1_new, 100, replace=True)
sample2_new = np.random.choice(pop2_new, 100, replace=True)

pop1_new2.mean()


# In[68]:


from scipy.stats import ttest_ind
print(ttest_ind(sample2_new, sample1_new, equal_var=False))


# In[74]:


pop1_new2 = np.random.binomial(10, 0.4, 10000)
pop2_new2 = np.random.binomial(10, 0.5, 10000)


# In[75]:


sample1_new2 = np.random.choice(pop1_new2, 100, replace=True)
sample2_new2 = np.random.choice(pop2_new2, 100, replace=True)


# In[76]:


from scipy.stats import ttest_ind
print(ttest_ind(sample2_new2, sample1_new2, equal_var=False))


# In[88]:


# Gamma Distribution
gpop1 = np.random.gamma(5, 1, 10000)
gpop2 = np.random.gamma(10, 1, 10000)

g_df = pd.DataFrame()
g_df['gpop1'] = gpop1
g_df['gpop2'] = gpop2
g_df.describe()


# In[89]:


gsample1 = np.random.choice(gpop1, 100, replace=True)
gsample2 = np.random.choice(gpop2, 100, replace=True)

gs_df = pd.DataFrame()
gs_df['gsample1'] = gsample1
gs_df['gsample2'] = gsample2
gs_df.describe()


# In[90]:


gsample3 = np.random.choice(gpop1, 1000, replace=True)
gsample4 = np.random.choice(gpop2, 1000, replace=True)

gs_df2 = pd.DataFrame()
gs_df2['gsample3'] = gsample3
gs_df2['gsample4'] = gsample4
gs_df2.describe()


# In[93]:


from scipy.stats import ttest_ind
print(ttest_ind(gsample4, gsample3, equal_var=False))


# In[94]:


from scipy.stats import ttest_ind
print(ttest_ind(gsample2, gsample1, equal_var=False))


# In[ ]:




