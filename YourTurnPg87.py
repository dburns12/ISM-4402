#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


plt.scatter(df['hours'], df['grade'])


# In[ ]:


# There is a direct relationship with the amount of hours studied and the final grade amount.
# For the most part, the students who studied the longest made the highest grades.

