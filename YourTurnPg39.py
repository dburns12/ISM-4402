#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the gradedata csv file into the dataframe
import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[3]:


import numpy as np
df['timemgmt'] = np.where((df['exercise']>3) & (df['hours'] > 17), 'busy', 'normal') # Creating column to display if busy
df.tail(10)


# In[ ]:




