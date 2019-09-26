#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[4]:


# Create the bin dividers
bins =[0, 80, 100]

# Create names for the two groups
status_names = ['Fail', 'Pass']


# In[5]:


# Display the new column for status
df['status']=pd.cut(df['grade'], bins, labels=status_names)
df.head()


# In[6]:


# View Counts by Bin
pd.value_counts(df['status'])


# In[ ]:




